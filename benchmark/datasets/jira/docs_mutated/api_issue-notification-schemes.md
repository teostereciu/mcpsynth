# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue notification schemes

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents notification schemes, lists of events and the recipients who will receive notifications for those events. Use it to get details of a notification scheme and a list of notification schemes.

### About notification schemes

A notification scheme is a list of events and recipients who will receive notifications for those events. The list is contained within the `notificationSchemeEvents` object and contains pairs of `events` and `notifications`:

  * `event` Identifies the type of event. The events can be [Jira system events](https://support.atlassian.com/jira-cloud-administration/docs/configure-notification-schemes/) (see the _Events_ section) or [custom events](https://support.atlassian.com/jira-cloud-administration/docs/add-a-custom-event/).

  * `notifications` Identifies the [recipients](https://confluence.atlassian.com/x/8YdKLg#Creatinganotificationscheme-recipientsRecipients) of notifications for each event. Recipients can be any of the following types:

    * `CurrentAssignee`
    * `Reporter`
    * `CurrentUser`
    * `ProjectLead`
    * `ComponentLead`
    * `User` (the `parameter` is the user key)
    * `Group` (the `parameter` is the group name)
    * `ProjectRole` (the `parameter` is the project role ID)
    * `EmailAddress` _(deprecated)_
    * `AllWatchers`
    * `UserCustomField` (the `parameter` is the ID of the custom field)
    * `GroupCustomField`(the `parameter` is the ID of the custom field)


Operations

[GET/rest/api/3/notificationscheme](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-get)[POST/rest/api/3/notificationscheme](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-post)[GET/rest/api/3/notificationscheme/project](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-project-get)[GET/rest/api/3/notificationscheme/{id}](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-id-get)[PUT/rest/api/3/notificationscheme/{id}](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-id-put)[PUT/rest/api/3/notificationscheme/{id}/notification](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-id-notification-put)[DEL/rest/api/3/notificationscheme/{notificationSchemeId}](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-notificationschemeid-delete)[DEL/rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}](/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-notificationschemeid-notification-notificationid-delete)

---

GET

## Get notification schemes paginated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) list of [notification schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

_Note that you should allow for events without recipients to appear in responses._

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with a notification scheme for it to be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`, `read:notification-scheme:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

string

**page_size**

string

**id**

array<string>

**projectId**

array<string>

**onlyDefault**

boolean

**expand**

string

### Responses

200OK

Returned if the request is successful. Only returns notification schemes that the user has permission to access. An empty list is returned if the user lacks permission to access all notification schemes.

#### application/json

PageBeanNotificationScheme

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/notificationscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/notificationscheme`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 ``{ "isLast": false, "page_size": 6, "start_index": 1, "total": 5, "values": [ { "description": "description", "expand": "notificationSchemeEvents,user,group,projectRole,field,all", "id": 10100, "name": "notification scheme name", "notificationSchemeEvents": [ { "event": { "description": "Event published when an issue is created", "id": 1, "name": "Issue created" }, "notifications": [ { "expand": "group", "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 1, "notificationType": "Group", "parameter": "jira-administrators", "recipient": "276f955c-63d7-42c8-9520-92d01dca0625" }, { "id": 2, "notificationType": "CurrentAssignee" }, { "expand": "projectRole", "id": 3, "notificationType": "ProjectRole", "parameter": "10360", "projectRole": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "recipient": "10360" }, { "emailAddress": "rest-developer@atlassian.com", "id": 4, "notificationType": "EmailAddress", "parameter": "rest-developer@atlassian.com", "recipient": "rest-developer@atlassian.com" }, { "expand": "user", "id": 5, "notificationType": "User", "parameter": "5b10a2844c20165700ede21g", "recipient": "5b10a2844c20165700ede21g", "user": { "user_id": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" } }, { "expand": "field", "field": { "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }, "id": 6, "notificationType": "GroupCustomField", "parameter": "customfield_10101", "recipient": "customfield_10101" } ] }, { "event": { "description": "Custom event that is published together with an issue created event", "id": 20, "name": "Custom event", "templateEvent": { "description": "Event published when an issue is created", "id": 1, "name": "Issue created" } }, "notifications": [ { "expand": "group", "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 1, "notificationType": "Group", "parameter": "jira-administrators", "recipient": "276f955c-63d7-42c8-9520-92d01dca0625" }, { "id": 2, "notificationType": "CurrentAssignee" }, { "expand": "projectRole", "id": 3, "notificationType": "ProjectRole", "parameter": "10360", "projectRole": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "recipient": "10360" }, { "emailAddress": "rest-developer@atlassian.com", "id": 4, "notificationType": "EmailAddress", "parameter": "rest-developer@atlassian.com", "recipient": "rest-developer@atlassian.com" }, { "expand": "user", "id": 5, "notificationType": "User", "parameter": "5b10a2844c20165700ede21g", "recipient": "5b10a2844c20165700ede21g", "user": { "user_id": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" } }, { "expand": "field", "field": { "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }, "id": 6, "notificationType": "GroupCustomField", "parameter": "customfield_10101", "recipient": "customfield_10101" } ] } ], "projects": [ 10001, 10002 ], "self": "https://your-domain.atlassian.net/rest/api/3/notificationscheme" } ] }`

---

POST

## Create notification schemeExperimental

Creates a notification scheme with notifications. You can create up to 1000 notifications per request.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

Required

**notificationSchemeEvents**

array<NotificationSchemeEventDetails>

**Additional Properties**

any

### Responses

201Created

Returned if the request is successful.

#### application/json

NotificationSchemeId

The ID of a notification scheme.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

POST/rest/api/3/notificationscheme

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My new scheme description", "name": "My new notification scheme", "notificationSchemeEvents": [ { "event": { "id": "1" }, "notifications": [ { "notificationType": "Group", "parameter": "jira-administrators" } ] } ] }`; const response = await requestJira(`/rest/api/3/notificationscheme`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

201Response

`1 2 3 ``{ "id": "10001" }`

---

GET

## Get projects using notification schemes paginated

Returns a [paginated](/cloud/jira/platform/rest/v3/intro/#pagination) mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Note that only company-managed (classic) projects are supported. This is because team-managed projects don't have a concept of a default notification scheme. The mappings are ordered by projectId.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:notification-scheme:jira`, `read:project:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Query parameters

Expand all

**start_index**

string

**page_size**

string

**notificationSchemeId**

array<string>

**projectId**

array<string>

### Responses

200OK

Returned if the request is successful.

#### application/json

PageBeanNotificationSchemeAndProjectMappingJsonBean

A page of items.

Show child properties

400Bad Request

401Unauthorized

GET/rest/api/3/notificationscheme/project

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/notificationscheme/project`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "isLast": true, "page_size": 50, "start_index": 0, "total": 4, "values": [ { "notificationSchemeId": "10001", "projectId": "100001" } ] }`

---

GET

## Get notification scheme

Returns a [notification scheme](https://confluence.atlassian.com/x/8YdKLg), including the list of events and the recipients who will receive notifications for those events.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with the notification scheme.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:jira-configuration`

**Granular** :`read:field:jira`, `read:notification-scheme:jira`, `read:project:jira`, `read:project-role:jira`, `read:user:jira` ...(Show more)

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `ADMIN`

### Request

#### Path parameters

**id**

integer

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

GET/rest/api/3/notificationscheme/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/notificationscheme/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 ``{ "description": "description", "expand": "notificationSchemeEvents,user,group,projectRole,field,all", "id": 10100, "name": "notification scheme name", "notificationSchemeEvents": [ { "event": { "description": "Event published when an issue is created", "id": 1, "name": "Issue created" }, "notifications": [ { "expand": "group", "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 1, "notificationType": "Group", "parameter": "jira-administrators", "recipient": "276f955c-63d7-42c8-9520-92d01dca0625" }, { "id": 2, "notificationType": "CurrentAssignee" }, { "expand": "projectRole", "id": 3, "notificationType": "ProjectRole", "parameter": "10360", "projectRole": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "recipient": "10360" }, { "emailAddress": "rest-developer@atlassian.com", "id": 4, "notificationType": "EmailAddress", "parameter": "rest-developer@atlassian.com", "recipient": "rest-developer@atlassian.com" }, { "expand": "user", "id": 5, "notificationType": "User", "parameter": "5b10a2844c20165700ede21g", "recipient": "5b10a2844c20165700ede21g", "user": { "user_id": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" } }, { "expand": "field", "field": { "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }, "id": 6, "notificationType": "GroupCustomField", "parameter": "customfield_10101", "recipient": "customfield_10101" } ] }, { "event": { "description": "Custom event that is published together with an issue created event", "id": 20, "name": "Custom event", "templateEvent": { "description": "Event published when an issue is created", "id": 1, "name": "Issue created" } }, "notifications": [ { "expand": "group", "group": { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "name": "jira-administrators", "self": "https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625" }, "id": 1, "notificationType": "Group", "parameter": "jira-administrators", "recipient": "276f955c-63d7-42c8-9520-92d01dca0625" }, { "id": 2, "notificationType": "CurrentAssignee" }, { "expand": "projectRole", "id": 3, "notificationType": "ProjectRole", "parameter": "10360", "projectRole": { "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360", "name": "Developers", "id": 10360, "description": "A project role that represents developers in a project", "actors": [ { "actorGroup": { "name": "jira-developers", "displayName": "jira-developers", "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2" }, "displayName": "jira-developers", "id": 10240, "name": "jira-developers", "type": "atlassian-group-role-actor" }, { "actorUser": { "user_id": "5b10a2844c20165700ede21g" }, "displayName": "Mia Krystof", "id": 10241, "type": "atlassian-user-role-actor" } ], "scope": { "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" }, "type": "PROJECT" } }, "recipient": "10360" }, { "emailAddress": "rest-developer@atlassian.com", "id": 4, "notificationType": "EmailAddress", "parameter": "rest-developer@atlassian.com", "recipient": "rest-developer@atlassian.com" }, { "expand": "user", "id": 5, "notificationType": "User", "parameter": "5b10a2844c20165700ede21g", "recipient": "5b10a2844c20165700ede21g", "user": { "user_id": "5b10a2844c20165700ede21g", "active": false, "displayName": "Mia Krystof", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" } }, { "expand": "field", "field": { "clauseNames": [ "cf[10101]", "New custom field" ], "custom": true, "id": "customfield_10101", "key": "customfield_10101", "name": "New custom field", "navigable": true, "orderable": true, "schema": { "custom": "com.atlassian.jira.plugin.system.customfieldtypes:project", "customId": 10101, "type": "project" }, "searchable": true, "untranslatedName": "New custom field" }, "id": 6, "notificationType": "GroupCustomField", "parameter": "customfield_10101", "recipient": "customfield_10101" } ] } ], "projects": [ 10001, 10002 ], "self": "https://your-domain.atlassian.net/rest/api/3/notificationscheme" }`

---

PUT

## Update notification schemeExperimental

Updates a notification scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**description**

string

**name**

string

**Additional Properties**

any

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/notificationscheme/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "description": "My updated notification scheme description", "name": "My updated notification scheme" }`; const response = await requestJira(`/rest/api/3/notificationscheme/{id}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

PUT

## Add notifications to notification scheme

Adds notifications to a notification scheme. You can add up to 1000 notifications per request.

_Deprecated: The notification type`EmailAddress` is no longer supported in Cloud. Refer to the [changelog](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1031) for more details._

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**id**

string

Required

#### Request bodyapplication/json

Expand all

**notificationSchemeEvents**

array<NotificationSchemeEventDetails>

Required

**Additional Properties**

any

### Responses

204No Content

Returned if the request is successful.

#### application/json

any

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/rest/api/3/notificationscheme/{id}/notification

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; var bodyData = `{ "notificationSchemeEvents": [ { "event": { "id": "1" }, "notifications": [ { "notificationType": "Group", "parameter": "jira-administrators" } ] } ] }`; const response = await requestJira(`/rest/api/3/notificationscheme/{id}/notification`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Delete notification schemeExperimental

Deletes a notification scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

**notificationSchemeId**

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

DEL/rest/api/3/notificationscheme/{notificationSchemeId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/notificationscheme/{notificationSchemeId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

DEL

## Remove notification from notification scheme

Removes a notification from a notification scheme.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Administer Jira_ [global permission](https://confluence.atlassian.com/x/x4dKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`manage:jira-configuration`

Connect apps cannot access this REST resource.

### Request

#### Path parameters

Expand all

**notificationSchemeId**

string

Required

**notificationId**

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

DEL/rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`