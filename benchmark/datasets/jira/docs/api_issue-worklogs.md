# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-worklogs/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue worklogs

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue worklogs. Use it to:

  * get, create, update, and delete worklogs.
  * obtain lists of updated or deleted worklogs.


Operations

[GET/rest/api/3/issue/{issueIdOrKey}/worklog](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-get)[POST/rest/api/3/issue/{issueIdOrKey}/worklog](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-post)[DEL/rest/api/3/issue/{issueIdOrKey}/worklog](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-delete)[POST/rest/api/3/issue/{issueIdOrKey}/worklog/move](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-move-post)[GET/rest/api/3/issue/{issueIdOrKey}/worklog/{id}](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-id-get)[PUT/rest/api/3/issue/{issueIdOrKey}/worklog/{id}](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-id-put)[DEL/rest/api/3/issue/{issueIdOrKey}/worklog/{id}](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-issue-issueidorkey-worklog-id-delete)[GET/rest/api/3/worklog/deleted](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-worklog-deleted-get)[POST/rest/api/3/worklog/list](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-worklog-list-post)[GET/rest/api/3/worklog/updated](/cloud/jira/platform/rest/v3/api-group-issue-worklogs/#api-rest-api-3-worklog-updated-get)

---

GET

## Get issue worklogs

Returns worklogs for an issue (ordered by created time), starting from the oldest worklog or from the worklog started on or after a date and time.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Workloads are only returned where the user has:

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:group:jira`, `read:issue-worklog:jira`, `read:issue-worklog.property:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Query parameters

Expand all

**startAt**

integer

**maxResults**

integer

**startedAfter**

integer

**startedBefore**

integer

**expand**

string

### Responses

200OK

Returned if the request is successful

#### application/json

PageOfWorklogs

Paginated list of worklog details

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/issue/{issueIdOrKey}/worklog

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``{ "maxResults": 1, "startAt": 0, "total": 1, "worklogs": [ { "author": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "comment": { "type": "doc", "version": 1, "content": [ { "type": "paragraph", "content": [ { "type": "text", "text": "I did some work here." } ] } ] }, "id": "100028", "issueId": "10002", "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000", "started": "2021-01-17T12:34:00.000+0000", "timeSpent": "3h 20m", "timeSpentSeconds": 12000, "updateAuthor": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "updated": "2021-01-18T23:45:00.000+0000", "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group", "value": "jira-developers" } } ] }`

---

POST

## Add worklog

Adds a worklog to an issue.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Work on issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue-worklog:jira`, `write:issue-worklog.property:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-worklog:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Query parameters

Expand all

**notifyUsers**

boolean

**adjustEstimate**

string

**newEstimate**

string

**reduceBy**

string

**expand**

string

**overrideEditableFlag**

boolean

#### Request bodyapplication/json

Expand all

**comment**

any

**properties**

array<EntityProperty>

**started**

string

**timeSpent**

string

**timeSpentSeconds**

integer

**visibility**

Visibility

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

Worklog

Details of a worklog.

Show child properties

400Bad Request

401Unauthorized

404Not Found

413Request Entity Too Large

POST/rest/api/3/issue/{issueIdOrKey}/worklog

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "comment": { "content": [ { "content": [ { "text": "I did some work here.", "type": "text" } ], "type": "paragraph" } ], "type": "doc", "version": 1 }, "started": "2021-01-17T12:34:00.000+0000", "timeSpentSeconds": 12000, "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group" } }`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``{ "author": { "accountId": "<string>", "accountType": "<string>", "active": true, "avatarUrls": { "16x16": "<string>", "24x24": "<string>", "32x32": "<string>", "48x48": "<string>" }, "displayName": "<string>", "emailAddress": "<string>", "key": "<string>", "name": "<string>", "self": "<string>", "timeZone": "<string>" }, "created": "<string>", "id": "<string>", "issueId": "<string>", "properties": [ { "key": "<string>" } ], "self": "<string>", "started": "<string>", "timeSpent": "<string>", "timeSpentSeconds": 192, "updateAuthor": { "accountId": "<string>", "accountType": "<string>", "active": true, "avatarUrls": { "16x16": "<string>", "24x24": "<string>", "32x32": "<string>", "48x48": "<string>" }, "displayName": "<string>", "emailAddress": "<string>", "key": "<string>", "name": "<string>", "self": "<string>", "timeZone": "<string>" }, "updated": "<string>", "visibility": { "identifier": "<string>", "type": "group", "value": "<string>" } }`

---

DEL

## Bulk delete worklogsExperimental

Deletes a list of worklogs from an issue. This is an experimental API with limitations:

  * You can't delete more than 5000 worklogs at once.
  * No notifications will be sent for deleted worklogs.


Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * _Delete all worklogs_[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog.
  * If any worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue-worklog:jira`, `delete:issue-worklog.property:jira`, `write:issue.time-tracking:jira`, `read:group:jira`, `read:issue-worklog:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Query parameters

Expand all

**adjustEstimate**

string

**overrideEditableFlag**

boolean

#### Request bodyapplication/json

A JSON object containing a list of worklog IDs.

**ids**

array<integer>

Required

### Responses

200OK

Returned if the bulk deletion request was partially successful, with a message indicating partial success.

204No Content

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/issue/{issueIdOrKey}/worklog

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "ids": [ 1, 2, 5, 10 ] }`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog`, { method: 'DELETE', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Bulk move worklogsExperimental

Moves a list of worklogs from one issue to another. This is an experimental API with several limitations:

  * You can't move more than 5000 worklogs at once.
  * You can't move worklogs containing an attachment.
  * You can't move worklogs restricted by project roles.
  * No notifications will be sent for moved worklogs.
  * No webhooks or events will be sent for moved worklogs.
  * No issue history will be recorded for moved worklogs.


Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the projects containing the source and destination issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * _Delete all worklogs_ [project permission](https://confluence.atlassian.com/x/yodKLg)
  * _Work on issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) to log work on an issue, that is to create a worklog entry, if time tracking is enabled. This permission is required as a prerequisite for applying the other time-tracking permissions
  * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:issue-worklog:jira`, `write:issue-worklog:jira`, `delete:issue-worklog:jira`, `read:issue-worklog.property:jira`, `write:issue-worklog.property:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Query parameters

Expand all

**adjustEstimate**

string

**overrideEditableFlag**

boolean

#### Request bodyapplication/json

Expand all

A JSON object containing a list of worklog IDs and the ID or key of the destination issue.

**ids**

array<integer>

**issueIdOrKey**

string

### Responses

200OK

Returned if the request is partially successful.

204No Content

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/issue/{issueIdOrKey}/worklog/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "ids": [ 1, 2, 5, 10 ], "issueIdOrKey": "ABC-1234" }`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog/move`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get worklog

Returns a worklog.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:comment:jira`, `read:group:jira`, `read:issue-worklog:jira`, `read:issue-worklog.property:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**id**

string

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Worklog

Details of a worklog.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/issue/{issueIdOrKey}/worklog/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``{ "author": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "comment": { "type": "doc", "version": 1, "content": [ { "type": "paragraph", "content": [ { "type": "text", "text": "I did some work here." } ] } ] }, "id": "100028", "issueId": "10002", "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000", "started": "2021-01-17T12:34:00.000+0000", "timeSpent": "3h 20m", "timeSpentSeconds": 12000, "updateAuthor": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "updated": "2021-01-18T23:45:00.000+0000", "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group", "value": "jira-developers" } }`

