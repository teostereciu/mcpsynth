# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-categories/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project categories

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents project categories. Use it to create, update, and delete project categories as well as obtain a list of all project categories and details of individual categories. For more information on managing project categories, see [Adding, assigning, and deleting project categories](https://confluence.atlassian.com/x/-A5WMg).

Operations

[GET/rest/api/3/projectCategory](/cloud/jira/platform/rest/v3/api-group-project-categories/#api-rest-api-3-projectcategory-get)[POST/rest/api/3/projectCategory](/cloud/jira/platform/rest/v3/api-group-project-categories/#api-rest-api-3-projectcategory-post)[GET/rest/api/3/projectCategory/{id}](/cloud/jira/platform/rest/v3/api-group-project-categories/#api-rest-api-3-projectcategory-id-get)[PUT/rest/api/3/projectCategory/{id}](/cloud/jira/platform/rest/v3/api-group-project-categories/#api-rest-api-3-projectcategory-id-put)[DEL/rest/api/3/projectCategory/{id}](/cloud/jira/platform/rest/v3/api-group-project-categories/#api-rest-api-3-projectcategory-id-delete)

---

GET

## Get all project categories

Returns all project categories.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ProjectCategory>

Show child properties

401Unauthorized

GET/rest/api/3/projectCategory

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projectCategory`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``[ { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, { "description": "Second Project Category", "id": "10001", "name": "SECOND", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10001" } ]`

---

POST

## Create project category

Creates a project category.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project-category:jira`, `read:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

### Responses

201Created

Returned if the request is successful.

#### application/json

ProjectCategory

A project category.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

409Conflict

POST/rest/api/3/projectCategory

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Created Project Category", "name": "CREATED" }`; const response = await requestJira(`/rest/api/3/projectCategory`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 ``{ "description": "Created Project Category", "id": "10100", "name": "CREATED", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10100" }`

---

GET

## Get project category by ID

Returns a project category.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectCategory

A project category.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/projectCategory/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projectCategory/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }`

---

PUT

## Update project category

Updates a project category.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:project-category:jira`, `write:project-category:jira`

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

UpdatedProjectCategory

A project category.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/projectCategory/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Updated Project Category", "name": "UPDATED" }`; const response = await requestJira(`/rest/api/3/projectCategory/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "Updated Project Category", "id": "10100", "name": "UPDATED", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10100" }`

---

DEL

## Delete project category

Deletes a project category.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/projectCategory/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projectCategory/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`