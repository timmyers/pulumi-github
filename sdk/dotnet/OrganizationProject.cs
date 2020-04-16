// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GitHub
{
    /// <summary>
    /// This resource allows you to create and manage projects for GitHub organization.
    /// </summary>
    public partial class OrganizationProject : Pulumi.CustomResource
    {
        /// <summary>
        /// The body of the project.
        /// </summary>
        [Output("body")]
        public Output<string?> Body { get; private set; } = null!;

        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// The name of the project.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// URL of the project
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a OrganizationProject resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OrganizationProject(string name, OrganizationProjectArgs? args = null, CustomResourceOptions? options = null)
            : base("github:index/organizationProject:OrganizationProject", name, args ?? new OrganizationProjectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private OrganizationProject(string name, Input<string> id, OrganizationProjectState? state = null, CustomResourceOptions? options = null)
            : base("github:index/organizationProject:OrganizationProject", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing OrganizationProject resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static OrganizationProject Get(string name, Input<string> id, OrganizationProjectState? state = null, CustomResourceOptions? options = null)
        {
            return new OrganizationProject(name, id, state, options);
        }
    }

    public sealed class OrganizationProjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The body of the project.
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        /// <summary>
        /// The name of the project.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public OrganizationProjectArgs()
        {
        }
    }

    public sealed class OrganizationProjectState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The body of the project.
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The name of the project.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// URL of the project
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public OrganizationProjectState()
        {
        }
    }
}
