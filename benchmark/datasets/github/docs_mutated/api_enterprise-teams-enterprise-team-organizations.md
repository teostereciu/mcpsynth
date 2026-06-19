# REST API endpoints for enterprise team organizations

*Source: https://docs.github.com/en/rest/enterprise-teams/enterprise-team-organizations*

---

# REST API endpoints for enterprise team organizations
Use the REST API to create and manage organization assignments for enterprise teams in your GitHub enterprise.

## About enterprise team organizations
Note
These endpoints are currently in public preview and subject to change.
This API documentation is for enterprises on GitHub Enterprise Cloud.
If your enterprise is Copilot Business for non-GHE, please refer to the early access documentation link that was previously shared to you.
These endpoints are only available to authenticated members of the enterprise team's enterprise with classic personal access tokens with theread:enterprisescopeforGETAPIs andadmin:enterprisefor other APIs.
These endpoints are not compatible with fine-grained personal access tokens or GitHub App access tokens.
GitHub generates the enterprise team'sslugfrom the teamnameand adds theent:prefix.

## Get organization assignments
Get all organizations assigned to an enterprise team

### Fine-grained access tokens for "Get organization assignments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (read)

### Parameters for "Get organization assignments"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "Get organization assignments"

[TABLE]
Status code | Description
200 | An array of organizations the team is assigned to
[/TABLE]
An array of organizations the team is assigned to

### Code samples for "Get organization assignments"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/organizations
```

#### An array of organizations the team is assigned to
- Example response
- Response schema

```
Status: 200
```

```
{
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
}
```

## Add organization assignments
Assign an enterprise team to multiple organizations.

### Fine-grained access tokens for "Add organization assignments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Add organization assignments"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.

[TABLE]
Name, Type, Description
organization_slugsarray of stringsRequiredOrganization slug to assign the team to.
[/TABLE]

```
organization_slugs
```
Organization slug to assign the team to.

### HTTP response status codes for "Add organization assignments"

[TABLE]
Status code | Description
200 | Successfully assigned the enterprise team to organizations.
[/TABLE]
Successfully assigned the enterprise team to organizations.

### Code samples for "Add organization assignments"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/organizations/add \
  -d '{"organization_slugs":["github"]}'
```

#### Successfully assigned the enterprise team to organizations.
- Example response
- Response schema

```
Status: 200
```

```
[
  {
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
  }
]
```

## Remove organization assignments
Unassign an enterprise team from multiple organizations.

### Fine-grained access tokens for "Remove organization assignments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Remove organization assignments"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.

[TABLE]
Name, Type, Description
organization_slugsarray of stringsRequiredOrganization slug to unassign the team from.
[/TABLE]

```
organization_slugs
```
Organization slug to unassign the team from.

### HTTP response status codes for "Remove organization assignments"

[TABLE]
Status code | Description
204 | Successfully unassigned the enterprise team from organizations.
[/TABLE]
Successfully unassigned the enterprise team from organizations.

### Code samples for "Remove organization assignments"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/organizations/remove \
  -d '{"organization_slugs":["github"]}'
```

#### Successfully unassigned the enterprise team from organizations.

```
Status: 204
```

## Get organization assignment
Check if an enterprise team is assigned to an organization

### Fine-grained access tokens for "Get organization assignment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (read)

### Parameters for "Get organization assignment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
The organization name. The name is not case sensitive.

### HTTP response status codes for "Get organization assignment"

[TABLE]
Status code | Description
200 | The team is assigned to the organization
404 | The team is not assigned to the organization
[/TABLE]
The team is assigned to the organization
The team is not assigned to the organization

### Code samples for "Get organization assignment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/organizations/ORG
```

#### The team is assigned to the organization
- Example response
- Response schema

```
Status: 200
```

```
{
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
}
```

## Add an organization assignment
Assign an enterprise team to an organization.

### Fine-grained access tokens for "Add an organization assignment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Add an organization assignment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
The organization name. The name is not case sensitive.

### HTTP response status codes for "Add an organization assignment"

[TABLE]
Status code | Description
201 | Successfully assigned the enterprise team to the organization.
[/TABLE]
Successfully assigned the enterprise team to the organization.

### Code samples for "Add an organization assignment"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/organizations/ORG
```

#### Successfully assigned the enterprise team to the organization.
- Example response
- Response schema

```
Status: 201
```

```
{
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
}
```

## Delete an organization assignment
Unassign an enterprise team from an organization.

### Fine-grained access tokens for "Delete an organization assignment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Delete an organization assignment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
The organization name. The name is not case sensitive.

### HTTP response status codes for "Delete an organization assignment"

[TABLE]
Status code | Description
204 | Successfully unassigned the enterprise team from the organization.
[/TABLE]
Successfully unassigned the enterprise team from the organization.

### Code samples for "Delete an organization assignment"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/organizations/ORG
```

#### Successfully unassigned the enterprise team from the organization.

```
Status: 204
```