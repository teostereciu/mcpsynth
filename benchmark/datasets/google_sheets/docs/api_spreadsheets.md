# REST Resource: spreadsheets

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets*

---

# REST Resource: spreadsheets


- Resource: Spreadsheet

- JSON representation
- SpreadsheetProperties

- JSON representation
- RecalculationInterval
- CellFormat

- JSON representation
- NumberFormat

- JSON representation
- NumberFormatType
- Color

- JSON representation
- ColorStyle

- JSON representation
- ThemeColorType
- Borders

- JSON representation
- Border

- JSON representation
- Style
- Padding

- JSON representation
- HorizontalAlign
- VerticalAlign
- WrapStrategy
- TextDirection
- TextFormat

- JSON representation
- Link

- JSON representation
- HyperlinkDisplayType
- TextRotation

- JSON representation
- IterativeCalculationSettings

- JSON representation
- SpreadsheetTheme

- JSON representation
- ThemeColorPair

- JSON representation
- Sheet

- JSON representation
- SheetProperties

- JSON representation
- SheetType
- GridProperties

- JSON representation
- DataSourceSheetProperties

- JSON representation
- DataSourceColumn

- JSON representation
- DataSourceColumnReference

- JSON representation
- DataExecutionStatus

- JSON representation
- DataExecutionState
- DataExecutionErrorCode
- GridData

- JSON representation
- RowData

- JSON representation
- CellData

- JSON representation
- ExtendedValue

- JSON representation
- ErrorValue

- JSON representation
- ErrorType
- TextFormatRun

- JSON representation
- DataValidationRule

- JSON representation
- BooleanCondition

- JSON representation
- ConditionType
- ConditionValue

- JSON representation
- RelativeDate
- PivotTable

- JSON representation
- GridRange

- JSON representation
- PivotGroup

- JSON representation
- PivotGroupValueMetadata

- JSON representation
- SortOrder
- PivotGroupSortValueBucket

- JSON representation
- PivotGroupRule

- JSON representation
- ManualRule

- JSON representation
- ManualRuleGroup

- JSON representation
- HistogramRule

- JSON representation
- DateTimeRule

- JSON representation
- DateTimeRuleType
- PivotGroupLimit

- JSON representation
- PivotFilterCriteria

- JSON representation
- PivotFilterSpec

- JSON representation
- PivotValue

- JSON representation
- PivotValueSummarizeFunction
- PivotValueCalculatedDisplayType
- PivotValueLayout
- DataSourceTable

- JSON representation
- DataSourceTableColumnSelectionType
- FilterSpec

- JSON representation
- FilterCriteria

- JSON representation
- SortSpec

- JSON representation
- DataSourceFormula

- JSON representation
- ChipRun

- JSON representation
- Chip

- JSON representation
- PersonProperties

- JSON representation
- DisplayFormat
- RichLinkProperties

- JSON representation
- DimensionProperties

- JSON representation
- ConditionalFormatRule

- JSON representation
- BooleanRule

- JSON representation
- GradientRule

- JSON representation
- InterpolationPoint

- JSON representation
- InterpolationPointType
- FilterView

- JSON representation
- ProtectedRange

- JSON representation
- Editors

- JSON representation
- BasicFilter

- JSON representation
- EmbeddedChart

- JSON representation
- ChartSpec

- JSON representation
- TextPosition

- JSON representation
- DataSourceChartProperties

- JSON representation
- BasicChartSpec

- JSON representation
- BasicChartType
- BasicChartLegendPosition
- BasicChartAxis

- JSON representation
- BasicChartAxisPosition
- ChartAxisViewWindowOptions

- JSON representation
- ViewWindowMode
- BasicChartDomain

- JSON representation
- ChartData

- JSON representation
- ChartSourceRange

- JSON representation
- ChartGroupRule

- JSON representation
- ChartDateTimeRule

- JSON representation
- ChartDateTimeRuleType
- ChartHistogramRule

- JSON representation
- ChartAggregateType
- BasicChartSeries

- JSON representation
- LineStyle

- JSON representation
- LineDashType
- DataLabel

- JSON representation
- DataLabelType
- DataLabelPlacement
- PointStyle

