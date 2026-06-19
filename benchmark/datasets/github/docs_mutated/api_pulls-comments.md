# REST API endpoints for pull request review comments

*Source: https://docs.github.com/en/rest/pulls/comments*

---

# REST API endpoints for pull request review comments
Use the REST API to interact with pull request review comments.

## About pull request review comments
Pull request review comments are comments made on a portion of the unified diff during a pull request review. These are different from commit comments and issue comments in a pull request. For more information, seeREST API endpoints for commit commentsandREST API endpoints for issue comments.

## List review comments in a repository
Lists review comments for all pull requests in a repository. By default,
review comments are in ascending order by ID.
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

### Fine-grained access tokens for "List review comments in a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List review comments in a repository"

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
sortstringCan be one of:created,updated,created_at
directionstringThe direction to sort results. Ignored withoutsortparameter.Can be one of:asc,desc
sincestringOnly show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Can be one of:created,updated,created_at
The direction to sort results. Ignored withoutsortparameter.
Can be one of:asc,desc
Only show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List review comments in a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List review comments in a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/comments
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
    "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
    "pull_request_review_id": 42,
    "id": 10,
    "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
    "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
    "path": "file1.txt",
    "position": 1,
    "original_position": 4,
    "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
    "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
    "in_reply_to_id": 8,
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
    "body": "Great stuff!",
    "created_at": "2011-04-14T16:00:49Z",
    "updated_at": "2011-04-14T16:00:49Z",
    "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
    "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
    "author_association": "NONE",
    "_links": {
      "self": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
      },
      "html": {
        "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
      },
      "pull_request": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
      }
    },
    "start_line": 1,
    "original_start_line": 1,
    "start_side": "RIGHT",
    "line": 2,
    "original_line": 2,
    "side": "RIGHT"
  }
]
```

## Get a review comment for a pull request
Provides details for a specified review comment.
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

### Fine-grained access tokens for "Get a review comment for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a review comment for a pull request"

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

### HTTP response status codes for "Get a review comment for a pull request"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a review comment for a pull request"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/comments/COMMENT_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
  "pull_request_review_id": 42,
  "id": 10,
  "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
  "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
  "path": "file1.txt",
  "position": 1,
  "original_position": 4,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
  "in_reply_to_id": 8,
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
  "body": "Great stuff!",
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z",
  "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "author_association": "NONE",
  "_links": {
    "self": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
    },
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
    }
  },
  "start_line": 1,
  "original_start_line": 1,
  "start_side": "RIGHT",
  "line": 2,
  "original_line": 2,
  "side": "RIGHT"
}
```

## Update a review comment for a pull request
Edits the content of a specified review comment.
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

### Fine-grained access tokens for "Update a review comment for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Update a review comment for a pull request"

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
bodystringRequiredThe text of the reply to the review comment.
[/TABLE]
The text of the reply to the review comment.

### HTTP response status codes for "Update a review comment for a pull request"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a review comment for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/comments/COMMENT_ID \
  -d '{"body":"I like this too!"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
  "pull_request_review_id": 42,
  "id": 10,
  "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
  "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
  "path": "file1.txt",
  "position": 1,
  "original_position": 4,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
  "in_reply_to_id": 8,
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
  "body": "Great stuff!",
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z",
  "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "author_association": "NONE",
  "_links": {
    "self": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
    },
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
    }
  },
  "start_line": 1,
  "original_start_line": 1,
  "start_side": "RIGHT",
  "line": 2,
  "original_line": 2,
  "side": "RIGHT"
}
```

## Delete a review comment for a pull request
Deletes a review comment.

### Fine-grained access tokens for "Delete a review comment for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Delete a review comment for a pull request"

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

### HTTP response status codes for "Delete a review comment for a pull request"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Delete a review comment for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/comments/COMMENT_ID
```

#### Response

```
Status: 204
```

## List review comments on a pull request
Lists all review comments for a specified pull request. By default, review comments
are in ascending order by ID.
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

### Fine-grained access tokens for "List review comments on a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List review comments on a pull request"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pull_numberintegerRequiredThe number that identifies the pull request.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.

