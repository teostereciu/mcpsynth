# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-remote-links/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue remote links

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents remote issue links, a way of linking Jira to information in other systems. Use it to get, create, update, and delete remote issue links either by ID or global ID. The global ID provides a way of accessing remote issue links using information about the item's remote system host and remote system identifier.

Operations

[GET/rest/api/3/issue/{issueIdOrKey}/remotelink](/cloud/jira/platform/rest/v3/api-group-issue-remote-links/#api-rest-api-3-issue-issueidorkey-remotelink-get)[POST/rest/api/3/issue/{issueIdOrKey}/remotelink](/cloud/jira/platform/rest/v3/api-group-issue-remote-links/#api-rest-api-3-issue-issueidorkey-remotelink-post)[DEL/rest/api/3/issue/{issueIdOrKey}/remotelink](/cloud/jira/platform/rest/v3/api-group-issue-remote-links/#api-rest-api-3-issue-issueidorkey-remotelink-delete)[GET/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}](/cloud/jira/platform/rest/v3/api-group-issue-remote-links/#api-rest-api-3-issue-issueidorkey-remotelink-linkid-get)[PUT/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}](/cloud/jira/platform/rest/v3/api-group-issue-remote-links/#api-rest-api-3-issue-issueidorkey-remotelink-linkid-put)[DEL/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}](/cloud/jira/platform/rest/v3/api-group-issue-remote-links/#api-rest-api-3-issue-issueidorkey-remotelink-linkid-delete)

---

GET

## Get remote issue links

Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue.remote-link:jira`, `read:status:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Query parameters

**globalId**

string

### Responses

200OK

Returned if the request is successful. A single RemoteIssueLink will be returned when specifying `globalId`, otherwise an array of RemoteIssueLink is returned.

#### application/json

oneOf [array<RemoteIssueLink>, RemoteIssueLink]

RemoteIssueLink

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

413Request Entity Too Large

GET/rest/api/3/issue/{issueIdOrKey}/remotelink

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/remotelink`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 ``[ { "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" }, "globalId": "system=http://www.mycompany.com/support&id=1", "id": 10000, "object": { "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" }, "status": { "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" }, "resolved": true }, "summary": "Customer support issue", "title": "TSTSUP-111", "url": "http://www.mycompany.com/support?id=1" }, "relationship": "causes", "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000" }, { "application": { "name": "My Acme Tester", "type": "com.acme.tester" }, "globalId": "system=http://www.anothercompany.com/tester&id=1234", "id": 10001, "object": { "icon": { "title": "Test Case", "url16x16": "http://www.anothercompany.com/tester/images/testcase.gif" }, "status": { "icon": { "link": "http://www.anothercompany.com/tester/person?accountId=5b10a2844c20165700ede21g", "title": "Tested by Mia Krystof", "url16x16": "http://www.anothercompany.com/tester/images/person/mia.gif" }, "resolved": false }, "summary": "Test that the submit button saves the item", "title": "Test Case #1234", "url": "http://www.anothercompany.com/tester/testcase/1234" }, "relationship": "is tested by", "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10001" } ]`

---

POST

## Create or update remote issue link

Creates or updates a remote issue link for an issue.

If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any fields without values in the request are set to null. Otherwise, the remote issue link is created.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Link issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `write:issue.remote-link:jira`, `read:issue.remote-link:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Request bodyapplication/json

Expand all

**application**

Application

**globalId**

string

**object**

RemoteObject

Required

**relationship**

string

**Additional Properties**

any

### Responses

200OK

Returned if the remote issue link is updated.

#### application/json

RemoteIssueLinkIdentifies

Details of the identifiers for a created or updated remote issue link.

Show child properties

201Created

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/issue/{issueIdOrKey}/remotelink

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" }, "globalId": "system=http://www.mycompany.com/support&id=1", "object": { "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" }, "status": { "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" }, "resolved": true }, "summary": "Customer support issue", "title": "TSTSUP-111", "url": "http://www.mycompany.com/support?id=1" }, "relationship": "causes" }`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/remotelink`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "id": 10000, "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000" }`

---

DEL

## Delete remote issue link by global ID

Deletes the remote issue link from the issue using the link's global ID. Where the global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Link issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is implemented, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue.remote-link:jira`, `write:issue:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Query parameters

**globalId**

string

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/issue/{issueIdOrKey}/remotelink

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/remotelink?globalId=system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get remote issue link by ID

Returns a remote issue link for an issue.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue.remote-link:jira`, `read:status:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**linkId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

RemoteIssueLink

Details of an issue remote link.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``{ "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" }, "globalId": "system=http://www.mycompany.com/support&id=1", "id": 10000, "object": { "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" }, "status": { "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" }, "resolved": true }, "summary": "Customer support issue", "title": "TSTSUP-111", "url": "http://www.mycompany.com/support?id=1" }, "relationship": "causes", "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000" }`

---

PUT

## Update remote issue link by ID

Updates a remote issue link for an issue.

Note: Fields without values in the request are set to null.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ and _Link issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:issue:jira`, `write:issue.remote-link:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**linkId**

string

Required

#### Request bodyapplication/json

Expand all

**application**

Application

**globalId**

string

**object**

RemoteObject

Required

**relationship**

string

**Additional Properties**

any

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "application": { "name": "My Acme Tracker", "type": "com.acme.tracker" }, "globalId": "system=http://www.mycompany.com/support&id=1", "object": { "icon": { "title": "Support Ticket", "url16x16": "http://www.mycompany.com/support/ticket.png" }, "status": { "icon": { "link": "http://www.mycompany.com/support?id=1&details=closed", "title": "Case Closed", "url16x16": "http://www.mycompany.com/support/resolved.png" }, "resolved": true }, "summary": "Customer support issue", "title": "TSTSUP-111", "url": "http://www.mycompany.com/support?id=1" }, "relationship": "causes" }`; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete remote issue link by ID

Deletes a remote issue link from an issue.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ , _Edit issues_ , and _Link issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue.remote-link:jira`, `write:issue:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

Expand all

**issueIdOrKey**

string

Required

**linkId**

string

Required

### Responses

204No Content

Returned if the request is successful.

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`