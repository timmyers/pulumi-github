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
    /// This resource allows you to create and manage webhooks for repositories within your
    /// GitHub organization.
    /// 
    /// This resource cannot currently be used to manage webhooks for *personal* repositories,
    /// outside of organizations.
    /// </summary>
    public partial class RepositoryWebhook : Pulumi.CustomResource
    {
        /// <summary>
        /// Indicate of the webhook should receive events. Defaults to `true`.
        /// </summary>
        [Output("active")]
        public Output<bool?> Active { get; private set; } = null!;

        /// <summary>
        /// key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`. `secret` is [the shared secret, see API documentation](https://developer.github.com/v3/repos/hooks/#create-a-hook).
        /// </summary>
        [Output("configuration")]
        public Output<Outputs.RepositoryWebhookConfiguration?> Configuration { get; private set; } = null!;

        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/).
        /// </summary>
        [Output("events")]
        public Output<ImmutableArray<string>> Events { get; private set; } = null!;

        /// <summary>
        /// The repository of the webhook.
        /// </summary>
        [Output("repository")]
        public Output<string> Repository { get; private set; } = null!;

        /// <summary>
        /// URL of the webhook
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a RepositoryWebhook resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RepositoryWebhook(string name, RepositoryWebhookArgs args, CustomResourceOptions? options = null)
            : base("github:index/repositoryWebhook:RepositoryWebhook", name, args ?? new RepositoryWebhookArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RepositoryWebhook(string name, Input<string> id, RepositoryWebhookState? state = null, CustomResourceOptions? options = null)
            : base("github:index/repositoryWebhook:RepositoryWebhook", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RepositoryWebhook resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RepositoryWebhook Get(string name, Input<string> id, RepositoryWebhookState? state = null, CustomResourceOptions? options = null)
        {
            return new RepositoryWebhook(name, id, state, options);
        }
    }

    public sealed class RepositoryWebhookArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicate of the webhook should receive events. Defaults to `true`.
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`. `secret` is [the shared secret, see API documentation](https://developer.github.com/v3/repos/hooks/#create-a-hook).
        /// </summary>
        [Input("configuration")]
        public Input<Inputs.RepositoryWebhookConfigurationArgs>? Configuration { get; set; }

        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/).
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// The repository of the webhook.
        /// </summary>
        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        public RepositoryWebhookArgs()
        {
        }
    }

    public sealed class RepositoryWebhookState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicate of the webhook should receive events. Defaults to `true`.
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// key/value pair of configuration for this webhook. Available keys are `url`, `content_type`, `secret` and `insecure_ssl`. `secret` is [the shared secret, see API documentation](https://developer.github.com/v3/repos/hooks/#create-a-hook).
        /// </summary>
        [Input("configuration")]
        public Input<Inputs.RepositoryWebhookConfigurationGetArgs>? Configuration { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("events")]
        private InputList<string>? _events;

        /// <summary>
        /// A list of events which should trigger the webhook. See a list of [available events](https://developer.github.com/v3/activity/events/types/).
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// The repository of the webhook.
        /// </summary>
        [Input("repository")]
        public Input<string>? Repository { get; set; }

        /// <summary>
        /// URL of the webhook
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public RepositoryWebhookState()
        {
        }
    }
}
