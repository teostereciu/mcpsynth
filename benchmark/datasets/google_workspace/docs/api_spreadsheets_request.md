# Requests

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request*

---

# Requests


## Request


A single kind of update to apply to a spreadsheet.


| JSON representation |
|---|
| { "updateSpreadsheetProperties" : { object ( UpdateSpreadsheetPropertiesRequest ) } , "updateSheetProperties" : { object ( UpdateSheetPropertiesRequest ) } , "updateDimensionProperties" : { object ( UpdateDimensionPropertiesRequest ) } , "updateNamedRange" : { object ( UpdateNamedRangeRequest ) } , "repeatCell" : { object ( RepeatCellRequest ) } , "addNamedRange" : { object ( AddNamedRangeRequest ) } , "deleteNamedRange" : { object ( DeleteNamedRangeRequest ) } , "addSheet" : { object ( AddSheetRequest ) } , "deleteSheet" : { object ( DeleteSheetRequest ) } , "autoFill" : { object ( AutoFillRequest ) } , "cutPaste" : { object ( CutPasteRequest ) } , "copyPaste" : { object ( CopyPasteRequest ) } , "mergeCells" : { object ( MergeCellsRequest ) } , "unmergeCells" : { object ( UnmergeCellsRequest ) } , "updateBorders" : { object ( UpdateBordersRequest ) } , "updateCells" : { object ( UpdateCellsRequest ) } , "addFilterView" : { object ( AddFilterViewRequest ) } , "appendCells" : { object ( AppendCellsRequest ) } , "clearBasicFilter" : { object ( ClearBasicFilterRequest ) } , "deleteDimension" : { object ( DeleteDimensionRequest ) } , "deleteEmbeddedObject" : { object ( DeleteEmbeddedObjectRequest ) } , "deleteFilterView" : { object ( DeleteFilterViewRequest ) } , "duplicateFilterView" : { object ( DuplicateFilterViewRequest ) } , "duplicateSheet" : { object ( DuplicateSheetRequest ) } , "findReplace" : { object ( FindReplaceRequest ) } , "insertDimension" : { object ( InsertDimensionRequest ) } , "insertRange" : { object ( InsertRangeRequest ) } , "moveDimension" : { object ( MoveDimensionRequest ) } , "updateEmbeddedObjectPosition" : { object ( UpdateEmbeddedObjectPositionRequest ) } , "pasteData" : { object ( PasteDataRequest ) } , "textToColumns" : { object ( TextToColumnsRequest ) } , "updateFilterView" : { object ( UpdateFilterViewRequest ) } , "deleteRange" : { object ( DeleteRangeRequest ) } , "appendDimension" : { object ( AppendDimensionRequest ) } , "addConditionalFormatRule" : { object ( AddConditionalFormatRuleRequest ) } , "updateConditionalFormatRule" : { object ( UpdateConditionalFormatRuleRequest ) } , "deleteConditionalFormatRule" : { object ( DeleteConditionalFormatRuleRequest ) } , "sortRange" : { object ( SortRangeRequest ) } , "setDataValidation" : { object ( SetDataValidationRequest ) } , "setBasicFilter" : { object ( SetBasicFilterRequest ) } , "addProtectedRange" : { object ( AddProtectedRangeRequest ) } , "updateProtectedRange" : { object ( UpdateProtectedRangeRequest ) } , "deleteProtectedRange" : { object ( DeleteProtectedRangeRequest ) } , "autoResizeDimensions" : { object ( AutoResizeDimensionsRequest ) } , "addChart" : { object ( AddChartRequest ) } , "updateChartSpec" : { object ( UpdateChartSpecRequest ) } , "updateBanding" : { object ( UpdateBandingRequest ) } , "addBanding" : { object ( AddBandingRequest ) } , "deleteBanding" : { object ( DeleteBandingRequest ) } , "createDeveloperMetadata" : { object ( CreateDeveloperMetadataRequest ) } , "updateDeveloperMetadata" : { object ( UpdateDeveloperMetadataRequest ) } , "deleteDeveloperMetadata" : { object ( DeleteDeveloperMetadataRequest ) } , "randomizeRange" : { object ( RandomizeRangeRequest ) } , "addDimensionGroup" : { object ( AddDimensionGroupRequest ) } , "deleteDimensionGroup" : { object ( DeleteDimensionGroupRequest ) } , "updateDimensionGroup" : { object ( UpdateDimensionGroupRequest ) } , "trimWhitespace" : { object ( TrimWhitespaceRequest ) } , "deleteDuplicates" : { object ( DeleteDuplicatesRequest ) } , "updateEmbeddedObjectBorder" : { object ( UpdateEmbeddedObjectBorderRequest ) } , "addSlicer" : { object ( AddSlicerRequest ) } , "updateSlicerSpec" : { object ( UpdateSlicerSpecRequest ) } , "addDataSource" : { object ( AddDataSourceRequest ) } , "updateDataSource" : { object ( UpdateDataSourceRequest ) } , "deleteDataSource" : { object ( DeleteDataSourceRequest ) } , "refreshDataSource" : { object ( RefreshDataSourceRequest ) } , "cancelDataSourceRefresh" : { object ( CancelDataSourceRefreshRequest ) } , "addTable" : { object ( AddTableRequest ) } , "updateTable" : { object ( UpdateTableRequest ) } , "deleteTable" : { object ( DeleteTableRequest ) } } |


