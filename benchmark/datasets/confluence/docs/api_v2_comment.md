# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-comment/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Comment

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/attachments/{id}/footer-comments](/cloud/confluence/rest/v2/api-group-comment/#api-attachments-id-footer-comments-get)[GET/custom-content/{id}/footer-comments](/cloud/confluence/rest/v2/api-group-comment/#api-custom-content-id-footer-comments-get)[GET/pages/{id}/footer-comments](/cloud/confluence/rest/v2/api-group-comment/#api-pages-id-footer-comments-get)[GET/pages/{id}/inline-comments](/cloud/confluence/rest/v2/api-group-comment/#api-pages-id-inline-comments-get)[GET/blogposts/{id}/footer-comments](/cloud/confluence/rest/v2/api-group-comment/#api-blogposts-id-footer-comments-get)[GET/blogposts/{id}/inline-comments](/cloud/confluence/rest/v2/api-group-comment/#api-blogposts-id-inline-comments-get)[GET/footer-comments](/cloud/confluence/rest/v2/api-group-comment/#api-footer-comments-get)[POST/footer-comments](/cloud/confluence/rest/v2/api-group-comment/#api-footer-comments-post)[GET/footer-comments/{comment-id}](/cloud/confluence/rest/v2/api-group-comment/#api-footer-comments-comment-id-get)[PUT/footer-comments/{comment-id}](/cloud/confluence/rest/v2/api-group-comment/#api-footer-comments-comment-id-put)[DEL/footer-comments/{comment-id}](/cloud/confluence/rest/v2/api-group-comment/#api-footer-comments-comment-id-delete)[GET/footer-comments/{id}/children](/cloud/confluence/rest/v2/api-group-comment/#api-footer-comments-id-children-get)[GET/inline-comments](/cloud/confluence/rest/v2/api-group-comment/#api-inline-comments-get)[POST/inline-comments](/cloud/confluence/rest/v2/api-group-comment/#api-inline-comments-post)[GET/inline-comments/{comment-id}](/cloud/confluence/rest/v2/api-group-comment/#api-inline-comments-comment-id-get)[PUT/inline-comments/{comment-id}](/cloud/confluence/rest/v2/api-group-comment/#api-inline-comments-comment-id-put)[DEL/inline-comments/{comment-id}](/cloud/confluence/rest/v2/api-group-comment/#api-inline-comments-comment-id-delete)[GET/inline-comments/{id}/children](/cloud/confluence/rest/v2/api-group-comment/#api-inline-comments-id-children-get)

---

GET

## Get attachment comments

Returns the comments of the specific attachment. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the attachment and its corresponding containers.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**cursor**

string

**limit**

integer

**sort**

CommentSortOrder

**version**

integer

### Responses

200OK

Returned if the attachment comments were successfully retrieved

#### Headers

**Link**

string

#### application/json

MultiEntityResult<AttachmentCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{id}/footer-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}/footer-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "attachmentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get custom content comments

Returns the comments of the specific custom content. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content and its corresponding containers.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**cursor**

string

**limit**

integer

**sort**

CommentSortOrder

### Responses

200OK

Returned if the custom content comments were successfully retrieved

#### Headers

**Link**

string

#### application/json

MultiEntityResult<CustomContentCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{id}/footer-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}/footer-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "customContentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get footer comments for page

Returns the root footer comments of specific page. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**status**

array<string>

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested footer comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<PageCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/footer-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/footer-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "pageId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get inline comments for page

Returns the root inline comments of specific page. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**status**

array<string>

**resolution-status**

array<string>

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested inline comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<PageInlineCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/inline-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/inline-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "pageId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "resolutionStatus": "open", "properties": { "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get footer comments for blog post

Returns the root footer comments of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**status**

array<string>

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested footer comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<BlogPostCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/footer-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/footer-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get inline comments for blog post

Returns the root inline comments of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**status**

array<string>

**resolution-status**

array<string>

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested inline comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<BlogPostInlineCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/inline-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/inline-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "resolutionStatus": "open", "properties": { "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get footer comments

Returns all footer comments. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the container and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested footer comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<FooterCommentModel>

Show child properties

400Bad Request

401Unauthorized

GET/footer-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "attachmentId": "<string>", "customContentId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

POST

## Create footer comment

Create a footer comment.

The footer comment can be made against several locations:

  * at the top level (specifying pageId or blogPostId in the request body)
  * as a reply (specifying parentCommentId in the request body)
  * against an attachment (note: this is different than the comments added via the attachment properties page on the UI, which are referred to as version comments)
  * against a custom content


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The footer comment to be created

**blogPostId**

string

**pageId**

string

**parentCommentId**

string

**attachmentId**

string

**customContentId**

string

**body**

oneOf [CommentBodyWrite, CommentNestedBodyWrite]

### Responses

201Created

Returned if the footer comment is created.

#### Headers

**location**

string

#### application/json

allOf [FooterCommentModel, object]

FooterCommentModel

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/footer-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "blogPostId": "<string>", "pageId": "<string>", "parentCommentId": "<string>", "attachmentId": "<string>", "customContentId": "<string>", "body": { "representation": "storage", "value": "<string>" } }`; const response = await requestConfluence(`/wiki/api/v2/footer-comments`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 ``{ "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "attachmentId": "<string>", "customContentId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "base": "<string>" } }`

---

GET

## Get footer comment by id

Retrieves a footer comment by id

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the container and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**comment-id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentationSingle

**version**

integer

**include-properties**

boolean

**include-operations**

boolean

**include-likes**

