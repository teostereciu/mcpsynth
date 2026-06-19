# REST API endpoints for security campaigns

*Source: https://docs.github.com/en/rest/campaigns/campaigns*

---

# REST API endpoints for security campaigns
Use the REST API to create and manage security campaigns for your organization.
Note
These endpoints only interact with published campaigns. Draft campaigns cannot currently be viewed or managed through the API.

## List campaigns for an organization
Lists campaigns in an organization.
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint.

### Fine-grained access tokens for "List campaigns for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Campaigns" organization permissions (read)

### Parameters for "List campaigns for an organization"

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
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
statestringIf specified, only campaigns with this issue_state will be returned.Can be one of:open,closed
sortstringThe property by which to sort the results.Default:createdCan be one of:created,updated,ends_at,published
[/TABLE]
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
If specified, only campaigns with this issue_state will be returned.
Can be one of:open,closed
The property by which to sort the results.
Default:created
Can be one of:created,updated,ends_at,published

### HTTP response status codes for "List campaigns for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Resource not found
Service unavailable

### Code samples for "List campaigns for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/campaigns
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
    "number": 3,
    "created_at": "2024-02-14T12:29:18Z",
    "updated_at": "2024-02-14T12:29:18Z",
    "name": "Critical CodeQL alert",
    "description": "Address critical alerts before they are exploited to prevent breaches, protect sensitive data, and mitigate financial and reputational damage.",
    "managers": [
      {
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
    ],
    "ends_at": "2024-03-14T12:29:18Z",
    "closed_at": null,
    "issue_state": "open"
  },
  {
    "number": 4,
    "created_at": "2024-03-30T12:29:18Z",
    "updated_at": "2024-03-30T12:29:18Z",
    "name": "Mitre top 10 KEV",
    "description": "Remediate the MITRE Top 10 KEV (Known Exploited Vulnerabilities) to enhance security by addressing vulnerabilities actively exploited by attackers. This reduces risk, prevents breaches and can help protect sensitive data.",
    "managers": [
      {
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
    ],
    "ends_at": "2024-04-30T12:29:18Z",
    "closed_at": null,
    "issue_state": "open"
  }
]
```

## Create a campaign for an organization
Create a campaign for an organization.
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint.
Fine-grained tokens must have the "Code scanning alerts" repository permissions (read) on all repositories included
in the campaign.

### Fine-grained access tokens for "Create a campaign for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Campaigns" organization permissions (write)

### Parameters for "Create a campaign for an organization"

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

### HTTP response status codes for "Create a campaign for an organization"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
404 | Resource not found
422 | Unprocessable Entity
429 | Too Many Requests
503 | Service unavailable
[/TABLE]
OK
Bad Request
Resource not found
Unprocessable Entity
Too Many Requests
Service unavailable

### Code samples for "Create a campaign for an organization"

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
  https://api.github.com/orgs/ORG/campaigns \
  -d '{"name":"Critical CodeQL alerts","description":"Address critical alerts before they are exploited to prevent breaches, protect sensitive data, and mitigate financial and reputational damage.","managers":["octocat"],"ends_at":"2024-03-14T00:00:00Z","code_scanning_alerts":[{"repository_id":1296269,"alert_numbers":[1,2]}]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 3,
  "created_at": "2024-02-14T12:29:18Z",
  "updated_at": "2024-02-14T12:29:18Z",
  "name": "Critical CodeQL alert",
  "description": "Address critical alerts before they are exploited to prevent breaches, protect sensitive data, and mitigate financial and reputational damage.",
  "managers": [
    {
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
  ],
  "published_at": "2024-02-14T12:29:18Z",
  "ends_at": "2024-03-14T12:29:18Z",
  "closed_at": null,
  "issue_state": "open",
  "alert_stats": {
    "open_count": 10,
    "closed_count": 3,
    "in_progress_count": 3
  }
}
```

## Get a campaign for an organization
Gets a campaign for an organization.
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint.

### Fine-grained access tokens for "Get a campaign for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Campaigns" organization permissions (read)

### Parameters for "Get a campaign for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
campaign_numberintegerRequiredThe campaign number.
[/TABLE]
The organization name. The name is not case sensitive.

