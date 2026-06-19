# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-email/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project email

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the email address used to send a project's notifications. Use it to get and set the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

Operations

[GET/rest/api/3/project/{projectId}/email](/cloud/jira/platform/rest/v3/api-group-project-email/#api-rest-api-3-project-projectid-email-get)[PUT/rest/api/3/project/{projectId}/email](/cloud/jira/platform/rest/v3/api-group-project-email/#api-rest-api-3-project-projectid-email-put)

---

GET

## Get project's sender email

Returns the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:project.email:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectId**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectEmailAddress

A project's sender email address.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/project/{projectId}/email

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectId}/email`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "emailAddress": "jira@example.customdomain.com", "emailAddressStatus": [ "Email address or domain not verified." ] }`

---

PUT

## Set project's sender email

Sets the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

If `emailAddress` is an empty string, the default email address is restored.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission.](https://confluence.atlassian.com/x/yodKLg)

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project.email:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectId**

integer

Required

#### Request bodyapplication/json

Expand all

The project's sender email address to be set.

**emailAddress**

string

**emailAddressStatus**

array<string>

### Responses

204No Content

Returned if the project's sender email address is successfully set.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/project/{projectId}/email

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "emailAddress": "jira@example.atlassian.net" }`; const response = await requestJira(`/rest/api/3/project/{projectId}/email`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`