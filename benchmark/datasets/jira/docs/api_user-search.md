# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-user-search/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# User search

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents various ways to search for and find users. Use it to obtain list of users including users assignable to projects and issues, users with permissions, user lists for pickup fields, and user lists generated using structured queries. Note that the operations in this resource only return users found within the first 1000 users.

Operations

[GET/rest/api/3/user/assignable/multiProjectSearch](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-assignable-multiprojectsearch-get)[GET/rest/api/3/user/assignable/search](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-assignable-search-get)[GET/rest/api/3/user/permission/search](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-permission-search-get)[GET/rest/api/3/user/picker](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-picker-get)[GET/rest/api/3/user/search](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-search-get)[GET/rest/api/3/user/search/query](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-search-query-get)[GET/rest/api/3/user/search/query/key](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-search-query-key-get)[GET/rest/api/3/user/viewissue/search](/cloud/jira/platform/rest/v3/api-group-user-search/#api-rest-api-3-user-viewissue-search-get)

---

GET

## Find users assignable to projects

Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned issues in the projects. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned issues in the projects, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for each project specified in `projectKeys`.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:project:jira`, `read:user:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

**username**

string

**accountId**

string

**projectKeys**

string

Required

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

401Unauthorized

404Not Found

429Too Many Requests

GET/rest/api/3/user/assignable/multiProjectSearch

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/assignable/multiProjectSearch?query=query&projectKeys={projectKeys}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``[ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, { "accountId": "5b10ac8d82e05b22cc7d4ef5", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" }, "displayName": "Emma Richards", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5" } ]`

---

GET

## Find users assignable to issues

Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to:

  * a new issue, by providing the `projectKeyOrId`.
  * an updated issue, by providing the `issueKey` or `issueId`.
  * to an issue during a transition (workflow action), by providing the `issueKey` or `issueId` and the transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using the `transitions` option in the `expand` parameter of [ Get issue](/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get).


In all these cases, you can pass an account ID to determine if a user can be assigned to an issue. The user is returned in the response if they can be assigned to the issue or issue transition.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned the issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned the issue, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Assign issues_ [project permission](https://confluence.atlassian.com/x/yodKLg)

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:issue:jira`, `read:project:jira`, `read:user:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

**sessionId**

string

**username**

string

**accountId**

string

**project**

string

**issueKey**

string

**issueId**

string

**startAt**

integer

**maxResults**

integer

**actionDescriptorId**

integer

Show 3 hidden parameters

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

401Unauthorized

404Not Found

429Too Many Requests

GET/rest/api/3/user/assignable/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/assignable/search?query=query`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }`

---

GET

## Find users with permissions

Returns a list of users who fulfill these criteria:

  * their user attributes match a search string.
  * they have a set of permissions for a project or issue.


If no search string is provided, a list of all users with the permissions is returned.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission for the project or issue, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project.
  * _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:issue:jira`, `read:project:jira`, `read:user:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

**username**

string

**accountId**

string

**permissions**

string

Required

**issueKey**

string

**projectKey**

string

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

429Too Many Requests

GET/rest/api/3/user/permission/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/permission/search?query=query&permissions={permissions}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``[ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, { "accountId": "5b10ac8d82e05b22cc7d4ef5", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" }, "displayName": "Emma Richards", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5" } ]`

---

GET

## Find users for picker

Returns a list of users whose attributes match the query term. The returned object includes the `html` field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results.

This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and then returns only the users from that range that match the query term. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the query term, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return search results for an exact name match only.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**maxResults**

integer

**showAvatar**

boolean

**exclude**

array<string>

**excludeAccountIds**

array<string>

**avatarSize**

string

**excludeConnectUsers**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

FoundUsers

The list of users found in a search, including header text (Showing X of Y matching users) and total of matched users.

Show child properties

400Bad Request

401Unauthorized

429Too Many Requests

