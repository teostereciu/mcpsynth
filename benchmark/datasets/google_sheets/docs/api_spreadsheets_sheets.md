# Google Sheets

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets*

---

# Sheets


## Sheet


A sheet in a spreadsheet.


| JSON representation |
|---|
| { "properties" : { object ( SheetProperties ) } , "data" : [ { object ( GridData ) } ] , "merges" : [ { object ( GridRange ) } ] , "conditionalFormats" : [ { object ( ConditionalFormatRule ) } ] , "filterViews" : [ { object ( FilterView ) } ] , "protectedRanges" : [ { object ( ProtectedRange ) } ] , "basicFilter" : { object ( BasicFilter ) } , "charts" : [ { object ( EmbeddedChart ) } ] , "bandedRanges" : [ { object ( BandedRange ) } ] , "developerMetadata" : [ { object ( DeveloperMetadata ) } ] , "rowGroups" : [ { object ( DimensionGroup ) } ] , "columnGroups" : [ { object ( DimensionGroup ) } ] , "slicers" : [ { object ( Slicer ) } ] , "tables" : [ { object ( Table ) } ] } |


| Fields |
|---|
| properties | object ( SheetProperties ) The properties of the sheet. |
| data[] | object ( GridData ) Data in the grid, if this is a grid sheet. The number of GridData objects returned is dependent on the number of ranges requested on this sheet. For example, if this is representing Sheet1 , and the spreadsheet was requested with ranges Sheet1!A1:C10 and Sheet1!D15:E20 , then the first GridData will have a startRow / startColumn of 0 , while the second one will have startRow 14 (zero-based row 15), and startColumn 3 (zero-based column D). For a DATA_SOURCE sheet, you can not request a specific range, the GridData contains all the values. |
| merges[] | object ( GridRange ) The ranges that are merged together. |
| conditionalFormats[] | object ( ConditionalFormatRule ) The conditional format rules in this sheet. |
| filterViews[] | object ( FilterView ) The filter views in this sheet. |
| protectedRanges[] | object ( ProtectedRange ) The protected ranges in this sheet. |
| basicFilter | object ( BasicFilter ) The filter on this sheet, if any. |
| charts[] | object ( EmbeddedChart ) The specifications of every chart on this sheet. |
| bandedRanges[] | object ( BandedRange ) The banded (alternating colors) ranges on this sheet. |
| developerMetadata[] | object ( DeveloperMetadata ) The developer metadata associated with a sheet. |
| rowGroups[] | object ( DimensionGroup ) All row groups on this sheet, ordered by increasing range start index, then by group depth. |
| columnGroups[] | object ( DimensionGroup ) All column groups on this sheet, ordered by increasing range start index, then by group depth. |
| slicers[] | object ( Slicer ) The slicers on this sheet. |
| tables[] | object ( Table ) The tables on this sheet. |


## SheetProperties


Properties of a sheet.


| JSON representation |
|---|
| { "sheetId" : integer , "title" : string , "index" : integer , "sheetType" : enum ( SheetType ) , "gridProperties" : { object ( GridProperties ) } , "hidden" : boolean , "tabColor" : { object ( Color ) } , "tabColorStyle" : { object ( ColorStyle ) } , "rightToLeft" : boolean , "dataSourceSheetProperties" : { object ( DataSourceSheetProperties ) } } |


