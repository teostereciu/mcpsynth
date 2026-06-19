# Method: spreadsheets.create

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/create*

---

# Method: spreadsheets.create


- HTTP request
- Request body
- Response body
- Authorization scopes
- Try it!


Creates a spreadsheet, returning the newly created spreadsheet.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Request body


The request body contains an instance of `Spreadsheet`.


### Response body


If successful, the response body contains a newly created instance of `Spreadsheet`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]