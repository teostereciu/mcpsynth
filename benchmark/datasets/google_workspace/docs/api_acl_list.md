# Acl: list

*Source: https://developers.google.com/calendar/api/v3/reference/acl/list*

---

# Acl: list


**Note:**
Requires authorization.


Returns the rules in the access control list for the calendar.
Try it now.


## Request


### HTTP request


```
GET https://www.googleapis.com/calendar/v3/calendars/calendarId/acl
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |
| Optional query parameters |
| maxResults | integer | Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional. |
| pageToken | string | Token specifying which result page to return. Optional. |
| showDeleted | boolean | Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to " none ". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False. |
| syncToken | string | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken . Learn more about incremental synchronization. Optional. The default is to return all entries. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.acls |
| https://www.googleapis.com/auth/calendar.acls.readonly |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


Do not supply a request body with this method.


## Response


If successful, this method returns a response body with the following structure:


```
{
  "kind": "calendar#acl",
  "etag": etag,
  "nextPageToken": string,
  "nextSyncToken": string,
  "items": [
    acl Resource
  ]
}
```


| Property name | Value | Description | Notes |
|---|---|---|---|
| kind | string | Type of the collection (" calendar#acl "). |  |
| etag | etag | ETag of the collection. |  |
| nextPageToken | string | Token used to access the next page of this result. Omitted if no further results are available, in which case nextSyncToken is provided. |  |
| items[] | list | List of rules on the access control list. |  |
| nextSyncToken | string | Token used at a later point in time to retrieve only the entries that have changed since this result was returned. Omitted if further results are available, in which case nextPageToken is provided. |  |


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]