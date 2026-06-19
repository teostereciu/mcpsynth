# REST API endpoints for GitHub Actions variables

*Source: https://docs.github.com/en/rest/actions/variables*

---

# REST API endpoints for GitHub Actions variables
Use the REST API to interact with variables in GitHub Actions.

## About variables in GitHub Actions
You can use the REST API to create, update, delete, and retrieve information about variables that can be used in workflows in GitHub Actions. Variables allow you to store non-sensitive information, such as a username, in your repository, repository environments, or organization. For more information, seeStore information in variablesin the GitHub Actions documentation.

## List organization variables
Lists all organization variables.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "List organization variables"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (read)

### Parameters for "List organization variables"

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
per_pageintegerThe number of results per page (max 30). For more information, see "Using pagination in the REST API."Default:10
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 30). For more information, see "Using pagination in the REST API."
Default:10
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List organization variables"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List organization variables"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/variables
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 3,
  "variables": [
    {
      "name": "USERNAME",
      "value": "octocat",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "private"
    },
    {
      "name": "ACTIONS_RUNNER_DEBUG",
      "value": true,
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "all"
    },
    {
      "name": "ADMIN_EMAIL",
      "value": "octocat@github.com",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "selected",
      "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/variables/ADMIN_EMAIL/repositories"
    }
  ]
}
```

## Create an organization variable
Creates an organization variable that you can reference in a GitHub Actions workflow.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (write)

### Parameters for "Create an organization variable"

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
namestringRequiredThe name of the variable.
valuestringRequiredThe value of the variable.
visibilitystringRequiredThe type of repositories in the organization that can access the variable.selectedmeans only the repositories specified byselected_repository_idscan access the variable.Can be one of:all,private,selected
selected_repository_idsarray of integersAn array of repository ids that can access the organization variable. You can only provide a list of repository ids when thevisibilityis set toselected.
[/TABLE]
The name of the variable.
The value of the variable.
The type of repositories in the organization that can access the variable.selectedmeans only the repositories specified byselected_repository_idscan access the variable.
Can be one of:all,private,selected

```
selected_repository_ids
```
An array of repository ids that can access the organization variable. You can only provide a list of repository ids when thevisibilityis set toselected.

### HTTP response status codes for "Create an organization variable"

[TABLE]
Status code | Description
201 | Response when creating a variable
[/TABLE]
Response when creating a variable

### Code samples for "Create an organization variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/variables \
  -d '{"name":"USERNAME","value":"octocat","visibility":"selected","selected_repository_ids":[1296269,1296280]}'
```

#### Response when creating a variable
- Example response
- Response schema

```
Status: 201
```

## Get an organization variable
Gets a specific variable in an organization.
The authenticated user must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (read)

### Parameters for "Get an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

### HTTP response status codes for "Get an organization variable"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an organization variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/variables/NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "USERNAME",
  "value": "octocat",
  "created_at": "2019-08-10T14:59:22Z",
  "updated_at": "2020-01-10T14:59:22Z",
  "visibility": "selected",
  "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/variables/USERNAME/repositories"
}
```

## Update an organization variable
Updates an organization variable that you can reference in a GitHub Actions workflow.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Update an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (write)

### Parameters for "Update an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

[TABLE]
Name, Type, Description
namestringThe name of the variable.
valuestringThe value of the variable.
visibilitystringThe type of repositories in the organization that can access the variable.selectedmeans only the repositories specified byselected_repository_idscan access the variable.Can be one of:all,private,selected
selected_repository_idsarray of integersAn array of repository ids that can access the organization variable. You can only provide a list of repository ids when thevisibilityis set toselected.
[/TABLE]
The name of the variable.
The value of the variable.
The type of repositories in the organization that can access the variable.selectedmeans only the repositories specified byselected_repository_idscan access the variable.
Can be one of:all,private,selected

```
selected_repository_ids
```
An array of repository ids that can access the organization variable. You can only provide a list of repository ids when thevisibilityis set toselected.

### HTTP response status codes for "Update an organization variable"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Update an organization variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/variables/NAME \
  -d '{"name":"USERNAME","value":"octocat","visibility":"selected","selected_repository_ids":[1296269,1296280]}'
```

#### Response

```
Status: 204
```

## Delete an organization variable
Deletes an organization variable using the variable name.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (write)

### Parameters for "Delete an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

### HTTP response status codes for "Delete an organization variable"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an organization variable"

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
  https://api.github.com/orgs/ORG/actions/variables/NAME
