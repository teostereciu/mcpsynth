# Confluence Cloud

*Source: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content-states/*

---

Cloud

Confluence Cloud / Reference / REST API

# Content states

[Postman Collection](/cloud/confluence/confcloud.1.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json?_v=1.8494.0)

Operations

[GET/wiki/rest/api/content/{id}/state](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-content-id-state-get)[PUT/wiki/rest/api/content/{id}/state](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-content-id-state-put)[DEL/wiki/rest/api/content/{id}/state](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-content-id-state-delete)[GET/wiki/rest/api/content/{id}/state/available](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-content-id-state-available-get)[GET/wiki/rest/api/content-states](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-content-states-get)[GET/wiki/rest/api/space/{spaceKey}/state](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-space-spacekey-state-get)[GET/wiki/rest/api/space/{spaceKey}/state/settings](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-space-spacekey-state-settings-get)[GET/wiki/rest/api/space/{spaceKey}/state/content](/cloud/confluence/rest/v1/api-group-content-states/#api-wiki-rest-api-space-spacekey-state-content-get)

---

GET

## Get content state

Gets the current content state of the draft or current version of content. To specify the draft version, set the parameter status to draft, otherwise archived or current will get the relevant published state. **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to view the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.summary`

**Granular** :`read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**status**

string

### Responses

200OK

Returned if permission allows viewing of content.

#### application/json

ContentStateResponse

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/content/{id}/state

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/state`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "contentState": { "id": 73, "name": "<string>", "color": "<string>" }, "lastUpdated": "<string>" }`

---

PUT

## Set the content state of a content and publishes a new version of the content.

Sets the content state of the content specified and creates a new version (publishes the content without changing the body) of the content with the new state.

You may pass in either an id of a state, or the name and color of a desired new state. If all 3 are passed in, id will be used. If the name and color passed in already exist under the current user's existing custom states, the existing state will be reused. If custom states are disabled in the space of the content (which can be determined by getting the content state space settings of the content's space) then this set will fail.

You may not remove a content state via this PUT request. You must use the DELETE method. A specified state is required in the body of this request.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content:confluence`, `read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**status**

string

Required

#### Request bodyapplication/json

Expand all

Content state fields for state. Pass in id for an existing state, or new name and color for best matching existing state, or new state if allowed in space.

**name**

string

**color**

string

**id**

integer

### Responses

200OK

Returned if content state is set successfully.

#### application/json

ContentStateResponse

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

PUT/wiki/rest/api/content/{id}/state

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; var bodyData = `{ "name": "<string>", "color": "<string>", "id": 80 }`; const response = await requestConfluence(`/wiki/rest/api/content/{id}/state?status={status}`, { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: bodyData }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "contentState": { "id": 73, "name": "<string>", "color": "<string>" }, "lastUpdated": "<string>" }`

---

DEL

## Removes the content state of a content and publishes a new version.

Removes the content state of the content specified and creates a new version (publishes the content without changing the body) of the content with the new status.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content:confluence`, `read:content-details:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**status**

string

### Responses

200OK

Returned if content state is removed from content.

#### application/json

ContentStateResponse

Show child properties

401Unauthorized

403Forbidden

404Not Found

DEL/wiki/rest/api/content/{id}/state

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/state`, { method: 'DELETE', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 ``{ "contentState": { "id": 73, "name": "<string>", "color": "<string>" }, "lastUpdated": "<string>" }`

---

GET

## Gets available content states for content.

Gets content states that are available for the content to be set as. Will return all enabled Space Content States. Will only return most the 3 most recently published custom content states to match UI editor list. To get all custom content states, use the /content-states endpoint.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Permission to edit the content.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:confluence-content`

**Granular** :`write:content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the content is found and permission is valid.

#### application/json

AvailableContentStates

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/content/{id}/state/available

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content/{id}/state/available`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``{ "spaceContentStates": [ { "id": 73, "name": "<string>", "color": "<string>" } ], "customContentStates": [ { "id": 73, "name": "<string>", "color": "<string>" } ] }`

---

GET

## Get Custom Content States

Get custom content states that authenticated user has created.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required** Must have user authentication.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:user.property:confluence`

**Granular** :`read:user.property:confluence`

Connect apps cannot access this REST resource.

### Request

This request has no parameters.

### Responses

200OK

Custom Content States that user has crated. Returned if user authenticated.

#### application/json

array<ContentState>

Show child properties

401Unauthorized

GET/wiki/rest/api/content-states

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/content-states`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``[ { "id": 73, "name": "<string>", "color": "<string>" } ]`

---

GET

## Get space suggested content states

Get content states that are suggested in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-space.summary`

**Granular** :`read:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

### Responses

200OK

Returned if the requested space exists, and user has space view permission.

#### application/json

array<ContentState>

Space suggested content states that users can choose from

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/space/{spaceKey}/state

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/state`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 ``[ { "id": 73, "name": "<string>", "color": "<string>" } ]`

---

GET

## Get content state settings for space

Get object describing whether content states are allowed at all, if custom content states or space content states are restricted, and a list of space content states allowed for the space if they are not restricted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'Admin' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-space.summary`

**Granular** :`read:space.setting:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

### Responses

200OK

Returned if the requested space exists, and user has space admin permission.

#### application/json

ContentStateSettings

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/space/{spaceKey}/state/settings

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/state/settings`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 ``{ "contentStatesAllowed": true, "customContentStatesAllowed": true, "spaceContentStatesAllowed": true, "spaceContentStates": [ { "id": 73, "name": "<string>", "color": "<string>" } ] }`

---

GET

## Get content in space with given content state

Returns all content that has the provided content state in a space.

If the expand query parameter is used with the `body.export_view` and/or `body.styled_view` properties, then the query limit parameter will be restricted to a maximum value of 25.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: 'View' permission for the space.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:confluence-content.all`

**Granular** :`read:content:confluence`

**[Connect app scope](/cloud/confluence/scopes) required**:Â `READ`

### Request

#### Path parameters

**spaceKey**

string

Required

#### Query parameters

Expand all

**state-id**

integer

Required

**expand**

array<string>

**limit**

integer

**start**

integer

### Responses

200OK

Returned if search was successful.

#### application/json

ContentArray

Show child properties

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/wiki/rest/api/space/{spaceKey}/state/content

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestConfluence } from "@forge/bridge"; const response = await requestConfluence(`/wiki/rest/api/space/{spaceKey}/state/content?state-id={state-id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 ``{ "results": [ { "id": "<string>", "type": "<string>", "status": "<string>", "title": "<string>", "space": { "id": 2154, "key": "<string>", "alias": "<string>", "name": "<string>", "icon": { "path": "<string>", "width": 2154, "height": 2154, "isDefault": true }, "description": { "plain": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "view": { "value": "<string>", "representation": "plain", "embeddedContent": [ {} ] }, "_expandable": { "view": "<string>", "plain": "<string>" } }, "type": "<string>", "metadata": { "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "size": 2154 }, "_expandable": {} }, "operations": [ { "operation": "administer", "targetType": "<string>" } ], "permissions": [ { "operation": { "operation": "administer", "targetType": "<string>" }, "anonymousAccess": true, "unlicensedAccess": true } ], "status": "<string>", "settings": { "routeOverrideEnabled": true, "_links": {} }, "theme": { "themeKey": "<string>" }, "lookAndFeel": { "headings": { "color": "<string>" }, "links": { "color": "<string>" }, "menus": { "hoverOrFocus": { "backgroundColor": "<string>" }, "color": "<string>" }, "header": { "backgroundColor": "<string>", "button": { "backgroundColor": "<string>", "color": "<string>" }, "primaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "secondaryNavigation": { "color": "<string>", "hoverOrFocus": { "backgroundColor": "<string>", "color": "<string>" } }, "search": { "backgroundColor": "<string>", "color": "<string>" } }, "content": {}, "bordersAndDividers": { "color": "<string>" } }, "history": { "createdDate": "<string>", "createdBy": { "type": "known" } }, "_expandable": { "settings": "<string>", "metadata": "<string>", "operations": "<string>", "lookAndFeel": "<string>", "permissions": "<string>", "icon": "<string>", "description": "<string>", "theme": "<string>", "history": "<string>", "homepage": "<string>", "identifiers": "<string>" }, "_links": {} }, "history": { "latest": true, "createdBy": { "type": "known" }, "ownedBy": { "type": "known" }, "lastOwnedBy": { "type": "known" }, "createdDate": "<string>", "lastUpdated": { "when": "<string>", "number": 57, "minorEdit": true }, "previousVersion": { "when": "<string>", "number": 57, "minorEdit": true }, "contributors": { "publishers": {} }, "nextVersion": { "when": "<string>", "number": 57, "minorEdit": true }, "_expandable": { "lastUpdated": "<string>", "previousVersion": "<string>", "contributors": "<string>", "nextVersion": "<string>", "ownedBy": "<string>", "lastOwnedBy": "<string>" }, "_links": {} }, "version": { "by": { "type": "known" }, "when": "<string>", "friendlyWhen": "<string>", "message": "<string>", "number": 57, "minorEdit": true, "collaborators": {}, "_expandable": { "content": "<string>", "collaborators": "<string>" }, "_links": {}, "contentTypeModified": true, "confRev": "<string>", "syncRev": "<string>", "syncRevSource": "<string>" }, "ancestors": [], "operations": [ { "operation": "administer", "targetType": "<string>" } ], "children": { "_expandable": { "attachment": "<string>", "comment": "<string>", "page": "<string>", "whiteboard": "<string>", "database": "<string>", "embed": "<string>", "folder": "<string>" }, "_links": {} }, "childTypes": { "attachment": { "value": true, "_links": {} }, "comment": { "value": true, "_links": {} }, "page": { "value": true, "_links": {} }, "_expandable": { "all": "<string>", "attachment": "<string>", "comment": "<string>", "page": "<string>", "whiteboard": "<string>", "database": "<string>", "embed": "<string>", "folder": "<string>" } }, "descendants": { "_expandable": { "attachment": "<string>", "comment": "<string>", "page": "<string>", "whiteboard": "<string>", "database": "<string>", "embed": "<string>", "folder": "<string>" }, "_links": {} }, "container": {}, "body": { "view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "styled_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "storage": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "wiki": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "editor2": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "anonymous_export_view": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "atlas_doc_format": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "dynamic": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "raw": { "value": "<string>", "representation": "view", "embeddedContent": [ {} ], "webresource": {}, "mediaToken": { "collectionIds": [ "<string>" ], "contentId": "<string>", "expiryDateTime": "<string>", "fileIds": [ "<string>" ], "token": "<string>" }, "_expandable": { "content": "<string>", "embeddedContent": "<string>", "webresource": "<string>", "mediaToken": "<string>" }, "_links": {} }, "_expandable": { "editor": "<string>", "view": "<string>", "export_view": "<string>", "styled_view": "<string>", "storage": "<string>", "editor2": "<string>", "anonymous_export_view": "<string>", "atlas_doc_format": "<string>", "wiki": "<string>", "dynamic": "<string>", "raw": "<string>" } }, "restrictions": { "read": { "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known" } ] }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} }, "update": { "operation": "administer", "restrictions": { "user": { "results": [ { "type": "known" } ] }, "group": { "results": [ { "type": "group", "name": "<string>", "id": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154 }, "_expandable": { "user": "<string>", "group": "<string>" } }, "_expandable": { "restrictions": "<string>", "content": "<string>" }, "_links": {} }, "_expandable": { "read": "<string>", "update": "<string>" }, "_links": {} }, "metadata": { "currentuser": { "favourited": { "isFavourite": true, "favouritedDate": "<string>" }, "lastmodified": { "version": { "when": "<string>", "number": 57, "minorEdit": true }, "friendlyLastModified": "<string>" }, "lastcontributed": { "status": "<string>", "when": "<string>" }, "viewed": { "lastSeen": "<string>", "friendlyLastSeen": "<string>" }, "scheduled": {}, "_expandable": { "favourited": "<string>", "lastmodified": "<string>", "lastcontributed": "<string>", "viewed": "<string>", "scheduled": "<string>" } }, "properties": {}, "frontend": {}, "labels": { "results": [ { "prefix": "<string>", "name": "<string>", "id": "<string>", "label": "<string>" } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} } }, "macroRenderedOutput": {}, "extensions": {}, "_expandable": { "childTypes": "<string>", "container": "<string>", "metadata": "<string>", "operations": "<string>", "children": "<string>", "restrictions": "<string>", "history": "<string>", "ancestors": "<string>", "body": "<string>", "version": "<string>", "descendants": "<string>", "space": "<string>", "extensions": "<string>", "schedulePublishDate": "<string>", "schedulePublishInfo": "<string>", "macroRenderedOutput": "<string>" }, "_links": {} } ], "start": 2154, "limit": 2154, "size": 2154, "_links": {} }`