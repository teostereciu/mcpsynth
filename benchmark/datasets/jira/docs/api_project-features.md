# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-features/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project features

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents project features. Use it to get the list of features for a project and modify the state of a feature. The project feature endpoint is available only for Jira Software, both for team- and company-managed projects.

Operations

[GET/rest/api/3/project/{projectIdOrKey}/features](/cloud/jira/platform/rest/v3/api-group-project-features/#api-rest-api-3-project-projectidorkey-features-get)[PUT/rest/api/3/project/{projectIdOrKey}/features/{featureKey}](/cloud/jira/platform/rest/v3/api-group-project-features/#api-rest-api-3-project-projectidorkey-features-featurekey-put)

---

GET

## Get project features

Returns the list of features for a project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project.feature:jira`

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

ContainerForProjectFeatures

The list of features on a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/features

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/features`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "features": [ { "feature": "jsw.classic.roadmap", "imageUri": "https://jira.atlassian.com/s/sb53l8/b/3/ab8a7691e4738b4f147e293f0864adfd5b8d3c85/_/download/resources/com.atlassian.jira.rest:classic-project-features/simple-roadmap-feature.svg", "localisedDescription": "Your roadmap is an optimized location to create and manage your epics.", "localisedName": "Roadmap", "prerequisites": [], "projectId": 10001, "state": "ENABLED", "toggleLocked": true }, { "feature": "jsw.classic.backlog", "imageUri": "https://jira.atlassian.com/s/sb53l8/b/3/ab8a7691e4738b4f147e293f0864adfd5b8d3c85/_/download/resources/com.atlassian.jira.rest:classic-project-features/simple-backlog-feature.svg", "localisedDescription": "Plan and prioritize work in a dedicated space. To enable and configure the backlog for each board, go to board settings.", "localisedName": "Backlog", "prerequisites": [], "projectId": 10001, "state": "ENABLED", "toggleLocked": true } ] }`

---

PUT

## Set project feature state

Sets the state of a project feature.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project.feature:jira`, `read:project.feature:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**projectIdOrKey**

string

Required

**featureKey**

string

Required

#### Request bodyapplication/json

Details of the feature state change.

**state**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

ContainerForProjectFeatures

The list of features on a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/project/{projectIdOrKey}/features/{featureKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "state": "ENABLED" }`; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/features/{featureKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "features": [ { "feature": "jsw.classic.roadmap", "imageUri": "https://jira.atlassian.com/s/sb53l8/b/3/ab8a7691e4738b4f147e293f0864adfd5b8d3c85/_/download/resources/com.atlassian.jira.rest:classic-project-features/simple-roadmap-feature.svg", "localisedDescription": "Your roadmap is an optimized location to create and manage your epics.", "localisedName": "Roadmap", "prerequisites": [], "projectId": 10001, "state": "ENABLED", "toggleLocked": true }, { "feature": "jsw.classic.backlog", "imageUri": "https://jira.atlassian.com/s/sb53l8/b/3/ab8a7691e4738b4f147e293f0864adfd5b8d3c85/_/download/resources/com.atlassian.jira.rest:classic-project-features/simple-backlog-feature.svg", "localisedDescription": "Plan and prioritize work in a dedicated space. To enable and configure the backlog for each board, go to board settings.", "localisedName": "Backlog", "prerequisites": [], "projectId": 10001, "state": "ENABLED", "toggleLocked": true } ] }`