# Method: users.drafts.list

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/list*

---

# Method: users.drafts.list


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- Try it!


Lists the drafts in the user's mailbox.


### HTTP request


`GET https://gmail.googleapis.com/gmail/v1/users/{userId}/drafts`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Query parameters


| Parameters |
|---|
| maxResults | integer ( uint32 format) Maximum number of drafts to return. This field defaults to 100. The maximum allowed value for this field is 500. |
| pageToken | string Page token to retrieve a specific page of results in the list. |
| q | string Only return draft messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com>
                  is:unread" . |
| includeSpamTrash | boolean Include drafts from SPAM and TRASH in the results. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "drafts" : [ { object ( Draft ) } ] , "nextPageToken" : string , "resultSizeEstimate" : integer } |


| Fields |
|---|
| drafts[] | object ( Draft ) List of drafts. Note that the Message property in each Draft resource only contains an id and a threadId . The messages.get method can fetch additional message details. |
| nextPageToken | string Token to retrieve the next page of results in the list. |
| resultSizeEstimate | integer ( uint32 format) Estimated total number of results. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.compose`
- `
          https://www.googleapis.com/auth/gmail.readonly`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]