| Fields |
|---|
| Union field kind . The kind of update. Exactly one field is required. kind can be only one of the following: |
| updateSpreadsheetProperties | object ( UpdateSpreadsheetPropertiesRequest ) Updates the spreadsheet's properties. |
| updateSheetProperties | object ( UpdateSheetPropertiesRequest ) Updates a sheet's properties. |
| updateDimensionProperties | object ( UpdateDimensionPropertiesRequest ) Updates dimensions' properties. |
| updateNamedRange | object ( UpdateNamedRangeRequest ) Updates a named range. |
| repeatCell | object ( RepeatCellRequest ) Repeats a single cell across a range. |
| addNamedRange | object ( AddNamedRangeRequest ) Adds a named range. |
| deleteNamedRange | object ( DeleteNamedRangeRequest ) Deletes a named range. |
| addSheet | object ( AddSheetRequest ) Adds a sheet. |
| deleteSheet | object ( DeleteSheetRequest ) Deletes a sheet. |
| autoFill | object ( AutoFillRequest ) Automatically fills in more data based on existing data. |
| cutPaste | object ( CutPasteRequest ) Cuts data from one area and pastes it to another. |
| copyPaste | object ( CopyPasteRequest ) Copies data from one area and pastes it to another. |
| mergeCells | object ( MergeCellsRequest ) Merges cells together. |
| unmergeCells | object ( UnmergeCellsRequest ) Unmerges merged cells. |
| updateBorders | object ( UpdateBordersRequest ) Updates the borders in a range of cells. |
| updateCells | object ( UpdateCellsRequest ) Updates many cells at once. |
| addFilterView | object ( AddFilterViewRequest ) Adds a filter view. |
| appendCells | object ( AppendCellsRequest ) Appends cells after the last row with data in a sheet. |
| clearBasicFilter | object ( ClearBasicFilterRequest ) Clears the basic filter on a sheet. |
| deleteDimension | object ( DeleteDimensionRequest ) Deletes rows or columns in a sheet. |
| deleteEmbeddedObject | object ( DeleteEmbeddedObjectRequest ) Deletes an embedded object (e.g, chart, image) in a sheet. |
| deleteFilterView | object ( DeleteFilterViewRequest ) Deletes a filter view from a sheet. |
| duplicateFilterView | object ( DuplicateFilterViewRequest ) Duplicates a filter view. |
| duplicateSheet | object ( DuplicateSheetRequest ) Duplicates a sheet. |
| findReplace | object ( FindReplaceRequest ) Finds and replaces occurrences of some text with other text. |
| insertDimension | object ( InsertDimensionRequest ) Inserts new rows or columns in a sheet. |
| insertRange | object ( InsertRangeRequest ) Inserts new cells in a sheet, shifting the existing cells. |
| moveDimension | object ( MoveDimensionRequest ) Moves rows or columns to another location in a sheet. |
| updateEmbeddedObjectPosition | object ( UpdateEmbeddedObjectPositionRequest ) Updates an embedded object's (e.g. chart, image) position. |
| pasteData | object ( PasteDataRequest ) Pastes data (HTML or delimited) into a sheet. |
| textToColumns | object ( TextToColumnsRequest ) Converts a column of text into many columns of text. |
| updateFilterView | object ( UpdateFilterViewRequest ) Updates the properties of a filter view. |
| deleteRange | object ( DeleteRangeRequest ) Deletes a range of cells from a sheet, shifting the remaining cells. |
| appendDimension | object ( AppendDimensionRequest ) Appends dimensions to the end of a sheet. |
| addConditionalFormatRule | object ( AddConditionalFormatRuleRequest ) Adds a new conditional format rule. |
| updateConditionalFormatRule | object ( UpdateConditionalFormatRuleRequest ) Updates an existing conditional format rule. |
| deleteConditionalFormatRule | object ( DeleteConditionalFormatRuleRequest ) Deletes an existing conditional format rule. |
| sortRange | object ( SortRangeRequest ) Sorts data in a range. |
| setDataValidation | object ( SetDataValidationRequest ) Sets data validation for one or more cells. |
| setBasicFilter | object ( SetBasicFilterRequest ) Sets the basic filter on a sheet. |
| addProtectedRange | object ( AddProtectedRangeRequest ) Adds a protected range. |
| updateProtectedRange | object ( UpdateProtectedRangeRequest ) Updates a protected range. |
| deleteProtectedRange | object ( DeleteProtectedRangeRequest ) Deletes a protected range. |
| autoResizeDimensions | object ( AutoResizeDimensionsRequest ) Automatically resizes one or more dimensions based on the contents of the cells in that dimension. |
| addChart | object ( AddChartRequest ) Adds a chart. |
| updateChartSpec | object ( UpdateChartSpecRequest ) Updates a chart's specifications. |
| updateBanding | object ( UpdateBandingRequest ) Updates a banded range |
| addBanding | object ( AddBandingRequest ) Adds a new banded range |
| deleteBanding | object ( DeleteBandingRequest ) Removes a banded range |
| createDeveloperMetadata | object ( CreateDeveloperMetadataRequest ) Creates new developer metadata |
| updateDeveloperMetadata | object ( UpdateDeveloperMetadataRequest ) Updates an existing developer metadata entry |
| deleteDeveloperMetadata | object ( DeleteDeveloperMetadataRequest ) Deletes developer metadata |
| randomizeRange | object ( RandomizeRangeRequest ) Randomizes the order of the rows in a range. |
| addDimensionGroup | object ( AddDimensionGroupRequest ) Creates a group over the specified range. |
| deleteDimensionGroup | object ( DeleteDimensionGroupRequest ) Deletes a group over the specified range. |
| updateDimensionGroup | object ( UpdateDimensionGroupRequest ) Updates the state of the specified group. |
| trimWhitespace | object ( TrimWhitespaceRequest ) Trims cells of whitespace (such as spaces, tabs, or new lines). |
| deleteDuplicates | object ( DeleteDuplicatesRequest ) Removes rows containing duplicate values in specified columns of a cell range. |
| updateEmbeddedObjectBorder | object ( UpdateEmbeddedObjectBorderRequest ) Updates an embedded object's border. |
| addSlicer | object ( AddSlicerRequest ) Adds a slicer. |
| updateSlicerSpec | object ( UpdateSlicerSpecRequest ) Updates a slicer's specifications. |
| addDataSource | object ( AddDataSourceRequest ) Adds a data source. |
| updateDataSource | object ( UpdateDataSourceRequest ) Updates a data source. |
| deleteDataSource | object ( DeleteDataSourceRequest ) Deletes a data source. |
| refreshDataSource | object ( RefreshDataSourceRequest ) Refreshes one or multiple data sources and associated dbobjects. |
| cancelDataSourceRefresh | object ( CancelDataSourceRefreshRequest ) Cancels refreshes of one or multiple data sources and associated dbobjects. |
| addTable | object ( AddTableRequest ) Adds a table. |
| updateTable | object ( UpdateTableRequest ) Updates a table. |
| deleteTable | object ( DeleteTableRequest ) A request for deleting a table. |


