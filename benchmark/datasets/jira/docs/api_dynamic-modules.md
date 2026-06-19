# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dynamic-modules/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Dynamic modules

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [modules registered dynamically](https://developer.atlassian.com/cloud/jira/platform/dynamic-modules/) by [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps).

Operations

[GET/rest/atlassian-connect/1/app/module/dynamic](/cloud/jira/platform/rest/v3/api-group-dynamic-modules/#api-rest-atlassian-connect-1-app-module-dynamic-get)[POST/rest/atlassian-connect/1/app/module/dynamic](/cloud/jira/platform/rest/v3/api-group-dynamic-modules/#api-rest-atlassian-connect-1-app-module-dynamic-post)[DEL/rest/atlassian-connect/1/app/module/dynamic](/cloud/jira/platform/rest/v3/api-group-dynamic-modules/#api-rest-atlassian-connect-1-app-module-dynamic-delete)

---

GET

## Get modules

Returns all modules registered dynamically by the calling app.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

ConnectModules

Show child properties

401Unauthorized

GET/rest/atlassian-connect/1/app/module/dynamic

curl

Node.js

Java

Python

PHP

`1 2 3 ``curl --request GET \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/app/module/dynamic' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "jiraEntityProperties": [ { "keyConfigurations": [ { "extractions": [ { "objectName": "extension", "type": "text", "alias": "attachmentExtension" } ], "propertyKey": "attachment" } ], "entityType": "issue", "name": { "value": "Attachment Index Document" }, "key": "dynamic-attachment-entity-property" } ], "jiraIssueFields": [ { "description": { "value": "A dynamically added single-select field" }, "type": "single_select", "extractions": [ { "path": "category", "type": "text", "name": "categoryName" } ], "name": { "value": "Dynamic single select" }, "key": "dynamic-select-field" } ] }`

---

POST

## Register modules

Registers a list of modules.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Request bodyapplication/json

**modules**

array<ConnectModule>

Required

### Responses

200OK

Returned if the request is successful.

400Bad Request

401Unauthorized

POST/rest/atlassian-connect/1/app/module/dynamic

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 ``curl --request POST \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/app/module/dynamic' \ --header 'Content-Type: application/json' \ --data '{ "jiraEntityProperties": [ { "keyConfigurations": [ { "extractions": [ { "objectName": "extension", "type": "text", "alias": "attachmentExtension" } ], "propertyKey": "attachment" } ], "entityType": "issue", "name": { "value": "Attachment Index Document" }, "key": "dynamic-attachment-entity-property" } ], "jiraIssueFields": [ { "description": { "value": "A dynamically added single-select field" }, "type": "single_select", "extractions": [ { "path": "category", "type": "text", "name": "categoryName" } ], "name": { "value": "Dynamic single select" }, "key": "dynamic-select-field" } ] }'`

---

DEL

## Remove modules

Remove all or a list of modules registered by the calling app.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Query parameters

**moduleKey**

array<string>

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

DEL/rest/atlassian-connect/1/app/module/dynamic

curl

Node.js

Java

Python

PHP

`1 2 ``curl --request DELETE \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/app/module/dynamic'`