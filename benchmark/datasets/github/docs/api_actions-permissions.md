# REST API endpoints for GitHub Actions permissions

*Source: https://docs.github.com/en/rest/actions/permissions*

---

# REST API endpoints for GitHub Actions permissions
Use the REST API to interact with permissions for GitHub Actions.

## About permissions for GitHub Actions
You can use the REST API to set permissions for the organizations and repositories that are allowed to run GitHub Actions, and the actions and reusable workflows that are allowed to run. For more information, seeBilling and usage.

## Get GitHub Actions permissions for an organization
Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable workflows in an organization.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions permissions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get GitHub Actions permissions for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get GitHub Actions permissions for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get GitHub Actions permissions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "enabled_repositories": "all",
  "allowed_actions": "selected",
  "selected_actions_url": "https://api.github.com/organizations/42/actions/permissions/selected-actions",
  "sha_pinning_required": true
}
```

## Set GitHub Actions permissions for an organization
Sets the GitHub Actions permissions policy for repositories and allowed actions and reusable workflows in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions permissions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set GitHub Actions permissions for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
enabled_repositoriesstringRequiredThe policy that controls the repositories in the organization that are allowed to run GitHub Actions.Can be one of:all,none,selected
allowed_actionsstringThe permissions policy that controls the actions and reusable workflows that are allowed to run.Can be one of:all,local_only,selected
sha_pinning_requiredbooleanWhether actions must be pinned to a full-length commit SHA.
[/TABLE]

```
enabled_repositories
```
The policy that controls the repositories in the organization that are allowed to run GitHub Actions.
Can be one of:all,none,selected

```
allowed_actions
```
The permissions policy that controls the actions and reusable workflows that are allowed to run.
Can be one of:all,local_only,selected

```
sha_pinning_required
```
Whether actions must be pinned to a full-length commit SHA.

### HTTP response status codes for "Set GitHub Actions permissions for an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set GitHub Actions permissions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions \
  -d '{"enabled_repositories":"all","allowed_actions":"selected","sha_pinning_required":true}'
```

#### Response

```
Status: 204
```

## Get artifact and log retention settings for an organization
Gets artifact and log retention settings for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Get artifact and log retention settings for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get artifact and log retention settings for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get artifact and log retention settings for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get artifact and log retention settings for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/artifact-and-log-retention
```

#### Example response
- Example response
- Response schema

```
Status: 200
```

```
{
  "days": 90,
  "maximum_allowed_days": 365
}
```

## Set artifact and log retention settings for an organization
Sets artifact and log retention settings for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Set artifact and log retention settings for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set artifact and log retention settings for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
daysintegerRequiredThe number of days to retain artifacts and logs
[/TABLE]
The number of days to retain artifacts and logs

### HTTP response status codes for "Set artifact and log retention settings for an organization"

[TABLE]
Status code | Description
204 | No content
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No content
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Set artifact and log retention settings for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/artifact-and-log-retention \
  -d '{"days":100}'
```

#### No content

```
Status: 204
```

## Get fork PR contributor approval permissions for an organization
Gets the fork PR contributor approval policy for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Get fork PR contributor approval permissions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get fork PR contributor approval permissions for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get fork PR contributor approval permissions for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get fork PR contributor approval permissions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/fork-pr-contributor-approval
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "approval_policy": "first_time_contributors"
}
```

## Set fork PR contributor approval permissions for an organization
Sets the fork PR contributor approval policy for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set fork PR contributor approval permissions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set fork PR contributor approval permissions for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
approval_policystringRequiredThe policy that controls when fork PR workflows require approval from a maintainer.Can be one of:first_time_contributors_new_to_github,first_time_contributors,all_external_contributors
[/TABLE]

```
approval_policy
```
The policy that controls when fork PR workflows require approval from a maintainer.
Can be one of:first_time_contributors_new_to_github,first_time_contributors,all_external_contributors

```
first_time_contributors_new_to_github
```

```
first_time_contributors
```

```
all_external_contributors
```

### HTTP response status codes for "Set fork PR contributor approval permissions for an organization"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set fork PR contributor approval permissions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/fork-pr-contributor-approval \
  -d '{"approval_policy":"first_time_contributors"}'
```

#### Response

```
Status: 204
```

