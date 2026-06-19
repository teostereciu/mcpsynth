# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Screen tab fields

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the screen tab fields used to record issue details. Use it to get, add, move, and remove fields from screen tabs.

Operations

[GET/rest/api/3/screens/{screenId}/tabs/{tabId}/fields](/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/#api-rest-api-3-screens-screenid-tabs-tabid-fields-get)[POST/rest/api/3/screens/{screenId}/tabs/{tabId}/fields](/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/#api-rest-api-3-screens-screenid-tabs-tabid-fields-post)[DEL/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}](/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/#api-rest-api-3-screens-screenid-tabs-tabid-fields-id-delete)[POST/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move](/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/#api-rest-api-3-screens-screenid-tabs-tabid-fields-id-move-post)

---

GET

## Get all screen tab fields

Returns all fields for a screen tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screenable-field:jira`

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

#### Query parameters

**projectKey**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ScreenableField>

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/screens/{screenId}/tabs/{tabId}/fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}/fields`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``[ { "id": "<string>", "name": "<string>" } ]`

---

POST

## Add screen tab field

Adds a field to a screen tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:screenable-field:jira`, `write:screenable-field:jira`

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

**fieldId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ScreenableField

A screen tab field.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/screens/{screenId}/tabs/{tabId}/fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "fieldId": "summary" }`; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}/fields`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "id": "summary", "name": "Summary" }`

---

DEL

## Remove screen tab field

Removes a field from a screen tab.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:screenable-field:jira`

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

**id**

string

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Move screen tab field

Moves a screen tab field.

If `after` and `position` are provided in the request, `position` is ignored.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:screenable-field:jira`

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

**id**

string

Required

#### Request bodyapplication/json

Expand all

**after**

string

**position**

string

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "after": "<string>", "position": "Earlier" }`; const response = await requestJira(`/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`