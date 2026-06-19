# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-properties/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow transition properties

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents workflow transition properties, which provides for storing custom data against a workflow transition. Use it to get, create, and delete workflow transition properties as well as get a list of property keys for a workflow transition. Workflow transition properties are a type of [entity property](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

Operations

[GET/rest/api/3/workflow/transitions/{transitionId}/properties](/cloud/jira/platform/rest/v3/api-group-workflow-transition-properties/#api-rest-api-3-workflow-transitions-transitionid-properties-get)[PUT/rest/api/3/workflow/transitions/{transitionId}/properties](/cloud/jira/platform/rest/v3/api-group-workflow-transition-properties/#api-rest-api-3-workflow-transitions-transitionid-properties-put)[POST/rest/api/3/workflow/transitions/{transitionId}/properties](/cloud/jira/platform/rest/v3/api-group-workflow-transition-properties/#api-rest-api-3-workflow-transitions-transitionid-properties-post)[DEL/rest/api/3/workflow/transitions/{transitionId}/properties](/cloud/jira/platform/rest/v3/api-group-workflow-transition-properties/#api-rest-api-3-workflow-transitions-transitionid-properties-delete)

---

GET

## Get workflow transition propertiesDeprecated

This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2570); fetch transition properties from [Bulk get workflows](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-rest-api-3-workflows-post) instead.

Returns the properties on a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**transitionId**

integer

Required

#### Query parameters

Expand all

**includeReservedKeys**

boolean

**key**

string

**workflowName**

string

Required

**workflowMode**

string

### Responses

200OK

200 response

#### application/json

WorkflowTransitionProperty

Details about the server Jira is running on.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/workflow/transitions/{transitionId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflow/transitions/{transitionId}/properties?workflowName={workflowName}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``[ { "id": "jira.i18n.title", "key": "jira.i18n.title", "value": "some.title" }, { "id": "jira.permission", "key": "jira.permission", "value": "createissue" } ]`

---

PUT

## Update workflow transition propertyDeprecated

This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2570); update transition properties using [Bulk update workflows](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-rest-api-3-workflows-update-post) instead.

Updates a workflow transition by changing the property value. Trying to update a property that does not exist results in a new property being added to the transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow.property:jira`, `read:workflow.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**transitionId**

integer

Required

#### Query parameters

Expand all

**key**

string

Required

**workflowName**

string

Required

**workflowMode**

string

#### Request bodyapplication/json

Expand all

**value**

string

Required

**Additional Properties**

any

### Responses

200OK

200 response

#### application/json

WorkflowTransitionProperty

Details about the server Jira is running on.

Show child properties

304Not Modified

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/workflow/transitions/{transitionId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "value": "createissue" }`; const response = await requestJira(`/rest/api/3/workflow/transitions/{transitionId}/properties?key={key}&workflowName={workflowName}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "key": "jira.i18n.title", "value": "some.title", "id": "jira.i18n.title" }`

---

POST

## Create workflow transition propertyDeprecated

This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2570); add transition properties using [Bulk update workflows](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-rest-api-3-workflows-update-post) instead.

Adds a property to a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow.property:jira`, `read:workflow.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**transitionId**

integer

Required

#### Query parameters

Expand all

**key**

string

Required

**workflowName**

string

Required

**workflowMode**

string

#### Request bodyapplication/json

Expand all

**value**

string

Required

**Additional Properties**

any

### Responses

200OK

200 response

#### application/json

WorkflowTransitionProperty

Details about the server Jira is running on.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

POST/rest/api/3/workflow/transitions/{transitionId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "value": "createissue" }`; const response = await requestJira(`/rest/api/3/workflow/transitions/{transitionId}/properties?key={key}&workflowName={workflowName}`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 ``{ "key": "jira.i18n.title", "value": "some.title", "id": "jira.i18n.title" }`

---

DEL

## Delete workflow transition propertyDeprecated

This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2570); delete transition properties using [Bulk update workflows](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-rest-api-3-workflows-update-post) instead.

Deletes a property from a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`delete:workflow.property:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**transitionId**

integer

Required

#### Query parameters

Expand all

**key**

string

Required

**workflowName**

string

Required

**workflowMode**

string

### Responses

200OK

200 response

304Not Modified

400Bad Request

401Unauthorized

403Forbidden

404Not Found

DEL/rest/api/3/workflow/transitions/{transitionId}/properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflow/transitions/{transitionId}/properties?key={key}&workflowName={workflowName}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`