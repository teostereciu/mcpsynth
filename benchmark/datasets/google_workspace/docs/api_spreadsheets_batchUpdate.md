# Method: spreadsheets.batchUpdate

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/batchUpdate*

---

# Method: spreadsheets.batchUpdate


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- Request

- JSON representation
- UpdateSpreadsheetPropertiesRequest

- JSON representation
- UpdateSheetPropertiesRequest

- JSON representation
- UpdateDimensionPropertiesRequest

- JSON representation
- DataSourceSheetDimensionRange

- JSON representation
- UpdateNamedRangeRequest

- JSON representation
- RepeatCellRequest

- JSON representation
- AddNamedRangeRequest

- JSON representation
- DeleteNamedRangeRequest

- JSON representation
- AddSheetRequest

- JSON representation
- DeleteSheetRequest

- JSON representation
- AutoFillRequest

- JSON representation
- SourceAndDestination

- JSON representation
- CutPasteRequest

- JSON representation
- PasteType
- CopyPasteRequest

- JSON representation
- PasteOrientation
- MergeCellsRequest

- JSON representation
- MergeType
- UnmergeCellsRequest

- JSON representation
- UpdateBordersRequest

- JSON representation
- UpdateCellsRequest

- JSON representation
- AddFilterViewRequest

- JSON representation
- AppendCellsRequest

- JSON representation
- ClearBasicFilterRequest

- JSON representation
- DeleteDimensionRequest

- JSON representation
- DeleteEmbeddedObjectRequest

- JSON representation
- DeleteFilterViewRequest

- JSON representation
- DuplicateFilterViewRequest

- JSON representation
- DuplicateSheetRequest

- JSON representation
- FindReplaceRequest

- JSON representation
- InsertDimensionRequest

- JSON representation
- InsertRangeRequest

- JSON representation
- MoveDimensionRequest

- JSON representation
- UpdateEmbeddedObjectPositionRequest

- JSON representation
- PasteDataRequest

- JSON representation
- TextToColumnsRequest

- JSON representation
- DelimiterType
- UpdateFilterViewRequest

- JSON representation
- DeleteRangeRequest

- JSON representation
- AppendDimensionRequest

- JSON representation
- AddConditionalFormatRuleRequest

- JSON representation
- UpdateConditionalFormatRuleRequest

- JSON representation
- DeleteConditionalFormatRuleRequest

- JSON representation
- SortRangeRequest

- JSON representation
- SetDataValidationRequest

- JSON representation
- SetBasicFilterRequest

- JSON representation
- AddProtectedRangeRequest

- JSON representation
- UpdateProtectedRangeRequest

- JSON representation
- DeleteProtectedRangeRequest

- JSON representation
- AutoResizeDimensionsRequest

- JSON representation
- AddChartRequest

- JSON representation
- UpdateChartSpecRequest

- JSON representation
- UpdateBandingRequest

- JSON representation
- AddBandingRequest

- JSON representation
- DeleteBandingRequest

- JSON representation
- CreateDeveloperMetadataRequest

- JSON representation
- UpdateDeveloperMetadataRequest

- JSON representation
- DeleteDeveloperMetadataRequest

- JSON representation
- RandomizeRangeRequest

- JSON representation
- AddDimensionGroupRequest

- JSON representation
- DeleteDimensionGroupRequest

- JSON representation
- UpdateDimensionGroupRequest

- JSON representation
- TrimWhitespaceRequest

- JSON representation
- DeleteDuplicatesRequest

- JSON representation
- UpdateEmbeddedObjectBorderRequest

- JSON representation
- AddSlicerRequest

- JSON representation
- UpdateSlicerSpecRequest

- JSON representation
- AddDataSourceRequest

- JSON representation
- UpdateDataSourceRequest

- JSON representation
- DeleteDataSourceRequest

- JSON representation
- RefreshDataSourceRequest

- JSON representation
- DataSourceObjectReferences

- JSON representation
- DataSourceObjectReference

- JSON representation
- CancelDataSourceRefreshRequest

- JSON representation
- AddTableRequest

- JSON representation
- UpdateTableRequest

- JSON representation
- DeleteTableRequest

- JSON representation
- Response

- JSON representation
- AddNamedRangeResponse

- JSON representation
- AddSheetResponse

- JSON representation
- AddFilterViewResponse

- JSON representation
- DuplicateFilterViewResponse

- JSON representation
- DuplicateSheetResponse

- JSON representation
- FindReplaceResponse

- JSON representation
- UpdateEmbeddedObjectPositionResponse

- JSON representation
- UpdateConditionalFormatRuleResponse

- JSON representation
- DeleteConditionalFormatRuleResponse

- JSON representation
- AddProtectedRangeResponse

- JSON representation
- AddChartResponse

- JSON representation
- AddBandingResponse

- JSON representation
- CreateDeveloperMetadataResponse

- JSON representation
- UpdateDeveloperMetadataResponse

- JSON representation
- DeleteDeveloperMetadataResponse

- JSON representation
- AddDimensionGroupResponse

- JSON representation
- DeleteDimensionGroupResponse

- JSON representation
- TrimWhitespaceResponse

- JSON representation
- DeleteDuplicatesResponse

- JSON representation
- AddSlicerResponse

- JSON representation
- AddDataSourceResponse

- JSON representation
- UpdateDataSourceResponse

- JSON representation
- RefreshDataSourceResponse

- JSON representation
- RefreshDataSourceObjectExecutionStatus

- JSON representation
- CancelDataSourceRefreshResponse

- JSON representation
- CancelDataSourceRefreshStatus

- JSON representation
- RefreshCancellationStatus

- JSON representation
- RefreshCancellationState
- RefreshCancellationErrorCode
- AddTableResponse

- JSON representation
- Try it!


Applies one or more updates to the spreadsheet.


Each `request` is validated before being applied. If any request is not valid then the entire request will fail and nothing will be applied.


Some requests have `replies` to give you some information about how they are applied. The replies will mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the response will have 2 empty replies, the actual reply, and another empty reply, in that order.


Due to the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect exactly your changes after this completes, however it is guaranteed that the updates in the request will be applied together atomically. Your changes may be altered with respect to collaborator changes. If there are no collaborators, the spreadsheet should reflect your changes.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}:batchUpdate`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The spreadsheet to apply the updates to. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "requests" : [ { object ( Request ) } ] , "includeSpreadsheetInResponse" : boolean , "responseRanges" : [ string ] , "responseIncludeGridData" : boolean } |


| Fields |
|---|
| requests[] | object ( Request ) A list of updates to apply to the spreadsheet. Requests will be applied in the order they are specified. If any request is not valid, no requests will be applied. |
| includeSpreadsheetInResponse | boolean Determines if the update response should include the spreadsheet resource. |
| responseRanges[] | string Limits the ranges included in the response spreadsheet. Meaningful only if includeSpreadsheetInResponse is 'true'. |
| responseIncludeGridData | boolean True if grid data should be returned. Meaningful only if includeSpreadsheetInResponse is 'true'. This parameter is ignored if a field mask was set in the request. |


### Response body


The reply for batch updating a spreadsheet.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "replies" : [ { object ( Response ) } ] , "updatedSpreadsheet" : { object ( Spreadsheet ) } } |


| Fields |
|---|
| spreadsheetId | string The spreadsheet the updates were applied to. |
| replies[] | object ( Response ) The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty. |
| updatedSpreadsheet | object ( Spreadsheet ) The spreadsheet after updates were applied. This is only set if BatchUpdateSpreadsheetRequest.include_spreadsheet_in_response is true . |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]