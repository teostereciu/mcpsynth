# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue security schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue security schemes. Use it to get an issue security scheme or a list of issue security schemes.

Issue security schemes control which users or groups of users can view an issue. When an issue security scheme is associated with a project, its security levels can be applied to issues in that project. Sub-tasks also inherit the security level of their parent issue.

Operations

[GET/rest/api/3/issuesecurityschemes](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-get)[POST/rest/api/3/issuesecurityschemes](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-post)[GET/rest/api/3/issuesecurityschemes/level](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-level-get)[PUT/rest/api/3/issuesecurityschemes/level/default](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-level-default-put)[GET/rest/api/3/issuesecurityschemes/level/member](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-level-member-get)[GET/rest/api/3/issuesecurityschemes/project](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-project-get)[PUT/rest/api/3/issuesecurityschemes/project](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-project-put)[GET/rest/api/3/issuesecurityschemes/search](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-search-get)[GET/rest/api/3/issuesecurityschemes/{id}](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-id-get)[PUT/rest/api/3/issuesecurityschemes/{id}](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-id-put)[DEL/rest/api/3/issuesecurityschemes/{schemeId}](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-schemeid-delete)[PUT/rest/api/3/issuesecurityschemes/{schemeId}/level](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-schemeid-level-put)[PUT/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-schemeid-level-levelid-put)[DEL/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-schemeid-level-levelid-delete)[PUT/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-schemeid-level-levelid-member-put)[DEL/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-schemeid-level-levelid-member-memberid-delete)

---

GET

## Get issue security schemes

Returns all [issue security schemes](https://confluence.atlassian.com/x/J4lKLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:issue-security-level:jira`, `read:issue-security-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

SecuritySchemes

List of security schemes.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/issuesecurityschemes

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "issueSecuritySchemes": [ { "defaultSecurityLevelId": 10021, "description": "Description for the default issue security scheme", "id": 10000, "name": "Default Issue Security Scheme", "self": "https://your-domain.atlassian.net/rest/api/3/issuesecurityschemes/10000" } ] }`

---

POST

## Create issue security schemeExperimental

Creates a security scheme with security scheme levels and levels' members. You can create up to 100 security scheme levels and security scheme levels' members per request.

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

**levels**

array<SecuritySchemeLevelBean>

**name**

string

Required

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

SecuritySchemeId

The ID of the issue security scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/issuesecurityschemes

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Newly created issue security scheme", "levels": [ { "description": "Newly created level", "isDefault": true, "members": [ { "parameter": "administrators", "type": "group" } ], "name": "New level" } ], "name": "New security scheme" }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": "10001" }`

---

GET

## Get issue security levelsExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue security levels.

Only issue security levels in the context of classic projects are returned.

Filtering using IDs is inclusive: if you specify both security scheme IDs and level IDs, the result will include both specified issue security levels and all issue security levels from the specified schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-security-level:jira`, `read:issue-security-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**id**

array<string>

**schemeId**

array<string>

**onlyDefault**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanSecurityLevel

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuesecurityschemes/level

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/level`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 1, "values": [ { "description": "Only the reporter and internal staff can see this issue.", "id": "10021", "isDefault": true, "issueSecuritySchemeId": "10001", "name": "Reporter Only", "self": "https://your-domain.atlassian.net/rest/api/3/issuesecurityscheme/level?id=10021" } ] }`

---

PUT

## Set default issue security levelsExperimental

Sets default issue security levels for schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**defaultValues**

array<DefaultLevelValue>

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

PUT/rest/api/3/issuesecurityschemes/level/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultValues": [ { "defaultLevelId": "20000", "issueSecuritySchemeId": "10000" }, { "defaultLevelId": "30000", "issueSecuritySchemeId": "12000" } ] }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes/level/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get issue security level membersExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue security level members.

Only issue security level members in the context of classic projects are returned.

Filtering using parameters is inclusive: if you specify both security scheme IDs and level IDs, the result will include all issue security level members from the specified schemes and levels.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-security-level:jira`, `read:issue-security-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**id**

array<string>

**schemeId**

array<string>

**levelId**

array<string>

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanSecurityLevelMember

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuesecurityschemes/level/member

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/level/member`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "isLast": true, "maxResults": 100, "startAt": 0, "total": 3, "values": [ { "id": "10000", "issueSecurityLevelId": "20010", "issueSecuritySchemeId": "10010", "holder": { "expand": "group", "type": "group" } } ] }`