## Get private repo fork PR workflow settings for an organization
Gets the settings for whether workflows from fork pull requests can run on private repositories in an organization.

### Fine-grained access tokens for "Get private repo fork PR workflow settings for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get private repo fork PR workflow settings for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get private repo fork PR workflow settings for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get private repo fork PR workflow settings for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/fork-pr-workflows-private-repos
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "run_workflows_from_fork_pull_requests": true,
  "send_write_tokens_to_workflows": false,
  "send_secrets_and_variables": false,
  "require_approval_for_fork_pr_workflows": true
}
```

## Set private repo fork PR workflow settings for an organization
Sets the settings for whether workflows from fork pull requests can run on private repositories in an organization.

### Fine-grained access tokens for "Set private repo fork PR workflow settings for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set private repo fork PR workflow settings for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
run_workflows_from_fork_pull_requestsbooleanRequiredWhether workflows triggered by pull requests from forks are allowed to run on private repositories.
send_write_tokens_to_workflowsbooleanWhether GitHub Actions can create pull requests or submit approving pull request reviews from a workflow triggered by a fork pull request.
send_secrets_and_variablesbooleanWhether to make secrets and variables available to workflows triggered by pull requests from forks.
require_approval_for_fork_pr_workflowsbooleanWhether workflows triggered by pull requests from forks require approval from a repository administrator to run.
[/TABLE]

```
run_workflows_from_fork_pull_requests
```
Whether workflows triggered by pull requests from forks are allowed to run on private repositories.

```
send_write_tokens_to_workflows
```
Whether GitHub Actions can create pull requests or submit approving pull request reviews from a workflow triggered by a fork pull request.

```
send_secrets_and_variables
```
Whether to make secrets and variables available to workflows triggered by pull requests from forks.

```
require_approval_for_fork_pr_workflows
```
Whether workflows triggered by pull requests from forks require approval from a repository administrator to run.

### HTTP response status codes for "Set private repo fork PR workflow settings for an organization"

[TABLE]
Status code | Description
204 | Empty response for successful settings update
403 | Forbidden - Fork PR workflow settings for private repositories are managed by the enterprise owner
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Empty response for successful settings update
Forbidden - Fork PR workflow settings for private repositories are managed by the enterprise owner
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set private repo fork PR workflow settings for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/fork-pr-workflows-private-repos \
  -d '{"run_workflows_from_fork_pull_requests":true,"send_write_tokens_to_workflows":false,"send_secrets_and_variables":false,"require_approval_for_fork_pr_workflows":true}'
```

#### Empty response for successful settings update

```
Status: 204
```

## List selected repositories enabled for GitHub Actions in an organization
Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy forenabled_repositoriesmust be configured toselected. For more information, see "Set GitHub Actions permissions for an organization."
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List selected repositories enabled for GitHub Actions in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List selected repositories enabled for GitHub Actions in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List selected repositories enabled for GitHub Actions in an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List selected repositories enabled for GitHub Actions in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/repositories
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "repositories": [
    {
      "id": 1296269,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "name": "Hello-World",
      "full_name": "octocat/Hello-World",
      "owner": {
        "login": "octocat",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": false
      },
      "private": false,
      "html_url": "https://github.com/octocat/Hello-World",
      "description": "This your first repo!",
      "fork": false,
      "url": "https://api.github.com/repos/octocat/Hello-World",
      "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
      "clone_url": "https://github.com/octocat/Hello-World.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World",
      "homepage": "https://github.com",
      "language": null,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues_count": 0,
      "is_template": true,
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "allow_rebase_merge": true,
      "template_repository": null,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://github.com/licenses/mit"
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  ]
}
```

## Set selected repositories enabled for GitHub Actions in an organization
Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy forenabled_repositoriesmust be configured toselected. For more information, see "Set GitHub Actions permissions for an organization."
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set selected repositories enabled for GitHub Actions in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set selected repositories enabled for GitHub Actions in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
selected_repository_idsarray of integersRequiredList of repository IDs to enable for GitHub Actions.
[/TABLE]

```
selected_repository_ids
```
List of repository IDs to enable for GitHub Actions.

### HTTP response status codes for "Set selected repositories enabled for GitHub Actions in an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set selected repositories enabled for GitHub Actions in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/repositories \
  -d '{"selected_repository_ids":[32,42]}'
```

