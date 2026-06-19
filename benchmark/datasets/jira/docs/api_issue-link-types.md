# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-link-types/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue link types

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [issue link](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-group-issue-links) types. Use it to get, create, update, and delete link issue types as well as get lists of all link issue types.

To use it, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

Operations

[GET/rest/api/3/issueLinkType](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-get)[POST/rest/api/3/issueLinkType](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-post)[GET/rest/api/3/issueLinkType/{issueLinkTypeId}](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-issuelinktypeid-get)[PUT/rest/api/3/issueLinkType/{issueLinkTypeId}](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-issuelinktypeid-put)[DEL/rest/api/3/issueLinkType/{issueLinkTypeId}](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-issuelinktypeid-delete)

---

GET

## Get issue link types

Returns a list of all issue link types.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-link-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueLinkTypes

A list of issue link type beans.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/issueLinkType

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issueLinkType`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``{ "issueLinkTypes": [ { "id": "1000", "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates", "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000" }, { "id": "1010", "inward": "Blocked by", "name": "Blocks", "outward": "Blocks", "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1010" } ] }`

---

POST

## Create issue link type

Creates an issue link type. Use this operation to create descriptions of the reasons why issues are linked. The issue link type consists of a name and descriptions for a link's inward and outward relationships.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-link-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

**id**

string

**inward**

string

**name**

string

**outward**

string

### Responses

201Created

Returned if the request is successful.

#### application/json

IssueLinkType

This object is used as follows:

  * In the [ issueLink](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-rest-api-3-issuelink-post) resource it defines and reports on the type of link between the issues. Find a list of issue link types with [Get issue link types](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-get).
  * In the [ issueLinkType](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-post) resource it defines and reports on issue link types.


Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/issueLinkType

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates" }`; const response = await requestJira(`/rest/api/3/issueLinkType`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 ``{ "id": "1000", "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates", "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000" }`

---

GET

## Get issue link type

Returns an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-link-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**issueLinkTypeId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueLinkType

This object is used as follows:

  * In the [ issueLink](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-rest-api-3-issuelink-post) resource it defines and reports on the type of link between the issues. Find a list of issue link types with [Get issue link types](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-get).
  * In the [ issueLinkType](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-post) resource it defines and reports on issue link types.


Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/issueLinkType/{issueLinkTypeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issueLinkType/{issueLinkTypeId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "id": "1000", "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates", "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000" }`

---

PUT

## Update issue link type

Updates an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-link-type:jira`, `write:issue-link-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueLinkTypeId**

string

Required

#### Request bodyapplication/json

Expand all

**id**

string

**inward**

string

**name**

string

**outward**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueLinkType

This object is used as follows:

  * In the [ issueLink](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-rest-api-3-issuelink-post) resource it defines and reports on the type of link between the issues. Find a list of issue link types with [Get issue link types](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-get).
  * In the [ issueLinkType](/cloud/jira/platform/rest/v3/api-group-issue-link-types/#api-rest-api-3-issuelinktype-post) resource it defines and reports on issue link types.


Show child properties

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/issueLinkType/{issueLinkTypeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates" }`; const response = await requestJira(`/rest/api/3/issueLinkType/{issueLinkTypeId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "id": "1000", "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates", "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000" }`

---

DEL

## Delete issue link type

Deletes an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:issue-link-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**issueLinkTypeId**

string

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/issueLinkType/{issueLinkTypeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issueLinkType/{issueLinkTypeId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`