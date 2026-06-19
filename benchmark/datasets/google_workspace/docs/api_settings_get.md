# Settings: get

*Source: https://developers.google.com/calendar/api/v3/reference/settings/get*

---

# Settings: get


**Note:**
Requires authorization.


Returns a single user setting.
Try it now.


## Request


### HTTP request


```
GET https://www.googleapis.com/calendar/v3/users/me/settings/setting
```


### Parameters


| Parameter name | Value | Description |
|---|---|---|
| Path parameters |
| setting | string | The id of the user setting. |


### Authorization


This request requires authorization with at least one of the following scopes:


| Scope |
|---|
| https://www.googleapis.com/auth/calendar.readonly |
| https://www.googleapis.com/auth/calendar |
| https://www.googleapis.com/auth/calendar.settings.readonly |


For more information, see the [authentication and authorization](/workspace/guides/configure-oauth-consent) page.


### Request body


Do not supply a request body with this method.


## Response


If successful, this method returns a [Settings resource](/workspace/calendar/api/v3/reference/settings#resource) in the response body.


## Try it!


Use the APIs Explorer below to call this method on live data and see the response.


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]]