#### Response

```
Status: 204
```

## Enable a selected repository for GitHub Actions in an organization
Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy forenabled_repositoriesmust be must be configured toselected. For more information, see "Set GitHub Actions permissions for an organization."
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Enable a selected repository for GitHub Actions in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Enable a selected repository for GitHub Actions in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
repository_idintegerRequiredThe unique identifier of the repository.
[/TABLE]
The organization name. The name is not case sensitive.

```
repository_id
```
The unique identifier of the repository.

### HTTP response status codes for "Enable a selected repository for GitHub Actions in an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Enable a selected repository for GitHub Actions in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/repositories/REPOSITORY_ID
```

#### Response

```
Status: 204
```

## Disable a selected repository for GitHub Actions in an organization
Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy forenabled_repositoriesmust be configured toselected. For more information, see "Set GitHub Actions permissions for an organization."
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Disable a selected repository for GitHub Actions in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Disable a selected repository for GitHub Actions in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
repository_idintegerRequiredThe unique identifier of the repository.
[/TABLE]
The organization name. The name is not case sensitive.

```
repository_id
```
The unique identifier of the repository.

### HTTP response status codes for "Disable a selected repository for GitHub Actions in an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Disable a selected repository for GitHub Actions in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/repositories/REPOSITORY_ID
```

#### Response

```
Status: 204
```

## Get allowed actions and reusable workflows for an organization
Gets the selected actions and reusable workflows that are allowed in an organization. To use this endpoint, the organization permission policy forallowed_actionsmust be configured toselected. For more information, see "Set GitHub Actions permissions for an organization."
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get allowed actions and reusable workflows for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get allowed actions and reusable workflows for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get allowed actions and reusable workflows for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get allowed actions and reusable workflows for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/selected-actions
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "github_owned_allowed": true,
  "verified_allowed": false,
  "patterns_allowed": [
    "monalisa/octocat@*",
    "docker/*"
  ]
}
```

## Set allowed actions and reusable workflows for an organization
Sets the actions and reusable workflows that are allowed in an organization. To use this endpoint, the organization permission policy forallowed_actionsmust be configured toselected. For more information, see "Set GitHub Actions permissions for an organization."
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set allowed actions and reusable workflows for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set allowed actions and reusable workflows for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
github_owned_allowedbooleanWhether GitHub-owned actions are allowed. For example, this includes the actions in theactionsorganization.
verified_allowedbooleanWhether actions from GitHub Marketplace verified creators are allowed. Set totrueto allow all actions by GitHub Marketplace verified creators.
patterns_allowedarray of stringsSpecifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,monalisa/octocat@*,monalisa/octocat@v2,monalisa/*.NoteThepatterns_allowedsetting only applies to public repositories.
[/TABLE]

```
github_owned_allowed
```
Whether GitHub-owned actions are allowed. For example, this includes the actions in theactionsorganization.

```
verified_allowed
```
Whether actions from GitHub Marketplace verified creators are allowed. Set totrueto allow all actions by GitHub Marketplace verified creators.

```
patterns_allowed
```
Specifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,monalisa/octocat@*,monalisa/octocat@v2,monalisa/*.
Note
Thepatterns_allowedsetting only applies to public repositories.

### HTTP response status codes for "Set allowed actions and reusable workflows for an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set allowed actions and reusable workflows for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/selected-actions \
  -d '{"github_owned_allowed":true,"verified_allowed":false,"patterns_allowed":["monalisa/octocat@*","docker/*"]}'
```

#### Response

```
Status: 204
```

## Get self-hosted runners settings for an organization
Gets the settings for self-hosted runners for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Get self-hosted runners settings for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get self-hosted runners settings for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get self-hosted runners settings for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get self-hosted runners settings for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/self-hosted-runners
```

#### Example response
- Example response
- Response schema

```
Status: 200
```

```
{
  "enabled_repositories": "selected",
  "selected_repositories_url": "http://api.github.localhost/organizations/1/actions/permissions/self-hosted-runners/repositories"
}
```

## Set self-hosted runners settings for an organization
Sets the settings for self-hosted runners for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Set self-hosted runners settings for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set self-hosted runners settings for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
enabled_repositoriesstringRequiredThe policy that controls whether self-hosted runners can be used in the organizationCan be one of:all,selected,none
[/TABLE]

```
enabled_repositories
```
The policy that controls whether self-hosted runners can be used in the organization
Can be one of:all,selected,none

### HTTP response status codes for "Set self-hosted runners settings for an organization"

[TABLE]
Status code | Description
204 | No content
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No content
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Set self-hosted runners settings for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/self-hosted-runners \
  -d '{"enabled_repositories":"all"}'
```

