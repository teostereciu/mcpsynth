# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents workflow schemes. Use it to manage workflow schemes and the workflow scheme's workflows and issue types.

A workflow scheme maps issue types to workflows. A workflow scheme can be associated with one or more projects, which enables the projects to use the workflow-issue type mappings.

Active workflow schemes (workflow schemes that are used by projects) cannot be edited. When an active workflow scheme is edited, a draft copy of the scheme is created. The draft workflow scheme is then be edited and published (replacing the active scheme).

See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.

Operations

[GET/rest/api/3/workflowscheme](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-get)[POST/rest/api/3/workflowscheme](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-post)[POST/rest/api/3/workflowscheme/project/switch](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-project-switch-post)[POST/rest/api/3/workflowscheme/read](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-read-post)[POST/rest/api/3/workflowscheme/update](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-update-post)[POST/rest/api/3/workflowscheme/update/mappings](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-update-mappings-post)[GET/rest/api/3/workflowscheme/{id}](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-get)[PUT/rest/api/3/workflowscheme/{id}](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-put)[DEL/rest/api/3/workflowscheme/{id}](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-delete)[GET/rest/api/3/workflowscheme/{id}/default](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-default-get)[PUT/rest/api/3/workflowscheme/{id}/default](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-default-put)[DEL/rest/api/3/workflowscheme/{id}/default](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-default-delete)[GET/rest/api/3/workflowscheme/{id}/issuetype/{issueType}](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-issuetype-issuetype-get)[PUT/rest/api/3/workflowscheme/{id}/issuetype/{issueType}](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-issuetype-issuetype-put)[DEL/rest/api/3/workflowscheme/{id}/issuetype/{issueType}](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-issuetype-issuetype-delete)[GET/rest/api/3/workflowscheme/{id}/workflow](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-workflow-get)[PUT/rest/api/3/workflowscheme/{id}/workflow](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-workflow-put)[DEL/rest/api/3/workflowscheme/{id}/workflow](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-id-workflow-delete)[GET/rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-workflowschemeid-projectusages-get)

---

GET

## Get all workflow schemes

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of all workflow schemes, not including draft workflow schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanWorkflowScheme

