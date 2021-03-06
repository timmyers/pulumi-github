# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class ActionsSecret(pulumi.CustomResource):
    created_at: pulumi.Output[str]
    """
    Date of actions_secret creation.
    """
    plaintext_value: pulumi.Output[str]
    """
    Plaintext value of the secret to be encrypted
    """
    repository: pulumi.Output[str]
    """
    Name of the repository
    """
    secret_name: pulumi.Output[str]
    """
    Name of the secret
    """
    updated_at: pulumi.Output[str]
    """
    Date of actions_secret update.
    """
    def __init__(__self__, resource_name, opts=None, plaintext_value=None, repository=None, secret_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a ActionsSecret resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
        :param pulumi.Input[str] repository: Name of the repository
        :param pulumi.Input[str] secret_name: Name of the secret
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

            if plaintext_value is None:
                raise TypeError("Missing required property 'plaintext_value'")
            __props__['plaintext_value'] = plaintext_value
            if repository is None:
                raise TypeError("Missing required property 'repository'")
            __props__['repository'] = repository
            if secret_name is None:
                raise TypeError("Missing required property 'secret_name'")
            __props__['secret_name'] = secret_name
            __props__['created_at'] = None
            __props__['updated_at'] = None
        super(ActionsSecret, __self__).__init__(
            'github:index/actionsSecret:ActionsSecret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, created_at=None, plaintext_value=None, repository=None, secret_name=None, updated_at=None):
        """
        Get an existing ActionsSecret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Date of actions_secret creation.
        :param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
        :param pulumi.Input[str] repository: Name of the repository
        :param pulumi.Input[str] secret_name: Name of the secret
        :param pulumi.Input[str] updated_at: Date of actions_secret update.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["created_at"] = created_at
        __props__["plaintext_value"] = plaintext_value
        __props__["repository"] = repository
        __props__["secret_name"] = secret_name
        __props__["updated_at"] = updated_at
        return ActionsSecret(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

