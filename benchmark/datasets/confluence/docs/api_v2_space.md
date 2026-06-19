# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Space

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/spaces](/cloud/confluence/rest/v2/api-group-space/#api-spaces-get)[POST/spaces](/cloud/confluence/rest/v2/api-group-space/#api-spaces-post)[GET/spaces/{id}](/cloud/confluence/rest/v2/api-group-space/#api-spaces-id-get)

---

GET

## Get spaces

Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the `limit` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission). Only spaces that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**ids**

array<integer>

**keys**

array<string>

**type**

string

**status**

string

**labels**

array<string>

**favorited-by**

string

**not-favorited-by**

string

**sort**

SpaceSortOrder

**description-format**

SpaceDescriptionBodyRepresentation

**include-icon**

boolean

Show 2 hidden parameters

### Responses

200OK

Returned if the requested spaces are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<Space>

Show child properties

400Bad Request

401Unauthorized

GET/spaces

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``{ "results": [ { "id": "<string>", "key": "<string>", "name": "<string>", "type": "global", "status": "current", "authorId": "<string>", "currentActiveAlias": "<string>", "createdAt": "<string>", "homepageId": "<string>", "description": { "plain": {}, "view": {} }, "icon": { "path": "<string>", "apiDownloadLink": "<string>" }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

POST

## Create space

Creates a Space as specified in the payload.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to create spaces.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:space:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

**name**

string

Required

**key**

string

**alias**

string

**description**

object

**roleAssignments**

array<object>

**copySpaceAccessConfiguration**

integer

**createPrivateSpace**

boolean

**templateKey**

string

### Responses

201Created

Returned if the requested space is created.

#### application/json

allOf [SpaceBulk, object]

SpaceBulk

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

413Request Entity Too Large

POST/spaces

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "name": "<string>", "key": "<string>", "alias": "<string>", "description": { "value": "<string>", "representation": "<string>" }, "roleAssignments": [ { "principal": { "principalType": "USER", "principalId": "<string>" }, "roleId": "<string>" } ], "copySpaceAccessConfiguration": 64, "createPrivateSpace": true, "templateKey": "<string>" }`; const response = await requestConfluence(`/wiki/api/v2/spaces`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``{ "id": "<string>", "key": "<string>", "name": "<string>", "type": "global", "status": "current", "authorId": "<string>", "currentActiveAlias": "<string>", "createdAt": "<string>", "homepageId": "<string>", "description": { "plain": {}, "view": {} }, "icon": { "path": "<string>", "apiDownloadLink": "<string>" }, "_links": { "base": "<string>" } }`

---

GET

## Get space by id

Returns a specific space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the space.

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

#### Query parameters

Expand all

**description-format**

SpaceDescriptionBodyRepresentation

**include-icon**

boolean

**include-operations**

boolean

**include-properties**

boolean

**include-permissions**

boolean

**include-role-assignments**

boolean

**include-labels**

boolean

### Responses

200OK

Returned if the requested space is returned.

#### application/json

allOf [SpaceSingle, object]

SpaceSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 ``{ "id": "<string>", "key": "<string>", "name": "<string>", "type": "global", "status": "current", "authorId": "<string>", "createdAt": "<string>", "homepageId": "<string>", "description": { "plain": {}, "view": {} }, "icon": { "path": "<string>", "apiDownloadLink": "<string>" }, "labels": { "results": [ { "id": "<string>", "name": "<string>", "prefix": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "properties": { "results": [ { "id": "<string>", "key": "<string>", "createdAt": "<string>", "createdBy": "<string>", "version": { "createdAt": "<string>", "createdBy": "<string>", "message": "<string>", "number": 44 } } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "operations": { "results": [ { "operation": "<string>", "targetType": "<string>" } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "permissions": { "results": [ { "id": "<string>", "principal": { "type": "user", "id": "<string>" }, "operation": { "key": "use", "targetType": "page" } } ], "meta": { "hasMore": true, "cursor": "<string>" }, "_links": { "self": "<string>" } }, "_links": { "base": "<string>" } }`