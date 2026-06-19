# REST API endpoints for security managers

*Source: https://docs.github.com/en/rest/orgs/security-managers*

---

# REST API endpoints for security managers
Use the REST API to manage security managers in an organization.

## About security managers
The security manager role is an organization-level role that organization owners can assign to any member or team in the organization. When applied, it gives permission to view security alerts and manage settings for security features across your organization, as well as read permission for all repositories in the organization.

## List security manager teams
Warning
Closing down notice:This operation is closing down and will be removed starting January 1, 2026. Please use the "Organization Roles" endpoints instead.

### Fine-grained access tokens for "List security manager teams"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List security manager teams"

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

### HTTP response status codes for "List security manager teams"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List security manager teams"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/security-managers
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
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/organizations/1/team/1",
    "html_url": "https://github.com/orgs/github/teams/justice-league",
    "name": "Justice League",
    "slug": "justice-league",
    "description": "A great team.",
    "privacy": "closed",
    "notification_setting": "notifications_enabled",
    "permission": "admin",
    "members_url": "https://api.github.com/organizations/1/team/1/members{/member}",
    "repositories_url": "https://api.github.com/organizations/1/team/1/repos",
    "type": "organization",
    "organization_id": 1
  }
]
```

## Add a security manager team
Warning
Closing down notice:This operation is closing down and will be removed starting January 1, 2026. Please use the "Organization Roles" endpoints instead.

### Fine-grained access tokens for "Add a security manager team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Add a security manager team"

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

### HTTP response status codes for "Add a security manager team"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Add a security manager team"

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
  https://api.github.com/orgs/ORG/security-managers/teams/TEAM_SLUG
```

#### Response

```
Status: 204
```

## Remove a security manager team
Warning
Closing down notice:This operation is closing down and will be removed starting January 1, 2026. Please use the "Organization Roles" endpoints instead.

### Fine-grained access tokens for "Remove a security manager team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Remove a security manager team"

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

### HTTP response status codes for "Remove a security manager team"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove a security manager team"

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
  https://api.github.com/orgs/ORG/security-managers/teams/TEAM_SLUG
```

#### Response

```
Status: 204
```