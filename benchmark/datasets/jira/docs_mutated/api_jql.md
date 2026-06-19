# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql_query/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# JQL

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents JQL search auto-complete details. Use it to obtain JQL search auto-complete data and suggestions for use in programmatic construction of queries or custom query builders. It also provides operations to:

  * convert one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.
  * convert readable details in one or more JQL queries to IDs where a user doesn't have permission to view the entity whose details are readable.


Operations

[GET/rest/api/3/jql_query/autocompletedata](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-autocompletedata-get)[POST/rest/api/3/jql_query/autocompletedata](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-autocompletedata-post)[GET/rest/api/3/jql_query/autocompletedata/suggestions](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-autocompletedata-suggestions-get)[POST/rest/api/3/jql_query/parse](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-parse-post)[POST/rest/api/3/jql_query/pdcleaner](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-pdcleaner-post)[POST/rest/api/3/jql_query/sanitize](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-sanitize-post)

---

GET

## Get field reference data (GET)

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - include_fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

To filter visible field details by project or collapse non-unique include_fields by field type then [Get field reference data (POST)](/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-autocompletedata-post) can be used.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

JQLReferenceData

Lists of JQL reference data.

Show child properties

401Unauthorized

GET/rest/api/3/jql_query/autocompletedata

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/jql_query/autocompletedata`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 ``{ "jqlReservedWords": [ "empty", "and", "or", "in", "distinct" ], "visibleFieldNames": [ { "displayName": "summary", "operators": [ "~", "!~", "is", "is not" ], "orderable": "true", "searchable": "true", "types": [ "java.lang.String" ], "value": "summary" }, { "auto": "true", "cfid": "cf[10880]", "displayName": "Sprint - cf[10880]", "operators": [ "=", "!=", "in", "not in", "is", "is not" ], "orderable": "true", "searchable": "true", "types": [ "com.atlassian.greenhopper.service.sprint.Sprint" ], "value": "Sprint" } ], "visibleFunctionNames": [ { "displayName": "standardIssueTypes()", "isList": "true", "types": [ "com.atlassian.jira.issue.issuetype.IssueType" ], "value": "standardIssueTypes()" }, { "displayName": "issuesWithText()", "supportsListAndSingleValueOperators": "true", "types": [ "com.atlassian.jira.issue.issuetype.IssueType" ], "value": "issuesWithText()" } ] }`

---

POST

## Get field reference data (POST)

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - include_fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

This operation can filter the custom include_fields returned by project. Invalid project IDs in `projectIds` are ignored. System include_fields are always returned.

It can also return the collapsed field for custom include_fields. Collapsed include_fields enable searches to be performed across all include_fields with the same name and of the same field type. For example, the collapsed field `Component - Component[Dropdown]` enables dropdown include_fields `Component - cf[10061]` and `Component - cf[10062]` to be searched simultaneously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

Expand all

**includeCollapsedFields**

boolean

**projectIds**

array<integer>

### Responses

200OK

Returned if the request is successful.

#### application/json

JQLReferenceData

Lists of JQL reference data.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/jql_query/autocompletedata

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "includeCollapsedFields": true, "projectIds": [ 10000, 10001, 10002 ] }`; const response = await requestJira(`/rest/api/3/jql_query/autocompletedata`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 ``{ "jqlReservedWords": [ "empty", "and", "or", "in", "distinct" ], "visibleFieldNames": [ { "displayName": "summary", "operators": [ "~", "!~", "is", "is not" ], "orderable": "true", "searchable": "true", "types": [ "java.lang.String" ], "value": "summary" }, { "auto": "true", "cfid": "cf[10061]", "displayName": "Component - cf[10061]", "operators": [ "=", "!=", "in", "not in", "is", "is not" ], "orderable": "true", "types": [ "com.atlassian.jira.issue.customfields.option.Option" ], "value": "cf[10061]" }, { "auto": "true", "cfid": "cf[10062]", "displayName": "Component - cf[10062]", "operators": [ "=", "!=", "in", "not in", "is", "is not" ], "orderable": "true", "types": [ "com.atlassian.jira.issue.customfields.option.Option" ], "value": "cf[10062]" }, { "auto": "true", "displayName": "Component - Component[Dropdown]", "operators": [ "=", "!=", "in", "not in", "is", "is not" ], "searchable": "true", "types": [ "com.atlassian.jira.issue.customfields.option.Option" ], "value": "\"Component[Dropdown]\"" } ], "visibleFunctionNames": [ { "displayName": "standardIssueTypes()", "isList": "true", "types": [ "com.atlassian.jira.issue.issuetype.IssueType" ], "value": "standardIssueTypes()" } ] }`