## UpdateSpreadsheetPropertiesRequest


Updates properties of a spreadsheet.


| JSON representation |
|---|
| { "properties" : { object ( SpreadsheetProperties ) } , "fields" : string } |


| Fields |
|---|
| properties | object ( SpreadsheetProperties ) The properties to update. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root 'properties' is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## UpdateSheetPropertiesRequest


Updates properties of the sheet with the specified
   `sheetId`.


| JSON representation |
|---|
| { "properties" : { object ( SheetProperties ) } , "fields" : string } |


| Fields |
|---|
| properties | object ( SheetProperties ) The properties to update. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root properties is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## UpdateDimensionPropertiesRequest


Updates properties of dimensions within the specified range.


| JSON representation |
|---|
| { "properties" : { object ( DimensionProperties ) } , "fields" : string , "range" : { object ( DimensionRange ) } , "dataSourceSheetRange" : { object ( DataSourceSheetDimensionRange ) } } |


| Fields |
|---|
| properties | object ( DimensionProperties ) Properties to update. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root properties is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |
| Union field dimension_range . The dimension range. dimension_range can be only one of the following: |
| range | object ( DimensionRange ) The rows or columns to update. |
| dataSourceSheetRange | object ( DataSourceSheetDimensionRange ) The columns on a data source sheet to update. |


## DataSourceSheetDimensionRange


A range along a single dimension on a
   `DATA_SOURCE`
   sheet.


| JSON representation |
|---|
| { "sheetId" : integer , "columnReferences" : [ { object ( DataSourceColumnReference ) } ] } |


| Fields |
|---|
| sheetId | integer The ID of the data source sheet the range is on. |
| columnReferences[] | object ( DataSourceColumnReference ) The columns on the data source sheet. |


## UpdateNamedRangeRequest


Updates properties of the named range with the specified
   `namedRangeId`.


| JSON representation |
|---|
| { "namedRange" : { object ( NamedRange ) } , "fields" : string } |


| Fields |
|---|
| namedRange | object ( NamedRange ) The named range to update with the new properties. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root namedRange is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## RepeatCellRequest


Updates all cells in the range to the values in the given Cell object. Only the fields listed in the
   `fields`
   field are updated; others are unchanged.


If writing a cell with a formula, the formula's ranges will automatically increment for each field in the range. For example, if writing a cell with formula
   `=A1`
   into range B2:C4, B2 would be
   `=A1`, B3 would be
   `=A2`, B4 would be
   `=A3`, C2 would be
   `=B1`, C3 would be
   `=B2`, C4 would be
   `=B3`.


To keep the formula's ranges static, use the
   `$`
   indicator. For example, use the formula
   `=$A$1`
   to prevent both the row and the column from incrementing.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "cell" : { object ( CellData ) } , "fields" : string } |


| Fields |
|---|
| range | object ( GridRange ) The range to repeat the cell in. |
| cell | object ( CellData ) The data to write. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root cell is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## AddNamedRangeRequest


Adds a named range to the spreadsheet.


| JSON representation |
|---|
| { "namedRange" : { object ( NamedRange ) } } |


| Fields |
|---|
| namedRange | object ( NamedRange ) The named range to add. The namedRangeId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a range that already exists.) |


## DeleteNamedRangeRequest


Removes the named range with the given ID from the spreadsheet.


| JSON representation |
|---|
| { "namedRangeId" : string } |


| Fields |
|---|
| namedRangeId | string The ID of the named range to delete. |


## AddSheetRequest


Adds a new sheet. When a sheet is added at a given index, all subsequent sheets' indexes are incremented. To add an object sheet, use
   `AddChartRequest`
   instead and specify
   `EmbeddedObjectPosition.sheetId`
   or
   `EmbeddedObjectPosition.newSheet`.


| JSON representation |
|---|
| { "properties" : { object ( SheetProperties ) } } |


| Fields |
|---|
| properties | object ( SheetProperties ) The properties the new sheet should have. All properties are optional. The sheetId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a sheet that already exists.) |


## DeleteSheetRequest


Deletes the requested sheet.


| JSON representation |
|---|
| { "sheetId" : integer } |


| Fields |
|---|
| sheetId | integer The ID of the sheet to delete. If the sheet is of DATA_SOURCE type, the associated DataSource is also deleted. |


## AutoFillRequest


Fills in more data based on existing data.


| JSON representation |
|---|
| { "useAlternateSeries" : boolean , "range" : { object ( GridRange ) } , "sourceAndDestination" : { object ( SourceAndDestination ) } } |


| Fields |
|---|
| useAlternateSeries | boolean True if we should generate data with the "alternate" series. This differs based on the type and amount of source data. |
| Union field area . The area to autofill. area can be only one of the following: |
| range | object ( GridRange ) The range to autofill. This will examine the range and detect the location that has data and automatically fill that data in to the rest of the range. |
| sourceAndDestination | object ( SourceAndDestination ) The source and destination areas to autofill. This explicitly lists the source of the autofill and where to extend that data. |


## SourceAndDestination


A combination of a source range and how to extend that source.


| JSON representation |
|---|
| { "source" : { object ( GridRange ) } , "dimension" : enum ( Dimension ) , "fillLength" : integer } |


| Fields |
|---|
| source | object ( GridRange ) The location of the data to use as the source of the autofill. |
| dimension | enum ( Dimension ) The dimension that data should be filled into. |
| fillLength | integer The number of rows or columns that data should be filled into. Positive numbers expand beyond the last row or last column of the source. Negative numbers expand before the first row or first column of the source. |


## CutPasteRequest


Moves data from the source to the destination.


| JSON representation |
|---|
| { "source" : { object ( GridRange ) } , "destination" : { object ( GridCoordinate ) } , "pasteType" : enum ( PasteType ) } |


| Fields |
|---|
| source | object ( GridRange ) The source data to cut. |
| destination | object ( GridCoordinate ) The top-left coordinate where the data should be pasted. |
| pasteType | enum ( PasteType ) What kind of data to paste. All the source data will be cut, regardless of what is pasted. |


## PasteType


What kind of data should be pasted.


