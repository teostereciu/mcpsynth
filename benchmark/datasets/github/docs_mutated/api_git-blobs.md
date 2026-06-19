# REST API endpoints for Git blobs

*Source: https://docs.github.com/en/rest/git/blobs*

---

# REST API endpoints for Git blobs
Use the REST API to interact with a Git blob (binary large object), the object type used to store the contents of each file in a repository.

## About Git blobs
A Git blob (binary large object) is the object type used to store the contents of each file in a repository. The file's SHA-1 hash is computed and stored in the blob object. These endpoints allow you to read and writeblob objectsto your Git database on GitHub. Blobs leverage custom media types. For more information about the use of media types in the API, seeGetting started with the REST API.

## Create a blob

### Fine-grained access tokens for "Create a blob"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a blob"

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
contentstringRequiredThe new blob's content.
encodingstringThe encoding used forcontent. Currently,"utf-8"and"base64"are supported.Default:utf-8
[/TABLE]
The new blob's content.
The encoding used forcontent. Currently,"utf-8"and"base64"are supported.
Default:utf-8

### HTTP response status codes for "Create a blob"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed
[/TABLE]
Created
Forbidden
Resource not found
Conflict
Validation failed

### Code samples for "Create a blob"

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
  https://api.github.com/repos/OWNER/REPO/git/blobs \
  -d '{"content":"Content of the blob","encoding":"utf-8"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "url": "https://api.github.com/repos/octocat/example/git/blobs/3a0f86fb8db8eea7ccbb9a95f325ddbedfb25e15",
  "commit_sha": "3a0f86fb8db8eea7ccbb9a95f325ddbedfb25e15"
}
```

## Get a blob
Thecontentin the response will always be Base64 encoded.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw blob data.
- application/vnd.github+json: Returns a JSON representation of the blob withcontentas a base64 encoded string. This is the default if no media type is specified.

```
application/vnd.github.raw+json
```

```
application/vnd.github+json
```
NoteThis endpoint supports blobs up to 100 megabytes in size.

### Fine-grained access tokens for "Get a blob"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a blob"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
file_shastringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get a blob"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Get a blob"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/git/blobs/FILE_SHA
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "content": "Q29udGVudCBvZiB0aGUgYmxvYg==",
  "encoding": "base64",
  "url": "https://api.github.com/repos/octocat/example/git/blobs/3a0f86fb8db8eea7ccbb9a95f325ddbedfb25e15",
  "commit_sha": "3a0f86fb8db8eea7ccbb9a95f325ddbedfb25e15",
  "size": 19,
  "node_id": "Q29udGVudCBvZiB0aGUgYmxvYg=="
}
```