# Other

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other*

---

# Other


## Color


Represents a color in the RGBA color space. This representation is designed for simplicity of conversion to and from color representations in various languages over compactness. For example, the fields of this representation can be trivially provided to the constructor of
   `java.awt.Color`
   in Java; it can also be trivially provided to UIColor's
   `+colorWithRed:green:blue:alpha`
   method in iOS; and, with just a little work, it can be easily formatted into a CSS
   `rgba()`
   string in JavaScript.


This reference page doesn't have information about the absolute color space that should be used to interpret the RGB value—for example, sRGB, Adobe RGB, DCI-P3, and BT.2020. By default, applications should assume the sRGB color space.


When color equality needs to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green, blue, and alpha values each differ by at most
   `1e-5`.


Example (Java):


```
 import com.google.type.Color;

 // ...
 public static java.awt.Color fromProto(Color protocolor) {
   float alpha = protocolor.hasAlpha()
       ? protocolor.getAlpha().getValue()
       : 1.0;

   return new java.awt.Color(
       protocolor.getRed(),
       protocolor.getGreen(),
       protocolor.getBlue(),
       alpha);
 }

 public static Color toProto(java.awt.Color color) {
   float red = (float) color.getRed();
   float green = (float) color.getGreen();
   float blue = (float) color.getBlue();
   float denominator = 255.0;
   Color.Builder resultBuilder =
       Color
           .newBuilder()
           .setRed(red / denominator)
           .setGreen(green / denominator)
           .setBlue(blue / denominator);
   int alpha = color.getAlpha();
   if (alpha != 255) {
     result.setAlpha(
         FloatValue
             .newBuilder()
             .setValue(((float) alpha) / denominator)
             .build());
   }
   return resultBuilder.build();
 }
 // ...

```


Example (iOS / Obj-C):


```
 // ...
 static UIColor* fromProto(Color* protocolor) {
    float red = [protocolor red];
    float green = [protocolor green];
    float blue = [protocolor blue];
    FloatValue* alpha_wrapper = [protocolor alpha];
    float alpha = 1.0;
    if (alpha_wrapper != nil) {
      alpha = [alpha_wrapper value];
    }
    return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
 }

 static Color* toProto(UIColor* color) {
     CGFloat red, green, blue, alpha;
     if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
       return nil;
     }
     Color* result = [[Color alloc] init];
     [result setRed:red];
     [result setGreen:green];
     [result setBlue:blue];
     if (alpha <= 0.9999) {
       [result setAlpha:floatWrapperWithValue(alpha)];
     }
     [result autorelease];
     return result;
}
// ...

```


Example (JavaScript):


```
// ...

var protoToCssColor = function(rgbColor) {
   var redFrac = rgbColor.red || 0.0;
   var greenFrac = rgbColor.green || 0.0;
   var blueFrac = rgbColor.blue || 0.0;
   var red = Math.floor(redFrac * 255);
   var green = Math.floor(greenFrac * 255);
   var blue = Math.floor(blueFrac * 255);

   if (!('alpha' in rgbColor)) {
      return rgbToCssColor(red, green, blue);
   }

   var alphaFrac = rgbColor.alpha.value || 0.0;
   var rgbParams = [red, green, blue].join(',');
   return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
};

var rgbToCssColor = function(red, green, blue) {
  var rgbNumber = new Number((red << 16) | (green << 8) | blue);
  var hexString = rgbNumber.toString(16);
  var missingZeros = 6 - hexString.length;
  var resultBuilder = ['#'];
  for (var i = 0; i < missingZeros; i++) {
     resultBuilder.push('0');
  }
  resultBuilder.push(hexString);
  return resultBuilder.join('');
};

// ...

```


| JSON representation |
|---|
| { "red" : number , "green" : number , "blue" : number , "alpha" : number } |


| Fields |
|---|
| red | number The amount of red in the color as a value in the interval [0, 1]. |
| green | number The amount of green in the color as a value in the interval [0, 1]. |
| blue | number The amount of blue in the color as a value in the interval [0, 1]. |
| alpha | number The fraction of this color that should be applied to the pixel. That is, the final pixel color is defined by the equation: pixel color = alpha * (this color) + (1.0 - alpha) * (background color) This means that a value of 1.0 corresponds to a solid color, whereas a value of 0.0 corresponds to a completely transparent color. This uses a wrapper message rather than a simple float scalar so that it is possible to distinguish between a default value and the value being unset. If omitted, this color object is rendered as a solid color (as if the alpha value had been explicitly given a value of 1.0). |


