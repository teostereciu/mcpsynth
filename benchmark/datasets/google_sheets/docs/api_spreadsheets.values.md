# REST Resource: spreadsheets.values

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values*

---

# REST Resource: spreadsheets.values


- Resource: ValueRange

- JSON representation
- Methods


## Resource: ValueRange


Data within a range of the spreadsheet.


| JSON representation |
|---|
| { "range" : string , "majorDimension" : enum ( Dimension ) , "values" : [ array ] } |


| Fields |
|---|
| range | string The range the values cover, in A1 notation . For output, this range indicates the entire requested range, even though the values will exclude trailing rows and columns. When appending values, this field represents the range to search for a table, after which values will be appended. |
| majorDimension | enum ( Dimension ) The major dimension of the values. For output, if the spreadsheet data is: A1=1,B1=2,A2=3,B2=4 , then requesting range=A1:B2,majorDimension=ROWS will return [[1,2],[3,4]] , whereas requesting range=A1:B2,majorDimension=COLUMNS will return [[1,3],[2,4]] . For input, with range=A1:B2,majorDimension=ROWS then [[1,2],[3,4]] will set A1=1,B1=2,A2=3,B2=4 . With range=A1:B2,majorDimension=COLUMNS then [[1,2],[3,4]] will set A1=1,B1=3,A2=2,B2=4 . When writing, if this field is not set, it defaults to ROWS. |
| values[] | array ( ListValue format) The data that was read or to be written. This is an array of arrays, the outer array representing all the data and each inner array representing a major dimension. Each item in the inner array corresponds with one cell. For output, empty trailing rows and columns will not be included. For input, supported value types are: bool, string, and double. Null values will be skipped. To set a cell to an empty value, set the string value to an empty string. |


| Methods |
|---|
| append | Appends values to a spreadsheet. |
| batchClear | Clears one or more ranges of values from a spreadsheet. |
| batchClearByDataFilter | Clears one or more ranges of values from a spreadsheet. |
| batchGet | Returns one or more ranges of values from a spreadsheet. |
| batchGetByDataFilter | Returns one or more ranges of values that match the specified data filters. |
| batchUpdate | Sets values in one or more ranges of a spreadsheet. |
| batchUpdateByDataFilter | Sets values in one or more ranges of a spreadsheet. |
| clear | Clears values from a spreadsheet. |
| get | Returns a range of values from a spreadsheet. |
| update | Sets values in a range of a spreadsheet. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]