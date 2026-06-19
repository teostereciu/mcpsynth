# Method: presentations.batchUpdate

*Source: https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate*

---

# Method: presentations.batchUpdate


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- Request

- JSON representation
- CreateSlideRequest

- JSON representation
- LayoutReference

- JSON representation
- PredefinedLayout
- LayoutPlaceholderIdMapping

- JSON representation
- CreateShapeRequest

- JSON representation
- PageElementProperties

- JSON representation
- CreateTableRequest

- JSON representation
- InsertTextRequest

- JSON representation
- InsertTableRowsRequest

- JSON representation
- InsertTableColumnsRequest

- JSON representation
- DeleteTableRowRequest

- JSON representation
- DeleteTableColumnRequest

- JSON representation
- ReplaceAllTextRequest

- JSON representation
- SubstringMatchCriteria

- JSON representation
- DeleteObjectRequest

- JSON representation
- UpdatePageElementTransformRequest

- JSON representation
- ApplyMode
- UpdateSlidesPositionRequest

- JSON representation
- DeleteTextRequest

- JSON representation
- Range

- JSON representation
- Type
- CreateImageRequest

- JSON representation
- CreateVideoRequest

- JSON representation
- CreateSheetsChartRequest

- JSON representation
- LinkingMode
- CreateLineRequest

- JSON representation
- Category
- RefreshSheetsChartRequest

- JSON representation
- UpdateShapePropertiesRequest

- JSON representation
- UpdateImagePropertiesRequest

- JSON representation
- UpdateVideoPropertiesRequest

- JSON representation
- UpdatePagePropertiesRequest

- JSON representation
- UpdateTableCellPropertiesRequest

- JSON representation
- TableRange

- JSON representation
- UpdateLinePropertiesRequest

- JSON representation
- CreateParagraphBulletsRequest

- JSON representation
- BulletGlyphPreset
- ReplaceAllShapesWithImageRequest

- JSON representation
- ReplaceMethod
- ImageReplaceMethod
- DuplicateObjectRequest

- JSON representation
- UpdateTextStyleRequest

- JSON representation
- ReplaceAllShapesWithSheetsChartRequest

- JSON representation
- LinkingMode
- DeleteParagraphBulletsRequest

- JSON representation
- UpdateParagraphStyleRequest

- JSON representation
- UpdateTableBorderPropertiesRequest

- JSON representation
- BorderPosition
- UpdateTableColumnPropertiesRequest

- JSON representation
- UpdateTableRowPropertiesRequest

- JSON representation
- MergeTableCellsRequest

- JSON representation
- UnmergeTableCellsRequest

- JSON representation
- GroupObjectsRequest

- JSON representation
- UngroupObjectsRequest

- JSON representation
- UpdatePageElementAltTextRequest

- JSON representation
- ReplaceImageRequest

- JSON representation
- UpdateSlidePropertiesRequest

- JSON representation
- UpdatePageElementsZOrderRequest

- JSON representation
- ZOrderOperation
- UpdateLineCategoryRequest

- JSON representation
- RerouteLineRequest

- JSON representation
- WriteControl

- JSON representation
- Response

- JSON representation
- CreateSlideResponse

- JSON representation
- CreateShapeResponse

- JSON representation
- CreateTableResponse

- JSON representation
- ReplaceAllTextResponse

- JSON representation
- CreateImageResponse

- JSON representation
- CreateVideoResponse

- JSON representation
- CreateSheetsChartResponse

- JSON representation
- CreateLineResponse

- JSON representation
- ReplaceAllShapesWithImageResponse

- JSON representation
- DuplicateObjectResponse

- JSON representation
- ReplaceAllShapesWithSheetsChartResponse

- JSON representation
- GroupObjectsResponse

- JSON representation
- Try it!


Applies one or more updates to the presentation.


Each `request` is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied.


Some requests have `replies` to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.


For example, suppose you call batchUpdate with four updates, and only the third one returns information. The response would have two empty replies: the reply to the third request, and another empty reply, in that order.


Because other users may be editing the presentation, the presentation might not exactly reflect your changes: your changes may be altered with respect to collaborator changes. If there are no collaborators, the presentation should reflect your changes. In any case, the updates in your request are guaranteed to be applied together atomically.


### HTTP request


`POST https://slides.googleapis.com/v1/presentations/{presentationId}:batchUpdate`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| presentationId | string The presentation to apply the updates to. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "requests" : [ { object ( Request ) } ] , "writeControl" : { object ( WriteControl ) } } |


| Fields |
|---|
| requests[] | object ( Request ) A list of updates to apply to the presentation. |
| writeControl | object ( WriteControl ) Provides control over how write requests are executed. |


### Response body


Response message from a batch update.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "presentationId" : string , "replies" : [ { object ( Response ) } ] , "writeControl" : { object ( WriteControl ) } } |


| Fields |
|---|
| presentationId | string The presentation the updates were applied to. |
| replies[] | object ( Response ) The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty. |
| writeControl | object ( WriteControl ) The updated write control after applying the request. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/drive.readonly`
- `https://www.googleapis.com/auth/presentations`
- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/spreadsheets.readonly`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


## WriteControl


Provides control over how write requests are executed.


| JSON representation |
|---|
| { "requiredRevisionId" : string } |


| Fields |
|---|
| requiredRevisionId | string The revision ID of the presentation required for the write request. If specified and the required revision ID doesn't match the presentation's current revision ID, the request is not processed and returns a 400 bad request error. When a required revision ID is returned in a response, it indicates the revision ID of the document after the request was applied. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-20 UTC."],[],[]]