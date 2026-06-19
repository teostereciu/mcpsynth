# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-statuses/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow statuses

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue workflow statuses. Use it to obtain a list of all statuses associated with workflows and the details of a status.

Operations

[GET/rest/api/3/status](/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-get)[GET/rest/api/3/status/{idOrName}](/cloud/jira/platform/rest/v3/api-group-workflow-statuses/#api-rest-api-3-status-idorname-get)

---

GET

## Get all statuses

Returns a list of all statuses associated with active workflows.

This operation can be accessed anonymously.

[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required: _Browse projects_ [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.

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

array<StatusDetails>

Show child properties

401Unauthorized

GET/rest/api/3/status

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/status`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``[ { "description": "The issue is currently being worked on.", "iconUrl": "https://your-domain.atlassian.net/images/icons/progress.gif", "id": "10000", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/status/10000", "statusCategory": { "colorName": "yellow", "id": 1, "key": "in-flight", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1" } }, { "description": "The issue is closed.", "iconUrl": "https://your-domain.atlassian.net/images/icons/closed.gif", "id": "5", "name": "Closed", "self": "https://your-domain.atlassian.net/rest/api/3/status/5", "statusCategory": { "colorName": "green", "id": 9, "key": "completed", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/9" } } ]`

---

GET

## Get status

Returns a status. The status must be associated with an active workflow to be returned.

If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable.

This operation can be accessed anonymously.

[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required: _Browse projects_ [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:status:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**idOrName**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

StatusDetails

A status.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/status/{idOrName}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/status/{idOrName}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "The issue is currently being worked on.", "iconUrl": "https://your-domain.atlassian.net/images/icons/progress.gif", "id": "10000", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/status/10000", "statusCategory": { "colorName": "yellow", "id": 1, "key": "in-flight", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1" } }`