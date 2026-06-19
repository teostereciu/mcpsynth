# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Field schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents field schemes which are replacing field configuration schemes to control field associations. They are currently in beta and only available to customers who have opted-in to the beta program. For more information see [RFC-103: Jira Field Configuration Overhaul: Admin Experience and API Changes](https://community.developer.atlassian.com/t/rfc-103-jira-field-configuration-overhaul-admin-experience-and-api-changes/94205)

Operations

[GET/rest/api/3/config/fieldschemes](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-get)[POST/rest/api/3/config/fieldschemes](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-post)[PUT/rest/api/3/config/fieldschemes/include_fields](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-include_fields-put)[DEL/rest/api/3/config/fieldschemes/include_fields](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-include_fields-delete)[PUT/rest/api/3/config/fieldschemes/include_fields/parameters](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-include_fields-parameters-put)[DEL/rest/api/3/config/fieldschemes/include_fields/parameters](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-include_fields-parameters-delete)[GET/rest/api/3/config/fieldschemes/projects](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-projects-get)[PUT/rest/api/3/config/fieldschemes/projects](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-projects-put)[GET/rest/api/3/config/fieldschemes/{id}](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-get)[PUT/rest/api/3/config/fieldschemes/{id}](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-put)[DEL/rest/api/3/config/fieldschemes/{id}](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-delete)[POST/rest/api/3/config/fieldschemes/{id}/clone](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-clone-post)[GET/rest/api/3/config/fieldschemes/{id}/include_fields](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-include_fields-get)[GET/rest/api/3/config/fieldschemes/{id}/include_fields/{fieldId}/parameters](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-include_fields-fieldid-parameters-get)[GET/rest/api/3/config/fieldschemes/{id}/projects](/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-rest-api-3-config-fieldschemes-id-projects-get)

---

GET

## Get field schemesExperimental

REST endpoint for retrieving a paginated list of field association schemes with optional filtering.

This endpoint allows clients to fetch field association schemes with optional filtering by project IDs and text queries. The response includes scheme details with navigation links and filter metadata when applicable.

Filtering Behavior:

  * When projectId or query parameters are provided, the response includes matchedFilters metadata showing which filters were applied.
  * When no filters are applied, matchedFilters is omitted from individual scheme objects


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**projectId**

array<integer>

**query**

string

**start_index**

integer

**page_size**

integer

### Responses

200OK

Pagianted list of field association schemes

#### application/json

