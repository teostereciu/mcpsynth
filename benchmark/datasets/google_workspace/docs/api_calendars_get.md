# Calendars: get

*Source: https://developers.google.com/calendar/api/v3/reference/calendars/get*

---

# Calendars: get


**Note:**
Requires authorization.


Returns metadata for a calendar.
Try it now.


## Request


### HTTP request


```
GET https://www.googleapis.com/calendar/v3/calendars/calendarId
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar.readonly |
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.app.created |
| https://www.googleapis.com/auth/calendar.calendars |
| https://www.googleapis.com/auth/calendar.calendars.readonly |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


Do not supply a request body with this method.


## Response


If successful, this method returns a [Calendars resource](/workspace/calendar/api/v3/reference/calendars#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]