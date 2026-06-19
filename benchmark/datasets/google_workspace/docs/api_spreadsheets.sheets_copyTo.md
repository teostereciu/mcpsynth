# Method: spreadsheets.sheets.copyTo

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.sheets/copyTo*

---

# Method: spreadsheets.sheets.copyTo


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body
- Authorization scopes
- Try it!


Copies a single sheet from a spreadsheet to another spreadsheet. Returns the properties of the newly created sheet.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/sheets/{sheetId}:copyTo`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet containing the sheet to copy. |
| sheetId | integer The ID of the sheet to copy. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "destinationSpreadsheetId" : string } |


| Fields |
|---|
| destinationSpreadsheetId | string The ID of the spreadsheet to copy the sheet to. |


### Response body


If successful, the response body contains an instance of `SheetProperties`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]