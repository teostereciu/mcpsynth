# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Groups

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents groups of users. Use it to get, create, find, and delete groups as well as add and remove users from groups. ([WARNING] The standard Atlassian group names are default names only and can be edited or deleted. For example, an admin or Atlassian support could delete the default group jira-software-users or rename it to jsw-users at any point. See <https://support.atlassian.com/user-management/docs/create-and-update-groups/>[](https://support.atlassian.com/user-management/docs/create-and-update-groups/) for details.)

Operations

[GET/rest/api/3/group](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-get)[POST/rest/api/3/group](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-post)[DEL/rest/api/3/group](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-delete)[GET/rest/api/3/group/bulk](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-bulk-get)[GET/rest/api/3/group/member](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-member-get)[POST/rest/api/3/group/user](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-user-post)[DEL/rest/api/3/group/user](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-user-delete)[GET/rest/api/3/groups/picker](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-groups-picker-get)

---

GET

## Get groupDeprecated

This operation is deprecated, use [`group/member`](/cloud/jira/platform/rest/v3/api-group-groups/#api-rest-api-3-group-member-get).

Returns all users in a group.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** either of:

  * _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:group:jira`, `read:user:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**groupname**

string

**groupId**

string

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Group

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/group

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/group?groupId={groupId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``{ "expand": "<string>", "groupId": "<string>", "name": "<string>", "self": "<string>", "users": { "end-index": 48, "items": [ { "accountId": "<string>", "accountType": "<string>", "active": true, "avatarUrls": {}, "displayName": "<string>", "emailAddress": "<string>", "key": "<string>", "name": "<string>", "self": "<string>", "timeZone": "<string>" } ], "max-results": 56, "size": 32, "start-index": 49 } }`

---

POST

## Create group

Creates a group.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Site administration (that is, member of the _site-admin_ [group](https://confluence.atlassian.com/x/24xjL)).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:group:jira`, `read:user:jira`, `write:group:jira`, `read:avatar:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The name of the group.

**name**

string

Required

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

Group

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/group

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "name": "power-users" }`; const response = await requestJira(`/rest/api/3/group`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "expand": "users", "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "power-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625", "users": { "end-index": 0, "items": [ { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" } ], "max-results": 50, "size": 1, "start-index": 0 } }`

---

DEL

## Remove group

Deletes a group.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Site administration (that is, member of the _site-admin_ strategic [group](https://confluence.atlassian.com/x/24xjL)).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:group:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**groupname**

string

**groupId**

string

**swapGroup**

string

**swapGroupId**

string

### Responses

200OK

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/group

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/group?groupId={groupId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Bulk get groupsExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of groups.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:group:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**startAt**

integer

**maxResults**

integer

**groupId**

array<string>

**groupName**

array<string>

**accessType**

string

**applicationKey**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanGroupDetails

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

500Internal Server Error

GET/rest/api/3/group/bulk

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/group/bulk?groupId={groupId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "isLast": true, "maxResults": 10, "startAt": 0, "total": 2, "values": [ { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jdog-developers" }, { "groupId": "6e87dc72-4f1f-421f-9382-2fee8b652487", "name": "juvenal-bot" } ] }`

---

GET

## Get users from group

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of all users in a group.

Note that users are ordered by username, however the username is not returned in the results due to privacy reasons.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** either of:

  * _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).
  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:group:jira`, `read:user:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**groupname**

string

**groupId**

string

**includeInactiveUsers**

boolean

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanUserDetails

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/group/member

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/group/member?groupId={groupId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``{ "isLast": false, "maxResults": 2, "nextPage": "https://your-domain.atlassian.net/rest/api/3/group/member?groupId=276f955c-63d7-42c8-9520-92d01dca0625&includeInactiveUsers=false&startAt=4&maxResults=2", "self": "https://your-domain.atlassian.net/rest/api/3/group/member?groupId=276f955c-63d7-42c8-9520-92d01dca0625&includeInactiveUsers=false&startAt=2&maxResults=2", "startAt": 3, "total": 5, "values": [ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "avatarUrls": {}, "displayName": "Mia", "emailAddress": "mia@example.com", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, { "accountId": "5b10a0effa615349cb016cd8", "accountType": "atlassian", "active": false, "avatarUrls": {}, "displayName": "Will", "emailAddress": "will@example.com", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a0effa615349cb016cd8", "timeZone": "Australia/Sydney" } ] }`

---

POST

## Add user to group

Adds a user to a group.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Site administration (that is, member of the _site-admin_ [group](https://confluence.atlassian.com/x/24xjL)).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:group:jira`, `read:avatar:jira`, `read:group:jira`, `read:user:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**groupname**

string

**groupId**

string

#### Request bodyapplication/json

Expand all

The user to add to the group.

**accountId**

string

**name**

string

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

Group

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

429Too Many Requests

POST/rest/api/3/group/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "accountId": "5b10ac8d82e05b22cc7d4ef5" }`; const response = await requestJira(`/rest/api/3/group/user?groupId={groupId}`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``{ "expand": "<string>", "groupId": "<string>", "name": "<string>", "self": "<string>", "users": { "end-index": 48, "items": [ { "accountId": "<string>", "accountType": "<string>", "active": true, "avatarUrls": {}, "displayName": "<string>", "emailAddress": "<string>", "key": "<string>", "name": "<string>", "self": "<string>", "timeZone": "<string>" } ], "max-results": 56, "size": 32, "start-index": 49 } }`

---

DEL

## Remove user from group

Removes a user from a group.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Site administration (that is, member of the _site-admin_ [group](https://confluence.atlassian.com/x/24xjL)).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:group:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**groupname**

string

**groupId**

string

**username**

string

**accountId**

string

Required

### Responses

200OK

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

429Too Many Requests

DEL/rest/api/3/group/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/group/user?groupId={groupId}&accountId=5b10ac8d82e05b22cc7d4ef5`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Find groups

Returns a list of groups whose names contain a query string. A list of group names can be provided to exclude groups from the results.

The primary use case for this resource is to populate a group picker suggestions list. To this end, the returned object includes the `html` field where the matched query term is highlighted in the group name with the HTML strong tag. Also, the groups list is wrapped in a response object that contains a header for use in the picker, specifically _Showing X of Y matching groups_.

The list returns with the groups sorted. If no groups match the list criteria, an empty list is returned.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without the required permission return an empty list.

_Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg). Without this permission, calls where query is not an exact match to an existing group will return an empty list.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:group:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**accountId**

string

**query**

string

**exclude**

array<string>

**excludeId**

array<string>

**maxResults**

integer

**caseInsensitive**

boolean

**userName**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

FoundGroups

The list of groups found in a search, including header text (Showing X of Y matching groups) and total of matched groups.

Show child properties

GET/rest/api/3/groups/picker

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/groups/picker`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "groups": [ { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "html": "<b>j</b>dog-developers", "name": "jdog-developers" }, { "groupId": "6e87dc72-4f1f-421f-9382-2fee8b652487", "html": "<b>j</b>uvenal-bot", "name": "juvenal-bot" } ], "header": "Showing 20 of 25 matching groups", "total": 25 }`