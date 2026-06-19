# REST API endpoints for pull request reviews

*Source: https://docs.github.com/en/rest/pulls/reviews*

---

# REST API endpoints for pull request reviews
Use the REST API to interact with pull request reviews.

## About pull request reviews
Pull Request Reviews are groups of pull request review comments on a pull request, grouped together with a state and optional body comment.

## List reviews for a pull request
Lists all reviews for a specified pull request. The list of reviews returns in chronological order.
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

### Fine-grained access tokens for "List reviews for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List reviews for a pull request"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List reviews for a pull request"

[TABLE]
Status code | Description
200 | The list of reviews returns in chronological order.
[/TABLE]
The list of reviews returns in chronological order.

### Code samples for "List reviews for a pull request"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews
```

#### The list of reviews returns in chronological order.
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 80,
    "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
    "body": "Here is the body for the review.",
    "state": "APPROVED",
    "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
    "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
    "_links": {
      "html": {
        "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
      },
      "pull_request": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
      }
    },
    "submitted_at": "2019-11-17T17:43:43Z",
    "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
    "author_association": "COLLABORATOR"
  }
]
```

## Create a review for a pull request
Creates a review on a specified pull request.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API" and "Best practices for using the REST API."
Pull request reviews created in thePENDINGstate are not submitted and therefore do not include thesubmitted_atproperty in the response. To create a pending review for a pull request, leave theeventparameter blank. For more information about submitting aPENDINGreview, see "Submit a review for a pull request."
Note
To comment on a specific line in a file, you need to first determine the position of that line in the diff. To see a pull request diff, add theapplication/vnd.github.v3.diffmedia type to theAcceptheader of a call to theGet a pull requestendpoint.
Thepositionvalue equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
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

### Fine-grained access tokens for "Create a review for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Create a review for a pull request"

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
commit_idstringThe SHA of the commit that needs a review. Not using the latest commit SHA may render your review comment outdated if a subsequent commit modifies the line you specify as theposition. Defaults to the most recent commit in the pull request when you do not specify a value.
bodystringRequiredwhen usingREQUEST_CHANGESorCOMMENTfor theeventparameter. The body text of the pull request review.
eventstringThe review action you want to perform. The review actions include:APPROVE,REQUEST_CHANGES, orCOMMENT. By leaving this blank, you set the review action state toPENDING, which means you will need tosubmit the pull request reviewwhen you are ready.Can be one of:APPROVE,REQUEST_CHANGES,COMMENT
commentsarray of objectsUse the following table to specify the location, destination, and contents of the draft review comment.
Properties ofcommentsName, Type, DescriptionpathstringRequiredThe relative path to the file that necessitates a review comment.positionintegerThe position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. Thepositionvalue equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.bodystringRequiredText of the review comment.lineintegersidestringstart_lineintegerstart_sidestring | Name, Type, Description | pathstringRequiredThe relative path to the file that necessitates a review comment. | positionintegerThe position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. Thepositionvalue equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file. | bodystringRequiredText of the review comment. | lineinteger | sidestring | start_lineinteger | start_sidestring
Name, Type, Description
pathstringRequiredThe relative path to the file that necessitates a review comment.
positionintegerThe position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. Thepositionvalue equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
bodystringRequiredText of the review comment.
lineinteger
sidestring
start_lineinteger
start_sidestring
[/TABLE]
The SHA of the commit that needs a review. Not using the latest commit SHA may render your review comment outdated if a subsequent commit modifies the line you specify as theposition. Defaults to the most recent commit in the pull request when you do not specify a value.
Requiredwhen usingREQUEST_CHANGESorCOMMENTfor theeventparameter. The body text of the pull request review.
The review action you want to perform. The review actions include:APPROVE,REQUEST_CHANGES, orCOMMENT. By leaving this blank, you set the review action state toPENDING, which means you will need tosubmit the pull request reviewwhen you are ready.
Can be one of:APPROVE,REQUEST_CHANGES,COMMENT

```
REQUEST_CHANGES
```
Use the following table to specify the location, destination, and contents of the draft review comment.

[TABLE]
Name, Type, Description
pathstringRequiredThe relative path to the file that necessitates a review comment.
positionintegerThe position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. Thepositionvalue equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
bodystringRequiredText of the review comment.
lineinteger
sidestring
start_lineinteger
start_sidestring
[/TABLE]
The relative path to the file that necessitates a review comment.
The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. Thepositionvalue equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
Text of the review comment.

### HTTP response status codes for "Create a review for a pull request"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Forbidden
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a review for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews \
  -d '{"commit_id":"ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091","body":"This is close to perfect! Please address the suggested inline change.","event":"REQUEST_CHANGES","comments":[{"path":"file.md","position":6,"body":"Please add more information here, and fix this typo."}]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 80,
  "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
  "body": "This is close to perfect! Please address the suggested inline change.",
  "state": "CHANGES_REQUESTED",
  "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
  "_links": {
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
    }
  },
  "submitted_at": "2019-11-17T17:43:43Z",
  "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
  "author_association": "COLLABORATOR"
}
```

## Get a review for a pull request
Retrieves a pull request review by its ID.
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

### Fine-grained access tokens for "Get a review for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a review for a pull request"

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
review_idintegerRequiredThe unique identifier of the review.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the review.

### HTTP response status codes for "Get a review for a pull request"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a review for a pull request"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews/REVIEW_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 80,
  "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
  "body": "Here is the body for the review.",
  "state": "APPROVED",
  "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
  "_links": {
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
    }
  },
  "submitted_at": "2019-11-17T17:43:43Z",
  "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
  "author_association": "COLLABORATOR"
}
```

