# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class UserSSHKey(pulumi.CustomResource):
    etag: pulumi.Output[str]
    key: pulumi.Output[str]
    """
    The public SSH key to add to your GitHub account.
    """
    title: pulumi.Output[str]
    """
    A descriptive name for the new key. e.g. `Personal MacBook Air`
    """
    url: pulumi.Output[str]
    """
    The URL of the SSH key
    """
    def __init__(__self__, resource_name, opts=None, key=None, title=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a GitHub user's SSH key resource.

        This resource allows you to add/remove SSH keys from your user account.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The public SSH key to add to your GitHub account.
        :param pulumi.Input[str] title: A descriptive name for the new key. e.g. `Personal MacBook Air`
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

            if key is None:
                raise TypeError("Missing required property 'key'")
            __props__['key'] = key
            if title is None:
                raise TypeError("Missing required property 'title'")
            __props__['title'] = title
            __props__['etag'] = None
            __props__['url'] = None
        super(UserSSHKey, __self__).__init__(
            'github:index/userSSHKey:UserSSHKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, etag=None, key=None, title=None, url=None):
        """
        Get an existing UserSSHKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The public SSH key to add to your GitHub account.
        :param pulumi.Input[str] title: A descriptive name for the new key. e.g. `Personal MacBook Air`
        :param pulumi.Input[str] url: The URL of the SSH key
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["etag"] = etag
        __props__["key"] = key
        __props__["title"] = title
        __props__["url"] = url
        return UserSSHKey(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

