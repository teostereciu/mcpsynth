# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-server-info/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Server info

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource provides information about the Jira instance.

Operations

[GET/rest/api/3/serverInfo](/cloud/jira/platform/rest/v3/api-group-server-info/#api-rest-api-3-serverinfo-get)

---

GET

## Get Jira instance info

Returns information about the Jira instance.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**Â Any Scope

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

ServerInformation

Details about the Jira instance.

Show child properties

401Unauthorized

GET/rest/api/3/serverInfo

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/serverInfo`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``{ "baseUrl": "https://your-domain.atlassian.net", "buildDate": "2020-03-26T22:20:59.000+0000", "buildNumber": 582, "defaultLocale": { "locale": "en_AU" }, "displayUrl": "https://instance.jira.your-domain.com", "displayUrlConfluence": "https://instance.confluence.your-domain.com", "displayUrlServicedeskHelpCenter": "https://instance.help.your-domain.com", "scmInfo": "1f51473f5c7b75c1a69a0090f4832cdc5053702a", "serverTime": "2020-03-31T16:43:50.000+0000", "serverTimeZone": "Australia/Sydney", "serverTitle": "My Jira instance", "version": "1001.0.0-SNAPSHOT", "versionNumbers": [ 5, 0, 0 ] }`