# REST API endpoints for Dependabot secrets

*Source: https://docs.github.com/en/rest/dependabot/secrets*

---

# REST API endpoints for Dependabot secrets
Use the REST API to manage Dependabot secrets for an organization or repository.

## About Dependabot secrets
You can create, update, delete, and retrieve information about encrypted secrets using the REST API. Secrets allow you to store sensitive information, such as access tokens, in your repository, repository environments, or organization. For more information, seeConfiguring access to private registries for Dependabot.
These endpoints are available for authenticated users, OAuth apps, and GitHub Apps. Access tokens requirereposcopefor private repositories andpublic_reposcopefor public repositories. GitHub Apps must have thedependabot_secretspermission to use these endpoints. Authenticated users must have collaborator access to a repository to create, update, or read secrets.

```
public_repo
```

## List organization secrets
Lists all secrets available in an organization without revealing their
encrypted values.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List organization secrets"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (read)

### Parameters for "List organization secrets"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List organization secrets"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List organization secrets"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/dependabot/secrets
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
  "secrets": [
    {
      "name": "MY_ARTIFACTORY_PASSWORD",
      "created_at": "2021-08-10T14:59:22Z",
      "updated_at": "2021-12-10T14:59:22Z",
      "visibility": "private"
    },
    {
      "name": "NPM_TOKEN",
      "created_at": "2021-08-10T14:59:22Z",
      "updated_at": "2021-12-10T14:59:22Z",
      "visibility": "all"
    },
    {
      "name": "GH_TOKEN",
      "created_at": "2021-08-10T14:59:22Z",
      "updated_at": "2021-12-10T14:59:22Z",
      "visibility": "selected",
      "selected_repositories_url": "https://api.github.com/orgs/octo-org/dependabot/secrets/SUPER_SECRET/repositories"
    }
  ]
}
```

## Get an organization public key
Gets your public key, which you need to encrypt secrets. You need to
encrypt a secret before you can create or update secrets.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get an organization public key"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (read)

### Parameters for "Get an organization public key"

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

### HTTP response status codes for "Get an organization public key"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an organization public key"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/dependabot/secrets/public-key
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

## Get an organization secret
Gets a single organization secret without revealing its encrypted value.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (read)

### Parameters for "Get an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Get an organization secret"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an organization secret"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "NPM_TOKEN",
  "created_at": "2019-08-10T14:59:22Z",
  "updated_at": "2020-01-10T14:59:22Z",
  "visibility": "selected",
  "selected_repositories_url": "https://api.github.com/orgs/octo-org/dependabot/secrets/NPM_TOKEN/repositories"
}
```

## Create or update an organization secret
Creates or updates an organization secret with an encrypted value. Encrypt your secret usingLibSodium. For more information, see "Encrypting secrets for the REST API."
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Create or update an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (write)

### Parameters for "Create or update an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
encrypted_valuestringValue for your secret, encrypted withLibSodiumusing the public key retrieved from theGet an organization public keyendpoint.
key_idstringID of the key you used to encrypt the secret.
visibilitystringRequiredWhich type of organization repositories have access to the organization secret.selectedmeans only the repositories specified byselected_repository_idscan access the secret.Can be one of:all,private,selected
selected_repository_idsarray of integersAn array of repository ids that can access the organization secret. You can only provide a list of repository ids when thevisibilityis set toselected. You can manage the list of selected repositories using theList selected repositories for an organization secret,Set selected repositories for an organization secret, andRemove selected repository from an organization secretendpoints.
[/TABLE]

```
encrypted_value
```
Value for your secret, encrypted withLibSodiumusing the public key retrieved from theGet an organization public keyendpoint.
ID of the key you used to encrypt the secret.
Which type of organization repositories have access to the organization secret.selectedmeans only the repositories specified byselected_repository_idscan access the secret.
Can be one of:all,private,selected

```
selected_repository_ids
```
An array of repository ids that can access the organization secret. You can only provide a list of repository ids when thevisibilityis set toselected. You can manage the list of selected repositories using theList selected repositories for an organization secret,Set selected repositories for an organization secret, andRemove selected repository from an organization secretendpoints.

### HTTP response status codes for "Create or update an organization secret"

[TABLE]
Status code | Description
201 | Response when creating a secret
204 | Response when updating a secret
[/TABLE]
Response when creating a secret
Response when updating a secret

### Code samples for "Create or update an organization secret"

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
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME \
  -d '{"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","visibility":"selected","selected_repository_ids":[1296269,1296280]}'
```

#### Response when creating a secret
- Example response
- Response schema

```
Status: 201
```

## Delete an organization secret
Deletes a secret in an organization using the secret name.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (write)

### Parameters for "Delete an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Delete an organization secret"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an organization secret"

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
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME
```

#### Response

```
Status: 204
```

## List selected repositories for an organization secret
Lists all repositories that have been selected when thevisibilityfor repository access to a secret is set toselected.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List selected repositories for an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (read)

