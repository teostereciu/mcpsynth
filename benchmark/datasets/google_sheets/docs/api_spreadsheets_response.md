# Responses

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response*

---

# Responses


## Response


A single response from an update.


| JSON representation |
|---|
| { "addNamedRange" : { object ( AddNamedRangeResponse ) } , "addSheet" : { object ( AddSheetResponse ) } , "addFilterView" : { object ( AddFilterViewResponse ) } , "duplicateFilterView" : { object ( DuplicateFilterViewResponse ) } , "duplicateSheet" : { object ( DuplicateSheetResponse ) } , "findReplace" : { object ( FindReplaceResponse ) } , "updateEmbeddedObjectPosition" : { object ( UpdateEmbeddedObjectPositionResponse ) } , "updateConditionalFormatRule" : { object ( UpdateConditionalFormatRuleResponse ) } , "deleteConditionalFormatRule" : { object ( DeleteConditionalFormatRuleResponse ) } , "addProtectedRange" : { object ( AddProtectedRangeResponse ) } , "addChart" : { object ( AddChartResponse ) } , "addBanding" : { object ( AddBandingResponse ) } , "createDeveloperMetadata" : { object ( CreateDeveloperMetadataResponse ) } , "updateDeveloperMetadata" : { object ( UpdateDeveloperMetadataResponse ) } , "deleteDeveloperMetadata" : { object ( DeleteDeveloperMetadataResponse ) } , "addDimensionGroup" : { object ( AddDimensionGroupResponse ) } , "deleteDimensionGroup" : { object ( DeleteDimensionGroupResponse ) } , "trimWhitespace" : { object ( TrimWhitespaceResponse ) } , "deleteDuplicates" : { object ( DeleteDuplicatesResponse ) } , "addSlicer" : { object ( AddSlicerResponse ) } , "addDataSource" : { object ( AddDataSourceResponse ) } , "updateDataSource" : { object ( UpdateDataSourceResponse ) } , "refreshDataSource" : { object ( RefreshDataSourceResponse ) } , "cancelDataSourceRefresh" : { object ( CancelDataSourceRefreshResponse ) } , "addTable" : { object ( AddTableResponse ) } } |


| Fields |
|---|
| Union field kind . The kind of reply. May have no fields set if the request had no response. kind can be only one of the following: |
| addNamedRange | object ( AddNamedRangeResponse ) A reply from adding a named range. |
| addSheet | object ( AddSheetResponse ) A reply from adding a sheet. |
| addFilterView | object ( AddFilterViewResponse ) A reply from adding a filter view. |
| duplicateFilterView | object ( DuplicateFilterViewResponse ) A reply from duplicating a filter view. |
| duplicateSheet | object ( DuplicateSheetResponse ) A reply from duplicating a sheet. |
| findReplace | object ( FindReplaceResponse ) A reply from doing a find/replace. |
| updateEmbeddedObjectPosition | object ( UpdateEmbeddedObjectPositionResponse ) A reply from updating an embedded object's position. |
| updateConditionalFormatRule | object ( UpdateConditionalFormatRuleResponse ) A reply from updating a conditional format rule. |
| deleteConditionalFormatRule | object ( DeleteConditionalFormatRuleResponse ) A reply from deleting a conditional format rule. |
| addProtectedRange | object ( AddProtectedRangeResponse ) A reply from adding a protected range. |
| addChart | object ( AddChartResponse ) A reply from adding a chart. |
| addBanding | object ( AddBandingResponse ) A reply from adding a banded range. |
| createDeveloperMetadata | object ( CreateDeveloperMetadataResponse ) A reply from creating a developer metadata entry. |
| updateDeveloperMetadata | object ( UpdateDeveloperMetadataResponse ) A reply from updating a developer metadata entry. |
| deleteDeveloperMetadata | object ( DeleteDeveloperMetadataResponse ) A reply from deleting a developer metadata entry. |
| addDimensionGroup | object ( AddDimensionGroupResponse ) A reply from adding a dimension group. |
| deleteDimensionGroup | object ( DeleteDimensionGroupResponse ) A reply from deleting a dimension group. |
| trimWhitespace | object ( TrimWhitespaceResponse ) A reply from trimming whitespace. |
| deleteDuplicates | object ( DeleteDuplicatesResponse ) A reply from removing rows containing duplicate values. |
| addSlicer | object ( AddSlicerResponse ) A reply from adding a slicer. |
| addDataSource | object ( AddDataSourceResponse ) A reply from adding a data source. |
| updateDataSource | object ( UpdateDataSourceResponse ) A reply from updating a data source. |
| refreshDataSource | object ( RefreshDataSourceResponse ) A reply from refreshing data source objects. |
| cancelDataSourceRefresh | object ( CancelDataSourceRefreshResponse ) A reply from cancelling data source object refreshes. |
| addTable | object ( AddTableResponse ) A reply from adding a table. |


## AddNamedRangeResponse


The result of adding a named range.


| JSON representation |
|---|
| { "namedRange" : { object ( NamedRange ) } } |


| Fields |
|---|
| namedRange | object ( NamedRange ) The named range to add. |


## AddSheetResponse


