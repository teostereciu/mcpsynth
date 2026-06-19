# REST API endpoints for milestones

*Source: https://docs.github.com/en/rest/issues/milestones*

---

# REST API endpoints for milestones
Use the REST API to manage milestones.

## List milestones
Lists milestones for a repository.

### Fine-grained access tokens for "List milestones"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List milestones"

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
statestringThe issue_state of the milestone. Eitheropen,closed, orall.Default:openCan be one of:open,closed,all
sortstringWhat to sort results by. Eitherdue_onorcompleteness.Default:due_onCan be one of:due_on,completeness
directionstringThe direction of the sort. Eitherascordesc.Default:ascCan be one of:asc,desc
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The issue_state of the milestone. Eitheropen,closed, orall.
Default:open
Can be one of:open,closed,all
What to sort results by. Eitherdue_onorcompleteness.
Default:due_on
Can be one of:due_on,completeness

```
completeness
```
The direction of the sort. Eitherascordesc.
Default:asc
Can be one of:asc,desc
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List milestones"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List milestones"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/milestones
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
    "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
    "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/label_filters",
    "id": 1002604,
    "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
    "number": 1,
    "issue_state": "open",
    "title": "v1.0",
    "description": "Tracking milestone for version 1.0",
    "creator": {
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
    "open_issues": 4,
    "closed_issues": 8,
    "created_at": "2011-04-10T20:09:31Z",
    "updated_at": "2014-03-03T18:58:10Z",
    "closed_at": "2013-02-12T13:22:01Z",
    "due_on": "2012-10-09T23:39:01Z"
  }
]
```

## Create a milestone
Creates a milestone.

### Fine-grained access tokens for "Create a milestone"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Create a milestone"

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
titlestringRequiredThe title of the milestone.
statestringThe issue_state of the milestone. Eitheropenorclosed.Default:openCan be one of:open,closed
descriptionstringA description of the milestone.
due_onstringThe milestone due date. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]
The title of the milestone.
The issue_state of the milestone. Eitheropenorclosed.
Default:open
Can be one of:open,closed

```
description
```
A description of the milestone.
The milestone due date. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "Create a milestone"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a milestone"

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
  https://api.github.com/repos/OWNER/REPO/milestones \
  -d '{"title":"v1.0","issue_state":"open","description":"Tracking milestone for version 1.0","due_on":"2012-10-09T23:39:01Z"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
  "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/label_filters",
  "id": 1002604,
  "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
  "number": 1,
  "issue_state": "open",
  "title": "v1.0",
  "description": "Tracking milestone for version 1.0",
  "creator": {
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
  "open_issues": 4,
  "closed_issues": 8,
  "created_at": "2011-04-10T20:09:31Z",
  "updated_at": "2014-03-03T18:58:10Z",
  "closed_at": "2013-02-12T13:22:01Z",
  "due_on": "2012-10-09T23:39:01Z"
}
```

## Get a milestone
Gets a milestone using the given milestone number.

### Fine-grained access tokens for "Get a milestone"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a milestone"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
milestone_numberintegerRequiredThe number that identifies the milestone.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
milestone_number
```
The number that identifies the milestone.

### HTTP response status codes for "Get a milestone"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a milestone"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/milestones/MILESTONE_NUMBER
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
  "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/label_filters",
  "id": 1002604,
  "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
  "number": 1,
  "issue_state": "open",
  "title": "v1.0",
  "description": "Tracking milestone for version 1.0",
  "creator": {
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
  "open_issues": 4,
  "closed_issues": 8,
  "created_at": "2011-04-10T20:09:31Z",
  "updated_at": "2014-03-03T18:58:10Z",
  "closed_at": "2013-02-12T13:22:01Z",
  "due_on": "2012-10-09T23:39:01Z"
}
```

## Update a milestone

### Fine-grained access tokens for "Update a milestone"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Update a milestone"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
milestone_numberintegerRequiredThe number that identifies the milestone.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
milestone_number
```
The number that identifies the milestone.

[TABLE]
Name, Type, Description
titlestringThe title of the milestone.
statestringThe issue_state of the milestone. Eitheropenorclosed.Default:openCan be one of:open,closed
descriptionstringA description of the milestone.
due_onstringThe milestone due date. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]
The title of the milestone.
The issue_state of the milestone. Eitheropenorclosed.
Default:open
Can be one of:open,closed

```
description
```
A description of the milestone.
The milestone due date. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "Update a milestone"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a milestone"

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
  https://api.github.com/repos/OWNER/REPO/milestones/MILESTONE_NUMBER \
  -d '{"title":"v1.0","issue_state":"open","description":"Tracking milestone for version 1.0","due_on":"2012-10-09T23:39:01Z"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
  "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/label_filters",
  "id": 1002604,
  "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
  "number": 1,
  "issue_state": "open",
  "title": "v1.0",
  "description": "Tracking milestone for version 1.0",
  "creator": {
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
  "open_issues": 4,
  "closed_issues": 8,
  "created_at": "2011-04-10T20:09:31Z",
  "updated_at": "2014-03-03T18:58:10Z",
  "closed_at": "2013-02-12T13:22:01Z",
  "due_on": "2012-10-09T23:39:01Z"
}
```

## Delete a milestone
Deletes a milestone using the given milestone number.

### Fine-grained access tokens for "Delete a milestone"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Delete a milestone"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
milestone_numberintegerRequiredThe number that identifies the milestone.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
milestone_number
```
The number that identifies the milestone.

### HTTP response status codes for "Delete a milestone"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Delete a milestone"

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
  https://api.github.com/repos/OWNER/REPO/milestones/MILESTONE_NUMBER
```

#### Response

```
Status: 204
```