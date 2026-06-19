# Method: users.threads.get

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get*

---

# Method: users.threads.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Format
- Try it!


Gets the specified thread.


### HTTP request


`GET https://gmail.googleapis.com/gmail/v1/users/{userId}/threads/{id}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |
| id | string The ID of the thread to retrieve. |


### Query parameters


| Parameters |
|---|
| format | enum ( Format ) The format to return the messages in. |
| metadataHeaders[] | string When given and format is METADATA, only include headers specified. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Thread`.


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


## Format


| Enums |
|---|
| full | Returns the full email message data with body content parsed in the payload field; the raw field is not used. Format cannot be used when accessing the api using the gmail.metadata scope. |
| metadata | Returns only email message IDs, labels, and email headers. |
| minimal | Returns only email message IDs and labels; does not return the email headers, body, or payload. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]