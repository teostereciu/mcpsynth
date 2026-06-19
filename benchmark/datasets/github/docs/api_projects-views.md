# REST API endpoints for Project views

*Source: https://docs.github.com/en/rest/projects/views*

---

# REST API endpoints for Project views
Use the REST API to manage Project views

## Create a view for an organization-owned project
Create a new view in an organization-owned project. Views allow you to customize how items in a project are displayed and filtered.

### Fine-grained access tokens for "Create a view for an organization-owned project"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Projects" organization permissions (write)

### Parameters for "Create a view for an organization-owned project"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
project_numberintegerRequiredThe project's number.
[/TABLE]
The organization name. The name is not case sensitive.

```
project_number
```
The project's number.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the view.
layoutstringRequiredThe layout of the view.Can be one of:table,board,roadmap
filterstringThe filter query for the view. SeeFiltering projectsfor more information.
visible_fieldsarray of integersvisible_fieldsis not applicable toroadmaplayout views.
Fortableandboardlayouts, this represents the field IDs that should be visible in the view. If not provided, the default visible fields will be used.
[/TABLE]
The name of the view.
The layout of the view.
Can be one of:table,board,roadmap
The filter query for the view. SeeFiltering projectsfor more information.

```
visible_fields
```
visible_fieldsis not applicable toroadmaplayout views.
Fortableandboardlayouts, this represents the field IDs that should be visible in the view. If not provided, the default visible fields will be used.

### HTTP response status codes for "Create a view for an organization-owned project"

[TABLE]
Status code | Description
201 | Response for creating a view in an organization-owned project.
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
Response for creating a view in an organization-owned project.
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Create a view for an organization-owned project"

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
  https://api.github.com/orgs/ORG/projectsV2/PROJECT_NUMBER/views \
  -d '{"name":"All Issues","layout":"table","filter":"is:issue","visible_fields":[123,456,789]}'
```

#### Response for creating a table view
- Example response
- Response schema

```
Status: 201
```

```
{
  "value": {
    "id": 1,
    "number": 1,
    "name": "Sprint Board",
    "layout": "board",
    "node_id": "PVTV_lADOANN5s84ACbL0zgBueEI",
    "project_url": "https://api.github.com/orgs/octocat/projectsV2/1",
    "html_url": "https://github.com/orgs/octocat/projects/1/views/1",
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
    "created_at": "2022-04-28T12:00:00Z",
    "updated_at": "2022-04-28T12:00:00Z",
    "filter": "is:issue is:open",
    "visible_fields": [
      123,
      456,
      789
    ],
    "sort_by": [
      [
        123,
        "asc"
      ],
      [
        456,
        "desc"
      ]
    ],
    "group_by": [
      123
    ],
    "vertical_group_by": [
      456
    ]
  }
}
```

## Create a view for a user-owned project
Create a new view in a user-owned project. Views allow you to customize how items in a project are displayed and filtered.

### Fine-grained access tokens for "Create a view for a user-owned project"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Create a view for a user-owned project"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
user_idstringRequiredThe unique identifier of the user.
project_numberintegerRequiredThe project's number.
[/TABLE]
The unique identifier of the user.

```
project_number
```
The project's number.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the view.
layoutstringRequiredThe layout of the view.Can be one of:table,board,roadmap
filterstringThe filter query for the view. SeeFiltering projectsfor more information.
visible_fieldsarray of integersvisible_fieldsis not applicable toroadmaplayout views.
Fortableandboardlayouts, this represents the field IDs that should be visible in the view. If not provided, the default visible fields will be used.
[/TABLE]
The name of the view.
The layout of the view.
Can be one of:table,board,roadmap
The filter query for the view. SeeFiltering projectsfor more information.

```
visible_fields
```
visible_fieldsis not applicable toroadmaplayout views.
Fortableandboardlayouts, this represents the field IDs that should be visible in the view. If not provided, the default visible fields will be used.

### HTTP response status codes for "Create a view for a user-owned project"

[TABLE]
Status code | Description
201 | Response for creating a view in a user-owned project.
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
Response for creating a view in a user-owned project.
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Create a view for a user-owned project"

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
  https://api.github.com/users/USER_ID/projectsV2/PROJECT_NUMBER/views \
  -d '{"name":"All Issues","layout":"table","filter":"is:issue","visible_fields":[123,456,789]}'
```

#### Response for creating a table view
- Example response
- Response schema

```
Status: 201
```

```
{
  "value": {
    "id": 1,
    "number": 1,
    "name": "Sprint Board",
    "layout": "board",
    "node_id": "PVTV_lADOANN5s84ACbL0zgBueEI",
    "project_url": "https://api.github.com/orgs/octocat/projectsV2/1",
    "html_url": "https://github.com/orgs/octocat/projects/1/views/1",
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
    "created_at": "2022-04-28T12:00:00Z",
    "updated_at": "2022-04-28T12:00:00Z",
    "filter": "is:issue is:open",
    "visible_fields": [
      123,
      456,
      789
    ],
    "sort_by": [
      [
        123,
        "asc"
      ],
      [
        456,
        "desc"
      ]
    ],
    "group_by": [
      123
    ],
    "vertical_group_by": [
      456
    ]
  }
}
```