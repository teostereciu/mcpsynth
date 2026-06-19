# REST API endpoints for issue comments

*Source: https://docs.github.com/en/rest/issues/comments*

---

# REST API endpoints for issue comments
Use the REST API to manage comments on issues and pull requests.

## About issue and pull request comments
You can use the REST API to create and manage comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. For this reason, "shared" actions for both features, like managing assignees, labels, and milestones, are provided within the Issues endpoints. To manage pull request review comments, seeREST API endpoints for pull request review comments.

## List issue comments for a repository
You can use the REST API to list comments on issues and pull requests for a repository. Every pull request is an issue, but not every issue is a pull request.
By default, issue comments are ordered by ascending ID.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github.raw+json
```

```
application/vnd.github.text+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.full+json
```

### Fine-grained access tokens for "List issue comments for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List issue comments for a repository"

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
sortstringThe property to sort the results by.Default:createdCan be one of:created,updated
directionstringEitherascordesc. Ignored without thesortparameter.Can be one of:asc,desc
sincestringOnly show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The property to sort the results by.
Default:created
Can be one of:created,updated
Eitherascordesc. Ignored without thesortparameter.
Can be one of:asc,desc
Only show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List issue comments for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "List issue comments for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/comments
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
    "node_id": "MDEyOklzc3VlQ29tbWVudDE=",
    "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1",
    "html_url": "https://github.com/octocat/Hello-World/issues/1347#issuecomment-1",
    "body": "Me too",
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
    "issue_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
    "author_association": "COLLABORATOR"
  }
]
```

## Get an issue comment
You can use the REST API to get comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github.raw+json
```

```
application/vnd.github.text+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.full+json
```

### Fine-grained access tokens for "Get an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get an issue comment"

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

### HTTP response status codes for "Get an issue comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get an issue comment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID
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
  "node_id": "MDEyOklzc3VlQ29tbWVudDE=",
  "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1",
  "html_url": "https://github.com/octocat/Hello-World/issues/1347#issuecomment-1",
  "body": "Me too",
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
  "issue_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
  "author_association": "COLLABORATOR",
  "pin": null
}
```

## Update an issue comment
You can use the REST API to update comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github.raw+json
```

```
application/vnd.github.text+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.full+json
```

### Fine-grained access tokens for "Update an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Update an issue comment"

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
bodystringRequiredThe contents of the comment.
[/TABLE]
The contents of the comment.

### HTTP response status codes for "Update an issue comment"

[TABLE]
Status code | Description
200 | OK
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Validation failed, or the endpoint has been spammed.

### Code samples for "Update an issue comment"

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
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID \
  -d '{"body":"Me too"}'
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
  "node_id": "MDEyOklzc3VlQ29tbWVudDE=",
  "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1",
  "html_url": "https://github.com/octocat/Hello-World/issues/1347#issuecomment-1",
  "body": "Me too",
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
  "issue_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
  "author_association": "COLLABORATOR",
  "pin": null
}
```

## Delete an issue comment
You can use the REST API to delete comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.

### Fine-grained access tokens for "Delete an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Delete an issue comment"

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

### HTTP response status codes for "Delete an issue comment"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an issue comment"

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
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID
```

#### Response

```
Status: 204
```

## Pin an issue comment
You can use the REST API to pin comments on issues.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github.raw+json
```

```
application/vnd.github.text+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.full+json
```

### Fine-grained access tokens for "Pin an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (write)

### Parameters for "Pin an issue comment"

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

### HTTP response status codes for "Pin an issue comment"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
410 | Gone
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found
Gone
Validation failed, or the endpoint has been spammed.

### Code samples for "Pin an issue comment"

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
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID/pin
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
  "node_id": "MDEyOklzc3VlQ29tbWVudDE=",
  "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1",
  "html_url": "https://github.com/octocat/Hello-World/issues/1347#issuecomment-1",
  "body": "Me too",
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
  "issue_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
  "author_association": "COLLABORATOR",
  "pin": {
    "pinned_at": "2021-01-01T00:00:00Z",
    "pinned_by": {
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
  }
}
```

## Unpin an issue comment
You can use the REST API to unpin comments on issues.

### Fine-grained access tokens for "Unpin an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (write)

### Parameters for "Unpin an issue comment"

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

### HTTP response status codes for "Unpin an issue comment"

[TABLE]
Status code | Description
204 | No Content
401 | Requires authentication
403 | Forbidden
404 | Resource not found
410 | Gone
503 | Service unavailable
[/TABLE]
No Content
Requires authentication
Forbidden
Resource not found
Gone
Service unavailable

### Code samples for "Unpin an issue comment"

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
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID/pin
```

#### Response

```
Status: 204
```

## List issue comments
You can use the REST API to list comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.
Issue comments are ordered by ascending ID.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github.raw+json
```

```
application/vnd.github.text+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.full+json
```

### Fine-grained access tokens for "List issue comments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List issue comments"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
issue_numberintegerRequiredThe number that identifies the issue.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
issue_number
```
The number that identifies the issue.

[TABLE]
Name, Type, Description
sincestringOnly show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Only show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List issue comments"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
410 | Gone
[/TABLE]
OK
Resource not found
Gone

### Code samples for "List issue comments"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/comments
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
    "node_id": "MDEyOklzc3VlQ29tbWVudDE=",
    "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1",
    "html_url": "https://github.com/octocat/Hello-World/issues/1347#issuecomment-1",
    "body": "Me too",
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
    "issue_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
    "author_association": "COLLABORATOR"
  }
]
```

## Create an issue comment
You can use the REST API to create comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.
This endpoint triggersnotifications.
Creating content too quickly using this endpoint may result in secondary rate limiting.
For more information, see "Rate limits for the API"
and "Best practices for using the REST API."
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw markdown body. Response will includebody. This is the default if you do not pass any specific media type.
- application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will includebody_text.
- application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will includebody_html.
- application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will includebody,body_text, andbody_html.

```
application/vnd.github.raw+json
```

```
application/vnd.github.text+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.full+json
```

### Fine-grained access tokens for "Create an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Create an issue comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
issue_numberintegerRequiredThe number that identifies the issue.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
issue_number
```
The number that identifies the issue.

[TABLE]
Name, Type, Description
bodystringRequiredThe contents of the comment.
[/TABLE]
The contents of the comment.

### HTTP response status codes for "Create an issue comment"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
404 | Resource not found
410 | Gone
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Forbidden
Resource not found
Gone
Validation failed, or the endpoint has been spammed.

### Code samples for "Create an issue comment"

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
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/comments \
  -d '{"body":"Me too"}'
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
  "node_id": "MDEyOklzc3VlQ29tbWVudDE=",
  "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1",
  "html_url": "https://github.com/octocat/Hello-World/issues/1347#issuecomment-1",
  "body": "Me too",
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
  "issue_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
  "author_association": "COLLABORATOR",
  "pin": null
}
```