// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GitHub.Inputs
{

    public sealed class RepositoryTemplateGetArgs : Pulumi.ResourceArgs
    {
        [Input("owner", required: true)]
        public Input<string> Owner { get; set; } = null!;

        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        public RepositoryTemplateGetArgs()
        {
        }
    }
}