- JSON representation
- PointShape
- BasicSeriesDataPointStyleOverride

- JSON representation
- BasicChartStackedType
- BasicChartCompareMode
- PieChartSpec

- JSON representation
- PieChartLegendPosition
- BubbleChartSpec

- JSON representation
- BubbleChartLegendPosition
- CandlestickChartSpec

- JSON representation
- CandlestickDomain

- JSON representation
- CandlestickData

- JSON representation
- CandlestickSeries

- JSON representation
- OrgChartSpec

- JSON representation
- OrgChartNodeSize
- HistogramChartSpec

- JSON representation
- HistogramSeries

- JSON representation
- HistogramChartLegendPosition
- WaterfallChartSpec

- JSON representation
- WaterfallChartDomain

- JSON representation
- WaterfallChartSeries

- JSON representation
- WaterfallChartColumnStyle

- JSON representation
- WaterfallChartCustomSubtotal

- JSON representation
- WaterfallChartStackedType
- TreemapChartSpec

- JSON representation
- TreemapChartColorScale

- JSON representation
- ScorecardChartSpec

- JSON representation
- KeyValueFormat

- JSON representation
- BaselineValueFormat

- JSON representation
- ComparisonType
- ChartNumberFormatSource
- ChartCustomNumberFormatOptions

- JSON representation
- ChartHiddenDimensionStrategy
- EmbeddedObjectPosition

- JSON representation
- OverlayPosition

- JSON representation
- GridCoordinate

- JSON representation
- EmbeddedObjectBorder

- JSON representation
- BandedRange

- JSON representation
- BandingProperties

- JSON representation
- DimensionGroup

- JSON representation
- Slicer

- JSON representation
- SlicerSpec

- JSON representation
- Table

- JSON representation
- TableRowsProperties

- JSON representation
- TableColumnProperties

- JSON representation
- ColumnType
- TableColumnDataValidationRule

- JSON representation
- NamedRange

- JSON representation
- DataSource

- JSON representation
- DataSourceSpec

- JSON representation
- BigQueryDataSourceSpec

- JSON representation
- BigQueryQuerySpec

- JSON representation
- BigQueryTableSpec

- JSON representation
- LookerDataSourceSpec

- JSON representation
- DataSourceParameter

- JSON representation
- DataSourceRefreshSchedule

- JSON representation
- DataSourceRefreshScope
- DataSourceRefreshDailySchedule

- JSON representation
- TimeOfDay

- JSON representation
- DataSourceRefreshWeeklySchedule

- JSON representation
- DayOfWeek
- DataSourceRefreshMonthlySchedule

- JSON representation
- Interval

- JSON representation
- Methods


## Resource: Spreadsheet


Resource that represents a spreadsheet.


| JSON representation |
|---|
| { "spreadsheetId" : string , "properties" : { object ( SpreadsheetProperties ) } , "sheets" : [ { object ( Sheet ) } ] , "namedRanges" : [ { object ( NamedRange ) } ] , "spreadsheetUrl" : string , "developerMetadata" : [ { object ( DeveloperMetadata ) } ] , "dataSources" : [ { object ( DataSource ) } ] , "dataSourceSchedules" : [ { object ( DataSourceRefreshSchedule ) } ] } |


| Fields |
|---|
| spreadsheetId | string The ID of the spreadsheet. This field is read-only. |
| properties | object ( SpreadsheetProperties ) Overall properties of a spreadsheet. |
| sheets[] | object ( Sheet ) The sheets that are part of a spreadsheet. |
| namedRanges[] | object ( NamedRange ) The named ranges defined in a spreadsheet. |
| spreadsheetUrl | string The url of the spreadsheet. This field is read-only. |
| developerMetadata[] | object ( DeveloperMetadata ) The developer metadata associated with a spreadsheet. |
| dataSources[] | object ( DataSource ) A list of external data sources connected with the spreadsheet. |
| dataSourceSchedules[] | object ( DataSourceRefreshSchedule ) Output only. A list of data source refresh schedules. |


## SpreadsheetProperties


Properties of a spreadsheet.


