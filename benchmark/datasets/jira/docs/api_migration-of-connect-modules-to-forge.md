# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-migration-of-connect-modules-to-forge/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Migration of Connect modules to Forge

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource supports the migration of some Connect modules to their equivalent Forge modules.

Operations

[GET/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task](/cloud/jira/platform/rest/v3/api-group-migration-of-connect-modules-to-forge/#api-rest-atlassian-connect-1-migration-connectkey-jiraissuefieldskey-task-get)[POST/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task](/cloud/jira/platform/rest/v3/api-group-migration-of-connect-modules-to-forge/#api-rest-atlassian-connect-1-migration-connectkey-jiraissuefieldskey-task-post)

---

GET

## Get Connect issue field migration task

Returns the details of a Connect issue field's migration to Forge.

When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/). When the Forge version of the app is installed, Forge creates a [background task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-group-tasks) to track the migration of field data across. This endpoint returns the status and other details of that background task.

For more details, see [Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect and Forge apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

Expand all

**connectKey**

string

Required

**jiraIssueFieldsKey**

string

Required

### Responses

200OK

Returned if the request is successful and a migration task is found.

#### application/json

TaskProgress

Details about a task.

Show child properties

401Unauthorized

404Not Found

GET/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": "<string>", "id": "<string>", "lastUpdate": "<string>", "message": "<string>", "progress": 51, "self": "<string>", "started": "<string>", "status": "ENQUEUED", "submitted": "<string>", "submittedBy": 42 }`

---

POST

## Submit Connect issue field migration task

Submits a request to trigger migration of connect issue field to its Forge custom field counterpart.

When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) modules. This endpoint triggers the background migration of field data. Use the GET endpoint to retrieve the status and progress of the task.

For more details, see [Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect and Forge apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:jira-work`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

Expand all

**connectKey**

string

Required

**jiraIssueFieldsKey**

string

Required

### Responses

202Accepted

Returned if the migration task was submitted successfully.

401Unauthorized

404Not Found

409Conflict

POST/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task`, { method: 'POST' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`