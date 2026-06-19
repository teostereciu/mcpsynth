# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jira-settings/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Jira settings

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents various settings in Jira. Use it to get and update Jira settings and properties.

Operations

[GET/rest/api/3/application-properties](/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-rest-api-3-application-properties-get)[GET/rest/api/3/application-properties/advanced-settings](/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-rest-api-3-application-properties-advanced-settings-get)[PUT/rest/api/3/application-properties/{id}](/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-rest-api-3-application-properties-id-put)[GET/rest/api/3/configuration](/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-rest-api-3-configuration-get)

---

GET

## Get application property

Returns all application properties or an application property.

If you specify a value for the `key` parameter, then an application property is returned as an object (not in an array). Otherwise, an array of all editable application properties is returned. See [Set application property](/cloud/jira/platform/rest/v3/api-group-jira-settings/#api-rest-api-3-application-properties-id-put) for descriptions of editable properties.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:instance-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**key**

string

**permissionLevel**

string

**keyFilter**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ApplicationProperty>

Show child properties

401Unauthorized

404Not Found

GET/rest/api/3/application-properties

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/application-properties`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``[ { "defaultValue": "", "desc": "Jira home directory", "id": "jira.home", "key": "jira.home", "name": "jira.home", "type": "string", "value": "/var/jira/jira-home" }, { "defaultValue": "CLONE -", "id": "jira.clone.prefix", "key": "jira.clone.prefix", "name": "The prefix added to the Summary field of cloned issues", "type": "string", "value": "CLONE -" } ]`

---

GET

## Get advanced settings

Returns the application properties that are accessible on the _Advanced Settings_ page. To navigate to the _Advanced Settings_ page in Jira, choose the Jira icon > **Jira settings** > **System** , **General Configuration** and then click **Advanced Settings** (in the upper right).

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:instance-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

array<ApplicationProperty>

Show child properties

401Unauthorized

403Forbidden

GET/rest/api/3/application-properties/advanced-settings

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/application-properties/advanced-settings`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``[ { "defaultValue": "", "desc": "Jira home directory", "id": "jira.home", "key": "jira.home", "name": "jira.home", "type": "string", "value": "/var/jira/jira-home" }, { "defaultValue": "CLONE -", "id": "jira.clone.prefix", "key": "jira.clone.prefix", "name": "The prefix added to the Summary field of cloned issues", "type": "string", "value": "CLONE -" } ]`

---

PUT

## Set application property

Changes the value of an application property. For example, you can change the value of the `jira.clone.prefix` from its default value of _CLONE -_ to _Clone -_ if you prefer sentence case capitalization. Editable properties are described below along with their default values.

#### Advanced settings

The advanced settings below are also accessible in [Jira](https://confluence.atlassian.com/x/vYXKM).

Key| Description| Default value
---|---|---
`jira.clone.prefix`| The string of text prefixed to the title of a cloned issue.| `CLONE -`
`jira.date.picker.java.format`| The date format for the Java (server-side) generated dates. This must be the same as the `jira.date.picker.javascript.format` format setting.| `d/MMM/yy`
`jira.date.picker.javascript.format`| The date format for the JavaScript (client-side) generated dates. This must be the same as the `jira.date.picker.java.format` format setting.| `%e/%b/%y`
`jira.date.time.picker.java.format`| The date format for the Java (server-side) generated date times. This must be the same as the `jira.date.time.picker.javascript.format` format setting.| `dd/MMM/yy h:mm a`
`jira.date.time.picker.javascript.format`| The date format for the JavaScript (client-side) generated date times. This must be the same as the `jira.date.time.picker.java.format` format setting.| `%e/%b/%y %I:%M %p`
`jira.issue.actions.order`| The default order of actions (such as _Comments_ or _Change history_) displayed on the issue view.| `asc`
`jira.view.issue.links.sort.order`| The sort order of the list of issue links on the issue view.| `type, status, priority`
`jira.comment.collapsing.minimum.hidden`| The minimum number of comments required for comment collapsing to occur. A value of `0` disables comment collapsing.| `4`
`jira.newsletter.tip.delay.days`| The number of days before a prompt to sign up to the Jira Insiders newsletter is shown. A value of `-1` disables this feature.| `7`

#### Look and feel

The settings listed below adjust the [look and feel](https://confluence.atlassian.com/x/VwCLLg).

Key| Description| Default value
---|---|---
`jira.lf.date.time`| The [ time format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html).| `h:mm a`
`jira.lf.date.day`| The [ day format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html).| `EEEE h:mm a`
`jira.lf.date.complete`| The [ date and time format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html).| `dd/MMM/yy h:mm a`
`jira.lf.date.dmy`| The [ date format](https://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html).| `dd/MMM/yy`
`jira.date.time.picker.use.iso8061`| When enabled, sets Monday as the first day of the week in the date picker, as specified by the ISO8601 standard.| `false`
`jira.lf.logo.url`| The URL of the logo image file.| `/images/icon-jira-logo.png`
`jira.lf.logo.show.application.title`| Controls the visibility of the application title on the sidebar.| `false`
`jira.lf.favicon.url`| The URL of the favicon.| `/favicon.ico`
`jira.lf.favicon.hires.url`| The URL of the high-resolution favicon.| `/images/64jira.png`
`jira.lf.navigation.bgcolour`| The background color of the sidebar.| `#0747A6`
`jira.lf.navigation.highlightcolour`| The color of the text and logo of the sidebar.| `#DEEBFF`
`jira.lf.hero.button.base.bg.colour`| The background color of the hero button.| `#3b7fc4`
`jira.title`| The text for the application title. The application title can also be set in _General settings_.| `Jira`
`jira.option.globalsharing`| Whether filters and dashboards can be shared with anyone signed into Jira.| `true`
`xflow.product.suggestions.enabled`| Whether to expose product suggestions for other Atlassian products within Jira.| `true`

#### Other settings

Key| Description| Default value
---|---|---
`jira.issuenav.criteria.autoupdate`| Whether instant updates to search criteria is active.| `true`

_Note: Be careful when changing[application properties and advanced settings](https://confluence.atlassian.com/x/vYXKM)._

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`write:instance-configuration:jira`, `read:instance-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**id**

string

**value**

string

### Responses

200OK

Returned if the request is successful.

#### application/json

ApplicationProperty

Details of an application property.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/application-properties/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "id": "jira.home", "value": "/var/jira/jira-home" }`; const response = await requestJira(`/rest/api/3/application-properties/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``{ "allowedValues": [ "<string>" ], "defaultValue": "<string>", "desc": "<string>", "example": "<string>", "id": "<string>", "key": "<string>", "name": "<string>", "type": "<string>", "value": "<string>" }`

---

GET

## Get global settings

Returns the [global settings](https://confluence.atlassian.com/x/qYXKM) in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-user`

**Granular** :`read:instance-configuration:jira`, `read:issue.time-tracking:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

Configuration

Details about the configuration of Jira.

Show child properties

401Unauthorized

GET/rest/api/3/configuration

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/configuration`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``{ "attachmentsEnabled": true, "issueLinkingEnabled": true, "subTasksEnabled": false, "timeTrackingConfiguration": { "defaultUnit": "day", "timeFormat": "pretty", "workingDaysPerWeek": 5, "workingHoursPerDay": 8 }, "timeTrackingEnabled": true, "unassignedIssuesAllowed": false, "votingEnabled": true, "watchingEnabled": true }`