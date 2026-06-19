# Method: spreadsheets.developerMetadata.get

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.developerMetadata/get*

---

# Method: spreadsheets.developerMetadata.get


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and the developer metadata's unique `metadataId`. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


### HTTP request


`GET https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/developerMetadata/{metadataId}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to retrieve metadata from. |
| metadataId | integer The ID of the developer metadata to retrieve. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `DeveloperMetadata`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]]