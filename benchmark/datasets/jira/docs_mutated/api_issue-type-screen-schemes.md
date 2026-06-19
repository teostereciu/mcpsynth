# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue type screen schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue type screen schemes. Use it to:

  * get issue type screen schemes and a list of the projects that use them.
  * create issue type screen schemes.
  * update issue type screen schemes.
  * delete issue type screen schemes.
  * associate issue type screen schemes with projects.
  * append issue type to screen scheme mappings to issue type screen schemes.
  * remove issue type to screen scheme mappings from issue type screen schemes.
  * update default screen scheme of issue type screen scheme.


Operations

[GET/rest/api/3/issuetypescreenscheme](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-get)[POST/rest/api/3/issuetypescreenscheme](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-post)[GET/rest/api/3/issuetypescreenscheme/mapping](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-mapping-get)[GET/rest/api/3/issuetypescreenscheme/project](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-project-get)[PUT/rest/api/3/issuetypescreenscheme/project](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-project-put)[PUT/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-issuetypescreenschemeid-put)[DEL/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-issuetypescreenschemeid-delete)[PUT/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-issuetypescreenschemeid-mapping-put)[PUT/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-issuetypescreenschemeid-mapping-default-put)[POST/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-issuetypescreenschemeid-mapping-remove-post)[GET/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project](/cloud/jira/platform/rest/v3/api-group-issue-type-screen-schemes/#api-rest-api-3-issuetypescreenscheme-issuetypescreenschemeid-project-get)

---

GET

## Get issue type screen schemes

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue type screen schemes.

Only issue type screen schemes used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type-screen-scheme:jira`

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

**orderBy**

string

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueTypeScreenScheme

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescreenscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescreenscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 2, "values": [ { "id": "1", "name": "Default Issue Type Screen Scheme", "description": "The default issue type screen scheme" }, { "id": "10000", "name": "Office issue type screen scheme", "description": "Managing office projects", "projects": { "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "avatarUrls": { "16x16": "secure/projectavatar?size=xsmall&pid=10000", "24x24": "secure/projectavatar?size=small&pid=10000", "32x32": "secure/projectavatar?size=medium&pid=10000", "48x48": "secure/projectavatar?size=large&pid=10000" }, "id": "10000", "key": "EX", "name": "Example", "projectCategory": { "description": "Project category description", "id": "10000", "name": "A project category" }, "projectTypeKey": "ProjectTypeKey{key='software'}", "self": "project/EX", "simplified": false } ] } } ] }`

---

POST

## Create issue type screen scheme

Creates an issue type screen scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

An issue type screen scheme bean.

**description**

string

**issueTypeMappings**

array<IssueTypeScreenSchemeMapping>

Required

**name**

string

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

IssueTypeScreenSchemeId

The ID of an issue type screen scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

POST/rest/api/3/issuetypescreenscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeMappings": [ { "issueTypeId": "default", "screenSchemeId": "10001" }, { "issueTypeId": "10001", "screenSchemeId": "10002" }, { "issueTypeId": "10002", "screenSchemeId": "10002" } ], "name": "Scrum issue type screen scheme" }`; const response = await requestJira(`/rest/api/3/issuetypescreenscheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": "10001" }`

---

GET

## Get issue type screen scheme items

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue type screen scheme items.

Only issue type screen schemes used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**issueTypeScreenSchemeId**

array<integer>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueTypeScreenSchemeItem

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescreenscheme/mapping

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/mapping`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 4, "values": [ { "issueTypeId": "10000", "issueTypeScreenSchemeId": "10020", "screenSchemeId": "10010" }, { "issueTypeId": "10001", "issueTypeScreenSchemeId": "10021", "screenSchemeId": "10010" }, { "issueTypeId": "10002", "issueTypeScreenSchemeId": "10022", "screenSchemeId": "10010" }, { "issueTypeId": "default", "issueTypeScreenSchemeId": "10023", "screenSchemeId": "10011" } ] }`

---

GET

## Get issue type screen schemes for projects

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it.

Only issue type screen schemes used in classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**projectId**

array<integer>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueTypeScreenSchemesProjects

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescreenscheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/project?projectId={projectId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "issueTypeScreenScheme": { "id": "1", "name": "Default Issue Type Screen Scheme", "description": "The default issue type screen scheme" }, "projectIds": [ "10000", "10001" ] } ] }`

---

PUT

## Assign issue type screen scheme to project

Assigns an issue type screen scheme to a project.

Issue type screen schemes can only be assigned to classic projects.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-screen-scheme:jira`, `write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**issueTypeScreenSchemeId**

string

**projectId**

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

PUT/rest/api/3/issuetypescreenscheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeScreenSchemeId": "10001", "projectId": "10002" }`; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/project`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Update issue type screen scheme

Updates an issue type screen scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeScreenSchemeId**

string

Required

#### Request bodyapplication/json

Expand all

The issue type screen scheme update details.

**description**

string

**name**

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

PUT/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Screens for scrum issue types.", "name": "Scrum scheme" }`; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete issue type screen scheme

Deletes an issue type screen scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeScreenSchemeId**

string

Required

### Responses

204No Content

Returned if the issue type screen scheme is deleted.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Append mappings to issue type screen scheme

Appends issue type to screen scheme mappings to an issue type screen scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeScreenSchemeId**

string

Required

#### Request bodyapplication/json

**issueTypeMappings**

array<IssueTypeScreenSchemeMapping>

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

409Conflict

PUT/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeMappings": [ { "issueTypeId": "10000", "screenSchemeId": "10001" }, { "issueTypeId": "10001", "screenSchemeId": "10002" }, { "issueTypeId": "10002", "screenSchemeId": "10002" } ] }`; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Update issue type screen scheme default screen scheme

Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeScreenSchemeId**

string

Required

#### Request bodyapplication/json

**screenSchemeId**

string

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

PUT/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "screenSchemeId": "10010" }`; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Remove mappings from issue type screen scheme

Removes issue type to screen scheme mappings from an issue type screen scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type-screen-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeScreenSchemeId**

string

Required

#### Request bodyapplication/json

**issueTypeIds**

array<string>

Required

### Responses

204No Content

Returned if the screen scheme mappings are removed from the issue type screen scheme.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypeIds": [ "10000", "10001", "10004" ] }`; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get issue type screen scheme projects

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of projects associated with an issue type screen scheme.

Only company-managed projects associated with an issue type screen scheme are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:project:jira`, `read:avatar:jira`, `read:project-category:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueTypeScreenSchemeId**

integer

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**query**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanProjectDetails

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "avatarUrls": { "16x16": "secure/projectavatar?size=xsmall&pid=10000", "24x24": "secure/projectavatar?size=small&pid=10000", "32x32": "secure/projectavatar?size=medium&pid=10000", "48x48": "secure/projectavatar?size=large&pid=10000" }, "id": "10000", "key": "EX", "name": "Example", "projectCategory": { "description": "Project category description", "id": "10000", "name": "A project category" }, "projectTypeKey": "ProjectTypeKey{key='software'}", "self": "project/EX", "simplified": false } ] }`