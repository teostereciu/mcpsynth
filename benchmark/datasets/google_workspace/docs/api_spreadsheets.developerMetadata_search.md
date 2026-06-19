# Method: spreadsheets.developerMetadata.search

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.developerMetadata/search*

---

# Method: spreadsheets.developerMetadata.search


- HTTP request
- Path parameters
- Request body

- JSON representation
- Response body

- JSON representation
- Authorization scopes
- MatchedDeveloperMetadata

- JSON representation
- Try it!


Returns all developer metadata matching the specified `DataFilter`. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


If the provided `DataFilter` represents a `DeveloperMetadataLookup` object, this will return all DeveloperMetadata entries selected by it. If the `DataFilter` represents a location in a spreadsheet, this will return all developer metadata associated with locations intersecting that region.


### HTTP request


`POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/developerMetadata:search`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| spreadsheetId | string The ID of the spreadsheet to retrieve metadata from. |


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "dataFilters" : [ { object ( DataFilter ) } ] } |


| Fields |
|---|
| dataFilters[] | object ( DataFilter ) The data filters describing the criteria used to determine which DeveloperMetadata entries to return. DeveloperMetadata matching any of the specified filters are included in the response. |


### Response body


A reply to a developer metadata search request.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "matchedDeveloperMetadata" : [ { object ( MatchedDeveloperMetadata ) } ] } |


| Fields |
|---|
| matchedDeveloperMetadata[] | object ( MatchedDeveloperMetadata ) The metadata matching the criteria of the search request. |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/spreadsheets`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


## MatchedDeveloperMetadata


A developer metadata entry and the data filters specified in the original request that matched it.


| JSON representation |
|---|
| { "developerMetadata" : { object ( DeveloperMetadata ) } , "dataFilters" : [ { object ( DataFilter ) } ] } |


| Fields |
|---|
| developerMetadata | object ( DeveloperMetadata ) The developer metadata matching the specified filters. |
| dataFilters[] | object ( DataFilter ) All filters matching the returned developer metadata. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]]