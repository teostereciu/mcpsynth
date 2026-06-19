# Method: spreadsheets.getByDataFilter

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/getByDataFilter*

---

# Method: spreadsheets.getByDataFilter


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body
- Authorization scopes
- Try it!


Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


This method differs from spreadsheets.get in that it allows selecting which subsets of spreadsheet data to return by specifying a `dataFilters` parameter. Multiple `DataFilters` can be specified. Specifying one or more data filters returns the portions of the spreadsheet that intersect ranges matched by any of the filters.


By default, data within grids is not returned. You can include grid data in one of two ways:


- Specify a [field mask](https://developers.google.com/workspace/sheets/api/guides/field-masks) listing your desired fields using the `fields` URL parameter in HTTP.
- Set the `includeGridData` parameter to `true`. If a field mask is set, the `includeGridData` parameter is ignored.


For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}:getByDataFilter`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The spreadsheet to request. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "dataFilters" : [ { object ( DataFilter ) } ] , "includeGridData" : boolean , "excludeTablesInBandedRanges" : boolean } |


| Fields |
|---|
| dataFilters[] | object ( DataFilter ) The DataFilters used to select which ranges to retrieve from the spreadsheet. |
| includeGridData | boolean True if grid data should be returned. This parameter is ignored if a field mask was set in the request. |
| excludeTablesInBandedRanges | boolean True if tables should be excluded in the banded ranges. False if not set. |


### Response body


If successful, the response body contains an instance of `Spreadsheet`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]]