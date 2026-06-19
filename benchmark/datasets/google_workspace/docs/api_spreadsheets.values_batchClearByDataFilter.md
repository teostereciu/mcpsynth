# Method: spreadsheets.values.batchClearByDataFilter

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/batchClearByDataFilter*

---

# Method: spreadsheets.values.batchClearByDataFilter


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- Try it!


Clears one or more ranges of values from a spreadsheet. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


The caller must specify the spreadsheet ID and one or more `DataFilters`. Ranges matching any of the specified data filters will be cleared. Only values are cleared -- all other properties of the cell (such as formatting, data validation, etc.) are kept.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values:batchClearByDataFilter`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to update. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "dataFilters" : [ { object ( DataFilter ) } ] } |


| Fields |
|---|
| dataFilters[] | object ( DataFilter ) The DataFilters used to determine which ranges to clear. |


### Response body


The response when clearing a range of values selected with `DataFilters` in a spreadsheet.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "clearedRanges" : [ string ] } |


| Fields |
|---|
| spreadsheetId | string The spreadsheet the updates were applied to. |
| clearedRanges[] | string The ranges that were cleared, in A1 notation . If the requests are for an unbounded range or a range larger than the bounds of the sheet, this is the actual ranges that were cleared, bounded to the sheet's limits. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]]