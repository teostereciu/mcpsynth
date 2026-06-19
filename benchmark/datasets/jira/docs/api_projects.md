# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Projects

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents projects. Use it to get, create, update, and delete projects. Also get statuses available to a project, a project's notification schemes, and update a project's type.

Operations

[GET/rest/api/3/project](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get)[POST/rest/api/3/project](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-post)[GET/rest/api/3/project/recent](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-recent-get)[GET/rest/api/3/project/search](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get)[GET/rest/api/3/project/{projectIdOrKey}](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-get)[PUT/rest/api/3/project/{projectIdOrKey}](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-put)[DEL/rest/api/3/project/{projectIdOrKey}](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-delete)[POST/rest/api/3/project/{projectIdOrKey}/archive](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-archive-post)[POST/rest/api/3/project/{projectIdOrKey}/delete](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-delete-post)[POST/rest/api/3/project/{projectIdOrKey}/restore](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-restore-post)[GET/rest/api/3/project/{projectIdOrKey}/statuses](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectidorkey-statuses-get)[GET/rest/api/3/project/{projectId}/hierarchy](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectid-hierarchy-get)[GET/rest/api/3/project/{projectKeyOrId}/notificationscheme](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-projectkeyorid-notificationscheme-get)

---

GET

## Get all projectsDeprecated

Returns all projects visible to the user. Deprecated, use [ Get projects paginated](/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get) that supports search and pagination.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Projects are returned only where the user has _Browse Projects_ or _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:project:jira`, `read:project.property:jira`, `read:user:jira`, `read:application-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**expand**

string

**recent**

integer

**properties**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Project>

Show child properties

401Unauthorized

GET/rest/api/3/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``[ { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "id": "10000", "insight": { "lastIssueUpdateTime": 1619069825000, "totalIssueCount": 100 }, "key": "EX", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "CLASSIC" }, { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10001", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10001", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10001", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10001" }, "id": "10001", "insight": { "lastIssueUpdateTime": 1619069825000, "totalIssueCount": 100 }, "key": "ABC", "name": "Alphabetical", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/ABC", "simplified": false, "style": "CLASSIC" } ]`

---

POST

## Create project

Creates a project based on a project type template, as shown in the following table:

Project Type Key| Project Template Key
---|---
`business`| `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`, `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking`
`service_desk`| `com.atlassian.servicedesk:simplified-it-service-management`, `com.atlassian.servicedesk:simplified-external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`, `com.atlassian.servicedesk:simplified-facilities-service-desk`, `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`, `com.atlassian.servicedesk:simplified-design-service-desk`, `com.atlassian.servicedesk:simplified-sales-service-desk`, `com.atlassian.servicedesk:simplified-finance-service-desk`, `com.atlassian.servicedesk:company-managed-blank-service-project`, `com.atlassian.servicedesk:company-managed-general-service-project`, `com.atlassian.servicedesk:team-managed-general-service-project`, `com.atlassian.servicedesk:next-gen-it-service-desk`, `com.atlassian.servicedesk:next-gen-hr-service-desk`, `com.atlassian.servicedesk:next-gen-legal-service-desk`, `com.atlassian.servicedesk:next-gen-marketing-service-desk`, `com.atlassian.servicedesk:next-gen-facilities-service-desk`, `com.atlassian.servicedesk:next-gen-analytics-service-desk`, `com.atlassian.servicedesk:next-gen-finance-service-desk`, `com.atlassian.servicedesk:next-gen-design-service-desk`, `com.atlassian.servicedesk:next-gen-sales-service-desk`
`software`| `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`, `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-simplified-scrum-classic`
`customer_service`| `com.atlassian.jcs:customer-service-management`
The project types are available according to the installed Jira features as follows:|

  * Jira Core, the default, enables `business` projects.
  * Jira Service Management enables `service_desk` projects.
  * Jira Software enables `software` projects.


To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance, use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-ons](https://confluence.atlassian.com/x/S31NLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Request bodyapplication/json

Expand all

The JSON representation of the project being created.

**assigneeType**

string

**avatarId**

integer

**categoryId**

integer

**description**

string

**fieldConfigurationScheme**

integer

Deprecated

**fieldScheme**

integer

**issueSecurityScheme**

integer

**issueTypeScheme**

integer

**issueTypeScreenScheme**

integer

**key**

string

Required

Show 9 hidden parameters

### Responses

201Created

Returned if the project is created.

#### application/json

ProjectIdentifiers

Identifiers for a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "assigneeType": "PROJECT_LEAD", "avatarId": 10200, "categoryId": 10120, "description": "Cloud migration initiative", "issueSecurityScheme": 10001, "key": "EX", "leadAccountId": "5b10a0effa615349cb016cd8", "name": "Example", "notificationScheme": 10021, "permissionScheme": 10011, "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control", "projectTypeKey": "business", "url": "http://atlassian.com" }`; const response = await requestJira(`/rest/api/3/project`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 ``{ "id": 10010, "key": "EX", "self": "https://your-domain.atlassian.net/jira/rest/api/3/project/10042" }`