#### No content

```
Status: 204
```

## List repositories allowed to use self-hosted runners in an organization
Lists repositories that are allowed to use self-hosted runners in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "List repositories allowed to use self-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List repositories allowed to use self-hosted runners in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repositories allowed to use self-hosted runners in an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "List repositories allowed to use self-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/self-hosted-runners/repositories
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "repositories": [
    {
      "id": 1296269,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "name": "Hello-World",
      "full_name": "octocat/Hello-World",
      "owner": {
        "login": "octocat",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": false
      },
      "private": false,
      "html_url": "https://github.com/octocat/Hello-World",
      "description": "This your first repo!",
      "fork": false,
      "url": "https://api.github.com/repos/octocat/Hello-World",
      "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
      "clone_url": "https://github.com/octocat/Hello-World.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World",
      "homepage": "https://github.com",
      "language": null,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues_count": 0,
      "is_template": true,
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "allow_rebase_merge": true,
      "template_repository": null,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://github.com/licenses/mit"
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  ]
}
```

## Set repositories allowed to use self-hosted runners in an organization
Sets repositories that are allowed to use self-hosted runners in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Set repositories allowed to use self-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set repositories allowed to use self-hosted runners in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
selected_repository_idsarray of integersRequiredIDs of repositories that can use repository-level self-hosted runners
[/TABLE]

```
selected_repository_ids
```
IDs of repositories that can use repository-level self-hosted runners

### HTTP response status codes for "Set repositories allowed to use self-hosted runners in an organization"

[TABLE]
Status code | Description
204 | No content
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No content
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set repositories allowed to use self-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/self-hosted-runners/repositories \
  -d '{"selected_repository_ids":[1,2,3]}'
```

#### No content

```
Status: 204
```

## Add a repository to the list of repositories allowed to use self-hosted runners in an organization
Adds a repository to the list of repositories that are allowed to use self-hosted runners in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Add a repository to the list of repositories allowed to use self-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Add a repository to the list of repositories allowed to use self-hosted runners in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
repository_idintegerRequiredThe unique identifier of the repository.
[/TABLE]
The organization name. The name is not case sensitive.

```
repository_id
```
The unique identifier of the repository.

### HTTP response status codes for "Add a repository to the list of repositories allowed to use self-hosted runners in an organization"

[TABLE]
Status code | Description
204 | No content
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No content
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Add a repository to the list of repositories allowed to use self-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/self-hosted-runners/repositories/REPOSITORY_ID
```

#### No content

```
Status: 204
```

## Remove a repository from the list of repositories allowed to use self-hosted runners in an organization
Removes a repository from the list of repositories that are allowed to use self-hosted runners in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope or the "Actions policies" fine-grained permission to use this endpoint.

### Fine-grained access tokens for "Remove a repository from the list of repositories allowed to use self-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Remove a repository from the list of repositories allowed to use self-hosted runners in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
repository_idintegerRequiredThe unique identifier of the repository.
[/TABLE]
The organization name. The name is not case sensitive.

```
repository_id
```
The unique identifier of the repository.

### HTTP response status codes for "Remove a repository from the list of repositories allowed to use self-hosted runners in an organization"

[TABLE]
Status code | Description
204 | No content
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No content
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Remove a repository from the list of repositories allowed to use self-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/self-hosted-runners/repositories/REPOSITORY_ID
```

#### No content

```
Status: 204
```

