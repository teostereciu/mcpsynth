# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-expressions/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Jira expressions

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource is a collection of operations for [Jira expressions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

Operations

[POST/rest/api/3/expression/analyse](/cloud/jira/platform/rest/v3/api-group-jira-expressions/#api-rest-api-3-expression-analyse-post)[POST/rest/api/3/expression/eval](/cloud/jira/platform/rest/v3/api-group-jira-expressions/#api-rest-api-3-expression-eval-post)[POST/rest/api/3/expression/evaluate](/cloud/jira/platform/rest/v3/api-group-jira-expressions/#api-rest-api-3-expression-evaluate-post)

---

POST

## Analyse Jira expression

Analyses and validates Jira expressions.

As an experimental feature, this operation can also attempt to type-check the expressions.

Learn more about Jira expressions in the [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required**: None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `read:jira-user`

**Granular** :`read:field:jira`, `read:jira-expressions:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**check**

string

#### Request bodyapplication/json

Expand all

The Jira expressions to analyse.

**contextVariables**

object

**expressions**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

JiraExpressionsAnalysis

Details about the analysed Jira expression.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/expression/analyse

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "contextVariables": { "listOfStrings": "List<String>", "record": "{ a: Number, b: String }", "value": "User" }, "expressions": [ "issues.map(issue => issue.properties['property_key'])" ] }`; const response = await requestJira(`/rest/api/3/expression/analyse`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``{ "results": [ { "expression": "analysed expression", "errors": [ { "line": 1, "column": 4, "message": "!, -, typeof, (, IDENTIFIER, null, true, false, NUMBER, STRING, TEMPLATE_LITERAL, new, [ or { expected, > encountered.", "type": "syntax" }, { "message": "Jira expression is too long (1040), limit: 1000 characters", "type": "other" }, { "message": "Jira expression has too many nodes (150), limit: 100 leaves", "type": "other" } ], "valid": false }, { "expression": "issues.map(i => {idAndKey: [i.id, i.key], summary: i.summary, comments: i.comments})", "valid": true, "type": "List<{idAndKey: [Number, String], summary: String, comments: List<Comment>}>", "complexity": { "expensiveOperations": "N", "variables": { "N": "issues" } } }, { "expression": "issues.map(i => i.id > '0')", "errors": [ { "expression": "i.id > 0", "message": "Can't compare Number to String.", "type": "type" } ], "valid": false, "type": "TypeError" } ] }`

---

POST

## Currently being removed. Evaluate Jira expressionDeprecated

Endpoint is currently being removed. [More details](https://developer.atlassian.com/changelog/#CHANGE-2046)

Evaluates a Jira expression and returns its value.

This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data in a flexible way. Consult the [Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more details.

#### Context variables

The following context variables are available to Jira expressions evaluated by this resource. Their presence depends on various factors; usually you need to manually request them in the context object sent in the payload, but some of them are added automatically under certain conditions.

  * `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)): The current user. Always available and equal to `null` if the request is anonymous.
  * `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#app)): The [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request. Available only for authenticated requests made by Connect Apps (read more here: [Authentication for Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
  * `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): The current issue. Available only when the issue is provided in the request context object.
  * `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is provided in the request context object.
  * `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#project)): The current project. Available only when the project is provided in the request context object.
  * `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#sprint)): The current sprint. Available only when the sprint is provided in the request context object.
  * `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#board)): The current board. Available only when the board is provided in the request context object.
  * `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#servicedesk)): The current service desk. Available only when the service desk is provided in the request context object.
  * `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#customerrequest)): The current customer request. Available only when the customer request is provided in the request context object.


Also, custom context variables can be passed in the request with their types. Those variables can be accessed by key in the Jira expression. These variable types are available for use in a custom context:

  * `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.
  * `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the include_fields of the issue object are available in the Jira expression.
  * `json`: A JSON object containing custom content.
  * `list`: A JSON list of `user`, `issue`, or `json` variable types.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required**: None. However, an expression may return different results for different users depending on their permissions. For example, different users may see different comments on the same issue.
Permission to access Jira Software is required to access Jira Software context variables (`board` and `sprint`) or include_fields (for example, `issue.sprint`).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `read:jira-user`

**Granular** :`read:jira-expressions:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

string

#### Request bodyapplication/json

Expand all

The Jira expression and the evaluation context.

**context**

JiraExpressionEvalContextBean

**expression**

string

Required

### Responses

200OK

Returned if the evaluation results in a value. The result is a JSON primitive value, list, or object.

#### application/json

JiraExpressionResult

The result of evaluating a Jira expression.

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/expression/eval

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "context": { "board": 10100, "custom": { "config": { "type": "json", "value": { "userId": "10002" } }, "issuesList": [ { "key": "ACJIRA-1471", "type": "issue" }, { "id": 100001, "type": "issue" } ], "myUser": { "user_id": "100001", "type": "user" }, "nullField": { "type": "json" } }, "customerRequest": 1450, "issue": { "key": "ACJIRA-1470" }, "issues": { "jql_query": { "page_size": 100, "query": "project = HSP", "start_index": 0, "validation": "strict" } }, "project": { "key": "ACJIRA" }, "serviceDesk": 10023, "sprint": 10001 }, "expression": "{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id), listCustomVariable: issuesList.includes(issue), customVariables: myUser.user_id == config.userId}" }`; const response = await requestJira(`/rest/api/3/expression/eval`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``{ "value": "The expression's result. This value can be any JSON, not necessarily a String", "meta": { "complexity": { "steps": { "value": 1, "limit": 10000 }, "expensiveOperations": { "value": 3, "limit": 10 }, "beans": { "value": 0, "limit": 1000 }, "primitiveValues": { "value": 1, "limit": 10000 } }, "issues": { "jql_query": { "start_index": 0, "page_size": 1000, "count": 140, "totalCount": 140, "validationWarnings": [ "There is a problem with the JQL query." ] } } } }`

---

POST

## Evaluate Jira expression using enhanced search API

Evaluates a Jira expression and returns its value. The difference between this and `eval` is that this endpoint uses the enhanced search API when evaluating JQL queries. This API is eventually consistent, unlike the strongly consistent `eval` API. This allows for better performance and scalability. In addition, this API's response for JQL evaluation is based on a scrolling view (backed by a `nextPageToken`) instead of a paginated view (backed by `start_index` and `totalCount`).

This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data in a flexible way. Consult the [Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more details.

#### Context variables

The following context variables are available to Jira expressions evaluated by this resource. Their presence depends on various factors; usually you need to manually request them in the context object sent in the payload, but some of them are added automatically under certain conditions.

  * `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)): The current user. Always available and equal to `null` if the request is anonymous.
  * `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#app)): The [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request. Available only for authenticated requests made by Connect apps (read more here: [Authentication for Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
  * `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): The current issue. Available only when the issue is provided in the request context object.
  * `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is provided in the request context object.
  * `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#project)): The current project. Available only when the project is provided in the request context object.
  * `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#sprint)): The current sprint. Available only when the sprint is provided in the request context object.
  * `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#board)): The current board. Available only when the board is provided in the request context object.
  * `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#servicedesk)): The current service desk. Available only when the service desk is provided in the request context object.
  * `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#customerrequest)): The current customer request. Available only when the customer request is provided in the request context object.


