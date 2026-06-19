# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-properties/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# App properties

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents app properties. Use it to store arbitrary data for your [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps).

Operations

[GET/rest/atlassian-connect/1/addons/{addonKey}/properties](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-atlassian-connect-1-addons-addonkey-properties-get)[GET/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-atlassian-connect-1-addons-addonkey-properties-propertykey-get)[PUT/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-atlassian-connect-1-addons-addonkey-properties-propertykey-put)[DEL/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-atlassian-connect-1-addons-addonkey-properties-propertykey-delete)[GET/rest/forge/1/app/properties](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-forge-1-app-properties-get)[GET/rest/forge/1/app/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-forge-1-app-properties-propertykey-get)[PUT/rest/forge/1/app/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-forge-1-app-properties-propertykey-put)[DEL/rest/forge/1/app/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-app-properties/#api-rest-forge-1-app-properties-propertykey-delete)

---

GET

## Get app properties

Gets all the properties of an app. The reserved key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8` is not returned.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**Â Any Scope

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

**addonKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PropertyKeys

List of property keys.

Show child properties

401Unauthorized

GET/rest/atlassian-connect/1/addons/{addonKey}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/atlassian-connect/1/addons/{addonKey}/properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "keys": [ { "self": "https://your-domain.atlassian.net/jira/rest/atlassian-connect/1/addon/example.app.key/properties/propertyKey", "key": "propertyKey" } ] }`

---

GET

## Get app property

Returns the key and value of an app's property. The property key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8` is reserved. It returns a synthetic, read-only property containing the Connect `clientKey` for the requested tenant. This is intended for Forge apps with `app.connect.key` to retrieve the Connect client key during migration.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**Â Any Scope

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

Expand all

**addonKey**

string

Required

**propertyKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

EntityProperty

An entity property, for more information see [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "self": "https://your-domain.atlassian.net/jira/rest/atlassian-connect/1/addon/example.app.key/properties/propertyKey", "key": "propertyKey", "value": "propertyValue" }`

---

PUT

## Set app property

Sets the value of an app's property. Use this resource to store custom data for your app.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**Â Any Scope

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

Expand all

**addonKey**

string

Required

**propertyKey**

string

Required

#### Request bodyapplication/json

any

### Responses

200OK

Returned if the property is updated.

#### application/json

OperationMessage

Show child properties

201Created

400Bad Request

401Unauthorized

403Forbidden

PUT/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{}`; const response = await requestJira(`/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "message": "Property updated.", "statusCode": 200 }`

---

DEL

## Delete app property

Deletes an app's property.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**Â Any Scope

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

Expand all

**addonKey**

string

Required

**propertyKey**

string

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get app property keys (Forge)Experimental

Returns all property keys for the Forge app.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:app-data:jira`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

object

Show child properties

401Unauthorized

403Forbidden

GET/rest/forge/1/app/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/forge/1/app/properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "keys": [ { "key": "key1", "self": "https://your-domain.atlassian.net/rest/forge/1/app/properties/key1" }, { "key": "key2", "self": "https://your-domain.atlassian.net/rest/forge/1/app/properties/key2" } ] }`

---

GET

## Get app property (Forge)Experimental

Returns the value of a Forge app's property.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:app-data:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**propertyKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

object

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/forge/1/app/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/forge/1/app/properties/{propertyKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "key": "property-key", "value": "property-value" }`

---

PUT

## Set app property (Forge)Experimental

Sets the value of a Forge app's property. These values can be retrieved in [Jira expressions](/cloud/jira/platform/jira-expressions/) through the `app` [context variable](/cloud/jira/platform/jira-expressions/#context-variables). They are also available in [entity property display conditions](/platform/forge/manifest-reference/display-conditions/entity-property-conditions/).

For other use cases, use the [Storage API](/platform/forge/runtime-reference/storage-api/).

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:app-data:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**propertyKey**

string

Required

#### Request bodyapplication/json

any

### Responses

200OK

Returned if the property is updated.

#### application/json

OperationMessage

Show child properties

201Created

400Bad Request

401Unauthorized

403Forbidden

PUT/rest/forge/1/app/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{}`; const response = await requestJira(`/rest/forge/1/app/properties/{propertyKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "message": "Property updated.", "statusCode": 200 }`

---

DEL

## Delete app property (Forge)Experimental

Deletes a Forge app's property.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`write:app-data:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**propertyKey**

string

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/forge/1/app/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/forge/1/app/properties/{propertyKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`