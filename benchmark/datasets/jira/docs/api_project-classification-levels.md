# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-classification-levels/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project classification levels

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents classification levels used in a project. Use it to view and manage classification levels in your projects.

Operations

[GET/rest/api/3/project/{projectIdOrKey}/classification-config](/cloud/jira/platform/rest/v3/api-group-project-classification-levels/#api-rest-api-3-project-projectidorkey-classification-config-get)[GET/rest/api/3/project/{projectIdOrKey}/classification-level/default](/cloud/jira/platform/rest/v3/api-group-project-classification-levels/#api-rest-api-3-project-projectidorkey-classification-level-default-get)[PUT/rest/api/3/project/{projectIdOrKey}/classification-level/default](/cloud/jira/platform/rest/v3/api-group-project-classification-levels/#api-rest-api-3-project-projectidorkey-classification-level-default-put)[DEL/rest/api/3/project/{projectIdOrKey}/classification-level/default](/cloud/jira/platform/rest/v3/api-group-project-classification-levels/#api-rest-api-3-project-projectidorkey-classification-level-default-delete)

---

GET

## Get the classification configuration for a projectExperimental

Returns the consolidated classification configuration for a project's admin settings page.

This includes permitted classification levels (with status), the project's default classification level, the organization's default classification level, and the container override setting.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

any

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/classification-config

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/classification-config`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "classificationLevels": [ { "id": "ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38", "status": "published", "name": "Restricted", "rank": 1, "description": "Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk if mishandled", "guideline": "Access to data must be restricted to only individuals who need access in order to perform their job duties.", "color": "RED" } ], "containerOverride": "ANY", "defaultClassificationLevel": { "id": "ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38", "status": "published", "name": "Restricted", "rank": 1, "description": "Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk if mishandled", "guideline": "Access to data must be restricted to only individuals who need access in order to perform their job duties.", "color": "RED" }, "organizationClassificationLevel": { "id": "ari:cloud:platform::classification-tag/a82d653e-1035-4aa2-b9de-4265511fd487", "status": "published", "name": "Confidential", "rank": 2, "description": "Data we hold that would likely be damaging and could cause loss of trust with our customers if mishandled", "guideline": "Data should be encrypted at rest and in transit.", "color": "BLUE" } }`

---

GET

## Get the default data classification level of a projectExperimental

Returns the default data classification for a project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

any

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/classification-level/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/classification-level/default`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "classification": { "id": "ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38", "status": "published", "name": "Restricted", "rank": 1, "description": "Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk if mishandled", "guideline": "Access to data must be restricted to only individuals who need access in order to perform their job duties.", "guidelineADF": "{\"version\":1,\"type\":\"doc\",\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"Access to data must be restricted to only individuals who need access in order to perform their job duties.\"}]}]}", "color": "RED" } }`

---

PUT

## Update the default data classification level of a projectExperimental

Updates the default data classification level for a project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

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

404Not Found

PUT/rest/api/3/project/{projectIdOrKey}/classification-level/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "id": "ari:cloud:platform::classification-tag/dec24c48-5073-4c25-8fef-9d81a992c30c" }`; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/classification-level/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove the default data classification level from a projectExperimental

Remove the default data classification level for a project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/project/{projectIdOrKey}/classification-level/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/classification-level/default`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`