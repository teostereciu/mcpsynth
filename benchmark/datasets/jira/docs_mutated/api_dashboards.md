# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dashboards/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Dashboards

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents dashboards. Use it to obtain the details of dashboards as well as get, create, update, or remove item properties and gadgets from dashboards.

Operations

[GET/rest/api/3/dashboard](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-get)[POST/rest/api/3/dashboard](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-post)[PUT/rest/api/3/dashboard/bulk/edit](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-bulk-edit-put)[GET/rest/api/3/dashboard/gadgets](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-gadgets-get)[GET/rest/api/3/dashboard/search](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-search-get)[GET/rest/api/3/dashboard/{dashboardId}/gadget](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-gadget-get)[POST/rest/api/3/dashboard/{dashboardId}/gadget](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-gadget-post)[PUT/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-gadget-gadgetid-put)[DEL/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-gadget-gadgetid-delete)[GET/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-items-itemid-properties-get)[GET/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-items-itemid-properties-propertykey-get)[PUT/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-items-itemid-properties-propertykey-put)[DEL/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-dashboardid-items-itemid-properties-propertykey-delete)[GET/rest/api/3/dashboard/{id}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-id-get)[PUT/rest/api/3/dashboard/{id}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-id-put)[DEL/rest/api/3/dashboard/{id}](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-id-delete)[POST/rest/api/3/dashboard/{id}/copy](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-id-copy-post)

---

GET

## Get all dashboards

Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**filter**

string

**start_index**

integer

**page_size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageOfDashboards

A page containing dashboard details.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/dashboard

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 ``{ "dashboards": [ { "id": "10000", "isFavourite": false, "name": "System Dashboard", "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000", "sharePermissions": [ { "type": "global" } ], "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000" }, { "id": "20000", "isFavourite": true, "name": "Build Engineering", "owner": { "key": "Mia", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "name": "mia", "displayName": "Mia Krystof", "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" } }, "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/20000", "sharePermissions": [ { "group": { "name": "administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupname=administrators" }, "id": 10105, "type": "group" } ], "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=20000" } ], "page_size": 10, "next": "https://your-domain.atlassian.net/rest/api/3/dashboard?start_index=10", "prev": "https://your-domain.atlassian.net/rest/api/3/dashboard?start_index=0", "start_index": 10, "total": 143 }`

---

POST

## Create dashboardExperimental

Creates a dashboard.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Query parameters

**extendAdminPermissions**

boolean

#### Request bodyapplication/json

Expand all

Dashboard details.

**description**

string

**editPermissions**

array<SharePermission>

Required

**name**

string

Required

**sharePermissions**

array<SharePermission>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

Dashboard

Details of a dashboard.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/dashboard

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A dashboard to help auditors identify sample of issues to check.", "editPermissions": [], "name": "Auditors dashboard", "sharePermissions": [ { "type": "global" } ] }`; const response = await requestJira(`/rest/api/3/dashboard`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "id": "10000", "isFavourite": false, "name": "System Dashboard", "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000", "sharePermissions": [ { "type": "global" } ], "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000" }`

---

PUT

## Bulk edit dashboardsExperimental

Bulk edit dashboards. Maximum number of dashboards to be edited at the same time is 100.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None

The dashboards to be updated must be owned by the user, or the user must be an administrator.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The details of dashboards being updated in bulk.

**action**

string

Required

**changeOwnerDetails**

BulkChangeOwnerDetails

**entityIds**

array<integer>

Required

**extendAdminPermissions**

boolean

**permissionDetails**

PermissionDetails

### Responses

200OK

Returned if the request is successful.

#### application/json

BulkEditShareableEntityResponse

Details of a request to bulk edit shareable entity.

Show child properties

400Bad Request

401Unauthorized

PUT/rest/api/3/dashboard/bulk/edit

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "action": "changePermission", "entityIds": [ 10001, 10002 ], "extendAdminPermissions": true, "permissionDetails": { "editPermissions": [ { "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/~ver~/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 10010, "type": "group" } ], "sharePermissions": [ { "id": 10000, "type": "global" } ] } }`; const response = await requestJira(`/rest/api/3/dashboard/bulk/edit`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "action": "changePermission", "entityErrors": { "10002": { "errorMessages": [ "Only owner or editors of the dashboard can change permissions." ], "errors": {} } } }`

---

GET

## Get available gadgetsExperimental

Gets a list of all available gadgets that can be added to all dashboards.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

AvailableDashboardGadgetsResponse

The list of available gadgets.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/dashboard/gadgets

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/gadgets`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "gadgets": [ { "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item", "title": "Issue statistics" }, { "uri": "rest/gadgets/1.0/g/com.atlassian.streams.streams-jira-plugin:activitystream-gadget/gadgets/activitystream-gadget.xml", "title": "Activity Stream" } ] }`

---

GET

## Search for dashboards

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of dashboards. This operation is similar to [Get dashboards](/cloud/jira/platform/rest/v3/api-group-dashboards/#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** The following dashboards that match the query parameters are returned:

  * Dashboards owned by the user. Not returned for anonymous users.
  * Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
  * Dashboards shared with a private project that the user can browse. Not returned for anonymous users.
  * Dashboards shared with a public project.
  * Dashboards shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**dashboardName**

string

**user_id**

string

**owner**

string

**groupname**

string

**groupId**

string

**projectId**

integer

**orderBy**

string

**start_index**

integer

**page_size**

integer

**status**

string

Show 1 hidden parameters

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanDashboard

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/dashboard/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``{ "isLast": true, "page_size": 100, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/search?expand=owner&page_size=50&start_index=0", "start_index": 0, "total": 2, "values": [ { "description": "Testing program", "id": "1", "isFavourite": true, "name": "Testing", "owner": { "self": "https://your-domain.atlassian.net/user?user_id=5b10a2844c20165700ede21g", "displayName": "Mia", "active": true, "user_id": "5b10a2844c20165700ede21g", "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" } }, "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/1", "sharePermissions": [ { "type": "global" } ], "view": "https://your-domain.atlassian.net/Dashboard.jspa?selectPageId=1" }, { "description": "Quantum initiative", "id": "2", "isFavourite": false, "name": "Quantum ", "owner": { "self": "https://your-domain.atlassian.net/user?user_id=5b10a2844c20165700ede21g", "displayName": "Mia", "active": true, "user_id": "5b10a2844c20165700ede21g", "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" } }, "popularity": 0, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/2", "sharePermissions": [ { "type": "loggedin" } ], "view": "https://your-domain.atlassian.net/Dashboard.jspa?selectPageId=2" } ] }`