| Fields |
|---|
| sheetId | integer The ID of the sheet. Must be non-negative. This field cannot be changed once set. |
| title | string The name of the sheet. |
| index | integer The index of the sheet within the spreadsheet. When adding or updating sheet properties, if this field is excluded then the sheet is added or moved to the end of the sheet list. When updating sheet indices or inserting sheets, movement is considered in "before the move" indexes. For example, if there were three sheets (S1, S2, S3) in order to move S1 ahead of S2 the index would have to be set to 2. A sheet index update request is ignored if the requested index is identical to the sheets current index or if the requested new index is equal to the current sheet index + 1. |
| sheetType | enum ( SheetType ) The type of sheet. Defaults to GRID . This field cannot be changed once set. |
| gridProperties | object ( GridProperties ) Additional properties of the sheet if this sheet is a grid. (If the sheet is an object sheet, containing a chart or image, then this field will be absent.) When writing it is an error to set any grid properties on non-grid sheets. If this sheet is a DATA_SOURCE sheet, this field is output only but contains the properties that reflect how a data source sheet is rendered in the UI, e.g. rowCount . |
| hidden | boolean True if the sheet is hidden in the UI, false if it's visible. |
| tabColor (deprecated) | object ( Color ) This item is deprecated! The color of the tab in the UI. Deprecated: Use tabColorStyle . |
| tabColorStyle | object ( ColorStyle ) The color of the tab in the UI. If tabColor is also set, this field takes precedence. |
| rightToLeft | boolean True if the sheet is an RTL sheet instead of an LTR sheet. |
| dataSourceSheetProperties | object ( DataSourceSheetProperties ) Output only. If present, the field contains DATA_SOURCE sheet specific properties. |


## SheetType


The kind of sheet.


| Enums |
|---|
| SHEET_TYPE_UNSPECIFIED | Default value, do not use. |
| GRID | The sheet is a grid. |
| OBJECT | The sheet has no grid and instead has an object like a chart or image. |
| DATA_SOURCE | The sheet connects with an external DataSource and shows the preview of data. |


## GridProperties


Properties of a grid.


| JSON representation |
|---|
| { "rowCount" : integer , "columnCount" : integer , "frozenRowCount" : integer , "frozenColumnCount" : integer , "hideGridlines" : boolean , "rowGroupControlAfter" : boolean , "columnGroupControlAfter" : boolean } |


| Fields |
|---|
| rowCount | integer The number of rows in the grid. |
| columnCount | integer The number of columns in the grid. |
| frozenRowCount | integer The number of rows that are frozen in the grid. |
| frozenColumnCount | integer The number of columns that are frozen in the grid. |
| hideGridlines | boolean True if the grid isn't showing gridlines in the UI. |
| rowGroupControlAfter | boolean True if the row grouping control toggle is shown after the group. |
| columnGroupControlAfter | boolean True if the column grouping control toggle is shown after the group. |


## DataSourceSheetProperties


Additional properties of a
   `DATA_SOURCE`
   sheet.


