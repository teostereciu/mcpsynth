# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-operation/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Operation

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/attachments/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-attachments-id-operations-get)[GET/blogposts/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-blogposts-id-operations-get)[GET/custom-content/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-custom-content-id-operations-get)[GET/pages/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-pages-id-operations-get)[GET/whiteboards/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-whiteboards-id-operations-get)[GET/databases/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-databases-id-operations-get)[GET/embeds/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-embeds-id-operations-get)[GET/folders/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-folders-id-operations-get)[GET/spaces/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-spaces-id-operations-get)[GET/footer-comments/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-footer-comments-id-operations-get)[GET/inline-comments/{id}/operations](/cloud/confluence/rest/v2/api-group-operation/#api-inline-comments-id-operations-get)

---

GET

## Get permitted operations for attachment

Returns the permitted operations on specific attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the attachment and its corresponding space.

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

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for blog post

Returns the permitted operations on specific blog post.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the blog post and its corresponding space.

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

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for custom content

Returns the permitted operations on specific custom content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the custom content and its corresponding space.

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

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for page

Returns the permitted operations on specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the page and its corresponding space.

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

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for a whiteboard

Returns the permitted operations on specific whiteboard.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the whiteboard and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:whiteboard:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/whiteboards/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/whiteboards/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for a database

Returns the permitted operations on specific database.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the database and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:database:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/databases/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/databases/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for a Smart Link in the content tree

Returns the permitted operations on specific Smart Link in the content tree.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the Smart Link in the content tree and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:embed:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/embeds/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/embeds/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for a folder

Returns the permitted operations on specific folder.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the folder and its corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:folder:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/folders/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/folders/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for space

Returns the permitted operations on specific space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the corresponding space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for footer comment

Returns the permitted operations on specific footer comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the footer comment and its corresponding space.

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

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/footer-comments/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/footer-comments/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`

---

GET

## Get permitted operations for inline comment

Returns the permitted operations on specific inline comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the inline comment and its corresponding space.

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

### Responses

200OK

Returned if the requested operations are returned.

#### application/json

PermittedOperationsResponse

The list of operations permitted on entity.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/inline-comments/{id}/operations

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/inline-comments/{id}/operations`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "operations": [ { "operation": "<string>", "targetType": "<string>" } ] }`