PageBean2GetFieldAssociationSchemeResponse

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/config/fieldschemes

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "description": "Field Association Scheme test description", "id": 1000, "isDefault": false, "links": { "associations": "rest/api/3/config/fieldschemes/10000/include_fields", "projects": "rest/api/3/config/fieldschemes/10000/projects" }, "matchedFilters": { "projectIds": [ 10001, 10002 ], "query": "query" }, "name": "Field Association Scheme test name" }`

---

POST

## Create field schemeExperimental

Endpoint for creating a new field association scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

The request containing the name and description of the field association scheme

**description**

string

**name**

string

Required

### Responses

200OK

Returned if the creation was successful.

#### application/json

CreateFieldAssociationSchemeResponse

Response object after successfully creating a new field association scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/config/fieldschemes

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Field association scheme description", "name": "Field association scheme name" }`; const response = await requestJira(`/rest/api/3/config/fieldschemes`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 ``{ "description": "Field association scheme description", "id": 10000, "links": { "associations": "{BASE_API_URL}/rest/api/2/config/fieldschemes/9/include_fields", "projects": "{BASE_API_URL}/rest/api/2/config/fieldschemes/9/projects" }, "name": "Field association scheme name" }`

---

PUT

## Update include_fields associated with field schemesExperimental

Update include_fields associated with field association schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The request containing the schemes and work types to associate each field with.

**Additional Properties**

array<UpdateFieldAssociationsRequestItem>

### Responses

200OK

Returned if the field association update was successful.

#### application/json

FieldSchemeToFieldsResponse

Response for updating field associations.

Show child properties

204No Content

207Multi-Status

400Bad Request

401Unauthorized

403Forbidden

PUT/rest/api/3/config/fieldschemes/include_fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "customfield_10000": [ { "restrictedToWorkTypes": [ 1, 2 ], "schemeIds": [ 10000, 10001 ] } ], "customfield_10001": [ { "schemeIds": [ 10002 ] } ] }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/include_fields`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``{ "results": [ { "fieldId": "customfield_10000", "schemeId": 10000, "success": true, "workTypeIds": [ 1, 2 ] }, { "fieldId": "customfield_10001", "schemeId": 10002, "success": true, "workTypeIds": [] } ] }`

---

DEL

## Remove include_fields associated with field schemesExperimental

Remove include_fields associated with field association schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The request containing the schemes and include_fields to be removed.

**Additional Properties**

RemoveFieldAssociationsRequestItem

### Responses

200OK

Returned if the field association update was successful.

#### application/json

MinimalFieldSchemeToFieldsResponse

Minimal response for updating field scheme to include_fields associations.

Show child properties

204No Content

207Multi-Status

400Bad Request

401Unauthorized

403Forbidden

DEL/rest/api/3/config/fieldschemes/include_fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "customfield_10000": { "schemeIds": [ 10000, 10001 ] }, "customfield_10001": { "schemeIds": [ 10002 ] } }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/include_fields`, { method: 'DELETE', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "results": [ { "fieldId": "customfield_10000", "schemeId": 10000, "success": true }, { "fieldId": "customfield_10001", "schemeId": 10002, "success": true } ] }`

---

PUT

## Update field parametersExperimental

Update field association item parameters in field association schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

The request containing the field association scheme id and the parameters to update.

**Additional Properties**

array<UpdateFieldSchemeParametersRequest>

### Responses

200OK

Returned if the field parameter update was successful.

#### application/json

UpdateFieldSchemeParametersResponse

Response bean for field scheme parameter update operations.

Show child properties

204No Content

207Multi-Status

400Bad Request

401Unauthorized

403Forbidden

PUT/rest/api/3/config/fieldschemes/include_fields/parameters

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "customfield_10000": [ { "parameters": { "description": "Field description", "isRequired": true }, "schemeIds": [ 10000, 10001 ], "workTypeParameters": [ { "description": "Description for Bug", "isRequired": false, "workTypeId": 10002 } ] } ], "customfield_10001": [ { "schemeIds": [ 10001 ], "workTypeParameters": [ { "description": "Description for Bug", "isRequired": false, "workTypeId": 10002 }, { "description": "Description for Task", "isRequired": true, "workTypeId": 10003 } ] } ] }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/include_fields/parameters`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "results": [ { "fieldId": "customfield_10000", "schemeId": 10000, "success": true }, { "fieldId": "customfield_10001", "schemeId": 10002, "success": true, "workTypeId": 10001 } ] }`

---

DEL

## Remove field parametersExperimental

Remove field association parameters overrides for work types.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

**Additional Properties**

array<ParameterRemovalDetails>

### Responses

200OK

Returned if the removal was successful.

204No Content

207Multi-Status

400Bad Request

401Unauthorized

403Forbidden

DEL/rest/api/3/config/fieldschemes/include_fields/parameters

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "customfield_10000": [ { "parameters": [ "description", "isRequired" ], "schemeId": 10000, "workTypeIds": [ 1, 2 ] } ], "description": [ { "parameters": [ "description" ], "schemeId": 10001, "workTypeIds": [ 3 ] } ] }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/include_fields/parameters`, { method: 'DELETE', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get projects with field schemesExperimental

Get projects with field association schemes. This will be a temporary API but useful when transitioning from the legacy field configuration APIs to the new ones.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**projectId**

array<integer>

Required

### Responses

200OK

Returns the list of project with field association schemes.

#### application/json

PageBean2GetProjectsWithFieldSchemesResponse

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/config/fieldschemes/projects

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes/projects?projectId={projectId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "isLast": true, "page_size": 3, "start_index": 0, "total": 3, "values": [ { "projectId": 10000, "schemeId": 1 }, { "projectId": 10001, "schemeId": 1 }, { "projectId": 10002, "schemeId": 2 } ] }`

---

PUT

## Associate projects to field schemesExperimental

Associate projects to field association schemes.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

**Additional Properties**

FieldSchemeToProjectsRequest

### Responses

200OK

Returned if the association was successful.

#### application/json

FieldSchemeToProjectsResponse

Response for updating field scheme to projects associations.

Show child properties

204No Content

207Multi-Status

400Bad Request

401Unauthorized

403Forbidden

PUT/rest/api/3/config/fieldschemes/projects

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "10000": { "projectIds": [ 10000, 10001 ] }, "10001": { "projectIds": [ 10002 ] } }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/projects`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "results": [ { "projectId": 10001, "schemeId": 10000, "success": true }, { "projectId": 10002, "schemeId": 10001, "success": true } ] }`

---

GET

## Get field schemeExperimental

Endpoint for fetching a field association scheme by its ID

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if a field association scheme matches the given scheme ID

#### application/json

GetFieldAssociationSchemeByIdResponse

Response object for getting a field association scheme by ID.

Show child properties

403Forbidden

404Not Found

GET/rest/api/3/config/fieldschemes/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "description": "This is a field association scheme", "id": "123", "isDefault": false, "links": { "associations": "rest/api/3/config/fieldschemes/10000/include_fields", "projects": "rest/api/3/config/fieldschemes/10000/projects" }, "name": "Scheme" }`

