# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-versions/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project versions

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents project versions. Use it to get, get lists of, create, update, move, merge, and delete project versions. This resource also provides counts of issues by version.

Operations

[GET/rest/api/3/project/{projectIdOrKey}/version](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-project-projectidorkey-version-get)[GET/rest/api/3/project/{projectIdOrKey}/versions](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-project-projectidorkey-versions-get)[POST/rest/api/3/version](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-post)[GET/rest/api/3/version/{id}](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-get)[PUT/rest/api/3/version/{id}](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-put)[DEL/rest/api/3/version/{id}](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-delete)[PUT/rest/api/3/version/{id}/mergeto/{moveIssuesTo}](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-mergeto-moveissuesto-put)[POST/rest/api/3/version/{id}/move](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-move-post)[GET/rest/api/3/version/{id}/relatedIssueCounts](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-relatedissuecounts-get)[GET/rest/api/3/version/{id}/relatedwork](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-relatedwork-get)[PUT/rest/api/3/version/{id}/relatedwork](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-relatedwork-put)[POST/rest/api/3/version/{id}/relatedwork](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-relatedwork-post)[POST/rest/api/3/version/{id}/removeAndSwap](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-removeandswap-post)[GET/rest/api/3/version/{id}/unresolvedIssueCount](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-unresolvedissuecount-get)[DEL/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-versionid-relatedwork-relatedworkid-delete)

---

GET

## Get project versions paginated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of all versions in a project. See the [Get project versions](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-project-projectidorkey-versions-get) resource if you want to get a full list of versions without pagination.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**orderBy**

string

**query**

string

**status**

string

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanVersion

A page of items.

Show child properties

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/version

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/version`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``{ "isLast": false, "page_size": 2, "nextPage": "https://your-domain.atlassian.net/rest/api/3/project/PR/version?start_index=2&page_size=2", "self": "https://your-domain.atlassian.net/rest/api/3/project/PR/version?start_index=0&page_size=2", "start_index": 0, "total": 7, "values": [ { "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "overdue": true, "projectId": 10000, "releaseDate": "2010-07-06", "released": true, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000", "userReleaseDate": "6/Jul/2010" }, { "archived": false, "description": "Minor Bugfix version", "id": "10010", "issuesStatusForFixVersion": { "done": 100, "inProgress": 20, "toDo": 10, "unmapped": 0 }, "name": "Next Version", "overdue": false, "projectId": 10000, "released": false, "self": "https://your-domain.atlassian.net/rest/api/3/version/10010" } ] }`

---

GET

## Get project versions

Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-project-projectidorkey-version-get) if you want to get the versions in a project with pagination.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Version>

Show child properties

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/versions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/versions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``[ { "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "overdue": true, "projectId": 10000, "releaseDate": 1278385482288, "releaseDateSet": true, "released": true, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000", "startDateSet": false, "userReleaseDate": "6/Jul/2010" }, { "archived": false, "description": "Minor Bugfix version", "id": "10010", "issuesStatusForFixVersion": { "done": 100, "inProgress": 20, "toDo": 10, "unmapped": 0 }, "name": "Next Version", "overdue": false, "projectId": 10000, "releaseDateSet": false, "released": false, "self": "https://your-domain.atlassian.net/rest/api/3/version/10010", "startDateSet": false } ]`

---

POST

## Create version

Creates a project version.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the version is added to.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project-version:jira`, `read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**archived**

boolean

**description**

string

**driver**

string

**expand**

string

**moveUnfixedIssuesTo**

string

**name**

string

**project**

string

**projectId**

integer

**releaseDate**

string

**released**

boolean

Show 1 hidden parameters

### Responses

201Created

Returned if the request is successful.

#### application/json

Version

Details about a project version.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/version

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "archived": false, "description": "An excellent version", "name": "New Version 1", "projectId": 10000, "releaseDate": "2010-07-06", "released": true }`; const response = await requestJira(`/rest/api/3/version`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "project": "PXA", "projectId": 10000, "releaseDate": "2010-07-06", "released": true, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000", "userReleaseDate": "6/Jul/2010" }`

---

GET

## Get version

Returns a project version.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Version

Details about a project version.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/version/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "overdue": true, "projectId": 10000, "releaseDate": "2010-07-06", "released": true, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000", "userReleaseDate": "6/Jul/2010" }`

---

PUT

## Update version

Updates a project version.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project-version:jira`, `read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**archived**

boolean

**description**

string

**driver**

string

**expand**

string

**moveUnfixedIssuesTo**

string

**name**

string

**project**

string

**projectId**

integer

**releaseDate**

string

**released**

boolean

Show 1 hidden parameters

### Responses

200OK

Returned if the request is successful.

#### application/json

Version

Details about a project version.

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/version/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "overdue": true, "projectId": 10000, "releaseDate": "2010-07-06", "released": true, "self": "https://your-domain.atlassian.net/rest/api/~ver~/version/10000", "userReleaseDate": "6/Jul/2010" }`; const response = await requestJira(`/rest/api/3/version/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "project": "PXA", "projectId": 10000, "releaseDate": "2010-07-06", "released": true, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000", "userReleaseDate": "6/Jul/2010" }`

---

DEL

## Delete versionDeprecated

Deletes a project version.

Deprecated, use [ Delete and replace version](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-removeandswap-post) that supports swapping version values in custom include_fields, in addition to the swapping for `fixVersion` and `affectedVersion` provided in this resource.

Alternative versions can be provided to update issues that use the deleted version in `fixVersion` or `affectedVersion`. If alternatives are not provided, occurrences of `fixVersion` and `affectedVersion` that contain the deleted version are cleared.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**moveFixIssuesTo**

