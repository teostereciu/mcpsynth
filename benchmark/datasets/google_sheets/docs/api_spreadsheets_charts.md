# Charts

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/charts*

---

# Charts


## EmbeddedChart


A chart embedded in a sheet.


| JSON representation |
|---|
| { "chartId" : integer , "spec" : { object ( ChartSpec ) } , "position" : { object ( EmbeddedObjectPosition ) } , "border" : { object ( EmbeddedObjectBorder ) } } |


| Fields |
|---|
| chartId | integer The ID of the chart. |
| spec | object ( ChartSpec ) The specification of the chart. |
| position | object ( EmbeddedObjectPosition ) The position of the chart. |
| border | object ( EmbeddedObjectBorder ) The border of the chart. |


## ChartSpec


The specifications of a chart.


| JSON representation |
|---|
| { "title" : string , "altText" : string , "titleTextFormat" : { object ( TextFormat ) } , "titleTextPosition" : { object ( TextPosition ) } , "subtitle" : string , "subtitleTextFormat" : { object ( TextFormat ) } , "subtitleTextPosition" : { object ( TextPosition ) } , "fontName" : string , "maximized" : boolean , "backgroundColor" : { object ( Color ) } , "backgroundColorStyle" : { object ( ColorStyle ) } , "dataSourceChartProperties" : { object ( DataSourceChartProperties ) } , "filterSpecs" : [ { object ( FilterSpec ) } ] , "sortSpecs" : [ { object ( SortSpec ) } ] , "hiddenDimensionStrategy" : enum ( ChartHiddenDimensionStrategy ) , "basicChart" : { object ( BasicChartSpec ) } , "pieChart" : { object ( PieChartSpec ) } , "bubbleChart" : { object ( BubbleChartSpec ) } , "candlestickChart" : { object ( CandlestickChartSpec ) } , "orgChart" : { object ( OrgChartSpec ) } , "histogramChart" : { object ( HistogramChartSpec ) } , "waterfallChart" : { object ( WaterfallChartSpec ) } , "treemapChart" : { object ( TreemapChartSpec ) } , "scorecardChart" : { object ( ScorecardChartSpec ) } } |


| Fields |
|---|
| title | string The title of the chart. |
| altText | string The alternative text that describes the chart. This is often used for accessibility. |
| titleTextFormat | object ( TextFormat ) The title text format. Strikethrough, underline, and link are not supported. |
| titleTextPosition | object ( TextPosition ) The title text position. This field is optional. |
| subtitle | string The subtitle of the chart. |
| subtitleTextFormat | object ( TextFormat ) The subtitle text format. Strikethrough, underline, and link are not supported. |
| subtitleTextPosition | object ( TextPosition ) The subtitle text position. This field is optional. |
| fontName | string The name of the font to use by default for all chart text (e.g. title, axis labels, legend). If a font is specified for a specific part of the chart it will override this font name. |
| maximized | boolean True to make a chart fill the entire space in which it's rendered with minimum padding. False to use the default padding. (Not applicable to Geo and Org charts.) |
| backgroundColor (deprecated) | object ( Color ) This item is deprecated! The background color of the entire chart. Not applicable to Org charts. Deprecated: Use backgroundColorStyle . |
| backgroundColorStyle | object ( ColorStyle ) The background color of the entire chart. Not applicable to Org charts. If backgroundColor is also set, this field takes precedence. |
| dataSourceChartProperties | object ( DataSourceChartProperties ) If present, the field contains data source chart specific properties. |
| filterSpecs[] | object ( FilterSpec ) The filters applied to the source data of the chart. Only supported for data source charts. |
| sortSpecs[] | object ( SortSpec ) The order to sort the chart data by. Only a single sort spec is supported. Only supported for data source charts. |
| hiddenDimensionStrategy | enum ( ChartHiddenDimensionStrategy ) Determines how the charts will use hidden rows or columns. |
| Union field chart . The specific chart specification, exactly one value must be set. chart can be only one of the following: |
| basicChart | object ( BasicChartSpec ) A basic chart specification, can be one of many kinds of charts. See BasicChartType for the list of all charts this supports. |
| pieChart | object ( PieChartSpec ) A pie chart specification. |
| bubbleChart | object ( BubbleChartSpec ) A bubble chart specification. |
| candlestickChart | object ( CandlestickChartSpec ) A candlestick chart specification. |
| orgChart | object ( OrgChartSpec ) An org chart specification. |
| histogramChart | object ( HistogramChartSpec ) A histogram chart specification. |
| waterfallChart | object ( WaterfallChartSpec ) A waterfall chart specification. |
| treemapChart | object ( TreemapChartSpec ) A treemap chart specification. |
| scorecardChart | object ( ScorecardChartSpec ) A scorecard chart specification. |


## TextPosition


Position settings for text.


| JSON representation |
|---|
| { "horizontalAlignment" : enum ( HorizontalAlign ) } |


| Fields |
|---|
| horizontalAlignment | enum ( HorizontalAlign ) Horizontal alignment setting for the piece of text. |


## DataSourceChartProperties


Properties of a data source chart.


| JSON representation |
|---|
| { "dataSourceId" : string , "dataExecutionStatus" : { object ( DataExecutionStatus ) } } |


| Fields |
|---|
| dataSourceId | string ID of the data source that the chart is associated with. |
| dataExecutionStatus | object ( DataExecutionStatus ) Output only. The data execution status. |


## BasicChartSpec


The specification for a basic chart. See
   `BasicChartType`
   for the list of charts this supports.


| JSON representation |
|---|
| { "chartType" : enum ( BasicChartType ) , "legendPosition" : enum ( BasicChartLegendPosition ) , "axis" : [ { object ( BasicChartAxis ) } ] , "domains" : [ { object ( BasicChartDomain ) } ] , "series" : [ { object ( BasicChartSeries ) } ] , "headerCount" : integer , "threeDimensional" : boolean , "interpolateNulls" : boolean , "stackedType" : enum ( BasicChartStackedType ) , "lineSmoothing" : boolean , "compareMode" : enum ( BasicChartCompareMode ) , "totalDataLabel" : { object ( DataLabel ) } } |


