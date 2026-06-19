# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow status categories

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents status categories. Use it to obtain a list of all status categories and the details of a category. Status categories provided a mechanism for categorizing [statuses](/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-group-workflow-statuses).

Operations

[GET/rest/api/3/statuscategory](/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/#api-rest-api-3-statuscategory-get)[GET/rest/api/3/statuscategory/{idOrKey}](/cloud/jira/platform/rest/v3/api-group-workflow-status-categories/#api-rest-api-3-statuscategory-idorkey-get)

---

GET

## Get all status categories

Returns a list of all status categories.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:status:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<StatusCategory>

Show child properties

401Unauthorized

GET/rest/api/3/statuscategory

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuscategory`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``[ { "colorName": "yellow", "id": 1, "key": "in-flight", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1" }, { "colorName": "green", "id": 9, "key": "completed", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/9" } ]`

---

GET

## Get status category

Returns a status category. Status categories provided a mechanism for categorizing [statuses](/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-idorname-get).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:status:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**idOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

StatusCategory

A status category.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/statuscategory/{idOrKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/statuscategory/{idOrKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "colorName": "yellow", "id": 1, "key": "in-flight", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1" }`