# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Whiteboard

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[POST/whiteboards](/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-post)[GET/whiteboards/{id}](/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get)[DEL/whiteboards/{id}](/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-delete)

---

POST

## Create whiteboard

Creates a whiteboard in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the corresponding space. Permission to create a whiteboard in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:whiteboard:confluence`

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

**title**

string

**parentId**

string

**templateKey**

string

**locale**

string

### Responses

200OK

Returned if the whiteboard was successfully created.

#### application/json

allOf [WhiteboardSingle, object]

WhiteboardSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

413Request Entity Too Large

POST/whiteboards

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "spaceId": "<string>", "title": "<string>", "parentId": "<string>", "templateKey": "2x2-prioritization", "locale": "de-DE" }`; const response = await requestConfluence(`/wiki/api/v2/whiteboards`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``{ "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "parentId": "<string>", "parentType": "page", "position": 61, "authorId": "<string>", "ownerId": "<string>", "createdAt": "<string>", "spaceId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "base": "<string>" } }`

---

GET

## Get whiteboard by id

Returns a specific whiteboard.

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

#### Query parameters

Expand all

**include-collaborators**

boolean

**include-direct-children**

boolean

**include-operations**

boolean

**include-properties**

boolean

### Responses

200OK

Returned if the requested whiteboard is returned.

#### application/json

allOf [WhiteboardSingle, object]

WhiteboardSingle

Show child properties

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/whiteboards/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/whiteboards/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``{ "id": "<string>", "type": "<string>", "status": "current", "title": "<string>", "parentId": "<string>", "parentType": "page", "position": 61, "authorId": "<string>", "ownerId": "<string>", "createdAt": "<string>", "spaceId": "<string>", "version": { "createdAt": "<string>", "message": "<string>", "number": 19, "minorEdit": true, "authorId": "<string>" }, "_links": { "base": "<string>" } }`

---

DEL

## Delete whiteboard

Delete a whiteboard by id.

Deleting a whiteboard moves the whiteboard to the trash, where it can be restored later

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the whiteboard and its corresponding space. Permission to delete whiteboards in the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`delete:whiteboard:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

integer

Required

### Responses

204No Content

Returned if the whiteboard was successfully deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/whiteboards/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/whiteboards/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`