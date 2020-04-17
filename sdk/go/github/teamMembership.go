// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a GitHub team membership resource.
//
// This resource allows you to add/remove users from teams in your organization. When applied,
// the user will be added to the team. If the user hasn't accepted their invitation to the
// organization, they won't be part of the team until they do. When
// destroyed, the user will be removed from the team.
type TeamMembership struct {
	pulumi.CustomResourceState

	Etag pulumi.StringOutput `pulumi:"etag"`
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role pulumi.StringPtrOutput `pulumi:"role"`
	// The GitHub team id
	TeamId pulumi.StringOutput `pulumi:"teamId"`
	// The user to add to the team.
	Username pulumi.StringOutput `pulumi:"username"`
}

// NewTeamMembership registers a new resource with the given unique name, arguments, and options.
func NewTeamMembership(ctx *pulumi.Context,
	name string, args *TeamMembershipArgs, opts ...pulumi.ResourceOption) (*TeamMembership, error) {
	if args == nil || args.TeamId == nil {
		return nil, errors.New("missing required argument 'TeamId'")
	}
	if args == nil || args.Username == nil {
		return nil, errors.New("missing required argument 'Username'")
	}
	if args == nil {
		args = &TeamMembershipArgs{}
	}
	var resource TeamMembership
	err := ctx.RegisterResource("github:index/teamMembership:TeamMembership", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTeamMembership gets an existing TeamMembership resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeamMembership(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TeamMembershipState, opts ...pulumi.ResourceOption) (*TeamMembership, error) {
	var resource TeamMembership
	err := ctx.ReadResource("github:index/teamMembership:TeamMembership", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TeamMembership resources.
type teamMembershipState struct {
	Etag *string `pulumi:"etag"`
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role *string `pulumi:"role"`
	// The GitHub team id
	TeamId *string `pulumi:"teamId"`
	// The user to add to the team.
	Username *string `pulumi:"username"`
}

type TeamMembershipState struct {
	Etag pulumi.StringPtrInput
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role pulumi.StringPtrInput
	// The GitHub team id
	TeamId pulumi.StringPtrInput
	// The user to add to the team.
	Username pulumi.StringPtrInput
}

func (TeamMembershipState) ElementType() reflect.Type {
	return reflect.TypeOf((*teamMembershipState)(nil)).Elem()
}

type teamMembershipArgs struct {
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role *string `pulumi:"role"`
	// The GitHub team id
	TeamId string `pulumi:"teamId"`
	// The user to add to the team.
	Username string `pulumi:"username"`
}

// The set of arguments for constructing a TeamMembership resource.
type TeamMembershipArgs struct {
	// The role of the user within the team.
	// Must be one of `member` or `maintainer`. Defaults to `member`.
	Role pulumi.StringPtrInput
	// The GitHub team id
	TeamId pulumi.StringInput
	// The user to add to the team.
	Username pulumi.StringInput
}

func (TeamMembershipArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*teamMembershipArgs)(nil)).Elem()
}