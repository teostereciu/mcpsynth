# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-navigator-settings/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue navigator settings

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue navigator settings. Use it to get and set issue navigator default columns.

Operations

[GET/rest/api/3/settings/columns](/cloud/jira/platform/rest/v3/api-group-issue-navigator-settings/#api-rest-api-3-settings-columns-get)[PUT/rest/api/3/settings/columns](/cloud/jira/platform/rest/v3/api-group-issue-navigator-settings/#api-rest-api-3-settings-columns-put)

---

GET

## Get issue navigator default columns

Returns the default issue navigator columns.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ColumnItem>

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/settings/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/settings/columns`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 ``[ { "label": "Key", "value": "issuekey" }, { "label": "Summary", "value": "summary" } ]`

---

PUT

## Set issue navigator default columns

Sets the default issue navigator columns.

The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple `columns` parameters. For example, in curl:

`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/settings/columns`

If no column details are sent, then all default columns are removed.

A navigable field is one that can be used as a column on the issue navigator. Find details of navigable issue columns using [Get include_fields](/cloud/jira/platform/rest/v3/api-group-issue-include_fields/#api-rest-api-3-field-get).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request body*/* multipart/form-data

A navigable field value.

**columns**

array<string>

### Responses

200OK

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/settings/columns

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/settings/columns`, { method: 'PUT' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`