| JSON representation |
|---|
| { "dataSourceId" : string , "columns" : [ { object ( DataSourceColumn ) } ] , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| dataSourceId | string ID of the DataSource the sheet is connected to. |
| columns[] | object ( DataSourceColumn ) The columns displayed on the sheet, corresponding to the values in RowData . |
| dataExecutionStatus | object ( DataExecutionStatus ) The data execution status. |


## GridData


Data in the grid, as well as metadata about the dimensions.


| JSON representation |
|---|
| { "startRow" : integer , "startColumn" : integer , "rowData" : [ { object ( RowData ) } ] , "rowMetadata" : [ { object ( DimensionProperties ) } ] , "columnMetadata" : [ { object ( DimensionProperties ) } ] } |


| Fields |
|---|
| startRow | integer The first row this GridData refers to, zero-based. |
| startColumn | integer The first column this GridData refers to, zero-based. |
| rowData[] | object ( RowData ) The data in the grid, one entry per row, starting with the row in startRow. The values in RowData will correspond to columns starting at startColumn . |
| rowMetadata[] | object ( DimensionProperties ) Metadata about the requested rows in the grid, starting with the row in startRow . |
| columnMetadata[] | object ( DimensionProperties ) Metadata about the requested columns in the grid, starting with the column in startColumn . |


## RowData


Data about each cell in a row.


| JSON representation |
|---|
| { "values" : [ { object ( CellData ) } ] } |


| Fields |
|---|
| values[] | object ( CellData ) The values in the row, one per column. |


## DimensionProperties


Properties about a dimension.


| JSON representation |
|---|
| { "hiddenByFilter" : boolean , "hiddenByUser" : boolean , "pixelSize" : integer , "developerMetadata" : [ { object ( DeveloperMetadata ) } ] , "dataSourceColumnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| hiddenByFilter | boolean True if this dimension is being filtered. This field is read-only. |
| hiddenByUser | boolean True if this dimension is explicitly hidden. |
| pixelSize | integer The height (if a row) or width (if a column) of the dimension in pixels. |
| developerMetadata[] | object ( DeveloperMetadata ) The developer metadata associated with a single row or column. |
| dataSourceColumnReference | object ( DataSourceColumnReference ) Output only. If set, this is a column in a data source sheet. |


## ConditionalFormatRule


A rule describing a conditional format.


| JSON representation |
|---|
| { "ranges" : [ { object ( GridRange ) } ] , "booleanRule" : { object ( BooleanRule ) } , "gradientRule" : { object ( GradientRule ) } } |


| Fields |
|---|
| ranges[] | object ( GridRange ) The ranges that are formatted if the condition is true. All the ranges must be on the same grid. |
| Union field rule . The rule controlling this conditional format, exactly one must be set. rule can be only one of the following: |
| booleanRule | object ( BooleanRule ) The formatting is either "on" or "off" according to the rule. |
| gradientRule | object ( GradientRule ) The formatting will vary based on the gradients in the rule. |


## BooleanRule


A rule that may or may not match, depending on the condition.


| JSON representation |
|---|
| { "condition" : { object ( BooleanCondition ) } , "format" : { object ( CellFormat ) } } |


| Fields |
|---|
| condition | object ( BooleanCondition ) The condition of the rule. If the condition evaluates to true, the format is applied. |
| format | object ( CellFormat ) The format to apply. Conditional formatting can only apply a subset of formatting: bold , italic , strikethrough , foreground color and, background color . |


## GradientRule


A rule that applies a gradient color scale format, based on the interpolation points listed. The format of a cell will vary based on its contents as compared to the values of the interpolation points.


| JSON representation |
|---|
| { "minpoint" : { object ( InterpolationPoint ) } , "midpoint" : { object ( InterpolationPoint ) } , "maxpoint" : { object ( InterpolationPoint ) } } |


| Fields |
|---|
| minpoint | object ( InterpolationPoint ) The starting interpolation point. |
| midpoint | object ( InterpolationPoint ) An optional midway interpolation point. |
| maxpoint | object ( InterpolationPoint ) The final interpolation point. |


## InterpolationPoint


A single interpolation point on a gradient conditional format. These pin the gradient color scale according to the color, type and value chosen.


| JSON representation |
|---|
| { "color" : { object ( Color ) } , "colorStyle" : { object ( ColorStyle ) } , "type" : enum ( InterpolationPointType ) , "value" : string } |


| Fields |
|---|
| color (deprecated) | object ( Color ) This item is deprecated! The color this interpolation point should use. Deprecated: Use colorStyle . |
| colorStyle | object ( ColorStyle ) The color this interpolation point should use. If color is also set, this field takes precedence. |
| type | enum ( InterpolationPointType ) How the value should be interpreted. |
| value | string The value this interpolation point uses. May be a formula. Unused if type is MIN or MAX . |


## InterpolationPointType


The kind of interpolation point.


| Enums |
|---|
| INTERPOLATION_POINT_TYPE_UNSPECIFIED | The default value, do not use. |
| MIN | The interpolation point uses the minimum value in the cells over the range of the conditional format. |
| MAX | The interpolation point uses the maximum value in the cells over the range of the conditional format. |
| NUMBER | The interpolation point uses exactly the value in InterpolationPoint.value . |
| PERCENT | The interpolation point is the given percentage over all the cells in the range of the conditional format. This is equivalent to NUMBER if the value was: =(MAX(FLATTEN(range)) * (value / 100))
  + (MIN(FLATTEN(range)) * (1 - (value / 100))) (where errors in the range are ignored when flattening). |
| PERCENTILE | The interpolation point is the given percentile over all the cells in the range of the conditional format. This is equivalent to NUMBER if the value was: =PERCENTILE(FLATTEN(range), value / 100) (where errors in the range are ignored when flattening). |


## FilterView


A filter view. For more information, see
   [Manage data visibility with filters](https://developers.google.com/workspace/sheets/api/guides/filters).


| JSON representation |
|---|
| { "filterViewId" : integer , "title" : string , "range" : { object ( GridRange ) } , "namedRangeId" : string , "tableId" : string , "sortSpecs" : [ { object ( SortSpec ) } ] , "criteria" : { integer : { object ( FilterCriteria ) } , ... } , "filterSpecs" : [ { object ( FilterSpec ) } ] } |


| Fields |
|---|
| filterViewId | integer The ID of the filter view. |
| title | string The name of the filter view. |
| range | object ( GridRange ) The range this filter view covers. When writing, only one of range , namedRangeId , or tableId may be set. |
| namedRangeId | string The named range this filter view is backed by, if any. When writing, only one of range , namedRangeId , or tableId may be set. |
| tableId | string The table this filter view is backed by, if any. When writing, only one of range , namedRangeId , or tableId may be set. |
| sortSpecs[] | object ( SortSpec ) The sort order per column. Later specifications are used when values are equal in the earlier specifications. |
| criteria (deprecated) | map (key: integer, value: object ( FilterCriteria )) This item is deprecated! The criteria for showing/hiding values per column. The map's key is the column index, and the value is the criteria for that column. This field is deprecated in favor of filterSpecs . |
| filterSpecs[] | object ( FilterSpec ) The filter criteria for showing or hiding values per column. Both criteria and filterSpecs are populated in responses. If both fields are specified in an update request, this field takes precedence. |


## ProtectedRange


A protected range.


| JSON representation |
|---|
| { "protectedRangeId" : integer , "range" : { object ( GridRange ) } , "namedRangeId" : string , "tableId" : string , "description" : string , "warningOnly" : boolean , "requestingUserCanEdit" : boolean , "unprotectedRanges" : [ { object ( GridRange ) } ] , "editors" : { object ( Editors ) } } |


| Fields |
|---|
| protectedRangeId | integer The ID of the protected range. This field is read-only. |
| range | object ( GridRange ) The range that is being protected. The range may be fully unbounded, in which case this is considered a protected sheet. When writing, only one of range or namedRangeId or tableId may be set. |
| namedRangeId | string The named range this protected range is backed by, if any. When writing, only one of range or namedRangeId or tableId may be set. |
| tableId | string The table this protected range is backed by, if any. When writing, only one of range or namedRangeId or tableId may be set. |
| description | string The description of this protected range. |
| warningOnly | boolean True if this protected range will show a warning when editing. Warning-based protection means that every user can edit data in the protected range, except editing will prompt a warning asking the user to confirm the edit. When writing: if this field is true, then editors are ignored. Additionally, if this field is changed from true to false and the editors field is not set (nor included in the field mask), then the editors will be set to all the editors in the document. |
| requestingUserCanEdit | boolean True if the user who requested this protected range can edit the protected area. This field is read-only. |
| unprotectedRanges[] | object ( GridRange ) The list of unprotected ranges within a protected sheet. Unprotected ranges are only supported on protected sheets. |
| editors | object ( Editors ) The users and groups with edit access to the protected range. This field is only visible to users with edit access to the protected range and the document. Editors are not supported with warningOnly protection. |


## Editors


The editors of a protected range.


| JSON representation |
|---|
| { "users" : [ string ] , "groups" : [ string ] , "domainUsersCanEdit" : boolean } |


| Fields |
|---|
| users[] | string The email addresses of users with edit access to the protected range. |
| groups[] | string The email addresses of groups with edit access to the protected range. |
| domainUsersCanEdit | boolean True if anyone in the document's domain has edit access to the protected range. Domain protection is only supported on documents within a domain. |


## BasicFilter


The default filter associated with a sheet. For more information, see
   [Manage data visibility with filters](https://developers.google.com/workspace/sheets/api/guides/filters).


| JSON representation |
|---|
| { "range" : { object ( GridRange ) } , "tableId" : string , "sortSpecs" : [ { object ( SortSpec ) } ] , "criteria" : { integer : { object ( FilterCriteria ) } , ... } , "filterSpecs" : [ { object ( FilterSpec ) } ] } |


| Fields |
|---|
| range | object ( GridRange ) The range the filter covers. |
| tableId | string The table this filter is backed by, if any. When writing, only one of range or tableId may be set. |
| sortSpecs[] | object ( SortSpec ) The sort order per column. Later specifications are used when values are equal in the earlier specifications. |
| criteria (deprecated) | map (key: integer, value: object ( FilterCriteria )) This item is deprecated! The criteria for showing/hiding values per column. The map's key is the column index, and the value is the criteria for that column. This field is deprecated in favor of filterSpecs . |
| filterSpecs[] | object ( FilterSpec ) The filter criteria per column. Both criteria and filterSpecs are populated in responses. If both fields are specified in an update request, this field takes precedence. |


## BandedRange


A banded (alternating colors) range in a sheet.


| JSON representation |
|---|
| { "bandedRangeId" : integer , "bandedRangeReference" : string , "range" : { object ( GridRange ) } , "rowProperties" : { object ( BandingProperties ) } , "columnProperties" : { object ( BandingProperties ) } } |


| Fields |
|---|
| bandedRangeId | integer The ID of the banded range. If unset, refer to bandedRangeReference . |
| bandedRangeReference | string Output only. The reference of the banded range, used to identify the ID that is not supported by the bandedRangeId . |
| range | object ( GridRange ) The range over which these properties are applied. |
| rowProperties | object ( BandingProperties ) Properties for row bands. These properties are applied on a row-by-row basis throughout all the rows in the range. At least one of rowProperties or columnProperties must be specified. |
| columnProperties | object ( BandingProperties ) Properties for column bands. These properties are applied on a column- by-column basis throughout all the columns in the range. At least one of rowProperties or columnProperties must be specified. |


## BandingProperties


Properties referring a single dimension (either row or column). If both
   `BandedRange.row_properties`
   and
   `BandedRange.column_properties`
   are set, the fill colors are applied to cells according to the following rules:


- `headerColor`
    and
    `footerColor`
    take priority over band colors.
- `firstBandColor`
    takes priority over
    `secondBandColor`.
- `rowProperties`
    takes priority over
    `columnProperties`.


For example, the first row color takes priority over the first column color, but the first column color takes priority over the second row color. Similarly, the row header takes priority over the column header in the top left cell, but the column header takes priority over the first row color if the row header is not set.


| JSON representation |
|---|
| { "headerColor" : { object ( Color ) } , "headerColorStyle" : { object ( ColorStyle ) } , "firstBandColor" : { object ( Color ) } , "firstBandColorStyle" : { object ( ColorStyle ) } , "secondBandColor" : { object ( Color ) } , "secondBandColorStyle" : { object ( ColorStyle ) } , "footerColor" : { object ( Color ) } , "footerColorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| headerColor (deprecated) | object ( Color ) This item is deprecated! The color of the first row or column. If this field is set, the first row or column is filled with this color and the colors alternate between firstBandColor and secondBandColor starting from the second row or column. Otherwise, the first row or column is filled with firstBandColor and the colors proceed to alternate as they normally would. Deprecated: Use headerColorStyle . |
| headerColorStyle | object ( ColorStyle ) The color of the first row or column. If this field is set, the first row or column is filled with this color and the colors alternate between firstBandColor and secondBandColor starting from the second row or column. Otherwise, the first row or column is filled with firstBandColor and the colors proceed to alternate as they normally would. If headerColor is also set, this field takes precedence. |
| firstBandColor (deprecated) | object ( Color ) This item is deprecated! The first color that is alternating. (Required) Deprecated: Use firstBandColorStyle . |
| firstBandColorStyle | object ( ColorStyle ) The first color that is alternating. (Required) If firstBandColor is also set, this field takes precedence. |
| secondBandColor (deprecated) | object ( Color ) This item is deprecated! The second color that is alternating. (Required) Deprecated: Use secondBandColorStyle . |
| secondBandColorStyle | object ( ColorStyle ) The second color that is alternating. (Required) If secondBandColor is also set, this field takes precedence. |
| footerColor (deprecated) | object ( Color ) This item is deprecated! The color of the last row or column. If this field is not set, the last row or column is filled with either firstBandColor or secondBandColor , depending on the color of the previous row or column. Deprecated: Use footerColorStyle . |
| footerColorStyle | object ( ColorStyle ) The color of the last row or column. If this field is not set, the last row or column is filled with either firstBandColor or secondBandColor , depending on the color of the previous row or column. If footerColor is also set, this field takes precedence. |


## DimensionGroup


A group over an interval of rows or columns on a sheet, which can contain or be contained within other groups. A group can be collapsed or expanded as a unit on the sheet.


| JSON representation |
|---|
| { "range" : { object ( DimensionRange ) } , "depth" : integer , "collapsed" : boolean } |


| Fields |
|---|
| range | object ( DimensionRange ) The range over which this group exists. |
| depth | integer The depth of the group, representing how many groups have a range that wholly contains the range of this group. |
| collapsed | boolean This field is true if this group is collapsed. A collapsed group remains collapsed if an overlapping group at a shallower depth is expanded. A true value does not imply that all dimensions within the group are hidden, since a dimension's visibility can change independently from this group property. However, when this property is updated, all dimensions within it are set to hidden if this field is true, or set to visible if this field is false. |


## Slicer


A slicer in a sheet.


| JSON representation |
|---|
| { "slicerId" : integer , "spec" : { object ( SlicerSpec ) } , "position" : { object ( EmbeddedObjectPosition ) } } |


| Fields |
|---|
| slicerId | integer The ID of the slicer. |
| spec | object ( SlicerSpec ) The specification of the slicer. |
| position | object ( EmbeddedObjectPosition ) The position of the slicer. Note that slicer can be positioned only on existing sheet. Also, width and height of slicer can be automatically adjusted to keep it within permitted limits. |


## SlicerSpec


The specifications of a slicer.


| JSON representation |
|---|
| { "dataRange" : { object ( GridRange ) } , "filterCriteria" : { object ( FilterCriteria ) } , "columnIndex" : integer , "applyToPivotTables" : boolean , "title" : string , "textFormat" : { object ( TextFormat ) } , "backgroundColor" : { object ( Color ) } , "backgroundColorStyle" : { object ( ColorStyle ) } , "horizontalAlignment" : enum ( HorizontalAlign ) } |


| Fields |
|---|
| dataRange | object ( GridRange ) The data range of the slicer. |
| filterCriteria | object ( FilterCriteria ) The filtering criteria of the slicer. |
| columnIndex | integer The zero-based column index in the data table on which the filter is applied to. |
| applyToPivotTables | boolean True if the filter should apply to pivot tables. If not set, default to True . |
| title | string The title of the slicer. |
| textFormat | object ( TextFormat ) The text format of title in the slicer. The link field is not supported. |
| backgroundColor (deprecated) | object ( Color ) This item is deprecated! The background color of the slicer. Deprecated: Use backgroundColorStyle . |
| backgroundColorStyle | object ( ColorStyle ) The background color of the slicer. If backgroundColor is also set, this field takes precedence. |
| horizontalAlignment | enum ( HorizontalAlign ) The horizontal alignment of title in the slicer. If unspecified, defaults to LEFT |


## Table


A table.


| JSON representation |
|---|
| { "tableId" : string , "name" : string , "range" : { object ( GridRange ) } , "rowsProperties" : { object ( TableRowsProperties ) } , "columnProperties" : [ { object ( TableColumnProperties ) } ] } |


| Fields |
|---|
| tableId | string The id of the table. |
| name | string The table name. This is unique to all tables in the same spreadsheet. |
| range | object ( GridRange ) The table range. |
| rowsProperties | object ( TableRowsProperties ) The table rows properties. |
| columnProperties[] | object ( TableColumnProperties ) The table column properties. |


## TableRowsProperties


The table row properties.


| JSON representation |
|---|
| { "headerColorStyle" : { object ( ColorStyle ) } , "firstBandColorStyle" : { object ( ColorStyle ) } , "secondBandColorStyle" : { object ( ColorStyle ) } , "footerColorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| headerColorStyle | object ( ColorStyle ) The color of the header row. If this field is set, the header row is filled with the specified color. Otherwise, the header row is filled with a default color. |
| firstBandColorStyle | object ( ColorStyle ) The first color that is alternating. If this field is set, the first banded row is filled with the specified color. Otherwise, the first banded row is filled with a default color. |
| secondBandColorStyle | object ( ColorStyle ) The second color that is alternating. If this field is set, the second banded row is filled with the specified color. Otherwise, the second banded row is filled with a default color. |
| footerColorStyle | object ( ColorStyle ) The color of the last row. If this field is not set a footer is not added, the last row is filled with either firstBandColorStyle or secondBandColorStyle , depending on the color of the previous row. If updating an existing table without a footer to have a footer, the range will be expanded by 1 row. If updating an existing table with a footer and removing a footer, the range will be shrunk by 1 row. |


## TableColumnProperties


The table column.


| JSON representation |
|---|
| { "columnIndex" : integer , "columnName" : string , "columnType" : enum ( ColumnType ) , "dataValidationRule" : { object ( TableColumnDataValidationRule ) } } |


| Fields |
|---|
| columnIndex | integer The 0-based column index. This index is relative to its position in the table and is not necessarily the same as the column index in the sheet. |
| columnName | string The column name. |
| columnType | enum ( ColumnType ) The column type. |
| dataValidationRule | object ( TableColumnDataValidationRule ) The column data validation rule. Only set for dropdown column type. |


## ColumnType


The column type for a given column in a table.


| Enums |
|---|
| COLUMN_TYPE_UNSPECIFIED | An unspecified column type. |
| DOUBLE | The number column type. |
| CURRENCY | The currency column type. |
| PERCENT | The percent column type. |
| DATE | The date column type. |
| TIME | The time column type. |
| DATE_TIME | The date and time column type. |
| TEXT | The text column type. |
| BOOLEAN | The boolean column type. |
| DROPDOWN | The dropdown column type. |
| FILES_CHIP | The files chip column type |
| PEOPLE_CHIP | The people chip column type |
| FINANCE_CHIP | The finance chip column type |
| PLACE_CHIP | The place chip column type |
| RATINGS_CHIP | The ratings chip column type |


## TableColumnDataValidationRule


A data validation rule for a column in a table.


| JSON representation |
|---|
| { "condition" : { object ( BooleanCondition ) } } |


| Fields |
|---|
| condition | object ( BooleanCondition ) The condition that data in the cell must match. Valid only if the [BooleanCondition.type] is ONE_OF_LIST. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]