# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-avatars/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project avatars

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents avatars associated with a project. Use it to get, load, set, and remove project avatars.

Operations

[PUT/rest/api/3/project/{projectIdOrKey}/avatar](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatar-put)[DEL/rest/api/3/project/{projectIdOrKey}/avatar/{id}](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatar-id-delete)[POST/rest/api/3/project/{projectIdOrKey}/avatar2](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatar2-post)[GET/rest/api/3/project/{projectIdOrKey}/avatars](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatars-get)

---

PUT

## Set project avatar

Sets the avatar displayed for a project.

Use [Load project avatar](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatar2-post) to store avatars against the project, before using this operation to set the displayed avatar.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project.avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Request bodyapplication/json

Expand all

**id**

string

Required

**Additional Properties**

any

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/project/{projectIdOrKey}/avatar

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "id": "10010" }`; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/avatar`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete project avatar

Deletes a custom avatar from a project. Note that system avatars cannot be deleted.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`delete:project.avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

Expand all

**projectIdOrKey**

string

Required

**id**

integer

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/project/{projectIdOrKey}/avatar/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/avatar/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Load project avatar

Loads an avatar for a project.

Specify the avatar's local file location in the body of the request. Also, include the following headers:

  * `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](/cloud/jira/platform/rest/v3/intro/#special-request-headers).
  * `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.


For example:
`curl --request POST `

`--user email@example.com:<api_token> `

`--header 'X-Atlassian-Token: no-check' `

`--header 'Content-Type: image/< image_type>' `

`--data-binary "<@/path/to/file/with/your/avatar>" `

`--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

After creating the avatar use [Set project avatar](/cloud/jira/platform/rest/v3/api-group-project-avatars/#api-rest-api-3-project-projectidorkey-avatar-put) to set it as the project's displayed avatar.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project.avatar:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

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

POST/rest/api/3/project/{projectIdOrKey}/avatar2

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/avatar2`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 ``{ "id": "1010", "isDeletable": true, "isSelected": false, "isSystemAvatar": false }`

---

GET

## Get all project avatars

Returns all project avatars, grouped by system and custom avatars.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project.avatar:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

200OK

Returned if request is successful.

#### application/json

ProjectAvatars

List of project avatars.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/avatars

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/avatars`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``{ "custom": [ { "id": "1010", "isDeletable": true, "isSelected": false, "isSystemAvatar": false, "urls": { "16x16": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10080&avatarType=project", "24x24": "https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10080&avatarType=project", "32x32": "https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10080&avatarType=project", "48x48": "https://your-domain.atlassian.net/secure/viewavatar?avatarId=10080&avatarType=project" } } ], "system": [ { "id": "1000", "isDeletable": false, "isSelected": false, "isSystemAvatar": true, "urls": { "16x16": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10040&avatarType=project", "24x24": "https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10040&avatarType=project", "32x32": "https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10040&avatarType=project", "48x48": "https://your-domain.atlassian.net/secure/viewavatar?avatarId=10040&avatarType=project" } } ] }`