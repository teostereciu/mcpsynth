# Cells

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells*

---

# Cells


## CellData


Data about a specific cell.


| JSON representation |
|---|
| { "userEnteredValue" : { object ( ExtendedValue ) } , "effectiveValue" : { object ( ExtendedValue ) } , "formattedValue" : string , "userEnteredFormat" : { object ( CellFormat ) } , "effectiveFormat" : { object ( CellFormat ) } , "hyperlink" : string , "note" : string , "textFormatRuns" : [ { object ( TextFormatRun ) } ] , "dataValidation" : { object ( DataValidationRule ) } , "pivotTable" : { object ( PivotTable ) } , "dataSourceTable" : { object ( DataSourceTable ) } , "dataSourceFormula" : { object ( DataSourceFormula ) } , "chipRuns" : [ { object ( ChipRun ) } ] } |


| Fields |
|---|
| userEnteredValue | object ( ExtendedValue ) The value the user entered in the cell. e.g., 1234 , 'Hello' , or =NOW() Note: Dates, Times and DateTimes are represented as doubles in serial number format. |
| effectiveValue | object ( ExtendedValue ) The effective value of the cell. For cells with formulas, this is the calculated value. For cells with literals, this is the same as the userEnteredValue. This field is read-only. |
| formattedValue | string The formatted value of the cell. This is the value as it's shown to the user. This field is read-only. |
| userEnteredFormat | object ( CellFormat ) The format the user entered for the cell. When writing, the new format will be merged with the existing format. |
| effectiveFormat | object ( CellFormat ) The effective format being used by the cell. This includes the results of applying any conditional formatting and, if the cell contains a formula, the computed number format. If the effective format is the default format, effective format will not be written. This field is read-only. |
| hyperlink | string A hyperlink this cell points to, if any. If the cell contains multiple hyperlinks, this field will be empty. This field is read-only. To set it, use a =HYPERLINK formula in the userEnteredValue.formulaValue field. A cell-level link can also be set from the userEnteredFormat.textFormat field. Alternatively, set a hyperlink in the textFormatRun.format.link field that spans the entire cell. |
| note | string Any note on the cell. |
| textFormatRuns[] | object ( TextFormatRun ) Runs of rich text applied to subsections of the cell. Runs are only valid on user entered strings, not formulas, bools, or numbers. Properties of a run start at a specific index in the text and continue until the next run. Runs will inherit the properties of the cell unless explicitly changed. When writing, the new runs will overwrite any prior runs. When writing a new userEnteredValue , previous runs are erased. |
| dataValidation | object ( DataValidationRule ) A data validation rule on the cell, if any. When writing, the new data validation rule will overwrite any prior rule. |
| pivotTable | object ( PivotTable ) A pivot table anchored at this cell. The size of pivot table itself is computed dynamically based on its data, grouping, filters, values, etc. Only the top-left cell of the pivot table contains the pivot table definition. The other cells will contain the calculated values of the results of the pivot in their effectiveValue fields. |
| dataSourceTable | object ( DataSourceTable ) A data source table anchored at this cell. The size of data source table itself is computed dynamically based on its configuration. Only the first cell of the data source table contains the data source table definition. The other cells will contain the display values of the data source table result in their effectiveValue fields. |
| dataSourceFormula | object ( DataSourceFormula ) Output only. Information about a data source formula on the cell. The field is set if userEnteredValue is a formula referencing some DATA_SOURCE sheet, e.g. =SUM(DataSheet!Column) . |
| chipRuns[] | object ( ChipRun ) Optional. Runs of chips applied to subsections of the cell. Properties of a run start at a specific index in the text and continue until the next run. When reading, all chipped and non-chipped runs are included. Non-chipped runs will have an empty Chip . When writing, only runs with chips are included. Runs containing chips are of length 1 and are represented in the user-entered text by an “@” placeholder symbol. New runs will overwrite any prior runs. Writing a new userEnteredValue will erase previous runs. |


## CellFormat


The format of a cell.


| JSON representation |
|---|
| { "numberFormat" : { object ( NumberFormat ) } , "backgroundColor" : { object ( Color ) } , "backgroundColorStyle" : { object ( ColorStyle ) } , "borders" : { object ( Borders ) } , "padding" : { object ( Padding ) } , "horizontalAlignment" : enum ( HorizontalAlign ) , "verticalAlignment" : enum ( VerticalAlign ) , "wrapStrategy" : enum ( WrapStrategy ) , "textDirection" : enum ( TextDirection ) , "textFormat" : { object ( TextFormat ) } , "hyperlinkDisplayType" : enum ( HyperlinkDisplayType ) , "textRotation" : { object ( TextRotation ) } } |


