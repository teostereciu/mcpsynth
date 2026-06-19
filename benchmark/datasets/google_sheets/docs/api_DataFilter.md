# DataFilter

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/DataFilter*

---

# DataFilter


- JSON representation
- DeveloperMetadataLookup

- JSON representation
- DeveloperMetadataLocationMatchingStrategy


Filter that describes what data should be selected or returned from a request. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata).


| JSON representation |
|---|
| { "developerMetadataLookup" : { object ( DeveloperMetadataLookup ) } , "a1Range" : string , "gridRange" : { object ( GridRange ) } } |


| Fields |
|---|
| Union field filter . The kinds of filters that may limit what data is selected. filter can be only one of the following: |
| developerMetadataLookup | object ( DeveloperMetadataLookup ) Selects data associated with the developer metadata matching the criteria described by this DeveloperMetadataLookup . |
| a1Range | string Selects data that matches the specified A1 range. |
| gridRange | object ( GridRange ) Selects data that matches the range described by the GridRange . |


## DeveloperMetadataLookup


Selects `DeveloperMetadata` that matches all of the specified fields. For example, if only a metadata ID is specified this considers the `DeveloperMetadata` with that particular unique ID. If a metadata key is specified, this considers all developer metadata with that key. If a key, visibility, and location type are all specified, this considers all developer metadata with that key and visibility that are associated with a location of that type. In general, this selects all `DeveloperMetadata` that match the intersection of all the specified fields; any field or combination of fields may be specified.


| JSON representation |
|---|
| { "locationType" : enum ( DeveloperMetadataLocationType ) , "metadataLocation" : { object ( DeveloperMetadataLocation ) } , "locationMatchingStrategy" : enum ( DeveloperMetadataLocationMatchingStrategy ) , "metadataId" : integer , "metadataKey" : string , "metadataValue" : string , "visibility" : enum ( DeveloperMetadataVisibility ) } |


| Fields |
|---|
| locationType | enum ( DeveloperMetadataLocationType ) Limits the selected developer metadata to those entries which are associated with locations of the specified type. For example, when this field is specified as ROW this lookup only considers developer metadata associated on rows. If the field is left unspecified, all location types are considered. This field cannot be specified as SPREADSHEET when the locationMatchingStrategy is specified as INTERSECTING or when the metadataLocation is specified as a non-spreadsheet location. Spreadsheet metadata cannot intersect any other developer metadata location. This field also must be left unspecified when the locationMatchingStrategy is specified as EXACT. |
| metadataLocation | object ( DeveloperMetadataLocation ) Limits the selected developer metadata to those entries associated with the specified location. This field either matches exact locations or all intersecting locations according the specified locationMatchingStrategy . |
| locationMatchingStrategy | enum ( DeveloperMetadataLocationMatchingStrategy ) Determines how this lookup matches the location. If this field is specified as EXACT, only developer metadata associated on the exact location specified is matched. If this field is specified to INTERSECTING, developer metadata associated on intersecting locations is also matched. If left unspecified, this field assumes a default value of INTERSECTING . If this field is specified, a metadataLocation must also be specified. |
| metadataId | integer Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_id . |
| metadataKey | string Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_key . |
| metadataValue | string Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_value . |
| visibility | enum ( DeveloperMetadataVisibility ) Limits the selected developer metadata to that which has a matching DeveloperMetadata.visibility . If left unspecified, all developer metadata visible to the requesting project is considered. |


## DeveloperMetadataLocationMatchingStrategy


An enumeration of strategies for matching developer metadata locations.


| Enums |
|---|
| DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED | Default value. This value must not be used. |
| EXACT_LOCATION | Indicates that a specified location should be matched exactly. For example, if row three were specified as a location this matching strategy would only match developer metadata also associated on row three. Metadata associated on other locations would not be considered. |
| INTERSECTING_LOCATION | Indicates that a specified location should match that exact location as well as any intersecting locations. For example, if row three were specified as a location this matching strategy would match developer metadata associated on row three as well as metadata associated on locations that intersect row three. If, for instance, there was developer metadata associated on column B, this matching strategy would also match that location because column B intersects row three. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]