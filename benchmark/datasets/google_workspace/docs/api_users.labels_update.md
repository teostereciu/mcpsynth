# Method: users.labels.update

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.labels/update*

---

# Method: users.labels.update


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Updates the specified label.


### HTTP request


`PUT https://gmail.googleapis.com/gmail/v1/users/{userId}/labels/{id}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the label to update. |


### Request body


The request body contains an instance of `Label`.


### Response body


If successful, the response body contains an instance of `Label`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.labels`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]