boolean

**include-versions**

boolean

**include-version**

boolean

### Responses

200OK

Returned if the footer comment is successfully retrieved.

#### application/json

allOf [FooterCommentModel, object]

FooterCommentModel

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/footer-comments/{comment-id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{comment-id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 ``{ "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "attachmentId": "<string>", "customContentId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "_links": { "base": "<string>" } }`

---

PUT

## Update footer comment

Update a footer comment. This can be used to update the body text of a comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**comment-id**

integer

Required

#### Request bodyapplication/json

The footer comment to be created

allOf [UpdateFooterCommentModel, object]

UpdateFooterCommentModel

Show child properties

object

Show child properties

### Responses

200OK

Returned if the footer comment is updated successfully

#### application/json

FooterCommentModel

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/footer-comments/{comment-id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "version": { "number": 78, "message": "<string>" }, "body": { "representation": "storage", "value": "<string>" }, "_links": { "base": "<string>" } }`; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{comment-id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 ``{ "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "attachmentId": "<string>", "customContentId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "body": { "storage": { "representation": "<string>", "value": "<string>" }, "atlas_doc_format": { "representation": "<string>", "value": "<string>" }, "view": { "representation": "<string>", "value": "<string>" } }, "_links": { "webui": "<string>" } }`

---

DEL

## Delete footer comment

Deletes a footer comment. This is a permanent deletion and cannot be reverted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to delete comments in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`delete:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**comment-id**

integer

Required

### Responses

204No Content

Returned if the footer comment is deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/footer-comments/{comment-id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{comment-id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get children footer comments

Returns the children footer comments of specific comment. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested footer comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<ChildrenCommentModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/footer-comments/{id}/children

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{id}/children`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get inline comments

Returns all inline comments. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested inline comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<InlineCommentModel>

Show child properties

400Bad Request

401Unauthorized

GET/inline-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "resolutionLastModifierId": "<string>", "resolutionLastModifiedAt": "<string>", "resolutionStatus": "open", "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" }, "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

POST

## Create inline comment

Create an inline comment. This can be at the top level (specifying pageId or blogPostId in the request body) or as a reply (specifying parentCommentId in the request body). Note the inlineCommentProperties object in the request body is used to select the text the inline comment should be tied to. This is what determines the text highlighting when viewing a page in Confluence.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The inline comment to be created

**blogPostId**

string

**pageId**

string

**parentCommentId**

string

**body**

oneOf [CommentBodyWrite, CommentNestedBodyWrite]

**inlineCommentProperties**

object

### Responses

201Created

Returned if the inline comment is created.

#### Headers

**location**

string

#### application/json

allOf [InlineCommentModel, object]

InlineCommentModel

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/inline-comments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "blogPostId": "<string>", "pageId": "<string>", "parentCommentId": "<string>", "body": { "representation": "storage", "value": "<string>" }, "inlineCommentProperties": { "textSelection": "<string>", "textSelectionMatchCount": 113, "textSelectionMatchIndex": 238 } }`; const response = await requestConfluence(`/wiki/api/v2/inline-comments`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 ``{ "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "resolutionLastModifierId": "<string>", "resolutionLastModifiedAt": "<string>", "resolutionStatus": "open", "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" }, "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "_links": { "base": "<string>" } }`

---

GET

## Get inline comment by id

Retrieves an inline comment by id

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**comment-id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentationSingle

**version**

integer

**include-properties**

boolean

**include-operations**

boolean

**include-likes**

boolean

**include-versions**

boolean

**include-version**

boolean

### Responses

200OK

Returned if the inline comment is successfully retrieved.

#### application/json

allOf [InlineCommentModel, object]

InlineCommentModel

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/inline-comments/{comment-id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{comment-id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 ``{ "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "resolutionLastModifierId": "<string>", "resolutionLastModifiedAt": "<string>", "resolutionStatus": "open", "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" }, "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "_links": { "base": "<string>" } }`

---

PUT

## Update inline comment

Update an inline comment. This can be used to update the body text of a comment and/or to resolve the comment

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**comment-id**

integer

Required

#### Request bodyapplication/json

Expand all

The inline comment to be updated

**version**

object

**body**

oneOf [CommentBodyWrite, CommentNestedBodyWrite]

**resolved**

boolean

### Responses

200OK

Returned if the inline comment is updated successfully.

#### application/json

allOf [InlineCommentModel, object]

InlineCommentModel

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/inline-comments/{comment-id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "version": { "number": 78, "message": "<string>" }, "body": { "representation": "storage", "value": "<string>" }, "resolved": true }`; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{comment-id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 ``{ "id": "<string>", "status": "current", "title": "<string>", "blogPostId": "<string>", "pageId": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "resolutionLastModifierId": "<string>", "resolutionLastModifiedAt": "<string>", "resolutionStatus": "open", "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" }, "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "_links": { "base": "<string>" } }`

---

DEL

## Delete inline comment

Deletes an inline comment. This is a permanent deletion and cannot be reverted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blogpost and its corresponding space. Permission to delete comments in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`delete:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**comment-id**

integer

Required

### Responses

204No Content

Returned if the inline comment is deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/inline-comments/{comment-id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{comment-id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get children inline comments

Returns the children inline comments of specific comment. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentation

**sort**

CommentSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested footer comments are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<InlineCommentChildrenModel>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/inline-comments/{id}/children

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{id}/children`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "parentCommentId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "resolutionStatus": "open", "properties": { "inlineMarkerRef": "<string>", "inlineOriginalSelection": "<string>" }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`