The result of adding a sheet.


| JSON representation |
|---|
| { "properties" : { object ( SheetProperties ) } } |


| Fields |
|---|
| properties | object ( SheetProperties ) The properties of the newly added sheet. |


## AddFilterViewResponse


The result of adding a filter view.


| JSON representation |
|---|
| { "filter" : { object ( FilterView ) } } |


| Fields |
|---|
| filter | object ( FilterView ) The newly added filter view. |


## DuplicateFilterViewResponse


The result of a filter view being duplicated.


| JSON representation |
|---|
| { "filter" : { object ( FilterView ) } } |


| Fields |
|---|
| filter | object ( FilterView ) The newly created filter. |


## DuplicateSheetResponse


The result of duplicating a sheet.


| JSON representation |
|---|
| { "properties" : { object ( SheetProperties ) } } |


| Fields |
|---|
| properties | object ( SheetProperties ) The properties of the duplicate sheet. |


## FindReplaceResponse


The result of the find/replace.


| JSON representation |
|---|
| { "valuesChanged" : integer , "formulasChanged" : integer , "rowsChanged" : integer , "sheetsChanged" : integer , "occurrencesChanged" : integer } |


| Fields |
|---|
| valuesChanged | integer The number of non-formula cells changed. |
| formulasChanged | integer The number of formula cells changed. |
| rowsChanged | integer The number of rows changed. |
| sheetsChanged | integer The number of sheets changed. |
| occurrencesChanged | integer The number of occurrences (possibly multiple within a cell) changed. For example, if replacing "e" with "o" in "Google Sheets" , this would be "3" because "Google Sheets" -> "Googlo Shoots" . |


## UpdateEmbeddedObjectPositionResponse


The result of updating an embedded object's position.


| JSON representation |
|---|
| { "position" : { object ( EmbeddedObjectPosition ) } } |


| Fields |
|---|
| position | object ( EmbeddedObjectPosition ) The new position of the embedded object. |


## UpdateConditionalFormatRuleResponse


The result of updating a conditional format rule.


| JSON representation |
|---|
| { "newRule" : { object ( ConditionalFormatRule ) } , "newIndex" : integer , "oldRule" : { object ( ConditionalFormatRule ) } , "oldIndex" : integer } |


| Fields |
|---|
| newRule | object ( ConditionalFormatRule ) The new rule that replaced the old rule (if replacing), or the rule that was moved (if moved) |
| newIndex | integer The index of the new rule. |
| Union field old_info . Information about the prior rule. old_info can be only one of the following: |
| oldRule | object ( ConditionalFormatRule ) The old (deleted) rule. Not set if a rule was moved (because it is the same as newRule ). |
| oldIndex | integer The old index of the rule. Not set if a rule was replaced (because it is the same as newIndex ). |


## DeleteConditionalFormatRuleResponse


The result of deleting a conditional format rule.


| JSON representation |
|---|
| { "rule" : { object ( ConditionalFormatRule ) } } |


| Fields |
|---|
| rule | object ( ConditionalFormatRule ) The rule that was deleted. |


## AddProtectedRangeResponse


The result of adding a new protected range.


| JSON representation |
|---|
| { "protectedRange" : { object ( ProtectedRange ) } } |


| Fields |
|---|
| protectedRange | object ( ProtectedRange ) The newly added protected range. |


## AddChartResponse


The result of adding a chart to a spreadsheet.


| JSON representation |
|---|
| { "chart" : { object ( EmbeddedChart ) } } |


| Fields |
|---|
| chart | object ( EmbeddedChart ) The newly added chart. |


## AddBandingResponse


The result of adding a banded range.


| JSON representation |
|---|
| { "bandedRange" : { object ( BandedRange ) } } |


| Fields |
|---|
| bandedRange | object ( BandedRange ) The banded range that was added. |


## CreateDeveloperMetadataResponse


The response from creating developer metadata.


| JSON representation |
|---|
| { "developerMetadata" : { object ( DeveloperMetadata ) } } |


| Fields |
|---|
| developerMetadata | object ( DeveloperMetadata ) The developer metadata that was created. |


## UpdateDeveloperMetadataResponse


The response from updating developer metadata.


| JSON representation |
|---|
| { "developerMetadata" : [ { object ( DeveloperMetadata ) } ] } |


| Fields |
|---|
| developerMetadata[] | object ( DeveloperMetadata ) The updated developer metadata. |


## DeleteDeveloperMetadataResponse


The response from deleting developer metadata.


| JSON representation |
|---|
| { "deletedDeveloperMetadata" : [ { object ( DeveloperMetadata ) } ] } |


| Fields |
|---|
| deletedDeveloperMetadata[] | object ( DeveloperMetadata ) The metadata that was deleted. |


## AddDimensionGroupResponse


The result of adding a group.


| JSON representation |
|---|
| { "dimensionGroups" : [ { object ( DimensionGroup ) } ] } |


| Fields |
|---|
| dimensionGroups[] | object ( DimensionGroup ) All groups of a dimension after adding a group to that dimension. |


## DeleteDimensionGroupResponse


The result of deleting a group.


