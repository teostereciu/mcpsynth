# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-watches/*

---

Cloud

Confluence Cloud / Reference / REST API

# Content watches

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/content/{id}/notification/child-created](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-content-id-notification-child-created-get)[GET/wiki/rest/api/content/{id}/notification/created](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-content-id-notification-created-get)[GET/wiki/rest/api/space/{spaceKey}/watch](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-space-spacekey-watch-get)[GET/wiki/rest/api/user/watch/content/{contentId}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-content-contentid-get)[POST/wiki/rest/api/user/watch/content/{contentId}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-content-contentid-post)[DEL/wiki/rest/api/user/watch/content/{contentId}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-content-contentid-delete)[GET/wiki/rest/api/user/watch/label/{labelName}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-label-labelname-get)[POST/wiki/rest/api/user/watch/label/{labelName}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-label-labelname-post)[DEL/wiki/rest/api/user/watch/label/{labelName}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-label-labelname-delete)[GET/wiki/rest/api/user/watch/space/{spaceKey}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-space-spacekey-get)[POST/wiki/rest/api/user/watch/space/{spaceKey}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-space-spacekey-post)[DEL/wiki/rest/api/user/watch/space/{spaceKey}](/cloud/confluence/rest/v1/api-group-content-watches/#api-wiki-rest-api-user-watch-space-spacekey-delete)

---

GET

## Get watches for page

Returns the watches for a page. A user that watches a page will receive receive notifications when the page is updated.

If you want to manage watches for a page, use the following `user` methods:

  * [Get content watch status for user]()
  * [Add content watch]()
  * [Remove content watch]()


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:watcher:confluence`, `read:user:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested watches are returned.

#### application/json

WatchArray

Show child properties

401Unauthorized

GET/wiki/rest/api/content/{id}/notification/child-created

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/notification/child-created`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``{ "results": [ { "type": "<string>", "watcher": { "type": "<string>", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "externalCollaborator": true, "isGuest": true, "isExternalCollaborator": true, "details": {}, "accountType": "<string>", "email": "<string>", "publicName": "<string>", "personalSpace": {} }, "contentId": 2154 } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

GET

## Get watches for space

Returns all space watches for the space that the content is in. A user that watches a space will receive receive notifications when any content in the space is updated.

If you want to manage watches for a space, use the following `user` methods:

  * [Get space watch status for user]()
  * [Add space watch]()
  * [Remove space watch]()


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:watcher:confluence`, `read:user:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested watches are returned.

#### application/json

SpaceWatchArray

Show child properties

401Unauthorized

GET/wiki/rest/api/content/{id}/notification/created

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/notification/created`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "results": [ { "type": "<string>", "watcher": { "type": "<string>", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "externalCollaborator": true, "isGuest": true, "isExternalCollaborator": true, "details": {}, "accountType": "<string>", "email": "<string>", "publicName": "<string>", "personalSpace": {} }, "spaceKey": "<string>", "labelName": "<string>", "prefix": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

GET

## Get space watchers

Returns a list of watchers of a space

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:watcher:confluence`, `read:user:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**start**

string

**limit**

string

### Responses

200OK

Returned if watchers list is returned.

#### application/json

SpaceWatchArray

Show child properties

404Not Found

GET/wiki/rest/api/space/{spaceKey}/watch

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/watch`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "results": [ { "type": "<string>", "watcher": { "type": "<string>", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "externalCollaborator": true, "isGuest": true, "isExternalCollaborator": true, "details": {}, "accountType": "<string>", "email": "<string>", "publicName": "<string>", "personalSpace": {} }, "spaceKey": "<string>", "labelName": "<string>", "prefix": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

GET

## Get content watch status

Returns whether a user is watching a piece of content. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**contentId**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

200OK

Returned if the requested watch status is returned.

#### application/json

UserWatch

Show child properties

403Forbidden

404Not Found

GET/wiki/rest/api/user/watch/content/{contentId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/content/{contentId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "watching": true }`

---

POST

## Add content watcher

Adds a user as a watcher to a piece of content. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


Note, you must add the `X-Atlassian-Token: no-check` header when making a request, as this operation has XSRF protection.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**contentId**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

204No Content

Returned if the watcher was successfully created. No response body is returned.

403Forbidden

404Not Found

POST/wiki/rest/api/user/watch/content/{contentId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/content/{contentId}`, { method: 'POST' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove content watcher

Removes a user as a watcher from a piece of content. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**contentId**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

#### Header parameters

**X-Atlassian-Token**

string

Required

### Responses

204No Content

Returned if the watcher was successfully deleted. No response body is returned.

403Forbidden

404Not Found

DEL/wiki/rest/api/user/watch/content/{contentId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/content/{contentId}`, { method: 'DELETE', headers: { 'X-Atlassian-Token': '<X-Atlassian-Token>' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get label watch status

Returns whether a user is watching a label. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**labelName**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

200OK

Returned if the requested watch status is returned.

#### application/json

UserWatch

Show child properties

403Forbidden

404Not Found

GET/wiki/rest/api/user/watch/label/{labelName}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/label/{labelName}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "watching": true }`

---

POST

## Add label watcher

Adds a user as a watcher to a label. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


Note, you must add the `X-Atlassian-Token: no-check` header when making a request, as this operation has XSRF protection.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**labelName**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

#### Header parameters

**X-Atlassian-Token**

string

Required

### Responses

204No Content

Returned if the watcher was successfully created. No response body is returned.

403Forbidden

404Not Found

POST/wiki/rest/api/user/watch/label/{labelName}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/label/{labelName}`, { method: 'POST', headers: { 'X-Atlassian-Token': '<X-Atlassian-Token>' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove label watcher

Removes a user as a watcher from a label. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**labelName**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

204No Content

Returned if the watcher was successfully deleted. No response body is returned.

403Forbidden

404Not Found

DEL/wiki/rest/api/user/watch/label/{labelName}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/label/{labelName}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get space watch status

Returns whether a user is watching a space. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

200OK

Returned if the requested watch status is returned.

#### application/json

UserWatch

Show child properties

403Forbidden

404Not Found

GET/wiki/rest/api/user/watch/space/{spaceKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/space/{spaceKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "watching": true }`

---

POST

## Add space watcher

Adds a user as a watcher to a space. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


Note, you must add the `X-Atlassian-Token: no-check` header when making a request, as this operation has XSRF protection.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

#### Header parameters

**X-Atlassian-Token**

string

Required

### Responses

204No Content

Returned if the watcher was successfully created. No response body is returned.

403Forbidden

404Not Found

POST/wiki/rest/api/user/watch/space/{spaceKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/space/{spaceKey}`, { method: 'POST', headers: { 'X-Atlassian-Token': '<X-Atlassian-Token>' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove space watch

Removes a user as a watcher from a space. Choose the user by doing one of the following:

  * Specify a user via a query parameter: Use the `accountId` to identify the user.
  * Do not specify a user: The currently logged-in user will be used.


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission if specifying a user, otherwise permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:watcher:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

204No Content

Returned if the watcher was successfully deleted. No response body is returned.

403Forbidden

404Not Found

DEL/wiki/rest/api/user/watch/space/{spaceKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/watch/space/{spaceKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`