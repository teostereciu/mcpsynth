# REST API endpoints for events

*Source: https://docs.github.com/en/rest/activity/events*

---

# REST API endpoints for events
Use the REST API to interact with GitHub events.

## About GitHub events
GitHub events power the various activity streams on the site.
You can use the REST API to return different types of events triggered by activity on GitHub. For more information about the specific events that you can receive, seeGitHub event types. Endpoints for repository issues are also available. For more information, seeREST API endpoints for issue events.
Events are optimized for polling with the "ETag" header. If no new events have been triggered, you will see a "304 Not Modified" response, and your current rate limit will be untouched. There is also an "X-Poll-Interval" header that specifies how often (in seconds) you are allowed to poll. In times of high server load, the time may increase. Please obey the header.

```
$curl -I https://api.github.com/users/tater/events>HTTP/2 200>X-Poll-Interval: 60>ETag:"a18c3bded88eb5dbb5c849a489412bf3"#The quotes around the ETag value are important$curl -I https://api.github.com/users/tater/events \
$    -H'If-None-Match: "a18c3bded88eb5dbb5c849a489412bf3"'>HTTP/2 304>X-Poll-Interval: 60
```

```
$curl -I https://api.github.com/users/tater/events>HTTP/2 200>X-Poll-Interval: 60>ETag:"a18c3bded88eb5dbb5c849a489412bf3"#The quotes around the ETag value are important$curl -I https://api.github.com/users/tater/events \
$    -H'If-None-Match: "a18c3bded88eb5dbb5c849a489412bf3"'>HTTP/2 304>X-Poll-Interval: 60
```
The timeline will include up to 300 events. Only events created within the past 30 days will be included. Events older than 30 days will not be included (even if the total number of events in the timeline is less than 300).

## List public events
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List public events"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List public events"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:15
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:15
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List public events"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Forbidden
503 | Service unavailable
[/TABLE]
OK
Not modified
Forbidden
Service unavailable

### Code samples for "List public events"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/events
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
    "id": "22249084947",
    "type": "WatchEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-07T07:50:26Z"
  }
]
```

## List public events for a network of repositories
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List public events for a network of repositories"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List public events for a network of repositories"

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

### HTTP response status codes for "List public events for a network of repositories"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
304 | Not modified
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Moved permanently
Not modified
Forbidden
Resource not found

### Code samples for "List public events for a network of repositories"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/networks/OWNER/REPO/events
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
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22237752260",
    "type": "WatchEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2022-06-08T23:29:25Z"
  }
]
```

## List public organization events
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List public organization events"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List public organization events"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List public organization events"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List public organization events"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/events
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
    "id": "22237752260",
    "type": "WatchEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octo-org/octo-repo",
      "url": "https://api.github.com/repos/octo-org/octo-repo"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2022-06-08T23:29:25Z",
    "org": {
      "id": 9919,
      "login": "octo-org",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/octo-org",
      "avatar_url": "https://avatars.githubusercontent.com/u/9919?"
    }
  },
  {
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octo-org/octo-repo",
      "url": "https://api.github.com/repos/octo-org/octo-repo"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z",
    "org": {
      "id": 9919,
      "login": "octo-org",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/octo-org",
      "avatar_url": "https://avatars.githubusercontent.com/u/9919?"
    }
  }
]
```

## List repository events
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List repository events"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List repository events"

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

### HTTP response status codes for "List repository events"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository events"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/events
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
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22237752260",
    "type": "WatchEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2022-06-08T23:29:25Z"
  }
]
```

## List events for the authenticated user
If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events.Optional: use the fine-grained token with following permission set to view private events: "Events" user permissions (read).
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List events for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List events for the authenticated user"

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

### HTTP response status codes for "List events for the authenticated user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List events for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/events
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
    "id": "22249084947",
    "type": "WatchEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": false,
    "created_at": "2022-06-07T07:50:26Z"
  }
]
```

## List organization events for the authenticated user
This is the user's organization dashboard. You must be authenticated as the user to view this.
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List organization events for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Events" organization permissions (read)

### Parameters for "List organization events for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The handle for the GitHub user account.
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List organization events for the authenticated user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List organization events for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/events/orgs/ORG
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
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octo-org/octo-repo",
      "url": "https://api.github.com/repos/octo-org/octo-repo"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": false,
    "created_at": "2022-06-09T12:47:28Z",
    "org": {
      "id": 9919,
      "login": "octo-org",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/octo-org",
      "avatar_url": "https://avatars.githubusercontent.com/u/9919?"
    }
  },
  {
    "id": "22196946742",
    "type": "CreateEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octo-org/octo-repo",
      "url": "https://api.github.com/repos/octo-org/octo-repo"
    },
    "payload": {
      "ref": "master",
      "ref_type": "repository",
      "full_ref": "refs/heads/master",
      "master_branch": "master",
      "description": null,
      "pusher_type": "user"
    },
    "public": false,
    "created_at": "2022-06-07T07:50:26Z",
    "org": {
      "id": 9919,
      "login": "octo-org",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/octo-org",
      "avatar_url": "https://avatars.githubusercontent.com/u/9919?"
    }
  }
]
```

## List public events for a user
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List public events for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List public events for a user"

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

### HTTP response status codes for "List public events for a user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List public events for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/events/public
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
    "id": "22249084947",
    "type": "WatchEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-08T23:29:25Z"
  }
]
```

## List events received by the authenticated user
These are events that you've received by watching repositories and following users. If you are authenticated as the
given user, you will see private events. Otherwise, you'll only see public events.
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List events received by the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List events received by the authenticated user"

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

### HTTP response status codes for "List events received by the authenticated user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List events received by the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/received_events
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
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22196946742",
    "type": "CreateEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "ref": "master",
      "ref_type": "repository",
      "full_ref": "refs/heads/master",
      "master_branch": "master",
      "description": null,
      "pusher_type": "user"
    },
    "public": false,
    "created_at": "2022-06-07T07:50:26Z"
  }
]
```

## List public events received by a user
Note
This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Fine-grained access tokens for "List public events received by a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List public events received by a user"

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

### HTTP response status codes for "List public events received by a user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List public events received by a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/received_events/public
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
    "id": "22249084964",
    "type": "PushEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "repository_id": 1296269,
      "push_id": 10115855396,
      "ref": "refs/heads/master",
      "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
      "before": "883efe034920928c47fe18598c01249d1a9fdabd"
    },
    "public": true,
    "created_at": "2022-06-09T12:47:28Z"
  },
  {
    "id": "22196946742",
    "type": "CreateEvent",
    "actor": {
      "id": 583231,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
    },
    "repo": {
      "id": 1296269,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "ref": "master",
      "ref_type": "repository",
      "full_ref": "refs/heads/master",
      "master_branch": "master",
      "description": null,
      "pusher_type": "user"
    },
    "public": false,
    "created_at": "2022-06-07T07:50:26Z"
  }
]
```