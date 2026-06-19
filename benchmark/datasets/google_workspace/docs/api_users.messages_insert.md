# Method: users.messages.insert

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/insert*

---

# Method: users.messages.insert


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. Does not send a message.


### HTTP request


- Upload URI, for media upload requests:`POST https://gmail.googleapis.com/upload/gmail/v1/users/{userId}/messages`
- Metadata URI, for metadata-only requests:`POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Query parameters


| Parameters |
|---|
| internalDateSource | enum ( InternalDateSource ) Source for Gmail's internal date of the message. |
| deleted | boolean Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for Google Workspace accounts. |


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
          https://www.googleapis.com/auth/gmail.insert`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]