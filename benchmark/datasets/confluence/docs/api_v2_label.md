# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-label/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Label

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/attachments/{id}/labels](/cloud/confluence/rest/v2/api-group-label/#api-attachments-id-labels-get)[GET/blogposts/{id}/labels](/cloud/confluence/rest/v2/api-group-label/#api-blogposts-id-labels-get)[GET/custom-content/{id}/labels](/cloud/confluence/rest/v2/api-group-label/#api-custom-content-id-labels-get)[GET/labels](/cloud/confluence/rest/v2/api-group-label/#api-labels-get)[GET/pages/{id}/labels](/cloud/confluence/rest/v2/api-group-label/#api-pages-id-labels-get)[GET/spaces/{id}/labels](/cloud/confluence/rest/v2/api-group-label/#api-spaces-id-labels-get)[GET/spaces/{id}/content/labels](/cloud/confluence/rest/v2/api-group-label/#api-spaces-id-content-labels-get)

---

GET

## Get labels for attachment

Returns the labels of specific attachment. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the parent content of the attachment and its corresponding space. Only labels that the user has permission to view will be returned.

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

**prefix**

string

**sort**

string

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/attachments/{id}/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/attachments/{id}/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get labels for blog post

Returns the labels of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the blog post and its corresponding space. Only labels that the user has permission to view will be returned.

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

**prefix**

string

**sort**

string

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/blogposts/{id}/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/blogposts/{id}/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get labels for custom content

Returns the labels for a specific piece of custom content. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the custom content and its corresponding space. Only labels that the user has permission to view will be returned.

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

**prefix**

string

**sort**

string

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/custom-content/{id}/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/custom-content/{id}/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get labels

Returns all labels. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission). Only labels that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:label:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**label-id**

array<integer>

**prefix**

array<string>

**cursor**

string

**sort**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

GET/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get labels for page

Returns the labels of specific page. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content of the page and its corresponding space. Only labels that the user has permission to view will be returned.

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

**prefix**

string

**sort**

string

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/pages/{id}/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/pages/{id}/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get labels for space

Returns the labels of specific space. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the space. Only labels that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**prefix**

string

**sort**

string

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get labels for space content

Returns the labels of space content (pages, blogposts etc). The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the space. Only labels that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**prefix**

string

**sort**

string

**cursor**

string

**limit**

integer

### Responses

200OK

Returned if the requested labels are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Label>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}/content/labels

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}/content/labels`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "_links": { "next": "<string>", "base": "<string>" } }`