A page of items.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/workflowscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``{ "isLast": true, "maxResults": 50, "startAt": 0, "total": 2, "values": [ { "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }, { "defaultWorkflow": "jira", "description": "The description of the another example workflow scheme.", "id": 101011, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Another example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101011" } ] }`

---

POST

## Create workflow scheme

Creates a workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**defaultWorkflow**

string

**description**

string

**issueTypeMappings**

object

**name**

string

**updateDraftIfNeeded**

boolean

### Responses

201Created

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/workflowscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme" }`; const response = await requestJira(`/rest/api/3/workflowscheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

POST

## Switch workflow scheme for projectExperimental

Switches a workflow scheme for a project.

Workflow schemes can only be assigned to classic projects.

**Calculating required mappings:** If statuses from the current workflow scheme won't exist in the target workflow scheme, you must provide `mappingsByIssueTypeOverride` to specify how issues with those statuses should be migrated. Use [the required workflow scheme mappings API](/cloud/jira/platform/rest/v3/api-group-workflow-schemes/#api-rest-api-3-workflowscheme-update-mappings-post) to determine which statuses and issue types require mappings.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

The request containing project ID, target scheme ID, and any issue type mappings.

**mappingsByIssueTypeOverride**

array<MappingsByIssueTypeOverride>

**projectId**

string

**targetSchemeId**

string

**Additional Properties**

any

### Responses

303See Other

Returned if the request is successful and the task has been started.

#### application/json

TaskProgressBeanObject

Details about a task.

Show child properties

400Bad Request

401Unauthorized

409Conflict

POST/rest/api/3/workflowscheme/project/switch

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "mappingsByIssueTypeOverride": [ { "issueTypeId": "10000", "statusMappings": [ { "newStatusId": "10003", "oldStatusId": "3" }, { "newStatusId": "10009", "oldStatusId": "10" } ] }, { "issueTypeId": "10011", "statusMappings": [ { "newStatusId": "10003", "oldStatusId": "3" }, { "newStatusId": "10002", "oldStatusId": "10003" } ] } ], "projectId": "10001", "targetSchemeId": "10002" }`; const response = await requestJira(`/rest/api/3/workflowscheme/project/switch`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`

---

POST

## Bulk get workflow schemes

Returns a list of workflow schemes by providing workflow scheme IDs or project IDs.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ global permission to access all, including project-scoped, workflow schemes
  * _Administer projects_ project permissions to access project-scoped workflow schemes


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**projectIds**

array<string>

**workflowSchemeIds**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

array<WorkflowSchemeReadResponse>

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/workflowscheme/read

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "projectIds": [ "10047", "10048" ], "workflowSchemeIds": [ "3e59db0f-ed6c-47ce-8d50-80c0c4572677" ] }`; const response = await requestJira(`/rest/api/3/workflowscheme/read`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``[ { "defaultWorkflow": { "description": "This is the default workflow for Software Development projects.", "id": "3e59db0f-ed6c-47ce-8d50-80c0c4572677", "name": "Default Software Development Workflow", "version": { "id": "657812fc-bc72-400f-aae0-df8d88db3d9g", "versionNumber": 1 } }, "description": "This is the workflow scheme for the Software Development project type.", "id": "3g78dg2a-ns2n-56ab-9812-42h5j1464567", "name": "Software Developer Workflow Scheme", "scope": { "project": { "id": "10047" }, "type": "GLOBAL" }, "taskId": "3f83dg2a-ns2n-56ab-9812-42h5j1461629", "version": { "id": "527213fc-bc72-400f-aae0-df8d88db2c8a", "versionNumber": 1 }, "workflowsForIssueTypes": [ { "issueTypeIds": [ "10013" ], "workflow": { "description": "This is the workflow for the Software Development bug issue type.", "id": "5e79ae0f-ed6c-47ce-8d50-80c0c4572745", "name": "Software Development Bug Workflow", "version": { "id": "897812dc-bc72-400f-aae0-df8d88fe3d8f", "versionNumber": 1 } } } ] } ]`

---

POST

## Update workflow scheme

Updates company-managed and team-managed project workflow schemes. This API doesn't have a concept of draft, so any changes made to a workflow scheme are immediately available. When changing the available statuses for issue types, an [asynchronous task](/cloud/jira/platform/rest/v3/intro/#async) migrates the issues as defined in the provided mappings.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ project permission to update all, including global-scoped, workflow schemes.
  * _Administer projects_ project permission to update project-scoped workflow schemes.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**defaultWorkflowId**

string

**description**

string

Required

**id**

string

Required

**name**

string

Required

**statusMappingsByIssueTypeOverride**

array<MappingsByIssueTypeOverride>

**statusMappingsByWorkflows**

array<MappingsByWorkflow>

**version**

DocumentVersion

Required

**workflowsForIssueTypes**

array<WorkflowSchemeAssociation>

**Additional Properties**

any

### Responses

200OK

Returned if the request is successful and there is no asynchronous task.

#### application/json

any

303See Other

400Bad Request

401Unauthorized

409Conflict

POST/rest/api/3/workflowscheme/update

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultWorkflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677", "description": "description", "id": "10000", "name": "name", "statusMappingsByIssueTypeOverride": [ { "issueTypeId": "10001", "statusMappings": [ { "newStatusId": "2", "oldStatusId": "1" }, { "newStatusId": "4", "oldStatusId": "3" } ] }, { "issueTypeId": "10002", "statusMappings": [ { "newStatusId": "4", "oldStatusId": "1" }, { "newStatusId": "2", "oldStatusId": "3" } ] } ], "statusMappingsByWorkflows": [ { "newWorkflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677", "oldWorkflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677", "statusMappings": [ { "newStatusId": "2", "oldStatusId": "1" }, { "newStatusId": "4", "oldStatusId": "3" } ] } ], "version": { "id": "527213fc-bc72-400f-aae0-df8d88db2c8a", "versionNumber": 1 }, "workflowsForIssueTypes": [ { "issueTypeIds": [ "10000", "10003" ], "workflowId": "3e59db0f-ed6c-47ce-8d50-80c0c4572677" }, { "issueTypeIds": [ "10001`", "10002" ], "workflowId": "3f83dg2a-ns2n-56ab-9812-42h5j1461629" } ] }`; const response = await requestJira(`/rest/api/3/workflowscheme/update`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Get required status mappings for workflow scheme update

Gets the required status mappings for the desired changes to a workflow scheme. The results are provided per issue type and workflow. When updating a workflow scheme, status mappings can be provided per issue type, per workflow, or both.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ permission to update all, including global-scoped, workflow schemes.
  * _Administer projects_ project permission to update project-scoped workflow schemes.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**defaultWorkflowId**

string

**id**

string

Required

**workflowsForIssueTypes**

array<WorkflowSchemeAssociation>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowSchemeUpdateRequiredMappingsResponse

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/workflowscheme/update/mappings

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultWorkflowId": "10010", "id": "10001", "workflowsForIssueTypes": [ { "issueTypeIds": [ "10010", "10011" ], "workflowId": "10001" } ] }`; const response = await requestJira(`/rest/api/3/workflowscheme/update/mappings`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``{ "statusMappingsByIssueTypes": [ { "issueTypeId": "10000", "statusIds": [ "10000", "10001" ] } ], "statusMappingsByWorkflows": [ { "sourceWorkflowId": "10000", "statusIds": [ "10000", "10001" ], "targetWorkflowId": "10001" } ], "statuses": [ { "category": "TODO", "id": "10000", "name": "To Do" } ], "statusesPerWorkflow": [ { "initialStatusId": "10000", "statuses": [ "10000", "10001" ], "workflowId": "10000" } ] }`

---

GET

## Get workflow scheme

Returns a workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**returnDraftIfExists**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

PUT

## Classic update workflow scheme

Updates a company-manged project workflow scheme, including the name, default workflow, issue type to project mappings, and more. If the workflow scheme is active (that is, being used by at least one project), then a draft workflow scheme is created or updated instead, provided that `updateDraftIfNeeded` is set to `true`.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `write:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

**defaultWorkflow**

string

**description**

string

**issueTypeMappings**

object

**name**

string

**updateDraftIfNeeded**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "issueTypeMappings": { "10000": "scrum workflow" }, "name": "Example workflow scheme", "updateDraftIfNeeded": false }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

DEL

## Delete workflow scheme

Deletes a workflow scheme. Note that a workflow scheme cannot be deleted if it is active (that is, being used by at least one project).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

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

DEL/rest/api/3/workflowscheme/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get default workflow

Returns the default workflow for a workflow scheme. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has _All Unassigned Issue Types_ listed in its issue types for the workflow scheme in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**returnDraftIfExists**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

DefaultWorkflow

Details about the default workflow.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/default`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "workflow": "jira" }`

---

PUT

## Update default workflow

Sets the default workflow for a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request object and a draft workflow scheme is created or updated with the new default workflow. The draft workflow scheme can be published in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `write:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

The new default workflow.

**updateDraftIfNeeded**

boolean

**workflow**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "updateDraftIfNeeded": false, "workflow": "jira" }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

DEL

## Delete default workflow

Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's system workflow (the _jira_ workflow).

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default workflow reset. The draft workflow scheme can be published in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `write:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**updateDraftIfNeeded**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/default`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

GET

## Get workflow for issue type in workflow scheme

Returns the issue type-workflow mapping for an issue type in a workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`, `read:issue-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**issueType**

string

Required

#### Query parameters

**returnDraftIfExists**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueTypeWorkflowMapping

Details about the mapping between an issue type and a workflow.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/issuetype/{issueType}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/issuetype/{issueType}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "issueType": "10000", "workflow": "jira" }`

---

PUT

## Set workflow for issue type in workflow scheme

Sets the workflow for an issue type in a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new issue type-workflow mapping. The draft workflow scheme can be published in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `read:workflow-scheme:jira`, `read:workflow:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**issueType**

