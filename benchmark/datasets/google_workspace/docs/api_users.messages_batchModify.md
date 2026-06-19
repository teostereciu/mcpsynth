# Method: users.messages.batchModify

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/batchModify*

---

# Method: users.messages.batchModify


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body
- Authorization scopes
- Try it!


Modifies the labels on the specified messages.


### HTTP request


`POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/batchModify`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "ids" : [ string ] , "addLabelIds" : [ string ] , "removeLabelIds" : [ string ] } |


| Fields |
|---|
| ids[] | string The IDs of the messages to modify. There is a limit of 1000 ids per request. |
| addLabelIds[] | string A list of label IDs to add to messages. |
| removeLabelIds[] | string A list of label IDs to remove from messages. |


### Response body


If successful, the response body is empty.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]