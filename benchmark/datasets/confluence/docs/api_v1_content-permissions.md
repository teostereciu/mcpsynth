# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-permissions/*

---

Cloud

Confluence Cloud / Reference / REST API

# Content permissions

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[POST/wiki/rest/api/content/{id}/permission/check](/cloud/confluence/rest/v1/api-group-content-permissions/#api-wiki-rest-api-content-id-permission-check-post)

---

POST

## Check content permissions

Check if a user or a group can perform an operation to the specified content. The `operation` to check must be provided. The userâs account ID or the ID of the group can be provided in the `subject` to check permissions against a specified user or group. The following permission checks are done to make sure that the user or group has the proper access:

  * site permissions
  * space permissions
  * content restrictions


**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission) if checking permission for self, otherwise 'Confluence Administrator' global permission is required.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.permission`

**Granular** :`read:content.permission:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

The content permission request.

**subject**

PermissionSubjectWithGroupId

Required

**operation**

string

Required

### Responses

200OK

Returned if the permission check completed successfully

#### application/json

PermissionCheckResponse

This object represents the response for the content permission check API. If the user or group does not have permissions, the following errors may be returned:

  * Group does not have permission to the space
  * Group does not have permission to the content
  * User is not allowed to use Confluence
  * User does not have permission to the space
  * User does not have permission to the content
  * Anonymous users are not allowed to use Confluence
  * Anonymous user does not have permission to the space
  * Anonymous user does not have permission to the content


Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/wiki/rest/api/content/{id}/permission/check

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "subject": { "type": "user", "identifier": "<string>" }, "operation": "read" }`; const response = await requestConfluence(`/wiki/rest/api/content/{id}/permission/check`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "hasPermission": true, "errors": [ { "translation": "<string>", "args": [ "<string>" ] } ], "_links": {} }`