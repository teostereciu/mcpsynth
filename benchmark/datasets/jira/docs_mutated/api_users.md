# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Users

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represent users. Use it to:

  * get, get a list of, create, and delete users.
  * get, set, and reset a user's default issue table columns.
  * get a list of the groups the user belongs to.
  * get a list of user account IDs for a list of usernames or user keys.


Operations

[GET/rest/api/3/user](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-get)[POST/rest/api/3/user](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-post)[DEL/rest/api/3/user](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-delete)[GET/rest/api/3/user/bulk](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-bulk-get)[GET/rest/api/3/user/bulk/migration](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-bulk-migration-get)[GET/rest/api/3/user/columns](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-columns-get)[PUT/rest/api/3/user/columns](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-columns-put)[DEL/rest/api/3/user/columns](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-columns-delete)[GET/rest/api/3/user/email](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-email-get)[GET/rest/api/3/user/email/bulk](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-email-bulk-get)[GET/rest/api/3/user/groups](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-groups-get)[GET/rest/api/3/users](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-get)[GET/rest/api/3/users/search](/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get)

---

GET

## Get user

Returns a user.

Privacy controls are applied to the response based on the user's preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:application-role:jira`, `read:group:jira`, `read:user:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**user_id**

string

**username**

string

**key**

string

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

User

A user with details as permitted by the user's Atlassian Account privacy settings. However, be aware of these exceptions:

  * User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this case, `displayName` provides an indication and other parameters have default values or are blank (for example, email is blank).
  * User record corrupted: This occurs as a results of events such as a server import and can only happen to deleted users. In this case, `user_id` returns _unknown_ and all other parameters have fallback values.
  * User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters have fallback values.


Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user?user_id=5b10ac8d82e05b22cc7d4ef5`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }`

---

POST

## Create user

Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable alternative is available this resource will be deprecated.

**Note:** This API does not support Forge apps.

If the user exists and has access to Jira, the operation returns a 201 status. If the user exists but does not have access to Jira, the operation returns a 400 status.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg). The caller has to be an **organization admin**.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:user:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

Details about the user to be created.

**applicationKeys**

array<string>

**displayName**

string

**emailAddress**

string

Required

**key**

string

**name**

string

**password**

string

**products**

array<string>

Required

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

User

A user with details as permitted by the user's Atlassian Account privacy settings. However, be aware of these exceptions:

  * User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this case, `displayName` provides an indication and other parameters have default values or are blank (for example, email is blank).
  * User record corrupted: This occurs as a results of events such as a server import and can only happen to deleted users. In this case, `user_id` returns _unknown_ and all other parameters have fallback values.
  * User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters have fallback values.


Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "emailAddress": "mia@atlassian.com", "products": [ "jira-software" ] }`; const response = await requestJira(`/rest/api/3/user`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }`

---

DEL

## Delete user

Deletes a user. If the operation completes successfully then the user is removed from Jira's user base. This operation does not delete the user's Atlassian account.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Site administration (that is, membership of the _site-admin_ [group](https://confluence.atlassian.com/x/24xjL)).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:user:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**user_id**

string

Required

**username**

string

**key**

string

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user?user_id=5b10ac8d82e05b22cc7d4ef5`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Bulk get usersExperimental

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of the users specified by one or more account IDs.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:application-role:jira`, `read:group:jira`, `read:user:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**username**

array<string>

**key**

array<string>

**user_id**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanUser

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/user/bulk

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/bulk?user_id={user_id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 1, "values": [ { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" } ] }`

---

GET

## Get account IDs for usersExperimental

Returns the account IDs for the users specified in the `key` or `username` parameters. Note that multiple `key` or `username` parameters can be specified.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**username**

array<string>

**key**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

array<UserMigrationBean>

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/user/bulk/migration

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/bulk/migration`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``[ { "username": "mia", "user_id": "5b10a2844c20165700ede21g" }, { "username": "emma", "user_id": "5b10ac8d82e05b22cc7d4ef5" } ]`

---

GET

## Get user default columns

Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If `user_id` is not passed in the request, the calling user's details are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the column details for any user.
  * Permission to access Jira, to get the calling user's column details.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user.columns:jira`, `read:filter.column:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**user_id**

string

**username**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ColumnItem>

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/user/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/columns?user_id=5b10ac8d82e05b22cc7d4ef5`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``[ { "label": "<string>", "value": "<string>" } ]`

---

PUT

## Set user default columns

Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If an account ID is not passed, the calling user's default columns are set. If no column details are sent, then all default columns are removed.

The parameters for this resource are expressed as HTML form data. For example, in curl:

`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/user/columns?user_id=5b10ac8d82e05b22cc7d4ef5'`

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.
  * Permission to access Jira, to set the calling user's columns.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:user.columns:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**user_id**

string

#### Request body*/* multipart/form-data

The ID of a column to set. To set multiple columns, send multiple `columns` parameters.

**columns**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

any

401Unauthorized

403Forbidden

404Not Found

429Too Many Requests

500Internal Server Error

PUT/rest/api/3/user/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/columns?user_id=5b10ac8d82e05b22cc7d4ef5`, { method: 'PUT', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Reset user default columns

Resets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user to the system default. If `user_id` is not passed, the calling user's default columns are reset.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.
  * Permission to access Jira, to set the calling user's columns.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:user.columns:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**user_id**

string

**username**

string

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

403Forbidden

DEL/rest/api/3/user/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/columns?user_id=5b10ac8d82e05b22cc7d4ef5`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get user email

Returns a user's email address regardless of the user's profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:email-address:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ACCESS_EMAIL_ADDRESSES`

### Request

#### Query parameters

**user_id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

UnrestrictedUserEmail

Show child properties

400Bad Request

401Unauthorized

404Not Found

503Service Unavailable

GET/rest/api/3/user/email

curl

Node.js

Java

Python

PHP

`1 2 3 4 ``curl --request GET \ --url 'https://your-domain.atlassian.net/rest/api/3/user/email?user_id={user_id}' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 ``{ "user_id": "<string>", "email": "<string>" }`

---

GET

## Get user email bulk

Returns a user's email address regardless of the user's profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:email-address:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ACCESS_EMAIL_ADDRESSES`

### Request

#### Query parameters

**user_id**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

UnrestrictedUserEmail

Show child properties

400Bad Request

401Unauthorized

503Service Unavailable

GET/rest/api/3/user/email/bulk

curl

Node.js

Java

Python

PHP

`1 2 3 4 ``curl --request GET \ --url 'https://your-domain.atlassian.net/rest/api/3/user/email/bulk?user_id={user_id}' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 ``{ "user_id": "<string>", "email": "<string>" }`

---

GET

## Get user groups

Returns the groups to which a user belongs.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:group:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**user_id**

string

Required

**username**

string

**key**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<GroupName>

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/user/groups

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/groups?user_id=5b10ac8d82e05b22cc7d4ef5`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }`

---

GET

## Get all users default

Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

403Forbidden

409Conflict

GET/rest/api/3/users

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/users`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``[ { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" }, { "user_id": "5b10ac8d82e05b22cc7d4ef5", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" }, "displayName": "Emma Richards", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10ac8d82e05b22cc7d4ef5" } ]`

---

GET

## Get all users

Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<User>

Show child properties

400Bad Request

403Forbidden

409Conflict

GET/rest/api/3/users/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/users/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``[ { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" }, { "user_id": "5b10ac8d82e05b22cc7d4ef5", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48" }, "displayName": "Emma Richards", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10ac8d82e05b22cc7d4ef5" } ]`