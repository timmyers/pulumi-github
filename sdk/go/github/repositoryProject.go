// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// This resource allows you to create and manage projects for GitHub repository.
type RepositoryProject struct {
	pulumi.CustomResourceState

	// The body of the project.
	Body pulumi.StringPtrOutput `pulumi:"body"`
	Etag pulumi.StringOutput    `pulumi:"etag"`
	// The name of the project.
	Name pulumi.StringOutput `pulumi:"name"`
	// The repository of the project.
	Repository pulumi.StringOutput `pulumi:"repository"`
	// URL of the project
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewRepositoryProject registers a new resource with the given unique name, arguments, and options.
func NewRepositoryProject(ctx *pulumi.Context,
	name string, args *RepositoryProjectArgs, opts ...pulumi.ResourceOption) (*RepositoryProject, error) {
	if args == nil || args.Repository == nil {
		return nil, errors.New("missing required argument 'Repository'")
	}
	if args == nil {
		args = &RepositoryProjectArgs{}
	}
	var resource RepositoryProject
	err := ctx.RegisterResource("github:index/repositoryProject:RepositoryProject", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRepositoryProject gets an existing RepositoryProject resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepositoryProject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RepositoryProjectState, opts ...pulumi.ResourceOption) (*RepositoryProject, error) {
	var resource RepositoryProject
	err := ctx.ReadResource("github:index/repositoryProject:RepositoryProject", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RepositoryProject resources.
type repositoryProjectState struct {
	// The body of the project.
	Body *string `pulumi:"body"`
	Etag *string `pulumi:"etag"`
	// The name of the project.
	Name *string `pulumi:"name"`
	// The repository of the project.
	Repository *string `pulumi:"repository"`
	// URL of the project
	Url *string `pulumi:"url"`
}

type RepositoryProjectState struct {
	// The body of the project.
	Body pulumi.StringPtrInput
	Etag pulumi.StringPtrInput
	// The name of the project.
	Name pulumi.StringPtrInput
	// The repository of the project.
	Repository pulumi.StringPtrInput
	// URL of the project
	Url pulumi.StringPtrInput
}

func (RepositoryProjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryProjectState)(nil)).Elem()
}

type repositoryProjectArgs struct {
	// The body of the project.
	Body *string `pulumi:"body"`
	// The name of the project.
	Name *string `pulumi:"name"`
	// The repository of the project.
	Repository string `pulumi:"repository"`
}

// The set of arguments for constructing a RepositoryProject resource.
type RepositoryProjectArgs struct {
	// The body of the project.
	Body pulumi.StringPtrInput
	// The name of the project.
	Name pulumi.StringPtrInput
	// The repository of the project.
	Repository pulumi.StringInput
}

func (RepositoryProjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryProjectArgs)(nil)).Elem()
}
