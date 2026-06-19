# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Screen schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents screen schemes in classic projects. Use it to get, create, update, and delete screen schemes.

Operations

[GET/rest/api/3/screenscheme](/cloud/jira/platform/rest/v3/api-group-screen-schemes/#api-rest-api-3-screenscheme-get)[POST/rest/api/3/screenscheme](/cloud/jira/platform/rest/v3/api-group-screen-schemes/#api-rest-api-3-screenscheme-post)[PUT/rest/api/3/screenscheme/{screenSchemeId}](/cloud/jira/platform/rest/v3/api-group-screen-schemes/#api-rest-api-3-screenscheme-screenschemeid-put)[DEL/rest/api/3/screenscheme/{screenSchemeId}](/cloud/jira/platform/rest/v3/api-group-screen-schemes/#api-rest-api-3-screenscheme-screenschemeid-delete)

---

GET

## Get screen schemes

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of screen schemes.

Only screen schemes used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen-scheme:jira`, `read:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**id**

array<integer>

**expand**

string

**queryString**

string

**orderBy**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanScreenScheme

A page of items.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/screenscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screenscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``{ "isLast": true, "page_size": 100, "self": "https://your-domain.atlassian.net/rest/api/3/screenscheme?page_size=25&start_index=0", "start_index": 0, "total": 2, "values": [ { "id": 10010, "name": "Employee screen scheme", "description": "Manage employee data", "screens": { "default": 10017, "edit": 10019, "create": 10019, "view": 10020 }, "issueTypeScreenSchemes": { "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "id": "10000", "name": "Office issue type screen scheme", "description": "Managing office projects" } ] } }, { "id": 10032, "name": "Office screen scheme", "description": "Manage office data", "screens": { "default": 10020 } } ] }`

---

POST

## Create screen scheme

Creates a screen scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

Required

**screens**

ScreenTypes

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

ScreenSchemeId

The ID of a screen scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/screenscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Manage employee data", "name": "Employee screen scheme", "screens": { "default": 10017, "edit": 10019, "view": 10020 } }`; const response = await requestJira(`/rest/api/3/screenscheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": 10001 }`

---

PUT

## Update screen scheme

Updates a screen scheme. Only screen schemes used in classic projects can be updated.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenSchemeId**

string

Required

#### Request bodyapplication/json

Expand all

The screen scheme update details.

**description**

string

**name**

string

**screens**

UpdateScreenTypes

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/screenscheme/{screenSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "name": "Employee screen scheme v2", "screens": { "create": "10019", "default": "10018" } }`; const response = await requestJira(`/rest/api/3/screenscheme/{screenSchemeId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete screen scheme

Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme.

Only screens schemes used in classic projects can be deleted.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenSchemeId**

string

Required

### Responses

204No Content

Returned if the screen scheme is deleted.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/screenscheme/{screenSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screenscheme/{screenSchemeId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`