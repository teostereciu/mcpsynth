# REST API endpoints for repository statistics

*Source: https://docs.github.com/en/rest/metrics/statistics*

---

# REST API endpoints for repository statistics
Use the REST API to fetch the data that GitHub uses for visualizing different types of repository activity.

## About repository statistics
You can use the REST API to fetch the data that GitHub uses for visualizing different types of repository activity.

### Best practices for caching
Computing repository statistics is an expensive operation, so we try to return cached
data whenever possible. If the data hasn't been cached when you query a repository's
statistics, you'll receive a202response; a background job is also fired to
start compiling these statistics. You should allow the job a short time to complete, and
then submit the request again. If the job has completed, that request will receive a200response with the statistics in the response body.
Repository statistics are cached by the SHA of the repository's default branch; pushing to the default branch resets the statistics cache.

### Statistics exclude some types of commits
The statistics exposed by the API match the statistics shown bydifferent repository graphs.
To summarize this:
- All statistics exclude merge commits.
- Contributor statistics also exclude empty commits.

## Get the weekly commit activity
Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
Note
This endpoint can only be used for repositories with fewer than 10,000 commits. If the repository contains 10,000 or more commits, a 422 status code will be returned.

### Fine-grained access tokens for "Get the weekly commit activity"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the weekly commit activity"

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

### HTTP response status codes for "Get the weekly commit activity"

[TABLE]
Status code | Description
200 | Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
202 | Accepted
204 | A header with no content is returned.
422 | Repository contains more than 10,000 commits
[/TABLE]
Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
Accepted
A header with no content is returned.
Repository contains more than 10,000 commits

### Code samples for "Get the weekly commit activity"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/stats/code_frequency
```

#### Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
- Example response
- Response schema

```
Status: 200
```

```
[
  [
    1302998400,
    1124,
    -435
  ]
]
```

## Get the last year of commit activity
Returns the last year of commit activity grouped by week. Thedaysarray is a group of commits per day, starting onSunday.

### Fine-grained access tokens for "Get the last year of commit activity"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the last year of commit activity"

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

### HTTP response status codes for "Get the last year of commit activity"

[TABLE]
Status code | Description
200 | OK
202 | Accepted
204 | A header with no content is returned.
[/TABLE]
OK
Accepted
A header with no content is returned.

### Code samples for "Get the last year of commit activity"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/stats/commit_activity
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
    "days": [
      0,
      3,
      26,
      20,
      39,
      1,
      0
    ],
    "total": 89,
    "week": 1336280400
  }
]
```

## Get all contributor commit activity
Returns thetotalnumber of commits authored by the contributor. In addition, the response includes a Weekly Hash (weeksarray) with the following information:
- w- Start of the week, given as aUnix timestamp.
- a- Number of additions
- d- Number of deletions
- c- Number of commits
Note
This endpoint will return0values for all addition and deletion counts in repositories with 10,000 or more commits.

### Fine-grained access tokens for "Get all contributor commit activity"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get all contributor commit activity"

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

### HTTP response status codes for "Get all contributor commit activity"

[TABLE]
Status code | Description
200 | OK
202 | Accepted
204 | A header with no content is returned.
[/TABLE]
OK
Accepted
A header with no content is returned.

### Code samples for "Get all contributor commit activity"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/stats/contributors
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
    "author": {
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
    "total": 135,
    "weeks": [
      {
        "w": 1367712000,
        "a": 6898,
        "d": 77,
        "c": 10
      }
    ]
  }
]
```

## Get the weekly commit count
Returns the total commit counts for theownerand total commit counts inall.allis everyone combined, including theownerin the last 52 weeks. If you'd like to get the commit counts for non-owners, you can subtractownerfromall.
The array order is oldest week (index 0) to most recent week.
The most recent week is seven days ago at UTC midnight to today at UTC midnight.

### Fine-grained access tokens for "Get the weekly commit count"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the weekly commit count"

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

### HTTP response status codes for "Get the weekly commit count"

[TABLE]
Status code | Description
200 | The array order is oldest week (index 0) to most recent week.
404 | Resource not found
[/TABLE]
The array order is oldest week (index 0) to most recent week.
Resource not found

### Code samples for "Get the weekly commit count"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/stats/participation
```

#### The array order is oldest week (index 0) to most recent week.
- Example response
- Response schema

```
Status: 200
```

```
{
  "all": [
    11,
    21,
    15,
    2,
    8,
    1,
    8,
    23,
    17,
    21,
    11,
    10,
    33,
    91,
    38,
    34,
    22,
    23,
    32,
    3,
    43,
    87,
    71,
    18,
    13,
    5,
    13,
    16,
    66,
    27,
    12,
    45,
    110,
    117,
    13,
    8,
    18,
    9,
    19,
    26,
    39,
    12,
    20,
    31,
    46,
    91,
    45,
    10,
    24,
    9,
    29,
    7
  ],
  "owner": [
    3,
    2,
    3,
    0,
    2,
    0,
    5,
    14,
    7,
    9,
    1,
    5,
    0,
    48,
    19,
    2,
    0,
    1,
    10,
    2,
    23,
    40,
    35,
    8,
    8,
    2,
    10,
    6,
    30,
    0,
    2,
    9,
    53,
    104,
    3,
    3,
    10,
    4,
    7,
    11,
    21,
    4,
    4,
    22,
    26,
    63,
    11,
    2,
    14,
    1,
    10,
    3
  ]
}
```

## Get the hourly commit count for each day
Each array contains the day number, hour number, and number of commits:
- 0-6: Sunday - Saturday
- 0-23: Hour of day
- Number of commits
For example,[2, 14, 25]indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.

### Fine-grained access tokens for "Get the hourly commit count for each day"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the hourly commit count for each day"

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

### HTTP response status codes for "Get the hourly commit count for each day"

[TABLE]
Status code | Description
200 | For example,[2, 14, 25]indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.
204 | A header with no content is returned.
[/TABLE]
For example,[2, 14, 25]indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.
A header with no content is returned.

### Code samples for "Get the hourly commit count for each day"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/stats/punch_card
```

#### For example,[2, 14, 25]indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.
- Example response
- Response schema

```
Status: 200
```

```
[
  [
    0,
    0,
    5
  ],
  [
    0,
    1,
    43
  ],
  [
    0,
    2,
    21
  ]
]
```