## ColorStyle


A color value.


| JSON representation |
|---|
| { "rgbColor" : { object ( Color ) } , "themeColor" : enum ( ThemeColorType ) } |


| Fields |
|---|
| Union field kind . The kind of color value. kind can be only one of the following: |
| rgbColor | object ( Color ) RGB color. The alpha value in the Color object isn't generally supported. |
| themeColor | enum ( ThemeColorType ) Theme color. |


## ThemeColorType


Theme color types.


`SpreadsheetProperties`
   contain a
   `SpreadsheetTheme`
   that defines a mapping of these theme color types to concrete colors.


| Enums |
|---|
| THEME_COLOR_TYPE_UNSPECIFIED | Unspecified theme color |
| TEXT | Represents the primary text color |
| BACKGROUND | Represents the primary background color |
| ACCENT1 | Represents the first accent color |
| ACCENT2 | Represents the second accent color |
| ACCENT3 | Represents the third accent color |
| ACCENT4 | Represents the fourth accent color |
| ACCENT5 | Represents the fifth accent color |
| ACCENT6 | Represents the sixth accent color |
| LINK | Represents the color to use for hyperlinks |


## HorizontalAlign


The horizontal alignment of text in a cell.


| Enums |
|---|
| HORIZONTAL_ALIGN_UNSPECIFIED | The horizontal alignment is not specified. Do not use this. |
| LEFT | The text is explicitly aligned to the left of the cell. |
| CENTER | The text is explicitly aligned to the center of the cell. |
| RIGHT | The text is explicitly aligned to the right of the cell. |


## TextFormat


The format of a run of text in a cell. Absent values indicate that the field isn't specified.


| JSON representation |
|---|
| { "foregroundColor" : { object ( Color ) } , "foregroundColorStyle" : { object ( ColorStyle ) } , "fontFamily" : string , "fontSize" : integer , "bold" : boolean , "italic" : boolean , "strikethrough" : boolean , "underline" : boolean , "link" : { object ( Link ) } } |


| Fields |
|---|
| foregroundColor (deprecated) | object ( Color ) This item is deprecated! The foreground color of the text. Deprecated: Use foregroundColorStyle . |
| foregroundColorStyle | object ( ColorStyle ) The foreground color of the text. If foregroundColor is also set, this field takes precedence. |
| fontFamily | string The font family. |
| fontSize | integer The size of the font. |
| bold | boolean True if the text is bold. |
| italic | boolean True if the text is italicized. |
| strikethrough | boolean True if the text has a strikethrough. |
| underline | boolean True if the text is underlined. |
| link | object ( Link ) The link destination of the text, if any. Setting the link field in a TextFormatRun will clear the cell's existing links or a cell-level link set in the same request. When a link is set, the text foreground color will be set to the default link color and the text will be underlined. If these fields are modified in the same request, those values will be used instead of the link defaults. |


## Link


An external or local reference.


| JSON representation |
|---|
| { "uri" : string } |


| Fields |
|---|
| Union field destination . The link destination. destination can be only one of the following: |
| uri | string The link identifier. |


## DataSourceColumn


A column in a data source.


| JSON representation |
|---|
| { "reference" : { object ( DataSourceColumnReference ) } , "formula" : string } |


| Fields |
|---|
| reference | object ( DataSourceColumnReference ) The column reference. |
| formula | string The formula of the calculated column. |


## DataSourceColumnReference


An unique identifier that references a data source column.


| JSON representation |
|---|
| { "name" : string } |


| Fields |
|---|
| name | string The display name of the column. It should be unique within a data source. |


## DataExecutionStatus


The data execution status.


A data execution is created to sync a data source object with the latest data from a
   `DataSource`. It is usually scheduled to run at background, you can check its
   `state`
   to tell if an execution completes


There are several scenarios where a data execution is triggered to run:


- `Adding a data source`
    creates an associated data  source sheet as well as a data execution to sync the data from the data  source to the sheet.
- `Updating a data source`
    creates a data execution  to refresh the associated data source sheet similarly.
- You can send
    `refresh request`
    to explicitly  refresh one or multiple data source objects.


| JSON representation |
|---|
| { "state" : enum ( DataExecutionState ) , "errorCode" : enum ( DataExecutionErrorCode ) , "errorMessage" : string , "lastRefreshTime" : string } |


