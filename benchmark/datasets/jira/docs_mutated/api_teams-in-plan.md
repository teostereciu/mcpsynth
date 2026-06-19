# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-teams-in-plan/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Teams in plan

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents planning settings for plan-only and Atlassian teams in a plan. Use it to get, create, update and delete planning settings.

Operations

[GET/rest/api/3/plans/plan/{planId}/team](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-get)[POST/rest/api/3/plans/plan/{planId}/team/atlassian](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-atlassian-post)[GET/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-atlassian-atlassianteamid-get)[PUT/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-atlassian-atlassianteamid-put)[DEL/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-atlassian-atlassianteamid-delete)[POST/rest/api/3/plans/plan/{planId}/team/planonly](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-planonly-post)[GET/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-planonly-planonlyteamid-get)[PUT/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-planonly-planonlyteamid-put)[DEL/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}](/cloud/jira/platform/rest/v3/api-group-teams-in-plan/#api-rest-api-3-plans-plan-planid-team-planonly-planonlyteamid-delete)

---

GET

## Get teams in plan paginatedExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of plan-only and Atlassian teams in a plan.

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

Expand all

**cursor**

string

**page_size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageWithCursorGetTeamResponseForPage

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/plans/plan/{planId}/team

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``{ "cursor": "", "isLast": true, "page_size": 2, "nextPageCursor": "2", "total": 10, "values": [ { "id": "1", "name": "Team 1", "type": "PlanOnly" }, { "id": "2", "type": "Atlassian" } ] }`

---

POST

## Add Atlassian team to planExperimental

Adds an existing Atlassian team to a plan and configures their plannning settings.

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

Expand all

**capacity**

number

**id**

string

Required

**issueSourceId**

integer

**planningStyle**

string

Required

**sprintLength**

integer

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

POST/rest/api/3/plans/plan/{planId}/team/atlassian

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "capacity": 200, "id": "AtlassianTeamId", "issueSourceId": 0, "planningStyle": "Scrum", "sprintLength": 2 }`; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/atlassian`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get Atlassian team in planExperimental

Returns planning settings for an Atlassian team in a plan.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**planId**

integer

Required

**atlassianTeamId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

GetAtlassianTeamResponse

Show child properties

401Unauthorized

403Forbidden

404Not Found

409Conflict

GET/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "capacity": 220, "id": "98WA-2JBO-12N3-2298", "issueSourceId": 1, "planningStyle": "Scrum", "sprintLength": 2 }`

---

PUT

## Update Atlassian team in planExperimental

Updates any of the following planning settings of an Atlassian team in a plan using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

  * planningStyle
  * issueSourceId
  * sprintLength
  * capacity


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

_Note that "add" operations do not respect array indexes in target locations. Call the "Get Atlassian team in plan" endpoint to find out the order of array elements._

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**planId**

integer

Required

**atlassianTeamId**

string

Required

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

PUT/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove Atlassian team from planExperimental

Removes an Atlassian team from a plan and deletes their planning settings.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**planId**

integer

Required

**atlassianTeamId**

string

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

DEL/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Create plan-only teamExperimental

Creates a plan-only team and configures their planning settings.

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

Expand all

**capacity**

number

**issueSourceId**

integer

**memberAccountIds**

array<string>

**name**

string

Required

**planningStyle**

string

Required

**sprintLength**

integer

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

POST/rest/api/3/plans/plan/{planId}/team/planonly

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "capacity": 200, "issueSourceId": 0, "memberAccountIds": [ "member1AccountId", "member2AccountId" ], "name": "Team1", "planningStyle": "Scrum", "sprintLength": 2 }`; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/planonly`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get plan-only teamExperimental

Returns planning settings for a plan-only team.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**planId**

integer

Required

**planOnlyTeamId**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

GetPlanOnlyTeamResponse

Show child properties

401Unauthorized

403Forbidden

404Not Found

409Conflict

GET/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "capacity": 30, "id": 123, "issueSourceId": 1, "memberAccountIds": [ "mek2-3jno-01n3", "kdsn-2nk3-2nn1" ], "name": "Team1", "planningStyle": "Scrum", "sprintLength": 2 }`

---

PUT

## Update plan-only teamExperimental

Updates any of the following planning settings of a plan-only team using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

  * name
  * planningStyle
  * issueSourceId
  * sprintLength
  * capacity
  * memberAccountIds


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

_Note that "add" operations do not respect array indexes in target locations. Call the "Get plan-only team" endpoint to find out the order of array elements._

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**planId**

integer

Required

**planOnlyTeamId**

integer

Required

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

PUT/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete plan-only teamExperimental

Deletes a plan-only team and their planning settings.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**planId**

integer

Required

**planOnlyTeamId**

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

DEL/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`