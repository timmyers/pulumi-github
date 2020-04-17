[![Build Status](https://travis-ci.com/timmyers/pulumi-github.svg?branch=master)](https://travis-ci.com/timmyers/pulumi-github)

# GitHub Resource Provider

The GitHub resource provider for Pulumi lets you manage GitHub resources in your cloud programs. To use
this package, please [install the Pulumi CLI first](https://pulumi.io/).

## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @timmyers/pulumi-github

or `yarn`:

    $ yarn add @timmyers/pulumi-github

### Python

To use from Python, install using `pip`:

    $ pip install pulumi_github

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/timmyers/pulumi-github/sdk/go/...

## Configuration

The following configuration points are available for the `github` provider:

- `github:token` (environment: `GITHUB_TOKEN`) - the account for `github`
- `github:organization` (environment: `GITHUB_ORGANIZATION`) - the api token for `github`
- `github:base_url` (environment: `GITHUB_BASE_URL`) - the api token for `github`

## Reference

For detailed reference documentation, please visit [the API docs][1].

[1]: https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/github/index.html
