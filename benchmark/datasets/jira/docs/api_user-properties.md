# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-user-properties/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# User properties

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [user](/cloud/jira/platform/rest/v3/api-group-users/#api-group-users) properties and provides for storing custom data against a user. Use it to get, create, and delete user properties as well as get a list of property keys for a user. This resourse is designed for integrations and apps to store per-user data and settings. This enables data used to customized the user experience to be kept in the Jira Cloud instance's database. User properties are a type of [entity property](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

This resource does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

Operations

[GET/rest/api/3/user/properties](/cloud/jira/platform/rest/v3/api-group-user-properties/#api-rest-api-3-user-properties-get)[GET/rest/api/3/user/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-user-properties/#api-rest-api-3-user-properties-propertykey-get)[PUT/rest/api/3/user/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-user-properties/#api-rest-api-3-user-properties-propertykey-put)[DEL/rest/api/3/user/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-user-properties/#api-rest-api-3-user-properties-propertykey-delete)

---

GET

## Get user property keys

Returns the keys of all properties for a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the property keys on any user.
  * Access to Jira, to access the calling user's property keys.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**accountId**

string

**userKey**

string

**username**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PropertyKeys

List of property keys.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/user/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/properties?accountId=5b10ac8d82e05b22cc7d4ef5`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "keys": [ { "key": "issue.support", "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support" } ] }`

---

GET

## Get user property

Returns the value of a user's property. If no property key is provided [Get user property keys](/cloud/jira/platform/rest/v3/api-group-user-properties/#api-rest-api-3-user-properties-get) is called.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a property from any user.
  * Access to Jira, to get a property from the calling user's record.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**propertyKey**

string

Required

#### Query parameters

Expand all

**accountId**

string

**userKey**

string

**username**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

EntityProperty

An entity property, for more information see [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/user/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/properties/{propertyKey}?accountId=5b10ac8d82e05b22cc7d4ef5`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "key": "issue.support", "value": { "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6", "system.support.time": "1m" } }`

---

PUT

## Set user property

Sets the value of a user's property. Use this resource to store custom data against a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a property on any user.
  * Access to Jira, to set a property on the calling user's record.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:user.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**propertyKey**

string

Required

#### Query parameters

Expand all

**accountId**

string

**userKey**

string

**username**

string

#### Request bodyapplication/json

The value of the property. The value has to be a valid, non-empty [JSON](https://tools.ietf.org/html/rfc4627) value. The maximum length of the property value is 32768 bytes.

any

### Responses

200OK

Returned if the user property is updated.

#### application/json

any

201Created

400Bad Request

401Unauthorized

403Forbidden

404Not Found

405Method Not Allowed

PUT/rest/api/3/user/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{}`; const response = await requestJira(`/rest/api/3/user/properties/{propertyKey}?accountId=5b10ac8d82e05b22cc7d4ef5`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete user property

Deletes a property from a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg), to delete a property from any user.
  * Access to Jira, to delete a property from the calling user's record.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:user.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**propertyKey**

string

Required

#### Query parameters

Expand all

**accountId**

string

**userKey**

string

**username**

string

### Responses

204No Content

Returned if the user property is deleted.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/user/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/user/properties/{propertyKey}?accountId=5b10ac8d82e05b22cc7d4ef5`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`