---

PUT

## Update field schemeExperimental

Endpoint for updating an existing field association scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

The request containing the desired updates to the field association scheme

**description**

string

**name**

string

### Responses

200OK

Returned if the update was successful.

#### application/json

UpdateFieldAssociationSchemeResponse

Response object after successfully updating an existing field association scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/config/fieldschemes/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Field association scheme description", "name": "Field association scheme name" }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 ``{ "description": "Field association scheme description", "id": 10000, "links": { "associations": "{BASE_API_URL}/rest/api/2/config/fieldschemes/9/include_fields", "projects": "{BASE_API_URL}/rest/api/2/config/fieldschemes/9/projects" }, "name": "Field association scheme name" }`

---

DEL

## Delete a field schemeExperimental

Delete a specified field association scheme

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the field association scheme deletion was successful.

#### application/json

DeleteFieldAssociationSchemeResponse

Response object after successfully deleting a field association scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

409Conflict

DEL/rest/api/3/config/fieldschemes/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "deleted": true, "id": "10000" }`

---

POST

## Clone field schemeExperimental

Endpoint for cloning an existing field association scheme into a new one.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration-scheme:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

The request containing the name and description for the new scheme

**description**

string

**name**

string

Required

### Responses

200OK

Returned if the clone was successful.

#### application/json

CreateFieldAssociationSchemeResponse

Response object after successfully creating a new field association scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/config/fieldschemes/{id}/clone

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "Field association scheme description", "name": "Field association scheme name" }`; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}/clone`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 ``{ "description": "Field association scheme description", "id": 10000, "links": { "associations": "{BASE_API_URL}/rest/api/2/config/fieldschemes/9/include_fields", "projects": "{BASE_API_URL}/rest/api/2/config/fieldschemes/9/projects" }, "name": "Field association scheme name" }`

---

GET

## Search field scheme fieldsExperimental

Search for include_fields belonging to a given field association scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**fieldId**

array<string>

### Responses

200OK

Returns the matching include_fields, at the specified page of the results.

#### application/json

PageBean2FieldAssociationSchemeFieldSearchResult

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/config/fieldschemes/{id}/include_fields

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}/include_fields`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``{ "allowedOperations": [ "REMOVE", "CHANGE_REQUIRED", "CHANGE_DESCRIPTION" ], "fieldId": "customfield_10000", "parameters": { "description": "text", "isRequired": true }, "restrictedToWorkTypes": [ "1", "2" ], "workTypeParameters": [ { "description": "text", "isRequired": true, "workTypeId": "1" }, { "description": "textarea", "isRequired": false, "workTypeId": "2" } ] }`

---

GET

## Get field parametersExperimental

Retrieve field association parameters on a field association scheme

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**id**

integer

Required

**fieldId**

string

Required

### Responses

200OK

Returned if the parameters fetched were successful.

#### application/json

GetFieldAssociationParametersResponse

Response object for getting field association parameters.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

GET/rest/api/3/config/fieldschemes/{id}/include_fields/{fieldId}/parameters

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}/include_fields/{fieldId}/parameters`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "fieldId": "customfield_10000", "parameters": { "description": "Teams field", "isRequired": true }, "workTypeParameters": [ { "description": "Teams field", "isRequired": false, "workTypeId": 10010 } ] }`

---

GET

## Search field scheme projectsExperimental

REST Endpoint for searching for projects belonging to a given field association scheme

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field-configuration:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**projectId**

array<integer>

### Responses

200OK

Returns a paginated list of projects associated with the field association scheme, matching the specified filter criteria.

#### application/json

PageBean2FieldAssociationSchemeProjectSearchResult

A page of items.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/config/fieldschemes/{id}/projects

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/config/fieldschemes/{id}/projects`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "isLast": true, "page_size": 51, "nextPage": "<string>", "self": "<string>", "start_index": 37, "total": 29, "values": [ { "id": "<string>", "name": "<string>" } ] }`