| Enums |
|---|
| PASTE_NORMAL | Paste values, formulas, formats, and merges. |
| PASTE_VALUES | Paste the values ONLY without formats, formulas, or merges. |
| PASTE_FORMAT | Paste the format and data validation only. |
| PASTE_NO_BORDERS | Like PASTE_NORMAL but without borders. |
| PASTE_FORMULA | Paste the formulas only. |
| PASTE_DATA_VALIDATION | Paste the data validation only. |
| PASTE_CONDITIONAL_FORMATTING | Paste the conditional formatting rules only. |


## CopyPasteRequest


Copies data from the source to the destination.


| JSON representation |
|---|
| { "source" : { object ( GridRange ) } , "destination" : { object ( GridRange ) } , "pasteType" : enum ( PasteType ) , "pasteOrientation" : enum ( PasteOrientation ) } |


| Fields |
|---|
| source | object ( GridRange ) The source range to copy. |
| destination | object ( GridRange ) The location to paste to. If the range covers a span that's a multiple of the source's height or width, then the data will be repeated to fill in the destination range. If the range is smaller than the source range, the entire source data will still be copied (beyond the end of the destination range). |
| pasteType | enum ( PasteType ) What kind of data to paste. |
| pasteOrientation | enum ( PasteOrientation ) How that data should be oriented when pasting. |


## PasteOrientation


How a paste operation should be performed.


| Enums |
|---|
| NORMAL | Paste normally. |
| TRANSPOSE | Paste transposed, where all rows become columns and vice versa. |


## MergeCellsRequest


Merges all cells in the range.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "mergeType" : enum ( MergeType ) } |


| Fields |
|---|
| range | object ( GridRange ) The range of cells to merge. |
| mergeType | enum ( MergeType ) How the cells should be merged. |


## MergeType


The type of merge to create.


| Enums |
|---|
| MERGE_ALL | Create a single merge from the range |
| MERGE_COLUMNS | Create a merge for each column in the range |
| MERGE_ROWS | Create a merge for each row in the range |


## UnmergeCellsRequest


Unmerges cells in the given range.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } } |


| Fields |
|---|
| range | object ( GridRange ) The range within which all cells should be unmerged. If the range spans multiple merges, all will be unmerged. The range must not partially span any merge. |


## UpdateBordersRequest


Updates the borders of a range. If a field is not set in the request, that means the border remains as-is. For example, with two subsequent UpdateBordersRequest:


1. range: A1:A5
    `{ top: RED, bottom: WHITE }`
2. range: A1:A5
    `{ left: BLUE }`


That would result in A1:A5 having a borders of
   `{ top: RED, bottom: WHITE, left: BLUE }`. If you want to clear a border, explicitly set the style to
   `NONE`.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "top" : { object ( Border ) } , "bottom" : { object ( Border ) } , "left" : { object ( Border ) } , "right" : { object ( Border ) } , "innerHorizontal" : { object ( Border ) } , "innerVertical" : { object ( Border ) } } |


| Fields |
|---|
| range | object ( GridRange ) The range whose borders should be updated. |
| top | object ( Border ) The border to put at the top of the range. |
| bottom | object ( Border ) The border to put at the bottom of the range. |
| left | object ( Border ) The border to put at the left of the range. |
| right | object ( Border ) The border to put at the right of the range. |
| innerHorizontal | object ( Border ) The horizontal border to put within the range. |
| innerVertical | object ( Border ) The vertical border to put within the range. |


## UpdateCellsRequest


Updates all cells in a range with new data.


| JSON representation |
|---|
| { "rows" : [ { object ( RowData ) } ] , "fields" : string , "start" : { object ( GridCoordinate ) } , "range" : { object ( GridRange ) } } |


| Fields |
|---|
| rows[] | object ( RowData ) The data to write. |
| fields | string ( FieldMask format) The fields of CellData that should be updated. At least one field must be specified. The root is the CellData; 'row.values.' should not be specified. A single "*" can be used as short-hand for listing every field. |
| Union field area . The location data should be written. Exactly one value must be set. area can be only one of the following: |
| start | object ( GridCoordinate ) The coordinate to start writing data at. Any number of rows and columns (including a different number of columns per row) may be written. |
| range | object ( GridRange ) The range to write data to. If the data in rows does not cover the entire requested range, the fields matching those set in fields will be cleared. |


## AddFilterViewRequest


Adds a filter view.


| JSON representation |
|---|
| { "filter" : { object ( FilterView ) } } |


| Fields |
|---|
| filter | object ( FilterView ) The filter to add. The filterViewId field is optional. If one is not set, an ID will be randomly generated. (It is an error to specify the ID of a filter that already exists.) |


## AppendCellsRequest


Adds new cells after the last row with data in a sheet, inserting new rows into the sheet if necessary.


| JSON representation |
|---|
| { "sheetId" : integer , "rows" : [ { object ( RowData ) } ] , "fields" : string , "tableId" : string } |


| Fields |
|---|
| sheetId | integer The sheet ID to append the data to. |
| rows[] | object ( RowData ) The data to append. |
| fields | string ( FieldMask format) The fields of CellData that should be updated. At least one field must be specified. The root is the CellData; 'row.values.' should not be specified. A single "*" can be used as short-hand for listing every field. |
| Union field area . The location data should be written. area can be only one of the following: |
| tableId | string The ID of the table to append data to. The data will be only appended to the table body. This field also takes precedence over the sheetId field. |


## ClearBasicFilterRequest


Clears the basic filter, if any exists on the sheet.


| JSON representation |
|---|
| { "sheetId" : integer } |


| Fields |
|---|
| sheetId | integer The sheet ID on which the basic filter should be cleared. |


## DeleteDimensionRequest


Deletes the dimensions from the sheet.


| JSON representation |
|---|
| { "range" : { object ( DimensionRange ) } } |


| Fields |
|---|
| range | object ( DimensionRange ) The dimensions to delete from the sheet. |


## DeleteEmbeddedObjectRequest


Deletes the embedded object with the given ID.


| JSON representation |
|---|
| { "objectId" : integer } |


| Fields |
|---|
| objectId | integer The ID of the embedded object to delete. |


## DeleteFilterViewRequest