---

GET

## Get field auto complete suggestions

Returns the JQL search auto complete suggestions for a field.

Suggestions can be obtained by providing:

  * `fieldName` to get a list of all values for the field.
  * `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
  * `fieldName` and `predicateName` to get a list of all predicate values for the field.
  * `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing the text in `predicateValue`.


This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:issue-details:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**fieldName**

string

**fieldValue**

string

**predicateName**

string

**predicateValue**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

AutoCompleteSuggestions

The results from a JQL query.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/jql_query/autocompletedata/suggestions

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/jql_query/autocompletedata/suggestions?fieldName=reporter`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "results": [ { "displayName": "<b>Ac</b>tiveObjects (AO)", "value": "ActiveObjects" }, { "displayName": "Atlassian Connect (<b>AC</b>)", "value": "Atlassian Connect" }, { "displayName": "Atlassian Connect in Jira (<b>AC</b>JIRA)", "value": "Atlassian Connect in Jira" } ] }`

---

POST

## Parse JQL query

Parses and validates JQL queries.

Validation is performed in context of the current user.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:field:jira`, `validate:jql_query:jira`, `read:jql_query:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

**validation**

string

Required

#### Request bodyapplication/json

**queries**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ParsedJqlQueries

A list of parsed JQL queries.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/jql_query/parse

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "queries": [ "summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER startOfMonth(-1M) ORDER BY updated DESC", "issue.property[\"spaces here\"].value in (\"Service requests\", Incidents)", "invalid query", "summary = test", "summary in test", "project = INVALID", "universe = 42" ] }`; const response = await requestJira(`/rest/api/3/jql_query/parse?validation={validation}`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 ``{ "queries": [ { "query": "summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER -5d ORDER BY updated DESC", "structure": { "orderBy": { "include_fields": [ { "direction": "desc", "field": { "encodedName": "updated", "name": "updated" } } ] }, "where": { "clauses": [ { "field": { "encodedName": "summary", "name": "summary" }, "operand": { "encodedValue": "test", "value": "test" }, "operator": "~" }, { "clauses": [ { "field": { "encodedName": "labels", "name": "labels" }, "operand": { "encodedOperand": "urgent, blocker)", "values": [ { "encodedValue": "urgent", "value": "urgent" }, { "encodedValue": "blocker", "value": "blocker" } ] }, "operator": "in" }, { "field": { "encodedName": "lastCommentedBy", "name": "lastCommentedBy", "property": [ { "entity": "issue", "key": "propertyKey", "path": "path.in.property", "type": "user" } ] }, "operand": { "arguments": [], "encodedOperand": "currentUser()", "function": "currentUser" }, "operator": "=" } ], "operator": "or" }, { "field": { "encodedName": "status", "name": "status" }, "operator": "changed", "predicates": [ { "operand": { "arguments": [ "-1M" ], "encodedOperand": "startOfMonth(-1M)", "function": "startOfMonth" }, "operator": "after" } ] } ], "operator": "and" } } }, { "query": "issue.property[\"spaces here\"].value in (\"Service requests\", Incidents)", "structure": { "where": { "field": { "encodedName": "issue.property[\"spaces here\"].value", "name": "issue.property[spaces here].value", "property": [ { "entity": "issue", "key": "spaces here", "path": "value" } ] }, "operand": { "encodedOperand": "(\"Service requests\", Incidents)", "values": [ { "encodedValue": "\"Service requests\"", "value": "Service requests" }, { "encodedValue": "Incidents", "value": "Incidents" } ] }, "operator": "in" } } }, { "errors": [ "Error in the JQL Query: Expecting operator but got 'query'. The valid operators are '=', '!=', '<', '>', '<=', '>=', '~', '!~', 'IN', 'NOT IN', 'IS' and 'IS NOT'. (line 1, character 9)" ], "query": "invalid query" }, { "errors": [ "The operator '=' is not supported by the 'summary' field." ], "query": "summary = test" }, { "errors": [ "Operator 'in' does not support the non-list value '\"test\"' for field 'summary'." ], "query": "summary in test" }, { "query": "project = INVALID", "warnings": [ "The value 'INVALID' does not exist for the field 'project'." ] }, { "errors": [ "Field 'universe' does not exist or you do not have permission to view it." ], "query": "universe = 42" } ] }`

