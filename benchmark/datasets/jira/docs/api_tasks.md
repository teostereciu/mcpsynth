# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Tasks

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents a [long-running asynchronous tasks](/cloud/jira/platform/rest/v3/intro/#async-operations). Use it to obtain details about the progress of a long-running task or cancel a long-running task.

Operations

[GET/rest/api/3/task/{taskId}](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get)[POST/rest/api/3/task/{taskId}/cancel](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-cancel-post)

---

GET

## Get task

Returns the status of a [long-running asynchronous task](/cloud/jira/platform/rest/v3/intro/#async).

When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

  * `read:jira-work`


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** either of:

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * Creator of the task.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

**taskId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

TaskProgressBeanObject

Details about a task.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/task/{taskId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/task/{taskId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "self": "https://your-domain.atlassian.net/rest/api/3/task/1", "id": "1", "description": "Task description", "status": "COMPLETE", "result": "the task result, this may be any JSON", "submittedBy": 10000, "progress": 100, "elapsedRuntime": 156, "submitted": 1501708132800, "started": 1501708132900, "finished": 1501708133000, "lastUpdate": 1501708133000 }`

---

POST

## Cancel taskExperimental

Cancels a task.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** either of:

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * Creator of the task.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:async-task:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

**taskId**

string

Required

### Responses

202Accepted

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/task/{taskId}/cancel

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/task/{taskId}/cancel`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`