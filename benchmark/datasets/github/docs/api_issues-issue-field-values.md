# REST API endpoints for issue field values

*Source: https://docs.github.com/en/rest/issues/issue-field-values*

---

# REST API endpoints for issue field values
Use the REST API to view and manage issue field values for issues.

## List issue field values for an issue
Lists all issue field values for an issue.

### Fine-grained access tokens for "List issue field values for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Issues" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List issue field values for an issue"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List issue field values for an issue"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
404 | Resource not found
410 | Gone
[/TABLE]
OK
Moved permanently
Resource not found
Gone

### Code samples for "List issue field values for an issue"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/issue-field-values
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
    "issue_field_id": 1,
    "node_id": "IFT_GDKND",
    "data_type": "text",
    "value": "DRI"
  },
  {
    "issue_field_id": 2,
    "node_id": "IFSS_SADMS",
    "data_type": "single_select",
    "value": 1,
    "single_select_option": {
      "id": 1,
      "name": "High",
      "color": "red"
    }
  },
  {
    "issue_field_id": 3,
    "node_id": "IFN_POINTS",
    "data_type": "number",
    "value": 42
  },
  {
    "issue_field_id": 4,
    "node_id": "IFD_DUEDATE",
    "data_type": "date",
    "value": "2025-12-25"
  }
]
```

## Add issue field values to an issue
Add custom field values to an issue. You can set values for organization-level issue fields that have been defined for the repository's organization.
Adding an empty array will clear all existing field values for the issue.
This endpoint supports the following field data types:
- text: String values for text fields
- single_select: Option names for single-select fields (must match an existing option name)
- number: Numeric values for number fields
- date: ISO 8601 date strings for date fields

```
single_select
```
Only users with push access to the repository can add issue field values. If you don't have the proper permissions, you'll receive a403 Forbiddenresponse.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API"
and "Best practices for using the REST API."

### Fine-grained access tokens for "Add issue field values to an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Add issue field values to an issue"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
repository_idintegerRequiredThe unique identifier of the repository.
issue_numberintegerRequiredThe number that identifies the issue.
[/TABLE]

```
repository_id
```
The unique identifier of the repository.

```
issue_number
```
The number that identifies the issue.

[TABLE]
Name, Type, Description
issue_field_valuesarray of objectsAn array of issue field values to add to this issue. Each field value must include the field ID and the value to set.
Properties ofissue_field_valuesName, Type, Descriptionfield_idintegerRequiredThe ID of the issue field to setvaluestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string | Name, Type, Description | field_idintegerRequiredThe ID of the issue field to set | valuestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string
Name, Type, Description
field_idintegerRequiredThe ID of the issue field to set
valuestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string
[/TABLE]

```
issue_field_values
```
An array of issue field values to add to this issue. Each field value must include the field ID and the value to set.

```
issue_field_values
```

[TABLE]
Name, Type, Description
field_idintegerRequiredThe ID of the issue field to set
valuestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string
[/TABLE]
The ID of the issue field to set
The value to set for the field. The type depends on the field's data type:
- For text fields: provide a string value
- For single_select fields: provide the option name as a string (must match an existing option)
- For number fields: provide a numeric value
- For date fields: provide an ISO 8601 date string

### HTTP response status codes for "Add issue field values to an issue"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
OK
Bad Request
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Add issue field values to an issue"

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
  https://api.github.com/repositories/REPOSITORY_ID/issues/ISSUE_NUMBER/issue-field-values \
  -d '{"issue_field_values":[{"field_id":123,"value":"Critical"},{"field_id":456,"value":5},{"field_id":789,"value":"2024-12-31"}]}'
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
    "issue_field_id": 1,
    "node_id": "IFT_GDKND",
    "data_type": "text",
    "value": "DRI"
  },
  {
    "issue_field_id": 2,
    "node_id": "IFSS_SADMS",
    "data_type": "single_select",
    "value": 1,
    "single_select_option": {
      "id": 1,
      "name": "High",
      "color": "red"
    }
  },
  {
    "issue_field_id": 3,
    "node_id": "IFN_POINTS",
    "data_type": "number",
    "value": 42
  },
  {
    "issue_field_id": 4,
    "node_id": "IFD_DUEDATE",
    "data_type": "date",
    "value": "2025-12-25"
  }
]
```

