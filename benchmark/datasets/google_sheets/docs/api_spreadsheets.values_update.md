# Method: spreadsheets.values.update

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/update*

---

# Method: spreadsheets.values.update


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Sets values in a range of a spreadsheet. The caller must specify the spreadsheet ID, range, and a `valueInputOption`.


### HTTP request


`PUT https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to update. |
| range | string The A1 notation of the values to update. |


### Query parameters


| Parameters |
|---|
| valueInputOption | enum ( ValueInputOption ) How the input data should be interpreted. |
| includeValuesInResponse | boolean Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns). |
| responseValueRenderOption | enum ( ValueRenderOption ) Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE . |
| responseDateTimeRenderOption | enum ( DateTimeRenderOption ) Determines how dates, times, and durations in the response should be rendered. This is ignored if responseValueRenderOption is FORMATTED_VALUE . The default dateTime render option is SERIAL_NUMBER . |


### Request body


The request body contains an instance of `ValueRange`.


### Response body


If successful, the response body contains an instance of `UpdateValuesResponse`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]