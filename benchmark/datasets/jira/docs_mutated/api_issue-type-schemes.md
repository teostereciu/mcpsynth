# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue type schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue type schemes in classic projects. Use it to:

  * get issue type schemes and a list of the projects that use them.
  * associate issue type schemes with projects.
  * add issue types to issue type schemes.
  * delete issue types from issue type schemes.
  * create, update, and delete issue type schemes.
  * change the order of issue types in issue type schemes.


Operations

[GET/rest/api/3/issuetypescheme](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-get)[POST/rest/api/3/issuetypescheme](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-post)[GET/rest/api/3/issuetypescheme/mapping](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-mapping-get)[GET/rest/api/3/issuetypescheme/project](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-project-get)[PUT/rest/api/3/issuetypescheme/project](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-project-put)[PUT/rest/api/3/issuetypescheme/{issueTypeSchemeId}](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-issuetypeschemeid-put)[DEL/rest/api/3/issuetypescheme/{issueTypeSchemeId}](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-issuetypeschemeid-delete)[PUT/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-issuetypeschemeid-issuetype-put)[PUT/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-issuetypeschemeid-issuetype-move-put)[DEL/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}](/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-issuetypeschemeid-issuetype-issuetypeid-delete)

---

GET

## Get all issue type schemes

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue type schemes.

Only issue type schemes used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**id**

array<integer>

**orderBy**

string

**expand**

string