[TABLE]
Name, Type, Description
sortstringThe property to sort the results by.Default:createdCan be one of:created,updated
directionstringThe direction to sort results. Ignored withoutsortparameter.Can be one of:asc,desc
sincestringOnly show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The property to sort the results by.
Default:created
Can be one of:created,updated
The direction to sort results. Ignored withoutsortparameter.
Can be one of:asc,desc
Only show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List review comments on a pull request"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List review comments on a pull request"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/comments
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
    "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
    "pull_request_review_id": 42,
    "id": 10,
    "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
    "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
    "path": "file1.txt",
    "position": 1,
    "original_position": 4,
    "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
    "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
    "in_reply_to_id": 8,
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
    "body": "Great stuff!",
    "created_at": "2011-04-14T16:00:49Z",
    "updated_at": "2011-04-14T16:00:49Z",
    "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
    "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
    "author_association": "NONE",
    "_links": {
      "self": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
      },
      "html": {
        "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
      },
      "pull_request": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
      }
    },
    "start_line": 1,
    "original_start_line": 1,
    "start_side": "RIGHT",
    "line": 2,
    "original_line": 2,
    "side": "RIGHT"
  }
]
```

## Create a review comment for a pull request
Creates a review comment on the diff of a specified pull request. To add a regular comment to a pull request timeline, see "Create an issue comment."
If your comment applies to more than one line in the pull request diff, you should use the parametersline,side, and optionallystart_lineandstart_sidein your request.
Thepositionparameter is closing down. If you useposition, theline,side,start_line, andstart_sideparameters are not required.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API"
and "Best practices for using the REST API."
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

### Fine-grained access tokens for "Create a review comment for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Create a review comment for a pull request"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pull_numberintegerRequiredThe number that identifies the pull request.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.

[TABLE]
Name, Type, Description
bodystringRequiredThe text of the review comment.
commit_idstringRequiredThe SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as theposition.
pathstringRequiredThe relative path to the file that necessitates a comment.
positionintegerThis parameter is closing down. Uselineinstead. The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
sidestringIn a split diff view, the side of the diff that the pull request's changes appear on. Can beLEFTorRIGHT. UseLEFTfor deletions that appear in red. UseRIGHTfor additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see "Diff view options" in the GitHub Help documentation.Can be one of:LEFT,RIGHT
lineintegerRequired unless usingsubject_type:file. The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to.
start_lineintegerRequired when using multi-line comments unless usingin_reply_to. Thestart_lineis the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see "Commenting on a pull request" in the GitHub Help documentation.
start_sidestringRequired when using multi-line comments unless usingin_reply_to. Thestart_sideis the starting side of the diff that the comment applies to. Can beLEFTorRIGHT. To learn more about multi-line comments, see "Commenting on a pull request" in the GitHub Help documentation. Seesidein this table for additional context.Can be one of:LEFT,RIGHT,side
in_reply_tointegerThe ID of the review comment to reply to. To find the ID of a review comment with"List review comments on a pull request". When specified, all parameters other thanbodyin the request body are ignored.
subject_typestringThe level at which the comment is targeted.Can be one of:line,file
[/TABLE]
The text of the review comment.
The SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as theposition.
The relative path to the file that necessitates a comment.
This parameter is closing down. Uselineinstead. The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
In a split diff view, the side of the diff that the pull request's changes appear on. Can beLEFTorRIGHT. UseLEFTfor deletions that appear in red. UseRIGHTfor additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see "Diff view options" in the GitHub Help documentation.
Can be one of:LEFT,RIGHT
Required unless usingsubject_type:file. The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to.

```
subject_type:file
```
Required when using multi-line comments unless usingin_reply_to. Thestart_lineis the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see "Commenting on a pull request" in the GitHub Help documentation.

```
in_reply_to
```
Required when using multi-line comments unless usingin_reply_to. Thestart_sideis the starting side of the diff that the comment applies to. Can beLEFTorRIGHT. To learn more about multi-line comments, see "Commenting on a pull request" in the GitHub Help documentation. Seesidein this table for additional context.

```
in_reply_to
```
Can be one of:LEFT,RIGHT,side

```
in_reply_to
```
The ID of the review comment to reply to. To find the ID of a review comment with"List review comments on a pull request". When specified, all parameters other thanbodyin the request body are ignored.

```
subject_type
```
The level at which the comment is targeted.
Can be one of:line,file

### HTTP response status codes for "Create a review comment for a pull request"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Forbidden
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a review comment for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/comments \
  -d '{"body":"Great stuff!","commit_id":"6dcb09b5b57875f334f61aebed695e2e4193db5e","path":"file1.txt","start_line":1,"start_side":"RIGHT","line":2,"side":"RIGHT"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
  "pull_request_review_id": 42,
  "id": 10,
  "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
  "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
  "path": "file1.txt",
  "position": 1,
  "original_position": 4,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
  "in_reply_to_id": 8,
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
  "body": "Great stuff!",
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z",
  "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "author_association": "NONE",
  "_links": {
    "self": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
    },
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
    }
  },
  "start_line": 1,
  "original_start_line": 1,
  "start_side": "RIGHT",
  "line": 2,
  "original_line": 2,
  "side": "RIGHT"
}
```

## Create a reply for a review comment
Creates a reply to a review comment for a pull request. For thecomment_id, provide the ID of the review comment you are replying to. This must be the ID of atop-level review comment, not a reply to that comment. Replies to replies are not supported.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API"
and "Best practices for using the REST API."
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

### Fine-grained access tokens for "Create a reply for a review comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Create a reply for a review comment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pull_numberintegerRequiredThe number that identifies the pull request.
comment_idintegerRequiredThe unique identifier of the comment.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the comment.

[TABLE]
Name, Type, Description
bodystringRequiredThe text of the review comment.
[/TABLE]
The text of the review comment.

### HTTP response status codes for "Create a reply for a review comment"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
[/TABLE]
Created
Resource not found

### Code samples for "Create a reply for a review comment"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/comments/COMMENT_ID/replies \
  -d '{"body":"Great stuff!"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
  "pull_request_review_id": 42,
  "id": 10,
  "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
  "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
  "path": "file1.txt",
  "position": 1,
  "original_position": 4,
  "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
  "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
  "in_reply_to_id": 426899381,
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
  "body": "Great stuff!",
  "created_at": "2011-04-14T16:00:49Z",
  "updated_at": "2011-04-14T16:00:49Z",
  "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "author_association": "NONE",
  "_links": {
    "self": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
    },
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
    }
  },
  "start_line": 1,
  "original_start_line": 1,
  "start_side": "RIGHT",
  "line": 2,
  "original_line": 2,
  "side": "RIGHT"
}
```