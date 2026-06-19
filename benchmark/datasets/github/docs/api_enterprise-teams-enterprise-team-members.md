# REST API endpoints for enterprise team memberships

*Source: https://docs.github.com/en/rest/enterprise-teams/enterprise-team-members*

---

# REST API endpoints for enterprise team memberships
Use the REST API to create and manage membership of enterprise teams in your GitHub enterprise.

## About enterprise team members
Note
These endpoints are currently in public preview and subject to change.
This API documentation is for enterprises on GitHub Enterprise Cloud.
If your enterprise is Copilot Business for non-GHE, please refer to the early access documentation link that was previously shared to you.
These endpoints are only available to authenticated members of the enterprise team's enterprise with classic personal access tokens with theread:enterprisescopeforGETAPIs andadmin:enterprisefor other APIs.
These endpoints are not compatible with fine-grained personal access tokens or GitHub App access tokens.
GitHub generates the enterprise team'sslugfrom the teamnameand adds theent:prefix.

## List members in an enterprise team
Lists all team members in an enterprise team.

### Fine-grained access tokens for "List members in an enterprise team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (read)

### Parameters for "List members in an enterprise team"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List members in an enterprise team"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List members in an enterprise team"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/memberships
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

## Bulk add team members
Add multiple team members to an enterprise team.

### Fine-grained access tokens for "Bulk add team members"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Bulk add team members"

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
usernamesarray of stringsRequiredThe GitHub user handles to add to the team.
[/TABLE]
The GitHub user handles to add to the team.

### HTTP response status codes for "Bulk add team members"

[TABLE]
Status code | Description
200 | Successfully added team members.
[/TABLE]
Successfully added team members.

### Code samples for "Bulk add team members"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/memberships/add \
  -d '{"usernames":["monalisa","octocat"]}'
```

#### Successfully added team members.
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

## Bulk remove team members
Remove multiple team members from an enterprise team.

### Fine-grained access tokens for "Bulk remove team members"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Bulk remove team members"

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
usernamesarray of stringsRequiredThe GitHub user handles to be removed from the team.
[/TABLE]
The GitHub user handles to be removed from the team.

### HTTP response status codes for "Bulk remove team members"

[TABLE]
Status code | Description
200 | Successfully removed team members.
[/TABLE]
Successfully removed team members.

### Code samples for "Bulk remove team members"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/memberships/remove \
  -d '{"usernames":["monalisa","octocat"]}'
```

#### Successfully removed team members.
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

## Get enterprise team membership
Returns whether the user is a member of the enterprise team.

### Fine-grained access tokens for "Get enterprise team membership"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (read)

### Parameters for "Get enterprise team membership"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
The handle for the GitHub user account.

### HTTP response status codes for "Get enterprise team membership"

[TABLE]
Status code | Description
200 | User is a member of the enterprise team.
[/TABLE]
User is a member of the enterprise team.

### Code samples for "Get enterprise team membership"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/memberships/USERNAME
```

#### User is a member of the enterprise team.
- Example response
- Response schema

```
Status: 200
```

```
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
```

## Add team member
Add a team member to an enterprise team.

### Fine-grained access tokens for "Add team member"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Add team member"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
The handle for the GitHub user account.

### HTTP response status codes for "Add team member"

[TABLE]
Status code | Description
201 | Successfully added team member
[/TABLE]
Successfully added team member

### Code samples for "Add team member"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/memberships/USERNAME
```

#### Successfully added team member
- Example response
- Response schema

```
Status: 201
```

```
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
```

## Remove team membership
Remove membership of a specific user from a particular team in an enterprise.

### Fine-grained access tokens for "Remove team membership"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Remove team membership"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
enterprise-teamstringRequiredThe slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The slug version of the enterprise name.

```
enterprise-team
```
The slug version of the enterprise team name. You can also substitute this value with the enterprise team id.
The handle for the GitHub user account.

### HTTP response status codes for "Remove team membership"

[TABLE]
Status code | Description
204 | No Content
403 | Forbidden
[/TABLE]
No Content
Forbidden

### Code samples for "Remove team membership"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/ENTERPRISE-TEAM/memberships/USERNAME
```

#### Response

```
Status: 204
```