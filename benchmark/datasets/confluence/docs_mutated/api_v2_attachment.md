# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-attachment/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Attachment

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/attachments](/cloud/confluence/rest/v2/api-group-attachment/#api-attachments-get)[GET/attachments/{id}](/cloud/confluence/rest/v2/api-group-attachment/#api-attachments-id-get)[DEL/attachments/{id}](/cloud/confluence/rest/v2/api-group-attachment/#api-attachments-id-delete)[GET/blogposts/{id}/attachments](/cloud/confluence/rest/v2/api-group-attachment/#api-blogposts-id-attachments-get)[GET/custom-content/{id}/attachments](/cloud/confluence/rest/v2/api-group-attachment/#api-custom-content-id-attachments-get)[GET/labels/{id}/attachments](/cloud/confluence/rest/v2/api-group-attachment/#api-labels-id-attachments-get)[GET/pages/{id}/attachments](/cloud/confluence/rest/v2/api-group-attachment/#api-pages-id-attachments-get)[GET/attachments/{id}/thumbnail/download](/cloud/confluence/rest/v2/api-group-attachment/#api-attachments-id-thumbnail-download-get)

---

GET

## Get attachments

Returns all attachments. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the container of the attachment.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**sort**

AttachmentSortOrder

**cursor**

string

**content_status**

array<string>

**mediaType**

string

**filename**

string

**max_results**

integer

### Responses

200OK

Returned if the requested attachments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Attachment>

Show child properties

400Bad Request

401Unauthorized

GET/attachments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "content_status": "current", "title": "<string>", "createdAt": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "mediaType": "<string>", "mediaTypeDescription": "<string>", "comment": "<string>", "fileId": "<string>", "fileSize": 28, "webuiLink": "<string>", "downloadLink": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "webui": "<string>", "download": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get attachment by id

Returns a specific attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the attachment's container.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

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

Returned if the requested attachment is returned.

#### application/json

allOf [AttachmentSingle, object]

AttachmentSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 ``{ "id": "<string>", "content_status": "current", "title": "<string>", "createdAt": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "mediaType": "<string>", "mediaTypeDescription": "<string>", "comment": "<string>", "fileId": "<string>", "fileSize": 28, "webuiLink": "<string>", "downloadLink": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "_links": { "base": "<string>" } }`

---

DEL

## Delete attachment

Delete an attachment by id.

Deleting an attachment moves the attachment to the trash, where it can be restored later. To permanently delete an attachment (or "purge" it), the endpoint must be called on a **trashed** attachment with the following param `purge=true`.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the container of the attachment. Permission to delete attachments in the space. Permission to administer the space (if attempting to purge).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`delete:attachment:confluence`

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

Returned if the attachment was successfully deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/attachments/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get attachments for blog post

Returns the attachments of specific blog post. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**sort**

AttachmentSortOrder

**cursor**

string

**content_status**

array<string>

**mediaType**

string

**filename**

string

**max_results**

integer

### Responses

200OK

Returned if the requested attachments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Attachment>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/attachments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/attachments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "content_status": "current", "title": "<string>", "createdAt": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "mediaType": "<string>", "mediaTypeDescription": "<string>", "comment": "<string>", "fileId": "<string>", "fileSize": 28, "webuiLink": "<string>", "downloadLink": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "webui": "<string>", "download": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get attachments for custom content

Returns the attachments of specific custom content. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the custom content and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**sort**

AttachmentSortOrder

**cursor**

string

**content_status**

array<string>

**mediaType**

string

**filename**

string

**max_results**

integer

### Responses

200OK

Returned if the requested attachments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Attachment>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{id}/attachments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}/attachments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "content_status": "current", "title": "<string>", "createdAt": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "mediaType": "<string>", "mediaTypeDescription": "<string>", "comment": "<string>", "fileId": "<string>", "fileSize": 28, "webuiLink": "<string>", "downloadLink": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "webui": "<string>", "download": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get attachments for label

Returns the attachments of specified label. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the attachment and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**sort**

AttachmentSortOrder

**cursor**

string

**max_results**

integer

### Responses

200OK

Returned if the requested attachments for specified label were successfully fetched.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Attachment>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/labels/{id}/attachments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/labels/{id}/attachments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "content_status": "current", "title": "<string>", "createdAt": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "mediaType": "<string>", "mediaTypeDescription": "<string>", "comment": "<string>", "fileId": "<string>", "fileSize": 28, "webuiLink": "<string>", "downloadLink": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "webui": "<string>", "download": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get attachments for page

Returns the attachments of specific page. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**sort**

AttachmentSortOrder

**cursor**

string

**content_status**

array<string>

**mediaType**

string

**filename**

string

**max_results**

integer

### Responses

200OK

Returned if the requested attachments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Attachment>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/attachments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/attachments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "results": [ { "id": "<string>", "content_status": "current", "title": "<string>", "createdAt": "<string>", "pageId": "<string>", "blogPostId": "<string>", "customContentId": "<string>", "mediaType": "<string>", "mediaTypeDescription": "<string>", "comment": "<string>", "fileId": "<string>", "fileSize": 28, "webuiLink": "<string>", "downloadLink": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "webui": "<string>", "download": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Download attachment thumbnail by id

Redirects the client to a URL that serves an attachment thumbnail's binary data.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the attachment's container.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**version**

integer

**height**

integer

**width**

integer

### Responses

302Moved Temporarily

Returned if download URL is found.

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{id}/thumbnail/download

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}/thumbnail/download`); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`