Deletes a particular filter view.


| JSON representation |
|---|
| { "filterId" : integer } |


| Fields |
|---|
| filterId | integer The ID of the filter to delete. |


## DuplicateFilterViewRequest


Duplicates a particular filter view.


| JSON representation |
|---|
| { "filterId" : integer } |


| Fields |
|---|
| filterId | integer The ID of the filter being duplicated. |


## DuplicateSheetRequest


Duplicates the contents of a sheet.


| JSON representation |
|---|
| { "sourceSheetId" : integer , "insertSheetIndex" : integer , "newSheetId" : integer , "newSheetName" : string } |


| Fields |
|---|
| sourceSheetId | integer The sheet to duplicate. If the source sheet is of DATA_SOURCE type, its backing DataSource is also duplicated and associated with the new copy of the sheet. No data execution is triggered, the grid data of this sheet is also copied over but only available after the batch request completes. |
| insertSheetIndex | integer The zero-based index where the new sheet should be inserted. The index of all sheets after this are incremented. |
| newSheetId | integer If set, the ID of the new sheet. If not set, an ID is chosen. If set, the ID must not conflict with any existing sheet ID. If set, it must be non-negative. |
| newSheetName | string The name of the new sheet. If empty, a new name is chosen for you. |


## FindReplaceRequest


Finds and replaces data in cells over a range, sheet, or all sheets.


| JSON representation |
|---|
| { "find" : string , "replacement" : string , "matchCase" : boolean , "matchEntireCell" : boolean , "searchByRegex" : boolean , "includeFormulas" : boolean , "range" : { object ( GridRange ) } , "sheetId" : integer , "allSheets" : boolean } |


| Fields |
|---|
| find | string The value to search. |
| replacement | string The value to use as the replacement. |
| matchCase | boolean True if the search is case sensitive. |
| matchEntireCell | boolean True if the find value should match the entire cell. |
| searchByRegex | boolean True if the find value is a regex. The regular expression and replacement should follow Java regex rules at https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html . The replacement string is allowed to refer to capturing groups. For example, if one cell has the contents "Google Sheets" and another has "Google Docs" , then searching for "o.* (.*)" with a replacement of "$1 Rocks" would change the contents of the cells to "GSheets Rocks" and "GDocs Rocks" respectively. |
| includeFormulas | boolean True if the search should include cells with formulas. False to skip cells with formulas. |
| Union field scope . The scope over which to find/replace -- one and only one must be set. scope can be only one of the following: |
| range | object ( GridRange ) The range to find/replace over. |
| sheetId | integer The sheet to find/replace over. |
| allSheets | boolean True to find/replace over all sheets. |


## InsertDimensionRequest


Inserts rows or columns in a sheet at a particular index.


| JSON representation |
|---|
| { "range" : { object ( DimensionRange ) } , "inheritFromBefore" : boolean } |


| Fields |
|---|
| range | object ( DimensionRange ) The dimensions to insert. Both the start and end indexes must be bounded. |
| inheritFromBefore | boolean Whether dimension properties should be extended from the dimensions before or after the newly inserted dimensions. True to inherit from the dimensions before (in which case the start index must be greater than 0), and false to inherit from the dimensions after. For example, if row index 0 has red background and row index 1 has a green background, then inserting 2 rows at index 1 can inherit either the green or red background. If inheritFromBefore is true, the two new rows will be red (because the row before the insertion point was red), whereas if inheritFromBefore is false, the two new rows will be green (because the row after the insertion point was green). |


## InsertRangeRequest


Inserts cells into a range, shifting the existing cells over or down.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "shiftDimension" : enum ( Dimension ) } |


| Fields |
|---|
| range | object ( GridRange ) The range to insert new cells into. The range is constrained to the current sheet boundaries. |
| shiftDimension | enum ( Dimension ) The dimension which will be shifted when inserting cells. If ROWS , existing cells will be shifted down. If COLUMNS , existing cells will be shifted right. |


## MoveDimensionRequest


Moves one or more rows or columns.


| JSON representation |
|---|
| { "source" : { object ( DimensionRange ) } , "destinationIndex" : integer } |


| Fields |
|---|
| source | object ( DimensionRange ) The source dimensions to move. |
| destinationIndex | integer The zero-based start index of where to move the source data to, based on the coordinates before the source data is removed from the grid. Existing data will be shifted down or right (depending on the dimension) to make room for the moved dimensions. The source dimensions are removed from the grid, so the the data may end up in a different index than specified. For example, given A1..A5 of 0, 1, 2, 3, 4 and wanting to move "1" and "2" to between "3" and "4" , the source would be ROWS [1..3) ,and the destination index would be "4" (the zero-based index of row 5). The end result would be A1..A5 of 0, 3, 1, 2, 4 . |


## UpdateEmbeddedObjectPositionRequest


Update an embedded object's position (such as a moving or resizing a chart or image).


| JSON representation |
|---|
| { "objectId" : integer , "newPosition" : { object ( EmbeddedObjectPosition ) } , "fields" : string } |


| Fields |
|---|
| objectId | integer The ID of the object to moved. |
| newPosition | object ( EmbeddedObjectPosition ) An explicit position to move the embedded object to. If newPosition.sheetId is set, a new sheet with that ID will be created. If newPosition.newSheet is set to true, a new sheet will be created with an ID that will be chosen for you. |
| fields | string ( FieldMask format) The fields of OverlayPosition that should be updated when setting a new position. Used only if newPosition.overlayPosition is set, in which case at least one field must be specified. The root newPosition.overlayPosition is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## PasteDataRequest


Inserts data into the spreadsheet starting at the specified coordinate.


| JSON representation |
|---|
| { "coordinate" : { object ( GridCoordinate ) } , "data" : string , "type" : enum ( PasteType ) , "delimiter" : string , "html" : boolean } |


| Fields |
|---|
| coordinate | object ( GridCoordinate ) The coordinate at which the data should start being inserted. |
| data | string The data to insert. |
| type | enum ( PasteType ) How the data should be pasted. |
| Union field kind . How to interpret the data, exactly one value must be set. kind can be only one of the following: |
| delimiter | string The delimiter in the data. |
| html | boolean True if the data is HTML. |