---

GET

## Get recent projectsExperimental

Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Projects are returned only where the user has one of:

  * _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:project:jira`, `read:project.property:jira`, `read:user:jira`, `read:application-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**expand**

string

**properties**

array<StringList>

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Project>

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/project/recent

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/recent`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``[ { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "id": "10000", "insight": { "lastIssueUpdateTime": 1619069825000, "totalIssueCount": 100 }, "key": "EX", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "CLASSIC" }, { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10001", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10001", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10001", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10001" }, "id": "10001", "insight": { "lastIssueUpdateTime": 1619069825000, "totalIssueCount": 100 }, "key": "ABC", "name": "Alphabetical", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/ABC", "simplified": false, "style": "CLASSIC" } ]`

---

GET

## Get projects paginated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of projects visible to the user.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Projects are returned only where the user has one of:

  * _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:project:jira`, `read:project.property:jira`, `read:user:jira`, `read:application-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**startAt**

integer

**maxResults**

integer

**orderBy**

string

**id**

array<integer>

**keys**

array<string>

**query**

string

**typeKey**

string

**categoryId**

integer

**action**

string

**expand**

string

Show 3 hidden parameters

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanProject

A page of items.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/project/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/search`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 ``{ "isLast": false, "maxResults": 2, "nextPage": "https://your-domain.atlassian.net/rest/api/3/project/search?startAt=2&maxResults=2", "self": "https://your-domain.atlassian.net/rest/api/3/project/search?startAt=0&maxResults=2", "startAt": 0, "total": 7, "values": [ { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "key": "EX", "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic" }, { "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10001", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10001", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10001", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10001" }, "id": "10001", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "key": "ABC", "name": "Alphabetical", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/ABC", "simplified": false, "style": "classic" } ] }`

---

GET

## Get project

Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:project:jira`, `read:project.property:jira`, `read:user:jira`, `read:application-role:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Query parameters

Expand all

**expand**

string

**properties**

array<string>

### Responses

200OK

Returned if successful.

#### application/json

Project

