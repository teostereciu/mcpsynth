# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-restrictions/*

---

Cloud

Confluence Cloud / Reference / REST API

# Content restrictions

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/content/{id}/restriction](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-get)[PUT/wiki/rest/api/content/{id}/restriction](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-put)[POST/wiki/rest/api/content/{id}/restriction](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-post)[DEL/wiki/rest/api/content/{id}/restriction](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-delete)[GET/wiki/rest/api/content/{id}/restriction/byOperation](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-get)[GET/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-get)[GET/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-bygroupid-groupid-get)[PUT/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-bygroupid-groupid-put)[DEL/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-bygroupid-groupid-delete)[GET/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-user-get)[PUT/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-user-put)[DEL/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user](/cloud/confluence/rest/v1/api-group-content-restrictions/#api-wiki-rest-api-content-id-restriction-byoperation-operationkey-user-delete)

---

GET

## Get restrictions

Returns the restrictions on a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**expand**

array<string>

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested restrictions are returned.

#### application/json

ContentRestrictionArray

Show child properties

404Not Found

GET/wiki/rest/api/content/{id}/restriction

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 ``{ "results": [ { "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known" } ], "start": 2154, "limit": 2154, "size": 2154, "totalSize": 150, "_links": {} }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "restrictionsHash": "<string>", "_links": {} }`

---

PUT

## Update restrictions

Updates restrictions for a piece of content. This removes the existing restrictions and replaces them with the restrictions in the request.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`read:content-details:confluence`, `write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**expand**

array<string>

#### Request bodyapplication/json

The updated restrictions for the content.

oneOf [object, array<ContentRestrictionUpdate>]

object

Show child properties

ContentRestrictionUpdate

Show child properties

### Responses

200OK

Returned if the requested restrictions are updated.

#### application/json

ContentRestrictionArray

Show child properties

404Not Found

