# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project permission schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents permission schemes for a project. Use this resource to:

  * get details of a project's issue security levels available to the calling user.
  * get the permission scheme associated with the project or assign different permission scheme to the project.
  * get details of a project's issue security scheme.


See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes.

Operations

[GET/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme](/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/#api-rest-api-3-project-projectkeyorid-issuesecuritylevelscheme-get)[GET/rest/api/3/project/{projectKeyOrId}/permissionscheme](/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/#api-rest-api-3-project-projectkeyorid-permissionscheme-get)[PUT/rest/api/3/project/{projectKeyOrId}/permissionscheme](/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/#api-rest-api-3-project-projectkeyorid-permissionscheme-put)[GET/rest/api/3/project/{projectKeyOrId}/securitylevel](/cloud/jira/platform/rest/v3/api-group-project-permission-schemes/#api-rest-api-3-project-projectkeyorid-securitylevel-get)

---

GET

## Get project issue security scheme

Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or the _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-security-level:jira`, `read:issue-security-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectKeyOrId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

SecurityScheme

Details about a security scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "defaultSecurityLevelId": 10021, "description": "Description for the default issue security scheme", "id": 10000, "levels": [ { "description": "Only the reporter and internal staff can see this issue.", "id": "10021", "name": "Reporter Only", "self": "https://your-domain.atlassian.net/rest/api/3/securitylevel/10021" } ], "name": "Default Issue Security Scheme", "self": "https://your-domain.atlassian.net/rest/api/3/issuesecurityschemes/10000" }`

---

GET

## Get assigned permission scheme

Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission-scheme:jira`, `read:permission:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectKeyOrId**

string

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PermissionScheme

Details of a permission scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/project/{projectKeyOrId}/permissionscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectKeyOrId}/permissionscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "description", "id": 10000, "name": "Example permission scheme", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000" }`

---

PUT

## Assign permission scheme

Assigns a permission scheme with a project. See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg)

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission-scheme:jira`, `read:permission:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectKeyOrId**

string

Required

#### Query parameters

**expand**

string

#### Request bodyapplication/json

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PermissionScheme

Details of a permission scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/project/{projectKeyOrId}/permissionscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "id": 10000 }`; const response = await requestJira(`/rest/api/3/project/{projectKeyOrId}/permissionscheme`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "description", "id": 10000, "name": "Example permission scheme", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000" }`

---

GET

## Get project issue security levels

Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with _Set Issue Security_ [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-security-level:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectKeyOrId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectIssueSecurityLevels

List of issue level security items in a project.

Show child properties

404Not Found

GET/rest/api/3/project/{projectKeyOrId}/securitylevel

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectKeyOrId}/securitylevel`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "levels": [ { "description": "Only the reporter and internal staff can see this issue.", "id": "100000", "name": "Reporter Only", "self": "https://your-domain.atlassian.net/rest/api/3/securitylevel/100000" }, { "description": "Only internal staff can see this issue.", "id": "100001", "name": "Staff Only", "self": "https://your-domain.atlassian.net/rest/api/3/securitylevel/100001" } ] }`