// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Protects a GitHub branch.
 * 
 * This resource allows you to configure branch protection for repositories in your organization. When applied, the branch will be protected from forced pushes and deletion. Additional constraints, such as required status checks or restrictions on users, teams, and apps, can also be configured.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as github from "@pulumi/github";
 * 
 * const exampleTeam = new github.Team("example", {});
 * // Protect the master branch of the foo repository. Additionally, require that
 * // the "ci/travis" context to be passing and only allow the engineers team merge
 * // to the branch.
 * const exampleBranchProtection = new github.BranchProtection("example", {
 *     branch: "master",
 *     enforceAdmins: true,
 *     repository: github_repository_example.name,
 *     requiredPullRequestReviews: {
 *         dismissStaleReviews: true,
 *         dismissalTeams: [
 *             exampleTeam.slug,
 *             github_team_second.slug,
 *         ],
 *         dismissalUsers: ["foo-user"],
 *     },
 *     requiredStatusChecks: {
 *         contexts: ["ci/travis"],
 *         strict: false,
 *     },
 *     restrictions: {
 *         apps: ["foo-app"],
 *         teams: [exampleTeam.slug],
 *         users: ["foo-user"],
 *     },
 * });
 * const exampleTeamRepository = new github.TeamRepository("example", {
 *     permission: "pull",
 *     repository: github_repository_example.name,
 *     teamId: exampleTeam.id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-github/blob/master/website/docs/r/branch_protection.html.markdown.
 */
export class BranchProtection extends pulumi.CustomResource {
    /**
     * Get an existing BranchProtection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BranchProtectionState, opts?: pulumi.CustomResourceOptions): BranchProtection {
        return new BranchProtection(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'github:index/branchProtection:BranchProtection';

    /**
     * Returns true if the given object is an instance of BranchProtection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BranchProtection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BranchProtection.__pulumiType;
    }

    /**
     * The Git branch to protect.
     */
    public readonly branch!: pulumi.Output<string>;
    /**
     * Boolean, setting this to `true` enforces status checks for repository administrators.
     */
    public readonly enforceAdmins!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * The GitHub repository name.
     */
    public readonly repository!: pulumi.Output<string>;
    /**
     * Boolean, setting this to `true` requires all commits to be signed with GPG.
     */
    public readonly requireSignedCommits!: pulumi.Output<boolean | undefined>;
    /**
     * Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
     */
    public readonly requiredPullRequestReviews!: pulumi.Output<outputs.BranchProtectionRequiredPullRequestReviews | undefined>;
    /**
     * Enforce restrictions for required status checks. See Required Status Checks below for details.
     */
    public readonly requiredStatusChecks!: pulumi.Output<outputs.BranchProtectionRequiredStatusChecks | undefined>;
    /**
     * Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.
     */
    public readonly restrictions!: pulumi.Output<outputs.BranchProtectionRestrictions | undefined>;

    /**
     * Create a BranchProtection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BranchProtectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BranchProtectionArgs | BranchProtectionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as BranchProtectionState | undefined;
            inputs["branch"] = state ? state.branch : undefined;
            inputs["enforceAdmins"] = state ? state.enforceAdmins : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["repository"] = state ? state.repository : undefined;
            inputs["requireSignedCommits"] = state ? state.requireSignedCommits : undefined;
            inputs["requiredPullRequestReviews"] = state ? state.requiredPullRequestReviews : undefined;
            inputs["requiredStatusChecks"] = state ? state.requiredStatusChecks : undefined;
            inputs["restrictions"] = state ? state.restrictions : undefined;
        } else {
            const args = argsOrState as BranchProtectionArgs | undefined;
            if (!args || args.branch === undefined) {
                throw new Error("Missing required property 'branch'");
            }
            if (!args || args.repository === undefined) {
                throw new Error("Missing required property 'repository'");
            }
            inputs["branch"] = args ? args.branch : undefined;
            inputs["enforceAdmins"] = args ? args.enforceAdmins : undefined;
            inputs["repository"] = args ? args.repository : undefined;
            inputs["requireSignedCommits"] = args ? args.requireSignedCommits : undefined;
            inputs["requiredPullRequestReviews"] = args ? args.requiredPullRequestReviews : undefined;
            inputs["requiredStatusChecks"] = args ? args.requiredStatusChecks : undefined;
            inputs["restrictions"] = args ? args.restrictions : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(BranchProtection.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BranchProtection resources.
 */
export interface BranchProtectionState {
    /**
     * The Git branch to protect.
     */
    readonly branch?: pulumi.Input<string>;
    /**
     * Boolean, setting this to `true` enforces status checks for repository administrators.
     */
    readonly enforceAdmins?: pulumi.Input<boolean>;
    readonly etag?: pulumi.Input<string>;
    /**
     * The GitHub repository name.
     */
    readonly repository?: pulumi.Input<string>;
    /**
     * Boolean, setting this to `true` requires all commits to be signed with GPG.
     */
    readonly requireSignedCommits?: pulumi.Input<boolean>;
    /**
     * Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
     */
    readonly requiredPullRequestReviews?: pulumi.Input<inputs.BranchProtectionRequiredPullRequestReviews>;
    /**
     * Enforce restrictions for required status checks. See Required Status Checks below for details.
     */
    readonly requiredStatusChecks?: pulumi.Input<inputs.BranchProtectionRequiredStatusChecks>;
    /**
     * Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.
     */
    readonly restrictions?: pulumi.Input<inputs.BranchProtectionRestrictions>;
}

/**
 * The set of arguments for constructing a BranchProtection resource.
 */
export interface BranchProtectionArgs {
    /**
     * The Git branch to protect.
     */
    readonly branch: pulumi.Input<string>;
    /**
     * Boolean, setting this to `true` enforces status checks for repository administrators.
     */
    readonly enforceAdmins?: pulumi.Input<boolean>;
    /**
     * The GitHub repository name.
     */
    readonly repository: pulumi.Input<string>;
    /**
     * Boolean, setting this to `true` requires all commits to be signed with GPG.
     */
    readonly requireSignedCommits?: pulumi.Input<boolean>;
    /**
     * Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
     */
    readonly requiredPullRequestReviews?: pulumi.Input<inputs.BranchProtectionRequiredPullRequestReviews>;
    /**
     * Enforce restrictions for required status checks. See Required Status Checks below for details.
     */
    readonly requiredStatusChecks?: pulumi.Input<inputs.BranchProtectionRequiredStatusChecks>;
    /**
     * Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.
     */
    readonly restrictions?: pulumi.Input<inputs.BranchProtectionRestrictions>;
}
