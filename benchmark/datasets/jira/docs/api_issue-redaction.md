# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-redaction/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue redaction

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents Issue Redaction. Provides APIs to redact issue data.

Operations

[POST/rest/api/3/redact](/cloud/jira/platform/rest/v3/api-group-issue-redaction/#api-rest-api-3-redact-post)[GET/rest/api/3/redact/status/{jobId}](/cloud/jira/platform/rest/v3/api-group-issue-redaction/#api-rest-api-3-redact-status-jobid-get)

---

POST

## Redact

Submit a job to redact issue field data. This will trigger the redaction of the data in the specified fields asynchronously. The redaction status can be polled using the job id.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`redact:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

List of redaction requests

**redactions**

array<SingleRedactionRequest>

### Responses

202Accepted

Returned if the job submission is successful. The response contains the job id.

#### application/json

string

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/redact

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``curl --request POST \ --url 'https://your-domain.atlassian.net/rest/api/3/redact' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json' \ --header 'Content-Type: application/json' \ --data '{ "redactions": [ { "contentItem": { "entityId": "summary", "entityType": "issuefieldvalue", "id": "10000" }, "externalId": "51101de6-d001-429d-a095-b2b96dd57fcb", "reason": "PII data", "redactionPosition": { "adfPointer": "/content/0/content/0/text", "expectedText": "ODFiNjM3ZDhmY2QyYzZkYTYzNTllNjk2MzExM2ExMTcwZGU3OTVlNGI3MjViODRkMWUwYjRjZmQ5ZWM1OGNlOQ==", "from": 14, "to": 20 } } ] }'`

202Response

`1 ``"<string>"`

---

GET

## Get redaction status

Retrieves the current status of a redaction job ID.

The jobStatus will be one of the following:

  * IN_PROGRESS - The redaction job is currently in progress
  * COMPLETED - The redaction job has completed successfully.
  * PENDING - The redaction job has not started yet


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`redact:issue:jira`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**jobId**

string

Required

### Responses

200OK

Returned if the job status is successfully retrieved.

#### application/json

RedactionJobStatusResponse

Show child properties

403Forbidden

404Not Found

GET/rest/api/3/redact/status/{jobId}

curl

Node.js

Java

Python

PHP

`1 2 3 4 ``curl --request GET \ --url 'https://your-domain.atlassian.net/rest/api/3/redact/status/{jobId}' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "bulkRedactionResponse": { "results": [ { "externalId": "<string>", "successful": true } ] }, "jobStatus": "PENDING" }`