## TextToColumnsRequest


Splits a column of text into multiple columns, based on a delimiter in each cell.


| JSON representation |
|---|
| { "source" : { object ( GridRange ) } , "delimiter" : string , "delimiterType" : enum ( DelimiterType ) } |


| Fields |
|---|
| source | object ( GridRange ) The source data range. This must span exactly one column. |
| delimiter | string The delimiter to use. Used only if delimiterType is CUSTOM . |
| delimiterType | enum ( DelimiterType ) The delimiter type to use. |


## DelimiterType


The delimiter to split on.


| Enums |
|---|
| DELIMITER_TYPE_UNSPECIFIED | Default value. This value must not be used. |
| COMMA | "," |
| SEMICOLON | ";" |
| PERIOD | "." |
| SPACE | " " |
| CUSTOM | A custom value as defined in delimiter. |
| AUTODETECT | Automatically detect columns. |


## UpdateFilterViewRequest


Updates properties of the filter view.


| JSON representation |
|---|
| { "filter" : { object ( FilterView ) } , "fields" : string } |


| Fields |
|---|
| filter | object ( FilterView ) The new properties of the filter view. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root filter is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## DeleteRangeRequest


Deletes a range of cells, shifting other cells into the deleted area.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "shiftDimension" : enum ( Dimension ) } |


| Fields |
|---|
| range | object ( GridRange ) The range of cells to delete. |
| shiftDimension | enum ( Dimension ) The dimension from which deleted cells will be replaced with. If ROWS , existing cells will be shifted upward to replace the deleted cells. If COLUMNS , existing cells will be shifted left to replace the deleted cells. |


## AppendDimensionRequest


Appends rows or columns to the end of a sheet.


| JSON representation |
|---|
| { "sheetId" : integer , "dimension" : enum ( Dimension ) , "length" : integer } |


| Fields |
|---|
| sheetId | integer The sheet to append rows or columns to. |
| dimension | enum ( Dimension ) Whether rows or columns should be appended. |
| length | integer The number of rows or columns to append. |


## AddConditionalFormatRuleRequest


Adds a new conditional format rule at the given index. All subsequent rules' indexes are incremented.


| JSON representation |
|---|
| { "rule" : { object ( ConditionalFormatRule ) } , "index" : integer } |


| Fields |
|---|
| rule | object ( ConditionalFormatRule ) The rule to add. |
| index | integer The zero-based index where the rule should be inserted. |


## UpdateConditionalFormatRuleRequest


Updates a conditional format rule at the given index, or moves a conditional format rule to another index.


| JSON representation |
|---|
| { "index" : integer , "sheetId" : integer , "rule" : { object ( ConditionalFormatRule ) } , "newIndex" : integer } |


| Fields |
|---|
| index | integer The zero-based index of the rule that should be replaced or moved. |
| sheetId | integer The sheet of the rule to move. Required if newIndex is set, unused otherwise. |
| Union field instruction . The kind of update that should happen. instruction can be only one of the following: |
| rule | object ( ConditionalFormatRule ) The rule that should replace the rule at the given index. |
| newIndex | integer The zero-based new index the rule should end up at. |


## DeleteConditionalFormatRuleRequest


Deletes a conditional format rule at the given index. All subsequent rules' indexes are decremented.


| JSON representation |
|---|
| { "index" : integer , "sheetId" : integer } |


| Fields |
|---|
| index | integer The zero-based index of the rule to be deleted. |
| sheetId | integer The sheet the rule is being deleted from. |


## SortRangeRequest


Sorts data in rows based on a sort order per column.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "sortSpecs" : [ { object ( SortSpec ) } ] } |


| Fields |
|---|
| range | object ( GridRange ) The range to sort. |
| sortSpecs[] | object ( SortSpec ) The sort order per column. Later specifications are used when values are equal in the earlier specifications. |


## SetDataValidationRequest


Sets a data validation rule to every cell in the range. To clear validation in a range, call this with no rule specified.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "rule" : { object ( DataValidationRule ) } , "filteredRowsIncluded" : boolean } |


| Fields |
|---|
| range | object ( GridRange ) The range the data validation rule should apply to. |
| rule | object ( DataValidationRule ) The data validation rule to set on each cell in the range, or empty to clear the data validation in the range. |
| filteredRowsIncluded | boolean Optional. If true, the data validation rule will be applied to the filtered rows as well. |


## SetBasicFilterRequest


Sets the basic filter associated with a sheet.


| JSON representation |
|---|
| { "filter" : { object ( BasicFilter ) } } |


| Fields |
|---|
| filter | object ( BasicFilter ) The filter to set. |


## AddProtectedRangeRequest


Adds a new protected range.


| JSON representation |
|---|
| { "protectedRange" : { object ( ProtectedRange ) } } |


| Fields |
|---|
| protectedRange | object ( ProtectedRange ) The protected range to be added. The protectedRangeId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a range that already exists.) |


## UpdateProtectedRangeRequest


Updates an existing protected range with the specified
   `protectedRangeId`.


| JSON representation |
|---|
| { "protectedRange" : { object ( ProtectedRange ) } , "fields" : string } |


| Fields |
|---|
| protectedRange | object ( ProtectedRange ) The protected range to update with the new properties. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root protectedRange is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## DeleteProtectedRangeRequest


Deletes the protected range with the given ID.


| JSON representation |
|---|
| { "protectedRangeId" : integer } |


| Fields |
|---|
| protectedRangeId | integer The ID of the protected range to delete. |


## AutoResizeDimensionsRequest


Automatically resizes one or more dimensions based on the contents of the cells in that dimension.


| JSON representation |
|---|
| { "dimensions" : { object ( DimensionRange ) } , "dataSourceSheetDimensions" : { object ( DataSourceSheetDimensionRange ) } } |


| Fields |
|---|
| Union field dimension_range . The dimension range. dimension_range can be only one of the following: |
| dimensions | object ( DimensionRange ) The dimensions to automatically resize. |
| dataSourceSheetDimensions | object ( DataSourceSheetDimensionRange ) The dimensions on a data source sheet to automatically resize. |


## AddChartRequest


Adds a chart to a sheet in the spreadsheet.


