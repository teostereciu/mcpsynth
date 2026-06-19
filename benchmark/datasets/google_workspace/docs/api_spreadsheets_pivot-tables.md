# Pivot Tables

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables*

---

# Pivot Tables


## PivotTable


A pivot table.


| JSON representation |
|---|
| { "rows" : [ { object ( PivotGroup ) } ] , "columns" : [ { object ( PivotGroup ) } ] , "criteria" : { integer : { object ( PivotFilterCriteria ) } , ... } , "filterSpecs" : [ { object ( PivotFilterSpec ) } ] , "values" : [ { object ( PivotValue ) } ] , "valueLayout" : enum ( PivotValueLayout ) , "dataExecutionStatus" : { object ( DataExecutionStatus ) } , "source" : { object ( GridRange ) } , "dataSourceId" : string } |


| Fields |
|---|
| rows[] | object ( PivotGroup ) Each row grouping in the pivot table. |
| columns[] | object ( PivotGroup ) Each column grouping in the pivot table. |
| criteria (deprecated) | map (key: integer, value: object ( PivotFilterCriteria )) This item is deprecated! An optional mapping of filters per source column offset. The filters are applied before aggregating data into the pivot table. The map's key is the column offset of the source range that you want to filter, and the value is the criteria for that column. For example, if the source was C10:E15 , a key of 0 will have the filter for column C , whereas the key 1 is for column D . This field is deprecated in favor of filterSpecs . |
| filterSpecs[] | object ( PivotFilterSpec ) The filters applied to the source columns before aggregating data for the pivot table. Both criteria and filterSpecs are populated in responses. If both fields are specified in an update request, this field takes precedence. |
| values[] | object ( PivotValue ) A list of values to include in the pivot table. |
| valueLayout | enum ( PivotValueLayout ) Whether values should be listed horizontally (as columns) or vertically (as rows). |
| dataExecutionStatus | object ( DataExecutionStatus ) Output only. The data execution status for data source pivot tables. |
| Union field source_data . The source of the pivot table data. source_data can be only one of the following: |
| source | object ( GridRange ) The range the pivot table is reading data from. |
| dataSourceId | string The ID of the data source the pivot table is reading data from. |


## PivotGroup


A single grouping (either row or column) in a pivot table.


