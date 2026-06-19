# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-version/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Version

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/attachments/{id}/versions](/cloud/confluence/rest/v2/api-group-version/#api-attachments-id-versions-get)[GET/attachments/{attachment-id}/versions/{version-number}](/cloud/confluence/rest/v2/api-group-version/#api-attachments-attachment-id-versions-version-number-get)[GET/blogposts/{id}/versions](/cloud/confluence/rest/v2/api-group-version/#api-blogposts-id-versions-get)[GET/blogposts/{blogpost-id}/versions/{version-number}](/cloud/confluence/rest/v2/api-group-version/#api-blogposts-blogpost-id-versions-version-number-get)[GET/pages/{id}/versions](/cloud/confluence/rest/v2/api-group-version/#api-pages-id-versions-get)[GET/pages/{page-id}/versions/{version-number}](/cloud/confluence/rest/v2/api-group-version/#api-pages-page-id-versions-version-number-get)[GET/custom-content/{custom-content-id}/versions](/cloud/confluence/rest/v2/api-group-version/#api-custom-content-custom-content-id-versions-get)[GET/custom-content/{custom-content-id}/versions/{version-number}](/cloud/confluence/rest/v2/api-group-version/#api-custom-content-custom-content-id-versions-version-number-get)[GET/footer-comments/{id}/versions](/cloud/confluence/rest/v2/api-group-version/#api-footer-comments-id-versions-get)[GET/footer-comments/{id}/versions/{version-number}](/cloud/confluence/rest/v2/api-group-version/#api-footer-comments-id-versions-version-number-get)[GET/inline-comments/{id}/versions](/cloud/confluence/rest/v2/api-group-version/#api-inline-comments-id-versions-get)[GET/inline-comments/{id}/versions/{version-number}](/cloud/confluence/rest/v2/api-group-version/#api-inline-comments-id-versions-version-number-get)

---

GET

## Get attachment versions

Returns the versions of specific attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the attachment and its corresponding space.

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

**cursor**

string

**max_results**

integer

**sort**

VersionSortOrder

### Responses

200OK

Returned if the requested attachment versions are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Version>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{id}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>", "attachment": { "title": "<string>", "id": "<string>", "body": {} } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get version details for attachment version

Retrieves version details for the specified attachment and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the attachment.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:attachment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**attachment-id**

string

Required

**version-number**

integer

Required

### Responses

200OK

Returned if the requested version details are successfully retrieved.

#### application/json

DetailedVersion

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{attachment-id}/versions/{version-number}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{attachment-id}/versions/{version-number}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "number": 27, "authorId": "<string>", "message": "<string>", "createdAt": "<string>", "minorEdit": true, "contentTypeModified": true, "collaborators": [ "<string>" ], "prevVersion": 71, "nextVersion": 68 }`

---

GET

## Get blog post versions

Returns the versions of specific blog post.

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

PrimaryBodyRepresentation

**cursor**

string

**max_results**

integer

**sort**

VersionSortOrder

### Responses

200OK

Returned if the requested blog post versions are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Version>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>", "blogpost": { "title": "<string>", "id": "<string>", "body": {} } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get version details for blog post version

Retrieves version details for the specified blog post and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the blog post.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**blogpost-id**

integer

Required

**version-number**

integer

Required

### Responses

200OK

Returned if the requested version details are successfully retrieved.

#### application/json

DetailedVersion

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{blogpost-id}/versions/{version-number}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{blogpost-id}/versions/{version-number}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "number": 27, "authorId": "<string>", "message": "<string>", "createdAt": "<string>", "minorEdit": true, "contentTypeModified": true, "collaborators": [ "<string>" ], "prevVersion": 71, "nextVersion": 68 }`

---

GET

## Get page versions

Returns the versions of specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the page and its corresponding space.

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

PrimaryBodyRepresentation

**cursor**

string

**max_results**

integer

**sort**

VersionSortOrder

### Responses

200OK

Returned if the requested page versions are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Version>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>", "page": { "title": "<string>", "id": "<string>", "body": {} } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get version details for page version

Retrieves version details for the specified page and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the page.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:page:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**page-id**

integer

Required

**version-number**

integer

Required

### Responses

200OK

Returned if the requested version details are successfully retrieved.

#### application/json

DetailedVersion

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{page-id}/versions/{version-number}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{page-id}/versions/{version-number}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "number": 27, "authorId": "<string>", "message": "<string>", "createdAt": "<string>", "minorEdit": true, "contentTypeModified": true, "collaborators": [ "<string>" ], "prevVersion": 71, "nextVersion": 68 }`

---

GET

## Get custom content versions

Returns the versions of specific custom content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content and its corresponding page and space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**custom-content-id**

integer

Required

#### Query parameters

Expand all

**body-format**

CustomContentBodyRepresentation

**cursor**

string

**max_results**

integer

**sort**

VersionSortOrder

### Responses

200OK

Returned if the requested custom content versions are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Version>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{custom-content-id}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{custom-content-id}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>", "custom": { "title": "<string>", "id": "<string>", "body": {} } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get version details for custom content version

Retrieves version details for the specified custom content and version number.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the page.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:custom-content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**custom-content-id**

integer

Required

**version-number**

integer

Required

### Responses

200OK

Returned if the requested version details are successfully retrieved.

#### application/json

DetailedVersion

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{custom-content-id}/versions/{version-number}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{custom-content-id}/versions/{version-number}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "number": 27, "authorId": "<string>", "message": "<string>", "createdAt": "<string>", "minorEdit": true, "contentTypeModified": true, "collaborators": [ "<string>" ], "prevVersion": 71, "nextVersion": 68 }`

---

GET

## Get footer comment versions

Retrieves the versions of the specified footer comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blog post and its corresponding space.

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

**max_results**

integer

**sort**

VersionSortOrder

### Responses

200OK

Returned if the requested footer comment versions are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Version>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/footer-comments/{id}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{id}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>", "comment": { "title": "<string>", "id": "<string>", "body": {} } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get version details for footer comment version

Retrieves version details for the specified footer comment version.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**version-number**

integer

Required

### Responses

200OK

Returned if the requested version details are successfully retrieved.

#### application/json

DetailedVersion

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/footer-comments/{id}/versions/{version-number}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{id}/versions/{version-number}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "number": 27, "authorId": "<string>", "message": "<string>", "createdAt": "<string>", "minorEdit": true, "contentTypeModified": true, "collaborators": [ "<string>" ], "prevVersion": 71, "nextVersion": 68 }`

---

GET

## Get inline comment versions

Retrieves the versions of the specified inline comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blog post and its corresponding space.

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

**max_results**

integer

**sort**

VersionSortOrder

### Responses

200OK

Returned if the requested inline comment versions are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Version>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/inline-comments/{id}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{id}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "results": [ { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>", "comment": { "title": "<string>", "id": "<string>", "body": {} } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get version details for inline comment version

Retrieves version details for the specified inline comment version.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page or blog post and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:comment:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**version-number**

integer

Required

### Responses

200OK

Returned if the requested version details are successfully retrieved.

#### application/json

DetailedVersion

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/inline-comments/{id}/versions/{version-number}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{id}/versions/{version-number}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "number": 27, "authorId": "<string>", "message": "<string>", "createdAt": "<string>", "minorEdit": true, "contentTypeModified": true, "collaborators": [ "<string>" ], "prevVersion": 71, "nextVersion": 68 }`