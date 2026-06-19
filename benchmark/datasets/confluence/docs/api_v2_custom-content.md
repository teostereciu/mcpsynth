# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-custom-content/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Custom Content

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/blogposts/{id}/custom-content](/cloud/confluence/rest/v2/api-group-custom-content/#api-blogposts-id-custom-content-get)[GET/custom-content](/cloud/confluence/rest/v2/api-group-custom-content/#api-custom-content-get)[POST/custom-content](/cloud/confluence/rest/v2/api-group-custom-content/#api-custom-content-post)[GET/custom-content/{id}](/cloud/confluence/rest/v2/api-group-custom-content/#api-custom-content-id-get)[PUT/custom-content/{id}](/cloud/confluence/rest/v2/api-group-custom-content/#api-custom-content-id-put)[DEL/custom-content/{id}](/cloud/confluence/rest/v2/api-group-custom-content/#api-custom-content-id-delete)[GET/pages/{id}/custom-content](/cloud/confluence/rest/v2/api-group-custom-content/#api-pages-id-custom-content-get)[GET/spaces/{id}/custom-content](/cloud/confluence/rest/v2/api-group-custom-content/#api-spaces-id-custom-content-get)

---

GET

## Get custom content by type in blog post

Returns all custom content for a given type within a given blogpost. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content, the container of the custom content (blog post), and the corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**type**

string

Required

**sort**

CustomContentSortOrder

**cursor**

string

**limit**

integer

**body-format**

CustomContentBodyRepresentation

### Responses

200OK

Returned if the requested custom content is returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<CustomContent>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/custom-content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/custom-content?type={type}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get custom content by type

Returns all custom content for a given type. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content, the container of the custom content, and the corresponding space (if different from the container).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**type**

string

Required

**id**

array<integer>

**space-id**

array<integer>

**sort**

CustomContentSortOrder

**cursor**

string

**limit**

integer

**body-format**

CustomContentBodyRepresentation

### Responses

200OK

Returned if the requested custom content is returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<CustomContent>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content?type={type}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

POST

## Create custom content

Creates a new custom content in the given space, page, blogpost or other custom content.

Only one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is required in the request body. **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to create custom content in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

**type**

string

Required

**status**

string

**spaceId**

string

**pageId**

string

**blogPostId**

string

**customContentId**

string

**title**

string

Required

**body**

oneOf [CustomContentBodyWrite, CustomContentNestedBodyWrite]

Required

### Responses

201Created

Returned if the requested custom content is created successfully.

#### Headers

**location**

string

#### application/json

allOf [CustomContentSingle, object]

CustomContentSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/custom-content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "type": "<string>", "status": "current", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "title": "<string>", "body": { "representation": "storage", "value": "<string>" } }`; const response = await requestConfluence(`/wiki/api/v2/custom-content`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 ``{ "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "base": "<string>" } }`

---

GET

## Get custom content by id

Returns a specific piece of custom content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content, the container of the custom content, and the corresponding space (if different from the container).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

CustomContentBodyRepresentationSingle

**version**

integer

**include-labels**

boolean

**include-properties**

boolean

**include-operations**

boolean

**include-versions**

boolean

**include-version**

boolean

**include-collaborators**

boolean

### Responses

200OK

Returned if the requested custom content is returned.

#### application/json

allOf [CustomContentSingle, object]

CustomContentSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 ``{ "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "base": "<string>" } }`

---

PUT

## Update custom content

Update a custom content by id. At most one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is allowed in the request body. Note that if `spaceId` is specified, it must be the same as the `spaceId` used for creating the custom content as moving custom content to a different space is not supported.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to update custom content in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

**id**

string

Required

**type**

string

Required

**status**

string

Required

**spaceId**

string

**pageId**

string

**blogPostId**

string

**customContentId**

string

**title**

string

Required

**body**

oneOf [CustomContentBodyWrite, CustomContentNestedBodyWrite]

Required

**version**

object

Required

### Responses

200OK

Returned if the requested custom content is updated successfully.

#### Headers

**location**

string

#### application/json

allOf [CustomContentSingle, object]

CustomContentSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/custom-content/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "id": "<string>", "type": "<string>", "status": "current", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "title": "<string>", "body": { "representation": "storage", "value": "<string>" }, "version": { "number": 47, "message": "<string>" } }`; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 ``{ "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "base": "<string>" } }`

---

DEL

## Delete custom content

Delete a custom content by id.

Deleting a custom content will either move it to the trash or permanently delete it (purge it), depending on the apiSupport. To permanently delete a **trashed** custom content, the endpoint must be called with the following param `purge=true`.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to delete custom content in the space. Permission to administer the space (if attempting to purge).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`delete:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**purge**

boolean

### Responses

204No Content

Returned if the custom content was deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/custom-content/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get custom content by type in page

Returns all custom content for a given type within a given page. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content, the container of the custom content (page), and the corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**type**

string

Required

**sort**

CustomContentSortOrder

**cursor**

string

**limit**

integer

**body-format**

CustomContentBodyRepresentation

### Responses

200OK

Returned if the requested custom content is returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<CustomContent>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/custom-content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/custom-content?type={type}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get custom content by type in space

Returns all custom content for a given type within a given space. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content and the corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**type**

string

Required

**cursor**

string

**limit**

integer

**body-format**

CustomContentBodyRepresentation

### Responses

200OK

Returned if the requested custom content is returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<CustomContent>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}/custom-content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}/custom-content?type={type}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "raw": {}, "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`