| Fields |
|---|
| numberFormat | object ( NumberFormat ) A format describing how number values should be represented to the user. |
| backgroundColor (deprecated) | object ( Color ) This item is deprecated! The background color of the cell. Deprecated: Use backgroundColorStyle . |
| backgroundColorStyle | object ( ColorStyle ) The background color of the cell. If backgroundColor is also set, this field takes precedence. |
| borders | object ( Borders ) The borders of the cell. |
| padding | object ( Padding ) The padding of the cell. |
| horizontalAlignment | enum ( HorizontalAlign ) The horizontal alignment of the value in the cell. |
| verticalAlignment | enum ( VerticalAlign ) The vertical alignment of the value in the cell. |
| wrapStrategy | enum ( WrapStrategy ) The wrap strategy for the value in the cell. |
| textDirection | enum ( TextDirection ) The direction of the text in the cell. |
| textFormat | object ( TextFormat ) The format of the text in the cell (unless overridden by a format run). Setting a cell-level link here clears the cell's existing links. Setting the link field in a TextFormatRun takes precedence over the cell-level link. |
| hyperlinkDisplayType | enum ( HyperlinkDisplayType ) If one exists, how a hyperlink should be displayed in the cell. |
| textRotation | object ( TextRotation ) The rotation applied to text in the cell. |


## NumberFormat


The number format of a cell.


| JSON representation |
|---|
| { "type" : enum ( NumberFormatType ) , "pattern" : string } |


| Fields |
|---|
| type | enum ( NumberFormatType ) The type of the number format. When writing, this field must be set. |
| pattern | string Pattern string used for formatting. If not set, a default pattern based on the spreadsheet's locale will be used if necessary for the given type. See the Date and Number Formats guide for more information about the supported patterns. |


## NumberFormatType


The number format of the cell. In this documentation the locale is assumed to be en_US, but the actual format depends on the locale of the spreadsheet.


| Enums |
|---|
| NUMBER_FORMAT_TYPE_UNSPECIFIED | The number format is not specified and is based on the contents of the cell. Do not explicitly use this. |
| TEXT | Text formatting, e.g 1000.12 |
| NUMBER | Number formatting, e.g, 1,000.12 |
| PERCENT | Percent formatting, e.g 10.12% |
| CURRENCY | Currency formatting, e.g $1,000.12 |
| DATE | Date formatting, e.g 9/26/2008 |
| TIME | Time formatting, e.g 3:59:00 PM |
| DATE_TIME | Date+Time formatting, e.g 9/26/08 15:59:00 |
| SCIENTIFIC | Scientific number formatting, e.g 1.01E+03 |


## Borders


The borders of the cell.


| JSON representation |
|---|
| { "top" : { object ( Border ) } , "bottom" : { object ( Border ) } , "left" : { object ( Border ) } , "right" : { object ( Border ) } } |


| Fields |
|---|
| top | object ( Border ) The top border of the cell. |
| bottom | object ( Border ) The bottom border of the cell. |
| left | object ( Border ) The left border of the cell. |
| right | object ( Border ) The right border of the cell. |


## Border


A border along a cell.


