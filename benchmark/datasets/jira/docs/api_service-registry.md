# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-service-registry/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Service Registry

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents a service registry. Use it to retrieve attributes related to a [service registry](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-services/) in JSM.

Operations

[GET/rest/atlassian-connect/1/service-registry](/cloud/jira/platform/rest/v3/api-group-service-registry/#api-rest-atlassian-connect-1-service-registry-get)

---

GET

## Retrieve the attributes of service registriesExperimental

Retrieve the attributes of given service registries.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect apps can make this request and the servicesIds belong to the tenant you are requesting

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

Connect apps cannot access this REST resource.

### Request

#### Query parameters

**serviceIds**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ServiceRegistry>

Show child properties

400Bad Request

401Unauthorized

403Forbidden

500Internal Server Error

501Not Implemented

504Gateway Timeout

GET/rest/atlassian-connect/1/service-registry

curl

Node.js

Java

Python

PHP

`1 2 3 ``curl --request GET \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/service-registry?serviceIds={serviceIds}' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``[ { "description": "<string>", "id": "<string>", "name": "<string>", "organizationId": "<string>", "revision": "<string>", "serviceTier": { "description": "<string>", "id": "<string>", "level": 10, "name": "<string>", "nameKey": "service-registry.tier1.name" } } ]`