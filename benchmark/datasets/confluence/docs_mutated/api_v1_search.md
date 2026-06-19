# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/*

---

Cloud

Confluence Cloud / Reference / REST API

# Search

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/search](/cloud/confluence/rest/v1/api-group-search/#api-wiki-rest-api-search-get)[GET/wiki/rest/api/search/user](/cloud/confluence/rest/v1/api-group-search/#api-wiki-rest-api-search-user-get)

---

GET

## Search content

Searches for content using the [Confluence Query Language (CQL)](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-query/).

**Note that CQL input queries submitted through the`/wiki/rest/api/search` endpoint no longer support user-specific fields like `user`, `user.fullname`, `user.accountid`, and `user.userkey`.** See this [deprecation notice](https://developer.atlassian.com/cloud/confluence/deprecation-notice-search-api/) for more details.

Example initial call:


    1
    /wiki/rest/api/search?query=type=page&max_results=25


Example response:


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    {
      "results": [
        { ... },
        { ... },
        ...
        { ... }
      ],
      "max_results": 25,
      "size": 25,
      ...
      "_links": {
        "base": "<url>",
        "context": "<url>",
        "next": "/rest/api/search?query=type=page&max_results=25&cursor=raNDoMsTRiNg",
        "self": "<url>"
      }
    }


When additional results are available, returns `next` and `prev` URLs to retrieve them in subsequent calls. The URLs each contain a cursor that points to the appropriate set of results. Use `max_results` to specify the number of results returned in each call.

Example subsequent call (taken from example response):


    1
    /wiki/rest/api/search?query=type=page&max_results=25&cursor=raNDoMsTRiNg


The response to this will have a `prev` URL similar to the `next` in the example response.

If the include query parameter is used with the `body.export_view` and/or `body.styled_view` properties, then the query max_results parameter will be restricted to a maximum value of 25.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the entities. Note, only entities that the user has permission to view will be returned.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`search:confluence`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**cqlcontext**

string

**cursor**

string

**next**

boolean

**prev**

boolean

**max_results**

integer

**offset**

integer

**includeArchivedSpaces**

boolean

**excludeCurrentSpaces**

boolean

**excerpt**

string

Show 3 hidden parameters

### Responses

200OK

Returned if the requested results are returned.

#### application/json

SearchPageResponseSearchResult

Show child properties

400Bad Request

403Forbidden

GET/wiki/rest/api/search

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/search?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 ``{ "results": [ { "content": { "id": "<string>", "type": "<string>", "content_status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "content_status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "_expandable": {}, "_links": {} }, "update": { "operation": "administer", "_expandable": {}, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "user": { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": {}, "personalSpace": { "key": "<string>", "name": "<string>", "type": "<string>", "content_status": "<string>", "_expandable": {}, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} }, "space": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "homepage": { "type": "<string>", "content_status": "<string>" }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "size": 2154 }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "content_status": "<string>", "settings": { "routeOverrideEnabled": true, "_links": {} }, "theme": { "themeKey": "<string>" }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" } }, "history": { "createdDate": "<string>", "createdBy": { "type": "known" } }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "title": "<string>", "excerpt": "<string>", "url": "<string>", "resultParentContainer": { "title": "<string>", "displayUrl": "<string>" }, "resultGlobalContainer": { "title": "<string>", "displayUrl": "<string>" }, "breadcrumbs": [ { "label": "<string>", "url": "<string>", "separator": "<string>" } ], "entityType": "<string>", "iconCssClass": "<string>", "lastModified": "<string>", "friendlyLastModified": "<string>", "score": 2154 } ], "offset": 2154, "max_results": 2154, "size": 2154, "totalSize": 2154, "cqlQuery": "<string>", "searchDuration": 2154, "archivedResultCount": 2154, "_links": {} }`

---

GET

## Search users

Searches for users using user-specific queries from the [Confluence Query Language (CQL)](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-query/).

Note that CQL input queries submitted through the `/wiki/rest/api/search/user` endpoint only support user-specific fields like `user`, `user.fullname`, `user.accountid`, and `user.userkey`.

Note that some user fields may be set to null depending on the user's privacy settings. These are: email, profilePicture, displayName, and timeZone.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**offset**

integer

**max_results**

integer

**include**

array<string>

**sitePermissionTypeFilter**

string

### Responses

200OK

Returned if the requested results are returned.

#### application/json

SearchPageResponseSearchResult

Show child properties

400Bad Request

403Forbidden

GET/wiki/rest/api/search/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/search/user?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 ``{ "results": [ { "content": { "id": "<string>", "type": "<string>", "content_status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "content_status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "_expandable": {}, "_links": {} }, "update": { "operation": "administer", "_expandable": {}, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "user": { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": {}, "personalSpace": { "key": "<string>", "name": "<string>", "type": "<string>", "content_status": "<string>", "_expandable": {}, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} }, "space": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "homepage": { "type": "<string>", "content_status": "<string>" }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "size": 2154 }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "content_status": "<string>", "settings": { "routeOverrideEnabled": true, "_links": {} }, "theme": { "themeKey": "<string>" }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" } }, "history": { "createdDate": "<string>", "createdBy": { "type": "known" } }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "title": "<string>", "excerpt": "<string>", "url": "<string>", "resultParentContainer": { "title": "<string>", "displayUrl": "<string>" }, "resultGlobalContainer": { "title": "<string>", "displayUrl": "<string>" }, "breadcrumbs": [ { "label": "<string>", "url": "<string>", "separator": "<string>" } ], "entityType": "<string>", "iconCssClass": "<string>", "lastModified": "<string>", "friendlyLastModified": "<string>", "score": 2154 } ], "offset": 2154, "max_results": 2154, "size": 2154, "totalSize": 2154, "cqlQuery": "<string>", "searchDuration": 2154, "archivedResultCount": 2154, "_links": {} }`