# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-resolutions/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue resolutions

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue resolution values. Use it to obtain a list of all issue resolution values and the details of individual resolution values.

Operations

[GET/rest/api/3/resolution](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-get)[POST/rest/api/3/resolution](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-post)[PUT/rest/api/3/resolution/default](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-default-put)[PUT/rest/api/3/resolution/move](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-move-put)[GET/rest/api/3/resolution/search](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-search-get)[GET/rest/api/3/resolution/{id}](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-id-get)[PUT/rest/api/3/resolution/{id}](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-id-put)[DEL/rest/api/3/resolution/{id}](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-id-delete)

---

GET

## Get resolutionsDeprecated

Returns a list of all issue resolution values.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:resolution:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Resolution>

Show child properties

401Unauthorized

GET/rest/api/3/resolution

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/resolution`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``[ { "description": "A fix for this issue is checked into the tree and tested.", "id": "10000", "name": "Fixed", "self": "https://your-domain.atlassian.net/rest/api/3/resolution/1" }, { "description": "This is what it is supposed to do.", "id": "10001", "name": "Works as designed", "self": "https://your-domain.atlassian.net/rest/api/3/resolution/3" } ]`

---

POST

## Create resolutionExperimental

Creates an issue resolution.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

Required

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

ResolutionId

The ID of an issue resolution.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/resolution

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My resolution description", "name": "My new resolution" }`; const response = await requestJira(`/rest/api/3/resolution`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": "10001" }`

---

PUT

## Set default resolutionExperimental

Sets default issue resolution.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

**id**

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

PUT/rest/api/3/resolution/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "id": "3" }`; const response = await requestJira(`/rest/api/3/resolution/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Move resolutionsExperimental

Changes the order of issue resolutions.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**after**

string

**ids**

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

PUT/rest/api/3/resolution/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "after": "10002", "ids": [ "10000", "10001" ] }`; const response = await requestJira(`/rest/api/3/resolution/move`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Search resolutionsExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria:

  * a list of resolutions IDs.
  * whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:resolution:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start_index**

string

**page_size**

string

**id**

array<string>

**onlyDefault**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanResolutionJsonBean

A page of items.

Show child properties

401Unauthorized

GET/rest/api/3/resolution/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/resolution/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "isLast": true, "page_size": 50, "start_index": 0, "total": 1, "values": [ { "description": "This is what it is supposed to do.", "id": "10001", "isDefault": true, "name": "Works as designed" } ] }`

---

GET

## Get resolution

Returns an issue resolution value.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:resolution:jira`

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

Resolution

Details of an issue resolution.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/resolution/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/resolution/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "A fix for this issue is checked into the tree and tested.", "id": "10000", "name": "Fixed", "self": "https://your-domain.atlassian.net/rest/api/3/resolution/1" }`

---

PUT

## Update resolutionExperimental

Updates an issue resolution.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

Required

**Additional Properties**

any

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/resolution/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My updated resolution description", "name": "My updated resolution" }`; const response = await requestJira(`/rest/api/3/resolution/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete resolutionExperimental

Deletes an issue resolution.

This operation is [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**replaceWith**

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

DEL/rest/api/3/resolution/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/resolution/{id}?replaceWith={replaceWith}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`