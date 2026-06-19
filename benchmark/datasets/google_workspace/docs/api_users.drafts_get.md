# Method: users.drafts.get

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/get*

---

# Method: users.drafts.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Gets the specified draft.


### HTTP request


`GET https://gmail.googleapis.com/gmail/v1/users/{userId}/drafts/{id}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the draft to retrieve. |


### Query parameters


| Parameters |
|---|
| format | enum ( Format ) The format to return the draft in. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Draft`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.compose`
- `
          https://www.googleapis.com/auth/gmail.readonly`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]