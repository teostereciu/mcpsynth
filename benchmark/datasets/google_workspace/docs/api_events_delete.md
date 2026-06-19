# Events: delete

*Source: https://developers.google.com/calendar/api/v3/reference/events/delete*

---

# Events: delete


**Note:**
Requires authorization.


Deletes an event.
Try it now.


## Request


### HTTP request


```
DELETE https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |
| eventId | string | Event identifier. |
| Optional query parameters |
| sendNotifications | boolean | Deprecated. Please use sendUpdates instead. Whether to send notifications about the deletion of the event. Note that some emails might still be sent even if you set the value to false . The default is false . |
| sendUpdates | string | Guests who should receive notifications about the deletion of the event. Acceptable values are: " all ": Notifications are sent to all guests. " externalOnly ": Notifications are sent to non-Google Calendar guests only. " none ": No notifications are sent. For calendar migration tasks, consider using the Events.import method instead. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.events |
| https://www.googleapis.com/auth/calendar.app.created |
| https://www.googleapis.com/auth/calendar.events.owned |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


Do not supply a request body with this method.


## Response


If successful, this method returns an empty response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]