In addition, you can pass custom context variables along with their types. You can then access them from the Jira expression by key. You can use the following variables in a custom context:

  * `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.
  * `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the include_fields of the issue object are available in the Jira expression.
  * `json`: A JSON object containing custom content.
  * `list`: A JSON list of `user`, `issue`, or `json` variable types.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required**: None. However, an expression may return different results for different users depending on their permissions. For example, different users may see different comments on the same issue.
Permission to access Jira Software is required to access Jira Software context variables (`board` and `sprint`) or include_fields (for example, `issue.sprint`).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`, `read:jira-user`

**Granular** :`read:jira-expressions:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

string

#### Request bodyapplication/json

Expand all

The Jira expression and the evaluation context.

**context**

JiraExpressionEvaluateContextBean

**expression**

string

Required

### Responses

200OK

Returned if the evaluation results in a value. The result is a JSON primitive value, list, or object.

#### application/json

JExpEvaluateJiraExpressionResultBean

The result of evaluating a Jira expression.This bean will be replacing `JiraExpressionResultBean` bean as part of new evaluate endpoint

Show child properties

400Bad Request

401Unauthorized

404Not Found

POST/rest/api/3/expression/evaluate

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "context": { "board": 10100, "custom": { "config": { "type": "json", "value": { "userId": "10002" } }, "issuesList": [ { "key": "ACJIRA-1471", "type": "issue" }, { "id": 100001, "type": "issue" } ], "myUser": { "user_id": "100001", "type": "user" }, "nullField": { "type": "json" } }, "customerRequest": 1450, "issue": { "key": "ACJIRA-1470" }, "issues": { "jql_query": { "page_size": 100, "nextPageToken": "EgQIlMIC", "query": "project = HSP" } }, "project": { "key": "ACJIRA" }, "serviceDesk": 10023, "sprint": 10001 }, "expression": "{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id), listCustomVariable: issuesList.includes(issue), customVariables: myUser.user_id == config.userId}" }`; const response = await requestJira(`/rest/api/3/expression/evaluate`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``{ "value": "The expression's result. This value can be any JSON, not necessarily a String", "meta": { "complexity": { "steps": { "value": 1, "limit": 10000 }, "expensiveOperations": { "value": 3, "limit": 10 }, "beans": { "value": 0, "limit": 1000 }, "primitiveValues": { "value": 1, "limit": 10000 } }, "issues": { "jql_query": { "nextPageToken": "EgQIlMIC", "isLast": false } } } }`