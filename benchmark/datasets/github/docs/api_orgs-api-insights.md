# REST API endpoints for API Insights

*Source: https://docs.github.com/en/rest/orgs/api-insights*

---

# REST API endpoints for API Insights
Use the REST API to view statistics for API usage in an organization.

## Get route stats by actor
Get API request count statistics for an actor broken down by route within a specified time frame.

### Fine-grained access tokens for "Get route stats by actor"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get route stats by actor"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
actor_typestringRequiredThe type of the actorCan be one of:installation,classic_pat,fine_grained_pat,oauth_app,github_app_user_to_server
actor_idintegerRequiredThe ID of the actor
[/TABLE]
The organization name. The name is not case sensitive.
The type of the actor
Can be one of:installation,classic_pat,fine_grained_pat,oauth_app,github_app_user_to_server

```
installation
```

```
classic_pat
```

```
fine_grained_pat
```

```
github_app_user_to_server
```
The ID of the actor

[TABLE]
Name, Type, Description
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
sortarrayThe property to sort the results by.
api_route_substringstringProviding a substring will filter results where the API route contains the substring. This is a case-insensitive search.
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
The property to sort the results by.

```
api_route_substring
```
Providing a substring will filter results where the API route contains the substring. This is a case-insensitive search.

### HTTP response status codes for "Get route stats by actor"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get route stats by actor"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/route-stats/ACTOR_TYPE/ACTOR_ID?min_timestamp=MIN_TIMESTAMP"
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
    "http_method": "GET",
    "api_route": "/repositories/:repository_id",
    "total_request_count": 544665,
    "rate_limited_request_count": 13,
    "last_request_timestamp": "2024-09-18T15:43:03Z",
    "last_rate_limited_timestamp": "2024-09-18T06:30:09Z"
  }
]
```

## Get subject stats
Get API request statistics for all subjects within an organization within a specified time frame. Subjects can be users or GitHub Apps.

### Fine-grained access tokens for "Get subject stats"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get subject stats"

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
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
sortarrayThe property to sort the results by.
subject_name_substringstringProviding a substring will filter results where the subject name contains the substring. This is a case-insensitive search.
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
The property to sort the results by.

```
subject_name_substring
```
Providing a substring will filter results where the subject name contains the substring. This is a case-insensitive search.

### HTTP response status codes for "Get subject stats"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get subject stats"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/subject-stats?min_timestamp=MIN_TIMESTAMP"
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
    "subject_type": "installation",
    "subject_id": 954453,
    "subject_name": "GitHub Actions",
    "total_request_count": 544665,
    "rate_limited_request_count": 13,
    "last_request_timestamp": "2024-09-18T15:43:03Z",
    "last_rate_limited_timestamp": "2024-09-18T06:30:09Z"
  }
]
```

## Get summary stats
Get overall statistics of API requests made within an organization by all users and apps within a specified time frame.

### Fine-grained access tokens for "Get summary stats"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get summary stats"

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
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "Get summary stats"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get summary stats"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/summary-stats?min_timestamp=MIN_TIMESTAMP"
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_request_count": 34225,
  "rate_limited_request_count": 23
}
```

## Get summary stats by user
Get overall statistics of API requests within the organization for a user.

### Fine-grained access tokens for "Get summary stats by user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get summary stats by user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
user_idstringRequiredThe ID of the user to query for stats
[/TABLE]
The organization name. The name is not case sensitive.
The ID of the user to query for stats

[TABLE]
Name, Type, Description
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "Get summary stats by user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get summary stats by user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/summary-stats/users/USER_ID?min_timestamp=MIN_TIMESTAMP"
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_request_count": 34225,
  "rate_limited_request_count": 23
}
```

## Get summary stats by actor
Get overall statistics of API requests within the organization made by a specific actor. Actors can be GitHub App installations, OAuth apps or other tokens on behalf of a user.

### Fine-grained access tokens for "Get summary stats by actor"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get summary stats by actor"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
actor_typestringRequiredThe type of the actorCan be one of:installation,classic_pat,fine_grained_pat,oauth_app,github_app_user_to_server
actor_idintegerRequiredThe ID of the actor
[/TABLE]
The organization name. The name is not case sensitive.
The type of the actor
Can be one of:installation,classic_pat,fine_grained_pat,oauth_app,github_app_user_to_server

```
installation
```

```
classic_pat
```

```
fine_grained_pat
```

```
github_app_user_to_server
```
The ID of the actor

[TABLE]
Name, Type, Description
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "Get summary stats by actor"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get summary stats by actor"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/summary-stats/ACTOR_TYPE/ACTOR_ID?min_timestamp=MIN_TIMESTAMP"
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_request_count": 34225,
  "rate_limited_request_count": 23
}
```

## Get time stats
Get the number of API requests and rate-limited requests made within an organization over a specified time period.

### Fine-grained access tokens for "Get time stats"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get time stats"

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
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
timestamp_incrementstringRequiredThe increment of time used to breakdown the query results (5m, 10m, 1h, etc.)
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
timestamp_increment
```
The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