---

GET

## Get gadgetsExperimental

Returns a list of dashboard gadgets on a dashboard.

This operation returns:

  * Gadgets from a list of IDs, when `id` is set.
  * Gadgets with a module key, when `moduleKey` is set.
  * Gadgets from a list of URIs, when `uri` is set.
  * All gadgets, when no other parameters are set.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**dashboardId**

integer

Required

#### Query parameters

Expand all

**moduleKey**

array<string>

**uri**

array<string>

**gadgetId**

array<integer>

### Responses

200OK

Returned if the request is successful.

#### application/json

DashboardGadgetResponse

The list of gadgets on the dashboard.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/dashboard/{dashboardId}/gadget

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/gadget`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``{ "gadgets": [ { "id": 10001, "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item", "color": "blue", "position": { "row": 0, "column": 0 }, "title": "Issue statistics" }, { "id": 10002, "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-graph", "color": "red", "position": { "row": 1, "column": 0 }, "title": "Activity stream" }, { "id": 10003, "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item", "color": "yellow", "position": { "row": 0, "column": 1 }, "title": "Bubble chart" } ] }`

---

POST

## Add gadget to dashboardExperimental

Adds a gadget to a dashboard.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`, `read:jira-work`

**Granular** :`write:dashboard:jira`, `read:dashboard:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**dashboardId**

integer

Required

#### Request bodyapplication/json

Expand all

**color**

string

**ignoreUriAndModuleKeyValidation**

boolean

**moduleKey**

string

**position**

DashboardGadgetPosition

**title**

string

**uri**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

DashboardGadget

Details of a gadget.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/dashboard/{dashboardId}/gadget

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "color": "blue", "ignoreUriAndModuleKeyValidation": false, "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item", "position": { "column": 1, "row": 0 }, "title": "Issue statistics" }`; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/gadget`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "color": "blue", "id": 10001, "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item", "position": { "column": 1, "row": 0 }, "title": "Issue statistics" }`

---

PUT

## Update gadget on dashboardExperimental

Changes the title, position, and color of the gadget on a dashboard.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:dashboard:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**dashboardId**

integer

Required

**gadgetId**

integer

Required

#### Request bodyapplication/json

Expand all

**color**

string

**position**

DashboardGadgetPosition

**title**

string

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "color": "red", "position": { "column": 1, "row": 1 }, "title": "My new gadget title" }`; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove gadget from dashboardExperimental

