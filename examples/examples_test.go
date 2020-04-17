// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

package examples

import (
	"os"
	"path"
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v2/testing/integration"
)

func TestGithubRepoTs(t *testing.T) {
	getToken(t)
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "github_repo", "ts"),
		})

	integration.ProgramTest(t, &test)
}

func TestGithubRepoPython(t *testing.T) {
	getToken(t)
	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "github_repo", "python"),
		})

	integration.ProgramTest(t, &test)
}

func TestGithubRepoCsharp(t *testing.T) {
	getToken(t)
	test := getCsharpBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "github_repo", "csharp"),
		})

	integration.ProgramTest(t, &test)
}

func getToken(t *testing.T) string {
	token := os.Getenv("GITHUB_TOKEN")
	if token == "" {
		t.Skipf("Skipping test due to missing GITHUB_TOKEN environment variable")
	}

	return token
}

func getOrganization(t *testing.T) string {
	organization := os.Getenv("GITHUB_ORGANIZATION")
	if organization == "" {
		t.Skipf("Skipping test due to missing GITHUB_ORGANIZATION environment variable")
	}

	return organization
}

func getCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

func getBaseOptions(t *testing.T) integration.ProgramTestOptions {
	return integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
		Config: map[string]string{
			"github:token":        getToken(t),
			"github:organization": getOrganization(t),
		},
	}
}

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@timmyers/pulumi-github",
		},
	})

	return baseJS
}

func getCsharpBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseCsharp := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"Pulumi.GitHub",
		},
	})

	return baseCsharp
}

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	basePython := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return basePython
}
