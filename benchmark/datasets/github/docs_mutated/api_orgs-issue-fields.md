# REST API endpoints for issue fields

*Source: https://docs.github.com/en/rest/orgs/issue-fields*

---

# REST API endpoints for issue fields
Use the REST API to create and manage issue fields for an organization.

## List issue fields for an organization
Lists all issue fields for an organization. OAuth app tokens and personal access tokens (classic) need the read:org scope to use this endpoint.

### Fine-grained access tokens for "List issue fields for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Fields" organization permissions (read)

### Parameters for "List issue fields for an organization"

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

### HTTP response status codes for "List issue fields for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List issue fields for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/issue-fields
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
    "node_id": "IFT_kwDNAd3NAZo",
    "name": "Text field",
    "description": "DRI",
    "data_type": "text",
    "created_at": "2024-12-11T14:39:09Z",
    "updated_at": "2024-12-11T14:39:09Z"
  },
  {
    "id": 2,
    "node_id": "IFSS_kwDNAd3NAZs",
    "name": "Priority",
    "description": "Level of importance",
    "data_type": "single_select",
    "options": [
      {
        "id": 1,
        "name": "High",
        "color": "red"
      },
      {
        "id": 2,
        "name": "Medium",
        "color": "yellow"
      },
      {
        "id": 3,
        "name": "Low",
        "color": "green"
      }
    ],
    "created_at": "2024-12-11T14:39:09Z",
    "updated_at": "2024-12-11T14:39:09Z"
  }
]
```

## Create issue field for an organization
Creates a new issue field for an organization.
You can find out more about issue fields inManaging issue fields in an organization.
To use this endpoint, the authenticated user must be an administrator for the organization. OAuth app tokens and
personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Create issue field for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Fields" organization permissions (write)

### Parameters for "Create issue field for an organization"

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
namestringRequiredName of the issue field.
descriptionstring or nullDescription of the issue field.
data_typestringRequiredThe data type of the issue field.Can be one of:text,date,single_select,number
visibilitystringThe visibility of the issue field. Can beorganization_members_only(visible only within the organization) orall(visible to all users who can see issues). Only used when the visibility settings feature is enabled. Defaults toorganization_members_only.Can be one of:organization_members_only,all
optionsarray of objects or nullOptions for single select fields. Required when data_type is 'single_select'.
Properties ofoptionsName, Type, DescriptionnamestringRequiredName of the option.descriptionstring or nullDescription of the option.colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purplepriorityintegerRequiredPriority of the option for ordering. | Name, Type, Description | namestringRequiredName of the option. | descriptionstring or nullDescription of the option. | colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purple | priorityintegerRequiredPriority of the option for ordering.
Name, Type, Description
namestringRequiredName of the option.
descriptionstring or nullDescription of the option.
colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purple
priorityintegerRequiredPriority of the option for ordering.
[/TABLE]
Name of the issue field.

```
description
```
Description of the issue field.
The data type of the issue field.
Can be one of:text,date,single_select,number

```
single_select
```
The visibility of the issue field. Can beorganization_members_only(visible only within the organization) orall(visible to all users who can see issues). Only used when the visibility settings feature is enabled. Defaults toorganization_members_only.
Can be one of:organization_members_only,all

```
organization_members_only
```
Options for single select fields. Required when data_type is 'single_select'.

[TABLE]
Name, Type, Description
namestringRequiredName of the option.
descriptionstring or nullDescription of the option.
colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purple
priorityintegerRequiredPriority of the option for ordering.
[/TABLE]
Name of the option.

```
description
```
Description of the option.
Color for the option.
Can be one of:gray,blue,green,yellow,orange,red,pink,purple
Priority of the option for ordering.

### HTTP response status codes for "Create issue field for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create issue field for an organization"

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
  https://api.github.com/orgs/ORG/issue-fields \
  -d '{"name":"Priority","description":"Level of importance for the issue","data_type":"single_select","options":[{"name":"High","description":"High priority","color":"red"},{"name":"Medium","description":"Medium priority","color":"yellow"},{"name":"Low","description":"Low priority","color":"green"}]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 512,
  "node_id": "IF_kwDNAd3NAZr",
  "name": "Priority",
  "description": "Level of importance for the issue",
  "data_type": "single_select",
  "options": [
    {
      "id": 1,
      "name": "High",
      "description": "High priority",
      "color": "red",
      "priority": 1,
      "created_at": "2025-01-15T10:30:15Z",
      "updated_at": "2025-01-15T10:30:15Z"
    },
    {
      "id": 2,
      "name": "Medium",
      "description": "Medium priority",
      "color": "yellow",
      "priority": 2,
      "created_at": "2025-01-15T10:30:15Z",
      "updated_at": "2025-01-15T10:30:15Z"
    },
    {
      "id": 3,
      "name": "Low",
      "description": "Low priority",
      "color": "green",
      "priority": 3,
      "created_at": "2025-01-15T10:30:15Z",
      "updated_at": "2025-01-15T10:30:15Z"
    }
  ],
  "created_at": "2025-01-15T10:30:15Z",
  "updated_at": "2025-01-15T10:30:15Z"
}
```

