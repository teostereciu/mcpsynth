# Method: documents.get

*Source: https://developers.google.com/docs/api/reference/rest/v1/documents/get*

---

# Method: documents.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Gets the latest version of the specified document.


### HTTP request


`GET https://docs.googleapis.com/v1/documents/{documentId}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| documentId | string The ID of the document to retrieve. |


### Query parameters


| Parameters |
|---|
| suggestionsViewMode | enum ( SuggestionsViewMode ) The suggestions view mode to apply to the document. This allows viewing the document with all suggestions inline, accepted or rejected. If one is not specified, DEFAULT_FOR_CURRENT_ACCESS is used. |
| includeTabsContent | boolean Whether to populate the Document.tabs field instead of the text content fields like body and documentStyle on Document . When True : Document content populates in the Document.tabs field instead of the text content fields in Document . When False : The content of the document's first tab populates the content fields in Document excluding Document.tabs . If a document has only one tab, then that tab is used to populate the document content. Document.tabs will be empty. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Document`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/documents`
- `https://www.googleapis.com/auth/documents.readonly`
- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.readonly`
- `https://www.googleapis.com/auth/drive.file`


For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]