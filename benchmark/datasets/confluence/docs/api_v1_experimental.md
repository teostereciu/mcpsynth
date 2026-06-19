# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-experimental/*

---

Cloud

Confluence Cloud / Reference / REST API

# Experimental

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

APIs in this section can change without any prior deprecation notice.

Operations

[DEL/wiki/rest/api/content/{id}/pageTree](/cloud/confluence/rest/v1/api-group-experimental/#api-wiki-rest-api-content-id-pagetree-delete)[GET/wiki/rest/api/space/{spaceKey}/label](/cloud/confluence/rest/v1/api-group-experimental/#api-wiki-rest-api-space-spacekey-label-get)[POST/wiki/rest/api/space/{spaceKey}/label](/cloud/confluence/rest/v1/api-group-experimental/#api-wiki-rest-api-space-spacekey-label-post)[DEL/wiki/rest/api/space/{spaceKey}/label](/cloud/confluence/rest/v1/api-group-experimental/#api-wiki-rest-api-space-spacekey-label-delete)

---

DEL

## Delete page tree

Moves a pagetree rooted at a page to the space's trash:

  * If the content's type is `page` and its status is `current`, it will be trashed including all its descendants.
  * For every other combination of content type and status, this API is not supported.


This API accepts the pageTree delete request and returns a task ID. The delete process happens asynchronously.

Response example:


    1
    2
    3
    4
    5
    6
    7
    8

     {
          "id" : "1180606",
          "links" : {
               "status" : "/rest/api/longtask/1180606"
          }
     }


Use the `/longtask/<taskId>` REST API to get the copy task status.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Delete' permission for the space that the content is in.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`delete:content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

string

Required

### Responses

202Accepted

Returned if the request to trash content and all its current page descendants, is successfully accepted.

#### application/json

LongTask

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/wiki/rest/api/content/{id}/pageTree

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/pageTree`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

202Response

`1 2 3 4 5 6 7 ``{ "ari": "<string>", "id": "<string>", "links": { "status": "<string>" } }`

---

GET

## Get Space LabelsExperimental

Returns a list of labels associated with a space. Can provide a prefix as well as other filters to select different types of labels.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-space.summary`

**Granular** :`read:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**prefix**

string

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the list of labels is returned.

#### application/json

LabelArray

Show child properties

404Not Found

GET/wiki/rest/api/space/{spaceKey}/label

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/label`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

POST

## Add labels to a spaceExperimental

Adds labels to a piece of content. Does not modify the existing labels.

Notes:

  * Labels can also be added when creating content ([Create content]()).
  * Labels can be updated when updating content ([Update content]()). This will delete the existing labels and replace them with the labels in the request.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to update the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-space`

**Granular** :`read:label:confluence`, `write:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Request bodyapplication/json

Expand all

The labels to add to the content.

array<LabelCreate>

**prefix**

string

Required

**name**

string

Required

**Additional Properties**

any

### Responses

200OK

Returned if the labels are added to the content.

#### application/json

LabelArray

Show child properties

400Bad Request

403Forbidden

404Not Found

POST/wiki/rest/api/space/{spaceKey}/label

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `[ { "prefix": "<string>", "name": "<string>" } ]`; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/label`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

DEL

## Remove label from a spaceExperimental

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-space`

**Granular** :`write:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**name**

string

Required

**prefix**

string

### Responses

204No Content

Returned if the label was successfully deleted.

400Bad Request

404Not Found

DEL/wiki/rest/api/space/{spaceKey}/label

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/label?name={name}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`