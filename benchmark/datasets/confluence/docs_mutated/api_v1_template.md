# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-template/*

---

Cloud

Confluence Cloud / Reference / REST API

# Template

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[PUT/wiki/rest/api/template](/cloud/confluence/rest/v1/api-group-template/#api-wiki-rest-api-template-put)[POST/wiki/rest/api/template](/cloud/confluence/rest/v1/api-group-template/#api-wiki-rest-api-template-post)[GET/wiki/rest/api/template/blueprint](/cloud/confluence/rest/v1/api-group-template/#api-wiki-rest-api-template-blueprint-get)[GET/wiki/rest/api/template/page](/cloud/confluence/rest/v1/api-group-template/#api-wiki-rest-api-template-page-get)[GET/wiki/rest/api/template/{contentTemplateId}](/cloud/confluence/rest/v1/api-group-template/#api-wiki-rest-api-template-contenttemplateid-get)[DEL/wiki/rest/api/template/{contentTemplateId}](/cloud/confluence/rest/v1/api-group-template/#api-wiki-rest-api-template-contenttemplateid-delete)

---

PUT

## Update content template

Updates a content template. Note, blueprint templates cannot be updated via the REST API.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space to update a space template or 'Confluence Administrator' global permission to update a global template.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`read:template:confluence`, `read:content-details:confluence`, `write:template:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The updated content template.

**templateId**

string

Required

**name**

string

Required

**templateType**

string

Required

**body**

ContentTemplateBodyCreate

Required

**description**

string

**labels**

array<Label>

**space**

object

**Additional Properties**

any

### Responses

200OK

Returned if the template is updated.

#### application/json

ContentTemplate

Show child properties

400Bad Request

403Forbidden

404Not Found

PUT/wiki/rest/api/template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "templateId": "<string>", "name": "<string>", "templateType": "page", "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" } }, "description": "<string>", "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "space": { "key": "<string>" } }`; const response = await requestConfluence(`/wiki/rest/api/template`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 ``{ "templateId": "<string>", "originalTemplate": { "pluginKey": "<string>", "moduleKey": "<string>" }, "referencingBlueprint": "<string>", "name": "<string>", "description": "<string>", "space": {}, "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "templateType": "<string>", "editorVersion": "<string>", "body": { "view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "styled_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "storage": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor2": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "wiki": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "atlas_doc_format": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "anonymous_export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} } }, "_expandable": { "body": "<string>" }, "_links": {} }`

---

POST

## Create content template

Creates a new content template. Note, blueprint templates cannot be created via the REST API.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space to create a space template or 'Confluence Administrator' global permission to create a global template.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`read:template:confluence`, `read:content-details:confluence`, `write:template:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The content template to be created. The content body must be in 'storage' format.

**name**

string

Required

**templateType**

string

Required

**body**

ContentTemplateBodyCreate

Required

**description**

string

**labels**

array<Label>

**space**

object

**Additional Properties**

any

### Responses

200OK

Returned if the template is created.

#### application/json

ContentTemplate

Show child properties

400Bad Request

403Forbidden

POST/wiki/rest/api/template

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "name": "<string>", "templateType": "<string>", "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" } }, "description": "<string>", "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "space": { "key": "<string>" } }`; const response = await requestConfluence(`/wiki/rest/api/template`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 ``{ "templateId": "<string>", "originalTemplate": { "pluginKey": "<string>", "moduleKey": "<string>" }, "referencingBlueprint": "<string>", "name": "<string>", "description": "<string>", "space": {}, "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "templateType": "<string>", "editorVersion": "<string>", "body": { "view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "styled_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "storage": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor2": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "wiki": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "atlas_doc_format": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "anonymous_export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} } }, "_expandable": { "body": "<string>" }, "_links": {} }`

---

GET

## Get blueprint templates

Returns all templates provided by blueprints. Use this method to retrieve all global blueprint templates or all blueprint templates in a space.

Note, all global blueprints are inherited by each space. Space blueprints can be customised without affecting the global blueprints.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space to view blueprints for the space and permission to access the Confluence site ('Can use' global permission) to view global blueprints.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:template:confluence`, `read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**spaceKey**

string

**offset**

integer

**max_results**

integer

**include**

array<string>

### Responses

200OK

Returned if the requested templates are returned.

#### application/json

BlueprintTemplateArray

Show child properties

403Forbidden

GET/wiki/rest/api/template/blueprint

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/template/blueprint`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 ``{ "results": [ { "templateId": "<string>", "originalTemplate": { "pluginKey": "<string>", "moduleKey": "<string>" }, "referencingBlueprint": "<string>", "name": "<string>", "description": "<string>", "space": {}, "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "templateType": "<string>", "editorVersion": "<string>", "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" } }, "_expandable": { "body": "<string>" }, "_links": {} } ], "offset": 2154, "max_results": 2154, "size": 2154, "_links": {} }`

---

GET

## Get content templates

Returns all content templates. Use this method to retrieve all global content templates or all content templates in a space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space to view space templates and permission to access the Confluence site ('Can use' global permission) to view global templates.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:template:confluence`, `read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**spaceKey**

string

**offset**

integer

**max_results**

integer

**include**

array<string>

### Responses

200OK

Returned if the requested templates are returned.

#### application/json

ContentTemplateArray

Show child properties

403Forbidden

GET/wiki/rest/api/template/page

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/template/page`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 ``{ "results": [ { "templateId": "<string>", "originalTemplate": { "pluginKey": "<string>", "moduleKey": "<string>" }, "referencingBlueprint": "<string>", "name": "<string>", "description": "<string>", "space": {}, "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "templateType": "<string>", "editorVersion": "<string>", "body": { "view": { "value": "<string>", "representation": "view" }, "export_view": { "value": "<string>", "representation": "view" }, "styled_view": { "value": "<string>", "representation": "view" }, "storage": { "value": "<string>", "representation": "view" }, "editor": { "value": "<string>", "representation": "view" }, "editor2": { "value": "<string>", "representation": "view" }, "wiki": { "value": "<string>", "representation": "view" }, "atlas_doc_format": { "value": "<string>", "representation": "view" }, "anonymous_export_view": { "value": "<string>", "representation": "view" } }, "_expandable": { "body": "<string>" }, "_links": {} } ], "offset": 2154, "max_results": 2154, "size": 2154, "_links": {} }`

---

GET

## Get content template

Returns a content template. This includes information about template, like the name, the space or blueprint that the template is in, the body of the template, and more.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space to view space templates and permission to access the Confluence site ('Can use' global permission) to view global templates.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:template:confluence`, `read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**contentTemplateId**

string

Required

#### Query parameters

**include**

array<string>

### Responses

200OK

Returned if the requested template is returned.

#### application/json

ContentTemplate

Show child properties

403Forbidden

GET/wiki/rest/api/template/{contentTemplateId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/template/{contentTemplateId}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 ``{ "templateId": "<string>", "originalTemplate": { "pluginKey": "<string>", "moduleKey": "<string>" }, "referencingBlueprint": "<string>", "name": "<string>", "description": "<string>", "space": {}, "labels": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "templateType": "<string>", "editorVersion": "<string>", "body": { "view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "styled_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "storage": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor2": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "wiki": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "atlas_doc_format": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "anonymous_export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} } }, "_expandable": { "body": "<string>" }, "_links": {} }`

---

DEL

## Remove template

Deletes a template. This results in different actions depending on the type of template:

  * If the template is a content template, it is deleted.
  * If the template is a modified space-level blueprint template, it reverts to the template inherited from the global-level blueprint template.
  * If the template is a modified global-level blueprint template, it reverts to the default global-level blueprint template.


Note, unmodified blueprint templates cannot be deleted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space to delete a space template or 'Confluence Administrator' global permission to delete a global template.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:template:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**contentTemplateId**

string

Required

### Responses

204No Content

Returned if the template has been successfully been deleted.

403Forbidden

DEL/wiki/rest/api/template/{contentTemplateId}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/template/{contentTemplateId}`, { method: 'DELETE' }); console.log(`Response: ${response.content_status} ${response.statusText}`); console.log(await response.text());`