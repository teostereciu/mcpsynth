# Method: users.messages.get

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get*

---

# Method: users.messages.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Gets the specified message.


### HTTP request


`GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the message to retrieve. This ID is usually retrieved using messages.list . The ID is also contained in the result when a message is inserted ( messages.insert ) or imported ( messages.import ). |


### Query parameters


| Parameters |
|---|
| format | enum ( Format ) The format to return the message in. |
| metadataHeaders[] | string When given and format is METADATA , only include headers specified. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Message`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.readonly`
- `
          https://www.googleapis.com/auth/gmail.metadata`
- `
          https://www.googleapis.com/auth/gmail.addons.current.message.metadata`
- `
          https://www.googleapis.com/auth/gmail.addons.current.message.readonly`
- `
          https://www.googleapis.com/auth/gmail.addons.current.message.action`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]