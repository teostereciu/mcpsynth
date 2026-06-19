# Calendars: insert

*Source: https://developers.google.com/calendar/api/v3/reference/calendars/insert*

---

# Calendars: insert


**Note:**
Requires authorization.


Creates a secondary calendar.

The authenticated user for the request is made the data owner of the new calendar.


**Note:** We recommend to authenticate as the intended data owner of the calendar. You can use [domain-wide delegation of authority](/workspace/cloud-search/docs/guides/delegation) to allow applications to act on behalf of a specific user. Don't use a service account for authentication. If you use a service account for authentication, the service account is the data owner, which can lead to unexpected behavior. For example, if a service account is the data owner, data ownership cannot be transferred.


Try it now.


## Request


### HTTP request


```
POST https://www.googleapis.com/calendar/v3/calendars
```


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.app.created |
| https://www.googleapis.com/auth/calendar.calendars |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


In the request body, supply a [Calendars resource](/workspace/calendar/api/v3/reference/calendars#resource) with the following properties:


| Property name | Value | Description | Notes |
|---|---|---|---|
| Required Properties |
| summary | string | Title of the calendar. | writable |


## Response


If successful, this method returns a [Calendars resource](/workspace/calendar/api/v3/reference/calendars#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-28 UTC."],[],[]]