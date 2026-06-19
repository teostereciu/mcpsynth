# Method: users.messages.modify

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify*

---

# Method: users.messages.modify


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body
- Authorization scopes
- Try it!


Modifies the labels on the specified message.


### HTTP request


`POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the message to modify. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "addLabelIds" : [ string ] , "removeLabelIds" : [ string ] } |


| Fields |
|---|
| addLabelIds[] | string A list of IDs of labels to add to this message. You can add up to 100 labels with each update. |
| removeLabelIds[] | string A list IDs of labels to remove from this message. You can remove up to 100 labels with each update. |


### Response body


If successful, the response body contains an instance of `Message`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]