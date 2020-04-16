// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//nolint: goconst
package hcl2

import (
	"github.com/hashicorp/hcl/v2"
	"github.com/hashicorp/hcl/v2/hclsyntax"
	"github.com/pulumi/pulumi/pkg/v2/codegen"
	"github.com/pulumi/pulumi/pkg/v2/codegen/hcl2/model"
	"github.com/pulumi/pulumi/pkg/v2/codegen/hcl2/syntax"
	"github.com/pulumi/pulumi/pkg/v2/codegen/schema"
)

func getResourceToken(node *Resource) (string, hcl.Range) {
	return node.Syntax.Labels[1], node.Syntax.LabelRanges[1]
}

func (b *binder) bindResource(node *Resource) hcl.Diagnostics {
	return b.bindResourceBody(node)
}

// bindResourceTypes binds the input and output types for a resource.
func (b *binder) bindResourceTypes(node *Resource) hcl.Diagnostics {
	// Set the input and output types to dynamic by default.
	node.InputType, node.OutputType, node.VariableType = model.DynamicType, model.DynamicType, model.DynamicType

	// Find the resource's schema.
	token, tokenRange := getResourceToken(node)
	pkg, module, name, diagnostics := DecomposeToken(token, tokenRange)
	if diagnostics.HasErrors() {
		return diagnostics
	}

	isProvider := false
	if pkg == "pulumi" && module == "providers" {
		pkg, isProvider = name, true
	}

	pkgSchema, ok := b.packageSchemas[pkg]
	if !ok {
		return hcl.Diagnostics{unknownPackage(pkg, tokenRange)}
	}

	var inputProperties, properties []*schema.Property
	if !isProvider {
		res, ok := pkgSchema.resources[token]
		if !ok {
			canon := canonicalizeToken(token, pkgSchema.schema)
			if res, ok = pkgSchema.resources[canon]; ok {
				token = canon
			}
		}
		if !ok {
			return hcl.Diagnostics{unknownResourceType(token, tokenRange)}
		}
		inputProperties, properties = res.InputProperties, res.Properties
	} else {
		inputProperties, properties = pkgSchema.schema.Config, pkgSchema.schema.Config
	}
	node.Token = token

	// Create input and output types for the schema.
	inputType := model.InputType(schemaTypeToType(&schema.ObjectType{Properties: inputProperties}))

	outputProperties := map[string]model.Type{
		"id":  model.NewOutputType(model.StringType),
		"urn": model.NewOutputType(model.StringType),
	}
	for _, prop := range properties {
		outputProperties[prop.Name] = model.NewOutputType(schemaTypeToType(prop.Type))
	}
	outputType := model.NewObjectType(outputProperties)

	// TODO(pdg): properly handle eventually-typed range expressions. This requires binding in topological order, as
	// we need to know the type of the range expression here. It might be worth representing resources as function
	// calls rather than blocks simply to pick up the automatic handling of eventuals in the binder.
	variableType := model.Type(outputType)
	for _, block := range node.Syntax.Body.Blocks {
		if block.Type == "options" {
			if rng, hasRange := block.Body.Attributes["range"]; hasRange {
				node.rangeNode = rng.Expr
				variableType = model.NewListType(variableType)
				break
			}
		}
	}

	node.InputType, node.OutputType, node.VariableType = inputType, outputType, variableType
	return diagnostics
}

type resourceScopes struct {
	root      *model.Scope
	withRange *model.Scope
	resource  *Resource
}

func newResourceScopes(root *model.Scope, resource *Resource, rangeKey, rangeValue model.Type) model.Scopes {
	scopes := &resourceScopes{
		root:      root,
		withRange: root,
		resource:  resource,
	}
	if _, hasRange := resource.VariableType.(*model.ListType); hasRange {
		scopes.withRange = root.Push(syntax.None)
		scopes.withRange.Define("range", &model.Variable{
			Name: "range",
			VariableType: model.NewObjectType(map[string]model.Type{
				"key":   rangeKey,
				"value": rangeValue,
			}),
		})
	}
	return scopes
}

func (s *resourceScopes) GetScopesForBlock(block *hclsyntax.Block) (model.Scopes, hcl.Diagnostics) {
	if block.Type == "options" {
		return &optionsScopes{root: s.root, resource: s.resource}, nil
	}
	return model.StaticScope(s.withRange), nil
}

func (s *resourceScopes) GetScopeForAttribute(attr *hclsyntax.Attribute) (*model.Scope, hcl.Diagnostics) {
	return s.withRange, nil
}