---

PUT

## Update worklog

Updates a worklog.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * _Edit all worklogs_[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or _Edit own worklogs_ to update worklogs created by the user.
  * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:comment:jira`, `read:group:jira`, `read:issue-worklog:jira`, `read:issue-worklog.property:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**id**

string

Required

#### Query parameters

Expand all

**notifyUsers**

boolean

**adjustEstimate**

string

**newEstimate**

string

**expand**

string

**overrideEditableFlag**

boolean

#### Request bodyapplication/json

Expand all

**comment**

any

**properties**

array<EntityProperty>

**started**

string

**timeSpent**

string

**timeSpentSeconds**

integer

**visibility**

Visibility

**Additional Properties**

any

### Responses

200OK

Returned if the request is successful

#### application/json

Worklog

Details of a worklog.

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/issue/{issueIdOrKey}/worklog/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "comment": { "content": [ { "content": [ { "text": "I did some work here.", "type": "text" } ], "type": "paragraph" } ], "type": "doc", "version": 1 }, "started": "2021-01-17T12:34:00.000+0000", "timeSpentSeconds": 12000, "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group" } }`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``{ "author": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "comment": { "type": "doc", "version": 1, "content": [ { "type": "paragraph", "content": [ { "type": "text", "text": "I did some work here." } ] } ] }, "id": "100028", "issueId": "10002", "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000", "started": "2021-01-17T12:34:00.000+0000", "timeSpent": "3h 20m", "timeSpentSeconds": 12000, "updateAuthor": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "updated": "2021-01-18T23:45:00.000+0000", "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group", "value": "jira-developers" } }`

