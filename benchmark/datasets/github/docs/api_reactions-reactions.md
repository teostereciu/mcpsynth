# REST API endpoints for reactions

*Source: https://docs.github.com/en/rest/reactions/reactions*

---

# REST API endpoints for reactions
Use the REST API to interact with reactions on GitHub.

## About reactions
You can create and manage reactions to comments, issues, pull requests, and discussions on GitHub. When creating a reaction, the allowed values for thecontentparameter are as follows (with the corresponding emoji for reference):

[TABLE]
Content | Emoji
+1 | 👍
-1 | 👎
laugh | 😄
confused | 😕
heart | ❤️
hooray | 🎉
rocket | 🚀
eyes | 👀
[/TABLE]

## List reactions for a commit comment
List the reactions to acommit comment.

### Fine-grained access tokens for "List reactions for a commit comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List reactions for a commit comment"

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
contentstringReturns a singlereaction type. Omit this parameter to list all reactions to a commit comment.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Returns a singlereaction type. Omit this parameter to list all reactions to a commit comment.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List reactions for a commit comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List reactions for a commit comment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/comments/COMMENT_ID/reactions
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
    "node_id": "MDg6UmVhY3Rpb24x",
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
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z"
  }
]
```

## Create reaction for a commit comment
Create a reaction to acommit comment. A response with an HTTP200status means that you already added the reaction type to this commit comment.

### Fine-grained access tokens for "Create reaction for a commit comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create reaction for a commit comment"

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
contentstringRequiredThereaction typeto add to the commit comment.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
[/TABLE]
Thereaction typeto add to the commit comment.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes

### HTTP response status codes for "Create reaction for a commit comment"

[TABLE]
Status code | Description
200 | Reaction exists
201 | Reaction created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Reaction exists
Reaction created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create reaction for a commit comment"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/comments/COMMENT_ID/reactions \
  -d '{"content":"heart"}'
```

#### Reaction exists
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "node_id": "MDg6UmVhY3Rpb24x",
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
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z"
}
```

## Delete a commit comment reaction
Note
You can also specify a repository byrepository_idusing the routeDELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id.
Delete a reaction to acommit comment.

### Fine-grained access tokens for "Delete a commit comment reaction"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Delete a commit comment reaction"

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
reaction_idintegerRequiredThe unique identifier of the reaction.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the comment.

```
reaction_id
```
The unique identifier of the reaction.

### HTTP response status codes for "Delete a commit comment reaction"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a commit comment reaction"

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
  https://api.github.com/repos/OWNER/REPO/comments/COMMENT_ID/reactions/REACTION_ID
```

#### Response

```
Status: 204
```

## List reactions for an issue comment
List the reactions to anissue comment.

### Fine-grained access tokens for "List reactions for an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List reactions for an issue comment"

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
contentstringReturns a singlereaction type. Omit this parameter to list all reactions to an issue comment.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Returns a singlereaction type. Omit this parameter to list all reactions to an issue comment.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List reactions for an issue comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List reactions for an issue comment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID/reactions
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
    "node_id": "MDg6UmVhY3Rpb24x",
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
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z"
  }
]
```

## Create reaction for an issue comment
Create a reaction to anissue comment. A response with an HTTP200status means that you already added the reaction type to this issue comment.

### Fine-grained access tokens for "Create reaction for an issue comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (write)

### Parameters for "Create reaction for an issue comment"

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
contentstringRequiredThereaction typeto add to the issue comment.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
[/TABLE]
Thereaction typeto add to the issue comment.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes

### HTTP response status codes for "Create reaction for an issue comment"

[TABLE]
Status code | Description
200 | Reaction exists
201 | Reaction created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Reaction exists
Reaction created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create reaction for an issue comment"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID/reactions \
  -d '{"content":"heart"}'
```

#### Reaction exists
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "node_id": "MDg6UmVhY3Rpb24x",
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
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z"
}
```

## Delete an issue comment reaction
Note
You can also specify a repository byrepository_idusing the routeDELETE delete /repositories/:repository_id/issues/comments/:comment_id/reactions/:reaction_id.
Delete a reaction to anissue comment.

### Fine-grained access tokens for "Delete an issue comment reaction"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (write)

### Parameters for "Delete an issue comment reaction"

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
reaction_idintegerRequiredThe unique identifier of the reaction.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the comment.

```
reaction_id
```
The unique identifier of the reaction.

### HTTP response status codes for "Delete an issue comment reaction"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an issue comment reaction"

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
  https://api.github.com/repos/OWNER/REPO/issues/comments/COMMENT_ID/reactions/REACTION_ID
```

#### Response

```
Status: 204
```

## List reactions for an issue
List the reactions to anissue.

### Fine-grained access tokens for "List reactions for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List reactions for an issue"

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
contentstringReturns a singlereaction type. Omit this parameter to list all reactions to an issue.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Returns a singlereaction type. Omit this parameter to list all reactions to an issue.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List reactions for an issue"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
410 | Gone
[/TABLE]
OK
Resource not found
Gone

### Code samples for "List reactions for an issue"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/reactions
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
    "node_id": "MDg6UmVhY3Rpb24x",
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
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z"
  }
]
```

## Create reaction for an issue
Create a reaction to anissue. A response with an HTTP200status means that you already added the reaction type to this issue.

### Fine-grained access tokens for "Create reaction for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (write)

### Parameters for "Create reaction for an issue"

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
contentstringRequiredThereaction typeto add to the issue.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
[/TABLE]
Thereaction typeto add to the issue.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes

### HTTP response status codes for "Create reaction for an issue"

[TABLE]
Status code | Description
200 | OK
201 | Created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create reaction for an issue"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/reactions \
  -d '{"content":"heart"}'
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
  "node_id": "MDg6UmVhY3Rpb24x",
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
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z"
}
```

