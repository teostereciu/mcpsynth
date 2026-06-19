# REST API endpoints for dependency review

*Source: https://docs.github.com/en/rest/dependency-graph/dependency-review*

---

# REST API endpoints for dependency review
Use the REST API to interact with dependency changes.

## About dependency review
You can use the REST API to view dependency changes, and the security impact of these changes, before you add them to your environment. You can view the diff of dependencies between two commits of a repository, including vulnerability data for any version updates with known vulnerabilities. For more information about dependency review, seeAbout dependency review.

## Get a diff of the dependencies between commits
Gets the diff of the dependency changes between two commits of a repository, based on the changes to the dependency manifests made in those commits.

### Fine-grained access tokens for "Get a diff of the dependencies between commits"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a diff of the dependencies between commits"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
baseheadstringRequiredThe base and head Git revisions to compare. The Git revisions will be resolved to commit SHAs. Named revisions will be resolved to their corresponding HEAD commits, and an appropriate merge base will be determined. This parameter expects the format{base}...{head}.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The base and head Git revisions to compare. The Git revisions will be resolved to commit SHAs. Named revisions will be resolved to their corresponding HEAD commits, and an appropriate merge base will be determined. This parameter expects the format{base}...{head}.

[TABLE]
Name, Type, Description
namestringThe full path, relative to the repository root, of the dependency manifest file.
[/TABLE]
The full path, relative to the repository root, of the dependency manifest file.

### HTTP response status codes for "Get a diff of the dependencies between commits"

[TABLE]
Status code | Description
200 | OK
403 | Response for a private repository when GitHub Advanced Security is not enabled, or if used against a fork
404 | Resource not found
[/TABLE]
OK
Response for a private repository when GitHub Advanced Security is not enabled, or if used against a fork
Resource not found

### Code samples for "Get a diff of the dependencies between commits"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependency-graph/compare/BASEHEAD
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "change_type": "removed",
    "manifest": "package.json",
    "ecosystem": "npm",
    "name": "helmet",
    "version": "4.6.0",
    "package_url": "pkg:npm/helmet@4.6.0",
    "license": "MIT",
    "source_repository_url": "https://github.com/helmetjs/helmet",
    "vulnerabilities": []
  },
  {
    "change_type": "added",
    "manifest": "package.json",
    "ecosystem": "npm",
    "name": "helmet",
    "version": "5.0.0",
    "package_url": "pkg:npm/helmet@5.0.0",
    "license": "MIT",
    "source_repository_url": "https://github.com/helmetjs/helmet",
    "vulnerabilities": []
  },
  {
    "change_type": "added",
    "manifest": "Gemfile",
    "ecosystem": "rubygems",
    "name": "ruby-openid",
    "version": "2.7.0",
    "package_url": "pkg:gem/ruby-openid@2.7.0",
    "license": null,
    "source_repository_url": "https://github.com/openid/ruby-openid",
    "vulnerabilities": [
      {
        "severity": "critical",
        "advisory_ghsa_id": "GHSA-fqfj-cmh6-hj49",
        "advisory_summary": "Ruby OpenID",
        "advisory_url": "https://github.com/advisories/GHSA-fqfj-cmh6-hj49"
      }
    ]
  }
]
```