# Method: documents.batchUpdate

*Source: https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate*

---

# Method: documents.batchUpdate


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- Request

- JSON representation
- ReplaceAllTextRequest

- JSON representation
- SubstringMatchCriteria

- JSON representation
- TabsCriteria

- JSON representation
- InsertTextRequest

- JSON representation
- Location

- JSON representation
- EndOfSegmentLocation

- JSON representation
- UpdateTextStyleRequest

- JSON representation
- CreateParagraphBulletsRequest

- JSON representation
- BulletGlyphPreset
- DeleteParagraphBulletsRequest

- JSON representation
- CreateNamedRangeRequest

- JSON representation
- DeleteNamedRangeRequest

- JSON representation
- UpdateParagraphStyleRequest

- JSON representation
- DeleteContentRangeRequest

- JSON representation
- InsertInlineImageRequest

- JSON representation
- InsertTableRequest

- JSON representation
- InsertTableRowRequest

- JSON representation
- TableCellLocation

- JSON representation
- InsertTableColumnRequest

- JSON representation
- DeleteTableRowRequest

- JSON representation
- DeleteTableColumnRequest

- JSON representation
- InsertPageBreakRequest

- JSON representation
- DeletePositionedObjectRequest

- JSON representation
- UpdateTableColumnPropertiesRequest

- JSON representation
- UpdateTableCellStyleRequest

- JSON representation
- TableRange

- JSON representation
- UpdateTableRowStyleRequest

- JSON representation
- ReplaceImageRequest

- JSON representation
- ImageReplaceMethod
- UpdateDocumentStyleRequest

- JSON representation
- MergeTableCellsRequest

- JSON representation
- UnmergeTableCellsRequest

- JSON representation
- CreateHeaderRequest

- JSON representation
- HeaderFooterType
- CreateFooterRequest

- JSON representation
- CreateFootnoteRequest

- JSON representation
- ReplaceNamedRangeContentRequest

- JSON representation
- UpdateSectionStyleRequest

- JSON representation
- InsertSectionBreakRequest

- JSON representation
- DeleteHeaderRequest

- JSON representation
- DeleteFooterRequest

- JSON representation
- PinTableHeaderRowsRequest

- JSON representation
- AddDocumentTabRequest

- JSON representation
- DeleteTabRequest

- JSON representation
- UpdateDocumentTabPropertiesRequest

- JSON representation
- InsertPersonRequest

- JSON representation
- InsertDateRequest

- JSON representation
- WriteControl

- JSON representation
- Response

- JSON representation
- ReplaceAllTextResponse

- JSON representation
- CreateNamedRangeResponse

- JSON representation
- InsertInlineImageResponse

- JSON representation
- InsertInlineSheetsChartResponse

- JSON representation
- CreateHeaderResponse

- JSON representation
- CreateFooterResponse

- JSON representation
- CreateFootnoteResponse

- JSON representation
- AddDocumentTabResponse

- JSON representation
- Try it!


Applies one or more updates to the document.


Each `request` is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied.


Some requests have `replies` to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.


For example, suppose you call batchUpdate with four updates, and only the third one returns information. The response would have two empty replies, the reply to the third request, and another empty reply, in that order.


Because other users may be editing the document, the document might not exactly reflect your changes: your changes may be altered with respect to collaborator changes. If there are no collaborators, the document should reflect your changes. In any case, the updates in your request are guaranteed to be applied together atomically.


### HTTP request


`POST https://docs.googleapis.com/v1/documents/{documentId}:batchUpdate`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| documentId | string The ID of the document to update. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "requests" : [ { object ( Request ) } ] , "writeControl" : { object ( WriteControl ) } } |


| Fields |
|---|
| requests[] | object ( Request ) A list of updates to apply to the document. |
| writeControl | object ( WriteControl ) Provides control over how write requests are executed. |


### Response body


Response message from a `documents.batchUpdate` request.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "documentId" : string , "replies" : [ { object ( Response ) } ] , "writeControl" : { object ( WriteControl ) } } |


| Fields |
|---|
| documentId | string The ID of the document to which the updates were applied to. |
| replies[] | object ( Response ) The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty. |
| writeControl | object ( WriteControl ) The updated write control after applying the request. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/documents`
- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`


For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


## WriteControl


Provides control over how write requests are executed.


| JSON representation |
|---|
| { "requiredRevisionId" : string , "targetRevisionId" : string } |


| Fields |
|---|
| Union field control . Determines the revision of the document to write to and how the request should behave if that revision is not the current revision of the document. If neither field is specified, updates are applied to the latest revision. control can be only one of the following: |
| requiredRevisionId | string The optional revision ID of the document the write request is applied to. If this is not the latest revision of the document, the request is not processed and returns a 400 bad request error. When a required revision ID is returned in a response, it indicates the revision ID of the document after the request was applied. |
| targetRevisionId | string The optional target revision ID of the document the write request is applied to. If collaborator changes have occurred after the document was read using the API, the changes produced by this write request are applied against the collaborator changes. This results in a new revision of the document that incorporates both the collaborator changes and the changes in the request, with the Docs server resolving conflicting changes. When using target revision ID, the API client can be thought of as another collaborator of the document. The target revision ID can only be used to write to recent versions of a document. If the target revision is too far behind the latest revision, the request is not processed and returns a 400 bad request error. The request should be tried again after retrieving the latest version of the document. Usually a revision ID remains valid for use as a target revision for several minutes after it's read, but for frequently edited documents this window might be shorter. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-02 UTC."],[],[]]