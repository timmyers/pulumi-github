# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from ../.. import utilities, tables

class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, avatar_url=None, bio=None, blog=None, company=None, created_at=None, email=None, followers=None, following=None, gpg_keys=None, gravatar_id=None, id=None, location=None, login=None, name=None, node_id=None, public_gists=None, public_repos=None, site_admin=None, ssh_keys=None, updated_at=None, username=None):
        if avatar_url and not isinstance(avatar_url, str):
            raise TypeError("Expected argument 'avatar_url' to be a str")
        __self__.avatar_url = avatar_url
        """
        the user's avatar URL.
        """
        if bio and not isinstance(bio, str):
            raise TypeError("Expected argument 'bio' to be a str")
        __self__.bio = bio
        """
        the user's bio.
        """
        if blog and not isinstance(blog, str):
            raise TypeError("Expected argument 'blog' to be a str")
        __self__.blog = blog
        """
        the user's blog location.
        """
        if company and not isinstance(company, str):
            raise TypeError("Expected argument 'company' to be a str")
        __self__.company = company
        """
        the user's company name.
        """
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        __self__.created_at = created_at
        """
        the creation date.
        """
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        __self__.email = email
        """
        the user's email.
        """
        if followers and not isinstance(followers, float):
            raise TypeError("Expected argument 'followers' to be a float")
        __self__.followers = followers
        """
        the number of followers.
        """
        if following and not isinstance(following, float):
            raise TypeError("Expected argument 'following' to be a float")
        __self__.following = following
        """
        the number of following users.
        """
        if gpg_keys and not isinstance(gpg_keys, list):
            raise TypeError("Expected argument 'gpg_keys' to be a list")
        __self__.gpg_keys = gpg_keys
        """
        list of user's GPG keys.
        """
        if gravatar_id and not isinstance(gravatar_id, str):
            raise TypeError("Expected argument 'gravatar_id' to be a str")
        __self__.gravatar_id = gravatar_id
        """
        the user's gravatar ID.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        the user's location.
        """
        if login and not isinstance(login, str):
            raise TypeError("Expected argument 'login' to be a str")
        __self__.login = login
        """
        the user's login.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        the user's full name.
        """
        if node_id and not isinstance(node_id, str):
            raise TypeError("Expected argument 'node_id' to be a str")
        __self__.node_id = node_id
        if public_gists and not isinstance(public_gists, float):
            raise TypeError("Expected argument 'public_gists' to be a float")
        __self__.public_gists = public_gists
        """
        the number of public gists.
        """
        if public_repos and not isinstance(public_repos, float):
            raise TypeError("Expected argument 'public_repos' to be a float")
        __self__.public_repos = public_repos
        """
        the number of public repositories.
        """
        if site_admin and not isinstance(site_admin, bool):
            raise TypeError("Expected argument 'site_admin' to be a bool")
        __self__.site_admin = site_admin
        """
        whether the user is a GitHub admin.
        """
        if ssh_keys and not isinstance(ssh_keys, list):
            raise TypeError("Expected argument 'ssh_keys' to be a list")
        __self__.ssh_keys = ssh_keys
        """
        list of user's SSH keys.
        """
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        __self__.updated_at = updated_at
        """
        the update date.
        """
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        __self__.username = username
class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            avatar_url=self.avatar_url,
            bio=self.bio,
            blog=self.blog,
            company=self.company,
            created_at=self.created_at,
            email=self.email,
            followers=self.followers,
            following=self.following,
            gpg_keys=self.gpg_keys,
            gravatar_id=self.gravatar_id,
            id=self.id,
            location=self.location,
            login=self.login,
            name=self.name,
            node_id=self.node_id,
            public_gists=self.public_gists,
            public_repos=self.public_repos,
            site_admin=self.site_admin,
            ssh_keys=self.ssh_keys,
            updated_at=self.updated_at,
            username=self.username)

def get_user(username=None,opts=None):
    """
    Use this data source to retrieve information about a GitHub user.




    :param str username: The username.
    """
    __args__ = dict()


    __args__['username'] = username
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('github:index/getuser/getUser:getUser', __args__, opts=opts).value

    return AwaitableGetUserResult(
        avatar_url=__ret__.get('avatarUrl'),
        bio=__ret__.get('bio'),
        blog=__ret__.get('blog'),
        company=__ret__.get('company'),
        created_at=__ret__.get('createdAt'),
        email=__ret__.get('email'),
        followers=__ret__.get('followers'),
        following=__ret__.get('following'),
        gpg_keys=__ret__.get('gpgKeys'),
        gravatar_id=__ret__.get('gravatarId'),
        id=__ret__.get('id'),
        location=__ret__.get('location'),
        login=__ret__.get('login'),
        name=__ret__.get('name'),
        node_id=__ret__.get('nodeId'),
        public_gists=__ret__.get('publicGists'),
        public_repos=__ret__.get('publicRepos'),
        site_admin=__ret__.get('siteAdmin'),
        ssh_keys=__ret__.get('sshKeys'),
        updated_at=__ret__.get('updatedAt'),
        username=__ret__.get('username'))