| Fields |
|---|
| state | enum ( DataExecutionState ) The state of the data execution. |
| errorCode | enum ( DataExecutionErrorCode ) The error code. |
| errorMessage | string The error message, which may be empty. |
| lastRefreshTime | string ( Timestamp format) Gets the time the data last successfully refreshed. |


## DataExecutionState


An enumeration of data execution states.


| Enums |
|---|
| DATA_EXECUTION_STATE_UNSPECIFIED | Default value, do not use. |
| NOT_STARTED | The data execution has not started. |
| RUNNING | The data execution has started and is running. |
| CANCELLING | The data execution is currently being cancelled. |
| SUCCEEDED | The data execution has completed successfully. |
| FAILED | The data execution has completed with errors. |


## DataExecutionErrorCode


An enumeration of data execution error code.


| Enums |
|---|
| DATA_EXECUTION_ERROR_CODE_UNSPECIFIED | Default value, do not use. |
| TIMED_OUT | The data execution timed out. |
| TOO_MANY_ROWS | The data execution returns more rows than the limit. |
| TOO_MANY_COLUMNS | The data execution returns more columns than the limit. |
| TOO_MANY_CELLS | The data execution returns more cells than the limit. |
| ENGINE | Error is received from the backend data execution engine (e.g. BigQuery). Check errorMessage for details. |
| PARAMETER_INVALID | One or some of the provided data source parameters are invalid. |
| UNSUPPORTED_DATA_TYPE | The data execution returns an unsupported data type. |
| DUPLICATE_COLUMN_NAMES | The data execution returns duplicate column names or aliases. |
| INTERRUPTED | The data execution is interrupted. Please refresh later. |
| CONCURRENT_QUERY | The data execution is currently in progress, can not be refreshed until it completes. |
| OTHER | Other errors. |
| TOO_MANY_CHARS_PER_CELL | The data execution returns values that exceed the maximum characters allowed in a single cell. |
| DATA_NOT_FOUND | The database referenced by the data source is not found. */ |
| PERMISSION_DENIED | The user does not have access to the database referenced by the data source. |
| MISSING_COLUMN_ALIAS | The data execution returns columns with missing aliases. |
| OBJECT_NOT_FOUND | The data source object does not exist. |
| OBJECT_IN_ERROR_STATE | The data source object is currently in error state. To force refresh, set force in RefreshDataSourceRequest . |
| OBJECT_SPEC_INVALID | The data source object specification is invalid. |
| DATA_EXECUTION_CANCELLED | The data execution has been cancelled. |


## ExtendedValue


The kinds of value that a cell in a spreadsheet can have.


| JSON representation |
|---|
| { "numberValue" : number , "stringValue" : string , "boolValue" : boolean , "formulaValue" : string , "errorValue" : { object ( ErrorValue ) } } |


| Fields |
|---|
| Union field value . The type of value in a cell. If no field is set, the cell has no data. value can be only one of the following: |
| numberValue | number Represents a double value. Note: Dates, Times and DateTimes are represented as doubles in SERIAL_NUMBER format. |
| stringValue | string Represents a string value. Leading single quotes are not included. For example, if the user typed '123 into the UI, this would be represented as a stringValue of "123" . |
| boolValue | boolean Represents a boolean value. |
| formulaValue | string Represents a formula. |
| errorValue | object ( ErrorValue ) Represents an error. This field is read-only. |


## ErrorValue


An error in a cell.


| JSON representation |
|---|
| { "type" : enum ( ErrorType ) , "message" : string } |


