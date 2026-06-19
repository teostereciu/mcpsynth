# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-data-policies/*

---

Cloud

Confluence Cloud / Reference / REST API v2

# Data Policies

[Postman Collection](/cloud/confluence/confcloud.2.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json?_v=1.8494.0)

Operations

[GET/data-policies/metadata](/cloud/confluence/rest/v2/api-group-data-policies/#api-data-policies-metadata-get)[GET/data-policies/spaces](/cloud/confluence/rest/v2/api-group-data-policies/#api-data-policies-spaces-get)

---

GET

## Get data policy metadata for the workspaceExperimental

Returns data policy metadata for the workspace.

**[Permissions](/cloud/confluence/rest/v2/intro/#permissions) required:** Only apps can make this request. Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

DataPolicyMetadata

Details about data policies.

Show child properties

400Bad Request

401Unauthorized

GET/data-policies/metadata

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/data-policies/metadata`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "anyContentBlocked": true }`

---

GET

## Get spaces with data policiesExperimental

Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the `max_results` parameter and additional results (if available) will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Only apps can make this request. Permission to access the Confluence site ('Can use' global permission). Only spaces that the app has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:space:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**ids**

array<integer>

**keys**

array<string>

**sort**

SpaceSortOrder

**cursor**

string

**max_results**

integer

### Responses

200OK

Returned if the requested spaces are returned.

#### Headers

**Link**

string

#### application/json

MultiEntityResult<DataPolicySpace>

Show child properties

400Bad Request

401Unauthorized

GET/data-policies/spaces

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/api/v2/data-policies/spaces`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``{ "results": [ { "id": "<string>", "key": "<string>", "name": "<string>", "description": { "plain": {}, "view": {} }, "dataPolicy": { "anyContentBlocked": true }, "icon": { "path": "<string>", "apiDownloadLink": "<string>" }, "_links": { "webui": "<string>" } } ], "_links": { "next": "<string>", "base": "<string>" } }`