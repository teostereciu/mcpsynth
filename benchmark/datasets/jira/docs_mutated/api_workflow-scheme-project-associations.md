# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-scheme-project-associations/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow scheme project associations

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the associations between workflow schemes and projects.

For more information, see [Managing your workflows](https://confluence.atlassian.com/x/q4hKLg).

Operations

[GET/rest/api/3/workflowscheme/project](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-project-associations/#api-rest-api-3-workflowscheme-project-get)[PUT/rest/api/3/workflowscheme/project](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-project-associations/#api-rest-api-3-workflowscheme-project-put)

---

GET

## Get workflow scheme project associations

Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned.

If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because the way the `Default Workflow Scheme` is stored means it has no ID.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

**projectId**

array<integer>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ContainerOfWorkflowSchemeAssociations

A container for a list of workflow schemes together with the projects they are associated with.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/workflowscheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/project?projectId={projectId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``{ "values": [ { "projectIds": [ "10010", "10020" ], "workflowScheme": { "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" } } ] }`

---

PUT

## Assign workflow scheme to project

Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project.

Workflow schemes can only be assigned to classic projects.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**projectId**

string

Required

**workflowSchemeId**

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

PUT/rest/api/3/workflowscheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "projectId": "10001", "workflowSchemeId": "10032" }`; const response = await requestJira(`/rest/api/3/workflowscheme/project`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`