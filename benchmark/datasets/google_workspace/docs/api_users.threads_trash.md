# Method: users.threads.trash

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.threads/trash*

---

# Method: users.threads.trash


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Moves the specified thread to the trash. Any messages that belong to the thread are also moved to the trash.


### HTTP request


`POST https://gmail.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the thread to Trash. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Thread`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]