| Fields |
|---|
| chartType | enum ( BasicChartType ) The type of the chart. |
| legendPosition | enum ( BasicChartLegendPosition ) The position of the chart legend. |
| axis[] | object ( BasicChartAxis ) The axis on the chart. |
| domains[] | object ( BasicChartDomain ) The domain of data this is charting. Only a single domain is supported. |
| series[] | object ( BasicChartSeries ) The data this chart is visualizing. |
| headerCount | integer The number of rows or columns in the data that are "headers". If not set, Google Sheets will guess how many rows are headers based on the data. (Note that BasicChartAxis.title may override the axis title  inferred from the header values.) |
| threeDimensional | boolean True to make the chart 3D. Applies to Bar and Column charts. |
| interpolateNulls | boolean If some values in a series are missing, gaps may appear in the chart (e.g, segments of lines in a line chart will be missing). To eliminate these gaps set this to true. Applies to Line, Area, and Combo charts. |
| stackedType | enum ( BasicChartStackedType ) The stacked type for charts that support vertical stacking. Applies to Area, Bar, Column, Combo, and Stepped Area charts. |
| lineSmoothing | boolean Gets whether all lines should be rendered smooth or straight by default. Applies to Line charts. |
| compareMode | enum ( BasicChartCompareMode ) The behavior of tooltips and data highlighting when hovering on data and chart area. |
| totalDataLabel | object ( DataLabel ) Controls whether to display additional data labels on stacked charts which sum the total value of all stacked values at each value along the domain axis. These data labels can only be set when chartType is one of AREA , BAR , COLUMN , COMBO or STEPPED_AREA and stackedType is either STACKED or PERCENT_STACKED . In addition, for COMBO , this will only be supported if there is only one type of stackable series type or one type has more series than the others and each of the other types have no more than one series. For example, if a chart has two stacked bar series and one area series, the total data labels will be supported. If it has three bar series and two area series, total data labels are not allowed. Neither CUSTOM nor placement can be set on the totalDataLabel . |


## BasicChartType


How the chart should be visualized.


| Enums |
|---|
| BASIC_CHART_TYPE_UNSPECIFIED | Default value, do not use. |
| BAR | A bar chart . |
| LINE | A line chart . |
| AREA | An area chart . |
| COLUMN | A column chart . |
| SCATTER | A scatter chart . |
| COMBO | A combo chart . |
| STEPPED_AREA | A stepped area chart . |


## BasicChartLegendPosition


Where the legend of the chart should be positioned.


| Enums |
|---|
| BASIC_CHART_LEGEND_POSITION_UNSPECIFIED | Default value, do not use. |
| BOTTOM_LEGEND | The legend is rendered on the bottom of the chart. |
| LEFT_LEGEND | The legend is rendered on the left of the chart. |
| RIGHT_LEGEND | The legend is rendered on the right of the chart. |
| TOP_LEGEND | The legend is rendered on the top of the chart. |
| NO_LEGEND | No legend is rendered. |


## BasicChartAxis


An axis of the chart. A chart may not have more than one axis per
   `axis position`.


| JSON representation |
|---|
| { "position" : enum ( BasicChartAxisPosition ) , "title" : string , "format" : { object ( TextFormat ) } , "titleTextPosition" : { object ( TextPosition ) } , "viewWindowOptions" : { object ( ChartAxisViewWindowOptions ) } } |


| Fields |
|---|
| position | enum ( BasicChartAxisPosition ) The position of this axis. |
| title | string The title of this axis. If set, this overrides any title inferred from headers of the data. |
| format | object ( TextFormat ) The format of the title. Only valid if the axis is not associated with the domain. The link field is not supported. |
| titleTextPosition | object ( TextPosition ) The axis title text position. |
| viewWindowOptions | object ( ChartAxisViewWindowOptions ) The view window options for this axis. |


## BasicChartAxisPosition


The position of a chart axis.


| Enums |
|---|
| BASIC_CHART_AXIS_POSITION_UNSPECIFIED | Default value, do not use. |
| BOTTOM_AXIS | The axis rendered at the bottom of a chart. For most charts, this is the standard major axis. For bar charts, this is a minor axis. |
| LEFT_AXIS | The axis rendered at the left of a chart. For most charts, this is a minor axis. For bar charts, this is the standard major axis. |
| RIGHT_AXIS | The axis rendered at the right of a chart. For most charts, this is a minor axis. For bar charts, this is an unusual major axis. |


## ChartAxisViewWindowOptions


The options that define a "view window" for a chart (such as the visible values in an axis).


| JSON representation |
|---|
| { "viewWindowMin" : number , "viewWindowMax" : number , "viewWindowMode" : enum ( ViewWindowMode ) } |


| Fields |
|---|
| viewWindowMin | number The minimum numeric value to be shown in this view window. If unset, will automatically determine a minimum value that looks good for the data. |
| viewWindowMax | number The maximum numeric value to be shown in this view window. If unset, will automatically determine a maximum value that looks good for the data. |
| viewWindowMode | enum ( ViewWindowMode ) The view window's mode. |


## ViewWindowMode


The view window's mode. It defines how to treat the min and max of the view window.


| Enums |
|---|
| DEFAULT_VIEW_WINDOW_MODE | The default view window mode used in the Sheets editor for this chart type. In most cases, if set, the default mode is equivalent to PRETTY . |
| VIEW_WINDOW_MODE_UNSUPPORTED | Do not use. Represents that the currently set mode is not supported by the API. |
| EXPLICIT | Follows the min and max exactly if specified. If a value is unspecified, it will fall back to the PRETTY value. |
| PRETTY | Chooses a min and max that make the chart look good. Both min and max are ignored in this mode. |


## BasicChartDomain


The domain of a chart. For example, if charting stock prices over time, this would be the date.


| JSON representation |
|---|
| { "domain" : { object ( ChartData ) } , "reversed" : boolean } |


| Fields |
|---|
| domain | object ( ChartData ) The data of the domain. For example, if charting stock prices over time, this is the data representing the dates. |
| reversed | boolean True to reverse the order of the domain values (horizontal axis). |


## ChartData


The data included in a domain or series.


