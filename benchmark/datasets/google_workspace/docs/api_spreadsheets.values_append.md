# Method: spreadsheets.values.append

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append*

---

# Method: spreadsheets.values.append


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- InsertDataOption
- Try it!


Appends values to a spreadsheet. The input range is used to search for existing data and find a "table" within that range. Values will be appended to the next row of the table, starting with the first column of the table. See the [guide](https://developers.google.com/workspace/sheets/api/guides/values#appending_values) and [sample code](https://developers.google.com/workspace/sheets/api/samples/writing#append_values) for specific details of how tables are detected and data is appended.


The caller must specify the spreadsheet ID, range, and a `valueInputOption`. The `valueInputOption` only controls how the input data will be added to the sheet (column-wise or row-wise), it does not influence what cell the data starts being written to.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}:append`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to update. |
| range | string The A1 notation of a range to search for a logical table of data. Values are appended after the last row of the table. |


### Query parameters


| Parameters |
|---|
| valueInputOption | enum ( ValueInputOption ) How the input data should be interpreted. |
| insertDataOption | enum ( InsertDataOption ) How the input data should be inserted. |
| includeValuesInResponse | boolean Determines if the update response should include the values of the cells that were appended. By default, responses do not include the updated values. |
| responseValueRenderOption | enum ( ValueRenderOption ) Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE . |
| responseDateTimeRenderOption | enum ( DateTimeRenderOption ) Determines how dates, times, and durations in the response should be rendered. This is ignored if responseValueRenderOption is FORMATTED_VALUE . The default dateTime render option is SERIAL_NUMBER . |


### Request body


The request body contains an instance of `ValueRange`.


### Response body


The response when updating a range of values in a spreadsheet.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "tableRange" : string , "updates" : { object ( UpdateValuesResponse ) } } |


| Fields |
|---|
| spreadsheetId | string The spreadsheet the updates were applied to. |
| tableRange | string The range (in A1 notation) of the table that values are being appended to (before the values were appended). Empty if no table was found. |
| updates | object ( UpdateValuesResponse ) Information about the updates that were applied. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


## InsertDataOption


Determines how existing data is changed when new data is input.


| Enums |
|---|
| OVERWRITE | The new data overwrites existing data in the areas it is written. (Note: adding data to the end of the sheet will still insert  new rows or columns so the data can be written.) |
| INSERT_ROWS | Rows are inserted for the new data. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]