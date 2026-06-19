# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-properties/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue type properties

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [issue type](/cloud/jira/platform/rest/v3/api-group-issue-types/#api-group-issue-types) properties, which provides for storing custom data against an issue type. Use it to get, create, and delete issue type properties as well as obtain the keys of all properties on a issues type. Issue type properties are a type of [entity property](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Operations

[GET/rest/api/3/issuetype/{issueTypeId}/properties](/cloud/jira/platform/rest/v3/api-group-issue-type-properties/#api-rest-api-3-issuetype-issuetypeid-properties-get)[GET/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-type-properties/#api-rest-api-3-issuetype-issuetypeid-properties-propertykey-get)[PUT/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-type-properties/#api-rest-api-3-issuetype-issuetypeid-properties-propertykey-put)[DEL/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-type-properties/#api-rest-api-3-issuetype-issuetypeid-properties-propertykey-delete)

---

GET

## Get issue type property keys

Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type.
  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**issueTypeId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PropertyKeys

List of property keys.

Show child properties

400Bad Request

404Not Found

GET/rest/api/3/issuetype/{issueTypeId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{issueTypeId}/properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "keys": [ { "key": "issue.support", "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support" } ] }`

---

GET

## Get issue type property

Returns the key and value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the details of any issue type.
  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) to get the details of any issue types associated with the projects the user has permission to browse.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**issueTypeId**

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

GET/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "key": "issue.support", "value": { "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6", "system.support.time": "1m" } }`

---

PUT

## Set issue type property

Creates or updates the value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against an issue type.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:issue-type.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**issueTypeId**

string

Required

**propertyKey**

string

Required

#### Request bodyapplication/json

The value of the property. The value has to be a valid, non-empty [JSON](https://tools.ietf.org/html/rfc4627) value. The maximum length of the property value is 32768 bytes.

any

### Responses

200OK

Returned if the issue type property is updated.

#### application/json

any

201Created

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "number": 5, "string": "string-value" }`; const response = await requestJira(`/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete issue type property

Deletes the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:issue-type.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**issueTypeId**

string

Required

**propertyKey**

string

Required

### Responses

204No Content

Returned if the issue type property is deleted.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`