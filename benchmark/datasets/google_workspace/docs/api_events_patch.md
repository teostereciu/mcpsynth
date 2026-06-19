# Events: patch

*Source: https://developers.google.com/calendar/api/v3/reference/events/patch*

---

# Events: patch


**Note:**
Requires authorization.


Updates an event. This method supports patch semantics. Note that each patch request consumes three quota units; prefer using a `get` followed by an `update`. The field values you specify replace the existing values. Fields that you don't specify in the request remain unchanged. Array fields, if specified, overwrite the existing arrays; this discards any previous array elements.
Try it now.


## Request


### HTTP request


```
PATCH https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |
| eventId | string | Event identifier. |
| Optional query parameters |
| alwaysIncludeEmail | boolean | Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided). |
| conferenceDataVersion | integer | Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
          Acceptable values are 0 to 1 , inclusive. |
| maxAttendees | integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. |
| sendNotifications | boolean | Deprecated. Please use sendUpdates instead. Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false . The default is false . |
| sendUpdates | string | Guests who should receive notifications about the event update (for example, title changes, etc.). Acceptable values are: " all ": Notifications are sent to all guests. " externalOnly ": Notifications are sent to non-Google Calendar guests only. " none ": No notifications are sent. For calendar migration tasks, consider using the Events.import method instead. |
| supportsAttachments | boolean | Whether API client performing operation supports event attachments. Optional. The default is False. |


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


In the request body, supply the relevant portions of an [Events resource](/workspace/calendar/api/v3/reference/events#resource), according to the rules of patch semantics.


## Response


If successful, this method returns an [Events resource](/workspace/calendar/api/v3/reference/events#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-03 UTC."],[],[]]