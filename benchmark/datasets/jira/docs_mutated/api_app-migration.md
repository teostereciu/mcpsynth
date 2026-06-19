# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-app-migration/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# App migration

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource supports [app migrations](https://developer.atlassian.com/platform/app-migration/). Use it to:

  * [to request migrated workflow rules details](https://developer.atlassian.com/platform/app-migration/tutorials/migration-app-workflow-rules/).
  * [perform bulk updates of entity properties](https://developer.atlassian.com/platform/app-migration/tutorials/entity-properties-bulk-api/).
  * [perform bulk updates of issue custom field values](https://developer.atlassian.com/platform/app-migration/tutorials/migrating-app-custom-include_fields/).


Operations

[PUT/rest/atlassian-connect/1/migration/field](/cloud/jira/platform/rest/v3/api-group-app-migration/#api-rest-atlassian-connect-1-migration-field-put)[PUT/rest/atlassian-connect/1/migration/properties/{entityType}](/cloud/jira/platform/rest/v3/api-group-app-migration/#api-rest-atlassian-connect-1-migration-properties-entitytype-put)[POST/rest/atlassian-connect/1/migration/workflow/rule/search](/cloud/jira/platform/rest/v3/api-group-app-migration/#api-rest-atlassian-connect-1-migration-workflow-rule-search-post)

---

PUT

## Bulk update custom field value

Updates the value of a custom field added by Connect apps on one or more issues. The values of up to 200 custom include_fields can be updated.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Only Connect apps can make this request

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Header parameters

**Atlassian-Transfer-Id**

string

Required

#### Request bodyapplication/json

**updateValueList**

array<ConnectCustomFieldValue>

### Responses

200OK

Returned if the request is successful.

#### application/json

any

400Bad Request

403Forbidden

PUT/rest/atlassian-connect/1/migration/field

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 ``curl --request PUT \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/migration/field' \ --header 'Accept: application/json' \ --header 'Atlassian-Transfer-Id: <Atlassian-Transfer-Id>' \ --header 'Content-Type: application/json' \ --data '{ "updateValueList": [ { "_type": "StringIssueField", "issueID": 10001, "fieldID": 10076, "string": "new string value" }, { "_type": "TextIssueField", "issueID": 10002, "fieldID": 10077, "text": "new text value" }, { "_type": "SingleSelectIssueField", "issueID": 10003, "fieldID": 10078, "optionID": "1" }, { "_type": "MultiSelectIssueField", "issueID": 10004, "fieldID": 10079, "optionID": "2" }, { "_type": "RichTextIssueField", "issueID": 10005, "fieldID": 10080, "richText": "new rich text value" }, { "_type": "NumberIssueField", "issueID": 10006, "fieldID": 10082, "number": 54 } ] }'`

---

PUT

## Bulk update entity properties

Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Path parameters

**entityType**

string

Required

#### Header parameters

**Atlassian-Transfer-Id**

string

Required

#### Request bodyapplication/json

Expand all

array<EntityPropertyDetails>

Min items: `1`Max items: `50`

**entityId**

number

Required

**key**

string

Required

**value**

string

Required

### Responses

200OK

Returned if the request is successful.

400Bad Request

403Forbidden

PUT/rest/atlassian-connect/1/migration/properties/{entityType}

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 ``curl --request PUT \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/migration/properties/{entityType}' \ --header 'Atlassian-Transfer-Id: <Atlassian-Transfer-Id>' \ --header 'Content-Type: application/json' \ --data '[ { "entityId": 123, "key": "mykey", "value": "newValue" } ]'`

---

POST

## Get workflow transition rule configurations

Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

Forge and OAuth2 apps cannot access this REST resource.

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `NONE`

### Request

#### Header parameters

**Atlassian-Transfer-Id**

string

Required

#### Request bodyapplication/json

Expand all

**expand**

string

**ruleIds**

array<string>

Required

**workflowEntityId**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

WorkflowRulesSearchDetails

Details of workflow transition rules.

Show child properties

400Bad Request

403Forbidden

POST/rest/atlassian-connect/1/migration/workflow/rule/search

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``curl --request POST \ --url 'https://your-domain.atlassian.net/rest/atlassian-connect/1/migration/workflow/rule/search' \ --header 'Accept: application/json' \ --header 'Atlassian-Transfer-Id: <Atlassian-Transfer-Id>' \ --header 'Content-Type: application/json' \ --data '{ "expand": "transition", "ruleIds": [ "55d44f1d-c859-42e5-9c27-2c5ec3f340b1" ], "workflowEntityId": "a498d711-685d-428d-8c3e-bc03bb450ea7" }'`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``{ "workflowEntityId": "a498d711-685d-428d-8c3e-bc03bb450ea7", "invalidRules": [ "55d44f1d-c859-42e5-9c27-2c5ec3f340b1" ], "validRules": [ { "workflowId": { "name": "Workflow name", "draft": true }, "postFunctions": [ { "id": "123", "key": "WorkflowKey", "configuration": { "value": "WorkflowValidator" }, "transition": { "name": "transition", "id": 123 } } ], "conditions": [ { "id": "123", "key": "WorkflowKey", "configuration": { "value": "WorkflowValidator" }, "transition": { "name": "transition", "id": 123 } } ], "validators": [ { "id": "123", "key": "WorkflowKey", "configuration": { "value": "WorkflowValidator" }, "transition": { "name": "transition", "id": 123 } } ] } ] }`