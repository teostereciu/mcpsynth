# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space-permissions/*

---

Cloud

Confluence Cloud / Reference / REST API

# Space permissions

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[POST/wiki/rest/api/space/{spaceKey}/permission](/cloud/confluence/rest/v1/api-group-space-permissions/#api-wiki-rest-api-space-spacekey-permission-post)[POST/wiki/rest/api/space/{spaceKey}/permission/custom-content](/cloud/confluence/rest/v1/api-group-space-permissions/#api-wiki-rest-api-space-spacekey-permission-custom-content-post)[DEL/wiki/rest/api/space/{spaceKey}/permission/{id}](/cloud/confluence/rest/v1/api-group-space-permissions/#api-wiki-rest-api-space-spacekey-permission-id-delete)

---

POST

## Add new permission to space

Adds new permission to space.

If the permission to be added is a group permission, the group can be identified by its group name or group id.

Note: Apps cannot access this REST resource - including when utilizing user impersonation.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space.permission:confluence`, `write:space.permission:confluence`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**spaceKey**

string

Required

#### Request bodyapplication/json

Expand all

The permission to be created.

**subject**

PermissionSubject

Required

**operation**

object

Required

**_links**

GenericLinks

**Additional Properties**

any

### Responses

200OK

Returned if the requested content is returned.

#### application/json

SpacePermissionV2

This object represents a single space permission. Permissions consist of at least one operation object with an accompanying subjects object.

The following combinations of `operation.key` and `operation.target` values are valid for the `operation` object:


    1
    2
    3
    4
    5
    6
    7
    'create': 'page', 'blogpost', 'comment', 'attachment'
    'read': 'space'
    'delete': 'page', 'blogpost', 'comment', 'attachment', 'space'
    'export': 'space'
    'administer': 'space'
    'archive': 'page'
    'restrict_content': 'space'


For example, to enable Delete Own permission, set the `operation` object to the following:


    1
    2
    3
    4
    "operation": {
        "key": "delete",
        "target": "space"
    }


To enable Add/Delete Restrictions permissions, set the `operation` object to the following:


    1
    2
    3
    4
    "operation": {
        "key": "restrict_content",
        "target": "space"
    }


Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/wiki/rest/api/space/{spaceKey}/permission

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "subject": { "type": "user", "identifier": "<string>" }, "operation": { "key": "administer", "target": "page" }, "_links": {} }`; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/permission`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "id": 2154, "subject": { "type": "user", "identifier": "<string>" }, "operation": { "key": "administer", "target": "page" }, "_links": {} }`

---

POST

## Add new custom content permission to space

Adds new custom content permission to space.

If the permission to be added is a group permission, the group can be identified by its group name or group id.

Note: Only apps can access this REST resource and only make changes to the respective app permissions.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space.permission:confluence`, `write:space.permission:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Request bodyapplication/json

Expand all

The permissions to be created.

**subject**

PermissionSubject

Required

**operations**

array<object>

Required

### Responses

200OK

Returned if the requested content is returned.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/wiki/rest/api/space/{spaceKey}/permission/custom-content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "subject": { "type": "user", "identifier": "<string>" }, "operations": [ { "key": "read", "target": "<string>", "access": true } ] }`; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/permission/custom-content`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove a space permission

Removes a space permission. Note that removing Read Space permission for a user or group will remove all the space permissions for that user or group.

Note: Apps cannot access this REST resource - including when utilizing user impersonation.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:space.permission:confluence`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**spaceKey**

string

Required

**id**

integer

Required

### Responses

204No Content

Permission successfully removed.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/wiki/rest/api/space/{spaceKey}/permission/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/permission/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`