Details about a project.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 ``{ "assigneeType": "PROJECT_LEAD", "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "components": [ { "ari": "ari:cloud:compass:fdb3fdec-4e70-be56-11ee-0242ac120002:component/fdb3fdec-4e70-11ee-be56-0242ac120002/fdb3fdec-11ee-4e70-be56-0242ac120002", "assignee": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "assigneeType": "PROJECT_LEAD", "description": "This is a Jira component", "id": "10000", "isAssigneeTypeValid": false, "lead": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "metadata": { "icon": "https://www.example.com/icon.png" }, "name": "Component 1", "project": "HSP", "projectId": 10000, "realAssignee": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "realAssigneeType": "PROJECT_LEAD", "self": "https://your-domain.atlassian.net/rest/api/3/component/10000" } ], "description": "This project was created as an example for REST.", "email": "from-jira@example.com", "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "issueTypes": [ { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }, { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false } ], "key": "EX", "lead": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "properties": { "propertyKey": "propertyValue" }, "roles": { "Developers": "https://your-domain.atlassian.net/rest/api/3/project/EX/role/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic", "url": "https://www.example.com", "versions": [] }`

---

PUT

## Update project

Updates the [project details](https://confluence.atlassian.com/x/ahLpNw) of a project.

All parameters are optional in the body of the request. Schemes will only be updated if they are included in the request, any omitted schemes will be left unchanged.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg). is only needed when changing the schemes or project key. Otherwise you will only need _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg)

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`read:issue-type:jira`, `read:project:jira`, `read:project.property:jira`, `read:user:jira`, `write:project:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Query parameters

**expand**

string

#### Request bodyapplication/json

Expand all

The project details to be updated.

**assigneeType**

string

**avatarId**

integer

**categoryId**

integer

**description**

string

**issueSecurityScheme**

integer

**key**

string

**lead**

string

**leadAccountId**

string

**name**

string

**notificationScheme**

integer

Show 3 hidden parameters

### Responses

200OK

Returned if the project is updated.

#### application/json

Project

Details about a project.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/project/{projectIdOrKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "assigneeType": "PROJECT_LEAD", "avatarId": 10200, "categoryId": 10120, "description": "Cloud migration initiative", "issueSecurityScheme": 10001, "key": "EX", "leadAccountId": "5b10a0effa615349cb016cd8", "name": "Example", "notificationScheme": 10021, "permissionScheme": 10011, "url": "http://atlassian.com" }`; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 ``{ "assigneeType": "PROJECT_LEAD", "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "components": [ { "ari": "ari:cloud:compass:fdb3fdec-4e70-be56-11ee-0242ac120002:component/fdb3fdec-4e70-11ee-be56-0242ac120002/fdb3fdec-11ee-4e70-be56-0242ac120002", "assignee": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "assigneeType": "PROJECT_LEAD", "description": "This is a Jira component", "id": "10000", "isAssigneeTypeValid": false, "lead": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "metadata": { "icon": "https://www.example.com/icon.png" }, "name": "Component 1", "project": "HSP", "projectId": 10000, "realAssignee": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "realAssigneeType": "PROJECT_LEAD", "self": "https://your-domain.atlassian.net/rest/api/3/component/10000" } ], "description": "This project was created as an example for REST.", "email": "from-jira@example.com", "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "issueTypes": [ { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }, { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false } ], "key": "EX", "lead": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "properties": { "propertyKey": "propertyValue" }, "roles": { "Developers": "https://your-domain.atlassian.net/rest/api/3/project/EX/role/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic", "url": "https://www.example.com", "versions": [] }`

---

DEL

## Delete project

Deletes a project.

You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

#### Query parameters

**enableUndo**

boolean

### Responses

204No Content

Returned if the project is deleted.

401Unauthorized

404Not Found

DEL/rest/api/3/project/{projectIdOrKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

POST

## Archive project

Archives a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-project`

**Granular** :`write:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/project/{projectIdOrKey}/archive

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/archive`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

POST

## Delete project asynchronouslyExperimental

Deletes a project asynchronously.

This operation is:

  * transactional, that is, if part of the delete fails the project is not deleted.
  * [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain subsequent updates.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:project:jira`, `write:project.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

303See Other

Returned if the request is successful.

#### application/json

TaskProgressBeanObject

Details about a task.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/project/{projectIdOrKey}/delete

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/delete`, { method: 'POST' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

303Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``{ "description": "<string>", "elapsedRuntime": 48, "finished": 49, "id": "<string>", "lastUpdate": 62, "message": "<string>", "progress": 51, "self": "<string>", "started": 48, "status": "ENQUEUED", "submitted": 50, "submittedBy": 42 }`

---

POST

## Restore deleted or archived projectExperimental

Restores a project that has been archived or placed in the Jira recycle bin.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg)for Company managed projects.
  * _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project for Team managed projects.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:issue-type:jira`, `read:project:jira`, `read:project.property:jira`, `read:user:jira`, `write:project:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `PROJECT_ADMIN`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

Project

Details about a project.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/project/{projectIdOrKey}/restore

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/restore`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 ``{ "assigneeType": "PROJECT_LEAD", "avatarUrls": { "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000", "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000", "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000", "48x48": "https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000" }, "components": [ { "ari": "ari:cloud:compass:fdb3fdec-4e70-be56-11ee-0242ac120002:component/fdb3fdec-4e70-11ee-be56-0242ac120002/fdb3fdec-11ee-4e70-be56-0242ac120002", "assignee": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "assigneeType": "PROJECT_LEAD", "description": "This is a Jira component", "id": "10000", "isAssigneeTypeValid": false, "lead": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "metadata": { "icon": "https://www.example.com/icon.png" }, "name": "Component 1", "project": "HSP", "projectId": 10000, "realAssignee": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "realAssigneeType": "PROJECT_LEAD", "self": "https://your-domain.atlassian.net/rest/api/3/component/10000" } ], "description": "This project was created as an example for REST.", "email": "from-jira@example.com", "id": "10000", "insight": { "lastIssueUpdateTime": "2021-04-22T05:37:05.000+0000", "totalIssueCount": 100 }, "issueTypes": [ { "avatarId": 1, "description": "A task that needs to be done.", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\",", "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "subtask": false }, { "avatarId": 10002, "description": "A problem with the software.", "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2", "hierarchyLevel": 0, "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\",", "id": "1", "name": "Bug", "scope": { "project": { "id": "10000" }, "type": "PROJECT" }, "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1", "subtask": false } ], "key": "EX", "lead": { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" }, "name": "Example", "projectCategory": { "description": "First Project Category", "id": "10000", "name": "FIRST", "self": "https://your-domain.atlassian.net/rest/api/3/projectCategory/10000" }, "properties": { "propertyKey": "propertyValue" }, "roles": { "Developers": "https://your-domain.atlassian.net/rest/api/3/project/EX/role/10000" }, "self": "https://your-domain.atlassian.net/rest/api/3/project/EX", "simplified": false, "style": "classic", "url": "https://www.example.com", "versions": [] }`

---

GET

## Get all statuses for project

Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-status:jira`, `read:issue-type:jira`, `read:status:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectIdOrKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<IssueTypeWithStatus>

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectIdOrKey}/statuses

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectIdOrKey}/statuses`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``[ { "id": "3", "name": "Task", "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3", "statuses": [ { "description": "The issue is currently being worked on.", "iconUrl": "https://your-domain.atlassian.net/images/icons/progress.gif", "id": "10000", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/status/10000" }, { "description": "The issue is closed.", "iconUrl": "https://your-domain.atlassian.net/images/icons/closed.gif", "id": "5", "name": "Closed", "self": "https://your-domain.atlassian.net/rest/api/3/status/5" } ], "subtask": false } ]`

---

GET

## Get project issue type hierarchy

Get the issue type hierarchy for a next-gen project.

The issue type hierarchy for a project consists of:

  * _Epic_ at level 1 (optional).
  * One or more issue types at level 0 such as _Story_ , _Task_ , or _Bug_. Where the issue type _Epic_ is defined, these issue types are used to break down the content of an epic.
  * _Subtask_ at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-type:jira`, `read:issue-type-hierarchy:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectId**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectIssueTypeHierarchy

The hierarchy of issue types within a project.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectId}/hierarchy

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectId}/hierarchy`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``{ "hierarchy": [ { "issueTypes": [ { "avatarId": 10324, "entityId": "ce32639b-8911-4689-81da-65681f451516", "id": 10008, "name": "Story" }, { "avatarId": 10324, "entityId": "ffdbced5-fbfc-4370-a848-94e2ce3751af", "id": 10001, "name": "Bug" } ], "level": 0, "name": "Base" }, { "issueTypes": [ { "avatarId": 10179, "entityId": "80f20d47-34dc-4680-8937-936b7e762a35", "id": 10007, "name": "Epic" } ], "level": 1, "name": "Epic" }, { "issueTypes": [ { "avatarId": 10573, "entityId": "210b4879-15cc-414c-9746-f8f6b6be0a72", "id": 10009, "name": "Subtask" } ], "level": -1, "name": "Subtask" } ], "projectId": 10030 }`

---

GET

## Get project notification scheme

Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg) or _Administer Projects_ [project permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-category:jira`, `read:project-role:jira`, `read:project:jira`, `read:user:jira`, `read:group:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectKeyOrId**

string

Required

#### Query parameters

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

NotificationScheme

Details about a notification scheme.

Show child properties

400Bad Request

401Unauthorized

404Not Found

GET/rest/api/3/project/{projectKeyOrId}/notificationscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/{projectKeyOrId}/notificationscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 ``{ "description": "description", "expand": "notificationSchemeEvents,user,group,projectRole,field,all", "id": 10100, "name": "notification scheme name", "notificationSchemeEvents": [ { "event": { "description": "Event published when an issue is created", "id": 1, "name": "Issue created" }, "notifications": [ { "expand": "group", "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 1, "notificationType": "Group", "parameter": "jira-administrators", "recipient": "276f955c-63d7-42c8-9520-92d01dca0625" }, { "id": 2, "notificationType": "CurrentAssignee" }, { "expand": "projectRole", "id": 3, "notificationType": "ProjectRole", "parameter": "10360", "projectRole": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "accountId": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "recipient": "10360" }, { "emailAddress": "rest-developer@atlassian.com", "id": 4, "notificationType": "EmailAddress", "parameter": "rest-developer@atlassian.com", "recipient": "rest-developer@atlassian.com" }, { "expand": "user", "id": 5, "notificationType": "User", "parameter": "5b10a2844c20165700ede21g", "recipient": "5b10a2844c20165700ede21g", "user": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" } }, { "expand": "field", "field": { "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }, "id": 6, "notificationType": "GroupCustomField", "parameter": "customfield_10101", "recipient": "customfield_10101" } ] }, { "event": { "description": "Custom event that is published together with an issue created event", "id": 20, "name": "Custom event", "templateEvent": { "description": "Event published when an issue is created", "id": 1, "name": "Issue created" } }, "notifications": [ { "expand": "group", "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 1, "notificationType": "Group", "parameter": "jira-administrators", "recipient": "276f955c-63d7-42c8-9520-92d01dca0625" }, { "id": 2, "notificationType": "CurrentAssignee" }, { "expand": "projectRole", "id": 3, "notificationType": "ProjectRole", "parameter": "10360", "projectRole": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "accountId": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "recipient": "10360" }, { "emailAddress": "rest-developer@atlassian.com", "id": 4, "notificationType": "EmailAddress", "parameter": "rest-developer@atlassian.com", "recipient": "rest-developer@atlassian.com" }, { "expand": "user", "id": 5, "notificationType": "User", "parameter": "5b10a2844c20165700ede21g", "recipient": "5b10a2844c20165700ede21g", "user": { "accountId": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g" } }, { "expand": "field", "field": { "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }, "id": 6, "notificationType": "GroupCustomField", "parameter": "customfield_10101", "recipient": "customfield_10101" } ] } ], "projects": [ 10001, 10002 ], "self": "https://your-domain.atlassian.net/rest/api/3/notificationscheme" }`