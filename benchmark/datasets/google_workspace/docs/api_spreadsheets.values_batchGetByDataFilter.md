# Method: spreadsheets.values.batchGetByDataFilter

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/batchGetByDataFilter*

---

# Method: spreadsheets.values.batchGetByDataFilter


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- MatchedValueRange

- JSON representation
- Try it!


Returns one or more ranges of values that match the specified data filters. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


The caller must specify the spreadsheet ID and one or more `DataFilters`. Ranges that match any of the data filters in the request will be returned.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values:batchGetByDataFilter`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to retrieve data from. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "dataFilters" : [ { object ( DataFilter ) } ] , "majorDimension" : enum ( Dimension ) , "valueRenderOption" : enum ( ValueRenderOption ) , "dateTimeRenderOption" : enum ( DateTimeRenderOption ) } |


| Fields |
|---|
| dataFilters[] | object ( DataFilter ) The data filters used to match the ranges of values to retrieve. Ranges that match any of the specified data filters are included in the response. |
| majorDimension | enum ( Dimension ) The major dimension that results should use. For example, if the spreadsheet data is: A1=1,B1=2,A2=3,B2=4 , then a request that selects that range and sets majorDimension=ROWS returns [[1,2],[3,4]] , whereas a request that sets majorDimension=COLUMNS returns [[1,3],[2,4]] . |
| valueRenderOption | enum ( ValueRenderOption ) How values should be represented in the output. The default render option is FORMATTED_VALUE . |
| dateTimeRenderOption | enum ( DateTimeRenderOption ) How dates, times, and durations should be represented in the output. This is ignored if valueRenderOption is FORMATTED_VALUE . The default dateTime render option is SERIAL_NUMBER . |


### Response body


The response when retrieving more than one range of values in a spreadsheet selected by `DataFilters`.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "valueRanges" : [ { object ( MatchedValueRange ) } ] } |


| Fields |
|---|
| spreadsheetId | string The ID of the spreadsheet the data was retrieved from. |
| valueRanges[] | object ( MatchedValueRange ) The requested values with the list of data filters that matched them. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


## MatchedValueRange


A value range that was matched by one or more data filers.


| JSON representation |
|---|
| { "valueRange" : { object ( ValueRange ) } , "dataFilters" : [ { object ( DataFilter ) } ] } |


| Fields |
|---|
| valueRange | object ( ValueRange ) The values matched by the DataFilter . |
| dataFilters[] | object ( DataFilter ) The DataFilters from the request that matched the range of values. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]]