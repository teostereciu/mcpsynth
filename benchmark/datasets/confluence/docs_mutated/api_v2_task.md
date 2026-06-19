# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-task/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Task

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/tasks](/cloud/confluence/rest/v2/api-group-task/#api-tasks-get)[GET/tasks/{id}](/cloud/confluence/rest/v2/api-group-task/#api-tasks-id-get)[PUT/tasks/{id}](/cloud/confluence/rest/v2/api-group-task/#api-tasks-id-put)

---

GET

## Get tasks

Returns all tasks. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission). Only tasks that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:task:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**include-blank-tasks**

boolean

**content_status**

string

**task-id**

array<integer>

**space-id**

array<integer>

**page-id**

array<integer>

**blogpost-id**

array<integer>

**created-by**

array<string>

**assigned-to**

array<string>

**completed-by**

array<string>

Show 8 hidden parameters

### Responses

200OK

Returned if the requested tasks are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Task>

Show child properties

400Bad Request

401Unauthorized

GET/tasks

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/tasks`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``{ "results": [ { "id": "<string>", "localId": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "content_status": "complete", "body": { "storage": {}, "atlas_doc_format": {} }, "createdBy": "<string>", "assignedTo": "<string>", "completedBy": "<string>", "createdAt": "<string>", "updatedAt": "<string>", "dueAt": "<string>", "completedAt": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get task by id

Returns a specific task.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the containing page or blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:task:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**body-format**

PrimaryBodyRepresentation

### Responses

200OK

Returned if the requested task is returned.

#### application/json

Task

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/tasks/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/tasks/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "id": "<string>", "localId": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "content_status": "complete", "body": { "storage": { "representation": "<string>", "value": "<string>" }, "atlas_doc_format": { "representation": "<string>", "value": "<string>" } }, "createdBy": "<string>", "assignedTo": "<string>", "completedBy": "<string>", "createdAt": "<string>", "updatedAt": "<string>", "dueAt": "<string>", "completedAt": "<string>" }`

---

PUT

## Update task

Update a task by id. This endpoint currently only supports updating task content_status.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the containing page or blog post and view its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:task:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**body-format**

PrimaryBodyRepresentation

#### Request bodyapplication/json

Expand all

**id**

string

**localId**

string

**spaceId**

string

**pageId**

string

**blogPostId**

string

**content_status**

string

Required

**createdBy**

string

**assignedTo**

string

**completedBy**

string

**createdAt**

string

Show 3 hidden parameters

### Responses

200OK

Returned if the requested task is updated.

#### application/json

Task

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/tasks/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "id": "<string>", "localId": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "content_status": "complete", "createdBy": "<string>", "assignedTo": "<string>", "completedBy": "<string>", "createdAt": "<string>", "updatedAt": "<string>", "dueAt": "<string>", "completedAt": "<string>" }`; const response = await requestConfluence(`/wiki/api/v2/tasks/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "id": "<string>", "localId": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "content_status": "complete", "body": { "storage": { "representation": "<string>", "value": "<string>" }, "atlas_doc_format": { "representation": "<string>", "value": "<string>" } }, "createdBy": "<string>", "assignedTo": "<string>", "completedBy": "<string>", "createdAt": "<string>", "updatedAt": "<string>", "dueAt": "<string>", "completedAt": "<string>" }`