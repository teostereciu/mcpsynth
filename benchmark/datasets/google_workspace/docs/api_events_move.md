# Events: move

*Source: https://developers.google.com/calendar/api/v3/reference/events/move*

---

# Events: move


**Note:**
Requires authorization.


Moves an event to another calendar, i.e. changes an event's organizer. Note that only `default` events can be moved; `birthday`, `focusTime`, `fromGmail`, `outOfOffice` and `workingLocation` events cannot be moved.
Try it now.


## Request


### HTTP request


```
POST https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId/move
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier of the source calendar where the event currently is on. |
| eventId | string | Event identifier. |
| Required query parameters |
| destination | string | Calendar identifier of the target calendar where the event is to be moved to. |
| Optional query parameters |
| sendNotifications | boolean | Deprecated. Please use sendUpdates instead. Whether to send notifications about the change of the event's organizer. Note that some emails might still be sent even if you set the value to false . The default is false . |
| sendUpdates | string | Guests who should receive notifications about the change of the event's organizer. Acceptable values are: " all ": Notifications are sent to all guests. " externalOnly ": Notifications are sent to non-Google Calendar guests only. " none ": No notifications are sent. For calendar migration tasks, consider using the Events.import method instead. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.events |
| https://www.googleapis.com/auth/calendar.events.owned |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


Do not supply a request body with this method.


## Response


If successful, this method returns an [Events resource](/workspace/calendar/api/v3/reference/events#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]