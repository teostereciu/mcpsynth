# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-project-types/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Project types

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents project types. Use it to obtain a list of all project types, a list of project types accessible to the calling user, and details of a project type.

Operations

[GET/rest/api/3/project/type](/cloud/jira/platform/rest/v3/api-group-project-types/#api-rest-api-3-project-type-get)[GET/rest/api/3/project/type/accessible](/cloud/jira/platform/rest/v3/api-group-project-types/#api-rest-api-3-project-type-accessible-get)[GET/rest/api/3/project/type/{projectTypeKey}](/cloud/jira/platform/rest/v3/api-group-project-types/#api-rest-api-3-project-type-projecttypekey-get)[GET/rest/api/3/project/type/{projectTypeKey}/accessible](/cloud/jira/platform/rest/v3/api-group-project-types/#api-rest-api-3-project-type-projecttypekey-accessible-get)

---

GET

## Get all project types

Returns all [project types](https://confluence.atlassian.com/x/Var1Nw), whether or not the instance has a valid license for each type.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ProjectType>

Show child properties

401Unauthorized

GET/rest/api/3/project/type

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/type`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``[ { "color": "#FFFFFF", "descriptionI18nKey": "jira.project.type.business.description", "formattedKey": "Business", "icon": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOC4xLjEsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHZpZXdCb3g9IjAgMCAzMiAzMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggZmlsbD0iIzY2NjY2NiIgZD0iTTE2LDBDNy4yLDAsMCw3LjIsMCwxNmMwLDguOCw3LjIsMTYsMTYsMTZjOC44LDAsMTYtNy4yLDE2LTE2QzMyLDcuMiwyNC44LDAsMTYsMHogTTI1LjcsMjMNCgkJYzAsMS44LTEuNCwzLjItMy4yLDMuMkg5LjJDNy41LDI2LjIsNiwyNC44LDYsMjNWOS44QzYsOCw3LjUsNi42LDkuMiw2LjZoMTMuMmMwLjIsMCwwLjQsMCwwLjcsMC4xbC0yLjgsMi44SDkuMg0KCQlDOSw5LjQsOC44LDkuNiw4LjgsOS44VjIzYzAsMC4yLDAuMiwwLjQsMC40LDAuNGgxMy4yYzAuMiwwLDAuNC0wLjIsMC40LTAuNHYtNS4zbDIuOC0yLjhWMjN6IE0xNS45LDIxLjNMMTEsMTYuNGwyLTJsMi45LDIuOQ0KCQlMMjYuNCw2LjhjMC42LDAuNywxLjIsMS41LDEuNywyLjNMMTUuOSwyMS4zeiIvPg0KPC9nPg0KPC9zdmc+", "key": "business" }, { "color": "#AAAAAA", "descriptionI18nKey": "jira.project.type.software.description", "formattedKey": "Software", "icon": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOC4xLjEsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHZpZXdCb3g9IjAgMCAzMiAzMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggZmlsbD0iIzY2NjY2NiIgZD0iTTE2LDBDNy4yLDAsMCw3LjIsMCwxNmMwLDguOCw3LjIsMTYsMTYsMTZjOC44LDAsMTYtNy4yLDE2LTE2QzMyLDcuMiwyNC44LDAsMTYsMHogTTI1LjcsMjMNCgkJYzAsMS44LTEuNCwzLjItMy4yLDMuMkg5LjJDNy41LDI2LjIsNiwyNC44LDYsMjNWOS44QzYsOCw3LjUsNi42LDkuMiw2LjZoMTMuMmMwLjIsMCwwLjQsMCwwLjcsMC4xbC0yLjgsMi44SDkuMg0KCQlDOSw5LjQsOC44LDkuNiw4LjgsOS44VjIzYzAsMC4yLDAuMiwwLjQsMC40LDAuNGgxMy4yYzAuMiwwLDAuNC0wLjIsMC40LTAuNHYtNS4zbDIuOC0yLjhWMjN6IE0xNS45LDIxLjNMMTEsMTYuNGwyLTJsMi45LDIuOQ0KCQlMMjYuNCw2LjhjMC42LDAuNywxLjIsMS41LDEuNywyLjNMMTUuOSwyMS4zeiIvPg0KPC9nPg0KPC9zdmc+", "key": "software" } ]`

---

GET

## Get licensed project types

Returns all [project types](https://confluence.atlassian.com/x/Var1Nw) with a valid license.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ProjectType>

Show child properties

GET/rest/api/3/project/type/accessible

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/type/accessible`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``[ { "color": "#FFFFFF", "descriptionI18nKey": "jira.project.type.business.description", "formattedKey": "Business", "icon": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOC4xLjEsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHZpZXdCb3g9IjAgMCAzMiAzMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggZmlsbD0iIzY2NjY2NiIgZD0iTTE2LDBDNy4yLDAsMCw3LjIsMCwxNmMwLDguOCw3LjIsMTYsMTYsMTZjOC44LDAsMTYtNy4yLDE2LTE2QzMyLDcuMiwyNC44LDAsMTYsMHogTTI1LjcsMjMNCgkJYzAsMS44LTEuNCwzLjItMy4yLDMuMkg5LjJDNy41LDI2LjIsNiwyNC44LDYsMjNWOS44QzYsOCw3LjUsNi42LDkuMiw2LjZoMTMuMmMwLjIsMCwwLjQsMCwwLjcsMC4xbC0yLjgsMi44SDkuMg0KCQlDOSw5LjQsOC44LDkuNiw4LjgsOS44VjIzYzAsMC4yLDAuMiwwLjQsMC40LDAuNGgxMy4yYzAuMiwwLDAuNC0wLjIsMC40LTAuNHYtNS4zbDIuOC0yLjhWMjN6IE0xNS45LDIxLjNMMTEsMTYuNGwyLTJsMi45LDIuOQ0KCQlMMjYuNCw2LjhjMC42LDAuNywxLjIsMS41LDEuNywyLjNMMTUuOSwyMS4zeiIvPg0KPC9nPg0KPC9zdmc+", "key": "business" }, { "color": "#AAAAAA", "descriptionI18nKey": "jira.project.type.software.description", "formattedKey": "Software", "icon": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOC4xLjEsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHZpZXdCb3g9IjAgMCAzMiAzMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggZmlsbD0iIzY2NjY2NiIgZD0iTTE2LDBDNy4yLDAsMCw3LjIsMCwxNmMwLDguOCw3LjIsMTYsMTYsMTZjOC44LDAsMTYtNy4yLDE2LTE2QzMyLDcuMiwyNC44LDAsMTYsMHogTTI1LjcsMjMNCgkJYzAsMS44LTEuNCwzLjItMy4yLDMuMkg5LjJDNy41LDI2LjIsNiwyNC44LDYsMjNWOS44QzYsOCw3LjUsNi42LDkuMiw2LjZoMTMuMmMwLjIsMCwwLjQsMCwwLjcsMC4xbC0yLjgsMi44SDkuMg0KCQlDOSw5LjQsOC44LDkuNiw4LjgsOS44VjIzYzAsMC4yLDAuMiwwLjQsMC40LDAuNGgxMy4yYzAuMiwwLDAuNC0wLjIsMC40LTAuNHYtNS4zbDIuOC0yLjhWMjN6IE0xNS45LDIxLjNMMTEsMTYuNGwyLTJsMi45LDIuOQ0KCQlMMjYuNCw2LjhjMC42LDAuNywxLjIsMS41LDEuNywyLjNMMTUuOSwyMS4zeiIvPg0KPC9nPg0KPC9zdmc+", "key": "software" } ]`

---

GET

## Get project type by key

Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectTypeKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectType

Details about a project type.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/type/{projectTypeKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/type/{projectTypeKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "color": "#FFFFFF", "descriptionI18nKey": "jira.project.type.business.description", "formattedKey": "Business", "icon": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOC4xLjEsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHZpZXdCb3g9IjAgMCAzMiAzMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggZmlsbD0iIzY2NjY2NiIgZD0iTTE2LDBDNy4yLDAsMCw3LjIsMCwxNmMwLDguOCw3LjIsMTYsMTYsMTZjOC44LDAsMTYtNy4yLDE2LTE2QzMyLDcuMiwyNC44LDAsMTYsMHogTTI1LjcsMjMNCgkJYzAsMS44LTEuNCwzLjItMy4yLDMuMkg5LjJDNy41LDI2LjIsNiwyNC44LDYsMjNWOS44QzYsOCw3LjUsNi42LDkuMiw2LjZoMTMuMmMwLjIsMCwwLjQsMCwwLjcsMC4xbC0yLjgsMi44SDkuMg0KCQlDOSw5LjQsOC44LDkuNiw4LjgsOS44VjIzYzAsMC4yLDAuMiwwLjQsMC40LDAuNGgxMy4yYzAuMiwwLDAuNC0wLjIsMC40LTAuNHYtNS4zbDIuOC0yLjhWMjN6IE0xNS45LDIxLjNMMTEsMTYuNGwyLTJsMi45LDIuOQ0KCQlMMjYuNCw2LjhjMC42LDAuNywxLjIsMS41LDEuNywyLjNMMTUuOSwyMS4zeiIvPg0KPC9nPg0KPC9zdmc+", "key": "business" }`

---

GET

## Get accessible project type by key

Returns a [project type](https://confluence.atlassian.com/x/Var1Nw) if it is accessible to the user.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:project-type:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**projectTypeKey**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

ProjectType

Details about a project type.

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/project/type/{projectTypeKey}/accessible

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/project/type/{projectTypeKey}/accessible`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``{ "color": "#FFFFFF", "descriptionI18nKey": "jira.project.type.business.description", "formattedKey": "Business", "icon": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOC4xLjEsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHZpZXdCb3g9IjAgMCAzMiAzMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggZmlsbD0iIzY2NjY2NiIgZD0iTTE2LDBDNy4yLDAsMCw3LjIsMCwxNmMwLDguOCw3LjIsMTYsMTYsMTZjOC44LDAsMTYtNy4yLDE2LTE2QzMyLDcuMiwyNC44LDAsMTYsMHogTTI1LjcsMjMNCgkJYzAsMS44LTEuNCwzLjItMy4yLDMuMkg5LjJDNy41LDI2LjIsNiwyNC44LDYsMjNWOS44QzYsOCw3LjUsNi42LDkuMiw2LjZoMTMuMmMwLjIsMCwwLjQsMCwwLjcsMC4xbC0yLjgsMi44SDkuMg0KCQlDOSw5LjQsOC44LDkuNiw4LjgsOS44VjIzYzAsMC4yLDAuMiwwLjQsMC40LDAuNGgxMy4yYzAuMiwwLDAuNC0wLjIsMC40LTAuNHYtNS4zbDIuOC0yLjhWMjN6IE0xNS45LDIxLjNMMTEsMTYuNGwyLTJsMi45LDIuOQ0KCQlMMjYuNCw2LjhjMC42LDAuNywxLjIsMS41LDEuNywyLjNMMTUuOSwyMS4zeiIvPg0KPC9nPg0KPC9zdmc+", "key": "business" }`