# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-body/*

---

Cloud

Confluence Cloud / Reference / REST API

# Content body

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[POST/wiki/rest/api/contentbody/convert/async/{to}](/cloud/confluence/rest/v1/api-group-content-body/#api-wiki-rest-api-contentbody-convert-async-to-post)[GET/wiki/rest/api/contentbody/convert/async/{id}](/cloud/confluence/rest/v1/api-group-content-body/#api-wiki-rest-api-contentbody-convert-async-id-get)[GET/wiki/rest/api/contentbody/convert/async/bulk/tasks](/cloud/confluence/rest/v1/api-group-content-body/#api-wiki-rest-api-contentbody-convert-async-bulk-tasks-get)[POST/wiki/rest/api/contentbody/convert/async/bulk/tasks](/cloud/confluence/rest/v1/api-group-content-body/#api-wiki-rest-api-contentbody-convert-async-bulk-tasks-post)

---

POST

## Asynchronously convert content body

Converts a content body from one format to another format asynchronously. Returns the asyncId for the asynchronous task.

Supported conversions:

  * atlas_doc_format: editor, export_view, storage, styled_view, view
  * storage: atlas_doc_format, editor, export_view, styled_view, view
  * editor: storage


No other conversions are supported at the moment. Once a conversion is completed, it will be available for 5 minutes at the result endpoint.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: If request specifies 'contentIdContext', 'View' permission for the space, and permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content.metadata:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**to**

string

Required

#### Query parameters

Expand all

**include**

array<string>

**spaceKeyContext**

string

**contentIdContext**

string

**allowCache**

boolean

**embeddedContentRender**

string

#### Request bodyapplication/json

Expand all

The content body to convert.

**value**

string

Required

**representation**

string

Required

**Additional Properties**

any

### Responses

200OK

Returned if the content is added to the messaging queue for conversion. This id will be available for 5 minutes after the conversion is complete.

#### application/json

AsyncId

Show child properties

400Bad Request

404Not Found

POST/wiki/rest/api/contentbody/convert/async/{to}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "value": "<string>", "representation": "view" }`; const response = await requestConfluence(`/wiki/rest/api/contentbody/convert/async/{to}`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "asyncId": "<string>" }`

---

GET

## Get asynchronously converted content body from the id or the current content_status of the task.

Returns the content body for the corresponding `asyncId` of a completed conversion task. If the task is not completed, the task content_status is returned instead.

Once a conversion task is completed, the result can be obtained for up to 5 minutes, or until an identical conversion request is made again with the `allowCache` parameter set to false.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: If request specifies 'contentIdContext', 'View' permission for the space, and permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content.metadata:confluence`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if successfully found an async conversion task associated with the id.

#### application/json

AsyncContentBody

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/contentbody/convert/async/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/contentbody/convert/async/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 ``{ "value": "<string>", "representation": "view", "renderTaskId": "<string>", "error": "<string>", "content_status": "WORKING", "embeddedContent": [ { "entityId": 2154, "entityType": "<string>", "entity": {} } ], "webresource": { "_expandable": { "uris": "<string>" }, "keys": [ "<string>" ], "contexts": [ "<string>" ], "uris": { "all": [ "<string>" ], "css": [ "<string>" ], "js": [ "<string>" ], "_expandable": { "css": [ "<string>" ], "js": [ "<string>" ] } }, "tags": { "all": "<string>", "css": "<string>", "data": "<string>", "js": "<string>", "_expandable": {} }, "superbatch": { "uris": { "all": [ "<string>" ], "css": [ "<string>" ], "js": [ "<string>" ] }, "tags": { "all": "<string>", "css": "<string>", "data": "<string>", "js": "<string>" }, "metatags": "<string>", "_expandable": {} } }, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }`

---

GET

## Get asynchronous content body conversion task result in bulk

Returns the content body for the corresponding `asyncId` of a completed conversion task. If the task is not completed, the task content_status is returned instead.

Once a conversion task is completed, the result can be obtained for up to 5 minutes, or until an identical conversion request is made again with the `allowCache` parameter set to false.

Note that there is a maximum max_results of 50 task results per request to this endpoint.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content.metadata:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**ids**

array<string>

Required

### Responses

200OK

Returned if asynchronous conversion tasks are successfully found.

#### application/json

array<AsyncContentBody>

Show child properties

400Bad Request

GET/wiki/rest/api/contentbody/convert/async/bulk/tasks

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/contentbody/convert/async/bulk/tasks?ids={ids}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 ``[ { "value": "<string>", "representation": "view", "renderTaskId": "<string>", "error": "<string>", "content_status": "WORKING", "embeddedContent": [ { "entityId": 2154, "entityType": "<string>", "entity": {} } ], "webresource": { "_expandable": { "uris": "<string>" }, "keys": [ "<string>" ], "contexts": [ "<string>" ], "uris": { "all": [ "<string>" ], "css": [ "<string>" ], "js": [ "<string>" ], "_expandable": { "css": [ "<string>" ], "js": [ "<string>" ] } }, "tags": { "all": "<string>", "css": "<string>", "data": "<string>", "js": "<string>", "_expandable": {} }, "superbatch": {} }, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} } ]`

---

POST

## Create asynchronous content body conversion tasks in bulk

Asynchronously converts content bodies from one format to another format in bulk. Use the Content body REST API to get the content_status of conversion tasks. Note that there is a maximum max_results of 10 conversions per request to this endpoint.

Supported conversions:

  * storage: editor, export_view, styled_view, view
  * editor: storage


Once a conversion task is completed, it is available for polling for up to 5 minutes.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space, and permission to view the content if the `spaceKeyContext` or `contentIdContext` are present.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content.metadata:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

An array of parameters to create content body conversion tasks.

**conversionInputs**

array<ContentBodyConversionInput>

### Responses

200OK

Returned if asynchronous tasks are created to convert content bodies. If a conversion task fails to be created, a âFAILED_TO_QUEUEâ string will be returned instead of an asyncId.

#### application/json

array<AsyncId>

Show child properties

400Bad Request

POST/wiki/rest/api/contentbody/convert/async/bulk/tasks

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "conversionInputs": [ { "to": "<string>", "allowCache": true, "spaceKeyContext": "<string>", "contentIdContext": "<string>", "embeddedContentRender": "current", "include": [ "<string>" ], "body": { "value": "<string>", "representation": "view" } } ] }`; const response = await requestConfluence(`/wiki/rest/api/contentbody/convert/async/bulk/tasks`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``[ { "asyncId": "<string>" } ]`