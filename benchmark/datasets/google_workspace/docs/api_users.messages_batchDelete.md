# Method: users.messages.batchDelete

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/batchDelete*

---

# Method: users.messages.batchDelete


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body
- Authorization scopes
- Try it!


Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.


### HTTP request


`POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/batchDelete`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "ids" : [ string ] } |


| Fields |
|---|
| ids[] | string The IDs of the messages to delete. |


### Response body


If successful, the response body is empty.


### Authorization scopes


Requires the following OAuth scope:


- `https://mail.google.com/`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]