# REST API endpoints for commit comments

*Source: https://docs.github.com/en/rest/commits/comments*

---

# REST API endpoints for commit comments
Use the REST API to interact with commit comments.

## About commit comments
You can create, edit, and view commit comments using the REST API. A commit comment is a comment made on a specific commit. For more information, seeWorking with comments.

## List commit comments for a repository
Lists the commit comments for a specified repository. Comments are ordered by ascending ID.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github-commitcomment.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github-commitcomment.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github-commitcomment.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github-commitcomment.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github-commitcomment.raw+json
```

```
application/vnd.github-commitcomment.text+json
```

```
application/vnd.github-commitcomment.html+json
```

```
application/vnd.github-commitcomment.full+json
```

### Fine-grained access tokens for "List commit comments for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List commit comments for a repository"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List commit comments for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List commit comments for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/comments
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
    "html_url": "https://github.com/octocat/Hello-World/commit/6dcb09b5b57875f334f61aebed695e2e4193db5e#commitcomment-1",
    "url": "https://api.github.com/repos/octocat/Hello-World/comments/1",
    "id": 1,
    "node_id": "MDEzOkNvbW1pdENvbW1lbnQx",
    "body": "Great stuff",
    "path": "file1.txt",
    "position": 4,
    "line": 14,
    "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
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
    "created_at": "2011-04-14T16:00:49Z",
    "updated_at": "2011-04-14T16:00:49Z",
    "author_association": "COLLABORATOR"
  }
]
```

## Get a commit comment
Gets a specified commit comment.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github-commitcomment.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github-commitcomment.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github-commitcomment.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github-commitcomment.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github-commitcomment.raw+json
```

```
application/vnd.github-commitcomment.text+json
```

```
application/vnd.github-commitcomment.html+json
```

```
application/vnd.github-commitcomment.full+json
```

### Fine-grained access tokens for "Get a commit comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a commit comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the comment.

### HTTP response status codes for "Get a commit comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a commit comment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/comments/COMMENT_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "html_url": "https://github.com/octocat/Hello-World/commit/6dcb09b5b57875f334f61aebed695e2e4193db5e#commitcomment-1",
  "url": "https://api.github.com/repos/octocat/Hello-World/comments/1",
  "id": 1,
  "node_id": "MDEzOkNvbW1pdENvbW1lbnQx",
  "body": "Great stuff",
  "path": "file1.txt",
  "position": 4,
  "line": 14,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "author_association": "COLLABORATOR",
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
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z"
}
```

## Update a commit comment
Updates the contents of a specified commit comment.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github-commitcomment.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github-commitcomment.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github-commitcomment.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github-commitcomment.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github-commitcomment.raw+json
```

```
application/vnd.github-commitcomment.text+json
```

```
application/vnd.github-commitcomment.html+json
```

```
application/vnd.github-commitcomment.full+json
```

### Fine-grained access tokens for "Update a commit comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Update a commit comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the comment.

[TABLE]
Name, Type, Description
bodystringRequiredThe contents of the comment
[/TABLE]
The contents of the comment

### HTTP response status codes for "Update a commit comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Update a commit comment"

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
  https://api.github.com/repos/OWNER/REPO/comments/COMMENT_ID \
  -d '{"body":"Nice change"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "html_url": "https://github.com/octocat/Hello-World/commit/6dcb09b5b57875f334f61aebed695e2e4193db5e#commitcomment-1",
  "url": "https://api.github.com/repos/octocat/Hello-World/comments/1",
  "id": 1,
  "node_id": "MDEzOkNvbW1pdENvbW1lbnQx",
  "body": "Nice change",
  "path": "file1.txt",
  "position": 4,
  "line": 14,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "author_association": "COLLABORATOR",
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
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z"
}
```

## Delete a commit comment

### Fine-grained access tokens for "Delete a commit comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Delete a commit comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the comment.

### HTTP response status codes for "Delete a commit comment"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Delete a commit comment"

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
  https://api.github.com/repos/OWNER/REPO/comments/COMMENT_ID
```

#### Response

```
Status: 204
```

## List commit comments
Lists the comments for a specified commit.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github-commitcomment.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github-commitcomment.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github-commitcomment.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github-commitcomment.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github-commitcomment.raw+json
```

```
application/vnd.github-commitcomment.text+json
```

```
application/vnd.github-commitcomment.html+json
```

```
application/vnd.github-commitcomment.full+json
```

### Fine-grained access tokens for "List commit comments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List commit comments"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
commit_shastringRequiredThe SHA of the commit.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The SHA of the commit.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List commit comments"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List commit comments"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/commits/COMMIT_SHA/comments
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
    "html_url": "https://github.com/octocat/Hello-World/commit/6dcb09b5b57875f334f61aebed695e2e4193db5e#commitcomment-1",
    "url": "https://api.github.com/repos/octocat/Hello-World/comments/1",
    "id": 1,
    "node_id": "MDEzOkNvbW1pdENvbW1lbnQx",
    "body": "Great stuff",
    "path": "file1.txt",
    "position": 4,
    "line": 14,
    "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
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
    "created_at": "2011-04-14T16:00:49Z",
    "updated_at": "2011-04-14T16:00:49Z",
    "author_association": "COLLABORATOR"
  }
]
```

## Create a commit comment
Create a comment for a commit using its:commit_sha.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API" and "Best practices for using the REST API."
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github-commitcomment.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github-commitcomment.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github-commitcomment.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github-commitcomment.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github-commitcomment.raw+json
```

```
application/vnd.github-commitcomment.text+json
```

```
application/vnd.github-commitcomment.html+json
```

```
application/vnd.github-commitcomment.full+json
```

### Fine-grained access tokens for "Create a commit comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)

### Parameters for "Create a commit comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
commit_shastringRequiredThe SHA of the commit.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The SHA of the commit.

[TABLE]
Name, Type, Description
bodystringRequiredThe contents of the comment.
pathstringRelative path of the file to comment on.
positionintegerLine index in the diff to comment on.
lineintegerClosing down notice. Usepositionparameter instead. Line number in the file to comment on.
[/TABLE]
The contents of the comment.
Relative path of the file to comment on.
Line index in the diff to comment on.
Closing down notice. Usepositionparameter instead. Line number in the file to comment on.

### HTTP response status codes for "Create a commit comment"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Forbidden
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a commit comment"

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
  https://api.github.com/repos/OWNER/REPO/commits/COMMIT_SHA/comments \
  -d '{"body":"Great stuff","path":"file1.txt","position":4,"line":1}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "html_url": "https://github.com/octocat/Hello-World/commit/6dcb09b5b57875f334f61aebed695e2e4193db5e#commitcomment-1",
  "url": "https://api.github.com/repos/octocat/Hello-World/comments/1",
  "id": 1,
  "node_id": "MDEzOkNvbW1pdENvbW1lbnQx",
  "body": "Great stuff",
  "path": "file1.txt",
  "position": 4,
  "line": 14,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "author_association": "COLLABORATOR",
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
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z"
}
```