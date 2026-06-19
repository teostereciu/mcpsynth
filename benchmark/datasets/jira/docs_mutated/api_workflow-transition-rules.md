# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Workflow transition rules

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents workflow transition rules. Workflow transition rules define a Connect or a Forge app routine, such as a [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/) that is executed in association with the workflow. Use it to read and modify configuration of workflow transition rules.

Operations

[GET/rest/api/3/workflow/rule/config](/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get)[PUT/rest/api/3/workflow/rule/config](/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-put)[PUT/rest/api/3/workflow/rule/config/delete](/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-delete-put)

---

GET

## Get workflow transition rule configurations

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:

  * of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
  * matching one or more transition rule keys.


Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.

Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:workflow:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**start_index**

integer

**page_size**

integer

**types**

array<string>

Required

**keys**

array<string>

**workflowNames**

array<string>

**withTags**

array<string>

**draft**

boolean

**expand**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanWorkflowTransitionRules

A page of items.

Show child properties

400Bad Request

403Forbidden

404Not Found

503Service Unavailable

GET/rest/api/3/workflow/rule/config

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/workflow/rule/config?types={types}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 ``{ "isLast": true, "page_size": 10, "start_index": 0, "total": 1, "values": [ { "workflowId": { "name": "My Workflow name", "draft": false }, "postFunctions": [ { "id": "b4d6cbdc-59f5-11e9-8647-d663bd873d93", "key": "postfunction-key", "configuration": { "value": "{ \"color\": \"red\" }", "disabled": false, "tag": "Sample tag" }, "transition": { "id": 1, "name": "Open" } } ], "conditions": [ { "id": "d663bd873d93-59f5-11e9-8647-b4d6cbdc", "key": "condition-key", "configuration": { "value": "{ \"size\": \"medium\" }", "disabled": false, "tag": "Another tag" }, "transition": { "id": 1, "name": "Open" } } ], "validators": [ { "id": "11e9-59f5-b4d6cbdc-8647-d663bd873d93", "key": "validator-key", "configuration": { "value": "\"{ \\\"shape\\\": \\\"square\\\" }\"", "disabled": false }, "transition": { "id": 1, "name": "Open" } } ] } ] }`

---

PUT

## Update workflow transition rule configurations

Updates configuration of workflow transition rules. The following rule types are supported:

  * [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
  * [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
  * [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)


Only rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app can be updated.

To assist with app migration, this operation can be used to:

  * Disable a rule.
  * Add a `tag`. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).


Rules are enabled if the `disabled` parameter is not provided.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:workflow:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

**workflows**

array<WorkflowTransitionRules>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowTransitionRulesUpdateErrors

Details of any errors encountered while updating workflow transition rules.

Show child properties

400Bad Request

403Forbidden

503Service Unavailable

PUT/rest/api/3/workflow/rule/config

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "workflows": [ { "conditions": [ { "configuration": { "disabled": false, "tag": "Another tag", "value": "{ \"size\": \"medium\" }" }, "id": "d663bd873d93-59f5-11e9-8647-b4d6cbdc" } ], "postFunctions": [ { "configuration": { "disabled": false, "tag": "Sample tag", "value": "{ \"color\": \"red\" }" }, "id": "b4d6cbdc-59f5-11e9-8647-d663bd873d93" } ], "validators": [ { "configuration": { "disabled": false, "value": "{ \"shape\": \"square\" }" }, "id": "11e9-59f5-b4d6cbdc-8647-d663bd873d93" } ], "workflowId": { "draft": false, "name": "My Workflow name" } } ] }`; const response = await requestJira(`/rest/api/3/workflow/rule/config`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``{ "updateResults": [ { "workflowId": { "name": "Workflow with one rule not updated", "draft": false }, "ruleUpdateErrors": { "example-rule-id": [ "The rule with this id does not exist: example-rule-id" ] }, "updateErrors": [] }, { "workflowId": { "name": "Workflow with all rules successfully updated", "draft": true }, "ruleUpdateErrors": {}, "updateErrors": [] }, { "workflowId": { "name": "Non-existing workflow", "draft": false }, "ruleUpdateErrors": {}, "updateErrors": [ "Workflow not found: WorkflowIdBean{name=Non-existing workflow, draft=false}" ] } ] }`

---

PUT

## Delete workflow transition rule configurations

Deletes workflow transition rules from one or more workflows. These rule types are supported:

  * [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
  * [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
  * [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)


Only rules created by the calling Connect app can be deleted.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect apps can use this operation.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

**workflows**

array<WorkflowTransitionRulesDetails>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowTransitionRulesUpdateErrors

Details of any errors encountered while updating workflow transition rules.

Show child properties

400Bad Request

403Forbidden

PUT/rest/api/3/workflow/rule/config/delete

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``curl --request PUT \ --url 'https://your-domain.atlassian.net/rest/api/3/workflow/rule/config/delete' \ --user 'email@example.com:<api_token>' \ --header 'Accept: application/json' \ --header 'Content-Type: application/json' \ --data '{ "workflows": [ { "workflowId": { "draft": false, "name": "Internal support workflow" }, "workflowRuleIds": [ "b4d6cbdc-59f5-11e9-8647-d663bd873d93", "d663bd873d93-59f5-11e9-8647-b4d6cbdc", "11e9-59f5-b4d6cbdc-8647-d663bd873d93" ] } ] }'`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``{ "updateResults": [ { "workflowId": { "name": "Workflow with one rule not updated", "draft": false }, "ruleUpdateErrors": { "example-rule-id": [ "The rule with this id does not exist: example-rule-id" ] }, "updateErrors": [] }, { "workflowId": { "name": "Workflow with all rules successfully updated", "draft": true }, "ruleUpdateErrors": {}, "updateErrors": [] }, { "workflowId": { "name": "Non-existing workflow", "draft": false }, "ruleUpdateErrors": {}, "updateErrors": [ "Workflow not found: WorkflowIdBean{name=Non-existing workflow, draft=false}" ] } ] }`