# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class BranchProtection(pulumi.CustomResource):
    branch: pulumi.Output[str]
    """
    The Git branch to protect.
    """
    enforce_admins: pulumi.Output[bool]
    """
    Boolean, setting this to `true` enforces status checks for repository administrators.
    """
    etag: pulumi.Output[str]
    repository: pulumi.Output[str]
    """
    The GitHub repository name.
    """
    require_signed_commits: pulumi.Output[bool]
    """
    Boolean, setting this to `true` requires all commits to be signed with GPG.
    """
    required_pull_request_reviews: pulumi.Output[dict]
    """
    Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.

      * `dismissStaleReviews` (`bool`)
      * `dismissalTeams` (`list`)
      * `dismissalUsers` (`list`)
      * `includeAdmins` (`bool`)
      * `requireCodeOwnerReviews` (`bool`)
      * `requiredApprovingReviewCount` (`float`)
    """
    required_status_checks: pulumi.Output[dict]
    """
    Enforce restrictions for required status checks. See Required Status Checks below for details.

      * `contexts` (`list`)
      * `includeAdmins` (`bool`)
      * `strict` (`bool`)
    """
    restrictions: pulumi.Output[dict]
    """
    Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.

      * `apps` (`list`)
      * `teams` (`list`)
      * `users` (`list`)
    """
    def __init__(__self__, resource_name, opts=None, branch=None, enforce_admins=None, repository=None, require_signed_commits=None, required_pull_request_reviews=None, required_status_checks=None, restrictions=None, __props__=None, __name__=None, __opts__=None):
        """
        Protects a GitHub branch.

        This resource allows you to configure branch protection for repositories in your organization. When applied, the branch will be protected from forced pushes and deletion. Additional constraints, such as required status checks or restrictions on users, teams, and apps, can also be configured.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The Git branch to protect.
        :param pulumi.Input[bool] enforce_admins: Boolean, setting this to `true` enforces status checks for repository administrators.
        :param pulumi.Input[str] repository: The GitHub repository name.
        :param pulumi.Input[bool] require_signed_commits: Boolean, setting this to `true` requires all commits to be signed with GPG.
        :param pulumi.Input[dict] required_pull_request_reviews: Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
        :param pulumi.Input[dict] required_status_checks: Enforce restrictions for required status checks. See Required Status Checks below for details.
        :param pulumi.Input[dict] restrictions: Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.

        The **required_pull_request_reviews** object supports the following:

          * `dismissStaleReviews` (`pulumi.Input[bool]`)
          * `dismissalTeams` (`pulumi.Input[list]`)
          * `dismissalUsers` (`pulumi.Input[list]`)
          * `includeAdmins` (`pulumi.Input[bool]`)
          * `requireCodeOwnerReviews` (`pulumi.Input[bool]`)
          * `requiredApprovingReviewCount` (`pulumi.Input[float]`)

        The **required_status_checks** object supports the following:

          * `contexts` (`pulumi.Input[list]`)
          * `includeAdmins` (`pulumi.Input[bool]`)
          * `strict` (`pulumi.Input[bool]`)

        The **restrictions** object supports the following:

          * `apps` (`pulumi.Input[list]`)
          * `teams` (`pulumi.Input[list]`)
          * `users` (`pulumi.Input[list]`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if branch is None:
                raise TypeError("Missing required property 'branch'")
            __props__['branch'] = branch
            __props__['enforce_admins'] = enforce_admins
            if repository is None:
                raise TypeError("Missing required property 'repository'")
            __props__['repository'] = repository
            __props__['require_signed_commits'] = require_signed_commits
            __props__['required_pull_request_reviews'] = required_pull_request_reviews
            __props__['required_status_checks'] = required_status_checks
            __props__['restrictions'] = restrictions
            __props__['etag'] = None
        super(BranchProtection, __self__).__init__(
            'github:index/branchProtection:BranchProtection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, branch=None, enforce_admins=None, etag=None, repository=None, require_signed_commits=None, required_pull_request_reviews=None, required_status_checks=None, restrictions=None):
        """
        Get an existing BranchProtection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The Git branch to protect.
        :param pulumi.Input[bool] enforce_admins: Boolean, setting this to `true` enforces status checks for repository administrators.
        :param pulumi.Input[str] repository: The GitHub repository name.
        :param pulumi.Input[bool] require_signed_commits: Boolean, setting this to `true` requires all commits to be signed with GPG.
        :param pulumi.Input[dict] required_pull_request_reviews: Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
        :param pulumi.Input[dict] required_status_checks: Enforce restrictions for required status checks. See Required Status Checks below for details.
        :param pulumi.Input[dict] restrictions: Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.

        The **required_pull_request_reviews** object supports the following:

          * `dismissStaleReviews` (`pulumi.Input[bool]`)
          * `dismissalTeams` (`pulumi.Input[list]`)
          * `dismissalUsers` (`pulumi.Input[list]`)
          * `includeAdmins` (`pulumi.Input[bool]`)
          * `requireCodeOwnerReviews` (`pulumi.Input[bool]`)
          * `requiredApprovingReviewCount` (`pulumi.Input[float]`)

        The **required_status_checks** object supports the following:

          * `contexts` (`pulumi.Input[list]`)
          * `includeAdmins` (`pulumi.Input[bool]`)
          * `strict` (`pulumi.Input[bool]`)

        The **restrictions** object supports the following:

          * `apps` (`pulumi.Input[list]`)
          * `teams` (`pulumi.Input[list]`)
          * `users` (`pulumi.Input[list]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["branch"] = branch
        __props__["enforce_admins"] = enforce_admins
        __props__["etag"] = etag
        __props__["repository"] = repository
        __props__["require_signed_commits"] = require_signed_commits
        __props__["required_pull_request_reviews"] = required_pull_request_reviews
        __props__["required_status_checks"] = required_status_checks
        __props__["restrictions"] = restrictions
        return BranchProtection(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

