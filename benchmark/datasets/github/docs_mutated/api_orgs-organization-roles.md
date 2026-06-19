# REST API endpoints for organization roles

*Source: https://docs.github.com/en/rest/orgs/organization-roles*

---

# REST API endpoints for organization roles
Use the REST API to interact with organization roles.

## Get all organization roles for an organization
Lists the organization roles available in this organization. For more information on organization roles, see "Using organization roles."
To use this endpoint, the authenticated user must be one of:
- An administrator for the organization.
- A user, or a user on a team, with the fine-grained permissions ofread_organization_custom_org_rolein the organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get all organization roles for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom organization roles" organization permissions (read)

### Parameters for "Get all organization roles for an organization"

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

### HTTP response status codes for "Get all organization roles for an organization"

[TABLE]
Status code | Description
200 | Response - list of organization roles
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Response - list of organization roles
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Get all organization roles for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/organization-roles
```

#### Response - list of organization roles
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "roles": [
    {
      "id": 8030,
      "name": "Custom Role Manager",
      "description": "Permissions to manage custom roles within an org",
      "permissions": [
        "write_organization_custom_repo_role",
        "write_organization_custom_org_role",
        "read_organization_custom_repo_role",
        "read_organization_custom_org_role"
      ],
      "organization": {
        "login": "github",
        "id": 9919,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjk5MTk=",
        "avatar_url": "https://avatars.githubusercontent.com/u/9919?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/github",
        "html_url": "https://github.com/github",
        "followers_url": "https://api.github.com/users/github/followers",
        "following_url": "https://api.github.com/users/github/following{/other_user}",
        "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/github/subscriptions",
        "organizations_url": "https://api.github.com/users/github/orgs",
        "repos_url": "https://api.github.com/users/github/repos",
        "events_url": "https://api.github.com/users/github/events{/privacy}",
        "received_events_url": "https://api.github.com/users/github/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "created_at": "2022-07-04T22:19:11Z",
      "updated_at": "2022-07-04T22:20:11Z"
    },
    {
      "id": 8031,
      "name": "Auditor",
      "description": "Permissions to read the organization audit log",
      "permissions": [
        "read_audit_logs"
      ],
      "organization": {
        "login": "github",
        "id": 9919,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjk5MTk=",
        "avatar_url": "https://avatars.githubusercontent.com/u/9919?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/github",
        "html_url": "https://github.com/github",
        "followers_url": "https://api.github.com/users/github/followers",
        "following_url": "https://api.github.com/users/github/following{/other_user}",
        "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/github/subscriptions",
        "organizations_url": "https://api.github.com/users/github/orgs",
        "repos_url": "https://api.github.com/users/github/repos",
        "events_url": "https://api.github.com/users/github/events{/privacy}",
        "received_events_url": "https://api.github.com/users/github/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "created_at": "2022-07-04T22:19:11Z",
      "updated_at": "2022-07-04T22:20:11Z"
    }
  ]
}
```

## Remove all organization roles for a team
Removes all assigned organization roles from a team. For more information on organization roles, see "Using organization roles."
The authenticated user must be an administrator for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove all organization roles for a team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove all organization roles for a team"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.

### HTTP response status codes for "Remove all organization roles for a team"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove all organization roles for a team"

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
  https://api.github.com/orgs/ORG/organization-roles/teams/TEAM_SLUG
```

#### Response

```
Status: 204
```

## Assign an organization role to a team
Assigns an organization role to a team in an organization. For more information on organization roles, see "Using organization roles."
The authenticated user must be an administrator for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Assign an organization role to a team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Assign an organization role to a team"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.
The unique identifier of the role.

### HTTP response status codes for "Assign an organization role to a team"

[TABLE]
Status code | Description
204 | No Content
404 | Response if the organization, team or role does not exist.
422 | Response if the organization roles feature is not enabled for the organization, or validation failed.
[/TABLE]
No Content
Response if the organization, team or role does not exist.
Response if the organization roles feature is not enabled for the organization, or validation failed.

### Code samples for "Assign an organization role to a team"

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
  https://api.github.com/orgs/ORG/organization-roles/teams/TEAM_SLUG/ROLE_ID
```

#### Response

```
Status: 204
```

## Remove an organization role from a team
Removes an organization role from a team. For more information on organization roles, see "Using organization roles."
The authenticated user must be an administrator for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove an organization role from a team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove an organization role from a team"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.
The unique identifier of the role.

### HTTP response status codes for "Remove an organization role from a team"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove an organization role from a team"

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
  https://api.github.com/orgs/ORG/organization-roles/teams/TEAM_SLUG/ROLE_ID
```

#### Response

```
Status: 204
```

## Remove all organization roles for a user
Revokes all assigned organization roles from a user. For more information on organization roles, see "Using organization roles."
The authenticated user must be an administrator for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove all organization roles for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove all organization roles for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The organization name. The name is not case sensitive.
The handle for the GitHub user account.

### HTTP response status codes for "Remove all organization roles for a user"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove all organization roles for a user"

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
  https://api.github.com/orgs/ORG/organization-roles/users/USERNAME
```

