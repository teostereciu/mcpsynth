# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-settings/*

---

Cloud

Confluence Cloud / Reference / REST API

# Settings

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/settings/lookandfeel](/cloud/confluence/rest/v1/api-group-settings/#api-wiki-rest-api-settings-lookandfeel-get)[PUT/wiki/rest/api/settings/lookandfeel](/cloud/confluence/rest/v1/api-group-settings/#api-wiki-rest-api-settings-lookandfeel-put)[POST/wiki/rest/api/settings/lookandfeel/custom](/cloud/confluence/rest/v1/api-group-settings/#api-wiki-rest-api-settings-lookandfeel-custom-post)[DEL/wiki/rest/api/settings/lookandfeel/custom](/cloud/confluence/rest/v1/api-group-settings/#api-wiki-rest-api-settings-lookandfeel-custom-delete)[GET/wiki/rest/api/settings/systemInfo](/cloud/confluence/rest/v1/api-group-settings/#api-wiki-rest-api-settings-systeminfo-get)

---

GET

## Get look and feel settings

Returns the look and feel settings for the site or a single space. This includes attributes such as the color scheme, padding, and border radius.

The look and feel settings for a space can be inherited from the global look and feel settings or provided by a theme.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: None

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:configuration:confluence`, `read:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Query parameters

**spaceKey**

string

### Responses

200OK

Returned if the requested look and feel settings are returned.

#### application/json

LookAndFeelSettings

Show child properties

400Bad Request

404Not Found

GET/wiki/rest/api/settings/lookandfeel

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/settings/lookandfeel`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 ``{ "selected": "global", "global": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "highlightColor": "<string>" }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": { "screen": { "background": "<string>" }, "container": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "header": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "body": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" } }, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {} }, "theme": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "highlightColor": "<string>" }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": { "screen": { "background": "<string>" }, "container": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "header": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "body": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" } }, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {} }, "custom": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "highlightColor": "<string>" }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": { "screen": { "background": "<string>" }, "container": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "header": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "body": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" } }, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {} } }`

---

PUT

## Select look and feel settings

Sets the look and feel settings to the default (global) settings, the custom settings, or the current theme's settings for a space. The custom and theme settings can only be selected if there is already a theme set for a space. Note, the default space settings are inherited from the current global settings.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:space.setting:confluence`, `write:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Request bodyapplication/json

Expand all

The look and feel type to be set.

**spaceKey**

string

Required

**lookAndFeelType**

string

Required

### Responses

200OK

Returned if the look and feel settings were set.

#### application/json

LookAndFeelSelection

Look and feel selection

Show child properties

400Bad Request

403Forbidden

404Not Found

409Conflict

PUT/wiki/rest/api/settings/lookandfeel

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "spaceKey": "<string>", "lookAndFeelType": "global" }`; const response = await requestConfluence(`/wiki/rest/api/settings/lookandfeel`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "spaceKey": "<string>", "lookAndFeelType": "global" }`

---

POST

## Update look and feel settings

Updates the look and feel settings for the site or for a single space. If custom settings exist, they are updated. If no custom settings exist, then a set of custom settings is created.

Note, if a theme is selected for a space, the space look and feel settings are provided by the theme and cannot be overridden.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:configuration:confluence`, `read:space.setting:confluence`, `write:configuration:confluence`, `write:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Query parameters

**spaceKey**

string

#### Request bodyapplication/json

Expand all

The updated settings. All values for the settings must be included, regardless of whether they are being changed.

One way to create the request body is to copy the settings from the response body of [Get look and feel settings]() and modify it as needed.

**headings**

object

Required

**links**

object

Required

**menus**

MenusLookAndFeel

Required

**header**

HeaderLookAndFeel

Required

**horizontalHeader**

HorizontalHeaderLookAndFeel

**content**

ContentLookAndFeel

Required

**bordersAndDividers**

object

Required

**spaceReference**

object

### Responses

200OK

Returned if the look and feel settings are updated.

#### application/json

allOf [LookAndFeel, object]

LookAndFeel

Show child properties

object

Show child properties

400Bad Request

403Forbidden

404Not Found

POST/wiki/rest/api/settings/lookandfeel/custom

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "highlightColor": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "highlightColor": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "highlightColor": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "highlightColor": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": { "screen": { "background": "<string>", "backgroundAttachment": "<string>", "backgroundBlendMode": "<string>", "backgroundClip": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundOrigin": "<string>", "backgroundPosition": "<string>", "backgroundRepeat": "<string>", "backgroundSize": "<string>", "layer": { "width": "<string>", "height": "<string>" }, "gutterTop": "<string>", "gutterRight": "<string>", "gutterBottom": "<string>", "gutterLeft": "<string>" }, "container": { "background": "<string>", "backgroundAttachment": "<string>", "backgroundBlendMode": "<string>", "backgroundClip": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundOrigin": "<string>", "backgroundPosition": "<string>", "backgroundRepeat": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "header": { "background": "<string>", "backgroundAttachment": "<string>", "backgroundBlendMode": "<string>", "backgroundClip": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundOrigin": "<string>", "backgroundPosition": "<string>", "backgroundRepeat": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "body": { "background": "<string>", "backgroundAttachment": "<string>", "backgroundBlendMode": "<string>", "backgroundClip": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundOrigin": "<string>", "backgroundPosition": "<string>", "backgroundRepeat": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" } }, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {} }`; const response = await requestConfluence(`/wiki/rest/api/settings/lookandfeel/custom`, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 ``{ "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "horizontalHeader": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "highlightColor": "<string>" }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": { "screen": { "background": "<string>" }, "container": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "header": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" }, "body": { "background": "<string>", "backgroundColor": "<string>", "backgroundImage": "<string>", "backgroundSize": "<string>", "padding": "<string>", "borderRadius": "<string>" } }, "bordersAndDividers": { "color": "<string>" }, "spaceReference": {}, "_links": {} }`

---

DEL

## Reset look and feel settings

Resets the custom look and feel settings for the site or a single space. This changes the values of the custom settings to be the same as the default settings. It does not change which settings (default or custom) are selected. Note, the default space settings are inherited from the current global settings.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`write:configuration:confluence`, `write:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Query parameters

**spaceKey**

string

### Responses

204No Content

Returned if the look and feel settings have been reset.

400Bad Request

403Forbidden

404Not Found

DEL/wiki/rest/api/settings/lookandfeel/custom

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/settings/lookandfeel/custom`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get system info

Returns the system information for the Confluence Cloud tenant. This information is used by Atlassian.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to access the Confluence site ('Can use' global permission).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`manage:confluence-configuration`

**Granular** :`read:configuration:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the system information for the Confluence Cloud tenant is returned.

#### application/json

SystemInfoEntity

Nullable: `true`

Show child properties

403Forbidden

GET/wiki/rest/api/settings/systemInfo

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/settings/systemInfo`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 ``{ "cloudId": "<string>", "commitHash": "<string>", "baseUrl": "<string>", "fallbackBaseUrl": "<string>", "edition": "<string>", "siteTitle": "<string>", "defaultLocale": "<string>", "defaultTimeZone": "<string>", "microsPerimeter": "<string>" }`