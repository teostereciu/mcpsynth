# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-users/*

---

Cloud

Confluence Cloud / Reference / REST API

# Users

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/user](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-get)[GET/wiki/rest/api/user/anonymous](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-anonymous-get)[GET/wiki/rest/api/user/current](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-current-get)[GET/wiki/rest/api/user/memberof](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-memberof-get)[GET/wiki/rest/api/user/bulk](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-bulk-get)[GET/wiki/rest/api/user/email](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-email-get)[GET/wiki/rest/api/user/email/bulk](/cloud/confluence/rest/v1/api-group-users/#api-wiki-rest-api-user-email-bulk-get)

---

GET

## Get user

Returns a user. This includes information about the user, such as the display name, account ID, profile picture, and more. The information returned may be restricted by the user's profile visibility settings.

**Note:** to add, edit, or delete users in your organization, see the [user management REST API](/cloud/admin/user-management/about/).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-user`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**accountId**

string

Required

**expand**

array<string>

### Responses

200OK

Returned if the requested user is returned.

#### application/json

User

Nullable: `true`

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user?accountId={accountId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 ``{ "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": { "business": { "position": "<string>", "department": "<string>", "location": "<string>" }, "personal": { "phone": "<string>", "im": "<string>", "website": "<string>", "email": "<string>" } }, "personalSpace": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "homepage": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "_expandable": {}, "_links": {} }, "update": { "operation": "administer", "_expandable": {}, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "id": 2154, "subjects": { "user": { "results": [], "size": 2154, "start": 2154, "limit": 2154 }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "size": 2154, "start": 2154, "limit": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "status": "<string>", "settings": { "routeOverrideEnabled": true, "editor": { "page": "<string>", "blogpost": "<string>", "default": "<string>" }, "spaceKey": "<string>", "_links": {} }, "theme": { "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "_links": {} }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "primaryNavigation": { "highlightColor": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {} }, "history": { "createdDate": "<string>" }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} }`

---

GET

## Get anonymous user

Returns information about how anonymous users are represented, like the profile picture and display name.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-user`

**Granular** :`read:user:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

array<string>

### Responses

200OK

Returned if the anonymous user representation is returned.

#### application/json

UserAnonymous

Show child properties

403Forbidden

GET/wiki/rest/api/user/anonymous

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/anonymous`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``{ "type": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "operations": [ { "operation": "administer", "targetType": "<string>" } ], "_expandable": { "operations": "<string>" }, "_links": {} }`

---

GET

## Get current user

Returns the currently logged-in user. This includes information about the user, like the display name, userKey, account ID, profile picture, and more.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-user`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

**expand**

array<string>

### Responses

200OK

Returned if the current user is returned.

#### application/json

User

Nullable: `true`

Show child properties

403Forbidden

GET/wiki/rest/api/user/current

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/current`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 ``{ "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": { "business": { "position": "<string>", "department": "<string>", "location": "<string>" }, "personal": { "phone": "<string>", "im": "<string>", "website": "<string>", "email": "<string>" } }, "personalSpace": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "homepage": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "_expandable": {}, "_links": {} }, "update": { "operation": "administer", "_expandable": {}, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "id": 2154, "subjects": { "user": { "results": [], "size": 2154, "start": 2154, "limit": 2154 }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "size": 2154, "start": 2154, "limit": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "status": "<string>", "settings": { "routeOverrideEnabled": true, "editor": { "page": "<string>", "blogpost": "<string>", "default": "<string>" }, "spaceKey": "<string>", "_links": {} }, "theme": { "themeKey": "<string>", "name": "<string>", "description": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "_links": {} }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "primaryNavigation": { "highlightColor": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {} }, "history": { "createdDate": "<string>" }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} }`

---

GET

## Get group memberships for user

Returns the groups that a user is a member of.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-user`

**Granular** :`read:user:confluence`, `read:group:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**accountId**

string

Required

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested groups are returned.

#### application/json

GroupArrayWithLinks

Same as GroupArray but with `_links` property.

Show child properties

403Forbidden

GET/wiki/rest/api/user/memberof

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/memberof?accountId={accountId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "results": [ { "type": "group", "name": "<string>", "id": "<string>", "usageType": "USERBASE_GROUP", "managedBy": "ADMINS", "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "totalSize": 150, "_links": {} }`

---

GET

## Get multiple users using ids

Returns user details for the ids provided in the request. Currently this API returns a maximum of 100 results. If more than 100 account ids are passed in, then the first 100 will be returned.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-user`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**accountId**

string

Required

**expand**

array<string>

### Responses

200OK

Returned if, the list of users is returned.

#### application/json

BulkUserLookupArray

Show child properties

403Forbidden

GET/wiki/rest/api/user/bulk

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/user/bulk?accountId={accountId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 ``{ "results": [ { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "<string>", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": { "business": { "position": "<string>", "department": "<string>", "location": "<string>" }, "personal": { "phone": "<string>", "im": "<string>", "website": "<string>", "email": "<string>" } }, "personalSpace": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "homepage": { "type": "<string>", "status": "<string>" }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "size": 2154 }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "status": "<string>", "settings": { "routeOverrideEnabled": true, "_links": {} }, "theme": { "themeKey": "<string>" }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" } }, "history": { "createdDate": "<string>", "createdBy": { "type": "known" } }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`

---

GET

## Get user email address

Returns a user's email address regardless of the userâs profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:email-address:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `ACCESS_EMAIL_ADDRESSES`

### Request

#### Query parameters

**accountId**

string

Required

### Responses

200OK

Returned if the requested user's email is returned.

#### application/json

AccountIdEmailRecord

Show child properties

400Bad Request

401Unauthorized

404Not Found

501Not Implemented

GET/wiki/rest/api/user/email

curl

Node.js

Java

Python

PHP

`1 2 3 ``curl --request GET \ --url 'https://your-domain.atlassian.net/wiki/rest/api/user/email?accountId={accountId}' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 ``{ "accountId": "<string>", "email": "<string>" }`

---

GET

## Get user email addresses in batch

Returns a user's email address regardless of the userâs profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.

Any accounts which are not available will not be included in the result.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:email-address:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `ACCESS_EMAIL_ADDRESSES`

### Request

#### Query parameters

**accountId**

array<string>

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

array<AccountIdEmailRecord>

Show child properties

400Bad Request

401Unauthorized

501Not Implemented

GET/wiki/rest/api/user/email/bulk

curl

Node.js

Java

Python

PHP

`1 2 3 ``curl --request GET \ --url 'https://your-domain.atlassian.net/wiki/rest/api/user/email/bulk?accountId={accountId}' \ --header 'Accept: application/json'`

200Response

`1 2 3 4 5 6 ``[ { "accountId": "<string>", "email": "<string>" } ]`