# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-plans/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Plans

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents plans. Use it to get, create, duplicate, update, trash and archive plans.

Operations

[GET/rest/api/3/plans/plan](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-get)[POST/rest/api/3/plans/plan](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-post)[GET/rest/api/3/plans/plan/{planId}](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-planid-get)[PUT/rest/api/3/plans/plan/{planId}](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-planid-put)[PUT/rest/api/3/plans/plan/{planId}/archive](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-planid-archive-put)[POST/rest/api/3/plans/plan/{planId}/duplicate](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-planid-duplicate-post)[PUT/rest/api/3/plans/plan/{planId}/trash](/cloud/jira/platform/rest/v3/api-group-plans/#api-rest-api-3-plans-plan-planid-trash-put)

---

GET

## Get plans paginatedExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of plans.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**includeTrashed**

boolean

**includeArchived**

boolean

**cursor**

string

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageWithCursorGetPlanResponseForPage

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/plans/plan

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``{ "cursor": "", "isLast": true, "maxResults": 2, "nextPageCursor": "2", "total": 10, "values": [ { "id": "100", "issueSources": [ { "type": "Project", "value": 10000 } ], "name": "Plan 1", "scenarioId": "200", "status": "Active" }, { "id": "200", "issueSources": [ { "type": "Board", "value": 20000 } ], "name": "Plan 2", "scenarioId": "300", "status": "Trashed" } ] }`

---

POST

## Create planExperimental

Creates a plan.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**useGroupId**

boolean

#### Request bodyapplication/json

Expand all

**crossProjectReleases**

array<CreateCrossProjectReleaseRequest>

**customFields**

array<CreateCustomFieldRequest>

**exclusionRules**

CreateExclusionRulesRequest

**issueSources**

array<CreateIssueSourceRequest>

Required

**leadAccountId**

string

**name**

string

Required

**permissions**

array<CreatePermissionRequest>

**scheduling**

CreateSchedulingRequest

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

integer

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/plans/plan

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "crossProjectReleases": [ { "name": "AB and BC merge", "releaseIds": [ 29, 39 ] } ], "customFields": [ { "customFieldId": 2335, "filter": true } ], "exclusionRules": { "issueIds": [ 2, 3 ], "issueTypeIds": [ 32, 33 ], "numberOfDaysToShowCompletedIssues": 50, "releaseIds": [ 42, 43 ], "workStatusCategoryIds": [ 22, 23 ], "workStatusIds": [ 12, 13 ] }, "issueSources": [ { "type": "Project", "value": 12 }, { "type": "Board", "value": 462 } ], "leadAccountId": "abc-12-rbji", "name": "ABC Quaterly plan", "permissions": [ { "holder": { "type": "AccountId", "value": "234-tgj-343" }, "type": "Edit" } ], "scheduling": { "dependencies": "Sequential", "endDate": { "type": "DueDate" }, "estimation": "Days", "inferredDates": "ReleaseDates", "startDate": { "type": "TargetStartDate" } } }`; const response = await requestJira(`/rest/api/3/plans/plan`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get planExperimental

Returns a plan.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**planId**

integer

Required

#### Query parameters

**useGroupId**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

GetPlanResponse

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/plans/plan/{planId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 ``{ "crossProjectReleases": [ { "name": "x-plr", "releaseIds": [ 345 ] } ], "customFields": [ { "customFieldId": 34, "filter": false }, { "customFieldId": 39, "filter": true } ], "exclusionRules": { "issueIds": [ 1, 2 ], "issueTypeIds": [ 13, 23 ], "numberOfDaysToShowCompletedIssues": 50, "releaseIds": [ 14, 24 ], "workStatusCategoryIds": [ 12, 22 ], "workStatusIds": [ 11, 21 ] }, "id": 23, "issueSources": [ { "type": "Project", "value": 12 }, { "type": "Filter", "value": 10293 } ], "lastSaved": "2024-10-03T10:15:30Z", "leadAccountId": "628f5e86d5ec1f006ne7363x2s", "name": "Onset TBJ Plan", "permissions": [ { "holder": { "type": "AccountId", "value": "04jekw86d5jjje006ne7363x2s" }, "type": "Edit" } ], "scheduling": { "dependencies": "Concurrent", "endDate": { "dateCustomFieldId": 1098, "type": "DateCustomField" }, "estimation": "Hours", "inferredDates": "ReleaseDates", "startDate": { "type": "TargetStartDate" } }, "status": "Active" }`

---

PUT

## Update planExperimental

Updates any of the following details of a plan using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

  * name

  * leadAccountId

  * scheduling

    * estimation with StoryPoints, Days or Hours as possible values

    * startDate

      * type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values
      * dateCustomFieldId
    * endDate

      * type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values
      * dateCustomFieldId
    * inferredDates with None, SprintDates or ReleaseDates as possible values

    * dependencies with Sequential or Concurrent as possible values

  * issueSources

    * type with Board, Project or Filter as possible values
    * value
  * exclusionRules

    * numberOfDaysToShowCompletedIssues
    * issueIds
    * workStatusIds
    * workStatusCategoryIds
    * issueTypeIds
    * releaseIds
  * crossProjectReleases

    * name
    * releaseIds
  * customFields

    * customFieldId
    * filter
  * permissions

    * type with View or Edit as possible values

    * holder

      * type with Group or AccountId as possible values
      * value


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

_Note that "add" operations do not respect array indexes in target locations. Call the "Get plan" endpoint to find out the order of array elements._

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**planId**

integer

Required

#### Query parameters

**useGroupId**

boolean

#### Request bodyapplication/json-patch+json

object

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

PUT/rest/api/3/plans/plan/{planId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Archive planExperimental

Archives a plan.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**planId**

integer

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

401Unauthorized

403Forbidden

404Not Found

409Conflict

PUT/rest/api/3/plans/plan/{planId}/archive

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/archive`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Duplicate planExperimental

Duplicates a plan.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**planId**

integer

Required

#### Request bodyapplication/json

**name**

string

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

integer

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

POST/rest/api/3/plans/plan/{planId}/duplicate

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "name": "Copied Plan" }`; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/duplicate`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Trash planExperimental

Moves a plan to trash.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**planId**

integer

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

401Unauthorized

403Forbidden

404Not Found

409Conflict

PUT/rest/api/3/plans/plan/{planId}/trash

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/trash`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`