# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-data-policies/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# App data policies

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents app access rule data policies.

Operations

[GET/rest/api/3/data-policy](/cloud/jira/platform/rest/v3/api-group-app-data-policies/#api-rest-api-3-data-policy-get)[GET/rest/api/3/data-policy/project](/cloud/jira/platform/rest/v3/api-group-app-data-policies/#api-rest-api-3-data-policy-project-get)

---

GET

## Get data policy for the workspace

Returns data policy for the workspace.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful

#### application/json

WorkspaceDataPolicy

Details about data policy.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/data-policy

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/data-policy`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "anyContentBlocked": false }`

---

GET

## Get data policy for projects

Returns data policies for the projects specified in the request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**ids**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectDataPolicies

Details about data policies for a list of projects.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/data-policy/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/data-policy/project`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "projectDataPolicies": [ { "dataPolicy": { "anyContentBlocked": false }, "id": 1000 }, { "dataPolicy": { "anyContentBlocked": true }, "id": 1001 } ] }`