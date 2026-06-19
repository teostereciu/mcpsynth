# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-dynamic-modules/*

---

Cloud

Confluence Cloud / Reference / REST API

# Dynamic modules

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/atlassian-connect/1/app/module/dynamic](/cloud/confluence/rest/v1/api-group-dynamic-modules/#api-wiki-rest-atlassian-connect-1-app-module-dynamic-get)[POST/wiki/rest/atlassian-connect/1/app/module/dynamic](/cloud/confluence/rest/v1/api-group-dynamic-modules/#api-wiki-rest-atlassian-connect-1-app-module-dynamic-post)[DEL/wiki/rest/atlassian-connect/1/app/module/dynamic](/cloud/confluence/rest/v1/api-group-dynamic-modules/#api-wiki-rest-atlassian-connect-1-app-module-dynamic-delete)

---

GET

## Get modulesExperimental

Returns all modules registered dynamically by the calling app.

**[Permissions](/cloud/confluence/rest/v1/intro/#permissions) required:** Only Connect apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/confluence/scopes) required**:Â `NONE`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### */*

ConnectModules

Show child properties

401Unauthorized

GET/wiki/rest/atlassian-connect/1/app/module/dynamic

curl

Node.js

Java

Python

PHP

`1 2 3 ``curl --request GET \ --url 'https://your-domain.atlassian.net/wiki/rest/atlassian-connect/1/app/module/dynamic' \ --header 'Accept: */*'`

---

POST

## Register modulesExperimental

Registers a list of modules. For the list of modules that support dynamic registration, see [Dynamic modules](https://developer.atlassian.com/cloud/confluence/dynamic-modules/).

**[Permissions](/cloud/confluence/rest/v1/intro/#permissions) required:** Only Connect apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/confluence/scopes) required**:Â `NONE`

### Request

#### Request body*/*

 **modules**

array<ConnectModule>

Required

### Responses

200OK

Returned if the request is successful.

400Bad Request

401Unauthorized

POST/wiki/rest/atlassian-connect/1/app/module/dynamic

curl

Node.js

Java

Python

PHP

`1 2 ``curl --request POST \ --url 'https://your-domain.atlassian.net/wiki/rest/atlassian-connect/1/app/module/dynamic'`

---

DEL

## Remove modulesExperimental

Remove all or a list of modules registered by the calling app.

**[Permissions](/cloud/confluence/rest/v1/intro/#permissions) required:** Only Connect apps can make this request.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/confluence/scopes) required**:Â `NONE`

### Request

#### Query parameters

**moduleKey**

array<string>

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

DEL/wiki/rest/atlassian-connect/1/app/module/dynamic

curl

Node.js

Java

Python

PHP

`1 2 ``curl --request DELETE \ --url 'https://your-domain.atlassian.net/wiki/rest/atlassian-connect/1/app/module/dynamic?moduleKey={moduleKey}'`