import * as github from "@pulumi/github";

const repo = new github.Repository("my-repo", {
  name: "my-repo"
})

export const githubCloneUrl = repo.httpCloneUrl