string

Required

#### Request bodyapplication/json

Expand all

The issue type-project mapping.

**issueType**

string

**updateDraftIfNeeded**

boolean

**workflow**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/issuetype/{issueType}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueType": "10000", "updateDraftIfNeeded": false, "workflow": "jira" }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/issuetype/{issueType}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

DEL

## Delete workflow for issue type in workflow scheme

Deletes the issue type-workflow mapping for an issue type in a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the issue type-workflow mapping deleted. The draft workflow scheme can be published in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**issueType**

string

Required

#### Query parameters

**updateDraftIfNeeded**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/issuetype/{issueType}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/issuetype/{issueType}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

GET

## Get issue types for workflows in workflow scheme

Returns the workflow-issue type mappings for a workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`, `read:issue-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**workflowName**

string

**returnDraftIfExists**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueTypesWorkflowMapping

Details about the mapping between issue types and a workflow.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/workflow

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/workflow`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "defaultMapping": false, "issueTypes": [ "10000", "10001" ], "workflow": "jira" }`

---

PUT

## Set issue types for workflow in workflow scheme

Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new workflow-issue types mappings. The draft workflow scheme can be published in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `read:workflow-scheme:jira`, `read:workflow:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**workflowName**

string

Required

#### Request bodyapplication/json

Expand all

**defaultMapping**

boolean

**issueTypes**

array<string>

**updateDraftIfNeeded**

boolean

**workflow**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/workflow

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypes": [ "10000" ], "updateDraftIfNeeded": true, "workflow": "jira" }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/workflow?workflowName={workflowName}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

DEL

## Delete issue types for workflow in workflow scheme

Deletes the workflow-issue type mapping for a workflow in a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the workflow-issue type mapping deleted. The draft workflow scheme can be published in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**workflowName**

string

Required

**updateDraftIfNeeded**

boolean

### Responses

200OK

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/workflow

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/workflow?workflowName={workflowName}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get projects which are using a given workflow scheme

Returns a page of projects using a given workflow scheme.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:project:jira`, `read:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**workflowSchemeId**

string

Required

#### Query parameters

Expand all

**nextPageToken**

string

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowSchemeProjectUsageDTO

Projects using the workflow scheme.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "projects": { "nextPageToken": "eyJvIjoyfQ==", "values": [ { "id": "1003" } ] }, "workflowSchemeId": "10005" }`