---

DEL

## Delete worklog

Deletes a worklog from an issue.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * _Delete all worklogs_[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog or _Delete own worklogs_ to delete worklogs created by the user,
  * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue-worklog:jira`, `delete:issue-worklog.property:jira`, `write:issue.time-tracking:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**id**

string

Required

#### Query parameters

Expand all

**notifyUsers**

boolean

**adjustEstimate**

string

**newEstimate**

string

**increaseBy**

string

**overrideEditableFlag**

boolean

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/issue/{issueIdOrKey}/worklog/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/worklog/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get IDs of deleted worklogs

Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

This resource does not return worklogs deleted during the minute preceding the request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-worklog:jira`, `read:issue-worklog.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**since**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

ChangedWorklogs

List of changed worklogs.

Show child properties

401Unauthorized

GET/rest/api/3/worklog/deleted

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/worklog/deleted`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "lastPage": true, "nextPage": "https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013693136", "self": "https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013671562", "since": 1438013671562, "until": 1438013693136, "values": [ { "properties": [], "updatedTime": 1438013671562, "worklogId": 103 }, { "properties": [], "updatedTime": 1438013672165, "worklogId": 104 }, { "properties": [], "updatedTime": 1438013693136, "worklogId": 105 } ] }`

---

POST

## Get worklogs

Returns worklog details for a list of worklog IDs.

The returned list of worklogs is limited to 1000 items.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

  * the worklog is set as _Viewable by All Users_.
  * the user is a member of a project role or group with permission to view the worklog.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:comment:jira`, `read:group:jira`, `read:issue-worklog:jira`, `read:issue-worklog.property:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

string

#### Request bodyapplication/json

A JSON object containing a list of worklog IDs.

**ids**

array<integer>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Worklog>

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/worklog/list

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "ids": [ 1, 2, 5, 10 ] }`; const response = await requestJira(`/rest/api/3/worklog/list`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``[ { "author": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "comment": { "type": "doc", "version": 1, "content": [ { "type": "paragraph", "content": [ { "type": "text", "text": "I did some work here." } ] } ] }, "id": "100028", "issueId": "10002", "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000", "started": "2021-01-17T12:34:00.000+0000", "timeSpent": "3h 20m", "timeSpentSeconds": 12000, "updateAuthor": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "updated": "2021-01-18T23:45:00.000+0000", "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group", "value": "jira-developers" } } ]`

---

GET

## Get IDs of updated worklogs

Returns a list of IDs and update timestamps for worklogs updated after a date and time.

This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

This resource does not return worklogs updated during the minute preceding the request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

  * the worklog is set as _Viewable by All Users_.
  * the user is a member of a project role or group with permission to view the worklog.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-worklog:jira`, `read:issue-worklog.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**since**

integer

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

ChangedWorklogs

List of changed worklogs.

Show child properties

401Unauthorized

GET/rest/api/3/worklog/updated

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/worklog/updated`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "lastPage": true, "nextPage": "https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013693136", "self": "https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013671562", "since": 1438013671562, "until": 1438013693136, "values": [ { "properties": [], "updatedTime": 1438013671562, "worklogId": 103 }, { "properties": [], "updatedTime": 1438013672165, "worklogId": 104 }, { "properties": [], "updatedTime": 1438013693136, "worklogId": 105 } ] }`