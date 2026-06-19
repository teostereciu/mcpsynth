# DateTimeRenderOption

*Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/DateTimeRenderOption*

---

# DateTimeRenderOption


Determines how dates should be rendered in the output.


| Enums |
|---|
| SERIAL_NUMBER | Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (left of the decimal) counts the days since December 30th 1899. The fractional portion (right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5, 2 because it's 2 days after December 30th 1899, and .5 because noon is half a day. February 1st 1900 at 3pm would be 33.625. This correctly treats the year 1900 as not a leap year. |
| FORMATTED_STRING | Instructs date, time, datetime, and duration fields to be output as strings in their given number format (which depends on the spreadsheet locale). |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]