| JSON representation |
|---|
| { "style" : enum ( Style ) , "width" : integer , "color" : { object ( Color ) } , "colorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| style | enum ( Style ) The style of the border. |
| width (deprecated) | integer This item is deprecated! The width of the border, in pixels. Deprecated; the width is determined by the "style" field. |
| color (deprecated) | object ( Color ) This item is deprecated! The color of the border. Deprecated: Use colorStyle . |
| colorStyle | object ( ColorStyle ) The color of the border. If color is also set, this field takes precedence. |


## Style


The style of a border.


| Enums |
|---|
| STYLE_UNSPECIFIED | The style is not specified. Do not use this. |
| DOTTED | The border is dotted. |
| DASHED | The border is dashed. |
| SOLID | The border is a thin solid line. |
| SOLID_MEDIUM | The border is a medium solid line. |
| SOLID_THICK | The border is a thick solid line. |
| NONE | No border. Used only when updating a border in order to erase it. |
| DOUBLE | The border is two solid lines. |


## Padding


The amount of padding around the cell, in pixels. When updating padding, every field must be specified.


| JSON representation |
|---|
| { "top" : integer , "right" : integer , "bottom" : integer , "left" : integer } |


| Fields |
|---|
| top | integer The top padding of the cell. |
| right | integer The right padding of the cell. |
| bottom | integer The bottom padding of the cell. |
| left | integer The left padding of the cell. |


## VerticalAlign


The vertical alignment of text in a cell.


| Enums |
|---|
| VERTICAL_ALIGN_UNSPECIFIED | The vertical alignment is not specified. Do not use this. |
| TOP | The text is explicitly aligned to the top of the cell. |
| MIDDLE | The text is explicitly aligned to the middle of the cell. |
| BOTTOM | The text is explicitly aligned to the bottom of the cell. |


## WrapStrategy


How to wrap text in a cell.


| Enums |
|---|
| WRAP_STRATEGY_UNSPECIFIED | The default value, do not use. |
| OVERFLOW_CELL | Lines that are longer than the cell width will be written in the next cell over, so long as that cell is empty. If the next cell over is non-empty, this behaves the same as CLIP . The text will never wrap to the next line unless the user manually inserts a new line. Example: \| First sentence. \|
\| Manual newline that is very long. <- Text continues into next cell
\| Next newline.   \| |
| LEGACY_WRAP | This wrap strategy represents the old Google Sheets wrap strategy where words that are longer than a line are clipped rather than broken. This strategy is not supported on all platforms and is being phased out. Example: \| Cell has a \|
\| loooooooooo\| <- Word is clipped.
\| word.      \| |
| CLIP | Lines that are longer than the cell width will be clipped. The text will never wrap to the next line unless the user manually inserts a new line. Example: \| First sentence. \|
\| Manual newline t\| <- Text is clipped
\| Next newline.   \| |
| WRAP | Words that are longer than a line are wrapped at the character level rather than clipped. Example: \| Cell has a \|
\| loooooooooo\| <- Word is broken.
\| ong word.  \| |


## TextDirection


The direction of text in a cell.


| Enums |
|---|
| TEXT_DIRECTION_UNSPECIFIED | The text direction is not specified. Do not use this. |
| LEFT_TO_RIGHT | The text direction of left-to-right was set by the user. |
| RIGHT_TO_LEFT | The text direction of right-to-left was set by the user. |


## HyperlinkDisplayType


Whether to explicitly render a hyperlink. If not specified, the hyperlink is linked.


| Enums |
|---|
| HYPERLINK_DISPLAY_TYPE_UNSPECIFIED | The default value: the hyperlink is rendered. Do not use this. |
| LINKED | A hyperlink should be explicitly rendered. |
| PLAIN_TEXT | A hyperlink should not be rendered. |


## TextRotation


The rotation applied to text in a cell.


| JSON representation |
|---|
| { "angle" : integer , "vertical" : boolean } |


| Fields |
|---|
| Union field type . The type of rotation, vertical or angled. type can be only one of the following: |
| angle | integer The angle between the standard orientation and the desired orientation. Measured in degrees. Valid values are between -90 and 90. Positive angles are angled upwards, negative are angled downwards. Note: For LTR text direction positive angles are in the counterclockwise direction, whereas for RTL they are in the clockwise direction |
| vertical | boolean If true, text reads top to bottom, but the orientation of individual characters is unchanged. For example: \| V \|
\| e \|
\| r \|
\| t \|
\| i \|
\| c \|
\| a \|
\| l \| |


## TextFormatRun


A run of a text format. The format of this run continues until the start index of the next run. When updating, all fields must be set.


| JSON representation |
|---|
| { "startIndex" : integer , "format" : { object ( TextFormat ) } } |


| Fields |
|---|
| startIndex | integer The zero-based character index where this run starts, in UTF-16 code units. |
| format | object ( TextFormat ) The format of this run. Absent values inherit the cell's format. |


## DataValidationRule


A data validation rule.


| JSON representation |
|---|
| { "condition" : { object ( BooleanCondition ) } , "inputMessage" : string , "strict" : boolean , "showCustomUi" : boolean } |


| Fields |
|---|
| condition | object ( BooleanCondition ) The condition that data in the cell must match. |
| inputMessage | string A message to show the user when adding data to the cell. |
| strict | boolean True if invalid data should be rejected. |
| showCustomUi | boolean True if the UI should be customized based on the kind of condition. If true, "List" conditions will show a dropdown. |


## DataSourceTable


A data source table, which allows the user to import a static table of data from the
   `DataSource`
   into Sheets. This is also known as "Extract" in the Sheets editor.


| JSON representation |
|---|
| { "dataSourceId" : string , "columnSelectionType" : enum ( DataSourceTableColumnSelectionType ) , "columns" : [ { object ( DataSourceColumnReference ) } ] , "filterSpecs" : [ { object ( FilterSpec ) } ] , "sortSpecs" : [ { object ( SortSpec ) } ] , "rowLimit" : integer , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| dataSourceId | string The ID of the data source the data source table is associated with. |
| columnSelectionType | enum ( DataSourceTableColumnSelectionType ) The type to select columns for the data source table. Defaults to SELECTED . |
| columns[] | object ( DataSourceColumnReference ) Columns selected for the data source table. The columnSelectionType must be SELECTED . |
| filterSpecs[] | object ( FilterSpec ) Filter specifications in the data source table. |
| sortSpecs[] | object ( SortSpec ) Sort specifications in the data source table. The result of the data source table is sorted based on the sort specifications in order. |
| rowLimit | integer The limit of rows to return. If not set, a default limit is applied. Please refer to the Sheets editor for the default and max limit. |
| dataExecutionStatus | object ( DataExecutionStatus ) Output only. The data execution status. |


## DataSourceTableColumnSelectionType


The data source table column selection types.


| Enums |
|---|
| DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED | The default column selection type, do not use. |
| SELECTED | Select columns specified by columns field. |
| SYNC_ALL | Sync all current and future columns in the data source. If set, the data source table fetches all the columns in the data source at the time of refresh. |


## DataSourceFormula


A data source formula.


| JSON representation |
|---|
| { "dataSourceId" : string , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| dataSourceId | string The ID of the data source the formula is associated with. |
| dataExecutionStatus | object ( DataExecutionStatus ) Output only. The data execution status. |


## ChipRun


The run of a chip. The chip continues until the start index of the next run.


| JSON representation |
|---|
| { "startIndex" : integer , "chip" : { object ( Chip ) } } |


| Fields |
|---|
| startIndex | integer Required. The zero-based character index where this run starts, in UTF-16 code units. |
| chip | object ( Chip ) Optional. The chip of this run. |


## Chip


The Smart Chip.


| JSON representation |
|---|
| { "personProperties" : { object ( PersonProperties ) } , "richLinkProperties" : { object ( RichLinkProperties ) } } |


| Fields |
|---|
| Union field properties . The properties of the chip. properties can be only one of the following: |
| personProperties | object ( PersonProperties ) Properties of a linked person. |
| richLinkProperties | object ( RichLinkProperties ) Properties of a rich link. |


## PersonProperties


Properties specific to a linked person.


| JSON representation |
|---|
| { "email" : string , "displayFormat" : enum ( DisplayFormat ) } |


| Fields |
|---|
| email | string Required. The email address linked to this person. This field is always present. |
| displayFormat | enum ( DisplayFormat ) Optional. The display format of the person chip. If not set, the default display format is used. |


## DisplayFormat


Preferred display format when available.


| Enums |
|---|
| DISPLAY_FORMAT_UNSPECIFIED | Default value, do not use. |
| DEFAULT | Default display format. |
| LAST_NAME_COMMA_FIRST_NAME | Last name, first name display format. |
| EMAIL | Email display format. |


## RichLinkProperties


Properties of a link to a Google resource (such as a file in Drive, a YouTube video, a Maps address, or a Calendar event). Only Drive files can be written as chips. All other rich link types are read only.


URIs cannot exceed 2000 bytes when writing.


NOTE: Writing Drive file chips requires at least one of the
   `drive.file`,
   `drive.readonly`, or
   `drive`
   OAuth scopes.


| JSON representation |
|---|
| { "uri" : string , "mimeType" : string } |


| Fields |
|---|
| uri | string Required. The URI to the link. This is always present. |
| mimeType | string Output only. The MIME type of the link, if there's one (for example, when it's a file in Drive). |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]