---

GET

## Get projects using issue security schemesExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) mapping of projects that are using security schemes. You can provide either one or multiple security scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Only issue security schemes in the context of classic projects are supported. **[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**issueSecuritySchemeId**

array<string>

**projectId**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueSecuritySchemeToProjectMapping

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuesecurityschemes/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/project`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "issueSecuritySchemeId": "10000", "projectId": "10000" }`

---

PUT

## Associate security scheme to projectExperimental

Associates an issue security scheme with a project and remaps security levels of issues to the new levels, if provided.

This operation is [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**oldToNewSecurityLevelMappings**

array<OldToNewSecurityLevelMappingsBean>

**projectId**

string

Required

**schemeId**

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

PUT/rest/api/3/issuesecurityschemes/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "oldToNewSecurityLevelMappings": [ { "newLevelId": "30001", "oldLevelId": "30000" } ], "projectId": "10000", "schemeId": "20000" }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes/project`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`

---

GET

## Search issue security schemesExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue security schemes.
If you specify the project ID parameter, the result will contain issue security schemes and related project IDs you filter by. Use {@link IssueSecuritySchemeResource#searchProjectsUsingSecuritySchemes(String, String, Set, Set)} to obtain all projects related to scheme.

Only issue security schemes in the context of classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-security-level:jira`, `read:issue-security-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Query parameters

Expand all

**startAt**

string

**maxResults**

string

**id**

array<string>

**projectId**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanSecuritySchemeWithProjects

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuesecurityschemes/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "id": 10000, "self": "https://your-domain.atlassian.net/rest/api/3/issuesecurityscheme/10000", "name": "Default scheme", "description": "Default scheme description", "defaultLevel": 10001, "projectIds": [ 10002 ] }`

---

GET

## Get issue security scheme

Returns an issue security scheme along with its security levels.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for a project that uses the requested issue security scheme.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:issue-security-level:jira`, `read:issue-security-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

SecurityScheme

Details about a security scheme.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/issuesecurityschemes/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "defaultSecurityLevelId": 10021, "description": "Description for the default issue security scheme", "id": 10000, "levels": [ { "description": "Only the reporter and internal staff can see this issue.", "id": "10021", "name": "Reporter Only", "self": "https://your-domain.atlassian.net/rest/api/3/securitylevel/10021" } ], "name": "Default Issue Security Scheme", "self": "https://your-domain.atlassian.net/rest/api/3/issuesecurityschemes/10000" }`

---

PUT

## Update issue security schemeExperimental

Updates the issue security scheme.

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

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issuesecurityschemes/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My issue security scheme description", "name": "My issue security scheme name" }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete issue security schemeExperimental

Deletes an issue security scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**schemeId**

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

DEL/rest/api/3/issuesecurityschemes/{schemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{schemeId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Add issue security levelsExperimental

Adds levels and levels' members to the issue security scheme. You can add up to 100 levels per request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**schemeId**

string

Required

#### Request bodyapplication/json

**levels**

array<SecuritySchemeLevelBean>

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issuesecurityschemes/{schemeId}/level

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "levels": [ { "description": "First Level Description", "isDefault": true, "members": [ { "type": "reporter" }, { "parameter": "jira-administrators", "type": "group" } ], "name": "First Level" } ] }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{schemeId}/level`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Update issue security levelExperimental

Updates the issue security level.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**schemeId**

string

Required

**levelId**

string

Required

#### Request bodyapplication/json

Expand all

**description**

string

**name**

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

PUT/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "New level description", "name": "New level name" }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove issue security levelExperimental

Deletes an issue security level.

This operation is [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**schemeId**

string

Required

**levelId**

string

Required

#### Query parameters

**replaceWith**

string

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

DEL/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`

---

PUT

## Add issue security level membersExperimental

Adds members to the issue security level. You can add up to 100 members per request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**schemeId**

string

Required

**levelId**

string

Required

#### Request bodyapplication/json

**members**

array<SecuritySchemeLevelMemberBean>

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "members": [ { "type": "reporter" }, { "parameter": "jira-administrators", "type": "group" } ] }`; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove member from issue security levelExperimental

Removes an issue security level member from an issue security scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**schemeId**

string

Required

**levelId**

string

Required

**memberId**

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

DEL/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`