| JSON representation |
|---|
| { "dimensionGroups" : [ { object ( DimensionGroup ) } ] } |


| Fields |
|---|
| dimensionGroups[] | object ( DimensionGroup ) All groups of a dimension after deleting a group from that dimension. |


## TrimWhitespaceResponse


The result of trimming whitespace in cells.


| JSON representation |
|---|
| { "cellsChangedCount" : integer } |


| Fields |
|---|
| cellsChangedCount | integer The number of cells that were trimmed of whitespace. |


## DeleteDuplicatesResponse


The result of removing duplicates in a range.


| JSON representation |
|---|
| { "duplicatesRemovedCount" : integer } |


| Fields |
|---|
| duplicatesRemovedCount | integer The number of duplicate rows removed. |


## AddSlicerResponse


The result of adding a slicer to a spreadsheet.


| JSON representation |
|---|
| { "slicer" : { object ( Slicer ) } } |


| Fields |
|---|
| slicer | object ( Slicer ) The newly added slicer. |


## AddDataSourceResponse


The result of adding a data source.


| JSON representation |
|---|
| { "dataSource" : { object ( DataSource ) } , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| dataSource | object ( DataSource ) The data source that was created. |
| dataExecutionStatus | object ( DataExecutionStatus ) The data execution status. |


## UpdateDataSourceResponse


The response from updating data source.


| JSON representation |
|---|
| { "dataSource" : { object ( DataSource ) } , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| dataSource | object ( DataSource ) The updated data source. |
| dataExecutionStatus | object ( DataExecutionStatus ) The data execution status. |


## RefreshDataSourceResponse


The response from refreshing one or multiple data source objects.


| JSON representation |
|---|
| { "statuses" : [ { object ( RefreshDataSourceObjectExecutionStatus ) } ] } |


| Fields |
|---|
| statuses[] | object ( RefreshDataSourceObjectExecutionStatus ) All the refresh status for the data source object references specified in the request. If isAll is specified, the field contains only those in failure status. |


## RefreshDataSourceObjectExecutionStatus


The execution status of refreshing one data source object.


| JSON representation |
|---|
| { "reference" : { object ( DataSourceObjectReference ) } , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| reference | object ( DataSourceObjectReference ) Reference to a data source object being refreshed. |
| dataExecutionStatus | object ( DataExecutionStatus ) The data execution status. |


## CancelDataSourceRefreshResponse


The response from cancelling one or multiple data source object refreshes.


| JSON representation |
|---|
| { "statuses" : [ { object ( CancelDataSourceRefreshStatus ) } ] } |


| Fields |
|---|
| statuses[] | object ( CancelDataSourceRefreshStatus ) The cancellation statuses of refreshes of all data source objects specified in the request. If isAll is specified, the field contains only those in failure status. Refreshing and canceling refresh the same data source object is also not allowed in the same batchUpdate . |


## CancelDataSourceRefreshStatus


The status of cancelling a single data source object refresh.


| JSON representation |
|---|
| { "reference" : { object ( DataSourceObjectReference ) } , "refreshCancellationStatus" : { object ( RefreshCancellationStatus ) } } |


| Fields |
|---|
| reference | object ( DataSourceObjectReference ) Reference to the data source object whose refresh is being cancelled. |
| refreshCancellationStatus | object ( RefreshCancellationStatus ) The cancellation status. |


## RefreshCancellationStatus


The status of a refresh cancellation.


You can send a
   `cancel request`
   to explicitly cancel one or multiple data source object refreshes.


| JSON representation |
|---|
| { "state" : enum ( RefreshCancellationState ) , "errorCode" : enum ( RefreshCancellationErrorCode ) } |


| Fields |
|---|
| state | enum ( RefreshCancellationState ) The state of a call to cancel a refresh in Sheets. |
| errorCode | enum ( RefreshCancellationErrorCode ) The error code. |


## RefreshCancellationState


An enumeration of refresh cancellation states.


| Enums |
|---|
| REFRESH_CANCELLATION_STATE_UNSPECIFIED | Default value, do not use. |
| CANCEL_SUCCEEDED | The API call to Sheets to cancel a refresh has succeeded. This does not mean that the cancel happened successfully, but that the call has been made successfully. |
| CANCEL_FAILED | The API call to Sheets to cancel a refresh has failed. |


## RefreshCancellationErrorCode


An enumeration of the refresh cancellation error codes.


| Enums |
|---|
| REFRESH_CANCELLATION_ERROR_CODE_UNSPECIFIED | Default value, do not use. |
| EXECUTION_NOT_FOUND | Execution to be cancelled not found in the query engine or in Sheets. |
| CANCEL_PERMISSION_DENIED | The user does not have permission to cancel the query. |
| QUERY_EXECUTION_COMPLETED | The query execution has already completed and thus could not be cancelled. |
| CONCURRENT_CANCELLATION | There is already another cancellation in process. |
| CANCEL_OTHER_ERROR | All other errors. |


## AddTableResponse


The result of adding a table.


| JSON representation |
|---|
| { "table" : { object ( Table ) } } |


| Fields |
|---|
| table | object ( Table ) Output only. The table that was added. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]