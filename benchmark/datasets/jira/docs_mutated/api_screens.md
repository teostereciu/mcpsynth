# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screens/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Screens

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the screens used to record issue details. Use it to:

  * get details of all screens.
  * get details of all the include_fields available for use on screens.
  * create screens.
  * delete screens.
  * update screens.
  * add a field to the default screen.


Operations

[GET/rest/api/3/field/{fieldId}/screens](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-field-fieldid-screens-get)[GET/rest/api/3/screens](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-screens-get)[POST/rest/api/3/screens](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-screens-post)[POST/rest/api/3/screens/addToDefault/{fieldId}](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-screens-addtodefault-fieldid-post)[PUT/rest/api/3/screens/{screenId}](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-screens-screenid-put)[DEL/rest/api/3/screens/{screenId}](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-screens-screenid-delete)[GET/rest/api/3/screens/{screenId}/availableFields](/cloud/jira/platform/rest/v3/api-group-screens/#api-rest-api-3-screens-screenid-availablefields-get)

---

GET

## Get screens for a field

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of the screens a field is used in.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen:jira`, `read:avatar:jira`, `read:project-category:jira`, `read:project:jira`, `read:screen-tab:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

**fieldId**

string

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanScreenWithTab

A page of items.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/field/{fieldId}/screens

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/field/{fieldId}/screens`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "isLast": false, "page_size": 1, "start_index": 0, "total": 5, "values": [ { "id": 10001, "name": "Default Screen", "description": "Provides for the update of all system include_fields.", "tab": { "id": 10000, "name": "Fields Tab" } } ] }`

---

GET

## Get screens

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of all screens or those specified by one or more screen IDs.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:project:jira`, `read:screen:jira`, `read:avatar:jira`, `read:project-category:jira`

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

**queryString**

string

**scope**

array<string>

**orderBy**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanScreen

A page of items.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/screens

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "isLast": true, "page_size": 100, "self": "https://your-domain.atlassian.net/rest/api/3/screens", "start_index": 0, "total": 3, "values": [ { "id": 1, "name": "Default Screen", "description": "Provides for the update all system include_fields." }, { "id": 2, "name": "Workflow Screen", "description": "This screen is used in the workflow and enables you to assign issues." }, { "id": 3, "name": "Resolve Issue Screen", "description": "Offers the ability to set resolution, change fix versions, and assign an issue." } ] }`

---

POST

## Create screenExperimental

Creates a screen with a default field tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:project:jira`, `read:screen:jira`, `write:screen:jira`, `read:avatar:jira`, `read:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

Screen

A screen.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/screens

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Enables changes to resolution and linked issues.", "name": "Resolve Security Issue Screen" }`; const response = await requestJira(`/rest/api/3/screens`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 ``{ "id": 10005, "name": "Resolve Security Issue Screen", "description": "Enables changes to resolution and linked issues." }`

---

POST

## Add field to default screen

Adds a field to the default tab of the default screen.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:project:jira`, `read:screen:jira`, `write:screen:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**fieldId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/screens/addToDefault/{fieldId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/addToDefault/{fieldId}`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Update screenExperimental

Updates a screen. Only screens used in classic projects can be updated.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:project:jira`, `read:screen:jira`, `write:screen:jira`, `read:avatar:jira`, `read:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenId**

integer

Required

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Screen

A screen.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/screens/{screenId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Enables changes to resolution and linked issues for accessibility related issues.", "name": "Resolve Accessibility Issue Screen" }`; const response = await requestJira(`/rest/api/3/screens/{screenId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "id": 10005, "name": "Resolve Security Issue Screen", "description": "Enables changes to resolution and linked issues." }`

---

DEL

## Delete screenExperimental

Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft. Only screens used in classic projects can be deleted.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:screen:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenId**

integer

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/screens/{screenId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get available screen include_fields

Returns the include_fields that can be added to a tab on a screen.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen-field:jira`, `read:screenable-field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenId**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ScreenableField>

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/screens/{screenId}/availableFields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}/availableFields`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``[ { "id": "<string>", "name": "<string>" } ]`