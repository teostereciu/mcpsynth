# REST API endpoints for blocking users

*Source: https://docs.github.com/en/rest/orgs/blocking*

---

# REST API endpoints for blocking users
Use the REST API to block and unblock users in an organization.

## About blocking users
The token used to authenticate the call must have theadmin:orgscope in order to make any blocking calls for an organization. Otherwise, the response returnsHTTP 404.

## List users blocked by an organization
List the users blocked by an organization.

### Fine-grained access tokens for "List users blocked by an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Blocking users" organization permissions (read)

### Parameters for "List users blocked by an organization"

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

### HTTP response status codes for "List users blocked by an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List users blocked by an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/blocks
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

## Check if a user is blocked by an organization
Returns a 204 if the given user is blocked by the given organization. Returns a 404 if the organization is not blocking the user, or if the user account has been identified as spam by GitHub.

### Fine-grained access tokens for "Check if a user is blocked by an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Blocking users" organization permissions (read)

### Parameters for "Check if a user is blocked by an organization"

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

### HTTP response status codes for "Check if a user is blocked by an organization"

[TABLE]
Status code | Description
204 | If the user is blocked
404 | If the user is not blocked
[/TABLE]
If the user is blocked
If the user is not blocked

### Code samples for "Check if a user is blocked by an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/blocks/USERNAME
```

#### If the user is blocked

```
Status: 204
```

## Block a user from an organization
Blocks the given user on behalf of the specified organization and returns a 204. If the organization cannot block the given user a 422 is returned.

### Fine-grained access tokens for "Block a user from an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Blocking users" organization permissions (write)

### Parameters for "Block a user from an organization"

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

### HTTP response status codes for "Block a user from an organization"

[TABLE]
Status code | Description
204 | No Content
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Validation failed, or the endpoint has been spammed.

### Code samples for "Block a user from an organization"

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
  https://api.github.com/orgs/ORG/blocks/USERNAME
```

#### Response

```
Status: 204
```

## Unblock a user from an organization
Unblocks the given user on behalf of the specified organization.

### Fine-grained access tokens for "Unblock a user from an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Blocking users" organization permissions (write)

### Parameters for "Unblock a user from an organization"

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

### HTTP response status codes for "Unblock a user from an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Unblock a user from an organization"

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
  https://api.github.com/orgs/ORG/blocks/USERNAME
```

#### Response

```
Status: 204
```