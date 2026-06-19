# Method: spreadsheets.values.batchUpdate

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate*

---

# Method: spreadsheets.values.batchUpdate


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- Try it!


Sets values in one or more ranges of a spreadsheet. The caller must specify the spreadsheet ID, a `valueInputOption`, and one or more `ValueRanges`.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values:batchUpdate`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to update. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "valueInputOption" : enum ( ValueInputOption ) , "data" : [ { object ( ValueRange ) } ] , "includeValuesInResponse" : boolean , "responseValueRenderOption" : enum ( ValueRenderOption ) , "responseDateTimeRenderOption" : enum ( DateTimeRenderOption ) } |


| Fields |
|---|
| valueInputOption | enum ( ValueInputOption ) How the input data should be interpreted. |
| data[] | object ( ValueRange ) The new values to apply to the spreadsheet. |
| includeValuesInResponse | boolean Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. The updatedData field within each of the BatchUpdateValuesResponse.responses contains the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns). |
| responseValueRenderOption | enum ( ValueRenderOption ) Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE . |
| responseDateTimeRenderOption | enum ( DateTimeRenderOption ) Determines how dates, times, and durations in the response should be rendered. This is ignored if responseValueRenderOption is FORMATTED_VALUE . The default dateTime render option is SERIAL_NUMBER . |


### Response body


The response when updating a range of values in a spreadsheet.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "totalUpdatedRows" : integer , "totalUpdatedColumns" : integer , "totalUpdatedCells" : integer , "totalUpdatedSheets" : integer , "responses" : [ { object ( UpdateValuesResponse ) } ] } |


| Fields |
|---|
| spreadsheetId | string The spreadsheet the updates were applied to. |
| totalUpdatedRows | integer The total number of rows where at least one cell in the row was updated. |
| totalUpdatedColumns | integer The total number of columns where at least one cell in the column was updated. |
| totalUpdatedCells | integer The total number of cells updated. |
| totalUpdatedSheets | integer The total number of sheets where at least one cell in the sheet was updated. |
| responses[] | object ( UpdateValuesResponse ) One UpdateValuesResponse per requested range, in the same order as the requests appeared. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]