# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-labels/*

---

Cloud

Confluence Cloud / Reference / REST API

# Content labels

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[POST/wiki/rest/api/content/{id}/label](/cloud/confluence/rest/v1/api-group-content-labels/#api-wiki-rest-api-content-id-label-post)[DEL/wiki/rest/api/content/{id}/label](/cloud/confluence/rest/v1/api-group-content-labels/#api-wiki-rest-api-content-id-label-delete)[DEL/wiki/rest/api/content/{id}/label/{label}](/cloud/confluence/rest/v1/api-group-content-labels/#api-wiki-rest-api-content-id-label-label-delete)

---

POST

## Add labels to content

Adds labels to a piece of content. Does not modify the existing labels.

Notes:

  * Labels can also be added when creating content ([Create content]()).
  * Labels can be updated when updating content ([Update content]()). This will delete the existing labels and replace them with the labels in the request.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to update the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`read:label:confluence`, `write:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

The labels to add to the content.

oneOf [array<LabelCreate>, LabelCreate]

LabelCreate

Show child properties

### Responses

200OK

Returned if the labels are added to the content.

#### application/json

LabelArray

Show child properties

400Bad Request

403Forbidden

404Not Found

POST/wiki/rest/api/content/{id}/label

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `[ { "prefix": "<string>", "name": "<string>" } ]`; const response = await requestConfluence(`/wiki/rest/api/content/{id}/label`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

DEL

## Remove label from content using query parameter

Removes a label from a piece of content. Labels can't be deleted from archived content. This is similar to [Remove label from content]() except that the label name is specified via a query parameter.

Use this method if the label name has "/" characters, as [Remove label from content using query parameter]() does not accept "/" characters for the label name.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to update the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**name**

string

Required

### Responses

204No Content

Returned if the label is removed. The response body will be empty.

403Forbidden

404Not Found

DEL/wiki/rest/api/content/{id}/label

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/label?name={name}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove label from content

Removes a label from a piece of content. Labels can't be deleted from archived content. This is similar to [Remove label from content using query parameter]() except that the label name is specified via a path parameter.

Use this method if the label name does not have "/" characters, as the path parameter does not accept "/" characters for security reasons. Otherwise, use [Remove label from content using query parameter]().

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to update the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**id**

string

Required

**label**

string

Required

### Responses

204No Content

Returned if the label is removed. The response body will be empty.

400Bad Request

403Forbidden

404Not Found

DEL/wiki/rest/api/content/{id}/label/{label}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/label/{label}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`