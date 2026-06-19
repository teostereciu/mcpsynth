# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tabs/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Screen tabs

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the screen tabs used to record issue details. Use it to get, create, update, move, and delete screen tabs.

Operations

[GET/rest/api/3/screens/tabs](/cloud/jira/platform/rest/v3/api-group-screen-tabs/#api-rest-api-3-screens-tabs-get)[GET/rest/api/3/screens/{screenId}/tabs](/cloud/jira/platform/rest/v3/api-group-screen-tabs/#api-rest-api-3-screens-screenid-tabs-get)[POST/rest/api/3/screens/{screenId}/tabs](/cloud/jira/platform/rest/v3/api-group-screen-tabs/#api-rest-api-3-screens-screenid-tabs-post)[PUT/rest/api/3/screens/{screenId}/tabs/{tabId}](/cloud/jira/platform/rest/v3/api-group-screen-tabs/#api-rest-api-3-screens-screenid-tabs-tabid-put)[DEL/rest/api/3/screens/{screenId}/tabs/{tabId}](/cloud/jira/platform/rest/v3/api-group-screen-tabs/#api-rest-api-3-screens-screenid-tabs-tabid-delete)[POST/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}](/cloud/jira/platform/rest/v3/api-group-screen-tabs/#api-rest-api-3-screens-screenid-tabs-tabid-move-pos-post)

---

GET

## Get bulk screen tabsExperimental

Returns the list of tabs for a bulk of screens.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen-tab:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**screenId**

array<integer>

**tabId**

array<integer>

**startAt**

integer

**maxResult**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/screens/tabs

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/tabs`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``{ "isLast": true, "maxResults": 100, "startAt": 0, "total": 2, "values": [ { "screenId": 10000, "tabId": 10001, "tabName": "My Custom Tab 1" }, { "screenId": 10001, "tabId": 10002, "tabName": "My Custom Tab 2" } ] }`

---

GET

## Get all screen tabs

Returns the list of tabs for a screen.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen-tab:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenId**

integer

Required

#### Query parameters

**projectKey**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ScreenableTab>

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/screens/{screenId}/tabs

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``[ { "id": 25, "name": "<string>" } ]`

---

POST

## Create screen tab

Creates a tab for a screen.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen-tab:jira`, `write:screen-tab:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**screenId**

integer

Required

#### Request bodyapplication/json

Expand all

**name**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ScreenableTab

A screen tab.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/screens/{screenId}/tabs

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "name": "Fields Tab" }`; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "id": 10000, "name": "Fields Tab" }`

---

PUT

## Update screen tab

Updates the name of a screen tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screen-tab:jira`, `write:screen-tab:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**screenId**

integer

Required

**tabId**

integer

Required

#### Request bodyapplication/json

Expand all

**name**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ScreenableTab

A screen tab.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/screens/{screenId}/tabs/{tabId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "name": "<string>" }`; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "id": 10000, "name": "Fields Tab" }`

---

DEL

## Delete screen tab

Deletes a screen tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:screen-tab:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**screenId**

integer

Required

**tabId**

integer

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/screens/{screenId}/tabs/{tabId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Move screen tab

Moves a screen tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:screen:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**screenId**

integer

Required

**tabId**

integer

Required

**pos**

integer

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`