## Delete an issue reaction
Note
You can also specify a repository byrepository_idusing the routeDELETE /repositories/:repository_id/issues/:issue_number/reactions/:reaction_id.
Delete a reaction to anissue.

### Fine-grained access tokens for "Delete an issue reaction"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (write)

### Parameters for "Delete an issue reaction"

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
reaction_idintegerRequiredThe unique identifier of the reaction.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
issue_number
```
The number that identifies the issue.

```
reaction_id
```
The unique identifier of the reaction.

### HTTP response status codes for "Delete an issue reaction"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an issue reaction"

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
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/reactions/REACTION_ID
```

#### Response

```
Status: 204
```

## List reactions for a pull request review comment
List the reactions to apull request review comment.

### Fine-grained access tokens for "List reactions for a pull request review comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List reactions for a pull request review comment"

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
contentstringReturns a singlereaction type. Omit this parameter to list all reactions to a pull request review comment.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Returns a singlereaction type. Omit this parameter to list all reactions to a pull request review comment.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List reactions for a pull request review comment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List reactions for a pull request review comment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/comments/COMMENT_ID/reactions
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
    "node_id": "MDg6UmVhY3Rpb24x",
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
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z"
  }
]
```

## Create reaction for a pull request review comment
Create a reaction to apull request review comment. A response with an HTTP200status means that you already added the reaction type to this pull request review comment.

### Fine-grained access tokens for "Create reaction for a pull request review comment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Create reaction for a pull request review comment"

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
contentstringRequiredThereaction typeto add to the pull request review comment.Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes
[/TABLE]
Thereaction typeto add to the pull request review comment.
Can be one of:+1,-1,laugh,confused,heart,hooray,rocket,eyes

### HTTP response status codes for "Create reaction for a pull request review comment"

[TABLE]
Status code | Description
200 | Reaction exists
201 | Reaction created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Reaction exists
Reaction created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create reaction for a pull request review comment"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/comments/COMMENT_ID/reactions \
  -d '{"content":"heart"}'
```

#### Reaction exists
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "node_id": "MDg6UmVhY3Rpb24x",
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
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z"
}
```

## Delete a pull request comment reaction
Note
You can also specify a repository byrepository_idusing the routeDELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.
Delete a reaction to apull request review comment.

### Fine-grained access tokens for "Delete a pull request comment reaction"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Delete a pull request comment reaction"

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
reaction_idintegerRequiredThe unique identifier of the reaction.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the comment.

```
reaction_id
```
The unique identifier of the reaction.

### HTTP response status codes for "Delete a pull request comment reaction"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a pull request comment reaction"

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
  https://api.github.com/repos/OWNER/REPO/pulls/comments/COMMENT_ID/reactions/REACTION_ID
```

#### Response

```
Status: 204
```

## List reactions for a release
List the reactions to arelease.

### Fine-grained access tokens for "List reactions for a release"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List reactions for a release"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
release_idintegerRequiredThe unique identifier of the release.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the release.

[TABLE]
Name, Type, Description
contentstringReturns a singlereaction type. Omit this parameter to list all reactions to a release.Can be one of:+1,laugh,heart,hooray,rocket,eyes
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Returns a singlereaction type. Omit this parameter to list all reactions to a release.
Can be one of:+1,laugh,heart,hooray,rocket,eyes
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List reactions for a release"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List reactions for a release"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/releases/RELEASE_ID/reactions
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
    "node_id": "MDg6UmVhY3Rpb24x",
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
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z"
  }
]
```

## Create reaction for a release
Create a reaction to arelease. A response with aStatus: 200 OKmeans that you already added the reaction type to this release.

### Fine-grained access tokens for "Create reaction for a release"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "Create reaction for a release"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
release_idintegerRequiredThe unique identifier of the release.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the release.

[TABLE]
Name, Type, Description
contentstringRequiredThereaction typeto add to the release.Can be one of:+1,laugh,heart,hooray,rocket,eyes
[/TABLE]
Thereaction typeto add to the release.
Can be one of:+1,laugh,heart,hooray,rocket,eyes

### HTTP response status codes for "Create reaction for a release"

[TABLE]
Status code | Description
200 | Reaction exists
201 | Reaction created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Reaction exists
Reaction created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create reaction for a release"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/releases/RELEASE_ID/reactions \
  -d '{"content":"heart"}'
```

#### Reaction exists
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "node_id": "MDg6UmVhY3Rpb24x",
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
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z"
}
```

## Delete a release reaction
Note
You can also specify a repository byrepository_idusing the routeDELETE delete /repositories/:repository_id/releases/:release_id/reactions/:reaction_id.
Delete a reaction to arelease.

### Fine-grained access tokens for "Delete a release reaction"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "Delete a release reaction"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
release_idintegerRequiredThe unique identifier of the release.
reaction_idintegerRequiredThe unique identifier of the reaction.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the release.

```
reaction_id
```
The unique identifier of the reaction.

### HTTP response status codes for "Delete a release reaction"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a release reaction"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/releases/RELEASE_ID/reactions/REACTION_ID
```

#### Response

```
Status: 204
```