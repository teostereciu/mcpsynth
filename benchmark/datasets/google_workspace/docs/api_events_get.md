# Events: get

*Source: https://developers.google.com/calendar/api/v3/reference/events/get*

---

# Events: get


**Note:**
Authorization optional.


Returns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the [events.list method using the iCalUID parameter](/workspace/calendar/api/v3/reference/events/list#iCalUID).
Try it now.


## Request


### HTTP request


```
GET https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |
| eventId | string | Event identifier. |
| Optional query parameters |
| alwaysIncludeEmail | boolean | Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided). |
| maxAttendees | integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. |
| timeZone | string | Time zone used in the response. Optional. The default is the time zone of the calendar. |


### Authorization


This request allows authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar.readonly |
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.events.readonly |
| https://www.googleapis.com/auth/calendar.events |
| https://www.googleapis.com/auth/calendar.app.created |
| https://www.googleapis.com/auth/calendar.events.freebusy |
| https://www.googleapis.com/auth/calendar.events.owned |
| https://www.googleapis.com/auth/calendar.events.owned.readonly |
| https://www.googleapis.com/auth/calendar.events.public.readonly |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


Do not supply a request body with this method.


## Response


If successful, this method returns an [Events resource](/workspace/calendar/api/v3/reference/events#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]