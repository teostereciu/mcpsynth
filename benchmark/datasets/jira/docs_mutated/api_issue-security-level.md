# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-security-level/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue security level

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue security levels. Use it to obtain the details of any issue security level. For more information about issue security levels, see [Configuring issue-level security](https://confluence.atlassian.com/x/J4lKLg).

Operations

[GET/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members](/cloud/jira/platform/rest/v3/api-group-issue-security-level/#api-rest-api-3-issuesecurityschemes-issuesecurityschemeid-members-get)[GET/rest/api/3/securitylevel/{id}](/cloud/jira/platform/rest/v3/api-group-issue-security-level/#api-rest-api-3-securitylevel-id-get)

---

GET

## Get issue security level members by issue security scheme

Returns issue security level members.

Only issue security level members in context of classic projects are returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`, `read:issue-security-level:jira`, `read:project-role:jira`, `read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**issueSecuritySchemeId**

integer

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**issueSecurityLevelId**

array<string>

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanIssueSecurityLevelMember

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``{ "isLast": true, "page_size": 100, "start_index": 0, "total": 3, "values": [ { "id": 10000, "issueSecurityLevelId": 10020, "holder": { "expand": "user", "type": "user", "user": { "user_id": "5b10a2844c20165700ede21g", "active": true, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" } } }, { "id": 10001, "issueSecurityLevelId": 10020, "holder": { "expand": "group", "parameter": "jira-core-users", "type": "group", "value": "9c559b11-6c5d-4f96-992c-a746cabab28b" } }, { "id": 10002, "issueSecurityLevelId": 10021, "holder": { "type": "assignee" } } ] }`

---

GET

## Get issue security level

Returns details of an issue security level.

Use [Get issue security scheme](/cloud/jira/platform/rest/v3/api-group-issue-security-schemes/#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`, `read:issue-security-level:jira`, `read:project-role:jira`, `read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

SecurityLevel

Details of an issue level security item.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/securitylevel/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/securitylevel/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "description": "Only the reporter and internal staff can see this issue.", "id": "10021", "name": "Reporter Only", "self": "https://your-domain.atlassian.net/rest/api/3/securitylevel/10021" }`