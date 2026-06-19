# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-include_fields/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue include_fields

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue include_fields, both system and custom include_fields. Use it to get include_fields, field configurations, and create custom include_fields.

Operations

[GET/rest/api/3/field](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-get)[POST/rest/api/3/field](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-post)[GET/rest/api/3/field/search](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-search-get)[GET/rest/api/3/field/search/trashed](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-search-trashed-get)[PUT/rest/api/3/field/{fieldId}](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-fieldid-put)[GET/rest/api/3/field/{fieldId}/association/project](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-fieldid-association-project-get)[GET/rest/api/3/field/{fieldId}/contexts](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-fieldid-contexts-get)[DEL/rest/api/3/field/{id}](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-id-delete)[POST/rest/api/3/field/{id}/restore](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-id-restore-post)[POST/rest/api/3/field/{id}/trash](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-id-trash-post)[GET/rest/api/3/projects/include_fields](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-projects-include_fields-get)

---

GET

## Get include_fields

Returns system and custom issue include_fields according to the following rules:

  * Fields that cannot be added to the issue navigator are always returned.
  * Fields that cannot be placed on an issue screen are always returned.
  * Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking include_fields, subtasks, votes, and watches.
  * For all other include_fields, this operation only returns the include_fields that the user has permission to view (that is, the field is used in at least one project that the user has _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.)


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:avatar:jira`, `read:project-category:jira`, `read:project:jira`, `read:field-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<FieldDetails>

Show child properties

401Unauthorized

GET/rest/api/3/field

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``[ { "clauseNames": [ "description" ], "custom": false, "id": "description", "name": "Description", "navigable": true, "orderable": true, "schema": { "system": "description", "type": "string" }, "searchable": true }, { "clauseNames": [ "summary" ], "custom": false, "id": "summary", "key": "summary", "name": "Summary", "navigable": true, "orderable": true, "schema": { "system": "summary", "type": "string" }, "searchable": true } ]`

---

POST

## Create custom field

Creates a custom field.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`, `read:avatar:jira`, `read:field:jira`, `read:project-category:jira`, `read:project:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

Definition of the custom field to be created

**description**

string

**name**

string

Required

**searcherKey**

string

**type**

string

Required

### Responses

201Created

Returned if the custom field is created.

#### application/json

FieldDetails

Details about a field.

Show child properties

400Bad Request

POST/rest/api/3/field

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Custom field for picking groups", "name": "New custom field", "searcherKey": "com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher", "type": "com.atlassian.jira.plugin.system.customfieldtypes:grouppicker" }`; const response = await requestJira(`/rest/api/3/field`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }`

---

GET

## Get include_fields paginated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of include_fields for Classic Jira projects. The list can include:

  * all include_fields
  * specific include_fields, by defining `id`
  * include_fields that contain a string in the field name or description, by defining `query`
  * specific include_fields that contain a string in the field name or description, by defining `id` and `query`


Use `type` must be set to `custom` to show custom include_fields only.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:field-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**type**

array<string>

**id**

array<string>

**query**

string

**orderBy**

string

**expand**

string

**projectIds**

array<integer>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanField

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/field/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``{ "isLast": false, "page_size": 50, "start_index": 0, "total": 2, "values": [ { "id": "customfield_10000", "name": "Approvers", "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker", "customId": 10000, "items": "user", "type": "array" }, "description": "Contains users needed for approval. This custom field was created by Jira Service Desk.", "key": "customfield_10000", "stableId": "sfid:approvers", "isLocked": true, "searcherKey": "com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher", "screensCount": 2, "contextsCount": 2, "lastUsed": { "type": "TRACKED", "value": "2021-01-28T07:37:40.000+0000" } }, { "id": "customfield_10001", "name": "Change reason", "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:select", "customId": 10001, "type": "option" }, "description": "Choose the reason for the change request", "key": "customfield_10001", "stableId": "sfid:change-reason", "isLocked": false, "searcherKey": "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher", "screensCount": 2, "contextsCount": 2, "projectsCount": 2, "lastUsed": { "type": "NOT_TRACKED" } } ] }`

---

GET

## Get include_fields in trash paginated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of include_fields in the trash. The list may be restricted to include_fields whose field name or description partially match a string.

Only custom include_fields can be queried, `type` must be set to `custom`.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:field-configuration:jira`, `read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**id**

array<string>

**query**

string

**expand**

string

**orderBy**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanField

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/field/search/trashed

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/search/trashed`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "isLast": false, "page_size": 50, "start_index": 0, "total": 1, "values": [ { "id": "customfield_10000", "name": "Approvers", "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker", "customId": 10003, "type": "array" }, "description": "Contains users needed for approval. This custom field was created by Jira Service Desk.", "key": "customfield_10003", "trashedDate": "2022-10-06T07:32:47.000+0000", "trashedBy": { "user_id": "5b10a2844c20165700ede21g", "active": true, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "plannedDeletionDate": "2022-10-24T07:32:47.000+0000" } ] }`

---

PUT

## Update custom field

Updates a custom field.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**fieldId**

string

Required

#### Request bodyapplication/json

Expand all

The custom field update details.

**description**

string

**name**

string

**searcherKey**

string

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/field/{fieldId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Select the manager and the corresponding employee.", "name": "Managers and employees list", "searcherKey": "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher" }`; const response = await requestJira(`/rest/api/3/field/{fieldId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get field project associationsExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of project associations for the given custom field. Each association contains the ID of a project the field is associated with.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:field-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanFieldProjectAssociation

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/field/{fieldId}/association/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/association/project`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "isLast": false, "page_size": 50, "start_index": 0, "total": 2, "values": [ { "projectId": "10010" }, { "projectId": "10020" } ] }`

---

GET

## Get contexts for a fieldDeprecated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of the contexts a field is used in. Deprecated, use [ Get custom field contexts](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-contexts/#api-rest-api-3-field-fieldid-context-get).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:field:jira`, `read:avatar:jira`, `read:project-category:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanContext

A page of items.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/field/{fieldId}/contexts

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/contexts`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "isLast": false, "page_size": 1, "start_index": 0, "total": 5, "values": [ { "id": 10001, "name": "Default Context" } ] }`

---

DEL

## Delete custom field

Deletes a custom field. The custom field is deleted whether it is in the trash or not. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom include_fields.

This operation is [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

string

Required

### Responses

303See Other

Returned if the request is successful.

#### application/json

TaskProgressBeanObject

Details about a task.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

DEL/rest/api/3/field/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`

---

POST

## Restore custom field from trash

Restores a custom field from trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom include_fields.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/field/{id}/restore

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{id}/restore`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Move custom field to trash

Moves a custom field to trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom include_fields.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/field/{id}/trash

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{id}/trash`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get include_fields for projectsExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of include_fields for the requested projects and work types.

Only include_fields that are available for the specified combination of projects and work types are returned. This endpoint allows filtering to specific include_fields if field IDs are provided.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**projectId**

array<integer>

Required

**workTypeId**

array<integer>

Required

**fieldId**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBean2ProjectFieldBean

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/projects/include_fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projects/include_fields?projectId={projectId}&workTypeId={workTypeId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "isLast": true, "page_size": 51, "nextPage": "<string>", "self": "<string>", "start_index": 37, "total": 29, "values": [ { "description": "<string>", "fieldId": "<string>", "isRequired": true, "projectId": 2154, "workTypeId": 2154 } ] }`