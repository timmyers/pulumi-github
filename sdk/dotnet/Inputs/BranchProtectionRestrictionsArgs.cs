// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GitHub.Inputs
{

    public sealed class BranchProtectionRestrictionsArgs : Pulumi.ResourceArgs
    {
        [Input("apps")]
        private InputList<string>? _apps;
        public InputList<string> Apps
        {
            get => _apps ?? (_apps = new InputList<string>());
            set => _apps = value;
        }

        [Input("teams")]
        private InputList<string>? _teams;
        public InputList<string> Teams
        {
            get => _teams ?? (_teams = new InputList<string>());
            set => _teams = value;
        }

        [Input("users")]
        private InputList<string>? _users;
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        public BranchProtectionRestrictionsArgs()
        {
        }
    }
}
