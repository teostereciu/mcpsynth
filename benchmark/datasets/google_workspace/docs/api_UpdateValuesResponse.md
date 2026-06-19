# UpdateValuesResponse

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/UpdateValuesResponse*

---

# UpdateValuesResponse


- JSON representation


The response when updating a range of values in a spreadsheet.


| JSON representation |
|---|
| { "spreadsheetId" : string , "updatedRange" : string , "updatedRows" : integer , "updatedColumns" : integer , "updatedCells" : integer , "updatedData" : { object ( ValueRange ) } } |


| Fields |
|---|
| spreadsheetId | string The spreadsheet the updates were applied to. |
| updatedRange | string The range (in A1 notation) that updates were applied to. |
| updatedRows | integer The number of rows where at least one cell in the row was updated. |
| updatedColumns | integer The number of columns where at least one cell in the column was updated. |
| updatedCells | integer The number of cells updated. |
| updatedData | object ( ValueRange ) The values of the cells after updates were applied. This is only included if the request's includeValuesInResponse field was true . |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]