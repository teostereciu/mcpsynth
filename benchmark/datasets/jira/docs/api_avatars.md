# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Avatars

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents system and custom avatars. Use it to obtain the details of system or custom avatars, add and remove avatars from a project, issue type or priority and obtain avatar images.

Operations

[GET/rest/api/3/avatar/{type}/system](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-avatar-type-system-get)[GET/rest/api/3/universal_avatar/type/{type}/owner/{entityId}](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-type-type-owner-entityid-get)[POST/rest/api/3/universal_avatar/type/{type}/owner/{entityId}](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-type-type-owner-entityid-post)[DEL/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-type-type-owner-owningobjectid-avatar-id-delete)[GET/rest/api/3/universal_avatar/view/type/{type}](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-view-type-type-get)[GET/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-view-type-type-avatar-id-get)[GET/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}](/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-view-type-type-owner-entityid-get)

---

GET

## Get system avatars by type

Returns a list of system avatar details by owner type, where the owner types are issue type, project, user or priority.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**type**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

SystemAvatars

List of system avatars.

Show child properties

401Unauthorized

500Internal Server Error

GET/rest/api/3/avatar/{type}/system

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/avatar/{type}/system`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "system": [ { "id": "1000", "isDeletable": false, "isSelected": false, "isSystemAvatar": true, "urls": { "16x16": "/secure/useravatar?size=xsmall&avatarId=10040&avatarType=project", "24x24": "/secure/useravatar?size=small&avatarId=10040&avatarType=project", "32x32": "/secure/useravatar?size=medium&avatarId=10040&avatarType=project", "48x48": "/secure/useravatar?avatarId=10040&avatarType=project" } } ] }`

---

GET

## Get avatars

Returns the system and custom avatars for a project, issue type or priority.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * for custom project avatars, _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
  * for custom issue type avatars, _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
  * for system avatars, none.
  * for priority avatars, none.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**type**

string

Required

**entityId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

Avatars

Details about system and custom avatars.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/universal_avatar/type/{type}/owner/{entityId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/universal_avatar/type/{type}/owner/{entityId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``{ "custom": [ { "id": "1010", "isDeletable": true, "isSelected": false, "isSystemAvatar": false, "urls": { "16x16": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10080&avatarType=project", "24x24": "https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10080&avatarType=project", "32x32": "https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10080&avatarType=project", "48x48": "https://your-domain.atlassian.net/secure/viewavatar?avatarId=10080&avatarType=project" } } ], "system": [ { "id": "1000", "isDeletable": false, "isSelected": false, "isSystemAvatar": true, "urls": { "16x16": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10040&avatarType=project", "24x24": "https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10040&avatarType=project", "32x32": "https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10040&avatarType=project", "48x48": "https://your-domain.atlassian.net/secure/viewavatar?avatarId=10040&avatarType=project" } } ] }`

---

POST

## Load avatar

Loads a custom avatar for a project, issue type or priority.

Specify the avatar's local file location in the body of the request. Also, include the following headers:

  * `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](/cloud/jira/platform/rest/v3/intro/#special-request-headers).
  * `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.


For example:
`curl --request POST `

`--user email@example.com:<api_token> `

`--header 'X-Atlassian-Token: no-check' `

`--header 'Content-Type: image/< image_type>' `

`--data-binary "<@/path/to/file/with/your/avatar>" `

`--url 'https://your-domain.atlassian.net/rest/api/3/universal_avatar/type/{type}/owner/{entityId}'`

The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

After creating the avatar use:

  * [Update issue type](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-put) to set it as the issue type's displayed avatar.
  * [Set project avatar](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatar-put) to set it as the project's displayed avatar.
  * [Update priority](/cloud/jira/platform/rest/v3/api-group-issue-priorities/#api-rest-api-3-priority-id-put) to set it as the priority's displayed avatar.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:avatar:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**type**

string

Required

**entityId**

string

Required

#### Query parameters

Expand all

**x**

integer

**y**

integer

**size**

integer

Required

#### Request body*/*

any

### Responses

201Created

Returned if the request is successful.

#### application/json

Avatar

Details of an avatar.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/universal_avatar/type/{type}/owner/{entityId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/universal_avatar/type/{type}/owner/{entityId}?size={size}`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 ``{ "id": "1010", "isDeletable": true, "isSelected": false, "isSystemAvatar": false }`

---

DEL

## Delete avatar

Deletes an avatar from a project, issue type or priority.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**type**

string

Required

**owningObjectId**

string

Required

**id**

integer

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

403Forbidden

404Not Found

DEL/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get avatar image by type

Returns the default project, issue type or priority avatar image.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**type**

string

Required

#### Query parameters

Expand all

**size**

string

**format**

string

### Responses

200OK

Returned if the request is successful.

#### */* image/png image/svg+xml

any

#### application/json

StreamingResponseBody

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/universal_avatar/view/type/{type}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/universal_avatar/view/type/{type}?size={size}&format={format}`, { headers: { 'Accept': '*/*' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get avatar image by ID

Returns a project, issue type or priority avatar image by ID.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * For system avatars, none.
  * For custom project avatars, _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
  * For custom issue type avatars, _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
  * For priority avatars, none.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**type**

string

Required

**id**

integer

Required

#### Query parameters

Expand all

**size**

string

**format**

string

### Responses

200OK

Returned if the request is successful.

#### */* image/png image/svg+xml

any

#### application/json

StreamingResponseBody

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}?size={size}&format={format}`, { headers: { 'Accept': '*/*' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get avatar image by owner

Returns the avatar image for a project, issue type or priority.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * For system avatars, none.
  * For custom project avatars, _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
  * For custom issue type avatars, _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
  * For priority avatars, none.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**type**

string

Required

**entityId**

string

Required

#### Query parameters

Expand all

**size**

string

**format**

string

### Responses

200OK

Returned if the request is successful.

#### */* image/png image/svg+xml

any

#### application/json

StreamingResponseBody

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}?size={size}&format={format}`, { headers: { 'Accept': '*/*' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`