## Get default workflow permissions for an organization
Gets the default workflow permissions granted to theGITHUB_TOKENwhen running workflows in an organization,
as well as whether GitHub Actions can submit approving pull request reviews. For more information, see
"Setting the permissions of the GITHUB_TOKEN for your organization."
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get default workflow permissions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get default workflow permissions for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get default workflow permissions for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get default workflow permissions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/workflow
```

#### Give read-only permission, and allow approving PRs.
- Example response
- Response schema

```
Status: 200
```

```
{
  "default_workflow_permissions": "read",
  "can_approve_pull_request_reviews": true
}
```

## Set default workflow permissions for an organization
Sets the default workflow permissions granted to theGITHUB_TOKENwhen running workflows in an organization, and sets if GitHub Actions
can submit approving pull request reviews. For more information, see
"Setting the permissions of the GITHUB_TOKEN for your organization."
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set default workflow permissions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set default workflow permissions for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
default_workflow_permissionsstringThe default workflow permissions granted to the GITHUB_TOKEN when running workflows.Can be one of:read,write
can_approve_pull_request_reviewsbooleanWhether GitHub Actions can approve pull requests. Enabling this can be a security risk.
[/TABLE]

```
default_workflow_permissions
```
The default workflow permissions granted to the GITHUB_TOKEN when running workflows.
Can be one of:read,write

```
can_approve_pull_request_reviews
```
Whether GitHub Actions can approve pull requests. Enabling this can be a security risk.

### HTTP response status codes for "Set default workflow permissions for an organization"

[TABLE]
Status code | Description
204 | Success response
[/TABLE]
Success response

### Code samples for "Set default workflow permissions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/permissions/workflow \
  -d '{"default_workflow_permissions":"read","can_approve_pull_request_reviews":true}'
```

#### Success response

```
Status: 204
```

## Get GitHub Actions permissions for a repository
Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions and reusable workflows allowed to run in the repository.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions permissions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get GitHub Actions permissions for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get GitHub Actions permissions for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get GitHub Actions permissions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "enabled": true,
  "allowed_actions": "selected",
  "selected_actions_url": "https://api.github.com/repositories/42/actions/permissions/selected-actions",
  "sha_pinning_required": true
}
```

## Set GitHub Actions permissions for a repository
Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions and reusable workflows in the repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions permissions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set GitHub Actions permissions for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
enabledbooleanRequiredWhether GitHub Actions is enabled on the repository.
allowed_actionsstringThe permissions policy that controls the actions and reusable workflows that are allowed to run.Can be one of:all,local_only,selected
sha_pinning_requiredbooleanWhether actions must be pinned to a full-length commit SHA.
[/TABLE]
Whether GitHub Actions is enabled on the repository.

```
allowed_actions
```
The permissions policy that controls the actions and reusable workflows that are allowed to run.
Can be one of:all,local_only,selected

```
sha_pinning_required
```
Whether actions must be pinned to a full-length commit SHA.

### HTTP response status codes for "Set GitHub Actions permissions for a repository"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set GitHub Actions permissions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions \
  -d '{"enabled":true,"allowed_actions":"selected","sha_pinning_required":true}'
```

#### Response

```
Status: 204
```

## Get the level of access for workflows outside of the repository
Gets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository.
This endpoint only applies to private repositories.
For more information, see "Allowing access to components in a private repository."
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get the level of access for workflows outside of the repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get the level of access for workflows outside of the repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get the level of access for workflows outside of the repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get the level of access for workflows outside of the repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/access
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "access_level": "organization"
}
```

## Set the level of access for workflows outside of the repository
Sets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository.
This endpoint only applies to private repositories.
For more information, see "Allowing access to components in a private repository".
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set the level of access for workflows outside of the repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set the level of access for workflows outside of the repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
access_levelstringRequiredDefines the level of access that workflows outside of the repository have to actions and reusable workflows within the
repository.nonemeans the access is only possible from workflows in this repository.userlevel access allows sharing across user owned private repositories only.organizationlevel access allows sharing across the organization.Can be one of:none,user,organization
[/TABLE]

```
access_level
```
Defines the level of access that workflows outside of the repository have to actions and reusable workflows within the
repository.
nonemeans the access is only possible from workflows in this repository.userlevel access allows sharing across user owned private repositories only.organizationlevel access allows sharing across the organization.
Can be one of:none,user,organization

```
organization
```

### HTTP response status codes for "Set the level of access for workflows outside of the repository"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set the level of access for workflows outside of the repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/access \
  -d '{"access_level":"organization"}'
```

#### Response

```
Status: 204
```