| JSON representation |
|---|
| { "title" : string , "locale" : string , "autoRecalc" : enum ( RecalculationInterval ) , "timeZone" : string , "defaultFormat" : { object ( CellFormat ) } , "iterativeCalculationSettings" : { object ( IterativeCalculationSettings ) } , "spreadsheetTheme" : { object ( SpreadsheetTheme ) } , "importFunctionsExternalUrlAccessAllowed" : boolean } |


| Fields |
|---|
| title | string The title of the spreadsheet. |
| locale | string The locale of the spreadsheet in one of the following formats: an ISO 639-1 language code such as en an ISO 639-2 language code such as fil , if no 639-1 code exists a combination of the ISO language code and country code, such as en_US Note: when updating this field, not all locales/languages are supported. |
| autoRecalc | enum ( RecalculationInterval ) The amount of time to wait before volatile functions are recalculated. |
| timeZone | string The time zone of the spreadsheet, in CLDR format such as America/New_York . If the time zone isn't recognized, this may be a custom time zone such as GMT-07:00 . |
| defaultFormat | object ( CellFormat ) The default format of all cells in the spreadsheet. CellData.effectiveFormat will not be set if the cell's format is equal to this default format. This field is read-only. |
| iterativeCalculationSettings | object ( IterativeCalculationSettings ) Determines whether and how circular references are resolved with iterative calculation. Absence of this field means that circular references result in calculation errors. |
| spreadsheetTheme | object ( SpreadsheetTheme ) Theme applied to the spreadsheet. |
| importFunctionsExternalUrlAccessAllowed | boolean Whether to allow external URL access for image and import functions. Read only when true. When false, you can set to true. This value will be bypassed and always return true if the admin has enabled the allowlisting feature . |


## RecalculationInterval


An enumeration of the possible recalculation interval options.


| Enums |
|---|
| RECALCULATION_INTERVAL_UNSPECIFIED | Default value. This value must not be used. |
| ON_CHANGE | Volatile functions are updated on every change. |
| MINUTE | Volatile functions are updated on every change and every minute. |
| HOUR | Volatile functions are updated on every change and hourly. |


## IterativeCalculationSettings


Settings to control how circular dependencies are resolved with iterative calculation.


| JSON representation |
|---|
| { "maxIterations" : integer , "convergenceThreshold" : number } |


| Fields |
|---|
| maxIterations | integer When iterative calculation is enabled, the maximum number of calculation rounds to perform. |
| convergenceThreshold | number When iterative calculation is enabled and successive results differ by less than this threshold value, the calculation rounds stop. |


## SpreadsheetTheme


Represents spreadsheet theme


| JSON representation |
|---|
| { "primaryFontFamily" : string , "themeColors" : [ { object ( ThemeColorPair ) } ] } |


| Fields |
|---|
| primaryFontFamily | string Name of the primary font family. |
| themeColors[] | object ( ThemeColorPair ) The spreadsheet theme color pairs. To update you must provide all theme color pairs. |


## ThemeColorPair


A pair mapping a spreadsheet theme color type to the concrete color it represents.


| JSON representation |
|---|
| { "colorType" : enum ( ThemeColorType ) , "color" : { object ( ColorStyle ) } } |


| Fields |
|---|
| colorType | enum ( ThemeColorType ) The type of the spreadsheet theme color. |
| color | object ( ColorStyle ) The concrete color corresponding to the theme color type. |


## NamedRange


A named range.


| JSON representation |
|---|
| { "namedRangeId" : string , "name" : string , "range" : { object ( GridRange ) } } |


| Fields |
|---|
| namedRangeId | string The ID of the named range. |
| name | string The name of the named range. |
| range | object ( GridRange ) The range this represents. |


## DataSource


Information about an external data source in the spreadsheet.


| JSON representation |
|---|
| { "dataSourceId" : string , "spec" : { object ( DataSourceSpec ) } , "calculatedColumns" : [ { object ( DataSourceColumn ) } ] , "sheetId" : integer } |


