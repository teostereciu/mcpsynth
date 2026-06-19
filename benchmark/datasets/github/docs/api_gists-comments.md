# REST API endpoints for gist comments

*Source: https://docs.github.com/en/rest/gists/comments*

---

# REST API endpoints for gist comments
Use the REST API to view and modify comments on a gist.

## About gist comments
You can use the REST API to view and modify comments on a gist. For more information about gists, seeEditing and sharing content with gists.

## List gist comments
Lists the comments on a gist.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown. This is the default if you do not pass any specific media type.
- application/vnd.github.base64+json: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

```
application/vnd.github.raw+json
```

```
application/vnd.github.base64+json
```

### Fine-grained access tokens for "List gist comments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List gist comments"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gist_idstringRequiredThe unique identifier of the gist.
[/TABLE]
The unique identifier of the gist.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List gist comments"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Not modified
Forbidden
Resource not found

### Code samples for "List gist comments"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/gists/GIST_ID/comments
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
    "node_id": "MDExOkdpc3RDb21tZW50MQ==",
    "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
    "body": "Just commenting for the sake of commenting",
    "user": {
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
    },
    "created_at": "2011-04-18T23:23:56Z",
    "updated_at": "2011-04-18T23:23:56Z",
    "author_association": "COLLABORATOR"
  }
]
```

## Create a gist comment
Creates a comment on a gist.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown. This is the default if you do not pass any specific media type.
- application/vnd.github.base64+json: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

```
application/vnd.github.raw+json
```

```
application/vnd.github.base64+json
```

### Fine-grained access tokens for "Create a gist comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Gists" user permissions (write)

### Parameters for "Create a gist comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gist_idstringRequiredThe unique identifier of the gist.
[/TABLE]
The unique identifier of the gist.

[TABLE]
Name, Type, Description
bodystringRequiredThe comment text.
[/TABLE]
The comment text.

### HTTP response status codes for "Create a gist comment"

[TABLE]
Status code | Description
201 | Created
304 | Not modified
403 | Forbidden
404 | Resource not found
[/TABLE]
Created
Not modified
Forbidden
Resource not found

### Code samples for "Create a gist comment"

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
  https://api.github.com/gists/GIST_ID/comments \
  -d '{"body":"This is a comment to a gist"}'
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
  "node_id": "MDExOkdpc3RDb21tZW50MQ==",
  "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
  "body": "Just commenting for the sake of commenting",
  "user": {
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
  },
  "created_at": "2011-04-18T23:23:56Z",
  "updated_at": "2011-04-18T23:23:56Z",
  "author_association": "COLLABORATOR"
}
```

## Get a gist comment
Gets a comment on a gist.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown. This is the default if you do not pass any specific media type.
- application/vnd.github.base64+json: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

```
application/vnd.github.raw+json
```

```
application/vnd.github.base64+json
```

### Fine-grained access tokens for "Get a gist comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "Get a gist comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gist_idstringRequiredThe unique identifier of the gist.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The unique identifier of the gist.
The unique identifier of the comment.

### HTTP response status codes for "Get a gist comment"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Forbidden Gist
404 | Resource not found
[/TABLE]
OK
Not modified
Forbidden Gist
Resource not found

### Code samples for "Get a gist comment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/gists/GIST_ID/comments/COMMENT_ID
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
  "node_id": "MDExOkdpc3RDb21tZW50MQ==",
  "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
  "body": "Just commenting for the sake of commenting",
  "user": {
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
  },
  "created_at": "2011-04-18T23:23:56Z",
  "updated_at": "2011-04-18T23:23:56Z",
  "author_association": "COLLABORATOR"
}
```

## Update a gist comment
Updates a comment on a gist.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown. This is the default if you do not pass any specific media type.
- application/vnd.github.base64+json: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

```
application/vnd.github.raw+json
```

```
application/vnd.github.base64+json
```

### Fine-grained access tokens for "Update a gist comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Gists" user permissions (write)

### Parameters for "Update a gist comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gist_idstringRequiredThe unique identifier of the gist.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The unique identifier of the gist.
The unique identifier of the comment.

[TABLE]
Name, Type, Description
bodystringRequiredThe comment text.
[/TABLE]
The comment text.

### HTTP response status codes for "Update a gist comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Update a gist comment"

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
  https://api.github.com/gists/GIST_ID/comments/COMMENT_ID \
  -d '{"body":"This is an update to a comment in a gist"}'
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
  "node_id": "MDExOkdpc3RDb21tZW50MQ==",
  "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
  "body": "Just commenting for the sake of commenting",
  "user": {
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
  },
  "created_at": "2011-04-18T23:23:56Z",
  "updated_at": "2011-04-18T23:23:56Z",
  "author_association": "COLLABORATOR"
}
```

## Delete a gist comment

### Fine-grained access tokens for "Delete a gist comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Gists" user permissions (write)

### Parameters for "Delete a gist comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gist_idstringRequiredThe unique identifier of the gist.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The unique identifier of the gist.
The unique identifier of the comment.

### HTTP response status codes for "Delete a gist comment"

[TABLE]
Status code | Description
204 | No Content
304 | Not modified
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Not modified
Forbidden
Resource not found

### Code samples for "Delete a gist comment"

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
  https://api.github.com/gists/GIST_ID/comments/COMMENT_ID
```

#### Response

```
Status: 204
```