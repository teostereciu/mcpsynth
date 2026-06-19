# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-status/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Status

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents statuses. Use it to search, get, create, delete, and change statuses.

Operations

[GET/rest/api/3/statuses](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-get)[PUT/rest/api/3/statuses](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-put)[POST/rest/api/3/statuses](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-post)[DEL/rest/api/3/statuses](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-delete)[GET/rest/api/3/statuses/byNames](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-bynames-get)[GET/rest/api/3/statuses/search](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-search-get)[GET/rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-statusid-project-projectid-issuetypeusages-get)[GET/rest/api/3/statuses/{statusId}/projectUsages](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-statusid-projectusages-get)[GET/rest/api/3/statuses/{statusId}/workflowUsages](/cloud/jira/platform/rest/v3/api-group-status/#api-rest-api-3-statuses-statusid-workflowusages-get)

---

GET

## Bulk get statuses

Returns a list of the statuses specified by one or more status IDs.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Administer Jira_ [project permission.](https://confluence.atlassian.com/x/yodKLg)


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**id**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<JiraStatus>

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/statuses

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses?id={id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``[ { "description": "The issue is resolved", "id": "1000", "name": "Finished", "scope": { "project": { "id": "1" }, "type": "PROJECT" }, "statusCategory": "DONE" } ]`

---

PUT

## Bulk update statuses

Updates statuses by ID.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Administer Jira_ [project permission.](https://confluence.atlassian.com/x/yodKLg)


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The list of statuses that will be updated.

**statuses**

array<StatusUpdate>

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

409Conflict

PUT/rest/api/3/statuses

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "statuses": [ { "description": "The issue is resolved", "id": "1000", "name": "Finished", "statusCategory": "DONE" } ] }`; const response = await requestJira(`/rest/api/3/statuses`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Bulk create statuses

Creates statuses for a global or project scope.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Administer Jira_ [project permission.](https://confluence.atlassian.com/x/yodKLg)


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

Details of the statuses being created and their scope.

**scope**

StatusScope

Required

**statuses**

array<StatusCreate>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<JiraStatus>

Show child properties

400Bad Request

401Unauthorized

409Conflict

POST/rest/api/3/statuses

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "scope": { "project": { "id": "1" }, "type": "PROJECT" }, "statuses": [ { "description": "The issue is resolved", "name": "Finished", "statusCategory": "DONE" } ] }`; const response = await requestJira(`/rest/api/3/statuses`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``[ { "description": "The issue is resolved", "id": "1000", "name": "Finished", "scope": { "project": { "id": "1" }, "type": "PROJECT" }, "statusCategory": "DONE" } ]`

---

DEL

## Bulk delete Statuses

Deletes statuses by ID.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Administer Jira_ [project permission.](https://confluence.atlassian.com/x/yodKLg)


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**id**

array<string>

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

DEL/rest/api/3/statuses

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses?id={id}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Bulk get statuses by name

Returns a list of the statuses specified by one or more status names.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Administer Jira_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Browse projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**name**

array<string>

Required

**projectId**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<JiraStatus>

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/statuses/byNames

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses/byNames?name={name}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``[ { "description": "The issue is resolved", "id": "1000", "name": "Finished", "scope": { "project": { "id": "1" }, "type": "PROJECT" }, "statusCategory": "DONE" } ]`

---

GET

## Search statuses paginated

Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)
  * _Administer Jira_ [project permission.](https://confluence.atlassian.com/x/yodKLg)


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**projectId**

string

**startAt**

integer

**maxResults**

integer

**searchString**

string

**statusCategory**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageOfStatuses

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/statuses/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``{ "isLast": true, "maxResults": 2, "nextPage": "https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=2&maxResults=2", "self": "https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=0&maxResults=2", "startAt": 0, "total": 5, "values": [ { "description": "The issue is resolved", "id": "1000", "name": "Finished", "scope": { "project": { "id": "1" }, "type": "PROJECT" }, "statusCategory": "DONE" } ] }`

---

GET

## Get issue type usages by status and project

Returns a page of issue types in a project using a given status.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:project:jira`, `read:status:jira`, `read:issue-type:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**statusId**

string

Required

**projectId**

string

Required

#### Query parameters

Expand all

**nextPageToken**

string

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

StatusProjectIssueTypeUsageDTO

The issue types using this status in a project.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "issueTypes": { "nextPageToken": "eyJvIjoyfQ==", "values": [ { "id": "1000" } ] }, "projectId": "2000", "statusId": "1000" }`

---

GET

## Get project usages by status

Returns a page of projects using a given status.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:project:jira`, `read:status:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**statusId**

string

Required

#### Query parameters

Expand all

**nextPageToken**

string

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

StatusProjectUsageDTO

The projects using this status.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/statuses/{statusId}/projectUsages

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses/{statusId}/projectUsages`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "projects": { "nextPageToken": "eyJvIjoyfQ==", "values": [ { "id": "1000" } ] }, "statusId": "1000" }`

---

GET

## Get workflow usages by status

Returns a page of workflows using a given status.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow:jira`, `read:status:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**statusId**

string

Required

#### Query parameters

Expand all

**nextPageToken**

string

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

StatusWorkflowUsageDTO

Workflows using the status.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/statuses/{statusId}/workflowUsages

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuses/{statusId}/workflowUsages`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "statusId": "1000", "workflows": { "nextPageToken": "eyJvIjoyfQ==", "values": [ { "id": "545d80a3-91ff-4949-8b0d-a2bc484e70e5" } ] } }`