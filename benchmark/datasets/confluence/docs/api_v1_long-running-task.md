# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-long-running-task/*

---

Cloud

Confluence Cloud / Reference / REST API

# Long-running task

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/longtask](/cloud/confluence/rest/v1/api-group-long-running-task/#api-wiki-rest-api-longtask-get)[GET/wiki/rest/api/longtask/{id}](/cloud/confluence/rest/v1/api-group-long-running-task/#api-wiki-rest-api-longtask-id-get)

---

GET

## Get long-running tasks

Returns information about all active long-running tasks (e.g. space export), such as how long each task has been running and the percentage of each task that has completed.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:content.metadata:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**key**

string

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested tasks are returned.

#### application/json

LongTaskStatusArray

Show child properties

401Unauthorized

GET/wiki/rest/api/longtask

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/longtask`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 ``{ "results": [ { "ari": "<string>", "id": "<string>", "name": { "key": "<string>", "args": [ {} ] }, "elapsedTime": 2154, "percentageComplete": 2154, "successful": true, "finished": true, "messages": [ { "translation": "<string>", "args": [ "<string>" ] } ], "status": "<string>", "errors": [ { "translation": "<string>", "args": [ "<string>" ] } ], "additionalDetails": { "destinationId": "<string>", "destinationUrl": "<string>", "totalPageNeedToCopy": 2154, "additionalProperties": "<string>" } } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

GET

## Get long-running task

Returns information about an active long-running task (e.g. space export), such as how long it has been running and the percentage of the task that has completed.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-space.summary`

**Granular** :`read:content.metadata:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the requested task is returned.

#### application/json

LongTaskStatusWithLinks

Same as LongTaskStatus but with `_links` property.

Status keys:

  * `ERROR_UNKNOWN` \- Generic error
  * `ERROR_LOCK_FAILED` \- Could not get the lock on destination space
  * `ERROR_RELINK` \- Error when relink pages/attachments
  * `ERROR_COPY_PAGE` \- Error while copying 1 page
  * `WARN_RENAME_PAGE` \- Warning page is rename during copy
  * `WARN_IGNORE_COPY_PERMISSION` \- Warning could not copy permission
  * `WARN_IGNORE_COPY_ATTACHMENT` \- Warning could not copy attachment
  * `WARN_IGNORE_DELETE_PAGE` \- Warning ignoring delete of a non agreed on page
  * `STATUS_COPIED_PAGES` \- Message total pages are copied
  * `STATUS_COPYING_PAGES` \- Message copy pages
  * `STATUS_RELINK_PAGES` \- Message relink pages/attachments
  * `STATUS_DELETING_PAGES` \- Message delete pages
  * `STATUS_DELETED_PAGES` \- Message total pages are deleted
  * `STATUS_MOVING_PAGES` \- Message move pages
  * `WARN_IGNORE_VIEW_RESTRICTED` \- Permission changed - view restricted
  * `WARN_IGNORE_EDIT_RESTRICTED` \- Permission changed - edit restricted
  * `INITIALIZING_TASK` \- Message when initializing task
  * `UNKNOWN_STATUS` \- Message when status is unknown


Show child properties

401Unauthorized

404Not Found

GET/wiki/rest/api/longtask/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/longtask/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``{ "ari": "<string>", "id": "<string>", "name": { "key": "<string>", "args": [ {} ] }, "elapsedTime": 2154, "percentageComplete": 2154, "successful": true, "finished": true, "messages": [ { "translation": "<string>", "args": [ "<string>" ] } ], "_links": {}, "status": "<string>", "errors": [ { "translation": "<string>", "args": [ "<string>" ] } ], "additionalDetails": { "destinationId": "<string>", "destinationUrl": "<string>", "totalPageNeedToCopy": 2154, "additionalProperties": "<string>" } }`