### HTTP response status codes for "Get time stats"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get time stats"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/time-stats?min_timestamp=MIN_TIMESTAMP&timestamp_increment=TIMESTAMP_INCREMENT"
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
    "timestamp": "2024-09-11T15:00:00Z",
    "total_request_count": 34225,
    "rate_limited_request_count": 0
  },
  {
    "timestamp": "2024-09-11T15:05:00Z",
    "total_request_count": 10587,
    "rate_limited_request_count": 18
  },
  {
    "timestamp": "2024-09-11T15:10:00Z",
    "total_request_count": 43587,
    "rate_limited_request_count": 14
  },
  {
    "timestamp": "2024-09-11T15:15:00Z",
    "total_request_count": 19463,
    "rate_limited_request_count": 4
  },
  {
    "timestamp": "2024-09-11T15:20:00Z",
    "total_request_count": 60542,
    "rate_limited_request_count": 3
  },
  {
    "timestamp": "2024-09-11T15:25:00Z",
    "total_request_count": 55872,
    "rate_limited_request_count": 23
  }
]
```

## Get time stats by user
Get the number of API requests and rate-limited requests made within an organization by a specific user over a specified time period.

### Fine-grained access tokens for "Get time stats by user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get time stats by user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
user_idstringRequiredThe ID of the user to query for stats
[/TABLE]
The organization name. The name is not case sensitive.
The ID of the user to query for stats

[TABLE]
Name, Type, Description
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
timestamp_incrementstringRequiredThe increment of time used to breakdown the query results (5m, 10m, 1h, etc.)
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
timestamp_increment
```
The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

### HTTP response status codes for "Get time stats by user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get time stats by user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/time-stats/users/USER_ID?min_timestamp=MIN_TIMESTAMP&timestamp_increment=TIMESTAMP_INCREMENT"
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
    "timestamp": "2024-09-11T15:00:00Z",
    "total_request_count": 34225,
    "rate_limited_request_count": 0
  },
  {
    "timestamp": "2024-09-11T15:05:00Z",
    "total_request_count": 10587,
    "rate_limited_request_count": 18
  },
  {
    "timestamp": "2024-09-11T15:10:00Z",
    "total_request_count": 43587,
    "rate_limited_request_count": 14
  },
  {
    "timestamp": "2024-09-11T15:15:00Z",
    "total_request_count": 19463,
    "rate_limited_request_count": 4
  },
  {
    "timestamp": "2024-09-11T15:20:00Z",
    "total_request_count": 60542,
    "rate_limited_request_count": 3
  },
  {
    "timestamp": "2024-09-11T15:25:00Z",
    "total_request_count": 55872,
    "rate_limited_request_count": 23
  }
]
```

## Get time stats by actor
Get the number of API requests and rate-limited requests made within an organization by a specific actor within a specified time period.

### Fine-grained access tokens for "Get time stats by actor"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get time stats by actor"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
actor_typestringRequiredThe type of the actorCan be one of:installation,classic_pat,fine_grained_pat,oauth_app,github_app_user_to_server
actor_idintegerRequiredThe ID of the actor
[/TABLE]
The organization name. The name is not case sensitive.
The type of the actor
Can be one of:installation,classic_pat,fine_grained_pat,oauth_app,github_app_user_to_server

```
installation
```

```
classic_pat
```

```
fine_grained_pat
```

```
github_app_user_to_server
```
The ID of the actor

[TABLE]
Name, Type, Description
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
timestamp_incrementstringRequiredThe increment of time used to breakdown the query results (5m, 10m, 1h, etc.)
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
timestamp_increment
```
The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

### HTTP response status codes for "Get time stats by actor"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get time stats by actor"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/time-stats/ACTOR_TYPE/ACTOR_ID?min_timestamp=MIN_TIMESTAMP&timestamp_increment=TIMESTAMP_INCREMENT"
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
    "timestamp": "2024-09-11T15:00:00Z",
    "total_request_count": 34225,
    "rate_limited_request_count": 0
  },
  {
    "timestamp": "2024-09-11T15:05:00Z",
    "total_request_count": 10587,
    "rate_limited_request_count": 18
  },
  {
    "timestamp": "2024-09-11T15:10:00Z",
    "total_request_count": 43587,
    "rate_limited_request_count": 14
  },
  {
    "timestamp": "2024-09-11T15:15:00Z",
    "total_request_count": 19463,
    "rate_limited_request_count": 4
  },
  {
    "timestamp": "2024-09-11T15:20:00Z",
    "total_request_count": 60542,
    "rate_limited_request_count": 3
  },
  {
    "timestamp": "2024-09-11T15:25:00Z",
    "total_request_count": 55872,
    "rate_limited_request_count": 23
  }
]
```

## Get user stats
Get API usage statistics within an organization for a user broken down by the type of access.

### Fine-grained access tokens for "Get user stats"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "API Insights" organization permissions (read)

### Parameters for "Get user stats"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
user_idstringRequiredThe ID of the user to query for stats
[/TABLE]
The organization name. The name is not case sensitive.
The ID of the user to query for stats

[TABLE]
Name, Type, Description
min_timestampstringRequiredThe minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
max_timestampstringThe maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
sortarrayThe property to sort the results by.
actor_name_substringstringProviding a substring will filter results where the actor name contains the substring. This is a case-insensitive search.
[/TABLE]

```
min_timestamp
```
The minimum timestamp to query for stats. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

```
max_timestamp
```
The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
The property to sort the results by.

```
actor_name_substring
```
Providing a substring will filter results where the actor name contains the substring. This is a case-insensitive search.

### HTTP response status codes for "Get user stats"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get user stats"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/orgs/ORG/insights/api/user-stats/USER_ID?min_timestamp=MIN_TIMESTAMP"
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
    "actor_type": "oauth_app",
    "actor_id": 954453,
    "actor_name": "GitHub Actions",
    "oauth_application_id": 1245,
    "total_request_count": 544665,
    "rate_limited_request_count": 13,
    "last_request_timestamp": "2024-09-18T15:43:03Z",
    "last_rate_limited_timestamp": "2024-09-18T06:30:09Z"
  }
]
```