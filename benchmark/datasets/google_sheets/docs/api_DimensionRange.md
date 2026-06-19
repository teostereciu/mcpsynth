# DimensionRange

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/DimensionRange*

---

# DimensionRange


- JSON representation


A range along a single dimension on a sheet. All indexes are zero-based. Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the range is unbounded on that side.


| JSON representation |
|---|
| { "sheetId" : integer , "dimension" : enum ( Dimension ) , "startIndex" : integer , "endIndex" : integer } |


| Fields |
|---|
| sheetId | integer The sheet this span is on. |
| dimension | enum ( Dimension ) The dimension of the span. |
| startIndex | integer The start (inclusive) of the span, or not set if unbounded. |
| endIndex | integer The end (exclusive) of the span, or not set if unbounded. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]