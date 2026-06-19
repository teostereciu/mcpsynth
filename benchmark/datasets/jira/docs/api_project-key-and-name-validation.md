# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project key and name validation

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource provides validation for project keys and names.

Operations

[GET/rest/api/3/projectvalidate/key](/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/#api-rest-api-3-projectvalidate-key-get)[GET/rest/api/3/projectvalidate/validProjectKey](/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/#api-rest-api-3-projectvalidate-validprojectkey-get)[GET/rest/api/3/projectvalidate/validProjectName](/cloud/jira/platform/rest/v3/api-group-project-key-and-name-validation/#api-rest-api-3-projectvalidate-validprojectname-get)

---

GET

## Validate project key

Validates a project key by confirming the key is a valid string and not in use.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**key**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

ErrorCollection

Error messages from an operation.

Show child properties

401Unauthorized

GET/rest/api/3/projectvalidate/key

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projectvalidate/key?key=HSP`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 ``{ "errorMessages": [], "errors": { "projectKey": "A project with that project key already exists." } }`

---

GET

## Get valid project key

Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**key**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

string

401Unauthorized

GET/rest/api/3/projectvalidate/validProjectKey

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projectvalidate/validProjectKey?key=HSP`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 ``"VPNE"`

---

GET

## Get valid project name

Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**name**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

string

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/projectvalidate/validProjectName

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/projectvalidate/validProjectName?name={name}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 ``"Valid Project Name Example"`