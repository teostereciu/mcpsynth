# Method: spreadsheets.values.batchGet

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/batchGet*

---

# Method: spreadsheets.values.batchGet


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- Try it!


Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges.


### HTTP request


`GET https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values:batchGet`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to retrieve data from. |


### Query parameters


| Parameters |
|---|
| ranges[] | string The A1 notation or R1C1 notation of the range to retrieve values from. |
| majorDimension | enum ( Dimension ) The major dimension that results should use. For example, if the spreadsheet data is: A1=1,B1=2,A2=3,B2=4 , then requesting ranges=["A1:B2"],majorDimension=ROWS returns [[1,2],[3,4]] , whereas requesting ranges=["A1:B2"],majorDimension=COLUMNS returns [[1,3],[2,4]] . |
| valueRenderOption | enum ( ValueRenderOption ) How values should be represented in the output. The default render option is ValueRenderOption.FORMATTED_VALUE . |
| dateTimeRenderOption | enum ( DateTimeRenderOption ) How dates, times, and durations should be represented in the output. This is ignored if valueRenderOption is FORMATTED_VALUE . The default dateTime render option is SERIAL_NUMBER . |


### Request body


The request body must be empty.


### Response body


The response when retrieving more than one range of values in a spreadsheet.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "valueRanges" : [ { object ( ValueRange ) } ] } |


| Fields |
|---|
| spreadsheetId | string The ID of the spreadsheet the data was retrieved from. |
| valueRanges[] | object ( ValueRange ) The requested values. The order of the ValueRanges is the same as the order of the requested ranges. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.readonly`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/spreadsheets.readonly`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]