GET/rest/api/3/user/picker

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/picker?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "header": "Showing 20 of 25 matching groups", "total": 25, "users": [ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "avatarUrl": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "displayName": "Mia Krystof", "html": "<strong>Mi</strong>a Krystof - <strong>mi</strong>a@example.com (<strong>mi</strong>a)", "key": "mia", "name": "mia" } ] }`

---

GET

## Find users

Returns a list of active users that match the search string and property.

This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get all the users who match the search string and property, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

This operation can be accessed anonymously.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without the required permission return empty search results.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user:jira`, `read:user.property:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

**username**

string

**accountId**

string

**startAt**

integer

**maxResults**

integer

**property**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

401Unauthorized

429Too Many Requests

GET/rest/api/3/user/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/search?query=query`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``[ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, { "accountId": "5b10ac8d82e05b22cc7d4ef5", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" }, "displayName": "Emma Richards", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5" } ]`

---

GET

## Find users by query

Finds users with a structured query and returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of user details.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

The query statements are:

  * `is assignee of PROJ` Returns the users that are assignees of at least one issue in project _PROJ_.
  * `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues _PROJ-1_ or _PROJ-2_.
  * `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues _PROJ-1_ or _PROJ-2_.
  * `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues _PROJ-1_ or _PROJ-2_.
  * `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues _PROJ-1_ or _PROJ-2_.
  * `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues _PROJ-1_ or _PROJ-2_.
  * `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues _PROJ-1_ or _PROJ-2_.
  * `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value. For example, if user property `location` is set to value `{"office": {"country": "AU", "city": "Sydney"}}`, then it's possible to use `[location].office.city is "Sydney"` to match the user.


The list of issues can be extended as needed, as in _(PROJ-1, PROJ-2, ... PROJ-n)_. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example:

`is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:comment:jira`, `read:issue:jira`, `read:issue.vote:jira`, `read:issue.watcher:jira`, `read:project:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanUser

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

408Request Timeout

GET/rest/api/3/user/search/query

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/search/query?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``{ "isLast": true, "maxResults": 51, "nextPage": "<string>", "self": "<string>", "startAt": 37, "total": 29, "values": [ { "accountId": "<string>", "accountType": "atlassian", "active": true, "appType": "<string>", "applicationRoles": { "callback": {}, "items": [ {} ], "max-results": 2154, "pagingCallback": {}, "size": 2154 }, "avatarUrls": { "16x16": "<string>", "24x24": "<string>", "32x32": "<string>", "48x48": "<string>" }, "displayName": "<string>", "emailAddress": "<string>", "expand": "<string>", "groups": { "callback": {}, "items": [ {} ], "max-results": 2154, "pagingCallback": {}, "size": 2154 }, "guest": true, "key": "<string>", "locale": "<string>", "name": "<string>", "self": "<string>", "timeZone": "<string>" } ] }`

---

GET

## Find user keys by query

Finds users with a structured query and returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of user keys.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

The query statements are:

  * `is assignee of PROJ` Returns the users that are assignees of at least one issue in project _PROJ_.
  * `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues _PROJ-1_ or _PROJ-2_.
  * `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues _PROJ-1_ or _PROJ-2_.
  * `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues _PROJ-1_ or _PROJ-2_.
  * `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues _PROJ-1_ or _PROJ-2_.
  * `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues _PROJ-1_ or _PROJ-2_.
  * `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues _PROJ-1_ or _PROJ-2_.
  * `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value. For example, if user property `location` is set to value `{"office": {"country": "AU", "city": "Sydney"}}`, then it's possible to use `[location].office.city is "Sydney"` to match the user.


The list of issues can be extended as needed, as in _(PROJ-1, PROJ-2, ... PROJ-n)_. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example:

`is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:comment:jira`, `read:issue:jira`, `read:issue.vote:jira`, `read:issue.watcher:jira`, `read:project:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**startAt**

integer

**maxResult**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanUserKey

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

408Request Timeout

GET/rest/api/3/user/search/query/key

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/search/query/key?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "isLast": true, "maxResults": 51, "nextPage": "<string>", "self": "<string>", "startAt": 37, "total": 29, "values": [ { "accountId": "<string>", "key": "<string>" } ] }`

---

GET

## Find users with browse permission

Returns a list of users who fulfill these criteria:

  * their user attributes match a search string.
  * they have permission to browse issues.


Use this resource to find users who can browse:

  * an issue, by providing the `issueKey`.
  * any issue in a project, by providing the `projectKey`.


This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission to browse issues. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission to browse issues, use [Get all users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return empty search results.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:issue:jira`, `read:project:jira`, `read:user:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

**username**

string

**accountId**

string

**issueKey**

string

**projectKey**

string

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

401Unauthorized

404Not Found

429Too Many Requests

GET/rest/api/3/user/viewissue/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/viewissue/search?query=query`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``[ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, { "accountId": "5b10ac8d82e05b22cc7d4ef5", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" }, "displayName": "Emma Richards", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5" } ]`