# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permission-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Permission schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents permission schemes. Use it to get, create, update, and delete permission schemes as well as get, create, update, and delete details of the permissions granted in those schemes.

Operations

[GET/rest/api/3/permissionscheme](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-get)[POST/rest/api/3/permissionscheme](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-post)[GET/rest/api/3/permissionscheme/{schemeId}](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-get)[PUT/rest/api/3/permissionscheme/{schemeId}](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-put)[DEL/rest/api/3/permissionscheme/{schemeId}](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-delete)[GET/rest/api/3/permissionscheme/{schemeId}/permission](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-permission-get)[POST/rest/api/3/permissionscheme/{schemeId}/permission](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-permission-post)[GET/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-permission-permissionid-get)[DEL/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-permission-permissionid-delete)

---

GET

## Get all permission schemes

Returns all permission schemes.

### About permission schemes and grants

A permission scheme is a collection of permission grants. A permission grant consists of a `holder` and a `permission`.

#### Holder object

The `holder` object contains information about the user or group being granted the permission. For example, the _Administer projects_ permission is granted to a group named _Teams in space administrators_. In this case, the type is `"type": "group"`, and the parameter is the group name, `"parameter": "Teams in space administrators"` and the value is group ID, `"value": "ca85fac0-d974-40ca-a615-7af99c48d24f"`.

The `holder` object is defined by the following properties:

  * `type` Identifies the user or group (see the list of types below).
  * `parameter` As a group's name can change, use of `value` is recommended. The value of this property depends on the `type`. For example, if the `type` is a group, then you need to specify the group name.
  * `value` The value of this property depends on the `type`. If the `type` is a group, then you need to specify the group ID. For other `type` it has the same value as `parameter`


The following `types` are available. The expected values for `parameter` and `value` are given in parentheses (some types may not have a `parameter` or `value`):

  * `anyone` Grant for anonymous users.
  * `applicationRole` Grant for users with access to the specified application (application name, application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL) for more information.
  * `assignee` Grant for the user currently assigned to an issue.
  * `group` Grant for the specified group (`parameter` : group name, `value` : group ID).
  * `groupCustomField` Grant for a user in the group selected in the specified custom field (`parameter` : custom field ID, `value` : custom field ID).
  * `projectLead` Grant for a project lead.
  * `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` : project role ID).
  * `reporter` Grant for the user who reported the issue.
  * `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the customer portal but not Jira. See [Customizing Jira Service Desk permissions](https://confluence.atlassian.com/x/24dKLg) for more information.
  * `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey but that is deprecated and the account ID should be used, `value` : user ID).
  * `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom field ID, `value` : custom field ID).


#### Built-in permissions

The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps can also define custom permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information.

**Administration permissions**

  * `ADMINISTER_PROJECTS`
  * `EDIT_WORKFLOW`
  * `EDIT_ISSUE_LAYOUT`


**Project permissions**

  * `BROWSE_PROJECTS`
  * `MANAGE_SPRINTS_PERMISSION` (Jira Software only)
  * `SERVICEDESK_AGENT` (Jira Service Desk only)
  * `VIEW_DEV_TOOLS` (Jira Software only)
  * `VIEW_READONLY_WORKFLOW`


**Issue permissions**

  * `ASSIGNABLE_USER`
  * `ASSIGN_ISSUES`
  * `CLOSE_ISSUES`
  * `CREATE_ISSUES`
  * `DELETE_ISSUES`
  * `EDIT_ISSUES`
  * `LINK_ISSUES`
  * `MODIFY_REPORTER`
  * `MOVE_ISSUES`
  * `RESOLVE_ISSUES`
  * `SCHEDULE_ISSUES`
  * `SET_ISSUE_SECURITY`
  * `TRANSITION_ISSUES`


**Voters and watchers permissions**

  * `MANAGE_WATCHERS`
  * `VIEW_VOTERS_AND_WATCHERS`


**Comments permissions**

  * `ADD_COMMENTS`
  * `DELETE_ALL_COMMENTS`
  * `DELETE_OWN_COMMENTS`
  * `EDIT_ALL_COMMENTS`
  * `EDIT_OWN_COMMENTS`


**Attachments permissions**

  * `CREATE_ATTACHMENTS`
  * `DELETE_ALL_ATTACHMENTS`
  * `DELETE_OWN_ATTACHMENTS`


**Time tracking permissions**

  * `DELETE_ALL_WORKLOGS`
  * `DELETE_OWN_WORKLOGS`
  * `EDIT_ALL_WORKLOGS`
  * `EDIT_OWN_WORKLOGS`
  * `WORK_ON_ISSUES`


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission-scheme:jira`, `read:permission:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PermissionSchemes

List of all permission schemes.

Show child properties

401Unauthorized

GET/rest/api/3/permissionscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissionscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "permissionSchemes": [ { "description": "description", "id": 10000, "name": "Example permission scheme", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000" } ] }`

