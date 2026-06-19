# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow scheme drafts

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents draft workflow schemes. Use it to manage drafts of workflow schemes.

A workflow scheme maps issue types to workflows. A workflow scheme can be associated with one or more projects, which enables the projects to use the workflow-issue type mappings.

Active workflow schemes (workflow schemes that are used by projects) cannot be edited. Editing an active workflow scheme creates a draft copy of the scheme. The draft workflow scheme can then be edited and published (replacing the active scheme).

See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.

Operations

[POST/rest/api/3/workflowscheme/{id}/createdraft](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-createdraft-post)[GET/rest/api/3/workflowscheme/{id}/draft](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-get)[PUT/rest/api/3/workflowscheme/{id}/draft](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-put)[DEL/rest/api/3/workflowscheme/{id}/draft](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-delete)[GET/rest/api/3/workflowscheme/{id}/draft/default](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-default-get)[PUT/rest/api/3/workflowscheme/{id}/draft/default](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-default-put)[DEL/rest/api/3/workflowscheme/{id}/draft/default](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-default-delete)[GET/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-issuetype-issuetype-get)[PUT/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-issuetype-issuetype-put)[DEL/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-issuetype-issuetype-delete)[POST/rest/api/3/workflowscheme/{id}/draft/publish](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-publish-post)[GET/rest/api/3/workflowscheme/{id}/draft/workflow](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-workflow-get)[PUT/rest/api/3/workflowscheme/{id}/draft/workflow](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-workflow-put)[DEL/rest/api/3/workflowscheme/{id}/draft/workflow](/cloud/jira/platform/rest/v3/api-group-workflow-scheme-drafts/#api-rest-api-3-workflowscheme-id-draft-workflow-delete)

---

POST

## Create draft workflow scheme

Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:group:jira`, `read:issue-security-level:jira`, `read:project-role:jira`, `read:screen:jira`, `read:status:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

201Created

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/workflowscheme/{id}/createdraft

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/createdraft`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

GET

## Get draft workflow scheme

Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.
Note that:

  * Only active workflow schemes can have draft workflow schemes.
  * An active workflow scheme can only have one draft workflow scheme.


**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:group:jira`, `read:issue-security-level:jira`, `read:project-role:jira`, `read:screen:jira`, `read:status:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/draft

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

PUT

## Update draft workflow scheme

Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. Note that an active workflow scheme can only have one draft workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:group:jira`, `read:issue-security-level:jira`, `read:project-role:jira`, `read:screen:jira`, `read:status:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

**defaultWorkflow**

string

**description**

string

**issueTypeMappings**

object

**name**

string

**updateDraftIfNeeded**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/draft

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "issueTypeMappings": { "10000": "scrum workflow" }, "name": "Example workflow scheme", "updateDraftIfNeeded": false }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

DEL

## Delete draft workflow scheme

Deletes a draft workflow scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

204No Content

Returned if the request is successful.

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/draft

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get draft default workflow

Returns the default workflow for a workflow scheme's draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has _All Unassigned Issue Types_ listed in its issue types for the workflow scheme in Jira.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

DefaultWorkflow

Details about the default workflow.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/draft/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/default`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 ``{ "workflow": "jira" }`

---

PUT

## Update draft default workflow

Sets the default workflow for a workflow scheme's draft.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `read:workflow-scheme:jira`, `read:workflow:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Request bodyapplication/json

Expand all

The object for the new default workflow.

**updateDraftIfNeeded**

boolean

**workflow**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/draft/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "updateDraftIfNeeded": false, "workflow": "jira" }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/default`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

DEL

## Delete draft default workflow

Resets the default workflow for a workflow scheme's draft. That is, the default workflow is set to Jira's system workflow (the _jira_ workflow).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/draft/default

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/default`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

GET

## Get workflow for issue type in draft workflow scheme

Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`, `read:issue-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**issueType**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueTypeWorkflowMapping

