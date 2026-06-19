# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue custom field contexts

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue custom field contexts. Use it to:

  * get, create, update, and delete custom field contexts.
  * get context to issue types and projects mappings.
  * get custom field contexts for projects and issue types.
  * assign custom field contexts to projects.
  * remove custom field contexts from projects.
  * add issue types to custom field contexts.


Operations

[GET/rest/api/3/field/{fieldId}/context](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-get)[POST/rest/api/3/field/{fieldId}/context](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-post)[GET/rest/api/3/field/{fieldId}/context/defaultValue](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-defaultvalue-get)[PUT/rest/api/3/field/{fieldId}/context/defaultValue](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-defaultvalue-put)[GET/rest/api/3/field/{fieldId}/context/issuetypemapping](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-issuetypemapping-get)[POST/rest/api/3/field/{fieldId}/context/mapping](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-mapping-post)[GET/rest/api/3/field/{fieldId}/context/projectmapping](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-projectmapping-get)[PUT/rest/api/3/field/{fieldId}/context/{contextId}](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-contextid-put)[DEL/rest/api/3/field/{fieldId}/context/{contextId}](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-contextid-delete)[PUT/rest/api/3/field/{fieldId}/context/{contextId}/issuetype](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-contextid-issuetype-put)[POST/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-contextid-issuetype-remove-post)[PUT/rest/api/3/field/{fieldId}/context/{contextId}/project](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-contextid-project-put)[POST/rest/api/3/field/{fieldId}/context/{contextId}/project/remove](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-contextid-project-remove-post)

---

GET

## Get custom field contexts

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows:

  * With no other parameters set, all contexts.
  * By defining `id` only, all contexts from the list of IDs.
  * By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false)
  * By defining `isGlobalContext`, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false).


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg). _Edit Workflow_ [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`, `read:custom-field-contextual-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**isAnyIssueType**

boolean

**isGlobalContext**

boolean

**contextId**

array<integer>

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanCustomFieldContext

A page of items.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/field/{fieldId}/context

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``{ "isLast": true, "maxResults": 100, "startAt": 0, "total": 2, "values": [ { "id": "10025", "name": "Bug fields context", "description": "A context used to define the custom field options for bugs.", "isGlobalContext": true, "isAnyIssueType": false }, { "id": "10026", "name": "Task fields context", "description": "A context used to define the custom field options for tasks.", "isGlobalContext": false, "isAnyIssueType": false } ] }`

---

POST

## Create custom field context

Creates a custom field context.

If `projectIds` is empty, a global context is created. A global context is one that applies to all project. If `issueTypeIds` is empty, the context applies to all issue types.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`, `write:field:jira`, `read:custom-field-contextual-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**fieldId**

string

Required

#### Request bodyapplication/json

Expand all

**description**

string

**issueTypeIds**

array<string>

**name**

string

Required

**projectIds**

array<string>

### Responses

201Created

Returned if the custom field context is created.

#### application/json

CreateCustomFieldContext

The details of a created custom field context.

Show child properties

400Bad Request

401Unauthorized

404Not Found

409Conflict

POST/rest/api/3/field/{fieldId}/context

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A context used to define the custom field options for bugs.", "issueTypeIds": [ "10010" ], "name": "Bug fields context", "projectIds": [] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 ``{ "id": "10025", "name": "Bug fields context", "description": "A context used to define the custom field options for bugs.", "projectIds": [], "issueTypeIds": [ "10010" ] }`

---

GET

## Get custom field contexts default valuesDeprecated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of defaults for a custom field. The results can be filtered by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is returned.
The returned object depends on type of the custom field:

  * `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
  * `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
  * `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons.
  * `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes.
  * `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists.
  * `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
  * `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
  * `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers.
  * `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers.
  * `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
  * `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
  * `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
  * `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
  * `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
  * `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
  * `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
  * `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers.
  * `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers.


Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

  * `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields.
  * `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields.
  * `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields.
  * `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields.
  * `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
  * `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields.
  * `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields.
  * `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
  * `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field.default-value:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**contextId**

array<integer>

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanCustomFieldContextDefaultValue

A page of items.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/field/{fieldId}/context/defaultValue

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/defaultValue`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "contextId": "10100", "optionId": "10001" }, { "contextId": "10101", "optionId": "10003" }, { "contextId": "10103" } ] }`

---

PUT

## Set custom field contexts default valuesDeprecated

Sets default for contexts of a custom field. Default are defined using these objects:

  * `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
  * `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
  * `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons.
  * `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes.
  * `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists.
  * `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
  * `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
  * `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers.
  * `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers.
  * `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
  * `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
  * `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
  * `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
  * `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
  * `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
  * `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
  * `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers.
  * `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers.


Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

  * `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields.
  * `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields.
  * `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields.
  * `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields.
  * `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
  * `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields.
  * `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields.
  * `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
  * `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields.


Only one type of default object can be included in a request. To remove a default for a context, set the default parameter to `null`.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field.default-value:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**fieldId**

string

Required

#### Request bodyapplication/json

**defaultValues**

