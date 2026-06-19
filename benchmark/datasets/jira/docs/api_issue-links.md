# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-links/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue links

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents links between issues. Use it to get, create, and delete links between issues.

To use it, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

Operations

[POST/rest/api/3/issueLink](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-rest-api-3-issuelink-post)[GET/rest/api/3/issueLink/{linkId}](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-rest-api-3-issuelink-linkid-get)[DEL/rest/api/3/issueLink/{linkId}](/cloud/jira/platform/rest/v3/api-group-issue-links/#api-rest-api-3-issuelink-linkid-delete)

---

POST

## Create issue link

Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link, use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`.

If the link request duplicates a link, the response indicates that the issue link was created. If the request included a comment, the comment is added.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse project_ [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues to be linked,
  * _Link issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) on the project containing the from (outward) issue,
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`write:comment:jira`, `write:issue:jira`, `write:issue-link:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The issue link request.

**comment**

Comment

**inwardIssue**

LinkedIssue

Required

**outwardIssue**

LinkedIssue

Required

**type**

IssueLinkType

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

404Not Found

413Request Entity Too Large

POST/rest/api/3/issueLink

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "comment": { "body": { "content": [ { "content": [ { "text": "Linked related issue!", "type": "text" } ], "type": "paragraph" } ], "type": "doc", "version": 1 }, "visibility": { "identifier": "276f955c-63d7-42c8-9520-92d01dca0625", "type": "group", "value": "jira-software-users" } }, "inwardIssue": { "key": "HSP-1" }, "outwardIssue": { "key": "MKY-1" }, "type": { "name": "Duplicate" } }`; const response = await requestJira(`/rest/api/3/issueLink`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get issue link

Returns an issue link.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse project_ [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `read:issue-link-type:jira`, `read:issue:jira`, `read:issue-type:jira`, `read:priority:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**linkId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueLink

Details of a link between issues.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/issueLink/{linkId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issueLink/{linkId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 ``{ "id": "10001", "inwardIssue": { "fields": { "issuetype": { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false }, "priority": { "description": "Very little impact.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/trivial.png", "id": "2", "name": "Trivial", "self": "https://your-domain.atlassian.net/rest/api/3/priority/5", "statusColor": "#cfcfcf" }, "status": { "description": "The issue is closed.", "iconUrl": "https://your-domain.atlassian.net/images/icons/closed.gif", "id": "5", "name": "Closed", "self": "https://your-domain.atlassian.net/rest/api/3/status/5", "statusCategory": { "colorName": "green", "id": 9, "key": "completed", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/9" } } }, "id": "10004", "key": "PR-3", "self": "https://your-domain.atlassian.net/rest/api/3/issue/PR-3" }, "outwardIssue": { "fields": { "issuetype": { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }, "priority": { "description": "Major loss of function.", "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/major.png", "id": "1", "name": "Major", "self": "https://your-domain.atlassian.net/rest/api/3/priority/3", "statusColor": "#009900" }, "status": { "description": "The issue is currently being worked on.", "iconUrl": "https://your-domain.atlassian.net/images/icons/progress.gif", "id": "10000", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/status/10000", "statusCategory": { "colorName": "yellow", "id": 1, "key": "in-flight", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1" } } }, "id": "10004L", "key": "PR-2", "self": "https://your-domain.atlassian.net/rest/api/3/issue/PR-2" }, "type": { "id": "1000", "inward": "Duplicated by", "name": "Duplicate", "outward": "Duplicates", "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000" } }`

---

DEL

## Delete issue link

Deletes an issue link.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * Browse project [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues in the link.
  * _Link issues_ [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one of the projects containing issues in the link.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:issue-link:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**linkId**

string

Required

### Responses

200OK

200 response

204No Content

400Bad Request

401Unauthorized

404Not Found

DEL/rest/api/3/issueLink/{linkId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issueLink/{linkId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`