### Parameters for "List selected repositories for an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List selected repositories for an organization secret"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List selected repositories for an organization secret"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME/repositories
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
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
      "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
    }
  ]
}
```

## Set selected repositories for an organization secret
Replaces all repositories for an organization secret when thevisibilityfor repository access is set toselected. The visibility is set when youCreate
or update an organization secret.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set selected repositories for an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (write)

### Parameters for "Set selected repositories for an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
selected_repository_idsarray of integersRequiredAn array of repository ids that can access the organization secret. You can only provide a list of repository ids when thevisibilityis set toselected. You can add and remove individual repositories using theSet selected repositories for an organization secretandRemove selected repository from an organization secretendpoints.
[/TABLE]

```
selected_repository_ids
```
An array of repository ids that can access the organization secret. You can only provide a list of repository ids when thevisibilityis set toselected. You can add and remove individual repositories using theSet selected repositories for an organization secretandRemove selected repository from an organization secretendpoints.

### HTTP response status codes for "Set selected repositories for an organization secret"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set selected repositories for an organization secret"

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
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME/repositories \
  -d '{"selected_repository_ids":[64780797]}'
```

#### Response

```
Status: 204
```

## Add selected repository to an organization secret
Adds a repository to an organization secret when thevisibilityfor
repository access is set toselected. The visibility is set when youCreate or
update an organization secret.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Add selected repository to an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Add selected repository to an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
repository_idintegerRequired
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

```
repository_id
```

### HTTP response status codes for "Add selected repository to an organization secret"

[TABLE]
Status code | Description
204 | No Content when repository was added to the selected list
409 | Conflict when visibility type is not set to selected
[/TABLE]
No Content when repository was added to the selected list
Conflict when visibility type is not set to selected

### Code samples for "Add selected repository to an organization secret"

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
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME/repositories/REPOSITORY_ID
```

#### No Content when repository was added to the selected list

```
Status: 204
```

## Remove selected repository from an organization secret
Removes a repository from an organization secret when thevisibilityfor repository access is set toselected. The visibility is set when youCreate
or update an organization secret.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove selected repository from an organization secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Organization dependabot secrets" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Remove selected repository from an organization secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
repository_idintegerRequired
[/TABLE]
The organization name. The name is not case sensitive.

```
secret_name
```
The name of the secret.

```
repository_id
```

### HTTP response status codes for "Remove selected repository from an organization secret"

[TABLE]
Status code | Description
204 | Response when repository was removed from the selected list
409 | Conflict when visibility type not set to selected
[/TABLE]
Response when repository was removed from the selected list
Conflict when visibility type not set to selected

### Code samples for "Remove selected repository from an organization secret"

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
  https://api.github.com/orgs/ORG/dependabot/secrets/SECRET_NAME/repositories/REPOSITORY_ID
```

#### Response when repository was removed from the selected list

```
Status: 204
```

## List repository secrets
Lists all secrets available in a repository without revealing their encrypted
values.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List repository secrets"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot secrets" repository permissions (read)

### Parameters for "List repository secrets"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repository secrets"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository secrets"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependabot/secrets
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
      "name": "AZURE_DEVOPS_PAT",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z"
    },
    {
      "name": "MY_ARTIFACTORY_PASSWORD",
      "created_at": "2020-01-10T10:59:22Z",
      "updated_at": "2020-01-11T11:59:22Z"
    }
  ]
}
```

## Get a repository public key
Gets your public key, which you need to encrypt secrets. You need to
encrypt a secret before you can create or update secrets. Anyone with read access
to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint if the repository is private.

### Fine-grained access tokens for "Get a repository public key"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot secrets" repository permissions (read)

### Parameters for "Get a repository public key"

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

### HTTP response status codes for "Get a repository public key"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a repository public key"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependabot/secrets/public-key
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

## Get a repository secret
Gets a single repository secret without revealing its encrypted value.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get a repository secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot secrets" repository permissions (read)

### Parameters for "Get a repository secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Get a repository secret"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a repository secret"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependabot/secrets/SECRET_NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "MY_ARTIFACTORY_PASSWORD",
  "created_at": "2019-08-10T14:59:22Z",
  "updated_at": "2020-01-10T14:59:22Z"
}
```

## Create or update a repository secret
Creates or updates a repository secret with an encrypted value. Encrypt your secret usingLibSodium. For more information, see "Encrypting secrets for the REST API."
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create or update a repository secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot secrets" repository permissions (write)

### Parameters for "Create or update a repository secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
encrypted_valuestringValue for your secret, encrypted withLibSodiumusing the public key retrieved from theGet a repository public keyendpoint.
key_idstringID of the key you used to encrypt the secret.
[/TABLE]

```
encrypted_value
```
Value for your secret, encrypted withLibSodiumusing the public key retrieved from theGet a repository public keyendpoint.
ID of the key you used to encrypt the secret.

### HTTP response status codes for "Create or update a repository secret"

[TABLE]
Status code | Description
201 | Response when creating a secret
204 | Response when updating a secret
[/TABLE]
Response when creating a secret
Response when updating a secret

### Code samples for "Create or update a repository secret"

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
  https://api.github.com/repos/OWNER/REPO/dependabot/secrets/SECRET_NAME \
  -d '{"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"}'
```

#### Response when creating a secret
- Example response
- Response schema

```
Status: 201
```

## Delete a repository secret
Deletes a secret in a repository using the secret name.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a repository secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot secrets" repository permissions (write)

### Parameters for "Delete a repository secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Delete a repository secret"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a repository secret"

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
  https://api.github.com/repos/OWNER/REPO/dependabot/secrets/SECRET_NAME
```

#### Response

```
Status: 204
```