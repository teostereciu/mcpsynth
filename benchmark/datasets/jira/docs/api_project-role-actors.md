# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-role-actors/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project role actors

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the users assigned to [project roles](/cloud/jira/platform/rest/v3/api-group-issue-comments/#api-group-issue-comments). Use it to get, add, and remove default users from project roles. Also use it to add and remove users from a project role associated with a project.

Operations

[PUT/rest/api/3/project/{projectIdOrKey}/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-project-projectidorkey-role-id-put)[POST/rest/api/3/project/{projectIdOrKey}/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-project-projectidorkey-role-id-post)[DEL/rest/api/3/project/{projectIdOrKey}/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-project-projectidorkey-role-id-delete)[GET/rest/api/3/role/{id}/actors](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-role-id-actors-get)[POST/rest/api/3/role/{id}/actors](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-role-id-actors-post)[DEL/rest/api/3/role/{id}/actors](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-role-id-actors-delete)

---

PUT

## Set actors for project role

Sets the actors for a project role for a project, replacing all existing actors.

To add actors to the project without overwriting the existing list, use [Add actors to project role](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-project-projectidorkey-role-id-post).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira`, `write:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**projectIdOrKey**

string

Required

**id**

integer

Required

#### Request bodyapplication/json

Expand all

The groups or users to associate with the project role for this project. Provide the user account ID, group name, or group ID. As a group's name can change, use of group ID is recommended.

**categorisedActors**

object

### Responses

200OK

Returned if the request is successful. The complete list of actors for the project is returned.

#### application/json

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/project/{projectIdOrKey}/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "categorisedActors": { "atlassian-group-role-actor-id": [ "952d12c3-5b5b-4d04-bb32-44d383afc4b2" ], "atlassian-user-role-actor": [ "12345678-9abc-def1-2345-6789abcdef12" ] } }`; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/role/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "accountId": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

POST

## Add actors to project role

Adds actors to a project role for the project.

To replace all actors for the project, use [Set actors for project role](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-project-projectidorkey-role-id-put).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira`, `write:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**projectIdOrKey**

string

Required

**id**

integer

Required

#### Request bodyapplication/json

Expand all

The groups or users to associate with the project role for this project. Provide the user account ID, group name, or group ID. As a group's name can change, use of group ID is recommended.

**group**

array<string>

**groupId**

array<string>

**user**

array<string>

### Responses

200OK

Returned if the request is successful. The complete list of actors for the project is returned.

For example, the cURL request above adds a group, _jira-developers_. For the response below to be returned as a result of that request, the user _Mia Krystof_ would have previously been added as a `user` actor for this project.

#### application/json

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/project/{projectIdOrKey}/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "groupId": [ "952d12c3-5b5b-4d04-bb32-44d383afc4b2" ] }`; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/role/{id}`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "accountId": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

DEL

## Delete actors from project role

Deletes actors from a project role for the project.

To remove default actors from the project role, use [Delete default actors from project role](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-role-id-actors-delete).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:project-role:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**projectIdOrKey**

string

Required

**id**

integer

Required

#### Query parameters

Expand all

**user**

string

**group**

string

**groupId**

string

### Responses

204No Content

Returned if the request is successful.

400Bad Request

404Not Found

DEL/rest/api/3/project/{projectIdOrKey}/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/role/{id}?user=5b10ac8d82e05b22cc7d4ef5`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get default actors for project role

Returns the [default actors](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-get) for the project role.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/role/{id}/actors

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/role/{id}/actors`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" } ] }`

---

POST

## Add default actors to project role

Adds [default actors](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-get) to a role. You may add groups or users, but you cannot add groups and users in the same request.

Changing a project role's default actors does not affect project role members for projects already created.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira`, `write:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

**group**

array<string>

**groupId**

array<string>

**user**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/role/{id}/actors

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "user": [ "admin" ] }`; const response = await requestJira(`/rest/api/3/role/{id}/actors`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" } ] }`

---

DEL

## Delete default actors from project role

Deletes the [default actors](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-get) from a project role. You may delete a group or user, but you cannot delete a group and a user in the same request.

Changing a project role's default actors does not affect project role members for projects already created.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project-role:jira`, `read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**user**

string

**groupId**

string

**group**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/role/{id}/actors

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/role/{id}/actors?user=5b10ac8d82e05b22cc7d4ef5`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" } ] }`