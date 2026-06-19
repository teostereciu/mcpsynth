# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-properties/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue properties

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents [issue](/cloud/jira/platform/rest/v3/api-group-issues/#api-group-issues) properties, which provides for storing custom data against an issue. Use it to get, set, and delete issue properties as well as obtain details of all properties on an issue. Operations to bulk update and delete issue properties are also provided. Issue properties are a type of [entity property](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Operations

[POST/rest/api/3/issue/properties](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-properties-post)[POST/rest/api/3/issue/properties/multi](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-properties-multi-post)[PUT/rest/api/3/issue/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-properties-propertykey-put)[DEL/rest/api/3/issue/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-properties-propertykey-delete)[GET/rest/api/3/issue/{issueIdOrKey}/properties](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-issueidorkey-properties-get)[GET/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-issueidorkey-properties-propertykey-get)[PUT/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-issueidorkey-properties-propertykey-put)[DEL/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}](/cloud/jira/platform/rest/v3/api-group-issue-properties/#api-rest-api-3-issue-issueidorkey-properties-propertykey-delete)

---

POST

## Bulk set issues properties by list

Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. The maximum length of single issue property value is 32768 characters. This operation can be accessed anonymously.

This operation is:

  * transactional, either all properties are updated in all eligible issues or, when errors occur, no properties are updated.
  * [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Edit issues_ [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

Issue properties to be set or updated with values.

**entitiesIds**

array<integer>

**properties**

object

### Responses

303See Other

Returned if the operation is successful.

400Bad Request

401Unauthorized

POST/rest/api/3/issue/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "entitiesIds": [ 2154 ], "properties": {} }`; const response = await requestJira(`/rest/api/3/issue/properties`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Bulk set issue properties by issue

Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.

This operation is:

  * [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.
  * non-transactional. Updating some entities may fail. Such information will available in the task result.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Edit issues_ [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Details of the issue properties to be set or updated. Note that if an issue is not found, it is ignored.

**issues**

array<IssueEntityPropertiesForMultiUpdate>

### Responses

303See Other

Returned if the operation is successful.

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/issue/properties/multi

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issues": [ { "issueID": 1000, "properties": { "myProperty": { "owner": "admin", "weight": 100 } } }, { "issueID": 1001, "properties": { "myOtherProperty": { "cost": 150, "transportation": "car" } } } ] }`; const response = await requestJira(`/rest/api/3/issue/properties/multi`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

PUT

## Bulk set issue property

Sets a property value on multiple issues.

The value set can be a constant or determined by a [Jira expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must be computable with constant complexity when applied to a set of issues. Expressions must also comply with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions) that apply to all Jira expressions.

The issues to be updated can be specified by a filter.

The filter identifies issues eligible for update using these criteria:

  * `entityIds` Only issues from this list are eligible.

  * `currentValue` Only issues with the property set to this value are eligible.

  * `hasProperty`:

    * If _true_ , only issues with the property are eligible.
    * If _false_ , only issues without the property are eligible.


If more than one criteria is specified, they are joined with the logical _AND_ : only issues that satisfy all criteria are eligible.

If an invalid combination of criteria is provided, an error is returned. For example, specifying a `currentValue` and `hasProperty` as _false_ would not match any issues (because without the property the property cannot have a value).

The filter is optional. Without the filter all the issues visible to the user and where the user has the EDIT_ISSUES permission for the issue are considered eligible.

This operation is:

  * transactional, either all eligible issues are updated or, when errors occur, none are updated.
  * [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * _Edit issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:jira-expressions:jira`, `write:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**propertyKey**

string

Required

#### Request bodyapplication/json

Expand all

**expression**

string

**filter**

IssueFilterForBulkPropertySet

**value**

any

### Responses

303See Other

Returned if the request is successful.

400Bad Request

401Unauthorized

PUT/rest/api/3/issue/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "filter": { "currentValue": { "owner": "admin", "weight": 50 }, "entityIds": [ 10100, 100010 ], "hasProperty": true }, "value": { "owner": "admin", "weight": 100 } }`; const response = await requestJira(`/rest/api/3/issue/properties/{propertyKey}`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Bulk delete issue property

Deletes a property value from multiple issues. The issues to be updated can be specified by filter criteria.

The criteria the filter used to identify eligible issues are:

  * `entityIds` Only issues from this list are eligible.
  * `currentValue` Only issues with the property set to this value are eligible.


If both criteria is specified, they are joined with the logical _AND_ : only issues that satisfy both criteria are considered eligible.

If no filter criteria are specified, all the issues visible to the user and where the user has the EDIT_ISSUES permission for the issue are considered eligible.

This operation is:

  * transactional, either the property is deleted from all eligible issues or, when errors occur, no properties are deleted.
  * [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [ project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * _Edit issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**propertyKey**

string

Required

#### Request bodyapplication/json

Expand all

**currentValue**

any

**entityIds**

array<integer>

### Responses

303See Other

Returned if the request is successful.

400Bad Request

401Unauthorized

DEL/rest/api/3/issue/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "currentValue": "deprecated value", "entityIds": [ 10100, 100010 ] }`; const response = await requestJira(`/rest/api/3/issue/properties/{propertyKey}`, { method: 'DELETE', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get issue property keys

Returns the URLs and keys of an issue's properties.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Property details are only returned where the user has:

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

PropertyKeys

List of property keys.

Show child properties

404Not Found

GET/rest/api/3/issue/{issueIdOrKey}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "keys": [ { "key": "issue.support", "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support" } ] }`

---

GET

## Get issue property

Returns the key and value of an issue's property.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

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

401Unauthorized

404Not Found

GET/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "key": "issue.support", "value": { "system.conversation.id": "b1bf38be-5e94-4b40-a3b8-9278735ee1e6", "system.support.time": "1m" } }`

---

PUT

## Set issue property

Sets the value of an issue's property. Use this resource to store custom data against an issue.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Edit issues_ [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

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

Returned if the issue property is updated.

#### application/json

any

201Created

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{}`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete issue property

Deletes an issue's property.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Edit issues_ [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**propertyKey**

string

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

404Not Found

DEL/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`