```

#### Response

```
Status: 204
```

## List selected repositories for an organization variable
Lists all repositories that can access an organization variable
that is available to selected repositories.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "List selected repositories for an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (read)

### Parameters for "List selected repositories for an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

[TABLE]
Name, Type, Description
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List selected repositories for an organization variable"

[TABLE]
Status code | Description
200 | OK
409 | Response when the visibility of the variable is not set toselected
[/TABLE]
OK
Response when the visibility of the variable is not set toselected

### Code samples for "List selected repositories for an organization variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/variables/NAME/repositories
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
      "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
    }
  ]
}
```

## Set selected repositories for an organization variable
Replaces all repositories for an organization variable that is available
to selected repositories. Organization variables that are available to selected
repositories have theirvisibilityfield set toselected.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Set selected repositories for an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (write)

### Parameters for "Set selected repositories for an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

[TABLE]
Name, Type, Description
selected_repository_idsarray of integersRequiredThe IDs of the repositories that can access the organization variable.
[/TABLE]

```
selected_repository_ids
```
The IDs of the repositories that can access the organization variable.

### HTTP response status codes for "Set selected repositories for an organization variable"

[TABLE]
Status code | Description
204 | No Content
409 | Response when the visibility of the variable is not set toselected
[/TABLE]
No Content
Response when the visibility of the variable is not set toselected

### Code samples for "Set selected repositories for an organization variable"

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
  https://api.github.com/orgs/ORG/actions/variables/NAME/repositories \
  -d '{"selected_repository_ids":[64780797]}'
```

#### Response

```
Status: 204
```

## Add selected repository to an organization variable
Adds a repository to an organization variable that is available to selected repositories.
Organization variables that are available to selected repositories have theirvisibilityfield set toselected.
Authenticated users must have collaborator access to a repository to create, update, or read secrets.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Add selected repository to an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Add selected repository to an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
repository_idintegerRequired
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

```
repository_id
```

### HTTP response status codes for "Add selected repository to an organization variable"

[TABLE]
Status code | Description
204 | No Content
409 | Response when the visibility of the variable is not set toselected
[/TABLE]
No Content
Response when the visibility of the variable is not set toselected

### Code samples for "Add selected repository to an organization variable"

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
  https://api.github.com/orgs/ORG/actions/variables/NAME/repositories/REPOSITORY_ID
```

#### Response

```
Status: 204
```

## Remove selected repository from an organization variable
Removes a repository from an organization variable that is
available to selected repositories. Organization variables that are available to
selected repositories have theirvisibilityfield set toselected.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Remove selected repository from an organization variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Remove selected repository from an organization variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
namestringRequiredThe name of the variable.
repository_idintegerRequired
[/TABLE]
The organization name. The name is not case sensitive.
The name of the variable.

```
repository_id
```

### HTTP response status codes for "Remove selected repository from an organization variable"

[TABLE]
Status code | Description
204 | No Content
409 | Response when the visibility of the variable is not set toselected
[/TABLE]
No Content
Response when the visibility of the variable is not set toselected

### Code samples for "Remove selected repository from an organization variable"

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
  https://api.github.com/orgs/ORG/actions/variables/NAME/repositories/REPOSITORY_ID
```

#### Response

```
Status: 204
```

## List repository organization variables
Lists all organization variables shared with a repository.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List repository organization variables"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" repository permissions (read)

### Parameters for "List repository organization variables"

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
per_pageintegerThe number of results per page (max 30). For more information, see "Using pagination in the REST API."Default:10
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 30). For more information, see "Using pagination in the REST API."
Default:10
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repository organization variables"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository organization variables"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/organization-variables
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "variables": [
    {
      "name": "USERNAME",
      "value": "octocat",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z"
    },
    {
      "name": "EMAIL",
      "value": "octocat@github.com",
      "created_at": "2020-01-10T10:59:22Z",
      "updated_at": "2020-01-11T11:59:22Z"
    }
  ]
}
```

## List repository variables
Lists all repository variables.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List repository variables"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" repository permissions (read)