string

**moveAffectedIssuesTo**

string

### Responses

204No Content

Returned if the version is deleted.

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/version/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

PUT

## Merge versions

Merges two project versions. The merge is completed by deleting the version specified in `id` and replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.

Consider using [ Delete and replace version](/cloud/jira/platform/rest/v3/api-group-project-versions/#api-rest-api-3-version-id-removeandswap-post) instead. This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom include_fields.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:project-version:jira`, `write:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**id**

string

Required

**moveIssuesTo**

string

Required

### Responses

204No Content

Returned if the version is deleted.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/version/{id}/mergeto/{moveIssuesTo}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{id}/mergeto/{moveIssuesTo}`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Move version

Modifies the version's sequence within the project, which affects the display order of the versions in Jira.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ project permission for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project-version:jira`, `read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

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

200OK

Returned if the request is successful.

#### application/json

Version

Details about a project version.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/version/{id}/move

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "after": "https://your-domain.atlassian.net/rest/api/~ver~/version/10000" }`; const response = await requestJira(`/rest/api/3/version/{id}/move`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "archived": false, "description": "An excellent version", "id": "10000", "name": "New Version 1", "overdue": true, "projectId": 10000, "releaseDate": "2010-07-06", "released": true, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000", "userReleaseDate": "6/Jul/2010" }`

---

GET

## Get version's related issues count

Returns the following counts for a version:

  * Number of issues where the `fixVersion` is set to the version.
  * Number of issues where the `affectedVersion` is set to the version.
  * Number of issues where a version custom field is set to the version.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ project permission for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

VersionIssueCounts

Various counts of issues within a version.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/version/{id}/relatedIssueCounts

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{id}/relatedIssueCounts`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``{ "customFieldUsage": [ { "customFieldId": 10000, "fieldName": "Field1", "issueCountWithVersionInCustomField": 2 }, { "customFieldId": 10010, "fieldName": "Field2", "issueCountWithVersionInCustomField": 3 } ], "issueCountWithCustomFieldsShowingVersion": 54, "issuesAffectedCount": 101, "issuesFixedCount": 23, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000" }`

---

GET

## Get related work

Returns related work items for the given version id.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<VersionRelatedWork>

Show child properties

401Unauthorized

404Not Found

500Internal Server Error

GET/rest/api/3/version/{id}/relatedwork

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{id}/relatedwork`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``[ { "category": "Design", "issueId": 10001, "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd", "title": "Design link", "url": "https://www.atlassian.com" }, { "category": "Communications", "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abce", "title": "Chat application", "url": "https://www.atlassian.com" }, { "category": "External Link", "issueId": 10003, "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcf", "url": "https://www.atlassian.com" } ]`

---

PUT

## Update related work

Updates the given related work. You can only update generic link related works via Rest APIs. Any archived version related works can't be edited.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Resolve issues:_ and _Edit issues_ [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**category**

string

Required

**title**

string

**url**

string

### Responses

200OK

Returned if the request is successful together with updated related work.

#### application/json

VersionRelatedWork

Associated related work to a version

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/version/{id}/relatedwork

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "category": "Design", "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd", "title": "Design link", "url": "https://www.atlassian.com" }`; const response = await requestJira(`/rest/api/3/version/{id}/relatedwork`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "category": "Design", "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd", "title": "Design link", "url": "https://www.atlassian.com" }`

---

POST

## Create related work

Creates a related work for the given version. You can only create a generic link type of related works via this API. relatedWorkId will be auto-generated UUID, that does not need to be provided.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Resolve issues:_ and _Edit issues_ [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**category**

string

Required

**title**

string

**url**

string

### Responses

201Created

Returned if the request is successful.

#### application/json

VersionRelatedWork

Associated related work to a version

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/version/{id}/relatedwork

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "category": "Design", "title": "Design link", "url": "https://www.atlassian.com" }`; const response = await requestJira(`/rest/api/3/version/{id}/relatedwork`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 ``{ "category": "Design", "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd", "title": "Design link", "url": "https://www.atlassian.com" }`

---

POST

## Delete and replace version

Deletes a project version.

Alternative versions can be provided to update issues that use the deleted version in `fixVersion`, `affectedVersion`, or any version picker custom include_fields. If alternatives are not provided, occurrences of `fixVersion`, `affectedVersion`, and any version picker custom field, that contain the deleted version, are cleared. Any replacement version must be in the same project as the version being deleted and cannot be the version being deleted.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:project-version:jira`, `write:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**customFieldReplacementList**

array<CustomFieldReplacement>

**moveAffectedIssuesTo**

integer

**moveFixIssuesTo**

integer

### Responses

204No Content

Returned if the version is deleted.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/version/{id}/removeAndSwap

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "customFieldReplacementList": [ { "customFieldId": 66, "moveTo": 67 } ], "moveAffectedIssuesTo": 97, "moveFixIssuesTo": 92 }`; const response = await requestJira(`/rest/api/3/version/{id}/removeAndSwap`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get version's unresolved issues count

Returns counts of the issues and unresolved issues for the project version.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ project permission for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-version:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

VersionUnresolvedIssuesCount

Count of a version's unresolved issues.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/version/{id}/unresolvedIssueCount

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{id}/unresolvedIssueCount`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "issuesCount": 30, "issuesUnresolvedCount": 23, "self": "https://your-domain.atlassian.net/rest/api/3/version/10000" }`

---

DEL

## Delete related work

Deletes the given related work for the given version.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Resolve issues:_ and _Edit issues_ [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**versionId**

string

Required

**relatedWorkId**

string

Required

### Responses

204No Content

Returned if the related work is deleted.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`