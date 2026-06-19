# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-announcement-banner/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Announcement banner

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents an announcement banner. Use it to retrieve and update banner configuration.

Operations

[GET/rest/api/3/announcementBanner](/cloud/jira/platform/rest/v3/api-group-announcement-banner/#api-rest-api-3-announcementbanner-get)[PUT/rest/api/3/announcementBanner](/cloud/jira/platform/rest/v3/api-group-announcement-banner/#api-rest-api-3-announcementbanner-put)

---

GET

## Get announcement banner configuration

Returns the current announcement banner configuration.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

AnnouncementBannerConfiguration

Announcement banner configuration.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/announcementBanner

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/announcementBanner`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "hashId": "9HN2FJK9DM8BHRWERVW3RRTGDJ4G4D5C", "isDismissible": false, "isEnabled": true, "message": "This is a public, enabled, non-dismissible banner, set using the API", "visibility": "public" }`

---

PUT

## Update announcement banner configuration

Updates the announcement banner configuration.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**isDismissible**

boolean

**isEnabled**

boolean

**message**

string

**visibility**

string

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

PUT/rest/api/3/announcementBanner

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "isDismissible": false, "isEnabled": true, "message": "This is a public, enabled, non-dismissible banner, set using the API", "visibility": "public" }`; const response = await requestJira(`/rest/api/3/announcementBanner`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`