# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-application-roles/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Application roles

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents application roles. Use it to get details of an application role or all application roles.

Operations

[GET/rest/api/3/applicationrole](/cloud/jira/platform/rest/v3/api-group-application-roles/#api-rest-api-3-applicationrole-get)[GET/rest/api/3/applicationrole/{key}](/cloud/jira/platform/rest/v3/api-group-application-roles/#api-rest-api-3-applicationrole-key-get)

---

GET

## Get all application roles

Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:application-role:jira`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ApplicationRole>

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/applicationrole

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/applicationrole`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 ``[ { "defaultGroups": [ "jira-software-users" ], "defaultGroupsDetails": [ { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-software-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" } ], "defined": false, "groupDetails": [ { "groupId": "42c8955c-63d7-42c8-9520-63d7aca0625", "name": "jira-testers", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=42c8955c-63d7-42c8-9520-63d7aca0625" }, { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-software-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" } ], "groups": [ "jira-software-users", "jira-testers" ], "hasUnlimitedSeats": false, "key": "jira-software", "name": "Jira Software", "numberOfSeats": 10, "platform": false, "remainingSeats": 5, "selectedByDefault": false, "userCount": 5, "userCountDescription": "5 developers" }, { "defaultGroups": [ "jira-core-users" ], "defaultGroupsDetails": [ { "groupId": "92d01dca0625-42c8-42c8-9520-276f955c", "name": "jira-core-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=92d01dca0625-42c8-42c8-9520-276f955c" } ], "defined": false, "groupDetails": [ { "groupId": "92d01dca0625-42c8-42c8-9520-276f955c", "name": "jira-core-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=92d01dca0625-42c8-42c8-9520-276f955c" } ], "groups": [ "jira-core-users" ], "hasUnlimitedSeats": false, "key": "jira-core", "name": "Jira Core", "numberOfSeats": 1, "platform": true, "remainingSeats": 1, "selectedByDefault": false, "userCount": 0, "userCountDescription": "0 users" } ]`

---

GET

## Get application role

Returns an application role.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:application-role:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**key**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ApplicationRole

Details of an application role.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/applicationrole/{key}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/applicationrole/{key}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``{ "defaultGroups": [ "jira-software-users" ], "defaultGroupsDetails": [ { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-software-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" } ], "defined": false, "groupDetails": [ { "groupId": "42c8955c-63d7-42c8-9520-63d7aca0625", "name": "jira-testers", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=42c8955c-63d7-42c8-9520-63d7aca0625" }, { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-software-users", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" } ], "groups": [ "jira-software-users", "jira-testers" ], "hasUnlimitedSeats": false, "key": "jira-software", "name": "Jira Software", "numberOfSeats": 10, "platform": false, "remainingSeats": 5, "selectedByDefault": false, "userCount": 5, "userCountDescription": "5 developers" }`