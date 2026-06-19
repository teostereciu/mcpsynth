# Method: spreadsheets.values.clear

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/clear*

---

# Method: spreadsheets.values.clear


- HTTP request
- Path parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- Try it!


Clears values from a spreadsheet. The caller must specify the spreadsheet ID and range. Only values are cleared -- all other properties of the cell (such as formatting, data validation, etc..) are kept.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}:clear`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to update. |
| range | string The A1 notation or R1C1 notation of the values to clear. |


### Request body


The request body must be empty.


### Response body


The response when clearing a range of values in a spreadsheet.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "spreadsheetId" : string , "clearedRange" : string } |


| Fields |
|---|
| spreadsheetId | string The spreadsheet the updates were applied to. |
| clearedRange | string The range (in A1 notation) that was cleared. (If the request was for an unbounded range or a range larger  than the bounds of the sheet, this will be the actual range  that was cleared, bounded to the sheet's limits.) |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]]