# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-license-metrics/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# License metrics

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents license metrics. Use it to get available metrics for Jira licences.

Operations

[GET/rest/api/3/instance/license](/cloud/jira/platform/rest/v3/api-group-license-metrics/#api-rest-api-3-instance-license-get)[GET/rest/api/3/license/approximateLicenseCount](/cloud/jira/platform/rest/v3/api-group-license-metrics/#api-rest-api-3-license-approximatelicensecount-get)[GET/rest/api/3/license/approximateLicenseCount/product/{applicationKey}](/cloud/jira/platform/rest/v3/api-group-license-metrics/#api-rest-api-3-license-approximatelicensecount-product-applicationkey-get)

---

GET

## Get licenseExperimental

Returns licensing information about the Jira instance.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:license:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

License

Details about a license for the Jira instance.

Show child properties

401Unauthorized

GET/rest/api/3/instance/license

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/instance/license`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "applications": [ { "id": "jira-core", "plan": "PAID" }, { "id": "jira-product-discovery", "plan": "FREE" }, { "id": "jira-servicedesk", "plan": "FREE" }, { "id": "jira-software", "plan": "PAID" } ] }`

---

GET

## Get approximate license countExperimental

Returns the approximate number of user accounts across all Jira licenses. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:license:jira`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

LicenseMetric

A metric that provides insight into the active licence details

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/license/approximateLicenseCount

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/license/approximateLicenseCount`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "key": "license.totalApproximateUserCount", "value": "1000" }`

---

GET

## Get approximate application license countExperimental

Returns the total approximate number of user accounts for a single Jira license. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:license:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**applicationKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

LicenseMetric

A metric that provides insight into the active licence details

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/license/approximateLicenseCount/product/{applicationKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/license/approximateLicenseCount/product/{applicationKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "key": "license.jira-software.approximateUserCount", "value": "115" }`