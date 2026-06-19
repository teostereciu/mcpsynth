# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-group/*

---

Cloud

Confluence Cloud / Reference / REST API

# Group

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

**[WARNING](https://support.atlassian.com/user-management/docs/create-and-update-groups/) The standard Atlassian group names are default names only and can be edited or deleted.** For example, an admin or Atlassian support could delete the default group jira-software-users or rename it to jsw-users at any point.

Operations

[GET/wiki/rest/api/group](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-get)[POST/wiki/rest/api/group](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-post)[GET/wiki/rest/api/group/by-id](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-by-id-get)[DEL/wiki/rest/api/group/by-id](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-by-id-delete)[GET/wiki/rest/api/group/picker](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-picker-get)[GET/wiki/rest/api/group/{groupId}/membersByGroupId](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-groupid-membersbygroupid-get)[POST/wiki/rest/api/group/userByGroupId](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-userbygroupid-post)[DEL/wiki/rest/api/group/userByGroupId](/cloud/confluence/rest/v1/api-group-group/#api-wiki-rest-api-group-userbygroupid-delete)

---

GET

## Get groups

Returns all user groups. The returned groups are ordered alphabetically in ascending order by group name.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-groups`

**Granular** :`read:group:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**offset**

integer

**max_results**

integer

**accessType**

string

### Responses

200OK

Returned if the requested groups are returned.

#### application/json

GroupArrayWithLinks

Same as GroupArray but with `_links` property.

Show child properties

403Forbidden

GET/wiki/rest/api/group

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/group`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "results": [ { "type": "group", "name": "<string>", "id": "<string>", "usageType": "USERBASE_GROUP", "managedBy": "ADMINS", "_links": {} } ], "offset": 2154, "max_results": 2154, "size": 2154, "totalSize": 150, "_links": {} }`

---

POST

## Create new user group

Creates a new user group.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User must be a site admin.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-groups`

**Granular** :`read:group:confluence`, `write:group:confluence`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Name of the group that is to be created.

**name**

string

Required

### Responses

201Created

Returned if the group was created successfully.

#### application/json

Group

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/wiki/rest/api/group

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "name": "<string>" }`; const response = await requestConfluence(`/wiki/rest/api/group`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 ``{ "type": "group", "name": "<string>", "id": "<string>", "usageType": "USERBASE_GROUP", "managedBy": "ADMINS", "_links": {} }`

---

GET

## Get group

Returns a user group for a given group id.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-groups`

**Granular** :`read:group:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

**id**

string

Required

### Responses

200OK

Returned if the requested group is returned.

#### application/json

Group

Show child properties

403Forbidden

404Not Found

GET/wiki/rest/api/group/by-id

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/group/by-id?id={id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "type": "group", "name": "<string>", "id": "<string>", "usageType": "USERBASE_GROUP", "managedBy": "ADMINS", "_links": {} }`

---

DEL

## Delete user group

Delete user group.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User must be a site admin.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-groups`

**Granular** :`write:group:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**id**

string

Required

### Responses

204No Content

Returned if the group was removed successfully.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/wiki/rest/api/group/by-id

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/group/by-id?id={id}`, { method: 'DELETE' }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Search groups by partial query

Get search results of groups by partial query provided.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-groups`

**Granular** :`read:group:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**offset**

integer

**max_results**

integer

**shouldReturnTotalSize**

boolean

### Responses

200OK

Returns a full JSON representation of group collection.

#### application/json

GroupArrayWithLinks

Same as GroupArray but with `_links` property.

Show child properties

403Forbidden

GET/wiki/rest/api/group/picker

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/group/picker?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "results": [ { "type": "group", "name": "<string>", "id": "<string>", "usageType": "USERBASE_GROUP", "managedBy": "ADMINS", "_links": {} } ], "offset": 2154, "max_results": 2154, "size": 2154, "totalSize": 150, "_links": {} }`

---

GET

## Get group members

Returns the users that are members of a group.

Use updated Get group API

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-groups`

**Granular** :`read:group:confluence`, `read:user:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**groupId**

string

Required

#### Query parameters

Expand all

**offset**

integer

**max_results**

integer

**shouldReturnTotalSize**

boolean

**include**

array<string>

### Responses

200OK

Returned if the requested users are returned.

#### application/json

UserArray

Show child properties

400Bad Request

403Forbidden

GET/wiki/rest/api/group/{groupId}/membersByGroupId

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/group/{groupId}/membersByGroupId`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 ``{ "results": [ { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": { "business": { "position": "<string>", "department": "<string>", "location": "<string>" }, "personal": { "phone": "<string>", "im": "<string>", "website": "<string>", "email": "<string>" } }, "personalSpace": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "homepage": { "type": "<string>", "content_status": "<string>" }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "size": 2154 }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "content_status": "<string>", "settings": { "routeOverrideEnabled": true, "_links": {} }, "theme": { "themeKey": "<string>" }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" } }, "history": { "createdDate": "<string>" }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} } ], "offset": 2154, "max_results": 2154, "size": 2154, "totalSize": 150, "_links": {} }`

---

POST

## Add member to group by groupId

Adds a user as a member in a group represented by its groupId

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User must be a site admin.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-groups`

**Granular** :`write:group:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**groupId**

string

Required

#### Request bodyapplication/json

AccountId of the user who needs to be added as member.

**accountId**

string

Required

### Responses

201Created

Returned if the group was created successfully.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/wiki/rest/api/group/userByGroupId

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "accountId": "<string>" }`; const response = await requestConfluence(`/wiki/rest/api/group/userByGroupId?groupId={groupId}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove member from group using group id

Remove user as a member from a group.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User must be a site admin.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-groups`

**Granular** :`write:group:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**groupId**

string

Required

**accountId**

string

Required

**key**

string

**username**

string

### Responses

204No Content

Returned if the group was removed successfully.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/wiki/rest/api/group/userByGroupId

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/group/userByGroupId?groupId={groupId}&accountId={accountId}`, { method: 'DELETE' }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`