## Set issue field values for an issue
Set custom field values for an issue, replacing any existing values. You can set values for organization-level issue fields that have been defined for the repository's organization.
This endpoint supports the following field data types:
- text: String values for text fields
- single_select: Option names for single-select fields (must match an existing option name)
- number: Numeric values for number fields
- date: ISO 8601 date strings for date fields

```
single_select
```
This operation will replace all existing field values with the provided ones. If you want to add field values without replacing existing ones, use thePOSTendpoint instead.
Only users with push access to the repository can set issue field values. If you don't have the proper permissions, you'll receive a403 Forbiddenresponse.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API"
and "Best practices for using the REST API."

### Fine-grained access tokens for "Set issue field values for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Set issue field values for an issue"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
repository_idintegerRequiredThe unique identifier of the repository.
issue_numberintegerRequiredThe number that identifies the issue.
[/TABLE]

```
repository_id
```
The unique identifier of the repository.

```
issue_number
```
The number that identifies the issue.

[TABLE]
Name, Type, Description
issue_field_valuesarray of objectsAn array of issue field values to set for this issue. Each field value must include the field ID and the value to set. All existing field values will be replaced.
Properties ofissue_field_valuesName, Type, Descriptionfield_idintegerRequiredThe ID of the issue field to setvaluestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string | Name, Type, Description | field_idintegerRequiredThe ID of the issue field to set | valuestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string
Name, Type, Description
field_idintegerRequiredThe ID of the issue field to set
valuestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string
[/TABLE]

```
issue_field_values
```
An array of issue field values to set for this issue. Each field value must include the field ID and the value to set. All existing field values will be replaced.

```
issue_field_values
```

[TABLE]
Name, Type, Description
field_idintegerRequiredThe ID of the issue field to set
valuestring or numberRequiredThe value to set for the field. The type depends on the field's data type:For text fields: provide a string valueFor single_select fields: provide the option name as a string (must match an existing option)For number fields: provide a numeric valueFor date fields: provide an ISO 8601 date string
[/TABLE]
The ID of the issue field to set
The value to set for the field. The type depends on the field's data type:
- For text fields: provide a string value
- For single_select fields: provide the option name as a string (must match an existing option)
- For number fields: provide a numeric value
- For date fields: provide an ISO 8601 date string

### HTTP response status codes for "Set issue field values for an issue"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
OK
Bad Request
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Set issue field values for an issue"

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
  https://api.github.com/repositories/REPOSITORY_ID/issues/ISSUE_NUMBER/issue-field-values \
  -d '{"issue_field_values":[{"field_id":123,"value":"Critical"},{"field_id":456,"value":5},{"field_id":789,"value":"2024-12-31"}]}'
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
    "issue_field_id": 1,
    "node_id": "IFT_GDKND",
    "data_type": "text",
    "value": "DRI"
  },
  {
    "issue_field_id": 2,
    "node_id": "IFSS_SADMS",
    "data_type": "single_select",
    "value": 1,
    "single_select_option": {
      "id": 1,
      "name": "High",
      "color": "red"
    }
  },
  {
    "issue_field_id": 3,
    "node_id": "IFN_POINTS",
    "data_type": "number",
    "value": 42
  },
  {
    "issue_field_id": 4,
    "node_id": "IFD_DUEDATE",
    "data_type": "date",
    "value": "2025-12-25"
  }
]
```

## Delete an issue field value from an issue
Remove a specific custom field value from an issue.
Only users with push access to the repository can delete issue field values. If you don't have the proper permissions, you'll receive a403 Forbiddenresponse.
If the specified field does not have a value set on the issue, this operation will return a404error.
This endpoint triggersnotifications. Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see "Rate limits for the API"
and "Best practices for using the REST API."

### Fine-grained access tokens for "Delete an issue field value from an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Delete an issue field value from an issue"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
repository_idintegerRequiredThe unique identifier of the repository.
issue_numberintegerRequiredThe number that identifies the issue.
issue_field_idintegerRequiredThe unique identifier of the issue field.
[/TABLE]

```
repository_id
```
The unique identifier of the repository.

```
issue_number
```
The number that identifies the issue.

```
issue_field_id
```
The unique identifier of the issue field.

### HTTP response status codes for "Delete an issue field value from an issue"

[TABLE]
Status code | Description
204 | Issue field value deleted successfully
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
Issue field value deleted successfully
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Delete an issue field value from an issue"

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
  https://api.github.com/repositories/REPOSITORY_ID/issues/ISSUE_NUMBER/issue-field-values/ISSUE_FIELD_ID
```

#### Issue field value deleted successfully

```
Status: 204
```