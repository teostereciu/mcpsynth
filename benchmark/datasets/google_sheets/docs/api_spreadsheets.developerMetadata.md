# REST Resource: spreadsheets.developerMetadata

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.developerMetadata*

---

# REST Resource: spreadsheets.developerMetadata


- Resource: DeveloperMetadata

- JSON representation
- DeveloperMetadataLocation

- JSON representation
- DeveloperMetadataLocationType
- DeveloperMetadataVisibility
- Methods


## Resource: DeveloperMetadata


Developer metadata associated with a location or object in a spreadsheet. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


Developer metadata may be used to associate arbitrary data with various parts of a spreadsheet and it will remain associated at those locations as they move around and the spreadsheet is edited. For example, if developer metadata is associated with row 5 and another row is then subsequently inserted above row 5, that original metadata is still associated with the row it was first associated with (what is now row 6). If the associated object is deleted then its metadata is deleted too.


| JSON representation |
|---|
| { "metadataId" : integer , "metadataKey" : string , "metadataValue" : string , "location" : { object ( DeveloperMetadataLocation ) } , "visibility" : enum ( DeveloperMetadataVisibility ) } |


| Fields |
|---|
| metadataId | integer The spreadsheet-scoped unique ID that identifies the metadata. IDs may be specified when metadata is created, otherwise one will be randomly generated and assigned. Must be positive. |
| metadataKey | string The metadata key. There may be multiple metadata in a spreadsheet with the same key. Developer metadata must always have a key specified. |
| metadataValue | string Data associated with the metadata's key. |
| location | object ( DeveloperMetadataLocation ) The location where the metadata is associated. |
| visibility | enum ( DeveloperMetadataVisibility ) The metadata visibility. Developer metadata must always have visibility specified. |


### DeveloperMetadataLocation


A location where metadata may be associated in a spreadsheet.


| JSON representation |
|---|
| { "locationType" : enum ( DeveloperMetadataLocationType ) , "spreadsheet" : boolean , "sheetId" : integer , "dimensionRange" : { object ( DimensionRange ) } } |


| Fields |
|---|
| locationType | enum ( DeveloperMetadataLocationType ) The type of location this object represents. This field is read-only. |
| Union field location . The location where metadata is associated. location can be only one of the following: |
| spreadsheet | boolean True when metadata is associated with an entire spreadsheet. |
| sheetId | integer The ID of the sheet when metadata is associated with an entire sheet. |
| dimensionRange | object ( DimensionRange ) Represents the row or column when metadata is associated with a dimension. The specified DimensionRange must represent a single row or column. It cannot be unbounded or span multiple rows or columns. |


### DeveloperMetadataLocationType


An enumeration of the types of locations on which developer metadata may be associated.


| Enums |
|---|
| DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED | Default value. |
| ROW | Developer metadata associated on an entire row dimension. |
| COLUMN | Developer metadata associated on an entire column dimension. |
| SHEET | Developer metadata associated on an entire sheet. |
| SPREADSHEET | Developer metadata associated on the entire spreadsheet. |


### DeveloperMetadataVisibility


An enumeration of possible metadata visibilities.


| Enums |
|---|
| DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED | Default value. |
| DOCUMENT | Document-visible metadata is accessible from any developer project with access to the document. |
| PROJECT | Project-visible metadata is only visible to and accessible by the developer project that created the metadata. |


| Methods |
|---|
| get | Returns the developer metadata with the specified ID. |
| search | Returns all developer metadata matching the specified DataFilter . |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]