# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue bulk operations

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the issue bulk operations. Use it to move multiple issues from one project to another project or edit fields of multiple issues in one go.

For additional clarity, we have created a page with further examples and answers to frequently asked questions related to these APIs. You can access it here: [Bulk operation APIs: additional examples and FAQ](https://developer.atlassian.com/cloud/jira/platform/bulk-operation-additional-examples-and-faqs/).

### Authentication

Access to the issue bulk operations requires authentication. For information on how to authenticate API requests, refer to the [Basic auth for REST APIs documentation](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).

### Rate limiting

The bulk edit and move APIs are subject to the usual rate limiting infrastructure in Jira. For more information, refer to [Rate limiting](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/). Additionally, at any given time, only 5 concurrent requests can be sent across all users.

Operations

[POST/rest/api/3/bulk/issues/delete](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-delete-post)[GET/rest/api/3/bulk/issues/fields](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-fields-get)[POST/rest/api/3/bulk/issues/fields](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-fields-post)[POST/rest/api/3/bulk/issues/move](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-move-post)[GET/rest/api/3/bulk/issues/transition](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-transition-get)[POST/rest/api/3/bulk/issues/transition](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-transition-post)[POST/rest/api/3/bulk/issues/unwatch](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-unwatch-post)[POST/rest/api/3/bulk/issues/watch](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-issues-watch-post)[GET/rest/api/3/bulk/queue/{taskId}](/cloud/jira/platform/rest/v3/api-group-issue-bulk-operations/#api-rest-api-3-bulk-queue-taskid-get)

---

POST

## Bulk delete issues

Use this API to submit a bulk delete request. You can delete up to 1,000 issues in a single operation.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Delete [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Delete-issues/) in all projects that contain the selected issues.
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The request body containing the issues to be deleted.

**selectedIssueIdsOrKeys**

array<string>

Required

**sendBulkNotification**

boolean

### Responses

201Created

Returned if the request is successful.

#### application/json

SubmittedBulkOperation

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/bulk/issues/delete

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "selectedIssueIdsOrKeys": [ "10001", "10002" ], "sendBulkNotification": false }`; const response = await requestJira(`/rest/api/3/bulk/issues/delete`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "taskId": "10641" }`

---

GET

## Get bulk editable fields

Use this API to get a list of fields visible to the user to perform bulk edit operations. You can pass single or multiple issues in the query to get eligible editable fields. This API uses pagination to return responses, delivering 50 fields at a time.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * Depending on the field, any field-specific permissions required to edit it.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**issueIdsOrKeys**

string

Required

**searchText**

string

**endingBefore**

string

**startingAfter**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

BulkEditGetFields

Bulk Edit Get Fields Response.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/bulk/issues/fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/bulk/issues/fields?issueIdsOrKeys={issueIdsOrKeys}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``{ "fields": [ { "id": "assignee", "isRequired": false, "name": "Assignee", "searchUrl": "https://your-domain.atlassian.net/rest/api/3/user/assignable/multiProjectSearch?projectKeys=KAN&query=", "type": "assignee" }, { "id": "components", "isRequired": false, "multiSelectFieldOptions": [ "ADD", "REMOVE", "REPLACE", "REMOVE_ALL" ], "name": "Components", "type": "components", "unavailableMessage": "{0}NOTE{1}: The project of the selected issue(s) does not have any components." }, { "fieldOptions": [ { "description": "This problem will block progress.", "id": "1", "priority": "Highest" }, { "description": "Has the potential to affect progress.", "id": "2", "priority": "Lowest" }, { "description": "Trivial problem with little or no impact on progress.", "id": "3", "priority": "Medium" } ], "id": "priority", "isRequired": false, "name": "Priority", "type": "priority" } ] }`

---

POST

## Bulk edit issues

Use this API to submit a bulk edit request and simultaneously edit multiple issues. There are limits applied to the number of issues and fields that can be edited. A single request can accommodate a maximum of 1000 issues (including subtasks) and 200 fields.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * Edit [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The request body containing the issues to be edited and the new field values.

**editedFieldsInput**

JiraIssueFields

Required

**selectedActions**

array<string>

Required

**selectedIssueIdsOrKeys**

array<string>

Required

**sendBulkNotification**

boolean

### Responses

201Created

Returned if the request is successful.

#### application/json

SubmittedBulkOperation

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/bulk/issues/fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "editedFieldsInput": { "cascadingSelectFields": [ { "childOptionValue": {}, "fieldId": "<string>", "parentOptionValue": {} } ], "clearableNumberFields": [ { "fieldId": "<string>", "value": 2154 } ], "colorFields": [ { "color": { "name": "<string>" }, "fieldId": "<string>" } ], "datePickerFields": [ { "date": { "formattedDate": "<string>" }, "fieldId": "<string>" } ], "dateTimePickerFields": [ { "dateTime": { "formattedDateTime": "<string>" }, "fieldId": "<string>" } ], "issueType": { "issueTypeId": "<string>" }, "labelsFields": [ { "bulkEditMultiSelectFieldOption": "ADD", "fieldId": "<string>", "labelProperties": [ {} ], "labels": [ { "name": "<string>" } ] } ], "multipleGroupPickerFields": [ { "fieldId": "<string>", "groups": [ { "groupName": "<string>" } ] } ], "multipleSelectClearableUserPickerFields": [ { "fieldId": "<string>", "users": [ { "accountId": "<string>" } ] } ], "multipleSelectFields": [ { "fieldId": "<string>", "options": [ {} ] } ], "multipleVersionPickerFields": [ { "bulkEditMultiSelectFieldOption": "ADD", "fieldId": "<string>", "versions": [ {} ] } ], "multiselectComponents": { "bulkEditMultiSelectFieldOption": "ADD", "components": [ { "componentId": 2154 } ], "fieldId": "<string>" }, "originalEstimateField": { "originalEstimateField": "<string>" }, "priority": { "priorityId": "<string>" }, "richTextFields": [ { "fieldId": "<string>", "richText": {} } ], "singleGroupPickerFields": [ { "fieldId": "<string>", "group": { "groupName": "<string>" } } ], "singleLineTextFields": [ { "fieldId": "<string>", "text": "<string>" } ], "singleSelectClearableUserPickerFields": [ { "fieldId": "<string>", "user": { "accountId": "<string>" } } ], "singleSelectFields": [ { "fieldId": "<string>", "option": {} } ], "singleVersionPickerFields": [ { "fieldId": "<string>", "version": {} } ], "status": { "statusId": "<string>" }, "timeTrackingField": { "timeRemaining": "<string>" }, "urlFields": [ { "fieldId": "<string>", "url": "<string>" } ] }, "selectedActions": [ "<string>" ], "selectedIssueIdsOrKeys": [ "<string>" ], "sendBulkNotification": true }`; const response = await requestJira(`/rest/api/3/bulk/issues/fields`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "taskId": "10641" }`

---

POST

## Bulk move issues

Use this API to submit a bulk issue move request. You can move multiple issues from multiple projects in a single request, but they must all be moved to a single project, issue type, and parent. You can't move more than 1000 issues (including subtasks) at once.

#### Scenarios:

This is an early version of the API and it doesn't have full feature parity with the Bulk Move UI experience.

  * Moving issue of type A to issue of type B in the same project or a different project: `SUPPORTED`

  * Moving multiple issues of type A in one or more projects to multiple issues of type B in one of the source projects or a different project: `SUPPORTED`

  * Moving issues of multiple issue types in one or more projects to issues of a single issue type in one of the source project or a different project: **`SUPPORTED`**
E.g. Moving issues of story and task issue types in project 1 and project 2 to issues of task issue type in project 3

  * Moving a standard parent issue of type A with its multiple subtask issue types in one project to standard issue of type B and multiple subtask issue types in the same project or a different project: `SUPPORTED`

  * Moving standard issues with their subtasks to a parent issue in the same project or a different project without losing their relation: `SUPPORTED`

  * Moving an epic issue with its child issues to a different project without losing their relation: `SUPPORTED`
This usecase is **supported using multiple requests**. Move the epic in one request and then move the children in a separate request with target parent set to the epic issue id

(Alternatively, move them individually and stitch the relationship back with the Bulk Edit API)


#### Limits applied to bulk issue moves:

When using the bulk move, keep in mind that there are limits on the number of issues and fields you can include.

  * You can move up to 1,000 issues in a single operation, including any subtasks.
  * The total combined number of fields across all issues must not exceed 1,500,000. For example, if each issue includes 15,000 fields, then the maximum number of issues that can be moved is 100.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Move [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in source projects.
  * Create [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects.
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects, if moving subtasks only.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**sendBulkNotification**

boolean

**targetToSourcesMapping**

object

### Responses

201Created

Returned if the request is successful.

#### application/json

SubmittedBulkOperation

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/bulk/issues/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "sendBulkNotification": true, "targetToSourcesMapping": { "PROJECT-KEY,10001": { "inferClassificationDefaults": false, "inferFieldDefaults": false, "inferStatusDefaults": false, "inferSubtaskTypeDefault": true, "issueIdsOrKeys": [ "ISSUE-1" ], "targetClassification": [ { "classifications": { "5bfa70f7-4af1-44f5-9e12-1ce185f15a38": [ "bd58e74c-c31b-41a7-ba69-9673ebd9dae9", "-1" ] } } ], "targetMandatoryFields": [ { "fields": { "customfield_10000": { "retain": false, "type": "raw", "value": [ "value-1", "value-2" ] }, "description": { "retain": true, "type": "adf", "value": { "content": [ { "content": [ { "text": "New description value", "type": "text" } ], "type": "paragraph" } ], "type": "doc", "version": 1 } }, "fixVersions": { "retain": false, "type": "raw", "value": [ "10009" ] }, "labels": { "retain": false, "type": "raw", "value": [ "label-1", "label-2" ] } } } ], "targetStatus": [ { "statuses": { "10001": [ "10002", "10003" ] } } ] } } }`; const response = await requestJira(`/rest/api/3/bulk/issues/move`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "taskId": "10641" }`

---

GET

## Get available transitions

Use this API to retrieve a list of transitions available for the specified issues that can be used or bulk transition operations. You can submit either single or multiple issues in the query to obtain the available transitions.

The response will provide the available transitions for issues, organized by their respective workflows. **Only the transitions that are common among the issues within that workflow and do not involve any additional field updates will be included.** For bulk transitions that require additional field updates, please utilise the Jira Cloud UI.

You can request available transitions for up to 1,000 issues in a single operation. This API uses pagination to return responses, delivering 50 workflows at a time.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**issueIdsOrKeys**

string

Required

**endingBefore**

string

**startingAfter**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

BulkTransitionGetAvailableTransitions

Bulk Transition Get Available Transitions Response.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/bulk/issues/transition

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/bulk/issues/transition?issueIdsOrKeys={issueIdsOrKeys}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``{ "availableTransitions": [ { "isTransitionsFiltered": false, "issues": [ "EPIC-1", "TASK-1" ], "transitions": [ { "to": { "statusId": 10001, "statusName": "To Do" }, "transitionId": 11, "transitionName": "To Do" }, { "to": { "statusId": 10002, "statusName": "In Progress" }, "transitionId": 21, "transitionName": "In Progress" }, { "to": { "statusId": 10003, "statusName": "Done" }, "transitionId": 31, "transitionName": "Done" } ] }, { "isTransitionsFiltered": true, "issues": [ "BUG-1" ], "transitions": [ { "to": { "statusId": 10004, "statusName": "To Do bug" }, "transitionId": 41, "transitionName": "To Do bug" }, { "to": { "statusId": 10005, "statusName": "Triage" }, "transitionId": 51, "transitionName": "Triage" } ] } ] }`

---

POST

## Bulk transition issue statuses

Use this API to submit a bulk issue status transition request. You can transition multiple issues, alongside with their valid transition Ids. You can transition up to 1,000 issues in a single operation.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The request body containing the issues to be transitioned.

**bulkTransitionInputs**

array<BulkTransitionSubmitInput>

Required

**sendBulkNotification**

boolean

### Responses

201Created

Returned if the request is successful.

#### application/json

SubmittedBulkOperation

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/bulk/issues/transition

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "bulkTransitionInputs": [ { "selectedIssueIdsOrKeys": [ "10001", "10002" ], "transitionId": "11" }, { "selectedIssueIdsOrKeys": [ "TEST-1" ], "transitionId": "2" } ], "sendBulkNotification": false }`; const response = await requestJira(`/rest/api/3/bulk/issues/transition`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "taskId": "10641" }`