Details about the mapping between an issue type and a workflow.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "issueType": "10000", "workflow": "jira" }`

---

PUT

## Set workflow for issue type in draft workflow scheme

Sets the workflow for an issue type in a workflow scheme's draft.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `read:workflow-scheme:jira`, `read:workflow:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**issueType**

string

Required

#### Request bodyapplication/json

Expand all

The issue type-project mapping.

**issueType**

string

**updateDraftIfNeeded**

boolean

**workflow**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueType": "10000", "updateDraftIfNeeded": false, "workflow": "jira" }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

DEL

## Delete workflow for issue type in draft workflow scheme

Deletes the issue type-workflow mapping for an issue type in a workflow scheme's draft.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`, `read:issue-type:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

Expand all

**id**

integer

Required

**issueType**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``{ "defaultWorkflow": "scrum workflow", "description": "The description of the example workflow scheme.", "draft": true, "id": 17218781, "issueTypeMappings": { "10000": "jira", "10001": "jira" }, "lastModified": "Today 6:38 PM", "lastModifiedUser": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": true, "applicationRoles": { "items": [], "size": 1 }, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "groups": { "items": [], "size": 3 }, "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "name": "Example workflow scheme", "originalDefaultWorkflow": "jira", "originalIssueTypeMappings": { "10001": "builds workflow" }, "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft" }`

---

POST

## Publish draft workflow scheme

Publishes a draft workflow scheme.

Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status.

This operation is [asynchronous](/cloud/jira/platform/rest/v3/intro/#async). Follow the `location` link in the response to determine the status of the task and use [Get task](/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) to obtain updates.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**validateOnly**

boolean

#### Request bodyapplication/json

Details of the status mappings.

**statusMappings**

array<StatusMapping>

### Responses

204No Content

Returned if the request is only for validation and is successful.

303See Other

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/workflowscheme/{id}/draft/publish

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "statusMappings": [ { "issueTypeId": "10001", "newStatusId": "1", "statusId": "3" }, { "issueTypeId": "10001", "newStatusId": "2", "statusId": "2" }, { "issueTypeId": "10002", "newStatusId": "10003", "statusId": "10005" }, { "issueTypeId": "10003", "newStatusId": "1", "statusId": "4" } ] }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/publish`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get issue types for workflows in draft workflow scheme

Returns the workflow-issue type mappings for a workflow scheme's draft.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow-scheme:jira`, `read:workflow:jira`, `read:issue-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**workflowName**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

IssueTypesWorkflowMapping

Details about the mapping between issue types and a workflow.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflowscheme/{id}/draft/workflow

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/workflow`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "defaultMapping": false, "issueTypes": [ "10000", "10001" ], "workflow": "jira" }`

---

PUT

## Set issue types for workflow in workflow scheme

Sets the issue types for a workflow in a workflow scheme's draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow-scheme:jira`, `read:workflow-scheme:jira`, `read:workflow:jira`, `read:application-role:jira`, `read:avatar:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**workflowName**

string

Required

#### Request bodyapplication/json

Expand all

**defaultMapping**

boolean

**issueTypes**

array<string>

**updateDraftIfNeeded**

boolean

**workflow**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowScheme

Details about a workflow scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflowscheme/{id}/draft/workflow

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "issueTypes": [ "10000" ], "updateDraftIfNeeded": true, "workflow": "jira" }`; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/workflow?workflowName={workflowName}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "defaultWorkflow": "jira", "description": "The description of the example workflow scheme.", "draft": false, "id": 101010, "issueTypeMappings": { "10000": "scrum workflow", "10001": "builds workflow" }, "name": "Example workflow scheme", "self": "https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010" }`

---

DEL

## Delete issue types for workflow in draft workflow scheme

Deletes the workflow-issue type mapping for a workflow in a workflow scheme's draft.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow-scheme:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

Required

#### Query parameters

**workflowName**

string

Required

### Responses

200OK

Returned if the request is successful.

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflowscheme/{id}/draft/workflow

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflowscheme/{id}/draft/workflow?workflowName={workflowName}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`