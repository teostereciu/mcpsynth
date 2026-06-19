# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-templates/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project templates

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents project templates. Use it to create a new project from a custom template.

Operations

[POST/rest/api/3/project-template](/cloud/jira/platform/rest/v3/api-group-project-templates/#api-rest-api-3-project-template-post)[PUT/rest/api/3/project-template/edit-template](/cloud/jira/platform/rest/v3/api-group-project-templates/#api-rest-api-3-project-template-edit-template-put)[GET/rest/api/3/project-template/live-template](/cloud/jira/platform/rest/v3/api-group-project-templates/#api-rest-api-3-project-template-live-template-get)[DEL/rest/api/3/project-template/remove-template](/cloud/jira/platform/rest/v3/api-group-project-templates/#api-rest-api-3-project-template-remove-template-delete)[POST/rest/api/3/project-template/save-template](/cloud/jira/platform/rest/v3/api-group-project-templates/#api-rest-api-3-project-template-save-template-post)

---

POST

## Create custom project

Creates a project based on a custom template provided in the request.

The request body should contain the project details and the capabilities that comprise the project:

  * `details` \- represents the project details settings
  * `template` \- represents a list of capabilities responsible for creating specific parts of a project


A capability is defined as a unit of configuration for the project you want to create.

This operation is:

  * [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `Location` link in the response header to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.


_**Note: This API is only supported for Jira Enterprise edition.**_

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `read:project:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The JSON payload containing the project details and capabilities

**details**

CustomTemplatesProjectDetails

**template**

CustomTemplateRequestDTO

### Responses

303See Other

The project creation task has been queued for execution

#### application/json

any

POST/rest/api/3/project-template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "details": { "accessLevel": "private", "additionalProperties": {}, "assigneeType": "PROJECT_LEAD", "avatarId": 10200, "categoryId": 219, "description": "This is a project for Foo Bar", "enableComponents": false, "key": "PRJ", "language": "en", "leadAccountId": "1234567890", "name": "Project Foo Bar", "url": "https://www.example.com" }, "template": { "boards": { "boards": [ {} ] }, "field": { "customFieldDefinitions": [ {} ], "fieldLayoutScheme": {}, "fieldLayouts": [ {} ], "fieldScheme": {}, "issueLayouts": [ {} ], "issueTypeScreenScheme": {}, "screenScheme": [ {} ], "screens": [ {} ] }, "issueType": { "issueTypeHierarchy": [ {} ], "issueTypeScheme": {}, "issueTypes": [ {} ] }, "notification": { "description": "<string>", "name": "<string>", "notificationSchemeEvents": [ {} ], "onConflict": "FAIL", "pcri": {} }, "permissionScheme": { "addAddonRole": true, "description": "<string>", "grants": [ {} ], "name": "<string>", "onConflict": "FAIL", "pcri": {} }, "project": { "fieldLayoutSchemeId": {}, "issueSecuritySchemeId": {}, "issueTypeSchemeId": {}, "issueTypeScreenSchemeId": {}, "notificationSchemeId": {}, "pcri": {}, "permissionSchemeId": {}, "projectTypeKey": "software", "workflowSchemeId": {} }, "role": { "roleToProjectActors": {}, "roles": [ {} ] }, "scope": { "type": "GLOBAL" }, "security": { "description": "Newly created issue security scheme", "name": "New Security Scheme", "pcri": {}, "securityLevels": [ {} ] }, "workflow": { "statuses": [ {} ], "workflowScheme": {}, "workflows": [ {} ] } } }`; const response = await requestJira(`/rest/api/3/project-template`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

PUT

## Edit a custom project templateExperimental

Edit custom template

This API endpoint allows you to edit an existing customised template.

_**Note: Custom Templates are only supported for Jira Enterprise edition.**_

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `read:project:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The object containing the updated template details: name, description

**templateDescription**

string

**templateGenerationOptions**

CustomTemplateOptions

**templateKey**

string

**templateName**

string

### Responses

200OK

200 response

#### application/json

any

PUT/rest/api/3/project-template/edit-template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "templateDescription": "<string>", "templateGenerationOptions": { "enableScreenDelegatedAdminSupport": true, "enableWorkflowDelegatedAdminSupport": true }, "templateKey": "<string>", "templateName": "<string>" }`; const response = await requestJira(`/rest/api/3/project-template/edit-template`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Gets a custom project templateExperimental

Get custom template

This API endpoint allows you to get a live custom project template details by either templateKey or projectId

_**Note: Custom Templates are only supported for Jira Enterprise edition.**_

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `read:project:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**projectId**

string

**templateKey**

string

### Responses

200OK

200 response

#### application/json

ProjectTemplateModel

Show child properties

GET/rest/api/3/project-template/live-template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project-template/live-template`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``{ "archetype": { "realType": "BUSINESS", "style": "classic", "type": "BUSINESS" }, "defaultBoardView": "<string>", "description": "<string>", "liveTemplateProjectIdReference": 2154, "name": "<string>", "projectTemplateKey": { "key": "<string>", "uuid": "<string>" }, "snapshotTemplate": {}, "templateGenerationOptions": { "enableScreenDelegatedAdminSupport": true, "enableWorkflowDelegatedAdminSupport": true }, "type": "LIVE" }`

---

DEL

## Deletes a custom project templateExperimental

Remove custom template

This API endpoint allows you to remove a specified customised template

_**Note: Custom Templates are only supported for Jira Enterprise edition.**_

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `read:project:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**templateKey**

string

Required

### Responses

200OK

200 response

#### application/json

any

DEL/rest/api/3/project-template/remove-template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project-template/remove-template?templateKey={templateKey}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Save a custom project templateExperimental

Save custom template

This API endpoint allows you to save a customised template

_**Note: Custom Templates are only supported for Jira Enterprise edition.**_

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `read:project:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The object containing the template basic details: name, description

**templateDescription**

string

**templateFromProjectRequest**

SaveProjectTemplateRequest

**templateName**

string

### Responses

200OK

200 response

#### application/json

SaveTemplateResponse

Show child properties

POST/rest/api/3/project-template/save-template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "templateDescription": "<string>", "templateFromProjectRequest": { "projectId": 28, "templateGenerationOptions": { "enableScreenDelegatedAdminSupport": true, "enableWorkflowDelegatedAdminSupport": true }, "templateType": "LIVE" }, "templateName": "<string>" }`; const response = await requestJira(`/rest/api/3/project-template/save-template`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "projectTemplateKey": { "key": "<string>", "uuid": "<string>" } }`