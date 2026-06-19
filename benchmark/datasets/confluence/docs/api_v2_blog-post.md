# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-blog-post/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Blog Post

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/blogposts](/cloud/confluence/rest/v2/api-group-blog-post/#api-blogposts-get)[POST/blogposts](/cloud/confluence/rest/v2/api-group-blog-post/#api-blogposts-post)[GET/blogposts/{id}](/cloud/confluence/rest/v2/api-group-blog-post/#api-blogposts-id-get)[PUT/blogposts/{id}](/cloud/confluence/rest/v2/api-group-blog-post/#api-blogposts-id-put)[DEL/blogposts/{id}](/cloud/confluence/rest/v2/api-group-blog-post/#api-blogposts-id-delete)[GET/labels/{id}/blogposts](/cloud/confluence/rest/v2/api-group-blog-post/#api-labels-id-blogposts-get)[GET/spaces/{id}/blogposts](/cloud/confluence/rest/v2/api-group-blog-post/#api-spaces-id-blogposts-get)

---

GET

## Get blog posts

Returns all blog posts. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission). Only blog posts that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**id**

array<integer>

**space-id**

array<integer>

**sort**

BlogPostSortOrder

**status**

array<string>

**title**

string

**body-format**

PrimaryBodyRepresentation

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested blog posts are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<BlogPost>

Show child properties

400Bad Request

401Unauthorized

GET/blogposts

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>", "editui": "<string>", "tinyui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

POST

## Create blog post

Creates a new blog post in the space specified by the spaceId.

By default this will create the blog post as a non-draft, unless the status is specified as draft. If creating a non-draft, the title must not be empty.

Currently only supports the storage representation specified in the body.representation enums below

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Query parameters

**private**

boolean

#### Request bodyapplication/json

Expand all

**spaceId**

string

Required

**status**

string

**title**

string

**body**

oneOf [BlogPostBodyWrite, BlogPostNestedBodyWrite]

**createdAt**

string

### Responses

200OK

Returned if the blog post was created successfully.

#### application/json

allOf [BlogPostSingle, object]

BlogPostSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

413Request Entity Too Large

POST/blogposts

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "spaceId": "<string>", "status": "current", "title": "<string>", "body": { "representation": "storage", "value": "<string>" }, "createdAt": "<string>" }`; const response = await requestConfluence(`/wiki/api/v2/blogposts`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 ``{ "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "isFavoritedByCurrentUser": true, "_links": { "base": "<string>" } }`

---

GET

## Get blog post by id

Returns a specific blog post.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**body-format**

PrimaryBodyRepresentationSingle

**get-draft**

boolean

**status**

array<string>

**version**

integer

**include-labels**

boolean

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

Show 3 hidden parameters

### Responses

200OK

Returned if the requested blog post is returned.

#### application/json

allOf [BlogPostSingle, object]

BlogPostSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 ``{ "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "isFavoritedByCurrentUser": true, "_links": { "base": "<string>" } }`

---

PUT

## Update blog post

Update a blog post by id.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the blog post and its corresponding space. Permission to update blog posts in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:page:confluence`

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

**status**

string

Required

**title**

string

Required

**spaceId**

string

**body**

oneOf [BlogPostBodyWrite, BlogPostNestedBodyWrite]

Required

**version**

object

Required

**createdAt**

string

### Responses

200OK

Returned if the requested blog post is successfully updated.

#### application/json

allOf [BlogPostSingle, object]

BlogPostSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/blogposts/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "body": { "representation": "storage", "value": "<string>" }, "version": { "number": 254, "message": "<string>" }, "createdAt": "<string>" }`; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 ``{ "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {}, "view": {} }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "version": {} } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "likes": { "results": [ { "accountId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "versions": { "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "isFavoritedByCurrentUser": true, "_links": { "base": "<string>" } }`

---

DEL

## Delete blog post

Delete a blog post by id.

By default this will delete blog posts that are non-drafts. To delete a blog post that is a draft, the endpoint must be called on a draft with the following param `draft=true`. Discarded drafts are not sent to the trash and are permanently deleted.

Deleting a blog post that is not a draft moves the blog post to the trash, where it can be restored later. To permanently delete a blog post (or "purge" it), the endpoint must be called on a **trashed** blog post with the following param `purge=true`.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the blog post and its corresponding space. Permission to delete blog posts in the space. Permission to administer the space (if attempting to purge).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`delete:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**purge**

boolean

**draft**

boolean

### Responses

204No Content

Returned if the blog post was successfully deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/blogposts/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get blog posts for label

Returns the blogposts of specified label. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**space-id**

array<integer>

**body-format**

PrimaryBodyRepresentation

**sort**

BlogPostSortOrder

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested blog posts for specified label were successfully fetched.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<BlogPost>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/labels/{id}/blogposts

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/labels/{id}/blogposts`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>", "editui": "<string>", "tinyui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get blog posts in space

Returns all blog posts in a space. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission) and view the space. Only blog posts that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**sort**

BlogPostSortOrder

**status**

array<string>

**title**

string

**body-format**

PrimaryBodyRepresentation

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested blog posts are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<BlogPost>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}/blogposts

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}/blogposts`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``{ "results": [ { "id": "<string>", "status": "current", "title": "<string>", "spaceId": "<string>", "authorId": "<string>", "createdAt": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "body": { "storage": {}, "atlas_doc_format": {} }, "_links": { "webui": "<string>", "editui": "<string>", "tinyui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`