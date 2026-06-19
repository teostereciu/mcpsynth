# REST API endpoints for Codespaces user secrets

*Source: https://docs.github.com/en/rest/codespaces/secrets*

---

# REST API endpoints for Codespaces user secrets
Use the REST API manage secrets that the user has access to in a codespace.

## About Codespaces user secrets
You can create, list, and delete secrets (such as access tokens for cloud services) as well as assign secrets to repositories that the user has access to. These secrets are made available to the codespace at runtime. For more information, seeManaging your account-specific secrets for GitHub Codespaces.

## List secrets for the authenticated user
Lists all development environment secrets available for a user's codespaces without revealing their
encrypted values.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "List secrets for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (read)

### Parameters for "List secrets for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List secrets for the authenticated user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List secrets for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/secrets
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
  "secrets": [
    {
      "name": "GH_TOKEN",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "all"
    },
    {
      "name": "GIST_ID",
      "created_at": "2020-01-10T10:59:22Z",
      "updated_at": "2020-01-11T11:59:22Z",
      "visibility": "all"
    }
  ]
}
```

## Get public key for the authenticated user
Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Get public key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (read)

### HTTP response status codes for "Get public key for the authenticated user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get public key for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/secrets/public-key
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "key_id": "012345678912345678",
  "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234"
}
```

## Get a secret for the authenticated user
Gets a development environment secret available to a user's codespaces without revealing its encrypted value.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Get a secret for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (read)

### Parameters for "Get a secret for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
[/TABLE]

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Get a secret for the authenticated user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a secret for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/secrets/SECRET_NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "CODESPACE_GH_SECRET",
  "created_at": "2019-08-10T14:59:22Z",
  "updated_at": "2020-01-10T14:59:22Z",
  "visibility": "selected",
  "selected_repositories_url": "https://api.github.com/user/codespaces/secrets/CODESPACE_GH_SECRET/repositories"
}
```

## Create or update a secret for the authenticated user
Creates or updates a development environment secret for a user's codespace with an encrypted value. Encrypt your secret usingLibSodium. For more information, see "Encrypting secrets for the REST API."
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Create or update a secret for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (write)

### Parameters for "Create or update a secret for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
[/TABLE]

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
encrypted_valuestringValue for your secret, encrypted withLibSodiumusing the public key retrieved from theGet the public key for the authenticated userendpoint.
key_idstringRequiredID of the key you used to encrypt the secret.
selected_repository_idsarrayAn array of repository ids that can access the user secret. You can manage the list of selected repositories using theList selected repositories for a user secret,Set selected repositories for a user secret, andRemove a selected repository from a user secretendpoints.
[/TABLE]

```
encrypted_value
```
Value for your secret, encrypted withLibSodiumusing the public key retrieved from theGet the public key for the authenticated userendpoint.
ID of the key you used to encrypt the secret.

```
selected_repository_ids
```
An array of repository ids that can access the user secret. You can manage the list of selected repositories using theList selected repositories for a user secret,Set selected repositories for a user secret, andRemove a selected repository from a user secretendpoints.

### HTTP response status codes for "Create or update a secret for the authenticated user"

[TABLE]
Status code | Description
201 | Response after successfully creating a secret
204 | Response after successfully updating a secret
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Response after successfully creating a secret
Response after successfully updating a secret
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create or update a secret for the authenticated user"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/secrets/SECRET_NAME \
  -d '{"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","selected_repository_ids":["1234567","2345678"]}'
```

#### Response after successfully creating a secret
- Example response
- Response schema

```
Status: 201
```

## Delete a secret for the authenticated user
Deletes a development environment secret from a user's codespaces using the secret name. Deleting the secret will remove access from all codespaces that were allowed to access the secret.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Delete a secret for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (write)

### Parameters for "Delete a secret for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
[/TABLE]

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Delete a secret for the authenticated user"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a secret for the authenticated user"

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
  https://api.github.com/user/codespaces/secrets/SECRET_NAME
