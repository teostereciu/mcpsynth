# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Filters

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [filters](https://confluence.atlassian.com/x/eQiiLQ). Use it to get, create, update, or delete filters. Also use it to configure the columns for a filter and set favorite filters.

Operations

[POST/rest/api/3/filter](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-post)[GET/rest/api/3/filter/favourite](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-favourite-get)[GET/rest/api/3/filter/my](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-my-get)[GET/rest/api/3/filter/search](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-search-get)[GET/rest/api/3/filter/{id}](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-get)[PUT/rest/api/3/filter/{id}](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-put)[DEL/rest/api/3/filter/{id}](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-delete)[GET/rest/api/3/filter/{id}/columns](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-columns-get)[PUT/rest/api/3/filter/{id}/columns](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-columns-put)[DEL/rest/api/3/filter/{id}/columns](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-columns-delete)[PUT/rest/api/3/filter/{id}/favourite](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-favourite-put)[DEL/rest/api/3/filter/{id}/favourite](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-favourite-delete)[PUT/rest/api/3/filter/{id}/owner](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-id-owner-put)

---

POST

## Create filter

Creates a filter. The filter is shared according to the [default share scope](/cloud/jira/platform/rest/v3/api-group-filters/#api-rest-api-3-filter-post). The filter is not selected as a favorite.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Query parameters

Expand all

**expand**

string

**overrideSharePermissions**

boolean

#### Request bodyapplication/json

Expand all

The filter to create.

**description**

string

**editPermissions**

array<SharePermission>

**favourite**

boolean

**jql**

string

**name**

string

Required

**sharePermissions**

array<SharePermission>

### Responses

200OK

Returned if the request is successful.

#### application/json

Filter

Details about a filter.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/filter

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Lists all open bugs", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs" }`; const response = await requestJira(`/rest/api/3/filter`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "approximateLastUsed": null, "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }`

---

GET

## Get favorite filters

Returns the visible favorite filters of the user.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** A favorite filter is only visible to the user where the filter is:

  * owned by the user.
  * shared with a group that the user is a member of.
  * shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * shared with a public project.
  * shared with the public.


For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Filter>

Show child properties

401Unauthorized

GET/rest/api/3/filter/favourite

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/favourite`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 ``[ { "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }, { "approximateLastUsed": null, "description": "Issues assigned to me", "favourite": true, "favouritedCount": 0, "id": "10010", "jql": "assignee = currentUser() and resolution is empty", "name": "My issues", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=assignee+in+%28currentUser%28%29%29+and+resolution+is+empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10010", "sharePermissions": [ { "id": 10000, "type": "global" }, { "id": 10010, "project": { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "key": "EX", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic" }, "type": "project" } ], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10010" } ]`

---

GET

## Get my filters

Returns the filters owned by the user. If `includeFavourites` is `true`, the user's visible favorite filters are also returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, a favorite filters is only visible to the user where the filter is:

  * owned by the user.
  * shared with a group that the user is a member of.
  * shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * shared with a public project.
  * shared with the public.


For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**expand**

string

**includeFavourites**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Filter>

Show child properties

401Unauthorized

GET/rest/api/3/filter/my

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/my`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 ``[ { "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }, { "approximateLastUsed": null, "description": "Issues assigned to me", "favourite": true, "favouritedCount": 0, "id": "10010", "jql": "assignee = currentUser() and resolution is empty", "name": "My issues", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=assignee+in+%28currentUser%28%29%29+and+resolution+is+empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10010", "sharePermissions": [ { "id": 10000, "type": "global" }, { "id": 10010, "project": { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "key": "EX", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic" }, "type": "project" } ], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10010" } ]`

---

GET

## Search for filters

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of filters. Use this operation to get:

  * specific filters, by defining `id` only.
  * filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. When multiple attributes are specified only filters matching all attributes are returned.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None, however, only the following filters that match the query parameters are returned:

  * filters owned by the user.
  * filters shared with a group that the user is a member of.
  * filters shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * filters shared with a public project.
  * filters shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**filterName**

string

**accountId**

string

**owner**

string

**groupname**

string

**groupId**

string

**projectId**

integer

**id**

array<integer>

**orderBy**

string

**startAt**

integer

**maxResults**

integer

Show 3 hidden parameters

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanFilterDetails

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/filter/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 ``{ "isLast": true, "maxResults": 100, "self": "https://your-domain.atlassian.net/rest/api/3/filter/search?accountId=&maxResults=50&filterName=&orderBy=name&startAt=0&expand=description,owner,jql,searchUrl,viewUrl,favourite,favouritedCount,sharePermissions,editPermissions,isWritable,subscriptions,approximateLastUsed", "startAt": 0, "total": 2, "values": [ { "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "editPermissions": [], "expand": "description,owner,jql,searchUrl,viewUrl,favourite,favouritedCount,sharePermissions,editPermissions,isWritable,approximateLastUsed,subscriptions", "favourite": false, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": [], "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }, { "approximateLastUsed": null, "description": "Issues assigned to me", "editPermissions": [ { "id": 10010, "project": { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10002", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10002", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10002", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10002" }, "deleted": true, "deletedBy": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "deletedDate": "2022-11-11T13:35:29.000+0000", "id": "10002", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "key": "MKY", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "retentionTillDate": "2023-01-10T13:35:29.000+0000", "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY", "simplified": false, "style": "classic" }, "role": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "accountId": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "type": "project" }, { "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 10010, "type": "group" } ], "expand": "description,owner,jql,searchUrl,viewUrl,favourite,favouritedCount,sharePermissions,editPermissions,isWritable,approximateLastUsed,subscriptions", "favourite": true, "favouritedCount": 123, "id": "10010", "jql": "assignee = currentUser() and resolution is empty", "name": "My issues", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=assignee+in+%28currentUser%28%29%29+and+resolution+is+empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10010", "sharePermissions": [ { "id": 10000, "type": "global" }, { "id": 10010, "project": { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "key": "EX", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic" }, "type": "project" } ], "subscriptions": [ { "id": 1, "user": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" } } ], "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10010" } ] }`

---

GET

## Get filter

Returns a filter.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None, however, the filter is only returned where it is:

  * owned by the user.
  * shared with a group that the user is a member of.
  * shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * shared with a public project.
  * shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**expand**

string

**overrideSharePermissions**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

Filter

Details about a filter.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/filter/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }`

---

PUT

## Update filter

Updates a filter. Use this operation to update a filter's name, description, JQL, or sharing.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however the user must own the filter.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:filter:jira`, `read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**expand**

string

**overrideSharePermissions**

boolean

#### Request bodyapplication/json

Expand all

The filter to update.

**description**

string

**editPermissions**

array<SharePermission>

**favourite**

boolean

**jql**

string

**name**

string

Required

**sharePermissions**

array<SharePermission>

### Responses

200OK

Returned if the request is successful.

#### application/json

Filter

Details about a filter.

Show child properties

400Bad Request

401Unauthorized

PUT/rest/api/3/filter/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Lists all open bugs", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs" }`; const response = await requestJira(`/rest/api/3/filter/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }`

---

DEL

## Delete filter

Delete a filter.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however filters can only be deleted by the creator of the filter or a user with _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:filter:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

integer

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

DEL/rest/api/3/filter/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get columns

Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in _List View_ with the _Columns_ set to _Filter_.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None, however, column details are only returned for:

  * filters owned by the user.
  * filters shared with a group that the user is a member of.
  * filters shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * filters shared with a public project.
  * filters shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:filter.column:jira`

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

array<ColumnItem>

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/filter/{id}/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/{id}/columns`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``[ { "label": "Key", "value": "issuekey" }, { "label": "Summary", "value": "summary" } ]`

---

PUT

## Set columns

Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-rest-api-3-field-get) to get the list fields in Jira. A navigable field has `navigable` set to `true`.

The parameters for this resource are expressed as HTML form data. For example, in curl:

`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/filter/10000/columns`

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, columns are only set for:

  * filters owned by the user.
  * filters shared with a group that the user is a member of.
  * filters shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * filters shared with a public project.
  * filters shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:filter.column:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

integer

Required

#### Request body*/* application/json multipart/form-data

The IDs of the fields to set as columns. In the form data, specify each field as `columns=id`, where `id` is the _id_ of a field (as seen in the response for Get fields). For example, `columns=summary`.

**columns**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

any

400Bad Request

403Forbidden

PUT/rest/api/3/filter/{id}/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "columns": [ "<string>" ] }`; const response = await requestJira(`/rest/api/3/filter/{id}/columns`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Reset columns

Reset the user's column configuration for the filter to the default.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, columns are only reset for:

  * filters owned by the user.
  * filters shared with a group that the user is a member of.
  * filters shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * filters shared with a public project.
  * filters shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:filter.column:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

integer

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

DEL/rest/api/3/filter/{id}/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/{id}/columns`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

PUT

## Add filter as favorite

Add a filter as a favorite for the user.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, the user can only favorite:

  * filters owned by the user.
  * filters shared with a group that the user is a member of.
  * filters shared with a private project that the user has _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for.
  * filters shared with a public project.
  * filters shared with the public.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:filter:jira`, `read:group:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Filter

Details about a filter.

Show child properties

400Bad Request

PUT/rest/api/3/filter/{id}/favourite

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/{id}/favourite`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }`

---

DEL

## Remove filter as favorite

Removes a filter as a favorite for the user. Note that this operation only removes filters visible to the user from the user's favorites list. For example, if the user favorites a public filter that is subsequently made private (and is therefore no longer visible on their favorites list) they cannot remove it from their favorites list.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:filter:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:filter:jira`, `read:group:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

Filter

Details about a filter.

Show child properties

400Bad Request

DEL/rest/api/3/filter/{id}/favourite

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/filter/{id}/favourite`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``{ "approximateLastUsed": "2023-03-01T13:15:00.000+0000", "description": "Lists all open bugs", "favourite": true, "favouritedCount": 0, "id": "10000", "jql": "type = Bug and resolution is empty", "name": "All Open Bugs", "owner": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "searchUrl": "https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty", "self": "https://your-domain.atlassian.net/rest/api/3/filter/10000", "sharePermissions": [], "subscriptions": { "end-index": 0, "items": [], "max-results": 0, "size": 0, "start-index": 0 }, "viewUrl": "https://your-domain.atlassian.net/issues/?filter=10000" }`

---

PUT

## Change filter ownerExperimental

Changes the owner of the filter.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira. However, the user must own the filter or have the _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:filter:jira`, `write:filter:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

The account ID of the new owner of the filter.

**accountId**

string

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

403Forbidden

404Not Found

PUT/rest/api/3/filter/{id}/owner

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "accountId": "0000-0000-0000-0000" }`; const response = await requestJira(`/rest/api/3/filter/{id}/owner`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`