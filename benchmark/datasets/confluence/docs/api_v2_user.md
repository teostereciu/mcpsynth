# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-user/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# User

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[POST/users-bulk](/cloud/confluence/rest/v2/api-group-user/#api-users-bulk-post)[POST/user/access/check-access-by-email](/cloud/confluence/rest/v2/api-group-user/#api-user-access-check-access-by-email-post)[POST/user/access/invite-by-email](/cloud/confluence/rest/v2/api-group-user/#api-user-access-invite-by-email-post)

---

POST

## Create bulk user lookup using ids

Returns user details for the ids provided in the request body.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission). The user must be able to view user profiles in the Confluence site.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:user:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

**accountIds**

array<string>

Required

### Responses

200OK

Returned if the user info is returned for the account IDs. `results` may be empty if no account IDs were found.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<User>

Show child properties

400Bad Request

404Not Found

POST/users-bulk

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "accountIds": [ "<string>" ] }`; const response = await requestConfluence(`/wiki/api/v2/users-bulk`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``{ "results": [ { "displayName": "<string>", "timeZone": "<string>", "personalSpaceId": "<string>", "isExternalCollaborator": true, "accountStatus": "active", "accountId": "<string>", "email": "<string>", "accountType": "atlassian", "publicName": "<string>", "profilePicture": { "path": "<string>", "isDefault": true } } ], "_links": { "next": "<string>", "base": "<string>" } }`

---

POST

## Check site access for a list of emailsExperimental

Returns the list of emails from the input list that do not have access to site.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `NONE`

### Request

#### Request bodyapplication/json

**emails**

array<string>

Required

### Responses

200OK

Returns object with list of emails without access to site.

#### application/json

object

Show child properties

400Bad Request

401Unauthorized

404Not Found

503Service Unavailable

POST/user/access/check-access-by-email

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "emails": [ "<string>" ] }`; const response = await requestConfluence(`/wiki/api/v2/user/access/check-access-by-email`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "emailsWithoutAccess": [ "<string>" ], "invalidEmails": [ "<string>" ] }`

---

POST

## Invite a list of emails to the siteExperimental

Invite a list of emails to the site.

Ignores all invalid emails and no action is taken for the emails that already have access to the site.

**NOTE:** This API is asynchronous and may take some time to complete.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `NONE`

### Request

#### Request bodyapplication/json

**emails**

array<string>

Required

### Responses

200OK

Returns object with list of emails without access to site.

400Bad Request

401Unauthorized

404Not Found

503Service Unavailable

POST/user/access/invite-by-email

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "emails": [ "<string>" ] }`; const response = await requestConfluence(`/wiki/api/v2/user/access/invite-by-email`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`