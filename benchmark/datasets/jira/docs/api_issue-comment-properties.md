# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-comment-properties/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue comment properties

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [issue comment](/cloud/jira/platform/rest/v3/api-group-issue-comments/#api-group-issue-comments) properties, which provides for storing custom data against an issue comment. Use is to get, set, and delete issue comment properties as well as obtain the keys of all properties on a comment. Comment properties are a type of [entity property](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Operations

[GET/rest/api/3/comment/{commentId}/properties](/cloud/jira/platform/rest/v3/api-group-issue-comment-properties/#api-rest-api-3-comment-commentid-properties-get)[GET/rest/api/3/comment/{commentId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-comment-properties/#api-rest-api-3-comment-commentid-properties-propertykey-get)[PUT/rest/api/3/comment/{commentId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-comment-properties/#api-rest-api-3-comment-commentid-properties-propertykey-put)[DEL/rest/api/3/comment/{commentId}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-comment-properties/#api-rest-api-3-comment-commentid-properties-propertykey-delete)

---

GET

## Get comment property keys

Returns the keys of all the properties of a comment.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:comment.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**commentId**

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

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/comment/{commentId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/comment/{commentId}/properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "keys": [ { "key": "issue.support", "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support" } ] }`

---

GET

## Get comment property

Returns the value of a comment property.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:comment.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**commentId**

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

403Forbidden

404Not Found

GET/rest/api/3/comment/{commentId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/comment/{commentId}/properties/{propertyKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "key": "issue.support", "value": { "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6", "system.support.time": "1m" } }`

---

PUT

## Set comment property

Creates or updates the value of a property for a comment. Use this resource to store custom data against a comment.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** either of:

  * _Edit All Comments_ [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on any comment.
  * _Edit Own Comments_ [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on a comment created by the user.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:comment.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**commentId**

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

Returned if the comment property is updated.

#### application/json

any

201Created

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/comment/{commentId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{}`; const response = await requestJira(`/rest/api/3/comment/{commentId}/properties/{propertyKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete comment property

Deletes a comment property.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** either of:

  * _Edit All Comments_ [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from any comment.
  * _Edit Own Comments_ [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from a comment created by the user.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:comment.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

Expand all

**commentId**

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

DEL/rest/api/3/comment/{commentId}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/comment/{commentId}/properties/{propertyKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`