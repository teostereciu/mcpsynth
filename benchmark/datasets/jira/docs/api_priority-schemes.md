# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-priority-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Priority schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue priority schemes. Use it to get priority schemes and related information, and to create, update and delete priority schemes.

Operations

[GET/rest/api/3/priorityscheme](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-get)[POST/rest/api/3/priorityscheme](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-post)[POST/rest/api/3/priorityscheme/mappings](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-mappings-post)[GET/rest/api/3/priorityscheme/priorities/available](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-priorities-available-get)[PUT/rest/api/3/priorityscheme/{schemeId}](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-schemeid-put)[DEL/rest/api/3/priorityscheme/{schemeId}](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-schemeid-delete)[GET/rest/api/3/priorityscheme/{schemeId}/priorities](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-schemeid-priorities-get)[GET/rest/api/3/priorityscheme/{schemeId}/projects](/cloud/jira/platform/rest/v3/api-group-priority-schemes/#api-rest-api-3-priorityscheme-schemeid-projects-get)

---

GET

## Get priority schemesExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of priority schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**priorityId**

array<integer>

**schemeId**

array<integer>

**schemeName**

string

**onlyDefault**

boolean

**orderBy**

string

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/priorityscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priorityscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 1, "values": [ { "description": "This is the default scheme used by all new and unassigned projects", "id": "1", "isDefault": true, "name": "Default Priority Scheme", "priorities": { "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "description": "Serious problem that could block progress.", "iconUrl": "/images/icons/priorities/high.svg", "id": "1", "isDefault": false, "name": "High", "statusColor": "#f15C75" }, { "description": "Has the potential to affect progress.", "iconUrl": "/images/icons/priorities/medium.svg", "id": "2", "isDefault": true, "name": "Medium", "statusColor": "#f79232" }, { "description": "Minor problem or easily worked around.", "iconUrl": "/images/icons/priorities/low.svg", "id": "3", "isDefault": false, "name": "Low", "statusColor": "#707070" } ] }, "projects": { "isLast": true, "maxResults": 50, "startAt": 0, "total": 1, "values": [ { "avatarUrls": { "16x16": "secure/projectavatar?size=xsmall&pid=10000", "24x24": "secure/projectavatar?size=small&pid=10000", "32x32": "secure/projectavatar?size=medium&pid=10000", "48x48": "secure/projectavatar?size=large&pid=10000" }, "id": "10000", "key": "EX", "name": "Example", "projectCategory": { "description": "Project category description", "id": "10000", "name": "A project category" }, "projectTypeKey": "ProjectTypeKey{key='software'}", "self": "project/EX", "simplified": false } ] } } ] }`

---

POST

## Create priority schemeExperimental

Creates a new priority scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**defaultPriorityId**

integer

Required

**description**

string

**mappings**

PriorityMapping

**name**

string

Required

**priorityIds**

array<integer>

Required

**projectIds**

array<integer>

### Responses

201Created

Returned if the request is completed.

#### application/json

PrioritySchemeId

The ID of a priority scheme.

Show child properties

202Accepted

400Bad Request

401Unauthorized

403Forbidden

409Conflict

POST/rest/api/3/priorityscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultPriorityId": 10001, "description": "My priority scheme description", "mappings": { "in": { "10002": 10000, "10005": 10001, "10006": 10001, "10008": 10003 }, "out": {} }, "name": "My new priority scheme", "priorityIds": [ 10000, 10001, 10003 ], "projectIds": [ 10005, 10006, 10007 ] }`; const response = await requestJira(`/rest/api/3/priorityscheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": "10001" }`

---

POST

## Suggested priorities for mappingsExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of priorities that would require mapping, given a change in priorities or projects associated with a priority scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**maxResults**

integer

**priorities**

SuggestedMappingsForPrioritiesRequestBean

**projects**

SuggestedMappingsForProjectsRequestBean

**schemeId**

integer

**startAt**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanPriorityWithSequence

A page of items.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/priorityscheme/mappings

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "maxResults": 50, "priorities": { "add": [ 10001, 10002 ], "remove": [ 10003 ] }, "projects": { "add": [ 10021 ] }, "schemeId": 10005, "startAt": 0 }`; const response = await requestJira(`/rest/api/3/priorityscheme/mappings`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "description": "Serious problem that could block progress.", "iconUrl": "/images/icons/priorities/high.svg", "id": "1", "isDefault": false, "name": "High", "statusColor": "#f15C75" }, { "description": "Has the potential to affect progress.", "iconUrl": "/images/icons/priorities/medium.svg", "id": "2", "isDefault": true, "name": "Medium", "statusColor": "#f79232" }, { "description": "Minor problem or easily worked around.", "iconUrl": "/images/icons/priorities/low.svg", "id": "3", "isDefault": false, "name": "Low", "statusColor": "#707070" } ] }`

---

GET

## Get available priorities by priority schemeExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of priorities available for adding to a priority scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**query**

string

**schemeId**

string

Required

**exclude**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanPriorityWithSequence

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/priorityscheme/priorities/available

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priorityscheme/priorities/available?schemeId={schemeId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "description": "Serious problem that could block progress.", "iconUrl": "/images/icons/priorities/high.svg", "id": "1", "isDefault": false, "name": "High", "statusColor": "#f15C75" }, { "description": "Has the potential to affect progress.", "iconUrl": "/images/icons/priorities/medium.svg", "id": "2", "isDefault": true, "name": "Medium", "statusColor": "#f79232" }, { "description": "Minor problem or easily worked around.", "iconUrl": "/images/icons/priorities/low.svg", "id": "3", "isDefault": false, "name": "Low", "statusColor": "#707070" } ] }`

---

PUT

## Update priority schemeExperimental

Updates a priority scheme. This includes its details, the lists of priorities and projects in it

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**schemeId**

integer

Required

#### Request bodyapplication/json

Expand all

**defaultPriorityId**

integer

**description**

string

**mappings**

PriorityMapping

**name**

string

**priorities**

UpdatePrioritiesInSchemeRequestBean

**projects**

UpdateProjectsInSchemeRequestBean

### Responses

202Accepted

Returned if the request is accepted.

#### application/json

UpdatePrioritySchemeResponseBean

Details of the updated priority scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

409Conflict

PUT/rest/api/3/priorityscheme/{schemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultPriorityId": 10001, "description": "My priority scheme description", "mappings": { "in": { "10003": 10002, "10004": 10001 }, "out": { "10001": 10005, "10002": 10006 } }, "name": "My new priority scheme", "priorities": { "add": { "ids": [ 10001, 10002 ] }, "remove": { "ids": [ 10003, 10004 ] } }, "projects": { "add": { "ids": [ 10101, 10102 ] }, "remove": { "ids": [ 10103, 10104 ] } } }`; const response = await requestJira(`/rest/api/3/priorityscheme/{schemeId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

202Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 ``{ "task": { "self": "https://your-domain.atlassian.net/rest/api/3/task/1", "id": "1", "description": "Task description", "status": "COMPLETE", "result": "the task result, this may be any JSON", "submittedBy": 10000, "progress": 100, "elapsedRuntime": 156, "submitted": 1501708132800, "started": 1501708132900, "finished": 1501708133000, "lastUpdate": 1501708133000 }, "updated": { "description": "This is the default scheme used by all new and unassigned projects", "id": "1", "isDefault": true, "name": "Default Priority Scheme", "priorities": { "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "description": "Serious problem that could block progress.", "iconUrl": "/images/icons/priorities/high.svg", "id": "1", "isDefault": false, "name": "High", "statusColor": "#f15C75" }, { "description": "Has the potential to affect progress.", "iconUrl": "/images/icons/priorities/medium.svg", "id": "2", "isDefault": true, "name": "Medium", "statusColor": "#f79232" }, { "description": "Minor problem or easily worked around.", "iconUrl": "/images/icons/priorities/low.svg", "id": "3", "isDefault": false, "name": "Low", "statusColor": "#707070" } ] }, "projects": { "isLast": true, "maxResults": 50, "startAt": 0, "total": 1, "values": [ { "avatarUrls": { "16x16": "secure/projectavatar?size=xsmall&pid=10000", "24x24": "secure/projectavatar?size=small&pid=10000", "32x32": "secure/projectavatar?size=medium&pid=10000", "48x48": "secure/projectavatar?size=large&pid=10000" }, "id": "10000", "key": "EX", "name": "Example", "projectCategory": { "description": "Project category description", "id": "10000", "name": "A project category" }, "projectTypeKey": "ProjectTypeKey{key='software'}", "self": "project/EX", "simplified": false } ] } } }`

---

DEL

## Delete priority schemeExperimental

Deletes a priority scheme.

This operation is only available for priority schemes without any associated projects. Any associated projects must be removed from the priority scheme before this operation can be performed.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**schemeId**

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

DEL/rest/api/3/priorityscheme/{schemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priorityscheme/{schemeId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get priorities by priority schemeExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of priorities by scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**schemeId**

string

Required

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanPriorityWithSequence

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/priorityscheme/{schemeId}/priorities

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priorityscheme/{schemeId}/priorities`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 3, "values": [ { "description": "Serious problem that could block progress.", "iconUrl": "/images/icons/priorities/high.svg", "id": "1", "isDefault": false, "name": "High", "statusColor": "#f15C75" }, { "description": "Has the potential to affect progress.", "iconUrl": "/images/icons/priorities/medium.svg", "id": "2", "isDefault": true, "name": "Medium", "statusColor": "#f79232" }, { "description": "Minor problem or easily worked around.", "iconUrl": "/images/icons/priorities/low.svg", "id": "3", "isDefault": false, "name": "Low", "statusColor": "#707070" } ] }`

---

GET

## Get projects by priority schemeExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of projects by scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:priority-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**schemeId**

string

Required

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**projectId**

array<integer>

**query**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanProject

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/priorityscheme/{schemeId}/projects

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/priorityscheme/{schemeId}/projects`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 1, "values": [ { "avatarUrls": { "16x16": "secure/projectavatar?size=xsmall&pid=10000", "24x24": "secure/projectavatar?size=small&pid=10000", "32x32": "secure/projectavatar?size=medium&pid=10000", "48x48": "secure/projectavatar?size=large&pid=10000" }, "id": "10000", "key": "EX", "name": "Example", "projectCategory": { "description": "Project category description", "id": "10000", "name": "A project category" }, "projectTypeKey": "ProjectTypeKey{key='software'}", "self": "project/EX", "simplified": false } ] }`