---

POST

## Create permission scheme

Creates a new permission scheme. You can create a permission scheme with or without defining a set of permission grants.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:permission-scheme:jira`, `read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission-scheme:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

**expand**

string

#### Request bodyapplication/json

Expand all

The permission scheme to create.

**description**

string

**name**

string

Required

**permissions**

array<PermissionGrant>

**scope**

Scope

**Additional Properties**

any

### Responses

201Created

Returned if the permission scheme is created.

#### application/json

PermissionScheme

Details of a permission scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/permissionscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "description", "name": "Example permission scheme", "permissions": [ { "holder": { "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "permission": "ADMINISTER_PROJECTS" } ] }`; const response = await requestJira(`/rest/api/3/permissionscheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "description": "description", "id": 10000, "name": "Example permission scheme", "permissions": [ { "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "id": 10000, "permission": "ADMINISTER_PROJECTS", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000" } ], "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000" }`

---

GET

## Get permission scheme

Returns a permission scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission-scheme:jira`, `read:permission:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**schemeId**

integer

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

404Not Found

GET/rest/api/3/permissionscheme/{schemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "description": "description", "id": 10000, "name": "Example permission scheme", "permissions": [ { "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "id": 10000, "permission": "ADMINISTER_PROJECTS", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000" } ], "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000" }`

---

PUT

## Update permission scheme

Updates a permission scheme. Below are some important things to note when using this resource:

  * If a permissions list is present in the request, then it is set in the permission scheme, overwriting _all existing_ grants.
  * If you want to update only the name and description, then do not send a permissions list in the request.
  * Sending an empty list will remove all permission grants from the permission scheme.


If you want to add or delete a permission grant instead of updating the whole list, see [Create permission grant](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-permission-post) or [Delete permission scheme entity](/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-schemeid-permission-permissionid-delete).

See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:permission-scheme:jira`, `read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission-scheme:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**schemeId**

integer

Required

#### Query parameters

**expand**

string

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

Required

**permissions**

array<PermissionGrant>

**scope**

Scope

**Additional Properties**

any

### Responses

200OK

Returned if the scheme is updated.

#### application/json

PermissionScheme

Details of a permission scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/permissionscheme/{schemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "description", "name": "Example permission scheme", "permissions": [ { "holder": { "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "permission": "ADMINISTER_PROJECTS" } ] }`; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "description": "description", "id": 10000, "name": "Example permission scheme", "permissions": [ { "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "id": 10000, "permission": "ADMINISTER_PROJECTS", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000" } ], "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000" }`

---

DEL

## Delete permission scheme

Deletes a permission scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:permission-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**schemeId**

integer

Required

### Responses

204No Content

Returned if the permission scheme is deleted.

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/permissionscheme/{schemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get permission scheme grants

Returns all permission grants for a permission scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**schemeId**

integer

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PermissionGrants

List of permission grants.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/permissionscheme/{schemeId}/permission

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}/permission`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "expand": "user,group,projectRole,field,all", "permissions": [ { "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "id": 10000, "permission": "ADMINISTER_PROJECTS", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000" } ] }`

---

POST

## Create permission grant

Creates a permission grant in a permission scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**schemeId**

integer

Required

#### Query parameters

**expand**

string

#### Request bodyapplication/json

Expand all

The permission grant to create.

**holder**

PermissionHolder

**permission**

string

**Additional Properties**

any

### Responses

201Created

Returned if the scheme permission is created.

#### application/json

PermissionGrant

Details about a permission granted to a user or group.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/permissionscheme/{schemeId}/permission

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "holder": { "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "permission": "ADMINISTER_PROJECTS" }`; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}/permission`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "id": 10000, "permission": "ADMINISTER_PROJECTS", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000" }`

---

GET

## Get permission scheme grant

Returns a permission grant.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:application-role:jira`, `read:field:jira`, `read:group:jira`, `read:permission:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**schemeId**

integer

Required

**permissionId**

integer

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PermissionGrant

Details about a permission granted to a user or group.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "ca85fac0-d974-40ca-a615-7af99c48d24f" }, "id": 10000, "permission": "ADMINISTER_PROJECTS", "self": "https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000" }`

---

DEL

## Delete permission scheme grant

Deletes a permission grant from a permission scheme. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:permission:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**schemeId**

integer

Required

**permissionId**

integer

Required

### Responses

204No Content

Returned if the permission grant is deleted.

400Bad Request

401Unauthorized

403Forbidden

DEL/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`