```
campaign_number
```
The campaign number.

### HTTP response status codes for "Get a campaign for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Unprocessable Entity
503 | Service unavailable
[/TABLE]
OK
Resource not found
Unprocessable Entity
Service unavailable

### Code samples for "Get a campaign for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/campaigns/CAMPAIGN_NUMBER
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 3,
  "created_at": "2024-02-14T12:29:18Z",
  "updated_at": "2024-02-14T12:29:18Z",
  "name": "Critical CodeQL alert",
  "description": "Address critical alerts before they are exploited to prevent breaches, protect sensitive data, and mitigate financial and reputational damage.",
  "managers": [
    {
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
  ],
  "published_at": "2024-02-14T12:29:18Z",
  "ends_at": "2024-03-14T12:29:18Z",
  "closed_at": null,
  "issue_state": "open",
  "alert_stats": {
    "open_count": 10,
    "closed_count": 3,
    "in_progress_count": 3
  }
}
```

## Update a campaign
Updates a campaign in an organization.
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint.

### Fine-grained access tokens for "Update a campaign"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Campaigns" organization permissions (write)

### Parameters for "Update a campaign"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
campaign_numberintegerRequiredThe campaign number.
[/TABLE]
The organization name. The name is not case sensitive.

```
campaign_number
```
The campaign number.

[TABLE]
Name, Type, Description
namestringThe name of the campaign
descriptionstringA description for the campaign
managersarray of stringsThe logins of the users to set as the campaign managers. At this time, only a single manager can be supplied.
team_managersarray of stringsThe slugs of the teams to set as the campaign managers.
ends_atstringThe end date and time of the campaign, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ.
contact_linkstring or nullThe contact link of the campaign. Must be a URI.
statestringIndicates whether a campaign is open or closedCan be one of:open,closed
[/TABLE]
The name of the campaign

```
description
```
A description for the campaign
The logins of the users to set as the campaign managers. At this time, only a single manager can be supplied.

```
team_managers
```
The slugs of the teams to set as the campaign managers.
The end date and time of the campaign, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ.

```
contact_link
```
The contact link of the campaign. Must be a URI.
Indicates whether a campaign is open or closed
Can be one of:open,closed

### HTTP response status codes for "Update a campaign"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
404 | Resource not found
422 | Unprocessable Entity
503 | Service unavailable
[/TABLE]
OK
Bad Request
Resource not found
Unprocessable Entity
Service unavailable

### Code samples for "Update a campaign"

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
  https://api.github.com/orgs/ORG/campaigns/CAMPAIGN_NUMBER \
  -d '{"name":"Critical CodeQL alerts"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 3,
  "created_at": "2024-02-14T12:29:18Z",
  "updated_at": "2024-02-14T12:29:18Z",
  "name": "Critical CodeQL alert",
  "description": "Address critical alerts before they are exploited to prevent breaches, protect sensitive data, and mitigate financial and reputational damage.",
  "managers": [
    {
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
  ],
  "published_at": "2024-02-14T12:29:18Z",
  "ends_at": "2024-03-14T12:29:18Z",
  "closed_at": null,
  "issue_state": "open",
  "alert_stats": {
    "open_count": 10,
    "closed_count": 3,
    "in_progress_count": 3
  }
}
```

## Delete a campaign for an organization
Deletes a campaign in an organization.
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint.

### Fine-grained access tokens for "Delete a campaign for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Campaigns" organization permissions (write)

### Parameters for "Delete a campaign for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
campaign_numberintegerRequiredThe campaign number.
[/TABLE]
The organization name. The name is not case sensitive.

```
campaign_number
```
The campaign number.

### HTTP response status codes for "Delete a campaign for an organization"

[TABLE]
Status code | Description
204 | Deletion successful
404 | Resource not found
503 | Service unavailable
[/TABLE]
Deletion successful
Resource not found
Service unavailable

### Code samples for "Delete a campaign for an organization"

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
  https://api.github.com/orgs/ORG/campaigns/CAMPAIGN_NUMBER
```

#### Deletion successful

```
Status: 204
```