# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue custom field options

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents custom issue field select list options created in Jira or using the REST API. This resource supports the following field types:

  * Checkboxes.
  * Radio Buttons.
  * Select List (single choice).
  * Select List (multiple choices).
  * Select List (cascading).


See [Issue custom field options (apps)](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options--apps-/#api-group-issue-custom-field-options--apps-) to manipulate custom issue field select list options created by a Connect app.

Use it to retrieve, create, update, order, and delete custom field options.

Operations

[GET/rest/api/3/customFieldOption/{id}](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-customfieldoption-id-get)[GET/rest/api/3/field/{fieldId}/context/{contextId}/option](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-field-fieldid-context-contextid-option-get)[PUT/rest/api/3/field/{fieldId}/context/{contextId}/option](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-field-fieldid-context-contextid-option-put)[POST/rest/api/3/field/{fieldId}/context/{contextId}/option](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-field-fieldid-context-contextid-option-post)[PUT/rest/api/3/field/{fieldId}/context/{contextId}/option/move](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-field-fieldid-context-contextid-option-move-put)[DEL/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-field-fieldid-context-contextid-option-optionid-delete)[DEL/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-rest-api-3-field-fieldid-context-contextid-option-optionid-issue-delete)

---

GET

## Get custom field option

Returns a custom field option. For example, an option in a select list.

Note that this operation **only works for issue field select list options created in Jira or using operations from the[Issue custom field options](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-group-issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** The custom field option is returned as follows:

  * if the user has the _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * if the user has the _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

CustomFieldOption

Details of a custom option for a field.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/customFieldOption/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/customFieldOption/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "self": "https://your-domain.atlassian.net/rest/api/3/customFieldOption/10000", "value": "To Do" }`

---

GET

## Get custom field options (context)

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the[Issue custom field options (apps)]() operations.**

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg). _Edit Workflow_ [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**fieldId**

string

Required

**contextId**

integer

Required

#### Query parameters

Expand all

**optionId**

integer

**onlyOptions**

boolean

**start_index**

integer

**page_size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanCustomFieldContextOption

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/field/{fieldId}/context/{contextId}/option

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/option`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 4, "values": [ { "id": "10001", "value": "New York" }, { "id": "10002", "value": "Boston", "disabled": true }, { "id": "10004", "value": "Denver" }, { "id": "10003", "value": "Brooklyn", "optionId": "10001" } ] }`

---

PUT

## Update custom field options (context)

Updates the options of a custom field.

If any of the options are not found, no options are updated. Options where the values in the request match the current values aren't updated and aren't reported in the response.

Note that this operation **only works for issue field select list options created in Jira or using operations from the[Issue custom field options](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-group-issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field.option:jira`, `write:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**fieldId**

string

Required

**contextId**

integer

Required

#### Request bodyapplication/json

**options**

array<CustomFieldOptionUpdate>

### Responses

200OK

Returned if the request is successful.

#### application/json

CustomFieldUpdatedContextOptionsList

A list of custom field options for a context.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/field/{fieldId}/context/{contextId}/option

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "options": [ { "disabled": false, "id": "10001", "value": "Scranton" }, { "disabled": true, "id": "10002", "value": "Manhattan" }, { "disabled": false, "id": "10003", "value": "The Electric City" } ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/option`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "options": [ { "disabled": false, "id": "10001", "value": "Scranton" }, { "disabled": true, "id": "10002", "value": "Manhattan" }, { "disabled": false, "id": "10003", "value": "The Electric City" } ] }`

---

POST

## Create custom field options (context)

Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field.

The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the[Issue custom field options (apps)]() operations.**

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field.option:jira`, `write:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**fieldId**

string

Required

**contextId**

integer

Required

#### Request bodyapplication/json

**options**

array<CustomFieldOptionCreate>

### Responses

200OK

Returned if the request is successful.

#### application/json

CustomFieldCreatedContextOptionsList

A list of custom field options for a context.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/field/{fieldId}/context/{contextId}/option

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "options": [ { "disabled": false, "value": "Scranton" }, { "disabled": true, "optionId": "10000", "value": "Manhattan" }, { "disabled": false, "value": "The Electric City" } ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/option`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "options": [ { "disabled": false, "id": "10001", "value": "Scranton" }, { "disabled": true, "id": "10002", "optionId": "10000", "value": "Manhattan" }, { "disabled": false, "id": "10003", "value": "The Electric City" } ] }`

---

PUT

## Reorder custom field options (context)

Changes the order of custom field options or cascading options in a context.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the[Issue custom field options (apps)]() operations.**

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**fieldId**

string

Required

**contextId**

integer

Required

#### Request bodyapplication/json

Expand all

**after**

string

**customFieldOptionIds**

array<string>

Required

**position**

string

### Responses

204No Content

Returned if options are reordered.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/field/{fieldId}/context/{contextId}/option/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "customFieldOptionIds": [ "10001", "10002" ], "position": "First" }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/option/move`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete custom field options (context)

Deletes a custom field option.

Options with cascading options cannot be deleted without deleting the cascading options first.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the[Issue custom field options (apps)]() operations.**

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**fieldId**

string

Required

**contextId**

integer

Required

**optionId**

integer

Required

### Responses

204No Content

Returned if the option is deleted.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Replace custom field options

Replaces the options of a custom field.

Note that this operation **only works for issue field select list options created in Jira or using operations from the[Issue custom field options](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-options/#api-group-issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect or Forge apps.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field.option:jira`, `write:field.option:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**fieldId**

string

Required

**optionId**

integer

Required

**contextId**

integer

Required

#### Query parameters

Expand all

**replaceWith**

integer

**jql_query**

string

### Responses

303See Other

Returned if the long-running task to deselect the option is started.

#### application/json

TaskProgressBeanRemoveOptionFromIssuesResult

Details about a task.

Show child properties

400Bad Request

403Forbidden

404Not Found

DEL/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``{ "self": "https://your-domain.atlassian.net/rest/api/3/task/1", "id": "1", "description": "Remove option 1 from issues matched by '*', and replace with option 3", "status": "COMPLETE", "result": { "errors": { "errorMessages": [ "Option 2 cannot be set on issue MKY-5 as it is not in the correct scope" ], "errors": {}, "httpStatusCode": { "empty": false, "present": true } }, "modifiedIssues": [ 10001, 10010 ], "unmodifiedIssues": [ 10005 ] }, "elapsedRuntime": 42 }`