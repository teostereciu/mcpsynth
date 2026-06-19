# REST API endpoints for deploy keys

*Source: https://docs.github.com/en/rest/deploy-keys/deploy-keys*

---

# REST API endpoints for deploy keys
Use the REST API to create and manage deploy keys.

## About deploy keys
You can launch projects from a repository on GitHub.com to your server by using a deploy key, which is an SSH key that grants access to a single repository. GitHub attaches the public part of the key directly to your repository instead of a personal account, and the private part of the key remains on your server. For more information, seeDelivering deployments.
Deploy keys can either be set up using the following API endpoints, or by using the GitHub web interface. To learn how to set deploy keys up in the web interface, seeManaging deploy keys.
There are a few cases when a deploy key will be deleted by other activity:
- If the deploy key is created with a personal access token, deleting the personal access token will also delete the deploy key. Regenerating the personal access token will not delete the deploy key.
- If the deploy key is created with an OAuth app token, revoking the token will also delete the deploy key.
Conversely, these activities will not delete a deploy key:
- If the deploy key is created with a GitHub App user access token, revoking the token will not delete the deploy key.
- If the deploy key is created with a GitHub App installation access token, uninstalling or deleting the app will not delete the deploy key.
- If the deploy key is created with a personal access token, regenerating the personal access token will not delete the deploy key.

## List deploy keys

### Fine-grained access tokens for "List deploy keys"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "List deploy keys"

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

### HTTP response status codes for "List deploy keys"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List deploy keys"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/keys
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
    "key": "ssh-rsa AAA...",
    "url": "https://api.github.com/repos/octocat/Hello-World/keys/1",
    "title": "octocat@octomac",
    "verified": true,
    "created_at": "2014-12-10T15:53:42Z",
    "read_only": true,
    "added_by": "octocat",
    "last_used": "2022-01-10T15:53:42Z",
    "enabled": true
  }
]
```

## Create a deploy key
You can create a read-only deploy key.

### Fine-grained access tokens for "Create a deploy key"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create a deploy key"

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
titlestringA name for the key.
keystringRequiredThe contents of the key.
read_onlybooleanIftrue, the key will only be able to read repository contents. Otherwise, the key will be able to read and write.Deploy keys with write access can perform the same actions as an organization member with admin access, or a collaborator on a personal repository. For more information, see "Repository permission levels for an organization" and "Permission levels for a user account repository."
[/TABLE]
A name for the key.
The contents of the key.
Iftrue, the key will only be able to read repository contents. Otherwise, the key will be able to read and write.
Deploy keys with write access can perform the same actions as an organization member with admin access, or a collaborator on a personal repository. For more information, see "Repository permission levels for an organization" and "Permission levels for a user account repository."

### HTTP response status codes for "Create a deploy key"

[TABLE]
Status code | Description
201 | Created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a deploy key"

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
  https://api.github.com/repos/OWNER/REPO/keys \
  -d '{"title":"octocat@octomac","key":"ssh-rsa AAA...","read_only":true}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "key": "ssh-rsa AAA...",
  "url": "https://api.github.com/repos/octocat/Hello-World/keys/1",
  "title": "octocat@octomac",
  "verified": true,
  "created_at": "2014-12-10T15:53:42Z",
  "read_only": true,
  "added_by": "octocat",
  "last_used": "2022-01-10T15:53:42Z",
  "enabled": true
}
```

## Get a deploy key

### Fine-grained access tokens for "Get a deploy key"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get a deploy key"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
key_idintegerRequiredThe unique identifier of the key.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the key.

### HTTP response status codes for "Get a deploy key"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a deploy key"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/keys/KEY_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "key": "ssh-rsa AAA...",
  "url": "https://api.github.com/repos/octocat/Hello-World/keys/1",
  "title": "octocat@octomac",
  "verified": true,
  "created_at": "2014-12-10T15:53:42Z",
  "read_only": true,
  "added_by": "octocat",
  "last_used": "2022-01-10T15:53:42Z",
  "enabled": true
}
```

## Delete a deploy key
Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.

### Fine-grained access tokens for "Delete a deploy key"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Delete a deploy key"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
key_idintegerRequiredThe unique identifier of the key.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the key.

### HTTP response status codes for "Delete a deploy key"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a deploy key"

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
  https://api.github.com/repos/OWNER/REPO/keys/KEY_ID
```

#### Response

```
Status: 204
```