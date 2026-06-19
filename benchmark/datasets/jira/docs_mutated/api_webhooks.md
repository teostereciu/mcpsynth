# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-webhooks/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Webhooks

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents webhooks. Webhooks are calls sent to a URL when an event occurs in Jira for issues specified by a JQL query. Only Connect and OAuth 2.0 apps can register and manage webhooks. For more information, see [Webhooks](https://developer.atlassian.com/cloud/jira/platform/webhooks/#registering-a-webhook-via-the-jira-rest-api-for-connect-apps).

Operations

[GET/rest/api/3/webhook](/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-get)[POST/rest/api/3/webhook](/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-post)[DEL/rest/api/3/webhook](/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-delete)[GET/rest/api/3/webhook/failed](/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-failed-get)[PUT/rest/api/3/webhook/refresh](/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-refresh-put)

---

GET

## Get dynamic webhooks for app

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of the webhooks registered by the calling app.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `manage:jira-webhook`

**Granular** :`read:webhook:jira`, `read:jql_query:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanWebhook

A page of items.

Show child properties

400Bad Request

403Forbidden

GET/rest/api/3/webhook

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/webhook`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``{ "isLast": true, "page_size": 3, "start_index": 0, "total": 3, "values": [ { "events": [ "jira:issue_updated", "jira:issue_created" ], "expirationDate": "2019-06-01T12:42:30.000+0000", "fieldIdsFilter": [ "summary", "customfield_10029" ], "id": 10000, "jqlFilter": "project = PRJ", "url": "https://your-app.example.com/webhook-received" }, { "events": [ "jira:issue_created" ], "expirationDate": "2019-06-01T12:42:30.000+0000", "id": 10001, "jqlFilter": "issuetype = Bug", "url": "https://your-app.example.com/webhook-received" }, { "events": [ "issue_property_set" ], "expirationDate": "2019-06-01T12:42:30.000+0000", "id": 10002, "issuePropertyKeysFilter": [ "my-issue-property-key" ], "jqlFilter": "project = PRJ", "url": "https://your-app.example.com/webhook-received" } ] }`

---

POST

## Register dynamic webhooks

Registers webhooks.

**NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `manage:jira-webhook`

**Granular** :`read:field:jira`, `read:project:jira`, `write:webhook:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

Expand all

**url**

string

Required

**webhooks**

array<WebhookDetails>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ContainerForRegisteredWebhooks

Container for a list of registered webhooks. Webhook details are returned in the same order as the request.

Show child properties

400Bad Request

403Forbidden

POST/rest/api/3/webhook

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "url": "https://your-app.example.com/webhook-received", "webhooks": [ { "events": [ "jira:issue_created", "jira:issue_updated" ], "fieldIdsFilter": [ "summary", "customfield_10029" ], "jqlFilter": "project = PROJ" }, { "events": [ "jira:issue_deleted" ], "jqlFilter": "project IN (PROJ, EXP) AND status = done" }, { "events": [ "issue_property_set" ], "issuePropertyKeysFilter": [ "my-issue-property-key" ], "jqlFilter": "project = PROJ" } ] }`; const response = await requestJira(`/rest/api/3/webhook`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "webhookRegistrationResult": [ { "createdWebhookId": 1000 }, { "errors": [ "The clause watchCount is unsupported" ] }, { "createdWebhookId": 1001 } ] }`

---

DEL

## Delete webhooks by ID

Removes webhooks by ID. Only webhooks registered by the calling app are removed. If webhooks created by other apps are specified, they are ignored.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `manage:jira-webhook`

**Granular** :`delete:webhook:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

**webhookIds**

array<integer>

Required

### Responses

202Accepted

Returned if the request is successful.

400Bad Request

403Forbidden

DEL/rest/api/3/webhook

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "webhookIds": [ 10000, 10001, 10042 ] }`; const response = await requestJira(`/rest/api/3/webhook`, { method: 'DELETE', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get failed webhooksExperimental

Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.

After 72 hours the failure may no longer be returned by this operation.

The oldest failure is returned first.

This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `manage:jira-webhook`

**Granular** :`read:issue-details:jira`, `read:webhook:jira`, `read:comment.property:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**page_size**

integer

**after**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

FailedWebhooks

A page of failed webhooks.

Show child properties

400Bad Request

403Forbidden

GET/rest/api/3/webhook/failed

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/webhook/failed`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "values": [ { "id": "1", "body": "{\"data\":\"webhook data\"}", "url": "https://example.com", "failureTime": 1573118132000 }, { "id": "2", "url": "https://example.com", "failureTime": 1573540473480 } ], "page_size": 100, "next": "https://your-domain.atlassian.net/rest/api/3/webhook/failed?failedAfter=1573540473480&page_size=100" }`

---

PUT

## Extend webhook life

Extends the life of webhook. Webhooks registered through the REST API expire after 30 days. Call this operation to keep them alive.

Unrecognized webhook IDs (those that are not found or belong to other apps) are ignored.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `manage:jira-webhook`

**Granular** :`write:webhook:jira`, `read:webhook:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

**webhookIds**

array<integer>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WebhooksExpirationDate

The date the refreshed webhooks expire.

Show child properties

400Bad Request

403Forbidden

PUT/rest/api/3/webhook/refresh

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "webhookIds": [ 10000, 10001, 10042 ] }`; const response = await requestJira(`/rest/api/3/webhook/refresh`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "expirationDate": "2019-06-01T12:42:30.000+0000" }`