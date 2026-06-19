# REST API endpoints for emails

*Source: https://docs.github.com/en/rest/users/emails*

---

# REST API endpoints for emails
Use the REST API to manage email addresses of authenticated users.

## About email administration
If a request URL does not include a{username}parameter then the response will be for the signed-in user (and you must passauthentication informationwith your request). Additional private information, such as whether a user has two-factor authentication enabled, is included when authenticated through OAuth with theuserscope.

## Set primary email visibility for the authenticated user
Sets the visibility for your primary email addresses.

### Fine-grained access tokens for "Set primary email visibility for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Email addresses" user permissions (write)

### Parameters for "Set primary email visibility for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
visibilitystringRequiredDenotes whether an email is publicly visible.Can be one of:public,private
[/TABLE]
Denotes whether an email is publicly visible.
Can be one of:public,private

### HTTP response status codes for "Set primary email visibility for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set primary email visibility for the authenticated user"

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
  https://api.github.com/user/email/visibility \
  -d '{"visibility":"private"}'
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
    "email": "octocat@github.com",
    "primary": true,
    "verified": true,
    "visibility": "private"
  }
]
```

## List email addresses for the authenticated user
Lists all of your email addresses, and specifies which one is visible
to the public.
OAuth app tokens and personal access tokens (classic) need theuser:emailscope to use this endpoint.

### Fine-grained access tokens for "List email addresses for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Email addresses" user permissions (read)

### Parameters for "List email addresses for the authenticated user"

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

### HTTP response status codes for "List email addresses for the authenticated user"

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

### Code samples for "List email addresses for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/emails
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
    "email": "octocat@github.com",
    "verified": true,
    "primary": true,
    "visibility": "public"
  }
]
```

## Add an email address for the authenticated user
OAuth app tokens and personal access tokens (classic) need theuserscope to use this endpoint.

### Fine-grained access tokens for "Add an email address for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Email addresses" user permissions (write)

### Parameters for "Add an email address for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
emailsarray of stringsRequiredAdds one or more email addresses to your GitHub account. Must contain at least one email address.Note:Alternatively, you can pass a single email address or anarrayof emails addresses directly, but we recommend that you pass an object using theemailskey.
[/TABLE]
Adds one or more email addresses to your GitHub account. Must contain at least one email address.Note:Alternatively, you can pass a single email address or anarrayof emails addresses directly, but we recommend that you pass an object using theemailskey.

### HTTP response status codes for "Add an email address for the authenticated user"

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

### Code samples for "Add an email address for the authenticated user"

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
  https://api.github.com/user/emails \
  -d '{"emails":["octocat@github.com","mona@github.com","octocat@octocat.org"]}'
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
    "email": "octocat@octocat.org",
    "primary": false,
    "verified": false,
    "visibility": "public"
  },
  {
    "email": "octocat@github.com",
    "primary": false,
    "verified": false,
    "visibility": null
  },
  {
    "email": "mona@github.com",
    "primary": false,
    "verified": false,
    "visibility": null
  }
]
```

## Delete an email address for the authenticated user
OAuth app tokens and personal access tokens (classic) need theuserscope to use this endpoint.

### Fine-grained access tokens for "Delete an email address for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Email addresses" user permissions (write)

### Parameters for "Delete an email address for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
emailsarray of stringsRequiredEmail addresses associated with the GitHub user account.
[/TABLE]
Email addresses associated with the GitHub user account.

### HTTP response status codes for "Delete an email address for the authenticated user"

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

### Code samples for "Delete an email address for the authenticated user"

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
  https://api.github.com/user/emails \
  -d '{"emails":["octocat@github.com","mona@github.com"]}'
```

#### Response

```
Status: 204
```

## List public email addresses for the authenticated user
Lists your publicly visible email address, which you can set with theSet primary email visibility for the authenticated userendpoint.
OAuth app tokens and personal access tokens (classic) need theuser:emailscope to use this endpoint.

### Fine-grained access tokens for "List public email addresses for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Email addresses" user permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List public email addresses for the authenticated user"

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

### HTTP response status codes for "List public email addresses for the authenticated user"

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

### Code samples for "List public email addresses for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/public_emails
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
    "email": "octocat@github.com",
    "verified": true,
    "primary": true,
    "visibility": "public"
  }
]
```