# Method: users.settings.updateVacation

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.settings/updateVacation*

---

# Method: users.settings.updateVacation


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Updates vacation responder settings.


### HTTP request


`PUT https://gmail.googleapis.com/gmail/v1/users/{userId}/settings/vacation`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string User's email address. The special value "me" can be used to indicate the authenticated user. |


### Request body


The request body contains an instance of `VacationSettings`.


### Response body


If successful, the response body contains an instance of `VacationSettings`.


### Authorization scopes


Requires the following OAuth scope:


- `https://www.googleapis.com/auth/gmail.settings.basic`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]