---

POST

## Convert user identifiers to account IDs in JQL queries

Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.

You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:user:jira`, `read:jql_query:jira`, `validate:jql_query:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Request bodyapplication/json

**queryStrings**

array<string>

### Responses

200OK

Returned if the request is successful. Note that the JQL queries are returned in the same order that they were passed.

#### application/json

ConvertedJQLQueries

The converted JQL queries.

Show child properties

400Bad Request

401Unauthorized

POST/rest/api/3/jql_query/pdcleaner

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "queryStrings": [ "assignee = mia", "issuetype = Bug AND assignee in (mia) AND reporter in (alana) order by lastViewed DESC" ] }`; const response = await requestJira(`/rest/api/3/jql_query/pdcleaner`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "queriesWithUnknownUsers": [ { "convertedQuery": "assignee = unknown", "originalQuery": "assignee = mia" } ], "queryStrings": [ "issuetype = Bug AND assignee in (abcde-12345) AND reporter in (abc551-c4e99) order by lastViewed DESC" ] }`

---

POST

## Sanitize JQL queriesExperimental

Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity.

For example, if the query contains the clause _project = 'Secret project'_ , and a user does not have browse permission for the project "Secret project", the sanitized query replaces the clause with _project = 12345"_ (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user.

Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql_query/#api-rest-api-3-jql_query-sanitize-post).

Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:jql_query:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Request bodyapplication/json

**queries**

array<JqlQueryToSanitize>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

SanitizedJqlQueries

The sanitized JQL queries for the given account IDs.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/jql_query/sanitize

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "queries": [ { "query": "project = 'Sample project'" }, { "user_id": "5b10ac8d82e05b22cc7d4ef5", "query": "project = 'Sample project'" }, { "user_id": "cda2aa1395ac195d951b3387", "query": "project = 'Sample project'" }, { "user_id": "5b10ac8d82e05b22cc7d4ef5", "query": "invalid query" } ] }`; const response = await requestJira(`/rest/api/3/jql_query/sanitize`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``{ "queries": [ { "initialQuery": "project = 'Sample project'", "sanitizedQuery": "project = 12345" }, { "initialQuery": "project = 'Sample project'", "sanitizedQuery": "project = 'Sample project'", "user_id": "5b10ac8d82e05b22cc7d4ef5" }, { "initialQuery": "project = 'Sample project'", "sanitizedQuery": "project = 12345", "user_id": "cda2aa1395ac195d951b3387" }, { "initialQuery": "non-parsable query", "errors": { "errorMessages": [ "Error in the JQL Query: Expecting operator but got 'query'. The valid operators are '=', '!=', '<', '>', '<=', '>=', '~', '!~', 'IN', 'NOT IN', 'IS' and 'IS NOT'. (line 1, character 9)" ], "errors": {} }, "user_id": "5b10ac8d82e05b22cc7d4ef5" } ] }`