## Get artifact and log retention settings for a repository
Gets artifact and log retention settings for a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get artifact and log retention settings for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get artifact and log retention settings for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get artifact and log retention settings for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get artifact and log retention settings for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/artifact-and-log-retention
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "days": 90,
  "maximum_allowed_days": 365
}
```

## Set artifact and log retention settings for a repository
Sets artifact and log retention settings for a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set artifact and log retention settings for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set artifact and log retention settings for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
daysintegerRequiredThe number of days to retain artifacts and logs
[/TABLE]
The number of days to retain artifacts and logs

### HTTP response status codes for "Set artifact and log retention settings for a repository"

[TABLE]
Status code | Description
204 | Empty response for successful settings update
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Empty response for successful settings update
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set artifact and log retention settings for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/artifact-and-log-retention \
  -d '{"days":90}'
```

#### Empty response for successful settings update

```
Status: 204
```

## Get fork PR contributor approval permissions for a repository
Gets the fork PR contributor approval policy for a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get fork PR contributor approval permissions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get fork PR contributor approval permissions for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get fork PR contributor approval permissions for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get fork PR contributor approval permissions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/fork-pr-contributor-approval
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "approval_policy": "first_time_contributors"
}
```

## Set fork PR contributor approval permissions for a repository
Sets the fork PR contributor approval policy for a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set fork PR contributor approval permissions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set fork PR contributor approval permissions for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
approval_policystringRequiredThe policy that controls when fork PR workflows require approval from a maintainer.Can be one of:first_time_contributors_new_to_github,first_time_contributors,all_external_contributors
[/TABLE]

```
approval_policy
```
The policy that controls when fork PR workflows require approval from a maintainer.
Can be one of:first_time_contributors_new_to_github,first_time_contributors,all_external_contributors

```
first_time_contributors_new_to_github
```

```
first_time_contributors
```

```
all_external_contributors
```

### HTTP response status codes for "Set fork PR contributor approval permissions for a repository"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set fork PR contributor approval permissions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/fork-pr-contributor-approval \
  -d '{"approval_policy":"first_time_contributors"}'
```

#### Response

```
Status: 204
```

## Get private repo fork PR workflow settings for a repository
Gets the settings for whether workflows from fork pull requests can run on a private repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get private repo fork PR workflow settings for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get private repo fork PR workflow settings for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get private repo fork PR workflow settings for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get private repo fork PR workflow settings for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/fork-pr-workflows-private-repos
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "run_workflows_from_fork_pull_requests": true,
  "send_write_tokens_to_workflows": false,
  "send_secrets_and_variables": false,
  "require_approval_for_fork_pr_workflows": true
}
```

## Set private repo fork PR workflow settings for a repository
Sets the settings for whether workflows from fork pull requests can run on a private repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set private repo fork PR workflow settings for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set private repo fork PR workflow settings for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
run_workflows_from_fork_pull_requestsbooleanRequiredWhether workflows triggered by pull requests from forks are allowed to run on private repositories.
send_write_tokens_to_workflowsbooleanWhether GitHub Actions can create pull requests or submit approving pull request reviews from a workflow triggered by a fork pull request.
send_secrets_and_variablesbooleanWhether to make secrets and variables available to workflows triggered by pull requests from forks.
require_approval_for_fork_pr_workflowsbooleanWhether workflows triggered by pull requests from forks require approval from a repository administrator to run.
[/TABLE]

```
run_workflows_from_fork_pull_requests
```
Whether workflows triggered by pull requests from forks are allowed to run on private repositories.

```
send_write_tokens_to_workflows
```
Whether GitHub Actions can create pull requests or submit approving pull request reviews from a workflow triggered by a fork pull request.

```
send_secrets_and_variables
```
Whether to make secrets and variables available to workflows triggered by pull requests from forks.

```
require_approval_for_fork_pr_workflows
```
Whether workflows triggered by pull requests from forks require approval from a repository administrator to run.

### HTTP response status codes for "Set private repo fork PR workflow settings for a repository"

[TABLE]
Status code | Description
204 | Empty response for successful settings update
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Empty response for successful settings update
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set private repo fork PR workflow settings for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/fork-pr-workflows-private-repos \
  -d '{"run_workflows_from_fork_pull_requests":true,"send_write_tokens_to_workflows":false,"send_secrets_and_variables":false,"require_approval_for_fork_pr_workflows":true}'
```