array<oneOf [CustomFieldContextDefaultValueCascadingOption, CustomFieldContextDefaultValueMultipleOption, CustomFieldContextDefaultValueSingleOption, CustomFieldContextSingleUserPickerDefaults, CustomFieldContextDefaultValueMultiUserPicker, CustomFieldContextDefaultValueSingleGroupPicker, CustomFieldContextDefaultValueMultipleGroupPicker, CustomFieldContextDefaultValueDate, CustomFieldContextDefaultValueDateTime, CustomFieldContextDefaultValueURL, CustomFieldContextDefaultValueProject, CustomFieldContextDefaultValueFloat, CustomFieldContextDefaultValueLabels, CustomFieldContextDefaultValueTextField, CustomFieldContextDefaultValueTextArea, CustomFieldContextDefaultValueReadOnly, CustomFieldContextDefaultValueSingleVersionPicker, CustomFieldContextDefaultValueMultipleVersionPicker, CustomFieldContextDefaultValueForgeStringField, CustomFieldContextDefaultValueForgeMultiStringField, CustomFieldContextDefaultValueForgeObjectField, CustomFieldContextDefaultValueForgeDateTimeField, CustomFieldContextDefaultValueForgeGroupField, CustomFieldContextDefaultValueForgeMultiGroupField, CustomFieldContextDefaultValueForgeNumberField, CustomFieldContextDefaultValueForgeUserField, CustomFieldContextDefaultValueForgeMultiUserField]>

### Responses

204No Content

Returned if operation is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/field/{fieldId}/context/defaultValue

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultValues": [ { "contextId": "10100", "optionId": "10001", "type": "option.single" }, { "contextId": "10101", "optionId": "10003", "type": "option.single" }, { "contextId": "10103", "optionId": "10005", "type": "option.single" } ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/defaultValue`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get issue types for custom field context

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**contextId**

array<integer>

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if operation is successful.

#### application/json

PageBeanIssueTypeToContextMapping

A page of items.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/field/{fieldId}/context/issuetypemapping

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/issuetypemapping`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "isLast": true, "maxResults": 100, "startAt": 0, "total": 3, "values": [ { "contextId": "10001", "issueTypeId": "10010" }, { "contextId": "10001", "issueTypeId": "10011" }, { "contextId": "10002", "isAnyIssueType": true } ] }`

---

POST

## Get custom field contexts for projects and issue types

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of project and issue type mappings and, for each mapping, the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the project and issue type.

If there is no custom field context assigned to the project then, if present, the custom field context that applies to all projects is returned if it also applies to the issue type or all issue types. If a custom field context is not found, the returned custom field context ID is `null`.

Duplicate project and issue type mappings cannot be provided in the request.

The order of the returned values is the same as provided in the request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**startAt**

integer

**maxResults**

integer

#### Request bodyapplication/json

The list of project and issue type mappings.

**mappings**

array<ProjectIssueTypeMapping>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanContextForProjectAndIssueType

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/field/{fieldId}/context/mapping

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "mappings": [ { "issueTypeId": "10000", "projectId": "10000" }, { "issueTypeId": "10001", "projectId": "10000" }, { "issueTypeId": "10002", "projectId": "10001" } ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/mapping`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "projectId": "10000", "issueTypeId": "10000", "contextId": "10000" }, { "projectId": "10000", "issueTypeId": "10001", "contextId": null }, { "projectId": "10001", "issueTypeId": "10002", "contextId": "10003" } ] }`

---

GET

## Get project mappings for custom field context

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of context to project mappings for a custom field. The result can be filtered by `contextId`. Otherwise, all mappings are returned. Invalid IDs are ignored.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**contextId**

array<integer>

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanCustomFieldContextProjectMapping

A page of items.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/field/{fieldId}/context/projectmapping

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/projectmapping`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "isLast": true, "maxResults": 100, "startAt": 0, "total": 2, "values": [ { "contextId": "10025", "projectId": "10001" }, { "contextId": "10026", "isGlobalContext": true } ] }`

---

PUT

## Update custom field context

Updates a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

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

**description**

string

**name**

string

### Responses

204No Content

Returned if the context is updated.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/field/{fieldId}/context/{contextId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A context used to define the custom field options for bugs.", "name": "Bug fields context" }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete custom field context

Deletes a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).

This API will not allow removing the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:field:jira`

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

### Responses

204No Content

Returned if the context is deleted.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/field/{fieldId}/context/{contextId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Add issue types to context

Adds issue types to a custom field context, appending the issue types to the issue types list.

A custom field context without any issue types applies to all issue types. Adding issue types to such a custom field context would result in it applying to only the listed issue types.

If any of the issue types exists in the custom field context, the operation fails and no issue types are added.

This API will not allow adding issue types to the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

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

**issueTypeIds**

array<string>

Required

### Responses

204No Content

Returned if operation is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

PUT/rest/api/3/field/{fieldId}/context/{contextId}/issuetype

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeIds": [ "10001", "10005", "10006" ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/issuetype`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Remove issue types from context

Removes issue types from a custom field context.

A custom field context without any issue types applies to all issue types.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

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

**issueTypeIds**

array<string>

Required

### Responses

204No Content

Returned if operation is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeIds": [ "10001", "10005", "10006" ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Assign custom field context to projects

Assigns a custom field context to projects.

If any project in the request is assigned to any context of the custom field, the operation fails.

This API will not allow adding projects to the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

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

**projectIds**

array<string>

Required

### Responses

204No Content

Returned if operation is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/field/{fieldId}/context/{contextId}/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "projectIds": [ "10001", "10005", "10006" ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/project`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Remove custom field context from projects

Removes a custom field context from projects.

A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects.

If any project in the request is not assigned to the context, or the operation would result in two global contexts for the field, the operation fails.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

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

**projectIds**

array<string>

Required

### Responses

204No Content

Returned if the custom field context is removed from the projects.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/field/{fieldId}/context/{contextId}/project/remove

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "projectIds": [ "10001", "10005", "10006" ] }`; const response = await requestJira(`/rest/api/3/field/{fieldId}/context/{contextId}/project/remove`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`