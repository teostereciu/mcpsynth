# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-audit/*

---

Cloud

Confluence Cloud / Reference / REST API

# Audit

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/audit](/cloud/confluence/rest/v1/api-group-audit/#api-wiki-rest-api-audit-get)[POST/wiki/rest/api/audit](/cloud/confluence/rest/v1/api-group-audit/#api-wiki-rest-api-audit-post)[GET/wiki/rest/api/audit/export](/cloud/confluence/rest/v1/api-group-audit/#api-wiki-rest-api-audit-export-get)[GET/wiki/rest/api/audit/retention](/cloud/confluence/rest/v1/api-group-audit/#api-wiki-rest-api-audit-retention-get)[PUT/wiki/rest/api/audit/retention](/cloud/confluence/rest/v1/api-group-audit/#api-wiki-rest-api-audit-retention-put)[GET/wiki/rest/api/audit/since](/cloud/confluence/rest/v1/api-group-audit/#api-wiki-rest-api-audit-since-get)

---

GET

## Get audit records

Returns all records in the audit log, optionally for a certain date range. This contains information about events like space exports, group membership changes, app installations, etc. For more information, see [Audit log](https://confluence.atlassian.com/confcloud/audit-log-802164269.html) in the Confluence administrator's guide.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:audit-log:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**startDate**

string

**endDate**

string

**searchString**

string

**offset**

integer

**max_results**

integer

### Responses

200OK

Returned if the requested records are returned.

#### application/json

AuditRecordArray

Show child properties

401Unauthorized

403Forbidden

GET/wiki/rest/api/audit

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/audit`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``{ "results": [ { "author": { "type": "user", "displayName": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "publicName": "<string>" }, "remoteAddress": "<string>", "creationDate": 59, "summary": "<string>", "description": "<string>", "category": "<string>", "sysAdmin": true, "superAdmin": true, "affectedObject": { "name": "<string>", "objectType": "<string>" }, "changedValues": [ { "name": "<string>", "oldValue": "<string>", "hiddenOldValue": "<string>", "newValue": "<string>", "hiddenNewValue": "<string>" } ], "associatedObjects": [ { "name": "<string>", "objectType": "<string>" } ] } ], "offset": 2154, "max_results": 2154, "size": 2154, "_links": {} }`

---

POST

## Create audit record

Creates a record in the audit log.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:audit-log:confluence`, `write:audit-log:confluence`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The record to be created in the audit log.

**author**

object

**remoteAddress**

string

Required

**creationDate**

integer

**summary**

string

**description**

string

**category**

string

**sysAdmin**

boolean

**affectedObject**

AffectedObject

**changedValues**

array<ChangedValue>

**associatedObjects**

array<AffectedObject>

### Responses

200OK

Returned if the record is created in the audit log.

#### application/json

AuditRecord

Show child properties

400Bad Request

401Unauthorized

POST/wiki/rest/api/audit

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "author": { "type": "user", "displayName": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "username": "<string>", "userKey": "<string>" }, "remoteAddress": "<string>", "creationDate": 226, "summary": "<string>", "description": "<string>", "category": "<string>", "sysAdmin": true, "affectedObject": { "name": "<string>", "objectType": "<string>" }, "changedValues": [ { "name": "<string>", "oldValue": "<string>", "hiddenOldValue": "<string>", "newValue": "<string>", "hiddenNewValue": "<string>" } ], "associatedObjects": [ { "name": "<string>", "objectType": "<string>" } ] }`; const response = await requestConfluence(`/wiki/rest/api/audit`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 ``{ "author": { "type": "user", "displayName": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "publicName": "<string>" }, "remoteAddress": "<string>", "creationDate": 59, "summary": "<string>", "description": "<string>", "category": "<string>", "sysAdmin": true, "superAdmin": true, "affectedObject": { "name": "<string>", "objectType": "<string>" }, "changedValues": [ { "name": "<string>", "oldValue": "<string>", "hiddenOldValue": "<string>", "newValue": "<string>", "hiddenNewValue": "<string>" } ], "associatedObjects": [ { "name": "<string>", "objectType": "<string>" } ] }`

---

GET

## Export audit records

Exports audit records as a CSV file or ZIP file.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:audit-log:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**startDate**

string

**endDate**

string

**searchString**

string

**format**

string

### Responses

200OK

Returned if the requested export of the audit records is returned.

#### application/zip text/csv

string

403Forbidden

GET/wiki/rest/api/audit/export

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/audit/export`, { headers: { 'Accept': 'application/zip' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get retention period

Returns the retention period for records in the audit log. The retention period is how long an audit record is kept for, from creation date until it is deleted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:audit-log:confluence`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the requested retention period is returned.

#### application/json

RetentionPeriod

Show child properties

403Forbidden

GET/wiki/rest/api/audit/retention

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/audit/retention`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "number": 45, "units": "NANOS" }`

---

PUT

## Set retention period

Sets the retention period for records in the audit log. The retention period can be set to a maximum of 1 year.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:audit-log:confluence`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The updated retention period.

**number**

integer

Required

**units**

string

Required

### Responses

200OK

Returned if the retention period is updated.

#### application/json

RetentionPeriod

Show child properties

403Forbidden

PUT/wiki/rest/api/audit/retention

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "number": 45, "units": "NANOS" }`; const response = await requestConfluence(`/wiki/rest/api/audit/retention`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "number": 45, "units": "NANOS" }`

---

GET

## Get audit records for time period

Returns records from the audit log, for a time period back from the current date. For example, you can use this method to get the last 3 months of records.

This contains information about events like space exports, group membership changes, app installations, etc. For more information, see [Audit log](https://confluence.atlassian.com/confcloud/audit-log-802164269.html) in the Confluence administrator's guide.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Confluence Administrator' global permission.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:audit-log:confluence`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**number**

integer

**units**

string

**searchString**

string

**offset**

integer

**max_results**

integer

### Responses

200OK

Returned if the requested records are returned.

#### application/json

AuditRecordArray

Show child properties

403Forbidden

GET/wiki/rest/api/audit/since

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/audit/since`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``{ "results": [ { "author": { "type": "user", "displayName": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "publicName": "<string>" }, "remoteAddress": "<string>", "creationDate": 59, "summary": "<string>", "description": "<string>", "category": "<string>", "sysAdmin": true, "superAdmin": true, "affectedObject": { "name": "<string>", "objectType": "<string>" }, "changedValues": [ { "name": "<string>", "oldValue": "<string>", "hiddenOldValue": "<string>", "newValue": "<string>", "hiddenNewValue": "<string>" } ], "associatedObjects": [ { "name": "<string>", "objectType": "<string>" } ] } ], "offset": 2154, "max_results": 2154, "size": 2154, "_links": {} }`