| JSON representation |
|---|
| { "showTotals" : boolean , "valueMetadata" : [ { object ( PivotGroupValueMetadata ) } ] , "sortOrder" : enum ( SortOrder ) , "valueBucket" : { object ( PivotGroupSortValueBucket ) } , "repeatHeadings" : boolean , "label" : string , "groupRule" : { object ( PivotGroupRule ) } , "groupLimit" : { object ( PivotGroupLimit ) } , "sourceColumnOffset" : integer , "dataSourceColumnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| showTotals | boolean True if the pivot table should include the totals for this grouping. |
| valueMetadata[] | object ( PivotGroupValueMetadata ) Metadata about values in the grouping. |
| sortOrder | enum ( SortOrder ) The order the values in this group should be sorted. |
| valueBucket | object ( PivotGroupSortValueBucket ) The bucket of the opposite pivot group to sort by. If not specified, sorting is alphabetical by this group's values. |
| repeatHeadings | boolean True if the headings in this pivot group should be repeated. This is only valid for row groupings and is ignored by columns. By default, we minimize repetition of headings by not showing higher level headings where they are the same. For example, even though the third row below corresponds to "Q1 Mar", "Q1" is not shown because it is redundant with previous rows. Setting repeatHeadings to true would cause "Q1" to be repeated for "Feb" and "Mar". +--------------+
\| Q1     \| Jan \|
\|        \| Feb \|
\|        \| Mar \|
+--------+-----+
\| Q1 Total     \|
+--------------+ |
| label | string The labels to use for the row/column groups which can be customized. For example, in the following pivot table, the row label is Region (which could be renamed to State ) and the column label is Product (which could be renamed Item ). Pivot tables created before December 2017 do not have header labels. If you'd like to add header labels to an existing pivot table, please delete the existing pivot table and then create a new pivot table with same parameters. +--------------+---------+-------+
\| SUM of Units \| Product \|       \|
\| Region       \| Pen     \| Paper \|
+--------------+---------+-------+
\| New York     \|     345 \|    98 \|
\| Oregon       \|     234 \|   123 \|
\| Tennessee    \|     531 \|   415 \|
+--------------+---------+-------+
\| Grand Total  \|    1110 \|   636 \|
+--------------+---------+-------+ |
| groupRule | object ( PivotGroupRule ) The group rule to apply to this row/column group. |
| groupLimit | object ( PivotGroupLimit ) The count limit on rows or columns to apply to this pivot group. |
| Union field source . The data source of the pivot group. source can be only one of the following: |
| sourceColumnOffset | integer The column offset of the source range that this grouping is based on. For example, if the source was C10:E15 , a sourceColumnOffset of 0 means this group refers to column C , whereas the offset 1 would refer to column D . |
| dataSourceColumnReference | object ( DataSourceColumnReference ) The reference to the data source column this grouping is based on. |


## PivotGroupValueMetadata


Metadata about a value in a pivot grouping.


| JSON representation |
|---|
| { "value" : { object ( ExtendedValue ) } , "collapsed" : boolean } |


| Fields |
|---|
| value | object ( ExtendedValue ) The calculated value the metadata corresponds to. (Note that formulaValue is not valid,  because the values will be calculated.) |
| collapsed | boolean True if the data corresponding to the value is collapsed. |


## PivotGroupSortValueBucket


Information about which values in a pivot group should be used for sorting.


| JSON representation |
|---|
| { "valuesIndex" : integer , "buckets" : [ { object ( ExtendedValue ) } ] } |


| Fields |
|---|
| valuesIndex | integer The offset in the PivotTable.values list which the values in this grouping should be sorted by. |
| buckets[] | object ( ExtendedValue ) Determines the bucket from which values are chosen to sort. For example, in a pivot table with one row group & two column groups, the row group can list up to two values. The first value corresponds to a value within the first column group, and the second value corresponds to a value in the second column group. If no values are listed, this would indicate that the row should be sorted according to the "Grand Total" over the column groups. If a single value is listed, this would correspond to using the "Total" of that bucket. |


## PivotGroupRule


An optional setting on a
   `PivotGroup`
   that defines buckets for the values in the source data column rather than breaking out each individual value. Only one
   `PivotGroup`
   with a group rule may be added for each column in the source data, though on any given column you may add both a
   `PivotGroup`
   that has a rule and a
   `PivotGroup`
   that does not.


| JSON representation |
|---|
| { "manualRule" : { object ( ManualRule ) } , "histogramRule" : { object ( HistogramRule ) } , "dateTimeRule" : { object ( DateTimeRule ) } } |


| Fields |
|---|
| Union field rule . The rule to apply to the PivotGroup . rule can be only one of the following: |
| manualRule | object ( ManualRule ) A ManualRule . |
| histogramRule | object ( HistogramRule ) A HistogramRule . |
| dateTimeRule | object ( DateTimeRule ) A DateTimeRule . |


## ManualRule


Allows you to manually organize the values in a source data column into buckets with names of your choosing. For example, a pivot table that aggregates population by state:


```
+-------+-------------------+
| State | SUM of Population |
+-------+-------------------+
| AK    |               0.7 |
| AL    |               4.8 |
| AR    |               2.9 |
...
+-------+-------------------+

```


could be turned into a pivot table that aggregates population by time zone by providing a list of groups (for example, groupName = 'Central', items = ['AL', 'AR', 'IA', ...]) to a manual group rule. Note that a similar effect could be achieved by adding a time zone column to the source data and adjusting the pivot table.


```
+-----------+-------------------+
| Time Zone | SUM of Population |
+-----------+-------------------+
| Central   |             106.3 |
| Eastern   |             151.9 |
| Mountain  |              17.4 |
...
+-----------+-------------------+

```


| JSON representation |
|---|
| { "groups" : [ { object ( ManualRuleGroup ) } ] } |


| Fields |
|---|
| groups[] | object ( ManualRuleGroup ) The list of group names and the corresponding items from the source data that map to each group name. |


## ManualRuleGroup


A group name and a list of items from the source data that should be placed in the group with this name.


| JSON representation |
|---|
| { "groupName" : { object ( ExtendedValue ) } , "items" : [ { object ( ExtendedValue ) } ] } |


| Fields |
|---|
| groupName | object ( ExtendedValue ) The group name, which must be a string. Each group in a given ManualRule must have a unique group name. |
| items[] | object ( ExtendedValue ) The items in the source data that should be placed into this group. Each item may be a string, number, or boolean. Items may appear in at most one group within a given ManualRule . Items that do not appear in any group will appear on their own. |


## HistogramRule


Allows you to organize the numeric values in a source data column into buckets of a constant size. All values from
   `HistogramRule.start`
   to
   `HistogramRule.end`
   are placed into groups of size
   `HistogramRule.interval`. In addition, all values below
   `HistogramRule.start`
   are placed in one group, and all values above
   `HistogramRule.end`
   are placed in another. Only
   `HistogramRule.interval`
   is required, though if
   `HistogramRule.start`
   and
   `HistogramRule.end`
   are both provided,
   `HistogramRule.start`
   must be less than
   `HistogramRule.end`. For example, a pivot table showing average purchase amount by age that has 50+ rows:


```
+-----+-------------------+
| Age | AVERAGE of Amount |
+-----+-------------------+
| 16  |            $27.13 |
| 17  |             $5.24 |
| 18  |            $20.15 |
...
+-----+-------------------+

```


could be turned into a pivot table that looks like the one below by applying a histogram group rule with a
   `HistogramRule.start`
   of 25, an
   `HistogramRule.interval`
   of 20, and an
   `HistogramRule.end`
   of 65.


```
+-------------+-------------------+
| Grouped Age | AVERAGE of Amount |
+-------------+-------------------+
| < 25        |            $19.34 |
| 25-45       |            $31.43 |
| 45-65       |            $35.87 |
| > 65        |            $27.55 |
+-------------+-------------------+
| Grand Total |            $29.12 |
+-------------+-------------------+

```


| JSON representation |
|---|
| { "interval" : number , "start" : number , "end" : number } |


| Fields |
|---|
| interval | number The size of the buckets that are created. Must be positive. |
| start | number The minimum value at which items are placed into buckets of constant size. Values below start are lumped into a single bucket. This field is optional. |
| end | number The maximum value at which items are placed into buckets of constant size. Values above end are lumped into a single bucket. This field is optional. |


## DateTimeRule


Allows you to organize the date-time values in a source data column into buckets based on selected parts of their date or time values. For example, consider a pivot table showing sales transactions by date:


```
+----------+--------------+
| Date     | SUM of Sales |
+----------+--------------+
| 1/1/2017 |      $621.14 |
| 2/3/2017 |      $708.84 |
| 5/8/2017 |      $326.84 |
...
+----------+--------------+

```


Applying a date-time group rule with a
   `DateTimeRuleType`
   of YEAR_MONTH results in the following pivot table.


```
+--------------+--------------+
| Grouped Date | SUM of Sales |
+--------------+--------------+
| 2017-Jan     |   $53,731.78 |
| 2017-Feb     |   $83,475.32 |
| 2017-Mar     |   $94,385.05 |
...
+--------------+--------------+

```


| JSON representation |
|---|
| { "type" : enum ( DateTimeRuleType ) } |


| Fields |
|---|
| type | enum ( DateTimeRuleType ) The type of date-time grouping to apply. |


## DateTimeRuleType


The available types of date-time grouping rules. This documentation assumes the spreadsheet locale is "en-US", though the actual rendering of the dates and times uses the locale of the spreadsheet for some rule types.


| Enums |
|---|
| DATE_TIME_RULE_TYPE_UNSPECIFIED | The default type, do not use. |
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


## PivotGroupLimit


The count limit on rows or columns in the pivot group.


| JSON representation |
|---|
| { "countLimit" : integer , "applyOrder" : integer } |


| Fields |
|---|
| countLimit | integer The count limit. |
| applyOrder | integer The order in which the group limit is applied to the pivot table. Pivot group limits are applied from lower to higher order number. Order numbers are normalized to consecutive integers from 0. For write request, to fully customize the applying orders, all pivot group limits should have this field set with an unique number. Otherwise, the order is determined by the index in the PivotTable.rows list and then the PivotTable.columns list. |


## PivotFilterCriteria


Criteria for showing/hiding rows in a pivot table.


| JSON representation |
|---|
| { "visibleValues" : [ string ] , "condition" : { object ( BooleanCondition ) } , "visibleByDefault" : boolean } |


| Fields |
|---|
| visibleValues[] | string Values that should be included. Values not listed here are excluded. |
| condition | object ( BooleanCondition ) A condition that must be true for values to be shown. ( visibleValues does not override this -- even if a value is listed there, it is still hidden if it does not meet the condition.) Condition values that refer to ranges in A1-notation are evaluated relative to the pivot table sheet. References are treated absolutely, so are not filled down the pivot table. For example, a condition value of =A1 on "Pivot Table 1" is treated as 'Pivot Table 1'!$A$1 . The source data of the pivot table can be referenced by column header name. For example, if the source data has columns named "Revenue" and "Cost" and a condition is applied to the "Revenue" column with type NUMBER_GREATER and value =Cost , then only columns where "Revenue" > "Cost" are included. |
| visibleByDefault | boolean Whether values are visible by default. If true, the visibleValues are ignored, all values that meet condition (if specified) are shown. If false, values that are both in visibleValues and meet condition are shown. |


## PivotFilterSpec


The pivot table filter criteria associated with a specific source column offset.


| JSON representation |
|---|
| { "filterCriteria" : { object ( PivotFilterCriteria ) } , "columnOffsetIndex" : integer , "dataSourceColumnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| filterCriteria | object ( PivotFilterCriteria ) The criteria for the column. |
| Union field source . The source column that this filter applies to. source can be only one of the following: |
| columnOffsetIndex | integer The zero-based column offset of the source range. |
| dataSourceColumnReference | object ( DataSourceColumnReference ) The reference to the data source column. |


## PivotValue


The definition of how a value in a pivot table should be calculated.


| JSON representation |
|---|
| { "summarizeFunction" : enum ( PivotValueSummarizeFunction ) , "name" : string , "calculatedDisplayType" : enum ( PivotValueCalculatedDisplayType ) , "sourceColumnOffset" : integer , "formula" : string , "dataSourceColumnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| summarizeFunction | enum ( PivotValueSummarizeFunction ) A function to summarize the value. If formula is set, the only supported values are SUM and CUSTOM . If sourceColumnOffset is set, then CUSTOM is not supported. |
| name | string A name to use for the value. |
| calculatedDisplayType | enum ( PivotValueCalculatedDisplayType ) If specified, indicates that pivot values should be displayed as the result of a calculation with another pivot value. For example, if calculatedDisplayType is specified as PERCENT_OF_GRAND_TOTAL, all the pivot values are displayed as the percentage of the grand total. In the Sheets editor, this is referred to as "Show As" in the value section of a pivot table. |
| Union field value . The data to use for the values in the pivot table. Exactly one value must be set. value can be only one of the following: |
| sourceColumnOffset | integer The column offset of the source range that this value reads from. For example, if the source was C10:E15 , a sourceColumnOffset of 0 means this value refers to column C , whereas the offset 1 would refer to column D . |
| formula | string A custom formula to calculate the value. The formula must start with an = character. |
| dataSourceColumnReference | object ( DataSourceColumnReference ) The reference to the data source column that this value reads from. |


## PivotValueSummarizeFunction


A function to summarize a pivot value.


| Enums |
|---|
| PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED | The default, do not use. |
| SUM | Corresponds to the SUM function. |
| COUNTA | Corresponds to the COUNTA function. |
| COUNT | Corresponds to the COUNT function. |
| COUNTUNIQUE | Corresponds to the COUNTUNIQUE function. |
| AVERAGE | Corresponds to the AVERAGE function. |
| MAX | Corresponds to the MAX function. |
| MIN | Corresponds to the MIN function. |
| MEDIAN | Corresponds to the MEDIAN function. |
| PRODUCT | Corresponds to the PRODUCT function. |
| STDEV | Corresponds to the STDEV function. |
| STDEVP | Corresponds to the STDEVP function. |
| VAR | Corresponds to the VAR function. |
| VARP | Corresponds to the VARP function. |
| CUSTOM | Indicates the formula should be used as-is. Only valid if PivotValue.formula was set. |
| NONE | Indicates that the value is already summarized, and the summarization function is not explicitly specified. Used for Looker data source pivot tables where the value is already summarized. |


## PivotValueCalculatedDisplayType


The possible ways that pivot values may be calculated for display.


| Enums |
|---|
| PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED | Default value, do not use. |
| PERCENT_OF_ROW_TOTAL | Shows the pivot values as percentage of the row total values. |
| PERCENT_OF_COLUMN_TOTAL | Shows the pivot values as percentage of the column total values. |
| PERCENT_OF_GRAND_TOTAL | Shows the pivot values as percentage of the grand total values. |


## PivotValueLayout


The layout of pivot values.


| Enums |
|---|
| HORIZONTAL | Values are laid out horizontally (as columns). |
| VERTICAL | Values are laid out vertically (as rows). |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]