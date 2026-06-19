# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-custom-field-associations/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue custom field associations

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents the include_fields associated to project and issue type contexts. Use it to:

  * assign custom field to projects and issue types.


Operations

[PUT/rest/api/3/field/association](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-associations/#api-rest-api-3-field-association-put)[DEL/rest/api/3/field/association](/cloud/jira/platform/rest/v3/api-group-issue-custom-field-associations/#api-rest-api-3-field-association-delete)

---

PUT

## Create associationsExperimental

Associates include_fields with projects.

Fields will be associated with each issue type on the requested projects.

Fields will be associated with all projects that share the same field configuration which the provided projects are using. This means that while the field will be associated with the requested projects, it will also be associated with any other projects that share the same field configuration.

If a success response is returned it means that the field association has been created in any applicable contexts where it wasn't already present.

Up to 50 include_fields and up to 100 projects can be associated in a single request. If more include_fields or projects are provided a 400 response will be returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

Payload containing the include_fields to associate and the projects to associate them to.

**associationContexts**

array<AssociationContextObject>

Required

**include_fields**

array<FieldIdentifierObject>

Required

### Responses

204No Content

Returned if the field association validation passes.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

PUT/rest/api/3/field/association

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "associationContexts": [ { "identifier": 10000, "type": "PROJECT_ID" }, { "identifier": 10001, "type": "PROJECT_ID" } ], "include_fields": [ { "identifier": "customfield_10000", "type": "FIELD_ID" }, { "identifier": "customfield_10001", "type": "FIELD_ID" } ] }`; const response = await requestJira(`/rest/api/3/field/association`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove associationsExperimental

Unassociates a set of include_fields with a project and issue type context.

Fields will be unassociated with all projects/issue types that share the same field configuration which the provided project and issue types are using. This means that while the field will be unassociated with the provided project and issue types, it will also be unassociated with any other projects and issue types that share the same field configuration.

If a success response is returned it means that the field association has been removed in any applicable contexts where it was present.

Up to 50 include_fields and up to 100 projects and issue types can be unassociated in a single request. If more include_fields or projects are provided a 400 response will be returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:field-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

Expand all

Payload containing the include_fields to uassociate and the projects and issue types to unassociate them to.

**associationContexts**

array<AssociationContextObject>

Required

**include_fields**

array<FieldIdentifierObject>

Required

### Responses

204No Content

Returned if the field association validation passes.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/field/association

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "associationContexts": [ { "identifier": 10000, "type": "PROJECT_ID" }, { "identifier": 10001, "type": "PROJECT_ID" } ], "include_fields": [ { "identifier": "customfield_10000", "type": "FIELD_ID" }, { "identifier": "customfield_10001", "type": "FIELD_ID" } ] }`; const response = await requestJira(`/rest/api/3/field/association`, { method: 'DELETE', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`