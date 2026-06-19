# REST API endpoints for issue types

*Source: https://docs.github.com/en/rest/orgs/issue-types*

---

# REST API endpoints for issue types
Use the REST API to interact with issue types in an organization.

## List issue types for an organization
Lists all issue types for an organization. OAuth app tokens and personal access tokens (classic) need the read:org scope to use this endpoint.

### Fine-grained access tokens for "List issue types for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Types" organization permissions (read)

### Parameters for "List issue types for an organization"

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

### HTTP response status codes for "List issue types for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List issue types for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/issue-types
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
    "id": 410,
    "node_id": "IT_kwDNAd3NAZo",
    "name": "Task",
    "description": "A specific piece of work",
    "created_at": "2024-12-11T14:39:09Z",
    "updated_at": "2024-12-11T14:39:09Z"
  },
  {
    "id": 411,
    "node_id": "IT_kwDNAd3NAZs",
    "name": "Bug",
    "description": "An unexpected problem or behavior",
    "created_at": "2024-12-11T14:39:09Z",
    "updated_at": "2024-12-11T14:39:09Z"
  }
]
```

## Create issue type for an organization
Create a new issue type for an organization.
You can find out more about issue types inManaging issue types in an organization.
To use this endpoint, the authenticated user must be an administrator for the organization. OAuth app tokens and
personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Create issue type for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Types" organization permissions (write)

### Parameters for "Create issue type for an organization"

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
namestringRequiredName of the issue type.
is_enabledbooleanRequiredWhether or not the issue type is enabled at the organization level.
descriptionstring or nullDescription of the issue type.
colorstring or nullColor for the issue type.Can be one of:gray,blue,green,yellow,orange,red,pink,purple,null
[/TABLE]
Name of the issue type.
Whether or not the issue type is enabled at the organization level.

```
description
```
Description of the issue type.
Color for the issue type.
Can be one of:gray,blue,green,yellow,orange,red,pink,purple,null

### HTTP response status codes for "Create issue type for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create issue type for an organization"

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
  https://api.github.com/orgs/ORG/issue-types \
  -d '{"name":"Epic","description":"An issue type for a multi-week tracking of work","is_enabled":true,"color":"green"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 410,
  "node_id": "IT_kwDNAd3NAZo",
  "name": "Task",
  "description": "A specific piece of work",
  "created_at": "2024-12-11T14:39:09Z",
  "updated_at": "2024-12-11T14:39:09Z"
}
```

## Update issue type for an organization
Updates an issue type for an organization.
You can find out more about issue types inManaging issue types in an organization.
To use this endpoint, the authenticated user must be an administrator for the organization. OAuth app tokens and
personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Update issue type for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Types" organization permissions (write)

### Parameters for "Update issue type for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
issue_type_idintegerRequiredThe unique identifier of the issue type.
[/TABLE]
The organization name. The name is not case sensitive.

```
issue_type_id
```
The unique identifier of the issue type.

[TABLE]
Name, Type, Description
namestringRequiredName of the issue type.
is_enabledbooleanRequiredWhether or not the issue type is enabled at the organization level.
descriptionstring or nullDescription of the issue type.
colorstring or nullColor for the issue type.Can be one of:gray,blue,green,yellow,orange,red,pink,purple,null
[/TABLE]
Name of the issue type.
Whether or not the issue type is enabled at the organization level.

```
description
```
Description of the issue type.
Color for the issue type.
Can be one of:gray,blue,green,yellow,orange,red,pink,purple,null

### HTTP response status codes for "Update issue type for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Update issue type for an organization"

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
  https://api.github.com/orgs/ORG/issue-types/ISSUE_TYPE_ID \
  -d '{"name":"Epic","description":"An issue type for a multi-week tracking of work","is_enabled":true,"color":"green"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 410,
  "node_id": "IT_kwDNAd3NAZo",
  "name": "Task",
  "description": "A specific piece of work",
  "created_at": "2024-12-11T14:39:09Z",
  "updated_at": "2024-12-11T14:39:09Z"
}
```

## Delete issue type for an organization
Deletes an issue type for an organization.
You can find out more about issue types inManaging issue types in an organization.
To use this endpoint, the authenticated user must be an administrator for the organization. OAuth app tokens and
personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete issue type for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Types" organization permissions (write)

### Parameters for "Delete issue type for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
issue_type_idintegerRequiredThe unique identifier of the issue type.
[/TABLE]
The organization name. The name is not case sensitive.

```
issue_type_id
```
The unique identifier of the issue type.

### HTTP response status codes for "Delete issue type for an organization"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete issue type for an organization"

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
  https://api.github.com/orgs/ORG/issue-types/ISSUE_TYPE_ID
```

#### Response

```
Status: 204
```