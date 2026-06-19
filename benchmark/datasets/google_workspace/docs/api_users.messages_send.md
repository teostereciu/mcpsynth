# Method: users.messages.send

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send*

---

# Method: users.messages.send


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. For example usage, see [Sending email](https://developers.google.com/workspace/gmail/api/guides/sending).


### HTTP request


- Upload URI, for media upload requests:`POST https://gmail.googleapis.com/upload/gmail/v1/users/{userId}/messages/send`
- Metadata URI, for metadata-only requests:`POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/send`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Request body


The request body contains an instance of `Message`.


### Response body


If successful, the response body contains an instance of `Message`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.compose`
- `
          https://www.googleapis.com/auth/gmail.send`
- `
          https://www.googleapis.com/auth/gmail.addons.current.action.compose`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]