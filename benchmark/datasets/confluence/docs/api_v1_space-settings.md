# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-space-settings/*

---

Cloud

Confluence Cloud / Reference / REST API

# Space settings

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/space/{spaceKey}/settings](/cloud/confluence/rest/v1/api-group-space-settings/#api-wiki-rest-api-space-spacekey-settings-get)[PUT/wiki/rest/api/space/{spaceKey}/settings](/cloud/confluence/rest/v1/api-group-space-settings/#api-wiki-rest-api-space-spacekey-settings-put)

---

GET

## Get space settings

Returns the settings of a space. Currently only the `routeOverrideEnabled` setting can be returned.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-space.summary`

**Granular** :`read:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

### Responses

200OK

Returned if the space settings are returned.

#### application/json

SpaceSettings

Nullable: `true`

Show child properties

401Unauthorized

404Not Found

GET/wiki/rest/api/space/{spaceKey}/settings

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/settings`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "routeOverrideEnabled": true, "editor": { "page": "<string>", "blogpost": "<string>", "default": "<string>" }, "spaceKey": "<string>", "_links": {} }`

---

PUT

## Update space settings

Updates the settings for a space. Currently only the `routeOverrideEnabled` setting can be updated.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-space`

**Granular** :`read:space.setting:confluence`, `write:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Request bodyapplication/json

The space settings to update.

**routeOverrideEnabled**

boolean

### Responses

200OK

Returned if space settings are updated.

#### application/json

SpaceSettings

Nullable: `true`

Show child properties

401Unauthorized

404Not Found

PUT/wiki/rest/api/space/{spaceKey}/settings

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "routeOverrideEnabled": true }`; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/settings`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "routeOverrideEnabled": true, "editor": { "page": "<string>", "blogpost": "<string>", "default": "<string>" }, "spaceKey": "<string>", "_links": {} }`