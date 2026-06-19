# Events: list

*Source: https://developers.google.com/calendar/api/v3/reference/events/list*

---

# Events: list


**Note:**
Authorization optional.


Returns events on the specified calendar.
Try it now.


## Request


### HTTP request


```
GET https://www.googleapis.com/calendar/v3/calendars/calendarId/events
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| calendarId | string | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the " primary " keyword. |
| Optional query parameters |
| alwaysIncludeEmail | boolean | Deprecated and ignored. |
| eventTypes | string | Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. If unset, returns all event types. Acceptable values are: " birthday ": Special all-day events with an annual recurrence. " default ": Regular events. " focusTime ": Focus time events. " fromGmail ": Events from Gmail. " outOfOffice ": Out of office events. " workingLocation ": Working location events. |
| iCalUID | string | Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID. |
| maxAttendees | integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. |
| maxResults | integer | Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional. |
| orderBy | string | The order of the events returned in the result. Optional. The default is an unspecified, stable order. Acceptable values are: " startTime ": Order by the start date/time (ascending). This is only available when querying single events (i.e. the parameter singleEvents is True) " updated ": Order by last modification time (ascending). |
| pageToken | string | Token specifying which result page to return. Optional. |
| privateExtendedProperty | string | Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints. |
| q | string | Free text search terms to find events that match these terms in the following fields: summary description location attendee's displayName attendee's email organizer's displayName organizer's email workingLocationProperties.officeLocation.buildingId workingLocationProperties.officeLocation.deskId workingLocationProperties.officeLocation.label workingLocationProperties.customLocation.label These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for "Office" or "Bureau" returns working location events of type officeLocation , whereas searching for "Out of office" or "Abwesend" returns out-of-office events. Optional. |
| sharedExtendedProperty | string | Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints. |
| showDeleted | boolean | Whether to include deleted events (with status equals " cancelled ") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False. |
| showHiddenInvitations | boolean | Whether to include hidden invitations in the result. Optional. The default is False. |
| singleEvents | boolean | Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False. |
| syncToken | string | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state. These are: iCalUID orderBy privateExtendedProperty q sharedExtendedProperty timeMin timeMax updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken . Learn more about incremental synchronization. Optional. The default is to return all entries. |
| timeMax | datetime | Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin . |
| timeMin | datetime | Lower bound (exclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax . |
| timeZone | string | Time zone used in the response. Optional. The default is the time zone of the calendar. |
| updatedMin | datetime | Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted . Optional. The default is not to filter by last modification time. |


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


If successful, this method returns a response body with the following structure:


```
{
  "kind": "calendar#events",
  "etag": etag,
  "summary": string,
  "description": string,
  "updated": datetime,
  "timeZone": string,
  "accessRole": string,
  "defaultReminders": [
    {
      "method": string,
      "minutes": integer
    }
  ],
  "nextPageToken": string,
  "nextSyncToken": string,
  "items": [
    events Resource
  ]
}
```


| Property name | Value | Description | Notes |
|---|---|---|---|
| kind | string | Type of the collection (" calendar#events "). |  |
| etag | etag | ETag of the collection. |  |
| summary | string | Title of the calendar. Read-only. |  |
| description | string | Description of the calendar. Read-only. |  |
| updated | datetime | Last modification time of the calendar (as a RFC3339 timestamp). Read-only. |  |
| timeZone | string | The time zone of the calendar. Read-only. |  |
| accessRole | string | The user's access role for this calendar. Read-only. Possible values are: " none " - The user has no access. " freeBusyReader " - The user has read access to free/busy information. " reader " - The user has read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. " writer " - The user has read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. " owner " - The user has manager access to the calendar. This role has all of the permissions of the writer role with the additional ability to see and modify access levels of other users. Important: the owner role is different from the calendar's data owner. A calendar has a single data owner, but can have multiple users with owner role. |  |
| defaultReminders[] | list | The default reminders on the calendar for the authenticated user. These reminders apply to all events on this calendar that do not explicitly override them (i.e. do not have reminders.useDefault set to True). |  |
| defaultReminders[]. method | string | The method used by this reminder. Possible values are: " email " - Reminders are sent via email. " popup " - Reminders are sent via a UI popup. Required when adding a reminder. | writable |
| defaultReminders[]. minutes | integer | Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes). Required when adding a reminder. | writable |
| nextPageToken | string | Token used to access the next page of this result. Omitted if no further results are available, in which case nextSyncToken is provided. |  |
| items[] | list | List of events on the calendar. |  |
| nextSyncToken | string | Token used at a later point in time to retrieve only the entries that have changed since this result was returned. Omitted if further results are available, in which case nextPageToken is provided. |  |


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-28 UTC."],[],[]]