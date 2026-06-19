# Method: users.messages.delete

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete*

---

# Method: users.messages.delete


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer `messages.trash` instead.


### HTTP request


`DELETE https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the message to delete. |


### Request body


The request body must be empty.


### Response body


If successful, the response body is an empty JSON object.


### Authorization scopes


Requires the following OAuth scope:


- `https://mail.google.com/`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]