#### Empty response for successful settings update

```
Status: 204
```

## Get allowed actions and reusable workflows for a repository
Gets the settings for selected actions and reusable workflows that are allowed in a repository. To use this endpoint, the repository policy forallowed_actionsmust be configured toselected. For more information, see "Set GitHub Actions permissions for a repository."
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get allowed actions and reusable workflows for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get allowed actions and reusable workflows for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get allowed actions and reusable workflows for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get allowed actions and reusable workflows for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/selected-actions
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "github_owned_allowed": true,
  "verified_allowed": false,
  "patterns_allowed": [
    "monalisa/octocat@*",
    "docker/*"
  ]
}
```

## Set allowed actions and reusable workflows for a repository
Sets the actions and reusable workflows that are allowed in a repository. To use this endpoint, the repository permission policy forallowed_actionsmust be configured toselected. For more information, see "Set GitHub Actions permissions for a repository."
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set allowed actions and reusable workflows for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set allowed actions and reusable workflows for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
github_owned_allowedbooleanWhether GitHub-owned actions are allowed. For example, this includes the actions in theactionsorganization.
verified_allowedbooleanWhether actions from GitHub Marketplace verified creators are allowed. Set totrueto allow all actions by GitHub Marketplace verified creators.
patterns_allowedarray of stringsSpecifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,monalisa/octocat@*,monalisa/octocat@v2,monalisa/*.NoteThepatterns_allowedsetting only applies to public repositories.
[/TABLE]

```
github_owned_allowed
```
Whether GitHub-owned actions are allowed. For example, this includes the actions in theactionsorganization.

```
verified_allowed
```
Whether actions from GitHub Marketplace verified creators are allowed. Set totrueto allow all actions by GitHub Marketplace verified creators.

```
patterns_allowed
```
Specifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,monalisa/octocat@*,monalisa/octocat@v2,monalisa/*.
Note
Thepatterns_allowedsetting only applies to public repositories.

### HTTP response status codes for "Set allowed actions and reusable workflows for a repository"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set allowed actions and reusable workflows for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/selected-actions \
  -d '{"github_owned_allowed":true,"verified_allowed":false,"patterns_allowed":["monalisa/octocat@*","docker/*"]}'
```

#### Response

```
Status: 204
```

## Get default workflow permissions for a repository
Gets the default workflow permissions granted to theGITHUB_TOKENwhen running workflows in a repository,
as well as if GitHub Actions can submit approving pull request reviews.
For more information, see "Setting the permissions of the GITHUB_TOKEN for your repository."
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get default workflow permissions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get default workflow permissions for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get default workflow permissions for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get default workflow permissions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/workflow
```

#### Give read-only permission, and allow approving PRs.
- Example response
- Response schema

```
Status: 200
```

```
{
  "default_workflow_permissions": "read",
  "can_approve_pull_request_reviews": true
}
```

## Set default workflow permissions for a repository
Sets the default workflow permissions granted to theGITHUB_TOKENwhen running workflows in a repository, and sets if GitHub Actions
can submit approving pull request reviews.
For more information, see "Setting the permissions of the GITHUB_TOKEN for your repository."
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set default workflow permissions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set default workflow permissions for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
default_workflow_permissionsstringThe default workflow permissions granted to the GITHUB_TOKEN when running workflows.Can be one of:read,write
can_approve_pull_request_reviewsbooleanWhether GitHub Actions can approve pull requests. Enabling this can be a security risk.
[/TABLE]

```
default_workflow_permissions
```
The default workflow permissions granted to the GITHUB_TOKEN when running workflows.
Can be one of:read,write

```
can_approve_pull_request_reviews
```
Whether GitHub Actions can approve pull requests. Enabling this can be a security risk.

### HTTP response status codes for "Set default workflow permissions for a repository"

[TABLE]
Status code | Description
204 | Success response
409 | Conflict response when changing a setting is prevented by the owning organization
[/TABLE]
Success response
Conflict response when changing a setting is prevented by the owning organization

### Code samples for "Set default workflow permissions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/permissions/workflow \
  -d '{"default_workflow_permissions":"read","can_approve_pull_request_reviews":true}'
```

#### Success response

```
Status: 204
```