| JSON representation |
|---|
| { "chart" : { object ( EmbeddedChart ) } } |


| Fields |
|---|
| chart | object ( EmbeddedChart ) The chart that should be added to the spreadsheet, including the position where it should be placed. The chartId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of an embedded object that already exists.) |


## UpdateChartSpecRequest


Updates a chart's specifications. (This does not move or resize a chart. To move or resize a chart, use
   `UpdateEmbeddedObjectPositionRequest`.)


| JSON representation |
|---|
| { "chartId" : integer , "spec" : { object ( ChartSpec ) } } |


| Fields |
|---|
| chartId | integer The ID of the chart to update. |
| spec | object ( ChartSpec ) The specification to apply to the chart. |


## UpdateBandingRequest


Updates properties of the supplied banded range.


| JSON representation |
|---|
| { "bandedRange" : { object ( BandedRange ) } , "fields" : string } |


| Fields |
|---|
| bandedRange | object ( BandedRange ) The banded range to update with the new properties. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root bandedRange is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## AddBandingRequest


Adds a new banded range to the spreadsheet.


| JSON representation |
|---|
| { "bandedRange" : { object ( BandedRange ) } } |


| Fields |
|---|
| bandedRange | object ( BandedRange ) The banded range to add. The bandedRangeId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a range that already exists.) |


## DeleteBandingRequest


Removes the banded range with the given ID from the spreadsheet.


| JSON representation |
|---|
| { "bandedRangeId" : integer } |


| Fields |
|---|
| bandedRangeId | integer The ID of the banded range to delete. |


## CreateDeveloperMetadataRequest


A request to create developer metadata.


| JSON representation |
|---|
| { "developerMetadata" : { object ( DeveloperMetadata ) } } |


| Fields |
|---|
| developerMetadata | object ( DeveloperMetadata ) The developer metadata to create. |


## UpdateDeveloperMetadataRequest


A request to update properties of developer metadata. Updates the properties of the developer metadata selected by the filters to the values provided in the
   `DeveloperMetadata`
   resource. Callers must specify the properties they wish to update in the fields parameter, as well as specify at least one
   `DataFilter`
   matching the metadata they wish to update.


| JSON representation |
|---|
| { "dataFilters" : [ { object ( DataFilter ) } ] , "developerMetadata" : { object ( DeveloperMetadata ) } , "fields" : string } |


| Fields |
|---|
| dataFilters[] | object ( DataFilter ) The filters matching the developer metadata entries to update. |
| developerMetadata | object ( DeveloperMetadata ) The value that all metadata matched by the data filters will be updated to. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root developerMetadata is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## DeleteDeveloperMetadataRequest


A request to delete developer metadata.


| JSON representation |
|---|
| { "dataFilter" : { object ( DataFilter ) } } |


| Fields |
|---|
| dataFilter | object ( DataFilter ) The data filter describing the criteria used to select which developer metadata entry to delete. |


## RandomizeRangeRequest


Randomizes the order of the rows in a range.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } } |


| Fields |
|---|
| range | object ( GridRange ) The range to randomize. |


## AddDimensionGroupRequest


Creates a group over the specified range.


If the requested range is a superset of the range of an existing group G, then the depth of G is incremented and this new group G' has the depth of that group. For example, a group [C:D, depth 1] + [B:E] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range is a subset of the range of an existing group G, then the depth of the new group G' becomes one greater than the depth of G. For example, a group [B:E, depth 1] + [C:D] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range starts before and ends within, or starts within and ends after, the range of an existing group G, then the range of the existing group G becomes the union of the ranges, and the new group G' has depth one greater than the depth of G and range as the intersection of the ranges. For example, a group [B:D, depth 1] + [C:E] results in groups [B:E, depth 1] and [C:D, depth 2].


| JSON representation |
|---|
| { "range" : { object ( DimensionRange ) } } |


| Fields |
|---|
| range | object ( DimensionRange ) The range over which to create a group. |


## DeleteDimensionGroupRequest


Deletes a group over the specified range by decrementing the depth of the dimensions in the range.


For example, assume the sheet has a depth-1 group over B:E and a depth-2 group over C:D. Deleting a group over D:E leaves the sheet with a depth-1 group over B:D and a depth-2 group over C:C.


| JSON representation |
|---|
| { "range" : { object ( DimensionRange ) } } |


| Fields |
|---|
| range | object ( DimensionRange ) The range of the group to be deleted. |


## UpdateDimensionGroupRequest


Updates the state of the specified group.


| JSON representation |
|---|
| { "dimensionGroup" : { object ( DimensionGroup ) } , "fields" : string } |


| Fields |
|---|
| dimensionGroup | object ( DimensionGroup ) The group whose state should be updated. The range and depth of the group should specify a valid group on the sheet, and all other fields updated. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root dimensionGroup is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## TrimWhitespaceRequest


Trims the whitespace (such as spaces, tabs, or new lines) in every cell in the specified range. This request removes all whitespace from the start and end of each cell's text, and reduces any subsequence of remaining whitespace characters to a single space. If the resulting trimmed text starts with a '+' or '=' character, the text remains as a string value and isn't interpreted as a formula.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } } |


| Fields |
|---|
| range | object ( GridRange ) The range whose cells to trim. |


## DeleteDuplicatesRequest


Removes rows within this range that contain values in the specified columns that are duplicates of values in any previous row. Rows with identical values but different letter cases, formatting, or formulas are considered to be duplicates.


This request also removes duplicate rows hidden from view (for example, due to a filter). When removing duplicates, the first instance of each duplicate row scanning from the top downwards is kept in the resulting range. Content outside of the specified range isn't removed, and rows considered duplicates do not have to be adjacent to each other in the range.


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "comparisonColumns" : [ { object ( DimensionRange ) } ] } |


| Fields |
|---|
| range | object ( GridRange ) The range to remove duplicates rows from. |
| comparisonColumns[] | object ( DimensionRange ) The columns in the range to analyze for duplicate values. If no columns are selected then all columns are analyzed for duplicates. |


## UpdateEmbeddedObjectBorderRequest


Updates an embedded object's border property.


| JSON representation |
|---|
| { "objectId" : integer , "border" : { object ( EmbeddedObjectBorder ) } , "fields" : string } |