```

#### Response

```
Status: 204
```

## List selected repositories for a user secret
List the repositories that have been granted the ability to use a user's development environment secret.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "List selected repositories for a user secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (read)

### Parameters for "List selected repositories for a user secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
[/TABLE]

```
secret_name
```
The name of the secret.

### HTTP response status codes for "List selected repositories for a user secret"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "List selected repositories for a user secret"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/secrets/SECRET_NAME/repositories
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
      "template_repository": {
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
        "organization": null,
        "language": null,
        "forks": 9,
        "forks_count": 9,
        "stargazers_count": 80,
        "watchers_count": 80,
        "watchers": 80,
        "size": 108,
        "default_branch": "master",
        "open_issues": 0,
        "open_issues_count": 0,
        "is_template": true,
        "license": {
          "key": "mit",
          "name": "MIT License",
          "url": "https://api.github.com/licenses/mit",
          "spdx_id": "MIT",
          "node_id": "MDc6TGljZW5zZW1pdA==",
          "html_url": "https://api.github.com/licenses/mit"
        },
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
        "network_count": 0
      },
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "delete_branch_on_merge": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA=="
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  ]
}
```

## Set selected repositories for a user secret
Select the repositories that will use a user's development environment secret.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Set selected repositories for a user secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (write)

### Parameters for "Set selected repositories for a user secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
[/TABLE]

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
selected_repository_idsarray of integersRequiredAn array of repository ids for which a codespace can access the secret. You can manage the list of selected repositories using theList selected repositories for a user secret,Add a selected repository to a user secret, andRemove a selected repository from a user secretendpoints.
[/TABLE]

```
selected_repository_ids
```
An array of repository ids for which a codespace can access the secret. You can manage the list of selected repositories using theList selected repositories for a user secret,Add a selected repository to a user secret, andRemove a selected repository from a user secretendpoints.

### HTTP response status codes for "Set selected repositories for a user secret"

[TABLE]
Status code | Description
204 | No Content when repositories were added to the selected list
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
No Content when repositories were added to the selected list
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Set selected repositories for a user secret"

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
  https://api.github.com/user/codespaces/secrets/SECRET_NAME/repositories \
  -d '{"selected_repository_ids":["1296269","1296280"]}'
```

#### No Content when repositories were added to the selected list

```
Status: 204
```

## Add a selected repository to a user secret
Adds a repository to the selected repositories for a user's development environment secret.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Add a selected repository to a user secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Add a selected repository to a user secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
repository_idintegerRequired
[/TABLE]

```
secret_name
```
The name of the secret.

```
repository_id
```

### HTTP response status codes for "Add a selected repository to a user secret"

[TABLE]
Status code | Description
204 | No Content when repository was added to the selected list
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
No Content when repository was added to the selected list
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Add a selected repository to a user secret"

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
  https://api.github.com/user/codespaces/secrets/SECRET_NAME/repositories/REPOSITORY_ID
```

#### No Content when repository was added to the selected list

```
Status: 204
```

## Remove a selected repository from a user secret
Removes a repository from the selected repositories for a user's development environment secret.
The authenticated user must have Codespaces access to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thecodespaceorcodespace:secretsscope to use this endpoint.

### Fine-grained access tokens for "Remove a selected repository from a user secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces user secrets" user permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Remove a selected repository from a user secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
secret_namestringRequiredThe name of the secret.
repository_idintegerRequired
[/TABLE]

```
secret_name
```
The name of the secret.

```
repository_id
```

### HTTP response status codes for "Remove a selected repository from a user secret"

[TABLE]
Status code | Description
204 | No Content when repository was removed from the selected list
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
No Content when repository was removed from the selected list
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Remove a selected repository from a user secret"

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
  https://api.github.com/user/codespaces/secrets/SECRET_NAME/repositories/REPOSITORY_ID
```

#### No Content when repository was removed from the selected list

```
Status: 204
```