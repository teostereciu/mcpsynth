# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-group-and-user-picker/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Group and user picker

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents a list of users and a list of groups. Use it to obtain the details to populate user and group picker suggestions list.

Operations

[GET/rest/api/3/groupuserpicker](/cloud/jira/platform/rest/v3/api-group-group-and-user-picker/#api-rest-api-3-groupuserpicker-get)

---

GET

## Find users and groups

Returns a list of users and groups matching a string. The string is used:

  * for users, to find a case-insensitive match with display name and e-mail address. Note that if a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.
  * for groups, to find a case-sensitive match with group name.


For example, if the string _tin_ is used, records with the display name _Tina_ , email address _[sarah@tinplatetraining.com](mailto:sarah@tinplatetraining.com)_ , and the group _accounting_ would be returned.

Optionally, the search can be refined to:

  * the projects and issue types associated with a custom field, such as a user picker. The search can then be further refined to return only users and groups that have permission to view specific:

    * projects.
    * issue types.

If multiple projects or issue types are specified, they must be a subset of those enabled for the custom field or no results are returned. For example, if a field is enabled for projects A, B, and C then the search could be limited to projects B and C. However, if the search is limited to projects B and D, nothing is returned.

  * not return Connect app users and groups.

  * return groups that have a case-insensitive match with the query.


The primary use case for this resource is to populate a picker field suggestion list with users or groups. To this end, the returned object includes an `html` field for each list. This field highlights the matched query term in the item name with the HTML strong tag. Also, each list is wrapped in a response object that contains a header for use in a picker, specifically _Showing X of Y matching groups_.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** _Browse users and groups_ [global permission](https://confluence.atlassian.com/x/yodKLg).

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:group:jira`, `read:user:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Query parameters

Expand all

**query**

string

Required

**maxResults**

integer

**showAvatar**

boolean

**fieldId**

string

**projectId**

array<string>

**issueTypeId**

array<string>

**avatarSize**

string

**caseInsensitive**

boolean

**excludeConnectAddons**

boolean

### Responses

200OK

Returned if the request is successful.

#### application/json

FoundUsersAndGroups

List of users and groups found in a search.

Show child properties

400Bad Request

401Unauthorized

403Forbidden

429Too Many Requests

GET/rest/api/3/groupuserpicker

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/groupuserpicker?query={query}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``{ "groups": { "groups": [ { "groupId": "276f955c-63d7-42c8-9520-92d01dca0625", "html": "<b>j</b>dog-developers", "name": "jdog-developers" }, { "groupId": "6e87dc72-4f1f-421f-9382-2fee8b652487", "html": "<b>j</b>uvenal-bot", "name": "juvenal-bot" } ], "header": "Showing 20 of 25 matching groups", "total": 25 }, "users": { "header": "Showing 20 of 25 matching groups", "total": 25, "users": [ { "accountId": "5b10a2844c20165700ede21g", "accountType": "atlassian", "avatarUrl": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "displayName": "Mia Krystof", "html": "<strong>Mi</strong>a Krystof - <strong>mi</strong>a@example.com (<strong>mi</strong>a)", "key": "mia", "name": "mia" } ] } }`