# REST API endpoints for social accounts

*Source: https://docs.github.com/en/rest/users/social-accounts*

---

# REST API endpoints for social accounts
Use the REST API to manage social accounts of authenticated users.

## About social account administration
If a request URL does not include a{username}parameter then the response will be for the signed-in user (and you must passauthentication informationwith your request). Additional private information, such as whether a user has two-factor authentication enabled, is included when authenticated through OAuth with theuserscope.

## List social accounts for the authenticated user
Lists all of your social accounts.

### Fine-grained access tokens for "List social accounts for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List social accounts for the authenticated user"

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

### HTTP response status codes for "List social accounts for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found

### Code samples for "List social accounts for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/social_accounts
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
    "provider": "twitter",
    "url": "https://twitter.com/github"
  }
]
```

## Add social accounts for the authenticated user
Add one or more social accounts to the authenticated user's profile.
OAuth app tokens and personal access tokens (classic) need theuserscope to use this endpoint.

### Fine-grained access tokens for "Add social accounts for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Profile" user permissions (write)

### Parameters for "Add social accounts for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
account_urlsarray of stringsRequiredFull URLs for the social media profiles to add.
[/TABLE]

```
account_urls
```
Full URLs for the social media profiles to add.

### HTTP response status codes for "Add social accounts for the authenticated user"

[TABLE]
Status code | Description
201 | Created
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Add social accounts for the authenticated user"

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
  https://api.github.com/user/social_accounts \
  -d '{"account_urls":["https://facebook.com/GitHub","https://www.youtube.com/@GitHub"]}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
[
  {
    "provider": "twitter",
    "url": "https://twitter.com/github"
  }
]
```

## Delete social accounts for the authenticated user
Deletes one or more social accounts from the authenticated user's profile.
OAuth app tokens and personal access tokens (classic) need theuserscope to use this endpoint.

### Fine-grained access tokens for "Delete social accounts for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Profile" user permissions (write)

### Parameters for "Delete social accounts for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
account_urlsarray of stringsRequiredFull URLs for the social media profiles to delete.
[/TABLE]

```
account_urls
```
Full URLs for the social media profiles to delete.

### HTTP response status codes for "Delete social accounts for the authenticated user"

[TABLE]
Status code | Description
204 | No Content
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete social accounts for the authenticated user"

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
  https://api.github.com/user/social_accounts \
  -d '{"account_urls":["https://facebook.com/GitHub","https://www.youtube.com/@GitHub"]}'
```

#### Response

```
Status: 204
```

## List social accounts for a user
Lists social media accounts for a user. This endpoint is accessible by anyone.

### Fine-grained access tokens for "List social accounts for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### Parameters for "List social accounts for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List social accounts for a user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List social accounts for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/social_accounts
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
    "provider": "twitter",
    "url": "https://twitter.com/github"
  }
]
```