| Fields |
|---|
| dataSourceId | string The spreadsheet-scoped unique ID that identifies the data source. Example: 1080547365. |
| spec | object ( DataSourceSpec ) The DataSourceSpec for the data source connected with this spreadsheet. |
| calculatedColumns[] | object ( DataSourceColumn ) All calculated columns in the data source. |
| sheetId | integer The ID of the Sheet connected with the data source. The field cannot be changed once set. When creating a data source, an associated DATA_SOURCE sheet is also created, if the field is not specified, the ID of the created sheet will be randomly generated. |


## DataSourceSpec


This specifies the details of the data source. For example, for BigQuery, this specifies information about the BigQuery source.


| JSON representation |
|---|
| { "parameters" : [ { object ( DataSourceParameter ) } ] , "bigQuery" : { object ( BigQueryDataSourceSpec ) } , "looker" : { object ( LookerDataSourceSpec ) } } |


| Fields |
|---|
| parameters[] | object ( DataSourceParameter ) The parameters of the data source, used when querying the data source. |
| Union field spec . The actual specification per data source type. spec can be only one of the following: |
| bigQuery | object ( BigQueryDataSourceSpec ) A BigQueryDataSourceSpec . |
| looker | object ( LookerDataSourceSpec ) A [LookerDatasourceSpec][]. |


## BigQueryDataSourceSpec


The specification of a BigQuery data source that's connected to a sheet.


| JSON representation |
|---|
| { "projectId" : string , "querySpec" : { object ( BigQueryQuerySpec ) } , "tableSpec" : { object ( BigQueryTableSpec ) } } |


| Fields |
|---|
| projectId | string The ID of a BigQuery enabled Google Cloud project with a billing account attached. For any queries executed against the data source, the project is charged. |
| Union field spec . The actual specification. spec can be only one of the following: |
| querySpec | object ( BigQueryQuerySpec ) A BigQueryQuerySpec . |
| tableSpec | object ( BigQueryTableSpec ) A BigQueryTableSpec . |


## BigQueryQuerySpec


Specifies a custom BigQuery query.


| JSON representation |
|---|
| { "rawQuery" : string } |


| Fields |
|---|
| rawQuery | string The raw query string. |


## BigQueryTableSpec