| Fields |
|---|
| type | enum ( ErrorType ) The type of error. |
| message | string A message with more information about the error (in the spreadsheet's locale). |


## ErrorType


The type of error.


| Enums |
|---|
| ERROR_TYPE_UNSPECIFIED | The default error type, do not use this. |
| ERROR | Corresponds to the #ERROR! error. |
| NULL_VALUE | Corresponds to the #NULL! error. |
| DIVIDE_BY_ZERO | Corresponds to the #DIV/0 error. |
| VALUE | Corresponds to the #VALUE! error. |
| REF | Corresponds to the #REF! error. |
| NAME | Corresponds to the #NAME? error. |
| NUM | Corresponds to the #NUM! error. |
| N_A | Corresponds to the #N/A error. |
| LOADING | Corresponds to the Loading... state. |


## BooleanCondition


A condition that can evaluate to true or false. BooleanConditions are used by conditional formatting, data validation, and the criteria in filters.


| JSON representation |
|---|
| { "type" : enum ( ConditionType ) , "values" : [ { object ( ConditionValue ) } ] } |


| Fields |
|---|
| type | enum ( ConditionType ) The type of condition. |
| values[] | object ( ConditionValue ) The values of the condition. The number of supported values depends on the condition type . Some support zero values, others one or two values, and ConditionType.ONE_OF_LIST supports an arbitrary number of values. |


## ConditionType


The type of condition.


| Enums |
|---|
| CONDITION_TYPE_UNSPECIFIED | The default value, do not use. |
| NUMBER_GREATER | The cell's value must be greater than the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue . |
| NUMBER_GREATER_THAN_EQ | The cell's value must be greater than or equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue . |
| NUMBER_LESS | The cell's value must be less than the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue . |
| NUMBER_LESS_THAN_EQ | The cell's value must be less than or equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue . |
| NUMBER_EQ | The cell's value must be equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects. |
| NUMBER_NOT_EQ | The cell's value must be not equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects. |
| NUMBER_BETWEEN | The cell's value must be between the two condition values. Supported by data validation, conditional formatting and filters. Requires exactly two ConditionValues . |
| NUMBER_NOT_BETWEEN | The cell's value must not be between the two condition values. Supported by data validation, conditional formatting and filters. Requires exactly two ConditionValues . |
| TEXT_CONTAINS | The cell's value must contain the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue . |
| TEXT_NOT_CONTAINS | The cell's value must not contain the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue . |
| TEXT_STARTS_WITH | The cell's value must start with the condition's value. Supported by conditional formatting and filters. Requires a single ConditionValue . |
| TEXT_ENDS_WITH | The cell's value must end with the condition's value. Supported by conditional formatting and filters. Requires a single ConditionValue . |
| TEXT_EQ | The cell's value must be exactly the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects. |
| TEXT_IS_EMAIL | The cell's value must be a valid email address. Supported by data validation. Requires no ConditionValues . |
| TEXT_IS_URL | The cell's value must be a valid URL. Supported by data validation. Requires no ConditionValues . |
| DATE_EQ | The cell's value must be the same date as the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects. |
| DATE_BEFORE | The cell's value must be before the date of the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue that may be a relative date . |
| DATE_AFTER | The cell's value must be after the date of the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue that may be a relative date . |
| DATE_ON_OR_BEFORE | The cell's value must be on or before the date of the condition's value. Supported by data validation. Requires a single ConditionValue that may be a relative date . |
| DATE_ON_OR_AFTER | The cell's value must be on or after the date of the condition's value. Supported by data validation. Requires a single ConditionValue that may be a relative date . |
| DATE_BETWEEN | The cell's value must be between the dates of the two condition values. Supported by data validation. Requires exactly two ConditionValues . |
| DATE_NOT_BETWEEN | The cell's value must be outside the dates of the two condition values. Supported by data validation. Requires exactly two ConditionValues . |
| DATE_IS_VALID | The cell's value must be a date. Supported by data validation. Requires no ConditionValues . |
| ONE_OF_RANGE | The cell's value must be listed in the grid in condition value's range. Supported by data validation. Requires a single ConditionValue , and the value must be a valid range in A1 notation. |
| ONE_OF_LIST | The cell's value must be in the list of condition values. Supported by data validation. Supports any number of condition values , one per item in the list. Formulas are not supported in the values. |
| BLANK | The cell's value must be empty. Supported by conditional formatting and filters. Requires no ConditionValues . |
| NOT_BLANK | The cell's value must not be empty. Supported by conditional formatting and filters. Requires no ConditionValues . |
| CUSTOM_FORMULA | The condition's formula must evaluate to true. Supported by data validation, conditional formatting and filters. Not supported by data source sheet filters. Requires a single ConditionValue . |
| BOOLEAN | The cell's value must be TRUE/FALSE or in the list of condition values. Supported by data validation. Renders as a cell checkbox. Supports zero, one or two ConditionValues . No values indicates the cell must be TRUE or FALSE, where TRUE renders as checked and FALSE renders as unchecked. One value indicates the cell will render as checked when it contains that value and unchecked when it is blank. Two values indicate that the cell will render as checked when it contains the first value and unchecked when it contains the second value. For example, ["Yes","No"] indicates that the cell will render a checked box when it has the value "Yes" and an unchecked box when it has the value "No". |
| TEXT_NOT_EQ | The cell's value must be exactly not the condition's value. Supported by filters on data source objects. Requires at least one ConditionValue . |
| DATE_NOT_EQ | The cell's value must be exactly not the condition's value. Supported by filters on data source objects. Requires at least one ConditionValue . |
| FILTER_EXPRESSION | The cell's value must follow the pattern specified. Requires a single ConditionValue . |


## ConditionValue


The value of the condition.


| JSON representation |
|---|
| { "relativeDate" : enum ( RelativeDate ) , "userEnteredValue" : string } |


| Fields |
|---|
| Union field value . The value of the condition, exactly one must be set. value can be only one of the following: |
| relativeDate | enum ( RelativeDate ) A relative date (based on the current date). Valid only if the type is DATE_BEFORE , DATE_AFTER , DATE_ON_OR_BEFORE or DATE_ON_OR_AFTER . Relative dates are not supported in data validation. They are supported only in conditional formatting and conditional filters. |
| userEnteredValue | string A value the condition is based on. The value is parsed as if the user typed into a cell. Formulas are supported (and must begin with an = or a '+'). |


## RelativeDate


Controls how a date condition is evaluated.


| Enums |
|---|
| RELATIVE_DATE_UNSPECIFIED | Default value, do not use. |
| PAST_YEAR | The value is one year before today. |
| PAST_MONTH | The value is one month before today. |
| PAST_WEEK | The value is one week before today. |
| YESTERDAY | The value is yesterday. |
| TODAY | The value is today. |
| TOMORROW | The value is tomorrow. |


## GridRange


A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the start index is inclusive and the end index is exclusive -- [startIndex, endIndex). Missing indexes indicate the range is unbounded on that side.


For example, if
   `"Sheet1"`
   is sheet ID 123456, then:


`Sheet1!A1:A1 == sheetId: 123456,
                            startRowIndex: 0, endRowIndex: 1,
                            startColumnIndex: 0, endColumnIndex: 1`


`Sheet1!A3:B4 == sheetId: 123456,
                            startRowIndex: 2, endRowIndex: 4,
                            startColumnIndex: 0, endColumnIndex: 2`


`Sheet1!A:B == sheetId: 123456,
                          startColumnIndex: 0, endColumnIndex: 2`


`Sheet1!A5:B == sheetId: 123456,
                           startRowIndex: 4,
                           startColumnIndex: 0, endColumnIndex: 2`


`Sheet1 == sheetId: 123456`


The start index must always be less than or equal to the end index. If the start index equals the end index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
   `#REF!`.


| JSON representation |
|---|
| { "sheetId" : integer , "startRowIndex" : integer , "endRowIndex" : integer , "startColumnIndex" : integer , "endColumnIndex" : integer } |


| Fields |
|---|
| sheetId | integer The sheet this range is on. |
| startRowIndex | integer The start row (inclusive) of the range, or not set if unbounded. |
| endRowIndex | integer The end row (exclusive) of the range, or not set if unbounded. |
| startColumnIndex | integer The start column (inclusive) of the range, or not set if unbounded. |
| endColumnIndex | integer The end column (exclusive) of the range, or not set if unbounded. |


## SortOrder


A sort order.


| Enums |
|---|
| SORT_ORDER_UNSPECIFIED | Default value, do not use this. |
| ASCENDING | Sort ascending. |
| DESCENDING | Sort descending. |


## FilterSpec


The filter criteria associated with a specific column.


| JSON representation |
|---|
| { "filterCriteria" : { object ( FilterCriteria ) } , "columnIndex" : integer , "dataSourceColumnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| filterCriteria | object ( FilterCriteria ) The criteria for the column. |
| Union field reference . Reference to the filtered column. reference can be only one of the following: |
| columnIndex | integer The zero-based column index. |
| dataSourceColumnReference | object ( DataSourceColumnReference ) Reference to a data source column. |


## FilterCriteria


Criteria for showing or hiding rows in a filter or filter view.


| JSON representation |
|---|
| { "hiddenValues" : [ string ] , "condition" : { object ( BooleanCondition ) } , "visibleBackgroundColor" : { object ( Color ) } , "visibleBackgroundColorStyle" : { object ( ColorStyle ) } , "visibleForegroundColor" : { object ( Color ) } , "visibleForegroundColorStyle" : { object ( ColorStyle ) } } |


| Fields |
|---|
| hiddenValues[] | string Values that should be hidden. |
| condition | object ( BooleanCondition ) A condition that must be true for values to be shown. (This does not override hiddenValues -- if a value is listed there,  it will still be hidden.) |
| visibleBackgroundColor (deprecated) | object ( Color ) This item is deprecated! The background fill color to filter by; only cells with this fill color are shown. Mutually exclusive with visibleForegroundColor . Deprecated: Use visibleBackgroundColorStyle . |
| visibleBackgroundColorStyle | object ( ColorStyle ) The background fill color to filter by; only cells with this fill color are shown. This field is mutually exclusive with visibleForegroundColor , and must be set to an RGB-type color. If visibleBackgroundColor is also set, this field takes precedence. |
| visibleForegroundColor (deprecated) | object ( Color ) This item is deprecated! The foreground color to filter by; only cells with this foreground color are shown. Mutually exclusive with visibleBackgroundColor . Deprecated: Use visibleForegroundColorStyle . |
| visibleForegroundColorStyle | object ( ColorStyle ) The foreground color to filter by; only cells with this foreground color are shown. This field is mutually exclusive with visibleBackgroundColor , and must be set to an RGB-type color. If visibleForegroundColor is also set, this field takes precedence. |


## SortSpec


A sort order associated with a specific column or row.


| JSON representation |
|---|
| { "sortOrder" : enum ( SortOrder ) , "foregroundColor" : { object ( Color ) } , "foregroundColorStyle" : { object ( ColorStyle ) } , "backgroundColor" : { object ( Color ) } , "backgroundColorStyle" : { object ( ColorStyle ) } , "dimensionIndex" : integer , "dataSourceColumnReference" : { object ( DataSourceColumnReference ) } } |


| Fields |
|---|
| sortOrder | enum ( SortOrder ) The order data should be sorted. |
| foregroundColor (deprecated) | object ( Color ) This item is deprecated! The foreground color to sort by; cells with this foreground color are sorted to the top. Mutually exclusive with backgroundColor . Deprecated: Use foregroundColorStyle . |
| foregroundColorStyle | object ( ColorStyle ) The foreground color to sort by; cells with this foreground color are sorted to the top. Mutually exclusive with backgroundColor , and must be an RGB-type color. If foregroundColor is also set, this field takes precedence. |
| backgroundColor (deprecated) | object ( Color ) This item is deprecated! The background fill color to sort by; cells with this fill color are sorted to the top. Mutually exclusive with foregroundColor . Deprecated: Use backgroundColorStyle . |
| backgroundColorStyle | object ( ColorStyle ) The background fill color to sort by; cells with this fill color are sorted to the top. Mutually exclusive with foregroundColor , and must be an RGB-type color. If backgroundColor is also set, this field takes precedence. |
| Union field reference . Reference to the sorted dimension. reference can be only one of the following: |
| dimensionIndex | integer The dimension the sort should be applied to. |
| dataSourceColumnReference | object ( DataSourceColumnReference ) Reference to a data source column. |


## EmbeddedObjectPosition


The position of an embedded object such as a chart.


| JSON representation |
|---|
| { "sheetId" : integer , "overlayPosition" : { object ( OverlayPosition ) } , "newSheet" : boolean } |


| Fields |
|---|
| Union field location . The location of the object. Exactly one value must be set. location can be only one of the following: |
| sheetId | integer The sheet this is on. Set only if the embedded object is on its own sheet. Must be non-negative. |
| overlayPosition | object ( OverlayPosition ) The position at which the object is overlaid on top of a grid. |
| newSheet | boolean If true, the embedded object is put on a new sheet whose ID is chosen for you. Used only when writing. |


## OverlayPosition


The location an object is overlaid on top of a grid.


| JSON representation |
|---|
| { "anchorCell" : { object ( GridCoordinate ) } , "offsetXPixels" : integer , "offsetYPixels" : integer , "widthPixels" : integer , "heightPixels" : integer } |


| Fields |
|---|
| anchorCell | object ( GridCoordinate ) The cell the object is anchored to. |
| offsetXPixels | integer The horizontal offset, in pixels, that the object is offset from the anchor cell. |
| offsetYPixels | integer The vertical offset, in pixels, that the object is offset from the anchor cell. |
| widthPixels | integer The width of the object, in pixels. Defaults to 600. |
| heightPixels | integer The height of the object, in pixels. Defaults to 371. |


## GridCoordinate


A coordinate in a sheet. All indexes are zero-based.


| JSON representation |
|---|
| { "sheetId" : integer , "rowIndex" : integer , "columnIndex" : integer } |


| Fields |
|---|
| sheetId | integer The sheet this coordinate is on. |
| rowIndex | integer The row index of the coordinate. |
| columnIndex | integer The column index of the coordinate. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]