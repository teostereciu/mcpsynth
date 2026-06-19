# Events: update

*Source: https://developers.google.com/calendar/api/v3/reference/events/update*

---

# Events: update


**Note:**
Requires authorization.


Updates an event. This method does not support patch semantics and always updates the entire event resource. To do a partial update, perform a `get` followed by an `update` using etags to ensure atomicity.
Try it now.


## Request


### HTTP request


```
PUT https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId
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


In the request body, supply an [Events resource](/workspace/calendar/api/v3/reference/events#resource) with the following properties:


| Property name | Value | Description | Notes |
|---|---|---|---|
| Required Properties |
| end | nested object | The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance. |  |
| start | nested object | The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance. |  |
| Optional Properties |
| anyoneCanAddSelf | boolean | Whether anyone can invite themselves to the event (deprecated). Optional. The default is False. | writable |
| attachments[]. fileUrl | string | URL link to the attachment. For adding Google Drive file attachments use the same format as in alternateLink property of the Files resource in the Drive API. Required when adding an attachment. | writable |
| attendees[] | list | The attendees of the event. See the Events with attendees guide for more information on scheduling events with other calendar users. Service accounts need to use domain-wide delegation of authority to populate the attendee list. | writable |
| attendees[]. additionalGuests | integer | Number of additional guests. Optional. The default is 0. | writable |
| attendees[]. comment | string | The attendee's response comment. Optional. | writable |
| attendees[]. displayName | string | The attendee's name, if available. Optional. | writable |
| attendees[]. email | string | The attendee's email address, if available. This field must be present when adding an attendee. It must be a valid email address as per RFC5322 . Required when adding an attendee. | writable |
| attendees[]. optional | boolean | Whether this is an optional attendee. Optional. The default is False. | writable |
| attendees[]. resource | boolean | Whether the attendee is a resource. Can only be set when the attendee is added to the event for the first time. Subsequent modifications are ignored. Optional. The default is False. | writable |
| attendees[]. responseStatus | string | The attendee's response status. Possible values are: " needsAction " - The attendee has not responded to the invitation (recommended for new events). " declined " - The attendee has declined the invitation. " tentative " - The attendee has tentatively accepted the invitation. " accepted " - The attendee has accepted the invitation. Warning: If you add an event using the values declined , tentative , or accepted , attendees with the "Add invitations to my calendar" setting set to "When I respond to invitation in email" or "Only if the sender is known" might have their response reset to needsAction and won't see an event in their calendar unless they change their response in the event invitation email. Furthermore, if more than 200 guests are invited to the event, response status is not propagated to the guests. | writable |
| attendeesOmitted | boolean | Whether attendees may have been omitted from the event's representation. When retrieving an event, this may be due to a restriction specified by the maxAttendee query parameter. When updating an event, this can be used to only update the participant's response. Optional. The default is False. | writable |
| colorId | string | The color of the event. This is an ID referring to an entry in the event section of the colors definition (see the colors endpoint ). Optional. | writable |
| conferenceData | nested object | The conference-related information, such as details of a Google Meet conference. To create new conference details use the createRequest field. To persist your changes, remember to set the conferenceDataVersion request parameter to 1 for all event modification requests. Warning: Reusing Google Meet conference data across different events can cause access issues and expose meeting details to unintended users. To help ensure meeting privacy, always generate a unique conference for each event by using the createRequest field. | writable |
| description | string | Description of the event. Can contain HTML. Optional. | writable |
| end. date | date | The date, in the format "yyyy-mm-dd", if this is an all-day event. | writable |
| end. dateTime | datetime | The time, as a combined date-time value (formatted according to RFC3339 ). A time zone offset is required unless a time zone is explicitly specified in timeZone . | writable |
| end. timeZone | string | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end. | writable |
| extendedProperties. private | object | Properties that are private to the copy of the event that appears on this calendar. | writable |
| extendedProperties. shared | object | Properties that are shared between copies of the event on other attendees' calendars. | writable |
| focusTimeProperties | nested object | Focus Time event data. Used if eventType is focusTime . | writable |
| gadget. display | string | The gadget's display mode. Deprecated. Possible values are: " icon " - The gadget displays next to the event's title in the calendar view. " chip " - The gadget displays when the event is clicked. | writable |
| gadget. height | integer | The gadget's height in pixels. The height must be an integer greater than 0. Optional. Deprecated. | writable |
| gadget. iconLink | string | The gadget's icon URL. The URL scheme must be HTTPS. Deprecated. | writable |
| gadget. link | string | The gadget's URL. The URL scheme must be HTTPS. Deprecated. | writable |
| gadget. preferences | object | Preferences. | writable |
| gadget. title | string | The gadget's title. Deprecated. | writable |
| gadget. type | string | The gadget's type. Deprecated. | writable |
| gadget. width | integer | The gadget's width in pixels. The width must be an integer greater than 0. Optional. Deprecated. | writable |
| guestsCanInviteOthers | boolean | Whether attendees other than the organizer can invite others to the event. Optional. The default is True. | writable |
| guestsCanModify | boolean | Whether attendees other than the organizer can modify the event. Optional. The default is False. | writable |
| guestsCanSeeOtherGuests | boolean | Whether attendees other than the organizer can see who the event's attendees are. Optional. The default is True. | writable |
| location | string | Geographic location of the event as free-form text. Optional. | writable |
| originalStartTime. date | date | The date, in the format "yyyy-mm-dd", if this is an all-day event. | writable |
| originalStartTime. dateTime | datetime | The time, as a combined date-time value (formatted according to RFC3339 ). A time zone offset is required unless a time zone is explicitly specified in timeZone . | writable |
| originalStartTime. timeZone | string | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end. | writable |
| outOfOfficeProperties | nested object | Out of office event data. Used if eventType is outOfOffice . | writable |
| recurrence[] | list | List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event, as specified in RFC5545 . Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events. | writable |
| reminders. overrides[] | list | If the event doesn't use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event. The maximum number of override reminders is 5. | writable |
| reminders.overrides[]. method | string | The method used by this reminder. Possible values are: " email " - Reminders are sent via email. " popup " - Reminders are sent via a UI popup. Required when adding a reminder. | writable |
| reminders.overrides[]. minutes | integer | Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes). Required when adding a reminder. | writable |
| reminders. useDefault | boolean | Whether the default reminders of the calendar apply to the event. | writable |
| sequence | integer | Sequence number as per iCalendar. | writable |
| source. title | string | Title of the source; for example a title of a web page or an email subject. | writable |
| source. url | string | URL of the source pointing to a resource. The URL scheme must be HTTP or HTTPS. | writable |
| start. date | date | The date, in the format "yyyy-mm-dd", if this is an all-day event. | writable |
| start. dateTime | datetime | The time, as a combined date-time value (formatted according to RFC3339 ). A time zone offset is required unless a time zone is explicitly specified in timeZone . | writable |
| start. timeZone | string | The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end. | writable |
| status | string | Status of the event. Optional. Possible values are: " confirmed " - The event is confirmed. This is the default status. " tentative " - The event is tentatively confirmed. " cancelled " - The event is cancelled (deleted). The list method returns cancelled events only on incremental sync (when syncToken or updatedMin are specified) or if the showDeleted flag is set to true . The get method always returns them. A cancelled status represents two different states depending on the event type: Cancelled exceptions of an uncancelled recurring event indicate that this instance should no longer be presented to the user. Clients should store these events for the lifetime of the parent recurring event. Cancelled exceptions are only guaranteed to have values for the id , recurringEventId and originalStartTime fields populated. The other fields might be empty. All other cancelled events represent deleted events. Clients should remove their locally synced copies. Such cancelled events will eventually disappear, so do not rely on them being available indefinitely. Deleted events are only guaranteed to have the id field populated. On the organizer's calendar, cancelled events continue to expose event details (summary, location, etc.) so that they can be restored (undeleted). Similarly, the events to which the user was invited and that they manually removed continue to provide details. However, incremental sync requests with showDeleted set to false will not return these details. If an event changes its organizer (for example via the move operation) and the original organizer is not on the attendee list, it will leave behind a cancelled event where only the id field is guaranteed to be populated. | writable |
| summary | string | Title of the event. | writable |
| transparency | string | Whether the event blocks time on the calendar. Optional. Possible values are: " opaque " - Default value. The event does block time on the calendar. This is equivalent to setting Show me as to Busy in the Calendar UI. " transparent " - The event does not block time on the calendar. This is equivalent to setting Show me as to Available in the Calendar UI. | writable |
| visibility | string | Visibility of the event. Optional. Possible values are: " default " - Uses the default visibility for events on the calendar. This is the default value. " public " - The event is public and event details are visible to all readers of the calendar. " private " - The event is private and only event attendees may view event details. " confidential " - The event is private. This value is provided for compatibility reasons. | writable |
| workingLocationProperties | nested object | Working location event data. | writable |
| workingLocationProperties. customLocation | object | If present, specifies that the user is working from a custom location. | writable |
| workingLocationProperties.customLocation. label | string | An optional extra label for additional information. | writable |
| workingLocationProperties. homeOffice | any value | If present, specifies that the user is working at home. | writable |
| workingLocationProperties. officeLocation | object | If present, specifies that the user is working from an office. | writable |
| workingLocationProperties.officeLocation. buildingId | string | An optional building identifier. This should reference a building ID in the organization's Resources database. | writable |
| workingLocationProperties.officeLocation. deskId | string | An optional desk identifier. | writable |
| workingLocationProperties.officeLocation. floorId | string | An optional floor identifier. | writable |
| workingLocationProperties.officeLocation. floorSectionId | string | An optional floor section identifier. | writable |
| workingLocationProperties.officeLocation. label | string | The office name that's displayed in Calendar Web and Mobile clients. We recommend you reference a building name in the organization's Resources database. | writable |
| workingLocationProperties. type | string | Type of the working location. Possible values are: " homeOffice " - The user is working at home. " officeLocation " - The user is working from an office. " customLocation " - The user is working from a custom location. Any details are specified in a sub-field of the specified name, but this field may be missing if empty. Any other fields are ignored. Required when adding working location properties. | writable |


## Response


If successful, this method returns an [Events resource](/workspace/calendar/api/v3/reference/events#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-12 UTC."],[],[]]