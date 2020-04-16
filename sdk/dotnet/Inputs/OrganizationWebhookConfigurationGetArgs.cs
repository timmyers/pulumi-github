// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GitHub.Inputs
{

    public sealed class OrganizationWebhookConfigurationGetArgs : Pulumi.ResourceArgs
    {
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        [Input("insecureSsl")]
        public Input<bool>? InsecureSsl { get; set; }

        [Input("secret")]
        public Input<string>? Secret { get; set; }

        /// <summary>
        /// URL of the webhook
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public OrganizationWebhookConfigurationGetArgs()
        {
        }
    }
}
