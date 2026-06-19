# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-panels/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue panels

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource supports bulk pinning and unpinning of [issue panels](https://developer.atlassian.com/platform/forge/) that are added by a Forge app. Only Jira administrators can use it.

Operations

[POST/rest/api/3/forge/panel/action/bulk/async](/cloud/jira/platform/rest/v3/api-group-issue-panels/#api-rest-api-3-forge-panel-action-bulk-async-post)

---

POST

## Bulk pin or unpin issue panel to projects

Bulk pin or unpin an issue panel (added by a Forge app) to or from multiple projects.

The operation runs asynchronously. The response includes a task ID - use the [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) endpoint to check progress.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-project`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

Forge module ID and the list of projects with pin or unpin action.

**moduleId**

string

Required

**projectList**

array<ProjectPinAction>

Required

### Responses

202Accepted

Accepted. Returns the task ID for polling progress.

#### application/json

ForgePanelProjectPinAsyncResponse

Show child properties

400Bad Request

403Forbidden

500Internal Server Error

POST/rest/api/3/forge/panel/action/bulk/async

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "moduleId": "<string>", "projectList": [ { "action": "PIN", "projectIdOrKey": "<string>" } ] }`; const response = await requestJira(`/rest/api/3/forge/panel/action/bulk/async`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

202Response

`1 2 3 ``{ "taskId": "<string>" }`