# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-classification-levels/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Classification levels

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents classification levels.

Operations

[GET/rest/api/3/classification-levels](/cloud/jira/platform/rest/v3/api-group-classification-levels/#api-rest-api-3-classification-levels-get)

---

GET

## Get all classification levelsExperimental

Returns all classification levels.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**status**

array<string>

**orderBy**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

DataClassificationLevelsBean

The data classification.

Show child properties

401Unauthorized

GET/rest/api/3/classification-levels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/classification-levels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "classifications": [ { "id": "ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38", "status": "published", "name": "Restricted", "rank": 1, "description": "Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk to Atlassian and/or customers if mishandled", "guideline": "Access to data must be restricted to only individuals who need access in order to perform their job duties.", "color": "RED" }, { "id": "ari:cloud:platform::classification-tag/bd58e74c-c31b-41a7-ba69-9673ebd9dae9", "status": "archived", "name": "Protected", "rank": 2, "description": "Data we hold that could cause loss of trust with customers or present legal risk to Atlassian if mishandled", "guideline": "Access to systems or APIs mapping data to other identifiers must be carefully controlled.", "color": "ORANGE" }, { "id": "ari:cloud:platform::classification-tag/a82d653e-1035-4aa2-b9de-4265511fd487", "status": "published", "name": "Confidential", "rank": 3, "description": "Data we hold that would likely be damaging and could cause loss of trust with our customers if mishandled", "guideline": "Data should be encrypted at rest and in transit.", "color": "BLUE" }, { "id": "ari:cloud:platform::classification-tag/a82d653e-1035-4aa2-b9de-4265511fd487", "status": "published", "name": "system-tag" } ] }`