#### Response

```
Status: 204
```

## Assign an organization role to a user
Assigns an organization role to a member of an organization. For more information on organization roles, see "Using organization roles."
The authenticated user must be an administrator for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Assign an organization role to a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Assign an organization role to a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
usernamestringRequiredThe handle for the GitHub user account.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The handle for the GitHub user account.
The unique identifier of the role.

### HTTP response status codes for "Assign an organization role to a user"

[TABLE]
Status code | Description
204 | No Content
404 | Response if the organization, user or role does not exist.
422 | Response if the organization roles feature is not enabled enabled for the organization, the validation failed, or the user is not an organization member.
[/TABLE]
No Content
Response if the organization, user or role does not exist.
Response if the organization roles feature is not enabled enabled for the organization, the validation failed, or the user is not an organization member.

### Code samples for "Assign an organization role to a user"

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
  https://api.github.com/orgs/ORG/organization-roles/users/USERNAME/ROLE_ID
```

#### Response

```
Status: 204
```

## Remove an organization role from a user
Remove an organization role from a user. For more information on organization roles, see "Using organization roles."
The authenticated user must be an administrator for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove an organization role from a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove an organization role from a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
usernamestringRequiredThe handle for the GitHub user account.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The handle for the GitHub user account.
The unique identifier of the role.

### HTTP response status codes for "Remove an organization role from a user"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove an organization role from a user"

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
  https://api.github.com/orgs/ORG/organization-roles/users/USERNAME/ROLE_ID
```

#### Response

```
Status: 204
```

## Get an organization role
Gets an organization role that is available to this organization. For more information on organization roles, see "Using organization roles."
To use this endpoint, the authenticated user must be one of:
- An administrator for the organization.
- A user, or a user on a team, with the fine-grained permissions ofread_organization_custom_org_rolein the organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get an organization role"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom organization roles" organization permissions (read)

### Parameters for "Get an organization role"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the role.

### HTTP response status codes for "Get an organization role"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Get an organization role"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/organization-roles/ROLE_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 8030,
  "name": "Custom Role Manager",
  "description": "Permissions to manage custom roles within an org",
  "permissions": [
    "write_organization_custom_repo_role",
    "write_organization_custom_org_role",
    "read_organization_custom_repo_role",
    "read_organization_custom_org_role"
  ],
  "organization": {
    "login": "github",
    "id": 1,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "url": "https://api.github.com/orgs/github",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "events_url": "https://api.github.com/orgs/github/events",
    "hooks_url": "https://api.github.com/orgs/github/hooks",
    "issues_url": "https://api.github.com/orgs/github/issues",
    "members_url": "https://api.github.com/orgs/github/members{/member}",
    "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "description": "A great organization"
  },
  "created_at": "2022-07-04T22:19:11Z",
  "updated_at": "2022-07-04T22:20:11Z"
}
```

## List teams that are assigned to an organization role
Lists the teams that are assigned to an organization role. For more information on organization roles, see "Using organization roles."
To use this endpoint, you must be an administrator for the organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List teams that are assigned to an organization role"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List teams that are assigned to an organization role"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the role.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List teams that are assigned to an organization role"

[TABLE]
Status code | Description
200 | Response - List of assigned teams
404 | Response if the organization or role does not exist.
422 | Response if the organization roles feature is not enabled or validation failed.
[/TABLE]
Response - List of assigned teams
Response if the organization or role does not exist.
Response if the organization roles feature is not enabled or validation failed.

### Code samples for "List teams that are assigned to an organization role"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/organization-roles/ROLE_ID/teams
```

#### Response - List of assigned teams
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/teams/1",
    "html_url": "https://github.com/orgs/github/teams/justice-league",
    "name": "Justice League",
    "slug": "justice-league",
    "description": "A great team.",
    "privacy": "closed",
    "notification_setting": "notifications_enabled",
    "permission": "admin",
    "members_url": "https://api.github.com/teams/1/members{/member}",
    "repositories_url": "https://api.github.com/teams/1/repos",
    "parent": null
  }
]
```

## List users that are assigned to an organization role
Lists organization members that are assigned to an organization role. For more information on organization roles, see "Using organization roles."
To use this endpoint, you must be an administrator for the organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List users that are assigned to an organization role"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List users that are assigned to an organization role"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
role_idintegerRequiredThe unique identifier of the role.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the role.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List users that are assigned to an organization role"

[TABLE]
Status code | Description
200 | Response - List of assigned users
404 | Response if the organization or role does not exist.
422 | Response if the organization roles feature is not enabled or validation failed.
[/TABLE]
Response - List of assigned users
Response if the organization or role does not exist.
Response if the organization roles feature is not enabled or validation failed.

### Code samples for "List users that are assigned to an organization role"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/organization-roles/ROLE_ID/users
```

#### Response - List of assigned users
- Example response
- Response schema

```
Status: 200
```

```
[
  {
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
  }
]
```