---

POST

## Bulk unwatch issues

Use this API to submit a bulk unwatch request. You can unwatch up to 1,000 issues in a single operation.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The request body containing the issues to be unwatched.

**selectedIssueIdsOrKeys**

array<string>

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

SubmittedBulkOperation

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/bulk/issues/unwatch

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "selectedIssueIdsOrKeys": [ "10001", "10002" ] }`; const response = await requestJira(`/rest/api/3/bulk/issues/unwatch`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "taskId": "10641" }`

---

POST

## Bulk watch issues

Use this API to submit a bulk watch request. You can watch up to 1,000 issues in a single operation.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
  * Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The request body containing the issues to be watched.

**selectedIssueIdsOrKeys**

array<string>

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

SubmittedBulkOperation

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/bulk/issues/watch

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "selectedIssueIdsOrKeys": [ "10001", "10002" ] }`; const response = await requestJira(`/rest/api/3/bulk/issues/watch`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "taskId": "10641" }`

---

GET

## Get bulk issue operation progress

Use this to get the progress state for the specified bulk operation `taskId`.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).


If the task is running, this resource will return:


    1
    {"taskId":"10779","status":"RUNNING","progressPercent":65,"submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"created":1690180055963,"started":1690180056206,"updated":169018005829}


If the task has completed, then this resource will return:


    1
    {"processedAccessibleIssues":[10001,10002],"created":1709189449954,"progressPercent":100,"started":1709189450154,"status":"COMPLETE","submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"invalidOrInaccessibleIssueCount":0,"taskId":"10000","totalIssueCount":2,"updated":1709189450354}


**Note:** You can view task progress for up to 14 days from creation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**taskId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

BulkOperationProgress

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/bulk/queue/{taskId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/bulk/queue/{taskId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "created": 1704110400000, "invalidOrInaccessibleIssueCount": 0, "processedAccessibleIssues": [ 10001, 10002 ], "progressPercent": 100, "started": 1704110460000, "status": "COMPLETE", "submittedBy": { "accountId": "5b10a2844c20165700ede21g" }, "taskId": "10000", "totalIssueCount": 2, "updated": 1704110520000 }`