Removes a dashboard gadget from a dashboard.

When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:dashboard:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

Expand all

**dashboardId**

integer

Required

**gadgetId**

integer

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

401Unauthorized

404Not Found

DEL/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get dashboard item property keys

Returns the keys of all properties for a dashboard item.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**dashboardId**

string

Required

**itemId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PropertyKeys

List of property keys.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "keys": [ { "key": "issue.support", "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support" } ] }`

---

GET

## Get dashboard item property

Returns the key and value of a dashboard item property.

A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).

When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

There is no resource to set or get dashboard items.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**dashboardId**

string

Required

**itemId**

string

Required

**propertyKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

EntityProperty

An entity property, for more information see [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "key": "issue.support", "value": { "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6", "system.support.time": "1m" } }`

---

PUT

## Set dashboard item property

Sets the value of a dashboard item property. Use this resource in apps to store custom data against a dashboard item.

A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).

When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

There is no resource to set or get dashboard items.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** The user must have edit permisson of the dashboard.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:dashboard.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**dashboardId**

string

Required

**itemId**

string

Required

**propertyKey**

string

Required

#### Request bodyapplication/json

The value of the property. The value has to be a valid, non-empty [JSON](https://tools.ietf.org/html/rfc4627) value. The maximum length of the property value is 32768 bytes.

any

### Responses

200OK

Returned if the dashboard item property is updated.

#### application/json

any

201Created

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "number": 5, "string": "string-value" }`; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete dashboard item property

Deletes a dashboard item property.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** The user must have edit permission of the dashboard.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:dashboard.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

Expand all

**dashboardId**

string

Required

**itemId**

string

Required

**propertyKey**

string

Required

### Responses

204No Content

Returned if the dashboard item property is deleted.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get dashboard

Returns a dashboard.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

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

Dashboard

Details of a dashboard.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/dashboard/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "id": "10000", "isFavourite": false, "name": "System Dashboard", "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000", "sharePermissions": [ { "type": "global" } ], "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000" }`

---

PUT

## Update dashboardExperimental

Updates a dashboard, replacing all the dashboard details with those provided.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None

The dashboard to be updated must be owned by the user.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**extendAdminPermissions**

boolean

#### Request bodyapplication/json

Expand all

Replacement dashboard details.

**description**

string

**editPermissions**

array<SharePermission>

Required

**name**

string

Required

**sharePermissions**

array<SharePermission>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

Dashboard

Details of a dashboard.

Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/dashboard/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A dashboard to help auditors identify sample of issues to check.", "editPermissions": [], "name": "Auditors dashboard", "sharePermissions": [ { "type": "global" } ] }`; const response = await requestJira(`/rest/api/3/dashboard/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "id": "10000", "isFavourite": false, "name": "System Dashboard", "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000", "sharePermissions": [ { "type": "global" } ], "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000" }`

---

DEL

## Delete dashboardExperimental

Deletes a dashboard.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None

The dashboard to be deleted must be owned by the user.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:dashboard:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

string

Required

### Responses

204No Content

Returned if the dashboard is deleted.

400Bad Request

401Unauthorized

DEL/rest/api/3/dashboard/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/dashboard/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Copy dashboardExperimental

Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied dashboard.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None

The dashboard to be copied must be owned by or shared with the user.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:dashboard:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**extendAdminPermissions**

boolean

#### Request bodyapplication/json

Expand all

Dashboard details.

**description**

string

**editPermissions**

array<SharePermission>

Required

**name**

string

Required

**sharePermissions**

array<SharePermission>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

Dashboard

Details of a dashboard.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/dashboard/{id}/copy

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "A dashboard to help auditors identify sample of issues to check.", "editPermissions": [], "name": "Auditors dashboard", "sharePermissions": [ { "type": "global" } ] }`; const response = await requestJira(`/rest/api/3/dashboard/{id}/copy`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "id": "10000", "isFavourite": false, "name": "System Dashboard", "popularity": 1, "self": "https://your-domain.atlassian.net/rest/api/3/dashboard/10000", "sharePermissions": [ { "type": "global" } ], "view": "https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000" }`