PUT/wiki/rest/api/content/{id}/restriction

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "results": [ { "operation": "administer", "restrictions": { "group": [ { "type": "group", "id": "<string>" } ], "user": [ { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": {}, "personalSpace": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} } ] }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "_expandable": {}, "_links": {} }, "update": { "operation": "administer", "_expandable": {}, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} } } ], "start": 2154, "limit": 2154, "size": 2154, "restrictionsHash": "<string>", "_links": {} }`; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 ``{ "results": [ { "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known" } ], "start": 2154, "limit": 2154, "size": 2154, "totalSize": 150, "_links": {} }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "restrictionsHash": "<string>", "_links": {} }`

---

POST

## Add restrictions

Adds restrictions to a piece of content. Note, this does not change any existing restrictions on the content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`read:content-details:confluence`, `write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**expand**

array<string>

#### Request bodyapplication/json

The restrictions to be added to the content.

oneOf [object, array<ContentRestrictionUpdate>]

object

Show child properties

ContentRestrictionUpdate

Show child properties

### Responses

200OK

Returned if the requested restrictions are added.

#### application/json

ContentRestrictionArray

Show child properties

404Not Found

POST/wiki/rest/api/content/{id}/restriction

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "results": [ { "operation": "administer", "restrictions": { "group": [ { "type": "group", "id": "<string>" } ], "user": [ { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": {}, "personalSpace": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} } ] }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "_expandable": {}, "_links": {} }, "update": { "operation": "administer", "_expandable": {}, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} } } ], "start": 2154, "limit": 2154, "size": 2154, "restrictionsHash": "<string>", "_links": {} }`; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 ``{ "results": [ { "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known" } ], "start": 2154, "limit": 2154, "size": 2154, "totalSize": 150, "_links": {} }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "restrictionsHash": "<string>", "_links": {} }`

---

DEL

## Delete restrictions

Removes all restrictions (read and update) on a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`read:content-details:confluence`, `write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**expand**

array<string>

### Responses

200OK

Returned if the restrictions are removed.

#### application/json

ContentRestrictionArray

Show child properties

400Bad Request

403Forbidden

404Not Found

DEL/wiki/rest/api/content/{id}/restriction

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 ``{ "results": [ { "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known" } ], "start": 2154, "limit": 2154, "size": 2154, "totalSize": 150, "_links": {} }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "history": { "latest": true }, "version": { "when": "<string>", "number": 57, "minorEdit": true }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": {}, "childTypes": {}, "descendants": {}, "container": {}, "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "dynamic": { "value": "<string>", "representation": "view" }, "raw": { "value": "<string>", "representation": "view" }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": {}, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "restrictionsHash": "<string>", "_links": {} }`

---

GET

## Get restrictions by operation

Returns restrictions on a piece of content by operation. This method is similar to [Get restrictions]() except that the operations are properties of the return object, rather than items in a results array.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**expand**

array<string>

### Responses

200OK

Returned if the requested restrictions are returned.

#### application/json

object

Show child properties

GET/wiki/rest/api/content/{id}/restriction/byOperation

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

---

GET

## Get restrictions for operation

Returns the restictions on a piece of content for a given operation (read or update).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

#### Query parameters

Expand all

**expand**

array<string>

**start**

integer

**limit**

integer

### Responses

200OK

Returned if the requested restrictions are returned.

#### application/json

ContentRestriction

Show child properties

GET/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719 720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 ``{ "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known", "username": "<string>", "userKey": "<string>", "accountId": "<string>", "accountType": "atlassian", "email": "<string>", "publicName": "<string>", "profilePicture": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "displayName": "<string>", "timeZone": "<string>", "externalCollaborator": true, "isExternalCollaborator": true, "isGuest": true, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "details": {}, "personalSpace": { "key": "<string>", "name": "<string>", "type": "<string>", "status": "<string>", "_expandable": {}, "_links": {} }, "_expandable": { "operations": "<string>", "details": "<string>", "personalSpace": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "totalSize": 150, "_links": {} }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>", "usageType": "USERBASE_GROUP", "managedBy": "ADMINS", "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "content": { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "size": 2154 }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "status": "<string>", "settings": { "routeOverrideEnabled": true, "_links": {} }, "theme": { "themeKey": "<string>" }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" } }, "history": { "createdDate": "<string>", "createdBy": { "type": "known" } }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "history": { "latest": true, "createdBy": { "type": "known" }, "ownedBy": { "type": "known" }, "lastOwnedBy": { "type": "known" }, "createdDate": "<string>", "lastUpdated": { "when": "<string>", "number": 57, "minorEdit": true }, "previousVersion": { "when": "<string>", "number": 57, "minorEdit": true }, "contributors": { "publishers": {} }, "nextVersion": { "when": "<string>", "number": 57, "minorEdit": true }, "_expandable": { "lastUpdated": "<string>", "previousVersion": "<string>", "contributors": "<string>", "nextVersion": "<string>", "ownedBy": "<string>", "lastOwnedBy": "<string>" }, "_links": {} }, "version": { "by": { "type": "known" }, "when": "<string>", "friendlyWhen": "<string>", "message": "<string>", "number": 57, "minorEdit": true, "collaborators": {}, "_expandable": { "content": "<string>", "collaborators": "<string>" }, "_links": {}, "contentTypeModified": true, "confRev": "<string>", "syncRev": "<string>", "syncRevSource": "<string>" }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": { "attachment": { "results": [], "size": 2154, "_links": {} }, "comment": { "results": [], "size": 2154, "_links": {} }, "page": { "results": [], "size": 2154, "_links": {} }, "whiteboard": { "results": [], "size": 2154, "_links": {} }, "database": { "results": [], "size": 2154, "_links": {} }, "embed": { "results": [], "size": 2154, "_links": {} }, "folder": { "results": [], "size": 2154, "_links": {} }, "_expandable": { "attachment": "<string>", "comment": "<string>", "page": "<string>", "whiteboard": "<string>", "database": "<string>", "embed": "<string>", "folder": "<string>" }, "_links": {} }, "childTypes": { "attachment": { "value": true, "_links": {} }, "comment": { "value": true, "_links": {} }, "page": { "value": true, "_links": {} }, "_expandable": { "all": "<string>", "attachment": "<string>", "comment": "<string>", "page": "<string>", "whiteboard": "<string>", "database": "<string>", "embed": "<string>", "folder": "<string>" } }, "descendants": { "attachment": { "results": [], "size": 2154, "_links": {} }, "comment": { "results": [], "size": 2154, "_links": {} }, "page": { "results": [], "size": 2154, "_links": {} }, "whiteboard": { "results": [], "size": 2154, "_links": {} }, "database": { "results": [], "size": 2154, "_links": {} }, "embed": { "results": [], "size": 2154, "_links": {} }, "folder": { "results": [], "size": 2154, "_links": {} }, "_expandable": { "attachment": "<string>", "comment": "<string>", "page": "<string>", "whiteboard": "<string>", "database": "<string>", "embed": "<string>", "folder": "<string>" }, "_links": {} }, "container": {}, "body": { "view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "styled_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "storage": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "wiki": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor2": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "anonymous_export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "atlas_doc_format": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "dynamic": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "raw": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": { "currentuser": { "favourited": { "isFavourite": true, "favouritedDate": "<string>" }, "lastmodified": { "version": { "when": "<string>", "number": 57, "minorEdit": true }, "friendlyLastModified": "<string>" }, "lastcontributed": { "status": "<string>", "when": "<string>" }, "viewed": { "lastSeen": "<string>", "friendlyLastSeen": "<string>" }, "scheduled": {}, "_expandable": { "favourited": "<string>", "lastmodified": "<string>", "lastcontributed": "<string>", "viewed": "<string>", "scheduled": "<string>" } }, "properties": {}, "frontend": {}, "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} } }, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} }`

---

GET

## Get content restriction status for group

Returns whether the specified content restriction applies to a group. For example, if a page with `id=123` has a `read` restriction for the `123456` group id, the following request will return `true`:

`/wiki/rest/api/content/123/restriction/byOperation/read/byGroupId/123456`

Note that a response of `true` does not guarantee that the group can view the page, as it does not account for account-inherited restrictions, space permissions, or even product access. For more information, see [Confluence permissions](https://confluence.atlassian.com/x/_AozKw).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

**groupId**

string

Required

### Responses

200OK

Returns true if the content restriction applies to the group. The response will not return a response body.

403Forbidden

404Not Found

GET/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}`); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

