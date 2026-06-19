# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-priorities/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue priorities

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue priorities. Use it to get, create and update issue priorities and details for individual issue priorities.

Operations

[GET/rest/api/3/priority](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-get)[POST/rest/api/3/priority](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-post)[PUT/rest/api/3/priority/default](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-default-put)[PUT/rest/api/3/priority/move](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-move-put)[GET/rest/api/3/priority/search](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-search-get)[GET/rest/api/3/priority/{id}](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-id-get)[PUT/rest/api/3/priority/{id}](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-id-put)[DEL/rest/api/3/priority/{id}](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-id-delete)

---

GET

## Get prioritiesDeprecated

Returns the list of all issue priorities.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:priority:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Priority>

Show child properties

401Unauthorized

GET/rest/api/3/priority

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priority`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``[ { "description": "Major loss of function.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/major.png", "id": "1", "name": "Major", "self": "https://your-domain.atlassian.net/rest/api/3/priority/3", "statusColor": "#009900" }, { "description": "Very little impact.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/trivial.png", "id": "2", "name": "Trivial", "self": "https://your-domain.atlassian.net/rest/api/3/priority/5", "statusColor": "#cfcfcf" } ]`

---

POST

## Create priorityDeprecated

Creates an issue priority.

Deprecation applies to iconUrl param in request body which will be sunset on 16th Mar 2025. For more details refer to [changelog](https://developer.atlassian.com/changelog/#CHANGE-1525).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**avatarId**

integer

**description**

string

**iconUrl**

string

**name**

string

Required

**statusColor**

string

Required

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

PriorityId

The ID of an issue priority.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/priority

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My priority description", "iconUrl": "/images/icons/priorities/major.png", "name": "My new priority", "statusColor": "#ABCDEF" }`; const response = await requestJira(`/rest/api/3/priority`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": "10001" }`

---

PUT

## Set default priority

Sets default issue priority.

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

PUT/rest/api/3/priority/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "id": "3" }`; const response = await requestJira(`/rest/api/3/priority/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Move priorities

Changes the order of issue priorities.

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

PUT/rest/api/3/priority/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "after": "10003", "ids": [ "10004", "10005" ] }`; const response = await requestJira(`/rest/api/3/priority/move`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Search prioritiesDeprecated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria:

  * a list of priority IDs. Any invalid priority IDs are ignored.
  * a list of project IDs. Only priorities that are available in these projects will be returned. Any invalid project IDs are ignored.
  * whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

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

**projectId**

array<string>

**priorityName**

string

**onlyDefault**

boolean

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanPriority

A page of items.

Show child properties

401Unauthorized

GET/rest/api/3/priority/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priority/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``{ "isLast": true, "page_size": 50, "start_index": 0, "total": 2, "values": [ { "description": "Major loss of function.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/major.png", "id": "1", "isDefault": true, "name": "Major", "self": "https://your-domain.atlassian.net/rest/api/3/priority/3", "statusColor": "#009900" }, { "description": "Very little impact.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/trivial.png", "id": "2", "isDefault": false, "name": "Trivial", "self": "https://your-domain.atlassian.net/rest/api/3/priority/5", "statusColor": "#cfcfcf" } ] }`

---

GET

## Get priority

Returns an issue priority.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:priority:jira`

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

Priority

An issue priority.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/priority/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priority/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "description": "Major loss of function.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/major.png", "id": "1", "name": "Major", "self": "https://your-domain.atlassian.net/rest/api/3/priority/3", "statusColor": "#009900" }`

---

PUT

## Update priorityDeprecated

Updates an issue priority.

At least one request body parameter must be defined.

Deprecation applies to iconUrl param in request body which will be sunset on 16th Mar 2025. For more details refer to [changelog](https://developer.atlassian.com/changelog/#CHANGE-1525).

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

**avatarId**

integer

**description**

string

**iconUrl**

string

**name**

string

**statusColor**

string

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

PUT/rest/api/3/priority/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My updated priority description", "iconUrl": "/images/icons/priorities/minor.png", "name": "My updated priority", "statusColor": "#123456" }`; const response = await requestJira(`/rest/api/3/priority/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete priority

Deletes an issue priority.

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

DEL/rest/api/3/priority/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priority/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`