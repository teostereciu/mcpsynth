# REST API endpoints for Git SSH keys

*Source: https://docs.github.com/en/rest/users/keys*

---

# REST API endpoints for Git SSH keys
Use the REST API to manage Git SSH keys of authenticated users.

## About Git SSH key administration
If a request URL does not include a{username}parameter then the response will be for the signed-in user (and you must passauthentication informationwith your request). Additional private information, such as whether a user has two-factor authentication enabled, is included when authenticated through OAuth with theuserscope.

## List public SSH keys for the authenticated user
Lists the public SSH keys for the authenticated user's GitHub account.
OAuth app tokens and personal access tokens (classic) need theread:public_keyscope to use this endpoint.

### Fine-grained access tokens for "List public SSH keys for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Git SSH keys" user permissions (read)

### Parameters for "List public SSH keys for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List public SSH keys for the authenticated user"

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

### Code samples for "List public SSH keys for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/keys
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
    "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234",
    "id": 2,
    "url": "https://api.github.com/user/keys/2",
    "title": "ssh-rsa AAAAB3NzaC1yc2EAAA",
    "created_at": "2020-06-11T21:31:57Z",
    "verified": false,
    "read_only": false
  },
  {
    "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJy931234",
    "id": 3,
    "url": "https://api.github.com/user/keys/3",
    "title": "ssh-rsa AAAAB3NzaC1yc2EAAB",
    "created_at": "2020-07-11T21:31:57Z",
    "verified": false,
    "read_only": false
  }
]
```

## Create a public SSH key for the authenticated user
Adds a public SSH key to the authenticated user's GitHub account.
OAuth app tokens and personal access tokens (classic) need thewrite:public_keyscope to use this endpoint.

### Fine-grained access tokens for "Create a public SSH key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Git SSH keys" user permissions (write)

### Parameters for "Create a public SSH key for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
titlestringA descriptive name for the new key.
keystringRequiredThe public SSH key to add to your GitHub account.
[/TABLE]
A descriptive name for the new key.
The public SSH key to add to your GitHub account.

### HTTP response status codes for "Create a public SSH key for the authenticated user"

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

### Code samples for "Create a public SSH key for the authenticated user"

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
  https://api.github.com/user/keys \
  -d '{"title":"ssh-rsa AAAAB3NzaC1yc2EAAA","key":"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234",
  "id": 2,
  "url": "https://api.github.com/user/keys/2",
  "title": "ssh-rsa AAAAB3NzaC1yc2EAAA",
  "created_at": "2020-06-11T21:31:57Z",
  "verified": false,
  "read_only": false
}
```

## Get a public SSH key for the authenticated user
View extended details for a single public SSH key.
OAuth app tokens and personal access tokens (classic) need theread:public_keyscope to use this endpoint.

### Fine-grained access tokens for "Get a public SSH key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Git SSH keys" user permissions (read)

### Parameters for "Get a public SSH key for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
key_idintegerRequiredThe unique identifier of the key.
[/TABLE]
The unique identifier of the key.

### HTTP response status codes for "Get a public SSH key for the authenticated user"

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

### Code samples for "Get a public SSH key for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/keys/KEY_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234",
  "id": 2,
  "url": "https://api.github.com/user/keys/2",
  "title": "ssh-rsa AAAAB3NzaC1yc2EAAA",
  "created_at": "2020-06-11T21:31:57Z",
  "verified": false,
  "read_only": false
}
```

## Delete a public SSH key for the authenticated user
Removes a public SSH key from the authenticated user's GitHub account.
OAuth app tokens and personal access tokens (classic) need theadmin:public_keyscope to use this endpoint.

### Fine-grained access tokens for "Delete a public SSH key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Git SSH keys" user permissions (write)

### Parameters for "Delete a public SSH key for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
key_idintegerRequiredThe unique identifier of the key.
[/TABLE]
The unique identifier of the key.

### HTTP response status codes for "Delete a public SSH key for the authenticated user"

[TABLE]
Status code | Description
204 | No Content
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Not modified
Requires authentication
Forbidden
Resource not found

### Code samples for "Delete a public SSH key for the authenticated user"

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
  https://api.github.com/user/keys/KEY_ID
```

#### Response

```
Status: 204
```

## List public keys for a user
Lists theverifiedpublic SSH keys for a user. This is accessible by anyone.

### Fine-grained access tokens for "List public keys for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Git SSH keys" user permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List public keys for a user"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List public keys for a user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List public keys for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/keys
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
    "key": "ssh-rsa AAA..."
  }
]
```