| JSON representation |
|---|
| { "groupRule" : { object ( ChartGroupRule ) } , "aggregateType" : enum ( ChartAggregateType ) , "sourceRange" : { object ( ChartSourceRange ) } , "columnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| groupRule | object ( ChartGroupRule ) The rule to group the data by if the ChartData backs the domain of a data source chart. Only supported for data source charts. |
| aggregateType | enum ( ChartAggregateType ) The aggregation type for the series of a data source chart. Only supported for data source charts. |
| Union field type . The type of data included, exactly one value must be set. type can be only one of the following: |
| sourceRange | object ( ChartSourceRange ) The source ranges of the data. |
| columnReference | object ( DataSourceColumnReference ) The reference to the data source column that the data reads from. |


## ChartSourceRange


Source ranges for a chart.


| JSON representation |
|---|
| { "sources" : [ { object ( GridRange ) } ] } |


| Fields |
|---|
| sources[] | object ( GridRange ) The ranges of data for a series or domain. Exactly one dimension must have a length of 1, and all sources in the list must have the same dimension with length 1. The domain (if it exists) & all series must have the same number of source ranges. If using more than one source range, then the source range at a given offset must be in order and contiguous across the domain and series. For example, these are valid configurations: domain sources: A1:A5
series1 sources: B1:B5
series2 sources: D6:D10

domain sources: A1:A5, C10:C12
series1 sources: B1:B5, D10:D12
series2 sources: C1:C5, E10:E12 |


## ChartGroupRule


An optional setting on the
   `ChartData`
   of the domain of a data source chart that defines buckets for the values in the domain rather than breaking out each individual value.


For example, when plotting a data source chart, you can specify a histogram rule on the domain (it should only contain numeric values), grouping its values into buckets. Any values of a chart series that fall into the same bucket are aggregated based on the
   `aggregateType`.


| JSON representation |
|---|
| { "dateTimeRule" : { object ( ChartDateTimeRule ) } , "histogramRule" : { object ( ChartHistogramRule ) } } |


| Fields |
|---|
| Union field rule . The rule to apply to the ChartData . rule can be only one of the following: |
| dateTimeRule | object ( ChartDateTimeRule ) A ChartDateTimeRule . |
| histogramRule | object ( ChartHistogramRule ) A ChartHistogramRule |


## ChartDateTimeRule


Allows you to organize the date-time values in a source data column into buckets based on selected parts of their date or time values.


| JSON representation |
|---|
| { "type" : enum ( ChartDateTimeRuleType ) } |


| Fields |
|---|
| type | enum ( ChartDateTimeRuleType ) The type of date-time grouping to apply. |


## ChartDateTimeRuleType


The available types of date-time grouping rules.


| Enums |
|---|
| CHART_DATE_TIME_RULE_TYPE_UNSPECIFIED | The default type, do not use. |
| SECOND | Group dates by second, from 0 to 59. |
| MINUTE | Group dates by minute, from 0 to 59. |
| HOUR | Group dates by hour using a 24-hour system, from 0 to 23. |
| HOUR_MINUTE | Group dates by hour and minute using a 24-hour system, for example 19:45. |
| HOUR_MINUTE_AMPM | Group dates by hour and minute using a 12-hour system, for example 7:45 PM. The AM/PM designation is translated based on the spreadsheet locale. |
| DAY_OF_WEEK | Group dates by day of week, for example Sunday. The days of the week will be translated based on the spreadsheet locale. |
| DAY_OF_YEAR | Group dates by day of year, from 1 to 366. Note that dates after Feb. 29 fall in different buckets in leap years than in non-leap years. |
| DAY_OF_MONTH | Group dates by day of month, from 1 to 31. |
| DAY_MONTH | Group dates by day and month, for example 22-Nov. The month is translated based on the spreadsheet locale. |
| MONTH | Group dates by month, for example Nov. The month is translated based on the spreadsheet locale. |
| QUARTER | Group dates by quarter, for example Q1 (which represents Jan-Mar). |
| YEAR | Group dates by year, for example 2008. |
| YEAR_MONTH | Group dates by year and month, for example 2008-Nov. The month is translated based on the spreadsheet locale. |
| YEAR_QUARTER | Group dates by year and quarter, for example 2008 Q4. |
| YEAR_MONTH_DAY | Group dates by year, month, and day, for example 2008-11-22. |


## ChartHistogramRule


Allows you to organize numeric values in a source data column into buckets of constant size.


| JSON representation |
|---|
| { "minValue" : number , "maxValue" : number , "intervalSize" : number } |


| Fields |
|---|
| minValue | number The minimum value at which items are placed into buckets. Values that are less than the minimum are grouped into a single bucket. If omitted, it is determined by the minimum item value. |
| maxValue | number The maximum value at which items are placed into buckets. Values greater than the maximum are grouped into a single bucket. If omitted, it is determined by the maximum item value. |
| intervalSize | number The size of the buckets that are created. Must be positive. |


## ChartAggregateType


The type of aggregation for chart series.


| Enums |
|---|
| CHART_AGGREGATE_TYPE_UNSPECIFIED | Default value, do not use. |
| AVERAGE | Average aggregate function. |
| COUNT | Count aggregate function. |
| MAX | Maximum aggregate function. |
| MEDIAN | Median aggregate function. |
| MIN | Minimum aggregate function. |
| SUM | Sum aggregate function. |


## BasicChartSeries


A single series of data in a chart. For example, if charting stock prices over time, multiple series may exist, one for the "Open Price", "High Price", "Low Price" and "Close Price".


| JSON representation |
|---|
| { "series" : { object ( ChartData ) } , "targetAxis" : enum ( BasicChartAxisPosition ) , "type" : enum ( BasicChartType ) , "lineStyle" : { object ( LineStyle ) } , "dataLabel" : { object ( DataLabel ) } , "color" : { object ( Color ) } , "colorStyle" : { object ( ColorStyle ) } , "pointStyle" : { object ( PointStyle ) } , "styleOverrides" : [ { object ( BasicSeriesDataPointStyleOverride ) } ] } |


| Fields |
|---|
| series | object ( ChartData ) The data being visualized in this chart series. |
| targetAxis | enum ( BasicChartAxisPosition ) The minor axis that will specify the range of values for this series. For example, if charting stocks over time, the "Volume" series may want to be pinned to the right with the prices pinned to the left, because the scale of trading volume is different than the scale of prices. It is an error to specify an axis that isn't a valid minor axis for the chart's type . |
| type | enum ( BasicChartType ) The type of this series. Valid only if the chartType is COMBO . Different types will change the way the series is visualized. Only LINE , AREA , and COLUMN are supported. |
| lineStyle | object ( LineStyle ) The line style of this series. Valid only if the chartType is AREA , LINE , or SCATTER . COMBO charts are also supported if the series chart type is AREA or LINE . |
| dataLabel | object ( DataLabel ) Information about the data labels for this series. |
| color (deprecated) | object ( Color ) This item is deprecated! The color for elements (such as bars, lines, and points) associated with this series. If empty, a default color is used. Deprecated: Use colorStyle . |
| colorStyle | object ( ColorStyle ) The color for elements (such as bars, lines, and points) associated with this series. If empty, a default color is used. If color is also set, this field takes precedence. |
| pointStyle | object ( PointStyle ) The style for points associated with this series. Valid only if the chartType is AREA , LINE , or SCATTER . COMBO charts are also supported if the series chart type is AREA , LINE , or SCATTER . If empty, a default point style is used. |
| styleOverrides[] | object ( BasicSeriesDataPointStyleOverride ) Style override settings for series data points. |


## LineStyle


Properties that describe the style of a line.


| JSON representation |
|---|
| { "width" : integer , "type" : enum ( LineDashType ) } |


| Fields |
|---|
| width | integer The thickness of the line, in px. |
| type | enum ( LineDashType ) The dash type of the line. |


## LineDashType


The dash type of a line.


| Enums |
|---|
| LINE_DASH_TYPE_UNSPECIFIED | Default value, do not use. |
| INVISIBLE | No dash type, which is equivalent to a non-visible line. |
| CUSTOM | A custom dash for a line. Modifying the exact custom dash style is currently unsupported. |
| SOLID | A solid line. |
| DOTTED | A dotted line. |
| MEDIUM_DASHED | A dashed line where the dashes have "medium" length. |
| MEDIUM_DASHED_DOTTED | A line that alternates between a "medium" dash and a dot. |
| LONG_DASHED | A dashed line where the dashes have "long" length. |
| LONG_DASHED_DOTTED | A line that alternates between a "long" dash and a dot. |


## DataLabel


Settings for one set of data labels. Data labels are annotations that appear next to a set of data, such as the points on a line chart, and provide additional information about what the data represents, such as a text representation of the value behind that point on the graph.


| JSON representation |
|---|
| { "type" : enum ( DataLabelType ) , "textFormat" : { object ( TextFormat ) } , "placement" : enum ( DataLabelPlacement ) , "customLabelData" : { object ( ChartData ) } } |


| Fields |
|---|
| type | enum ( DataLabelType ) The type of the data label. |
| textFormat | object ( TextFormat ) The text format used for the data label. The link field is not supported. |
| placement | enum ( DataLabelPlacement ) The placement of the data label relative to the labeled data. |
| customLabelData | object ( ChartData ) Data to use for custom labels. Only used if type is set to CUSTOM . This data must be the same length as the series or other element this data label is applied to. In addition, if the series is split into multiple source ranges, this source data must come from the next column in the source data. For example, if the series is B2:B4,E6:E8 then this data must come from C2:C4,F6:F8. |


## DataLabelType


The type of a data label.


| Enums |
|---|
| DATA_LABEL_TYPE_UNSPECIFIED | The data label type is not specified and will be interpreted depending on the context of the data label within the chart. |
| NONE | The data label is not displayed. |
| DATA | The data label is displayed using values from the series data. |
| CUSTOM | The data label is displayed using values from a custom data source indicated by customLabelData . |


## DataLabelPlacement


The placement of a data label relative to the labeled data.


| Enums |
|---|
| DATA_LABEL_PLACEMENT_UNSPECIFIED | The positioning is determined automatically by the renderer. |
| CENTER | Center within a bar or column, both horizontally and vertically. |
| LEFT | To the left of a data point. |
| RIGHT | To the right of a data point. |
| ABOVE | Above a data point. |
| BELOW | Below a data point. |
| INSIDE_END | Inside a bar or column at the end (top if positive, bottom if negative). |
| INSIDE_BASE | Inside a bar or column at the base. |
| OUTSIDE_END | Outside a bar or column at the end. |


## PointStyle


The style of a point on the chart.


| JSON representation |
|---|
| { "size" : number , "shape" : enum ( PointShape ) } |


| Fields |
|---|
| size | number The point size. If empty, a default size is used. |
| shape | enum ( PointShape ) The point shape. If empty or unspecified, a default shape is used. |


## PointShape


The shape of a point.


| Enums |
|---|
| POINT_SHAPE_UNSPECIFIED | Default value. |
| CIRCLE | A circle shape. |
| DIAMOND | A diamond shape. |
| HEXAGON | A hexagon shape. |
| PENTAGON | A pentagon shape. |
| SQUARE | A square shape. |
| STAR | A star shape. |
| TRIANGLE | A triangle shape. |
| X_MARK | An x-mark shape. |


## BasicSeriesDataPointStyleOverride


Style override settings for a single series data point.


| JSON representation |
|---|
| { "index" : integer , "color" : { object ( Color ) } , "colorStyle" : { object ( ColorStyle ) } , "pointStyle" : { object ( PointStyle ) } } |


| Fields |
|---|
| index | integer The zero-based index of the series data point. |
| color (deprecated) | object ( Color ) This item is deprecated! Color of the series data point. If empty, the series default is used. Deprecated: Use colorStyle . |
| colorStyle | object ( ColorStyle ) Color of the series data point. If empty, the series default is used. If color is also set, this field takes precedence. |
| pointStyle | object ( PointStyle ) Point style of the series data point. Valid only if the chartType is AREA , LINE , or SCATTER . COMBO charts are also supported if the series chart type is AREA , LINE , or SCATTER . If empty, the series default is used. |


## BasicChartStackedType


When charts are stacked, range (vertical axis) values are rendered on top of one another rather than from the horizontal axis. For example, the two values 20 and 80 would be drawn from 0, with 80 being 80 units away from the horizontal axis. If they were stacked, 80 would be rendered from 20, putting it 100 units away from the horizontal axis.


| Enums |
|---|
| BASIC_CHART_STACKED_TYPE_UNSPECIFIED | Default value, do not use. |
| NOT_STACKED | Series are not stacked. |
| STACKED | Series values are stacked, each value is rendered vertically beginning from the top of the value below it. |
| PERCENT_STACKED | Vertical stacks are stretched to reach the top of the chart, with values laid out as percentages of each other. |


## BasicChartCompareMode


The compare mode type, which describes the behavior of tooltips and data highlighting when hovering on data and chart area.


| Enums |
|---|
| BASIC_CHART_COMPARE_MODE_UNSPECIFIED | Default value, do not use. |
| DATUM | Only the focused data element is highlighted and shown in the tooltip. |
| CATEGORY | All data elements with the same category (e.g., domain value) are highlighted and shown in the tooltip. |


## PieChartSpec


A
   [pie chart](/chart/interactive/docs/gallery/piechart).


| JSON representation |
|---|
| { "legendPosition" : enum ( PieChartLegendPosition ) , "domain" : { object ( ChartData ) } , "series" : { object ( ChartData ) } , "threeDimensional" : boolean , "pieHole" : number } |


| Fields |
|---|
| legendPosition | enum ( PieChartLegendPosition ) Where the legend of the pie chart should be drawn. |
| domain | object ( ChartData ) The data that covers the domain of the pie chart. |
| series | object ( ChartData ) The data that covers the one and only series of the pie chart. |
| threeDimensional | boolean True if the pie is three dimensional. |
| pieHole | number The size of the hole in the pie chart. |


## PieChartLegendPosition


Where the legend of the chart should be positioned.


| Enums |
|---|
| PIE_CHART_LEGEND_POSITION_UNSPECIFIED | Default value, do not use. |
| BOTTOM_LEGEND | The legend is rendered on the bottom of the chart. |
| LEFT_LEGEND | The legend is rendered on the left of the chart. |
| RIGHT_LEGEND | The legend is rendered on the right of the chart. |
| TOP_LEGEND | The legend is rendered on the top of the chart. |
| NO_LEGEND | No legend is rendered. |
| LABELED_LEGEND | Each pie slice has a label attached to it. |


## BubbleChartSpec


A
   [bubble chart](/chart/interactive/docs/gallery/bubblechart).


| JSON representation |
|---|
| { "legendPosition" : enum ( BubbleChartLegendPosition ) , "bubbleLabels" : { object ( ChartData ) } , "domain" : { object ( ChartData ) } , "series" : { object ( ChartData ) } , "groupIds" : { object ( ChartData ) } , "bubbleSizes" : { object ( ChartData ) } , "bubbleOpacity" : number , "bubbleBorderColor" : { object ( Color ) } , "bubbleBorderColorStyle" : { object ( ColorStyle ) } , "bubbleMaxRadiusSize" : integer , "bubbleMinRadiusSize" : integer , "bubbleTextStyle" : { object ( TextFormat ) } } |


| Fields |
|---|
| legendPosition | enum ( BubbleChartLegendPosition ) Where the legend of the chart should be drawn. |
| bubbleLabels | object ( ChartData ) The data containing the bubble labels. These do not need to be unique. |
| domain | object ( ChartData ) The data containing the bubble x-values. These values locate the bubbles in the chart horizontally. |
| series | object ( ChartData ) The data containing the bubble y-values. These values locate the bubbles in the chart vertically. |
| groupIds | object ( ChartData ) The data containing the bubble group IDs. All bubbles with the same group ID are drawn in the same color. If bubbleSizes is specified then this field must also be specified but may contain blank values. This field is optional. |
| bubbleSizes | object ( ChartData ) The data containing the bubble sizes. Bubble sizes are used to draw the bubbles at different sizes relative to each other. If specified, groupIds must also be specified. This field is optional. |
| bubbleOpacity | number The opacity of the bubbles between 0 and 1.0. 0 is fully transparent and 1 is fully opaque. |
| bubbleBorderColor (deprecated) | object ( Color ) This item is deprecated! The bubble border color. Deprecated: Use bubbleBorderColorStyle . |
| bubbleBorderColorStyle | object ( ColorStyle ) The bubble border color. If bubbleBorderColor is also set, this field takes precedence. |
| bubbleMaxRadiusSize | integer The max radius size of the bubbles, in pixels. If specified, the field must be a positive value. |
| bubbleMinRadiusSize | integer The minimum radius size of the bubbles, in pixels. If specific, the field must be a positive value. |
| bubbleTextStyle | object ( TextFormat ) The format of the text inside the bubbles. Strikethrough, underline, and link are not supported. |


## BubbleChartLegendPosition


Where the legend of the chart should be positioned.


| Enums |
|---|
| BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED | Default value, do not use. |
| BOTTOM_LEGEND | The legend is rendered on the bottom of the chart. |
| LEFT_LEGEND | The legend is rendered on the left of the chart. |
| RIGHT_LEGEND | The legend is rendered on the right of the chart. |
| TOP_LEGEND | The legend is rendered on the top of the chart. |
| NO_LEGEND | No legend is rendered. |
| INSIDE_LEGEND | The legend is rendered inside the chart area. |


## CandlestickChartSpec


A
   [candlestick chart](/chart/interactive/docs/gallery/candlestickchart).


| JSON representation |
|---|
| { "domain" : { object ( CandlestickDomain ) } , "data" : [ { object ( CandlestickData ) } ] } |


| Fields |
|---|
| domain | object ( CandlestickDomain ) The domain data (horizontal axis) for the candlestick chart. String data will be treated as discrete labels, other data will be treated as continuous values. |
| data[] | object ( CandlestickData ) The Candlestick chart data. Only one CandlestickData is supported. |


## CandlestickDomain


The domain of a CandlestickChart.


| JSON representation |
|---|
| { "data" : { object ( ChartData ) } , "reversed" : boolean } |


| Fields |
|---|
| data | object ( ChartData ) The data of the CandlestickDomain. |
| reversed | boolean True to reverse the order of the domain values (horizontal axis). |


## CandlestickData


The Candlestick chart data, each containing the low, open, close, and high values for a series.


| JSON representation |
|---|
| { "lowSeries" : { object ( CandlestickSeries ) } , "openSeries" : { object ( CandlestickSeries ) } , "closeSeries" : { object ( CandlestickSeries ) } , "highSeries" : { object ( CandlestickSeries ) } } |


| Fields |
|---|
| lowSeries | object ( CandlestickSeries ) The range data (vertical axis) for the low/minimum value for each candle. This is the bottom of the candle's center line. |
| openSeries | object ( CandlestickSeries ) The range data (vertical axis) for the open/initial value for each candle. This is the bottom of the candle body. If less than the close value the candle will be filled. Otherwise the candle will be hollow. |
| closeSeries | object ( CandlestickSeries ) The range data (vertical axis) for the close/final value for each candle. This is the top of the candle body. If greater than the open value the candle will be filled. Otherwise the candle will be hollow. |
| highSeries | object ( CandlestickSeries ) The range data (vertical axis) for the high/maximum value for each candle. This is the top of the candle's center line. |


## CandlestickSeries


The series of a CandlestickData.


| JSON representation |
|---|
| { "data" : { object ( ChartData ) } } |


| Fields |
|---|
| data | object ( ChartData ) The data of the CandlestickSeries. |


## OrgChartSpec


An
   [org chart](/chart/interactive/docs/gallery/orgchart). Org charts require a unique set of labels in
   `labels`
   and may optionally include
   `parentLabels`
   and
   `tooltips`.
   `parentLabels`
   contain, for each node, the label identifying the parent node.
   `tooltips`
   contain, for each node, an optional tooltip.


For example, to describe an OrgChart with Alice as the CEO, Bob as the President (reporting to Alice) and Cathy as VP of Sales (also reporting to Alice), have
   `labels`
   contain "Alice", "Bob", "Cathy",
   `parentLabels`
   contain "", "Alice", "Alice" and
   `tooltips`
   contain "CEO", "President", "VP Sales".


| JSON representation |
|---|
| { "nodeSize" : enum ( OrgChartNodeSize ) , "nodeColor" : { object ( Color ) } , "nodeColorStyle" : { object ( ColorStyle ) } , "selectedNodeColor" : { object ( Color ) } , "selectedNodeColorStyle" : { object ( ColorStyle ) } , "labels" : { object ( ChartData ) } , "parentLabels" : { object ( ChartData ) } , "tooltips" : { object ( ChartData ) } } |


| Fields |
|---|
| nodeSize | enum ( OrgChartNodeSize ) The size of the org chart nodes. |
| nodeColor (deprecated) | object ( Color ) This item is deprecated! The color of the org chart nodes. Deprecated: Use nodeColorStyle . |
| nodeColorStyle | object ( ColorStyle ) The color of the org chart nodes. If nodeColor is also set, this field takes precedence. |
| selectedNodeColor (deprecated) | object ( Color ) This item is deprecated! The color of the selected org chart nodes. Deprecated: Use selectedNodeColorStyle . |
| selectedNodeColorStyle | object ( ColorStyle ) The color of the selected org chart nodes. If selectedNodeColor is also set, this field takes precedence. |
| labels | object ( ChartData ) The data containing the labels for all the nodes in the chart. Labels must be unique. |
| parentLabels | object ( ChartData ) The data containing the label of the parent for the corresponding node. A blank value indicates that the node has no parent and is a top-level node. This field is optional. |
| tooltips | object ( ChartData ) The data containing the tooltip for the corresponding node. A blank value results in no tooltip being displayed for the node. This field is optional. |


## OrgChartNodeSize


The size of the org chart nodes.


| Enums |
|---|
| ORG_CHART_LABEL_SIZE_UNSPECIFIED | Default value, do not use. |
| SMALL | The small org chart node size. |
| MEDIUM | The medium org chart node size. |
| LARGE | The large org chart node size. |


## HistogramChartSpec


A
   [histogram chart](/chart/interactive/docs/gallery/histogram). A histogram chart groups data items into bins, displaying each bin as a column of stacked items. Histograms are used to display the distribution of a dataset. Each column of items represents a range into which those items fall. The number of bins can be chosen automatically or specified explicitly.


| JSON representation |
|---|
| { "series" : [ { object ( HistogramSeries ) } ] , "legendPosition" : enum ( HistogramChartLegendPosition ) , "showItemDividers" : boolean , "bucketSize" : number , "outlierPercentile" : number } |


| Fields |
|---|
| series[] | object ( HistogramSeries ) The series for a histogram may be either a single series of values to be bucketed or multiple series, each of the same length, containing the name of the series followed by the values to be bucketed for that series. |
| legendPosition | enum ( HistogramChartLegendPosition ) The position of the chart legend. |
| showItemDividers | boolean Whether horizontal divider lines should be displayed between items in each column. |
| bucketSize | number By default the bucket size (the range of values stacked in a single column) is chosen automatically, but it may be overridden here. E.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc. Cannot be negative. This field is optional. |
| outlierPercentile | number The outlier percentile is used to ensure that outliers do not adversely affect the calculation of bucket sizes. For example, setting an outlier percentile of 0.05 indicates that the top and bottom 5% of values when calculating buckets. The values are still included in the chart, they will be added to the first or last buckets instead of their own buckets. Must be between 0.0 and 0.5. |


## HistogramSeries


A histogram series containing the series color and data.


| JSON representation |
|---|
| { "barColor" : { object ( Color ) } , "barColorStyle" : { object ( ColorStyle ) } , "data" : { object ( ChartData ) } } |


| Fields |
|---|
| barColor (deprecated) | object ( Color ) This item is deprecated! The color of the column representing this series in each bucket. This field is optional. Deprecated: Use barColorStyle . |
| barColorStyle | object ( ColorStyle ) The color of the column representing this series in each bucket. This field is optional. If barColor is also set, this field takes precedence. |
| data | object ( ChartData ) The data for this histogram series. |


## HistogramChartLegendPosition


Where the legend of the chart should be positioned.


| Enums |
|---|
| HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED | Default value, do not use. |
| BOTTOM_LEGEND | The legend is rendered on the bottom of the chart. |
| LEFT_LEGEND | The legend is rendered on the left of the chart. |
| RIGHT_LEGEND | The legend is rendered on the right of the chart. |
| TOP_LEGEND | The legend is rendered on the top of the chart. |
| NO_LEGEND | No legend is rendered. |
| INSIDE_LEGEND | The legend is rendered inside the chart area. |


## WaterfallChartSpec


A waterfall chart.


| JSON representation |
|---|
| { "domain" : { object ( WaterfallChartDomain ) } , "series" : [ { object ( WaterfallChartSeries ) } ] , "stackedType" : enum ( WaterfallChartStackedType ) , "firstValueIsTotal" : boolean , "hideConnectorLines" : boolean , "connectorLineStyle" : { object ( LineStyle ) } , "totalDataLabel" : { object ( DataLabel ) } } |


| Fields |
|---|
| domain | object ( WaterfallChartDomain ) The domain data (horizontal axis) for the waterfall chart. |
| series[] | object ( WaterfallChartSeries ) The data this waterfall chart is visualizing. |
| stackedType | enum ( WaterfallChartStackedType ) The stacked type. |
| firstValueIsTotal | boolean True to interpret the first value as a total. |
| hideConnectorLines | boolean True to hide connector lines between columns. |
| connectorLineStyle | object ( LineStyle ) The line style for the connector lines. |
| totalDataLabel | object ( DataLabel ) Controls whether to display additional data labels on stacked charts which sum the total value of all stacked values at each value along the domain axis. stackedType must be STACKED and neither CUSTOM nor placement can be set on the totalDataLabel . |


## WaterfallChartDomain


The domain of a waterfall chart.


| JSON representation |
|---|
| { "data" : { object ( ChartData ) } , "reversed" : boolean } |


| Fields |
|---|
| data | object ( ChartData ) The data of the WaterfallChartDomain. |
| reversed | boolean True to reverse the order of the domain values (horizontal axis). |


## WaterfallChartSeries


A single series of data for a waterfall chart.


| JSON representation |
|---|
| { "data" : { object ( ChartData ) } , "positiveColumnsStyle" : { object ( WaterfallChartColumnStyle ) } , "negativeColumnsStyle" : { object ( WaterfallChartColumnStyle ) } , "subtotalColumnsStyle" : { object ( WaterfallChartColumnStyle ) } , "hideTrailingSubtotal" : boolean , "customSubtotals" : [ { object ( WaterfallChartCustomSubtotal ) } ] , "dataLabel" : { object ( DataLabel ) } } |


| Fields |
|---|
| data | object ( ChartData ) The data being visualized in this series. |
| positiveColumnsStyle | object ( WaterfallChartColumnStyle ) Styles for all columns in this series with positive values. |
| negativeColumnsStyle | object ( WaterfallChartColumnStyle ) Styles for all columns in this series with negative values. |
| subtotalColumnsStyle | object ( WaterfallChartColumnStyle ) Styles for all subtotal columns in this series. |
| hideTrailingSubtotal | boolean True to hide the subtotal column from the end of the series. By default, a subtotal column will appear at the end of each series. Setting this field to true will hide that subtotal column for this series. |
| customSubtotals[] | object ( WaterfallChartCustomSubtotal ) Custom subtotal columns appearing in this series. The order in which subtotals are defined is not significant. Only one subtotal may be defined for each data point. |
| dataLabel | object ( DataLabel ) Information about the data labels for this series. |


## WaterfallChartColumnStyle


Styles for a waterfall chart column.


| JSON representation |
|---|
| { "label" : string , "color" : { object ( Color ) } , "colorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| label | string The label of the column's legend. |
| color (deprecated) | object ( Color ) This item is deprecated! The color of the column. Deprecated: Use colorStyle . |
| colorStyle | object ( ColorStyle ) The color of the column. If color is also set, this field takes precedence. |


## WaterfallChartCustomSubtotal


A custom subtotal column for a waterfall chart series.


| JSON representation |
|---|
| { "subtotalIndex" : integer , "label" : string , "dataIsSubtotal" : boolean } |


| Fields |
|---|
| subtotalIndex | integer The zero-based index of a data point within the series. If dataIsSubtotal is true, the data point at this index is the subtotal. Otherwise, the subtotal appears after the data point with this index. A series can have multiple subtotals at arbitrary indices, but subtotals do not affect the indices of the data points. For example, if a series has three data points, their indices will always be 0, 1, and 2, regardless of how many subtotals exist on the series or what data points they are associated with. |
| label | string A label for the subtotal column. |
| dataIsSubtotal | boolean True if the data point at subtotalIndex is the subtotal. If false, the subtotal will be computed and appear after the data point. |


## WaterfallChartStackedType


Stacked type options for waterfall charts.


| Enums |
|---|
| WATERFALL_STACKED_TYPE_UNSPECIFIED | Default value, do not use. |
| STACKED | Values corresponding to the same domain (horizontal axis) value will be stacked vertically. |
| SEQUENTIAL | Series will spread out along the horizontal axis. |


## TreemapChartSpec


A
   [Treemap chart](/chart/interactive/docs/gallery/treemap).


| JSON representation |
|---|
| { "labels" : { object ( ChartData ) } , "parentLabels" : { object ( ChartData ) } , "sizeData" : { object ( ChartData ) } , "colorData" : { object ( ChartData ) } , "textFormat" : { object ( TextFormat ) } , "levels" : integer , "hintedLevels" : integer , "minValue" : number , "maxValue" : number , "headerColor" : { object ( Color ) } , "headerColorStyle" : { object ( ColorStyle ) } , "colorScale" : { object ( TreemapChartColorScale ) } , "hideTooltips" : boolean } |


| Fields |
|---|
| labels | object ( ChartData ) The data that contains the treemap cell labels. |
| parentLabels | object ( ChartData ) The data the contains the treemap cells' parent labels. |
| sizeData | object ( ChartData ) The data that determines the size of each treemap data cell. This data is expected to be numeric. The cells corresponding to non-numeric or missing data will not be rendered. If colorData is not specified, this data is used to determine data cell background colors as well. |
| colorData | object ( ChartData ) The data that determines the background color of each treemap data cell. This field is optional. If not specified, sizeData is used to determine background colors. If specified, the data is expected to be numeric. colorScale will determine how the values in this data map to data cell background colors. |
| textFormat | object ( TextFormat ) The text format for all labels on the chart. The link field is not supported. |
| levels | integer The number of data levels to show on the treemap chart. These levels are interactive and are shown with their labels. Defaults to 2 if not specified. |
| hintedLevels | integer The number of additional data levels beyond the labeled levels to be shown on the treemap chart. These levels are not interactive and are shown without their labels. Defaults to 0 if not specified. |
| minValue | number The minimum possible data value. Cells with values less than this will have the same color as cells with this value. If not specified, defaults to the actual minimum value from colorData , or the minimum value from sizeData if colorData is not specified. |
| maxValue | number The maximum possible data value. Cells with values greater than this will have the same color as cells with this value. If not specified, defaults to the actual maximum value from colorData , or the maximum value from sizeData if colorData is not specified. |
| headerColor (deprecated) | object ( Color ) This item is deprecated! The background color for header cells. Deprecated: Use headerColorStyle . |
| headerColorStyle | object ( ColorStyle ) The background color for header cells. If headerColor is also set, this field takes precedence. |
| colorScale | object ( TreemapChartColorScale ) The color scale for data cells in the treemap chart. Data cells are assigned colors based on their color values. These color values come from colorData , or from sizeData if colorData is not specified. Cells with color values less than or equal to minValue will have minValueColor as their background color. Cells with color values greater than or equal to maxValue will have maxValueColor as their background color. Cells with color values between minValue and maxValue will have background colors on a gradient between minValueColor and maxValueColor , the midpoint of the gradient being midValueColor . Cells with missing or non-numeric color values will have noDataColor as their background color. |
| hideTooltips | boolean True to hide tooltips. |


## TreemapChartColorScale


A color scale for a treemap chart.


| JSON representation |
|---|
| { "minValueColor" : { object ( Color ) } , "minValueColorStyle" : { object ( ColorStyle ) } , "midValueColor" : { object ( Color ) } , "midValueColorStyle" : { object ( ColorStyle ) } , "maxValueColor" : { object ( Color ) } , "maxValueColorStyle" : { object ( ColorStyle ) } , "noDataColor" : { object ( Color ) } , "noDataColorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| minValueColor (deprecated) | object ( Color ) This item is deprecated! The background color for cells with a color value less than or equal to minValue . Defaults to #dc3912 if not specified. Deprecated: Use minValueColorStyle . |
| minValueColorStyle | object ( ColorStyle ) The background color for cells with a color value less than or equal to minValue . Defaults to #dc3912 if not specified. If minValueColor is also set, this field takes precedence. |
| midValueColor (deprecated) | object ( Color ) This item is deprecated! The background color for cells with a color value at the midpoint between minValue and maxValue . Defaults to #efe6dc if not specified. Deprecated: Use midValueColorStyle . |
| midValueColorStyle | object ( ColorStyle ) The background color for cells with a color value at the midpoint between minValue and maxValue . Defaults to #efe6dc if not specified. If midValueColor is also set, this field takes precedence. |
| maxValueColor (deprecated) | object ( Color ) This item is deprecated! The background color for cells with a color value greater than or equal to maxValue . Defaults to #109618 if not specified. Deprecated: Use maxValueColorStyle . |
| maxValueColorStyle | object ( ColorStyle ) The background color for cells with a color value greater than or equal to maxValue . Defaults to #109618 if not specified. If maxValueColor is also set, this field takes precedence. |
| noDataColor (deprecated) | object ( Color ) This item is deprecated! The background color for cells that have no color data associated with them. Defaults to #000000 if not specified. Deprecated: Use noDataColorStyle . |
| noDataColorStyle | object ( ColorStyle ) The background color for cells that have no color data associated with them. Defaults to #000000 if not specified. If noDataColor is also set, this field takes precedence. |


## ScorecardChartSpec


A scorecard chart. Scorecard charts are used to highlight key performance indicators, known as KPIs, on the spreadsheet. A scorecard chart can represent things like total sales, average cost, or a top selling item. You can specify a single data value, or aggregate over a range of data. Percentage or absolute difference from a baseline value can be highlighted, like changes over time.


| JSON representation |
|---|
| { "keyValueData" : { object ( ChartData ) } , "baselineValueData" : { object ( ChartData ) } , "aggregateType" : enum ( ChartAggregateType ) , "keyValueFormat" : { object ( KeyValueFormat ) } , "baselineValueFormat" : { object ( BaselineValueFormat ) } , "scaleFactor" : number , "numberFormatSource" : enum ( ChartNumberFormatSource ) , "customFormatOptions" : { object ( ChartCustomNumberFormatOptions ) } } |


| Fields |
|---|
| keyValueData | object ( ChartData ) The data for scorecard key value. |
| baselineValueData | object ( ChartData ) The data for scorecard baseline value. This field is optional. |
| aggregateType | enum ( ChartAggregateType ) The aggregation type for key and baseline chart data in scorecard chart. This field is not supported for data source charts. Use the ChartData.aggregateType field of the keyValueData or baselineValueData instead for data source charts. This field is optional. |
| keyValueFormat | object ( KeyValueFormat ) Formatting options for key value. |
| baselineValueFormat | object ( BaselineValueFormat ) Formatting options for baseline value. This field is needed only if baselineValueData is specified. |
| scaleFactor | number Value to scale scorecard key and baseline value. For example, a factor of 10 can be used to divide all values in the chart by 10. This field is optional. |
| numberFormatSource | enum ( ChartNumberFormatSource ) The number format source used in the scorecard chart. This field is optional. |
| customFormatOptions | object ( ChartCustomNumberFormatOptions ) Custom formatting options for numeric key/baseline values in scorecard chart. This field is used only when numberFormatSource is set to CUSTOM . This field is optional. |


## KeyValueFormat


Formatting options for key value.


| JSON representation |
|---|
| { "textFormat" : { object ( TextFormat ) } , "position" : { object ( TextPosition ) } } |


| Fields |
|---|
| textFormat | object ( TextFormat ) Text formatting options for key value. The link field is not supported. |
| position | object ( TextPosition ) Specifies the horizontal text positioning of key value. This field is optional. If not specified, default positioning is used. |


## BaselineValueFormat


Formatting options for baseline value.


| JSON representation |
|---|
| { "comparisonType" : enum ( ComparisonType ) , "textFormat" : { object ( TextFormat ) } , "position" : { object ( TextPosition ) } , "description" : string , "positiveColor" : { object ( Color ) } , "positiveColorStyle" : { object ( ColorStyle ) } , "negativeColor" : { object ( Color ) } , "negativeColorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| comparisonType | enum ( ComparisonType ) The comparison type of key value with baseline value. |
| textFormat | object ( TextFormat ) Text formatting options for baseline value. The link field is not supported. |
| position | object ( TextPosition ) Specifies the horizontal text positioning of baseline value. This field is optional. If not specified, default positioning is used. |
| description | string Description which is appended after the baseline value. This field is optional. |
| positiveColor (deprecated) | object ( Color ) This item is deprecated! Color to be used, in case baseline value represents a positive change for key value. This field is optional. Deprecated: Use positiveColorStyle . |
| positiveColorStyle | object ( ColorStyle ) Color to be used, in case baseline value represents a positive change for key value. This field is optional. If positiveColor is also set, this field takes precedence. |
| negativeColor (deprecated) | object ( Color ) This item is deprecated! Color to be used, in case baseline value represents a negative change for key value. This field is optional. Deprecated: Use negativeColorStyle . |
| negativeColorStyle | object ( ColorStyle ) Color to be used, in case baseline value represents a negative change for key value. This field is optional. If negativeColor is also set, this field takes precedence. |


## ComparisonType


The comparison type of key value with baseline value.


| Enums |
|---|
| COMPARISON_TYPE_UNDEFINED | Default value, do not use. |
| ABSOLUTE_DIFFERENCE | Use absolute difference between key and baseline value. |
| PERCENTAGE_DIFFERENCE | Use percentage difference between key and baseline value. |


## ChartNumberFormatSource


The number formatting source options for chart attributes.


| Enums |
|---|
| CHART_NUMBER_FORMAT_SOURCE_UNDEFINED | Default value, do not use. |
| FROM_DATA | Inherit number formatting from data. |
| CUSTOM | Apply custom formatting as specified by ChartCustomNumberFormatOptions . |


## ChartCustomNumberFormatOptions


Custom number formatting options for chart attributes.


| JSON representation |
|---|
| { "prefix" : string , "suffix" : string } |


| Fields |
|---|
| prefix | string Custom prefix to be prepended to the chart attribute. This field is optional. |
| suffix | string Custom suffix to be appended to the chart attribute. This field is optional. |


## ChartHiddenDimensionStrategy


Determines how charts should handle source rows that are hidden. Hidden rows include both manually hidden and hidden by a filter.


| Enums |
|---|
| CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED | Default value, do not use. |
| SKIP_HIDDEN_ROWS_AND_COLUMNS | Charts will skip hidden rows and columns. |
| SKIP_HIDDEN_ROWS | Charts will skip hidden rows only. |
| SKIP_HIDDEN_COLUMNS | Charts will skip hidden columns only. |
| SHOW_ALL | Charts will not skip any hidden rows or columns. |


## EmbeddedObjectBorder


A border along an embedded object.


| JSON representation |
|---|
| { "color" : { object ( Color ) } , "colorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| color (deprecated) | object ( Color ) This item is deprecated! The color of the border. Deprecated: Use colorStyle . |
| colorStyle | object ( ColorStyle ) The color of the border. If color is also set, this field takes precedence. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]