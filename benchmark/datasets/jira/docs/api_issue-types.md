# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-types/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue types

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issues types. Use it to:

  * get, create, update, and delete issue types.
  * get all issue types for a user.
  * get alternative issue types.
  * set an avatar for an issue type.


Operations

[GET/rest/api/3/issuetype](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-get)[POST/rest/api/3/issuetype](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-post)[GET/rest/api/3/issuetype/project](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-project-get)[GET/rest/api/3/issuetype/{id}](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-get)[PUT/rest/api/3/issuetype/{id}](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-put)[DEL/rest/api/3/issuetype/{id}](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-delete)[GET/rest/api/3/issuetype/{id}/alternatives](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-alternatives-get)[POST/rest/api/3/issuetype/{id}/avatar2](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-avatar2-post)

---

GET

## Get all issue types for user

Returns all issue types.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Issue types are only returned as follows:

  * if the user has the _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
  * if the user has the _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.
  * if the user is anonymous then they will be able to access projects with the _Browse projects_ for anonymous users
  * if the user authentication is incorrect they will fall back to anonymous


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:avatar:jira`, `read:project-category:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<IssueTypeDetails>

Show child properties

GET/rest/api/3/issuetype

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``[ { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }, { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false } ]`

---

POST

## Create issue type

Creates an issue type.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type:jira`, `read:avatar:jira`, `read:issue-type:jira`, `read:project-category:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**description**

string

**hierarchyLevel**

integer

**name**

string

Required

**type**

string

### Responses

201Created

Returned if the request is successful.

#### application/json

IssueTypeDetails

Details about an issue type.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

409Conflict

POST/rest/api/3/issuetype

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "description", "name": "name", "type": "standard" }`; const response = await requestJira(`/rest/api/3/issuetype`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "avatarId": 34, "description": "<string>", "entityId": "<string>", "hierarchyLevel": 34, "iconUrl": "<string>", "id": "<string>", "name": "<string>", "scope": { "project": { "avatarUrls": {}, "id": "<string>", "key": "<string>", "name": "<string>", "projectCategory": {}, "projectTypeKey": "software", "self": "<string>", "simplified": true }, "type": "PROJECT" }, "self": "<string>", "subtask": true }`

---

GET

## Get issue types for projectExperimental

Returns issue types for a project.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:avatar:jira`, `read:project-category:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**projectId**

integer

Required

**level**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

array<IssueTypeDetails>

Show child properties

400Bad Request

404Not Found

GET/rest/api/3/issuetype/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/project?projectId={projectId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``[ { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false }, { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false } ]`

---

GET

## Get issue type

Returns an issue type.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated with or _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:avatar:jira`, `read:project-category:jira`, `read:project:jira`

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

IssueTypeDetails

Details about an issue type.

Show child properties

400Bad Request

404Not Found

GET/rest/api/3/issuetype/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }`

---

PUT

## Update issue type

Updates the issue type.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type:jira`, `read:avatar:jira`, `read:issue-type:jira`, `read:project-category:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**avatarId**

integer

**description**

string

**name**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueTypeDetails

Details about an issue type.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

PUT/rest/api/3/issuetype/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "avatarId": 1, "description": "description", "name": "name" }`; const response = await requestJira(`/rest/api/3/issuetype/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``{ "avatarId": 34, "description": "<string>", "entityId": "<string>", "hierarchyLevel": 34, "iconUrl": "<string>", "id": "<string>", "name": "<string>", "scope": { "project": { "avatarUrls": {}, "id": "<string>", "key": "<string>", "name": "<string>", "projectCategory": {}, "projectTypeKey": "software", "self": "<string>", "simplified": true }, "type": "PROJECT" }, "self": "<string>", "subtask": true }`

---

DEL

## Delete issue type

Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (`alternativeIssueTypeId`). A list of alternative issue types are obtained from the [Get alternative issue types](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-alternatives-get) resource.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:issue-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**alternativeIssueTypeId**

string

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

423Locked

DEL/rest/api/3/issuetype/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get alternative issue types

Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:project-category:jira`, `read:project:jira`, `read:avatar:jira`

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

array<IssueTypeDetails>

Show child properties

404Not Found

GET/rest/api/3/issuetype/{id}/alternatives

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{id}/alternatives`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``[ { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }, { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false } ]`

---

POST

## Load issue type avatar

Loads an avatar for the issue type.

Specify the avatar's local file location in the body of the request. Also, include the following headers:

  * `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](/cloud/jira/platform/rest/v3/intro/#special-request-headers).
  * `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.


For example:
`curl --request POST \ --user email@example.com:<api_token> \ --header 'X-Atlassian-Token: no-check' \ --header 'Content-Type: image/< image_type>' \ --data-binary "<@/path/to/file/with/your/avatar>" \ --url 'https://your-domain.atlassian.net/rest/api/3/issuetype/{issueTypeId}'This`

The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

After creating the avatar, use [ Update issue type](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-rest-api-3-issuetype-id-put) to set it as the issue type's displayed avatar.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:avatar:jira`, `write:issue-type:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

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

POST/rest/api/3/issuetype/{id}/avatar2

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{id}/avatar2?size={size}`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 ``{ "id": "1010", "isDeletable": true, "isSelected": false, "isSystemAvatar": false }`