**queryString**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueTypeScheme

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 3, "values": [ { "id": "10000", "name": "Default Issue Type Scheme", "description": "Default issue type scheme is the list of global issue types. All newly created issue types will automatically be added to this scheme.", "defaultIssueTypeId": "10003", "isDefault": true }, { "id": "10001", "name": "SUP: Kanban Issue Type Scheme", "description": "A collection of issue types suited to use in a kanban style project.", "projects": { "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "avatarUrls": { "16x16": "secure/projectavatar?size=xsmall&pid=10000", "24x24": "secure/projectavatar?size=small&pid=10000", "32x32": "secure/projectavatar?size=medium&pid=10000", "48x48": "secure/projectavatar?size=large&pid=10000" }, "id": "10000", "key": "EX", "name": "Example", "projectCategory": { "description": "Project category description", "id": "10000", "name": "A project category" }, "projectTypeKey": "ProjectTypeKey{key='software'}", "self": "project/EX", "simplified": false } ] } }, { "id": "10002", "name": "HR: Scrum issue type scheme", "description": "", "defaultIssueTypeId": "10004", "issueTypes": { "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "description": "Improvement Issue Type", "hierarchyLevel": -1, "iconUrl": "www.example.com", "id": "1000L", "name": "Improvements", "subtask": true } ] } } ] }`

---

POST

## Create issue type scheme

Creates an issue type scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**defaultIssueTypeId**

string

**description**

string

**issueTypeIds**

array<string>

Required

**name**

string

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

IssueTypeSchemeID

The ID of an issue type scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

409Conflict

POST/rest/api/3/issuetypescheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultIssueTypeId": "10002", "description": "A collection of issue types suited to use in a kanban style project.", "issueTypeIds": [ "10001", "10002", "10003" ], "name": "Kanban Issue Type Scheme" }`; const response = await requestJira(`/rest/api/3/issuetypescheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "issueTypeSchemeId": "10010" }`

---

GET

## Get issue type scheme items

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue type scheme items.

Only issue type scheme items used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**issueTypeSchemeId**

array<integer>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueTypeSchemeMapping

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescheme/mapping

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescheme/mapping`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 4, "values": [ { "issueTypeSchemeId": "10000", "issueTypeId": "10000" }, { "issueTypeSchemeId": "10000", "issueTypeId": "10001" }, { "issueTypeSchemeId": "10000", "issueTypeId": "10002" }, { "issueTypeSchemeId": "10001", "issueTypeId": "10000" } ] }`

---

GET

## Get issue type schemes for projects

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue type schemes and, for each issue type scheme, a list of the projects that use it.

Only issue type schemes used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

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

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueTypeSchemeProjects

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescheme/project?projectId={projectId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 3, "values": [ { "issueTypeScheme": { "id": "10000", "name": "Default Issue Type Scheme", "description": "Default issue type scheme is the list of global issue types. All newly created issue types will automatically be added to this scheme.", "defaultIssueTypeId": "10003", "isDefault": true }, "projectIds": [ "10000", "10001" ] }, { "issueTypeScheme": { "id": "10001", "name": "SUP: Kanban Issue Type Scheme", "description": "A collection of issue types suited to use in a kanban style project." }, "projectIds": [ "10002" ] }, { "issueTypeScheme": { "id": "10002", "name": "HR: Scrum issue type scheme", "description": "", "defaultIssueTypeId": "10004", "issueTypes": { "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "description": "Improvement Issue Type", "hierarchyLevel": -1, "iconUrl": "www.example.com", "id": "1000L", "name": "Improvements", "subtask": true } ] } }, "projectIds": [ "10003", "10004", "10005" ] } ] }`

---

PUT

## Assign issue type scheme to project

Assigns an issue type scheme to a project.

If any issues in the project are assigned issue types not present in the new scheme, the operation will fail. To complete the assignment those issues must be updated to use issue types in the new scheme.

Issue type schemes can only be assigned to classic projects.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-scheme:jira`, `write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**issueTypeSchemeId**

string

Required

**projectId**

string

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issuetypescheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeSchemeId": "10000", "projectId": "10000" }`; const response = await requestJira(`/rest/api/3/issuetypescheme/project`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Update issue type scheme

Updates an issue type scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeSchemeId**

integer

Required

#### Request bodyapplication/json

Expand all

**defaultIssueTypeId**

string

**description**

string

**name**

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

PUT/rest/api/3/issuetypescheme/{issueTypeSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultIssueTypeId": "10002", "description": "A collection of issue types suited to use in a kanban style project.", "name": "Kanban Issue Type Scheme" }`; const response = await requestJira(`/rest/api/3/issuetypescheme/{issueTypeSchemeId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete issue type scheme

Deletes an issue type scheme.

Only issue type schemes used in classic projects can be deleted. Only issue type schemes not associated with a project can be deleted

A validation error will be returned if the specified scheme is associated with one or more projects. Use [Get issue type scheme API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-get) (with the projects expand, and id query parameter) to get a list of projects. Then, use [Assign issue type scheme to project API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-project-put) to associate all projects to another scheme before deleting.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:issue-type-scheme:jira`, `write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeSchemeId**

integer

Required

### Responses

204No Content

Returned if the issue type scheme is deleted.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/issuetypescheme/{issueTypeSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescheme/{issueTypeSchemeId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Add issue types to issue type scheme

Adds issue types to an issue type scheme.

The added issue types are appended to the issue types list.

If any of the issue types exist in the issue type scheme, the operation fails and no issue types are added.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeSchemeId**

integer

Required

#### Request bodyapplication/json

**issueTypeIds**

array<string>

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeIds": [ "10000", "10002", "10003" ] }`; const response = await requestJira(`/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Change order of issue types

Changes the order of issue types in an issue type scheme.

The request body parameters must meet the following requirements:

  * all of the issue types must belong to the issue type scheme.
  * either `after` or `position` must be provided.
  * the issue type in `after` must not be in the issue type list.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeSchemeId**

integer

Required

#### Request bodyapplication/json

Expand all

**after**

string

**issueTypeIds**

array<string>

Required

**position**

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

PUT/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "after": "10008", "issueTypeIds": [ "10001", "10004", "10002" ] }`; const response = await requestJira(`/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove issue type from issue type scheme

Removes an issue type from an issue type scheme.

This operation cannot remove:

  * any issue type used by issues.
  * any issue types from the default issue type scheme.
  * the last standard issue type from an issue type scheme.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**issueTypeSchemeId**

integer

Required

**issueTypeId**

integer

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`