PUT

## Add group to content restriction

Adds a group to a content restriction by Group Id. That is, grant read or update permission to the group for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

**groupId**

string

Required

### Responses

200OK

Returned if the group is added to the content restriction by Group Id. The response body will be empty.

400Bad Request

403Forbidden

404Not Found

PUT/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}`, { method: 'PUT' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove group from content restriction

Removes a group from a content restriction. That is, remove read or update permission for the group for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

**groupId**

string

Required

### Responses

200OK

Returned if the group is removed from the content restriction. The response body will be empty.

400Bad Request

403Forbidden

404Not Found

DEL/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get content restriction status for user

Returns whether the specified content restriction applies to a user. For example, if a page with `id=123` has a `read` restriction for a user with an account ID of `384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192`, the following request will return `true`:

`/wiki/rest/api/content/123/restriction/byOperation/read/user?accountId=384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192`

Note that a response of `true` does not guarantee that the user can view the page, as it does not account for account-inherited restrictions, space permissions, or even product access. For more information, see [Confluence permissions](https://confluence.atlassian.com/x/_AozKw).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

200OK

Return true if the content restriction applies to the user. The response body will be empty.

404Not Found

GET/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user`); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

PUT

## Add user to content restriction

Adds a user to a content restriction. That is, grant read or update permission to the user for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

200OK

Returned if the user is added to the content restriction. The response body will be empty.

400Bad Request

404Not Found

PUT/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user`, { method: 'PUT' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

DEL

## Remove user from content restriction

Removes a group from a content restriction. That is, remove read or update permission for the group for a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content.restriction:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

Expand all

**id**

string

Required

**operationKey**

string

Required

#### Query parameters

Expand all

**key**

string

**username**

string

**accountId**

string

### Responses

200OK

Returned if the user is removed from the content restriction. The response body will be empty.

404Not Found

DEL/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`