## Update issue field for an organization
Updates an issue field for an organization.
You can find out more about issue fields inManaging issue fields in an organization.
To use this endpoint, the authenticated user must be an administrator for the organization. OAuth app tokens and
personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Update issue field for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Fields" organization permissions (write)

### Parameters for "Update issue field for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
issue_field_idintegerRequiredThe unique identifier of the issue field.
[/TABLE]
The organization name. The name is not case sensitive.

```
issue_field_id
```
The unique identifier of the issue field.

[TABLE]
Name, Type, Description
namestringName of the issue field.
descriptionstring or nullDescription of the issue field.
visibilitystringThe visibility of the issue field. Can beorganization_members_only(visible only within the organization) orall(visible to all users who can see issues). Only used when the visibility settings feature is enabled.Can be one of:organization_members_only,all
optionsarray of objectsOptions for single select fields. Only applicable when updating single_select fields.
Properties ofoptionsName, Type, DescriptionnamestringRequiredName of the option.descriptionstring or nullDescription of the option.colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purplepriorityintegerRequiredPriority of the option for ordering. | Name, Type, Description | namestringRequiredName of the option. | descriptionstring or nullDescription of the option. | colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purple | priorityintegerRequiredPriority of the option for ordering.
Name, Type, Description
namestringRequiredName of the option.
descriptionstring or nullDescription of the option.
colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purple
priorityintegerRequiredPriority of the option for ordering.
[/TABLE]
Name of the issue field.

```
description
```
Description of the issue field.
The visibility of the issue field. Can beorganization_members_only(visible only within the organization) orall(visible to all users who can see issues). Only used when the visibility settings feature is enabled.
Can be one of:organization_members_only,all

```
organization_members_only
```
Options for single select fields. Only applicable when updating single_select fields.

[TABLE]
Name, Type, Description
namestringRequiredName of the option.
descriptionstring or nullDescription of the option.
colorstringRequiredColor for the option.Can be one of:gray,blue,green,yellow,orange,red,pink,purple
priorityintegerRequiredPriority of the option for ordering.
[/TABLE]
Name of the option.

```
description
```
Description of the option.
Color for the option.
Can be one of:gray,blue,green,yellow,orange,red,pink,purple
Priority of the option for ordering.

### HTTP response status codes for "Update issue field for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Update issue field for an organization"

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
  https://api.github.com/orgs/ORG/issue-fields/ISSUE_FIELD_ID \
  -d '{"name":"Priority","description":"Level of importance for the issue"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 512,
  "node_id": "IF_kwDNAd3NAZr",
  "name": "Priority",
  "description": "Level of importance for the issue",
  "data_type": "single_select",
  "options": [
    {
      "id": 1,
      "name": "High",
      "description": "High priority",
      "color": "red",
      "priority": 1,
      "created_at": "2025-01-15T10:30:15Z",
      "updated_at": "2025-01-15T10:30:15Z"
    },
    {
      "id": 2,
      "name": "Medium",
      "description": "Medium priority",
      "color": "yellow",
      "priority": 2,
      "created_at": "2025-01-15T10:30:15Z",
      "updated_at": "2025-01-15T10:30:15Z"
    },
    {
      "id": 3,
      "name": "Low",
      "description": "Low priority",
      "color": "green",
      "priority": 3,
      "created_at": "2025-01-15T10:30:15Z",
      "updated_at": "2025-01-15T10:30:15Z"
    }
  ],
  "created_at": "2025-01-15T10:30:15Z",
  "updated_at": "2025-01-15T10:30:15Z"
}
```

## Delete issue field for an organization
Deletes an issue field for an organization.
You can find out more about issue fields inManaging issue fields in an organization.
To use this endpoint, the authenticated user must be an administrator for the organization. OAuth app tokens and
personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete issue field for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issue Fields" organization permissions (write)

### Parameters for "Delete issue field for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
issue_field_idintegerRequiredThe unique identifier of the issue field.
[/TABLE]
The organization name. The name is not case sensitive.

```
issue_field_id
```
The unique identifier of the issue field.

### HTTP response status codes for "Delete issue field for an organization"

[TABLE]
Status code | Description
204 | A header with no content is returned.
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
A header with no content is returned.
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete issue field for an organization"

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
  https://api.github.com/orgs/ORG/issue-fields/ISSUE_FIELD_ID
```

#### A header with no content is returned.

```
Status: 204
```