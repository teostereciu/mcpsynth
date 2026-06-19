# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-myself/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Myself

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents information about the current user, such as basic details, group membership, application roles, preferences, and locale. Use it to get, create, update, and delete (restore default) values of the user's preferences and locale.

Operations

[GET/rest/api/3/mypreferences](/cloud/jira/platform/rest/v3/api-group-myself/#api-rest-api-3-mypreferences-get)[PUT/rest/api/3/mypreferences](/cloud/jira/platform/rest/v3/api-group-myself/#api-rest-api-3-mypreferences-put)[DEL/rest/api/3/mypreferences](/cloud/jira/platform/rest/v3/api-group-myself/#api-rest-api-3-mypreferences-delete)[GET/rest/api/3/mypreferences/locale](/cloud/jira/platform/rest/v3/api-group-myself/#api-rest-api-3-mypreferences-locale-get)[PUT/rest/api/3/mypreferences/locale](/cloud/jira/platform/rest/v3/api-group-myself/#api-rest-api-3-mypreferences-locale-put)[GET/rest/api/3/myself](/cloud/jira/platform/rest/v3/api-group-myself/#api-rest-api-3-myself-get)

---

GET

## Get preference

Returns the value of a preference of the current user.

Note that these keys are deprecated:

  * _jira.user.locale_ The locale of the user. By default this is not set and the user takes the locale of the instance.
  * _jira.user.timezone_ The time zone of the user. By default this is not set and the user takes the timezone of the instance.


These system preferences keys will be deprecated by 15/07/2024. You can still retrieve these keys, but it will not have any impact on Notification behaviour.

  * _user.notifications.watcher_ Whether the user gets notified when they are watcher.
  * _user.notifications.assignee_ Whether the user gets notified when they are assignee.
  * _user.notifications.reporter_ Whether the user gets notified when they are reporter.
  * _user.notifications.mentions_ Whether the user gets notified when they are mentions.


Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ACT_AS_USER`

### Request

#### Query parameters

**key**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

string

401Unauthorized

404Not Found

GET/rest/api/3/mypreferences

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/mypreferences?key={key}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 ``"<string>"`

---

PUT

## Set preference

Creates a preference for the user or updates a preference's value by sending a plain text string. For example, `false`. An arbitrary preference can be created with the value containing up to 255 characters. In addition, the following keys define system preferences that can be set or created:

  * _user.notifications.mimetype_ The mime type used in notifications sent to the user. Defaults to `html`.
  * _user.default.share.private_ Whether new [ filters](https://confluence.atlassian.com/x/eQiiLQ) are set to private. Defaults to `true`.
  * _user.keyboard.shortcuts.disabled_ Whether keyboard shortcuts are disabled. Defaults to `false`.
  * _user.autowatch.disabled_ Whether the user automatically watches issues they create or add a comment to. By default, not set: the user takes the instance autowatch setting.
  * _user.notifiy.own.changes_ Whether the user gets notified of their own changes.


Note that these keys are deprecated:

  * _jira.user.locale_ The locale of the user. By default, not set. The user takes the instance locale.
  * _jira.user.timezone_ The time zone of the user. By default, not set. The user takes the instance timezone.


These system preferences keys will be deprecated by 15/07/2024. You can still use these keys to create arbitrary preferences, but it will not have any impact on Notification behaviour.

  * _user.notifications.watcher_ Whether the user gets notified when they are watcher.
  * _user.notifications.assignee_ Whether the user gets notified when they are assignee.
  * _user.notifications.reporter_ Whether the user gets notified when they are reporter.
  * _user.notifications.mentions_ Whether the user gets notified when they are mentions.


Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:user-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ACT_AS_USER`

### Request

#### Query parameters

**key**

string

Required

#### Request bodyapplication/json text/plain

The value of the preference as a plain text string. The maximum length is 255 characters.

string

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

401Unauthorized

404Not Found

PUT/rest/api/3/mypreferences

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `"<string>"`; const response = await requestJira(`/rest/api/3/mypreferences?key={key}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete preference

Deletes a preference of the user, which restores the default value of system defined settings.

Note that these keys are deprecated:

  * _jira.user.locale_ The locale of the user. By default, not set. The user takes the instance locale.
  * _jira.user.timezone_ The time zone of the user. By default, not set. The user takes the instance timezone.


Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:user-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ACT_AS_USER`

### Request

#### Query parameters

**key**

string

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

404Not Found

DEL/rest/api/3/mypreferences

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/mypreferences?key={key}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get locale

Returns the locale for the user.

If the user has no language preference set (which is the default setting) or this resource is accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale using the _Accept-Language_ header in the request. However, if this doesn't match a locale available Jira, the site default locale is returned.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:user-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ACT_AS_USER`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

Locale

Details of a locale.

Show child properties

401Unauthorized

GET/rest/api/3/mypreferences/locale

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/mypreferences/locale`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "locale": "en_US" }`

---

PUT

## Set localeDeprecated

Deprecated, use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API instead.

Sets the locale of the user. The locale must be one supported by the instance of Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The locale defined in a LocaleBean.

**locale**

string

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

PUT/rest/api/3/mypreferences/locale

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 ``curl --request PUT \ --url 'https://your-domain.atlassian.net/rest/api/3/mypreferences/locale' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json' \ --header 'Content-Type: application/json' \ --data '{ "locale": "en_US" }'`

---

GET

## Get current user

Returns details for the current user.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:application-role:jira`, `read:group:jira`, `read:user:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

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

GET/rest/api/3/myself

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/myself`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }`