# Acl: insert

*Source: https://developers.google.com/calendar/api/v3/reference/acl/insert*

---

# Acl: insert


**Note:**
Requires authorization.


Creates an access control rule.
Try it now.


## Request


### HTTP request


```
POST https://www.googleapis.com/calendar/v3/calendars/calendarId/acl
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |
| Optional query parameters |
| sendNotifications | boolean | Whether to send notifications about the calendar sharing change. Optional. The default is True. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.acls |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


In the request body, supply an [Acl resource](/workspace/calendar/api/v3/reference/acl#resource) with the following properties:


| Property name | Value | Description | Notes |
|---|---|---|---|
| Required Properties |
| role | string | The role assigned to the scope. Possible values are: " none " - Provides no access. " freeBusyReader " - Provides read access to free/busy information. " reader " - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. " writer " - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. Provides read access to the calendar's ACLs. " owner " - Provides manager access to the calendar. This role has all of the permissions of the writer role with the additional ability to modify access levels of other users. Important: the owner role is different from the calendar's data owner. A calendar has a single data owner, but can have multiple users with owner role. | writable |
| scope | object | The extent to which calendar access is granted by this ACL rule. |  |
| scope. type | string | The type of the scope. Possible values are: " default " - The public scope. This is the default value. " user " - Limits the scope to a single user. " group " - Limits the scope to a group. " domain " - Limits the scope to a domain. Note: The permissions granted to the " default ", or public, scope apply to any user, authenticated or not. |  |
| Optional Properties |
| scope. value | string | The email address of a user or group, or the name of a domain, depending on the scope type. Omitted for type " default ". | writable |


## Response


If successful, this method returns an [Acl resource](/workspace/calendar/api/v3/reference/acl#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-28 UTC."],[],[]]