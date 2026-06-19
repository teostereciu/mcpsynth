# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-roles/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project roles

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the roles that users can play in projects. Use this resource to get, create, update, and delete project roles.

Operations

[GET/rest/api/3/project/{projectIdOrKey}/role](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-project-projectidorkey-role-get)[GET/rest/api/3/project/{projectIdOrKey}/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-project-projectidorkey-role-id-get)[GET/rest/api/3/project/{projectIdOrKey}/roledetails](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-project-projectidorkey-roledetails-get)[GET/rest/api/3/role](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-get)[POST/rest/api/3/role](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-post)[GET/rest/api/3/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-id-get)[PUT/rest/api/3/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-id-put)[POST/rest/api/3/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-id-post)[DEL/rest/api/3/role/{id}](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-id-delete)

---

GET

## Get project roles for project

Returns a list of [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) for the project returning the name and self URL for each role.

Note that all project roles are shared with all projects in Jira Cloud. See [Get all project roles](/cloud/jira/platform/rest/v3/api-group-project-roles/#api-rest-api-3-role-get) for more information.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-role:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

object

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/role

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/role`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "Administrators": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10002", "Developers": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10000", "Users": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10001" }`

---

GET

## Get project role for project

Returns a project role's details and actors associated with the project. The list of actors is sorted by display name.

To check whether a user belongs to a role based on their group memberships, use [Get user](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-get) with the `groups` expand parameter selected. Then check whether the user keys and groups match with the actors returned for the project.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

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

**excludeInactiveUsers**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/role/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

GET

## Get project role details

Returns all [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) and the details for each role. Note that the list of project roles is common to all projects.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-category:jira`, `read:project-role:jira`, `read:project:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Query parameters

Expand all

**currentMember**

boolean

**excludeConnectAddons**

boolean

**excludeOtherServiceRoles**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ProjectRoleDetails>

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/roledetails

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/roledetails`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``[ { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "admin": false, "default": true, "roleConfigurable": true, "translatedName": "Developers", "type": "DEFAULT" } ]`

---

GET

## Get all project roles

Gets a list of all project roles, complete with project role details and default actors.

### About project roles

[Project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) are a flexible way to to associate users and groups with projects. In Jira Cloud, the list of project roles is shared globally with all projects, but each project can have a different set of actors associated with it (unlike groups, which have the same membership throughout all Jira applications).

Project roles are used in [permission schemes](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-get), [email notification schemes](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-get), [issue security levels](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-get), [comment visibility](/cloud/jira/platform/rest/v3/api-group-issue-comments/#api-rest-api-3-comment-list-post), and workflow conditions.

#### Members and actors

In the Jira REST API, a member of a project role is called an _actor_. An _actor_ is a group or user associated with a project role.

Actors may be set as [default members](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/#Specifying-'default-members'-for-a-project-role) of the project role or set at the project level:

  * Default actors: Users and groups that are assigned to the project role for all newly created projects. The default actors can be removed at the project level later if desired.
  * Actors: Users and groups that are associated with a project role for a project, which may differ from the default actors. This enables you to assign a user to different roles in different projects.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project-role:jira`, `read:project:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ProjectRole>

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/role

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/role`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``[ { "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" } ]`

---

POST

## Create project role

Creates a new project role with no [default actors](/cloud/jira/platform/rest/v3/api-group-issue-resolutions/#api-rest-api-3-resolution-get). You can use the [Add default actors to project role](/cloud/jira/platform/rest/v3/api-group-project-role-actors/#api-rest-api-3-role-id-actors-post) operation to add default actors to the project role after creating it.

_Note that although a new project role is available to all projects upon creation, any default actors that are associated with the project role are not added to projects that existed prior to the role being created._ <

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project:jira`, `write:project-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

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

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

409Conflict

POST/rest/api/3/role

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A project role that represents developers in a project", "name": "Developers" }`; const response = await requestJira(`/rest/api/3/role`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

GET

## Get project role by ID

Gets the project role details and the default actors associated with the role. The list of default actors is sorted by display name.

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

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/role/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

PUT

## Fully update project role

Updates the project role's name and description. You must include both a name and a description in the request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project:jira`, `write:project-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

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

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A project role that represents developers in a project", "name": "Developers" }`; const response = await requestJira(`/rest/api/3/role/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

POST

## Partial update project role

Updates either the project role's name or its description.

You cannot update both the name and description at the same time using this operation. If you send a request with a name and a description only the name is updated.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user:jira`, `read:group:jira`, `read:project:jira`, `write:project-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

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

ProjectRole

Details about the roles in a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A project role that represents developers in a project", "name": "Developers" }`; const response = await requestJira(`/rest/api/3/role/{id}`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``{ "actors": [ { "actorGroup": { "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2", "name": "jira-developers" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor", "user": "jira-developers" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "description": "A project role that represents developers in a project", "id": 10360, "name": "Developers", "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360" }`

---

DEL

## Delete project role

Deletes a project role. You must specify a replacement project role if you wish to delete a project role that is in use.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:project-role:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**swap**

integer

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

DEL/rest/api/3/role/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/role/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`