type optionsScopes struct {
	root     *model.Scope
	resource *Resource
}

func (s *optionsScopes) GetScopesForBlock(block *hclsyntax.Block) (model.Scopes, hcl.Diagnostics) {
	return model.StaticScope(s.root), nil
}

func (s *optionsScopes) GetScopeForAttribute(attr *hclsyntax.Attribute) (*model.Scope, hcl.Diagnostics) {
	if attr.Name == "ignoreChanges" {
		obj, ok := s.resource.InputType.(*model.ObjectType)
		if !ok {
			return nil, nil
		}
		scope := model.NewRootScope(syntax.None)
		for k, t := range obj.Properties {
			scope.Define(k, &ResourceProperty{
				Path:         hcl.Traversal{hcl.TraverseRoot{Name: k}},
				PropertyType: t,
			})
		}
		return scope, nil
	}
	return s.root, nil
}

// bindResourceBody binds the body of a resource.
func (b *binder) bindResourceBody(node *Resource) hcl.Diagnostics {
	var diagnostics hcl.Diagnostics

	// If the resource has a range option, we need to know the type of the collection being ranged over. Pre-bind the
	// range expression now, but ignore the diagnostics.
	var rangeKey, rangeValue model.Type
	if node.rangeNode != nil {
		expr, _ := model.BindExpression(node.rangeNode, b.root, b.tokens)
		rangeKey, rangeValue, diagnostics = model.GetCollectionTypes(expr.Type(), node.rangeNode.Range())
	}

	// Bind the resource's body.
	block, blockDiags := model.BindBlock(node.Syntax, newResourceScopes(b.root, node, rangeKey, rangeValue), b.tokens)
	diagnostics = append(diagnostics, blockDiags...)

	var options *model.Block
	for _, item := range block.Body.Items {
		switch item := item.(type) {
		case *model.Attribute:
			node.Inputs = append(node.Inputs, item)
		case *model.Block:
			switch item.Type {
			case "options":
				if options != nil {
					diagnostics = append(diagnostics, duplicateBlock(item.Type, item.Syntax.TypeRange))
				} else {
					options = item
				}
			default:
				diagnostics = append(diagnostics, unsupportedBlock(item.Type, item.Syntax.TypeRange))
			}
		}
	}

	// Typecheck the attributes.
	if objectType, ok := node.InputType.(*model.ObjectType); ok {
		attrNames := codegen.StringSet{}
		for _, attr := range node.Inputs {
			attrNames.Add(attr.Name)

			if typ, ok := objectType.Properties[attr.Name]; ok {
				if !typ.ConversionFrom(attr.Value.Type()).Exists() {
					diagnostics = append(diagnostics, model.ExprNotConvertible(typ, attr.Value))
				}
			} else {
				diagnostics = append(diagnostics, unsupportedAttribute(attr.Name, attr.Syntax.NameRange))
			}
		}

		for _, k := range codegen.SortedKeys(objectType.Properties) {
			if !model.IsOptionalType(objectType.Properties[k]) && !attrNames.Has(k) {
				diagnostics = append(diagnostics, missingRequiredAttribute(k, node.Body.Syntax.MissingItemRange()))
			}
		}
	}

	// Typecheck the options block.
	if options != nil {
		resourceOptions := &ResourceOptions{}
		for _, item := range options.Body.Items {
			switch item := item.(type) {
			case *model.Attribute:
				var t model.Type
				switch item.Name {
				case "range":
					t = model.NewUnionType(model.NumberType, model.NewListType(model.DynamicType), model.NewMapType(model.DynamicType))
					resourceOptions.Range = item.Value
				case "provider":
					t = ResourceType
					resourceOptions.Provider = item.Value
				case "dependsOn":
					t = model.NewListType(model.DynamicType)
					resourceOptions.DependsOn = item.Value
				case "protect":
					t = model.BoolType
					resourceOptions.Protect = item.Value
				case "ignoreChanges":
					t = model.NewListType(ResourcePropertyType)
					resourceOptions.IgnoreChanges = item.Value
				default:
					diagnostics = append(diagnostics, unsupportedAttribute(item.Name, item.Syntax.NameRange))
					continue
				}
				if model.InputType(t).ConversionFrom(item.Value.Type()) == model.NoConversion {
					diagnostics = append(diagnostics, model.ExprNotConvertible(model.InputType(t), item.Value))
				}
			case *model.Block:
				diagnostics = append(diagnostics, unsupportedBlock(item.Type, item.Syntax.TypeRange))
			}
		}
		node.Options = resourceOptions
	}

	return diagnostics
}
