# Method: replies.list

*Source: https://developers.google.com/drive/api/reference/rest/v3/replies/list*

---

# Method: replies.list


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- Try it!


Lists a comment's replies. For more information, see [Manage comments and replies](https://developers.google.com/workspace/drive/api/guides/manage-comments).


### HTTP request


`GET https://www.googleapis.com/drive/v3/files/{fileId}/comments/{commentId}/replies`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| fileId | string The ID of the file. |
| commentId | string The ID of the comment. |


### Query parameters


| Parameters |
|---|
| includeDeleted | boolean Whether to include deleted replies. Deleted replies don't include their original content. |
| pageSize | integer The maximum number of replies to return per page. |
| pageToken | string The token for continuing a previous list request on the next page. This should be set to the value of nextPageToken from the previous response. |


### Request body


The request body must be empty.


### Response body


A list of replies to a comment on a file.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "replies" : [ { object ( Reply ) } ] , "kind" : string , "nextPageToken" : string } |


| Fields |
|---|
| replies[] | object ( Reply ) The list of replies. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
| kind | string Identifies what kind of resource this is. Value: the fixed string "drive#replyList" . |
| nextPageToken | string The page token for the next page of replies. This will be absent if the end of the replies list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. The page token is typically valid for several hours. However, if new items are added or removed, your expected results might differ. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `
          https://www.googleapis.com/auth/drive.file`
- `
          https://www.googleapis.com/auth/drive.meet.readonly`
- `
          https://www.googleapis.com/auth/drive.readonly`


Some scopes are restricted and require a security assessment for your app to use them. For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-02 UTC."],[],[]]