Specifies a BigQuery table definition. Only [native tables](https://cloud.google.com/bigquery/docs/tables-intro) are allowed.


| JSON representation |
|---|
| { "tableProjectId" : string , "tableId" : string , "datasetId" : string } |


| Fields |
|---|
| tableProjectId | string The ID of a BigQuery project the table belongs to. If not specified, the projectId is assumed. |
| tableId | string The BigQuery table id. |
| datasetId | string The BigQuery dataset id. |


## LookerDataSourceSpec


The specification of a Looker data source.


| JSON representation |
|---|
| { "instanceUri" : string , "model" : string , "explore" : string } |


| Fields |
|---|
| instanceUri | string A Looker instance URL. |
| model | string Name of a Looker model. |
| explore | string Name of a Looker model explore. |


## DataSourceParameter


A parameter in a data source's query. The parameter allows the user to pass in values from the spreadsheet into a query.


| JSON representation |
|---|
| { "name" : string "namedRangeId" : string , "range" : { object ( GridRange ) } } |


| Fields |
|---|
| Union field identifier . The parameter identifier. identifier can be only one of the following: |
| name | string Named parameter. Must be a legitimate identifier for the DataSource that supports it. For example, BigQuery identifier . |
| Union field value . The parameter value. value can be only one of the following: |
| namedRangeId | string ID of a NamedRange . Its size must be 1x1. |
| range | object ( GridRange ) A range that contains the value of the parameter. Its size must be 1x1. |


## DataSourceRefreshSchedule


Schedule for refreshing the data source.


Data sources in the spreadsheet are refreshed within a time interval. You can specify the start time by clicking the Scheduled Refresh button in the Sheets editor, but the interval is fixed at 4 hours. For example, if you specify a start time of 8 AM , the refresh will take place between 8 AM and 12 PM every day.


| JSON representation |
|---|
| { "enabled" : boolean , "refreshScope" : enum ( DataSourceRefreshScope ) , "nextRun" : { object ( Interval ) } , "dailySchedule" : { object ( DataSourceRefreshDailySchedule ) } , "weeklySchedule" : { object ( DataSourceRefreshWeeklySchedule ) } , "monthlySchedule" : { object ( DataSourceRefreshMonthlySchedule ) } } |


| Fields |
|---|
| enabled | boolean True if the refresh schedule is enabled, or false otherwise. |
| refreshScope | enum ( DataSourceRefreshScope ) The scope of the refresh. Must be ALL_DATA_SOURCES . |
| nextRun | object ( Interval ) Output only. The time interval of the next run. |
| Union field schedule_config . Schedule configurations schedule_config can be only one of the following: |
| dailySchedule | object ( DataSourceRefreshDailySchedule ) Daily refresh schedule. |
| weeklySchedule | object ( DataSourceRefreshWeeklySchedule ) Weekly refresh schedule. |
| monthlySchedule | object ( DataSourceRefreshMonthlySchedule ) Monthly refresh schedule. |


## DataSourceRefreshScope


The data source refresh scopes.


| Enums |
|---|
| DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED | Default value, do not use. |
| ALL_DATA_SOURCES | Refreshes all data sources and their associated data source objects in the spreadsheet. |


## DataSourceRefreshDailySchedule


A schedule for data to refresh every day in a given time interval.


| JSON representation |
|---|
| { "startTime" : { object ( TimeOfDay ) } } |


| Fields |
|---|
| startTime | object ( TimeOfDay ) The start time of a time interval in which a data source refresh is scheduled. Only hours part is used. The time interval size defaults to that in the Sheets editor. |


## TimeOfDay


Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `google.type.Date` and `google.protobuf.Timestamp`.


| JSON representation |
|---|
| { "hours" : integer , "minutes" : integer , "seconds" : integer , "nanos" : integer } |


| Fields |
|---|
| hours | integer Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time. |
| minutes | integer Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59. |
| seconds | integer Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds. |
| nanos | integer Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999. |


## DataSourceRefreshWeeklySchedule


A weekly schedule for data to refresh on specific days in a given time interval.


| JSON representation |
|---|
| { "startTime" : { object ( TimeOfDay ) } , "daysOfWeek" : [ enum ( DayOfWeek ) ] } |


| Fields |
|---|
| startTime | object ( TimeOfDay ) The start time of a time interval in which a data source refresh is scheduled. Only hours part is used. The time interval size defaults to that in the Sheets editor. |
| daysOfWeek[] | enum ( DayOfWeek ) Days of the week to refresh. At least one day must be specified. |


## DayOfWeek


Represents a day of the week.


| Enums |
|---|
| DAY_OF_WEEK_UNSPECIFIED | The day of the week is unspecified. |
| MONDAY | Monday |
| TUESDAY | Tuesday |
| WEDNESDAY | Wednesday |
| THURSDAY | Thursday |
| FRIDAY | Friday |
| SATURDAY | Saturday |
| SUNDAY | Sunday |


## DataSourceRefreshMonthlySchedule


A monthly schedule for data to refresh on specific days in the month in a given time interval.


| JSON representation |
|---|
| { "startTime" : { object ( TimeOfDay ) } , "daysOfMonth" : [ integer ] } |


| Fields |
|---|
| startTime | object ( TimeOfDay ) The start time of a time interval in which a data source refresh is scheduled. Only hours part is used. The time interval size defaults to that in the Sheets editor. |
| daysOfMonth[] | integer Days of the month to refresh. Only 1-28 are supported, mapping to the 1st to the 28th day. At least one day must be specified. |


## Interval


Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).


The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.


| JSON representation |
|---|
| { "startTime" : string , "endTime" : string } |


| Fields |
|---|
| startTime | string ( Timestamp format) Optional. Inclusive start of the interval. If specified, a Timestamp matching this interval will have to be the same or after the start. |
| endTime | string ( Timestamp format) Optional. Exclusive end of the interval. If specified, a Timestamp matching this interval will have to be before the end. |


| Methods |
|---|
| batchUpdate | Applies one or more updates to the spreadsheet. |
| create | Creates a spreadsheet, returning the newly created spreadsheet. |
| get | Returns the spreadsheet at the given ID. |
| getByDataFilter | Returns the spreadsheet at the given ID. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]