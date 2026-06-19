# ValueInputOption

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueInputOption*

---

# ValueInputOption


Determines how input data should be interpreted.


| Enums |
|---|
| INPUT_VALUE_OPTION_UNSPECIFIED | Default input value. This value must not be used. |
| RAW | The values the user has entered will not be parsed and will be stored as-is. |
| USER_ENTERED | The values will be parsed as if the user typed them into the UI. Numbers will stay as numbers, but strings may be converted to numbers, dates, etc. following the same rules that are applied when entering text into a cell via the Google Sheets UI. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]