# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-themes/*

---

Cloud

Confluence Cloud / Reference / REST API

# Themes

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/settings/theme](/cloud/confluence/rest/v1/api-group-themes/#api-wiki-rest-api-settings-theme-get)[GET/wiki/rest/api/settings/theme/selected](/cloud/confluence/rest/v1/api-group-themes/#api-wiki-rest-api-settings-theme-selected-get)[GET/wiki/rest/api/settings/theme/{themeKey}](/cloud/confluence/rest/v1/api-group-themes/#api-wiki-rest-api-settings-theme-themekey-get)[GET/wiki/rest/api/space/{spaceKey}/theme](/cloud/confluence/rest/v1/api-group-themes/#api-wiki-rest-api-space-spacekey-theme-get)[PUT/wiki/rest/api/space/{spaceKey}/theme](/cloud/confluence/rest/v1/api-group-themes/#api-wiki-rest-api-space-spacekey-theme-put)[DEL/wiki/rest/api/space/{spaceKey}/theme](/cloud/confluence/rest/v1/api-group-themes/#api-wiki-rest-api-space-spacekey-theme-delete)

---

GET

## Get themes

Returns all themes, not including the default theme.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested themes are returned.

#### application/json

ThemeArray

Show child properties

GET/wiki/rest/api/settings/theme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/settings/theme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "results": [ { "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true } } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

GET

## Get global theme

Returns the globally assigned theme.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the global theme is returned.

#### application/json

Theme

Show child properties

404Not Found

GET/wiki/rest/api/settings/theme/selected

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/settings/theme/selected`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "_links": {} }`

---

GET

## Get theme

Returns a theme. This includes information about the theme name, description, and icon.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**themeKey**

string

Required

### Responses

200OK

Returned if the requested theme is returned.

#### application/json

Theme

Show child properties

404Not Found

GET/wiki/rest/api/settings/theme/{themeKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/settings/theme/{themeKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "_links": {} }`

---

GET

## Get space theme

Returns the theme selected for a space, if one is set. If no space theme is set, this means that the space is inheriting the global look and feel settings.

**[Permissions required](https://confluence.atlassian.com/x/_AozKw)** : âViewâ permission for the space.

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

Returned if the requested theme is returned.

#### application/json

Theme

Show child properties

404Not Found

GET/wiki/rest/api/space/{spaceKey}/theme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/theme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "_links": {} }`

---

PUT

## Set space theme

Sets the theme for a space. Note, if you want to reset the space theme to the default Confluence theme, use the 'Reset space theme' method instead of this method.

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

**themeKey**

string

Required

### Responses

200OK

Returned if the theme was set for the space.

#### application/json

Theme

Show child properties

403Forbidden

404Not Found

PUT/wiki/rest/api/space/{spaceKey}/theme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "themeKey": "<string>" }`; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/theme`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "_links": {} }`

---

DEL

## Reset space theme

Resets the space theme. This means that the space will inherit the global look and feel settings

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-space`

**Granular** :`write:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**spaceKey**

string

Required

### Responses

204No Content

Returned if the theme was reset for the space.

404Not Found

DEL/wiki/rest/api/space/{spaceKey}/theme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/theme`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`