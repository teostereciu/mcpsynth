# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-audit-records/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Audit records

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents audits that record activities undertaken in Jira. Use it to get a list of audit records.

Operations

[GET/rest/api/3/auditing/record](/cloud/jira/platform/rest/v3/api-group-audit-records/#api-rest-api-3-auditing-record-get)

---

GET

## Get audit records

Returns a list of audit records. The list can be filtered to include items:

  * where each item in `filter` has at least one match in any of these fields:

    * `summary`
    * `category`
    * `eventSource`
    * `objectItem.name` If the object is a user, account ID is available to filter.
    * `objectItem.parentName`
    * `objectItem.typeName`
    * `changedValues.changedFrom`
    * `changedValues.changedTo`
    * `remoteAddress`

For example, if `filter` contains _man ed_ , an audit record containing `summary": "User added to group"` and `"category": "group management"` is returned.

  * created on or after a date and time.

  * created or or before a date and time.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:audit-log:jira`, `read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**offset**

integer

**limit**

integer

**filter**

string

**from**

string

**to**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

AuditRecords

Container for a list of audit records.

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/auditing/record

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/auditing/record`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``{ "limit": 1000, "offset": 0, "records": [ { "associatedItems": [ { "id": "jira-software-users", "name": "jira-software-users", "parentId": "1", "parentName": "Jira Internal Directory", "typeName": "GROUP" } ], "authorAccountId": "5ab8f18d741e9c2c7e9d4538", "authorKey": "administrator", "category": "user management", "changedValues": [ { "changedFrom": "user@atlassian.com", "changedTo": "newuser@atlassian.com", "fieldName": "email" } ], "created": "2014-03-19T18:45:42.967+0000", "description": "Optional description", "eventSource": "Jira Connect Plugin", "id": 1, "objectItem": { "id": "user", "name": "user", "parentId": "1", "parentName": "Jira Internal Directory", "typeName": "USER" }, "remoteAddress": "192.168.1.1", "summary": "User created" } ], "total": 1 }`