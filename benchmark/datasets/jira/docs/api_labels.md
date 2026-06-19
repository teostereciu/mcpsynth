# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-labels/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Labels

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents available labels. Use it to get available labels for the global label field.

Operations

[GET/rest/api/3/label](/cloud/jira/platform/rest/v3/api-group-labels/#api-rest-api-3-label-get)

---

GET

## Get all labels

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of labels.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:label:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**startAt**

integer

**maxResults**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanString

A page of items.

Show child properties

GET/rest/api/3/label

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/label`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``{ "isLast": false, "maxResults": 2, "startAt": 0, "total": 100, "values": [ "performance", "security" ] }`