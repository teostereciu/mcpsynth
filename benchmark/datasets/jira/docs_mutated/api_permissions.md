# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permissions/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Permissions

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents permissions. Use it to obtain details of all permissions and determine whether the user has certain permissions.

Operations

[GET/rest/api/3/mypermissions](/cloud/jira/platform/rest/v3/api-group-permissions/#api-rest-api-3-mypermissions-get)[GET/rest/api/3/permissions](/cloud/jira/platform/rest/v3/api-group-permissions/#api-rest-api-3-permissions-get)[POST/rest/api/3/permissions/check](/cloud/jira/platform/rest/v3/api-group-permissions/#api-rest-api-3-permissions-check-post)[POST/rest/api/3/permissions/project](/cloud/jira/platform/rest/v3/api-group-permissions/#api-rest-api-3-permissions-project-post)

---

GET

## Get my permissions

Returns a list of permissions indicating which permissions the user has. Details of the user's permissions can be obtained in a global, project, issue or comment context.

The user is reported as having a project permission:

  * in the global context, if the user has the project permission in any project.
  * for a project, where the project permission is determined using issue data, if the user meets the permission's criteria for any issue in the project. Otherwise, if the user has the project permission in the project.
  * for an issue, where a project permission is determined using issue data, if the user has the permission in the issue. Otherwise, if the user has the project permission in the project containing the issue.
  * for a comment, where the user has both the permission to browse the comment and the project permission for the comment's parent issue. Only the BROWSE_PROJECTS permission is supported. If a `commentId` is provided whose `permissions` does not equal BROWSE_PROJECTS, a 400 error will be returned.


This means that users may be shown as having an issue permission (such as EDIT_ISSUES) in the global context or a project context but may not have the permission for any or all issues. For example, if Reporters have the EDIT_ISSUES permission a user would be shown as having this permission in the global context or the context of a project, because any user can be a reporter. However, if they are not the user who reported the issue queried they would not have EDIT_ISSUES permission for that issue.

For [Jira Service Management project permissions](https://support.atlassian.com/jira-cloud-administration/docs/customize-jira-service-management-permissions/), this will be evaluated similarly to a user in the customer portal. For example, if the BROWSE_PROJECTS permission is granted to Service Project Customer - Portal Access, any users with access to the customer portal will have the BROWSE_PROJECTS permission.

Global permissions are unaffected by context.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:permission:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**projectKey**

string

**projectId**

string

**issueKey**

string

**issueId**

string

**permissions**

string

**projectUuid**

string

**projectConfigurationUuid**

string

**commentId**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Permissions

Details about permissions.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/mypermissions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/mypermissions?permissions=BROWSE_PROJECTS%2CEDIT_ISSUES`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "permissions": { "EDIT_ISSUES": { "description": "Ability to edit issues.", "havePermission": true, "id": "12", "key": "EDIT_ISSUES", "name": "Edit Issues", "type": "PROJECT" } } }`

---

GET

## Get all permissions

Returns all permissions, including:

  * global permissions.
  * project permissions.
  * global permissions added by plugins.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:permission:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

Permissions

Details about permissions.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/permissions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissions`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "permissions": { "BULK_CHANGE": { "description": "Ability to modify a collection of issues at once. For example, resolve multiple issues in one step.", "key": "BULK_CHANGE", "name": "Bulk Change", "type": "GLOBAL" } } }`

---

POST

## Get bulk permissions

Returns:

  * for a list of global permissions, the global permissions granted to a user.
  * for a list of project permissions and lists of projects and issues, for each project permission a list of the projects and issues a user can access or manipulate.


If no account ID is provided, the operation returns details for the logged in user.

Note that:

  * Invalid project and issue IDs are ignored.
  * A maximum of 1000 projects and 1000 issues can be checked.
  * Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and `projectPermissions.issues` are ignored.
  * Empty strings in `projectPermissions.permissions` are ignored.


**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

  * **Classic** : `read:jira-work`
  * **Granular** : `read:permission:jira`


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users, otherwise none. However, Connect apps can make a call from the app server to the product to obtain permission details for any user, without admin permission. This Connect app ability doesn't apply to calls made using AP.request() in a browser.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:permission:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

Expand all

Details of the permissions to check.

**user_id**

string

**globalPermissions**

array<string>

**projectPermissions**

array<BulkProjectPermissions>

### Responses

200OK

Returned if the request is successful.

#### application/json

BulkPermissionGrants

Details of global and project permissions granted to the user.

Show child properties

400Bad Request

403Forbidden

POST/rest/api/3/permissions/check

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "user_id": "5b10a2844c20165700ede21g", "globalPermissions": [ "ADMINISTER" ], "projectPermissions": [ { "issues": [ 10010, 10011, 10012, 10013, 10014 ], "permissions": [ "EDIT_ISSUES" ], "projects": [ 10001 ] } ] }`; const response = await requestJira(`/rest/api/3/permissions/check`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``{ "globalPermissions": [ "ADMINISTER" ], "projectPermissions": [ { "issues": [ 10010, 10013, 10014 ], "permission": "EDIT_ISSUES", "projects": [ 10001 ] } ] }`

---

POST

## Get permitted projects

Returns all the projects where the user is granted a list of project permissions.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:permission:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

**permissions**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PermittedProjects

A list of projects in which a user is granted permissions.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/permissions/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "permissions": [ "<string>" ] }`; const response = await requestJira(`/rest/api/3/permissions/project`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "projects": [ { "id": 22, "key": "<string>" } ] }`