## Update a review for a pull request
Updates the contents of a specified review summary comment.
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

### Fine-grained access tokens for "Update a review for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Update a review for a pull request"

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
review_idintegerRequiredThe unique identifier of the review.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the review.

[TABLE]
Name, Type, Description
bodystringRequiredThe body text of the pull request review.
[/TABLE]
The body text of the pull request review.

### HTTP response status codes for "Update a review for a pull request"

[TABLE]
Status code | Description
200 | OK
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Validation failed, or the endpoint has been spammed.

### Code samples for "Update a review for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews/REVIEW_ID \
  -d '{"body":"This is close to perfect! Please address the suggested inline change. And add more about this."}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 80,
  "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
  "body": "This is close to perfect! Please address the suggested inline change. And add more about this.",
  "state": "CHANGES_REQUESTED",
  "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
  "_links": {
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
    }
  },
  "submitted_at": "2019-11-17T17:43:43Z",
  "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
  "author_association": "COLLABORATOR"
}
```

## Delete a pending review for a pull request
Deletes a pull request review that has not been submitted. Submitted reviews cannot be deleted.
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

### Fine-grained access tokens for "Delete a pending review for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Delete a pending review for a pull request"

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
review_idintegerRequiredThe unique identifier of the review.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the review.

### HTTP response status codes for "Delete a pending review for a pull request"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete a pending review for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews/REVIEW_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 80,
  "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
  "body": "This is close to perfect! Please address the suggested inline change.",
  "state": "CHANGES_REQUESTED",
  "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
  "_links": {
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
    }
  },
  "submitted_at": "2019-11-17T17:43:43Z",
  "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
  "author_association": "COLLABORATOR"
}
```

## List comments for a pull request review
Lists comments for a specific pull request review.
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

### Fine-grained access tokens for "List comments for a pull request review"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List comments for a pull request review"

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
review_idintegerRequiredThe unique identifier of the review.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the review.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List comments for a pull request review"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List comments for a pull request review"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews/REVIEW_ID/comments
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
    }
  }
]
```

## Dismiss a review for a pull request
Dismisses a specified review on a pull request.
Note
To dismiss a pull request review on aprotected branch, you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews.
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

### Fine-grained access tokens for "Dismiss a review for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Dismiss a review for a pull request"

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
review_idintegerRequiredThe unique identifier of the review.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the review.

[TABLE]
Name, Type, Description
messagestringRequiredThe message for the pull request review dismissal
eventstringValue:DISMISS
[/TABLE]
The message for the pull request review dismissal
Value:DISMISS

### HTTP response status codes for "Dismiss a review for a pull request"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Dismiss a review for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews/REVIEW_ID/dismissals \
  -d '{"message":"You are dismissed","event":"DISMISS"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 80,
  "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
  "body": "Here is the body for the review.",
  "state": "DISMISSED",
  "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
  "_links": {
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
    }
  },
  "submitted_at": "2019-11-17T17:43:43Z",
  "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
  "author_association": "COLLABORATOR"
}
```

## Submit a review for a pull request
Submits a pending review for a pull request. For more information about creating a pending review for a pull request, see "Create a review for a pull request."
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

### Fine-grained access tokens for "Submit a review for a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Pull requests" repository permissions (write)

### Parameters for "Submit a review for a pull request"

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
review_idintegerRequiredThe unique identifier of the review.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.
The unique identifier of the review.

[TABLE]
Name, Type, Description
bodystringThe body text of the pull request review
eventstringRequiredThe review action you want to perform. The review actions include:APPROVE,REQUEST_CHANGES, orCOMMENT. When you leave this blank, the API returnsHTTP 422 (Unrecognizable entity)and sets the review action state toPENDING, which means you will need to re-submit the pull request review using a review action.Can be one of:APPROVE,REQUEST_CHANGES,COMMENT
[/TABLE]
The body text of the pull request review
The review action you want to perform. The review actions include:APPROVE,REQUEST_CHANGES, orCOMMENT. When you leave this blank, the API returnsHTTP 422 (Unrecognizable entity)and sets the review action state toPENDING, which means you will need to re-submit the pull request review using a review action.
Can be one of:APPROVE,REQUEST_CHANGES,COMMENT

```
REQUEST_CHANGES
```

### HTTP response status codes for "Submit a review for a pull request"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Submit a review for a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/reviews/REVIEW_ID/events \
  -d '{"body":"Here is the body for the review.","event":"REQUEST_CHANGES"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 80,
  "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
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
  "body": "Here is the body for the review.",
  "state": "APPROVED",
  "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
  "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
  "_links": {
    "html": {
      "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
    },
    "pull_request": {
      "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
    }
  },
  "submitted_at": "2019-11-17T17:43:43Z",
  "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
  "author_association": "COLLABORATOR"
}
```