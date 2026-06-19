# CalendarList: insert

*Source: https://developers.google.com/calendar/api/v3/reference/calendarList/insert*

---

# CalendarList: insert


**Note:**
Requires authorization.


Inserts an existing calendar into the user's calendar list.
Try it now.


## Request


### HTTP request


```
POST https://www.googleapis.com/calendar/v3/users/me/calendarList
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Optional query parameters |
| colorRgbFormat | boolean | Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.calendarlist |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


In the request body, supply a [CalendarList resource](/workspace/calendar/api/v3/reference/calendarList#resource) with the following properties:


| Property name | Value | Description | Notes |
|---|---|---|---|
| Required Properties |
| id | string | Identifier of the calendar. |  |
| Optional Properties |
| backgroundColor | string | The main color of the calendar in the hexadecimal format " #0088aa ". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert , update and patch methods. Optional. | writable |
| colorId | string | The color of the calendar. This is an ID referring to an entry in the calendar section of the colors definition (see the colors endpoint ). This property is superseded by the backgroundColor and foregroundColor properties and can be ignored when using these properties. Optional. | writable |
| defaultReminders[] | list | The default reminders that the authenticated user has for this calendar. | writable |
| defaultReminders[]. method | string | The method used by this reminder. Possible values are: " email " - Reminders are sent via email. " popup " - Reminders are sent via a UI popup. Required when adding a reminder. | writable |
| defaultReminders[]. minutes | integer | Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes). Required when adding a reminder. | writable |
| foregroundColor | string | The foreground color of the calendar in the hexadecimal format " #ffffff ". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert , update and patch methods. Optional. | writable |
| hidden | boolean | Whether the calendar has been hidden from the list. Optional. The attribute is only returned when the calendar is hidden, in which case the value is true . | writable |
| notificationSettings | object | The notifications that the authenticated user is receiving for this calendar. | writable |
| notificationSettings.notifications[]. method | string | The method used to deliver the notification. The possible value is: " email " - Notifications are sent via email. Required when adding a notification. | writable |
| notificationSettings.notifications[]. type | string | The type of notification. Possible values are: " eventCreation " - Notification sent when a new event is put on the calendar. " eventChange " - Notification sent when an event is changed. " eventCancellation " - Notification sent when an event is cancelled. " eventResponse " - Notification sent when an attendee responds to the event invitation. " agenda " - An agenda with the events of the day (sent out in the morning). Required when adding a notification. | writable |
| selected | boolean | Whether the calendar content shows up in the calendar UI. Optional. The default is False. | writable |
| summaryOverride | string | The summary that the authenticated user has set for this calendar. Optional. | writable |


## Response


If successful, this method returns a [CalendarList resource](/workspace/calendar/api/v3/reference/calendarList#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]