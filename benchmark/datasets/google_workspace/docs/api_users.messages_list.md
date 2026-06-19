# Method: users.messages.list

*Source: https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list*

---

# Method: users.messages.list


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- Try it!


Lists the messages in the user's mailbox. For example usage, see [List Gmail messages](https://developers.google.com/workspace/gmail/api/guides/list-messages).


### HTTP request


`GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| userId | string The user's email address. The special value me can be used to indicate the authenticated user. |


### Query parameters


| Parameters |
|---|
| maxResults | integer ( uint32 format) Maximum number of messages to return. This field defaults to 100. The maximum allowed value for this field is 500. |
| pageToken | string Page token to retrieve a specific page of results in the list. |
| q | string Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com>
                  is:unread" . Parameter cannot be used when accessing the api using the gmail.metadata scope. |
| labelIds[] | string Only return messages with labels that match all of the specified label IDs. Messages in a thread might have labels that other messages in the same thread don't have. To learn more, see Manage labels on messages and threads . |
| includeSpamTrash | boolean Include messages from SPAM and TRASH in the results. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "messages" : [ { object ( Message ) } ] , "nextPageToken" : string , "resultSizeEstimate" : integer } |


| Fields |
|---|
| messages[] | object ( Message ) List of messages. Note that each message resource contains only an id and a threadId . Additional message details can be fetched using the messages.get method. |
| nextPageToken | string Token to retrieve the next page of results in the list. |
| resultSizeEstimate | integer ( uint32 format) Estimated total number of results. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://mail.google.com/`
- `
          https://www.googleapis.com/auth/gmail.modify`
- `
          https://www.googleapis.com/auth/gmail.readonly`
- `
          https://www.googleapis.com/auth/gmail.metadata`


For more information, see the [OAuth 2.0 Overview](/identity/protocols/OAuth2).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-05 UTC."],[],[]]