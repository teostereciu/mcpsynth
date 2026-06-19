# Method: presentations.pages.get

*Source: https://developers.google.com/slides/api/reference/rest/v1/presentations.pages/get*

---

# Method: presentations.pages.get


- HTTP request
- Path parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Gets the latest version of the specified page in the presentation.


### HTTP request


`GET https://slides.googleapis.com/v1/presentations/{presentationId}/pages/{pageObjectId}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| presentationId | string The ID of the presentation to retrieve. |
| pageObjectId | string The object ID of the page to retrieve. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Page`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/drive.readonly`
- `https://www.googleapis.com/auth/presentations`
- `https://www.googleapis.com/auth/presentations.readonly`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-20 UTC."],[],[]]