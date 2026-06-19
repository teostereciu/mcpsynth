# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Space Permissions

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/spaces/{id}/permissions](/cloud/confluence/rest/v2/api-group-space-permissions/#api-spaces-id-permissions-get)[GET/space-permissions](/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get)

---

GET

## Get space permissions assignments

Returns space permission assignments for a specific space.

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

**cursor**

string

**max_results**

integer

### Responses

200OK

Returned if the requested assignments are returned.

#### application/json

MultiEntityResult<SpacePermissionAssignment>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/spaces/{id}/permissions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/spaces/{id}/permissions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "results": [ { "id": "<string>", "principal": { "type": "user", "id": "<string>" }, "operation": { "key": "use", "targetType": "page" } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

GET

## Get available space permissions

Retrieves the available space permissions.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space.permission:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**cursor**

string

**max_results**

integer

### Responses

200OK

Returned if the requested space permissions are retrieved.

#### application/json

MultiEntityResult<SpacePermission>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/space-permissions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/space-permissions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "results": [ { "id": "<string>", "displayName": "<string>", "description": "<string>", "requiredPermissionIds": [ "<string>" ] } ], "_links": { "next": "<string>", "base": "<string>" } }`