| Fields |
|---|
| objectId | integer The ID of the embedded object to update. |
| border | object ( EmbeddedObjectBorder ) The border that applies to the embedded object. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root border is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## AddSlicerRequest


Adds a slicer to a sheet in the spreadsheet.


| JSON representation |
|---|
| { "slicer" : { object ( Slicer ) } } |


| Fields |
|---|
| slicer | object ( Slicer ) The slicer that should be added to the spreadsheet, including the position where it should be placed. The slicerId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a slicer that already exists.) |


## UpdateSlicerSpecRequest


Updates a slicer's specifications. (This does not move or resize a slicer. To move or resize a slicer use
   `UpdateEmbeddedObjectPositionRequest`.


| JSON representation |
|---|
| { "slicerId" : integer , "spec" : { object ( SlicerSpec ) } , "fields" : string } |


| Fields |
|---|
| slicerId | integer The id of the slicer to update. |
| spec | object ( SlicerSpec ) The specification to apply to the slicer. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root SlicerSpec is implied and should not be specified. A single "*"` can be used as short-hand for listing every field. |


## AddDataSourceRequest


Adds a data source. After the data source is added successfully, an associated
   `DATA_SOURCE`
   sheet is created and an execution is triggered to refresh the sheet to read data from the data source.


The request requires an additional
   `bigquery.readonly`
   OAuth scope if you are adding a BigQuery data source.


| JSON representation |
|---|
| { "dataSource" : { object ( DataSource ) } } |


| Fields |
|---|
| dataSource | object ( DataSource ) The data source to add. |


## UpdateDataSourceRequest


Updates a data source. After the data source is updated successfully, an execution is triggered to refresh the associated
   `DATA_SOURCE`
   sheet to read data from the updated data source.


The request requires an additional
   `bigquery.readonly`
   OAuth scope if you are updating a BigQuery data source.


| JSON representation |
|---|
| { "dataSource" : { object ( DataSource ) } , "fields" : string } |


| Fields |
|---|
| dataSource | object ( DataSource ) The data source to update. |
| fields | string ( FieldMask format) The fields that should be updated. At least one field must be specified. The root dataSource is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## DeleteDataSourceRequest


Deletes a data source. The request also deletes the associated data source sheet, and unlinks all associated data source objects.


| JSON representation |
|---|
| { "dataSourceId" : string } |


| Fields |
|---|
| dataSourceId | string The ID of the data source to delete. |


## RefreshDataSourceRequest


Refreshes one or multiple data source objects in the spreadsheet by the specified references.


The request requires an additional
   `bigquery.readonly`
   OAuth scope if you are refreshing a BigQuery data source.


If there are multiple refresh requests referencing the same data source objects in one batch, only the last refresh request is processed, and all those requests will have the same response accordingly.


| JSON representation |
|---|
| { "force" : boolean , "references" : { object ( DataSourceObjectReferences ) } , "dataSourceId" : string , "isAll" : boolean } |


| Fields |
|---|
| force | boolean Refreshes the data source objects regardless of the current state. If not set and a referenced data source object was in error state, the refresh will fail immediately. |
| Union field target . Specifies what to refresh. target can be only one of the following: |
| references | object ( DataSourceObjectReferences ) References to data source objects to refresh. |
| dataSourceId | string Reference to a DataSource . If specified, refreshes all associated data source objects for the data source. |
| isAll | boolean Refreshes all existing data source objects in the spreadsheet. |


## DataSourceObjectReferences


A list of references to data source objects.


| JSON representation |
|---|
| { "references" : [ { object ( DataSourceObjectReference ) } ] } |


| Fields |
|---|
| references[] | object ( DataSourceObjectReference ) The references. |


## DataSourceObjectReference


Reference to a data source object.


| JSON representation |
|---|
| { "sheetId" : string , "chartId" : integer , "dataSourceTableAnchorCell" : { object ( GridCoordinate ) } , "dataSourcePivotTableAnchorCell" : { object ( GridCoordinate ) } , "dataSourceFormulaCell" : { object ( GridCoordinate ) } } |


| Fields |
|---|
| Union field value . The reference type. value can be only one of the following: |
| sheetId | string References to a DATA_SOURCE sheet. |
| chartId | integer References to a data source chart. |
| dataSourceTableAnchorCell | object ( GridCoordinate ) References to a DataSourceTable anchored at the cell. |
| dataSourcePivotTableAnchorCell | object ( GridCoordinate ) References to a data source PivotTable anchored at the cell. |
| dataSourceFormulaCell | object ( GridCoordinate ) References to a cell containing DataSourceFormula . |


## CancelDataSourceRefreshRequest


Cancels one or multiple refreshes of data source objects in the spreadsheet by the specified references.


The request requires an additional
   `bigquery.readonly`
   OAuth scope if you are cancelling a refresh on a BigQuery data source.


| JSON representation |
|---|
| { "references" : { object ( DataSourceObjectReferences ) } , "dataSourceId" : string , "isAll" : boolean } |


| Fields |
|---|
| Union field target . Specifies what to cancel. target can be only one of the following: |
| references | object ( DataSourceObjectReferences ) References to data source objects whose refreshes are to be cancelled. |
| dataSourceId | string Reference to a DataSource . If specified, cancels all associated data source object refreshes for this data source. |
| isAll | boolean Cancels all existing data source object refreshes for all data sources in the spreadsheet. |


## AddTableRequest


Adds a new table to the spreadsheet.


| JSON representation |
|---|
| { "table" : { object ( Table ) } } |


| Fields |
|---|
| table | object ( Table ) Required. The table to add. |


## UpdateTableRequest


Updates a table in the spreadsheet.


| JSON representation |
|---|
| { "table" : { object ( Table ) } , "fields" : string } |


| Fields |
|---|
| table | object ( Table ) Required. The table to update. |
| fields | string ( FieldMask format) Required. The fields that should be updated. At least one field must be specified. The root table is implied and should not be specified. A single "*" can be used as short-hand for listing every field. |


## DeleteTableRequest


Removes the table with the given ID from the spreadsheet.


| JSON representation |
|---|
| { "tableId" : string } |


| Fields |
|---|
| tableId | string The ID of the table to delete. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]