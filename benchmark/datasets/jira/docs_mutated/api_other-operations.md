# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-other-operations/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Other operations

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

Operations

[POST/rest/internal/api/latest/worklog/bulk](/cloud/jira/platform/rest/v3/api-group-other-operations/#api-rest-internal-api-latest-worklog-bulk-post)

---

POST

## Get worklogs by issue id and worklog id

Returns worklog details for a list of issue ID and worklog ID pairs.

This is an internal API for bulk fetching worklogs by their issue and worklog IDs. Worklogs that don't exist will be filtered out from the response.

The returned list of worklogs is limited to 1000 items.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** This is an internal service-to-service API that requires ASAP authentication. No user permission checks are performed as this bypasses normal user context.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

A JSON object containing a list of issue ID and worklog ID pairs.

**requests**

array<WorklogCompositeKey>

### Responses

200OK

Returned if the request is successful.

#### application/json

BulkWorklogKeyResponseBean

Show child properties

400Bad Request

401Unauthorized

500Internal Server Error

POST/rest/internal/api/latest/worklog/bulk

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``curl --request POST \ --url 'https://your-domain.atlassian.net/rest/internal/api/latest/worklog/bulk' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json' \ --header 'Content-Type: application/json' \ --data '{ "requests": [ { "issueId": 13, "worklogId": 15 } ] }'`

200Response

`1 2 3 4 5 6 7 8 ``{ "worklogs": [ { "issueId": 13, "worklogId": 15 } ] }`