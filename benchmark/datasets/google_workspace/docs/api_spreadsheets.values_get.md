# Method: spreadsheets.values.get

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/get*

---

# Method: spreadsheets.values.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Returns a range of values from a spreadsheet. The caller must specify the spreadsheet ID and a range.


### HTTP request


`GET https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to retrieve data from. |
| range | string The A1 notation or R1C1 notation of the range to retrieve values from. |


### Query parameters


| Parameters |
|---|
| majorDimension | enum ( Dimension ) The major dimension that results should use. For example, if the spreadsheet data in Sheet1 is: A1=1,B1=2,A2=3,B2=4 , then requesting range=Sheet1!A1:B2?majorDimension=ROWS returns [[1,2],[3,4]] , whereas requesting range=Sheet1!A1:B2?majorDimension=COLUMNS returns [[1,3],[2,4]] . |
| valueRenderOption | enum ( ValueRenderOption ) How values should be represented in the output. The default render option is FORMATTED_VALUE . |
| dateTimeRenderOption | enum ( DateTimeRenderOption ) How dates, times, and durations should be represented in the output. This is ignored if valueRenderOption is FORMATTED_VALUE . The default dateTime render option is SERIAL_NUMBER . |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `ValueRange`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.readonly`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/spreadsheets.readonly`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]