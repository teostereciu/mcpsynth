# Method: users.labels.list

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list*

---

# Method: users.labels.list


- HTTP request
- Path parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- Try it!


Lists all labels in the user's mailbox.


### HTTP request


`GET https://gmail.googleapis.com/gmail/v1/users/{userId}/labels`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "labels" : [ { object ( Label ) } ] } |


| Fields |
|---|
| labels[] | object ( Label ) List of labels. Note that each label resource only contains an id , name , messageListVisibility , labelListVisibility , and type . The labels.get method can fetch additional label details. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.readonly`
- `
          https://www.googleapis.com/auth/gmail.labels`
- `
          https://www.googleapis.com/auth/gmail.metadata`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]