### Parameters for "List repository variables"

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
per_pageintegerThe number of results per page (max 30). For more information, see "Using pagination in the REST API."Default:10
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 30). For more information, see "Using pagination in the REST API."
Default:10
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repository variables"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository variables"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/variables
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "variables": [
    {
      "name": "USERNAME",
      "value": "octocat",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z"
    },
    {
      "name": "EMAIL",
      "value": "octocat@github.com",
      "created_at": "2020-01-10T10:59:22Z",
      "updated_at": "2020-01-11T11:59:22Z"
    }
  ]
}
```

## Create a repository variable
Creates a repository variable that you can reference in a GitHub Actions workflow.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a repository variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" repository permissions (write)

### Parameters for "Create a repository variable"

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
namestringRequiredThe name of the variable.
valuestringRequiredThe value of the variable.
[/TABLE]
The name of the variable.
The value of the variable.

### HTTP response status codes for "Create a repository variable"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a repository variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/variables \
  -d '{"name":"USERNAME","value":"octocat"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## Get a repository variable
Gets a specific variable in a repository.
The authenticated user must have collaborator access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get a repository variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" repository permissions (read)

### Parameters for "Get a repository variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The name of the variable.

### HTTP response status codes for "Get a repository variable"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a repository variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/variables/NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "USERNAME",
  "value": "octocat",
  "created_at": "2021-08-10T14:59:22Z",
  "updated_at": "2022-01-10T14:59:22Z"
}
```

## Update a repository variable
Updates a repository variable that you can reference in a GitHub Actions workflow.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Update a repository variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" repository permissions (write)

### Parameters for "Update a repository variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The name of the variable.

[TABLE]
Name, Type, Description
namestringThe name of the variable.
valuestringThe value of the variable.
[/TABLE]
The name of the variable.
The value of the variable.

### HTTP response status codes for "Update a repository variable"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Update a repository variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/variables/NAME \
  -d '{"name":"USERNAME","value":"octocat"}'
```

#### Response

```
Status: 204
```

## Delete a repository variable
Deletes a repository variable using the variable name.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a repository variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Variables" repository permissions (write)

### Parameters for "Delete a repository variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequiredThe name of the variable.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The name of the variable.

### HTTP response status codes for "Delete a repository variable"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a repository variable"

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
  https://api.github.com/repos/OWNER/REPO/actions/variables/NAME
```

#### Response

```
Status: 204
```

## List environment variables
Lists all environment variables.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List environment variables"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Environments" repository permissions (read)

### Parameters for "List environment variables"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 30). For more information, see "Using pagination in the REST API."Default:10
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 30). For more information, see "Using pagination in the REST API."
Default:10
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List environment variables"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List environment variables"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/variables
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "variables": [
    {
      "name": "USERNAME",
      "value": "octocat",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z"
    },
    {
      "name": "EMAIL",
      "value": "octocat@github.com",
      "created_at": "2020-01-10T10:59:22Z",
      "updated_at": "2020-01-11T11:59:22Z"
    }
  ]
}
```

## Create an environment variable
Create an environment variable that you can reference in a GitHub Actions workflow.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create an environment variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Environments" repository permissions (write)

### Parameters for "Create an environment variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the variable.
valuestringRequiredThe value of the variable.
[/TABLE]
The name of the variable.
The value of the variable.

### HTTP response status codes for "Create an environment variable"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create an environment variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/variables \
  -d '{"name":"USERNAME","value":"octocat"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## Get an environment variable
Gets a specific variable in an environment.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get an environment variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Environments" repository permissions (read)

### Parameters for "Get an environment variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
namestringRequiredThe name of the variable.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
The name of the variable.

### HTTP response status codes for "Get an environment variable"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an environment variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/variables/NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "USERNAME",
  "value": "octocat",
  "created_at": "2021-08-10T14:59:22Z",
  "updated_at": "2022-01-10T14:59:22Z"
}
```

## Update an environment variable
Updates an environment variable that you can reference in a GitHub Actions workflow.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Update an environment variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Environments" repository permissions (write)

### Parameters for "Update an environment variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequiredThe name of the variable.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The name of the variable.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

[TABLE]
Name, Type, Description
namestringThe name of the variable.
valuestringThe value of the variable.
[/TABLE]
The name of the variable.
The value of the variable.

### HTTP response status codes for "Update an environment variable"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Update an environment variable"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/variables/NAME \
  -d '{"name":"USERNAME","value":"octocat"}'
```

#### Response

```
Status: 204
```

## Delete an environment variable
Deletes an environment variable using the variable name.
Authenticated users must have collaborator access to a repository to create, update, or read variables.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete an environment variable"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Environments" repository permissions (write)

### Parameters for "Delete an environment variable"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequiredThe name of the variable.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The name of the variable.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

### HTTP response status codes for "Delete an environment variable"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an environment variable"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/variables/NAME
```

#### Response

```
Status: 204
```