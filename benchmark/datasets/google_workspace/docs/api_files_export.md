# Method: files.export

*Source: https://developers.google.com/drive/api/reference/rest/v3/files/export*

---

# Method: files.export


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Exports a Google Workspace document to the requested MIME type and returns exported byte content. For more information, see [Download and export files](https://developers.google.com/workspace/drive/api/guides/manage-downloads).


Note that the exported content is limited to 10 MB.


### HTTP request


`GET https://www.googleapis.com/drive/v3/files/{fileId}/export`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| fileId | string The ID of the file. |


### Query parameters


| Parameters |
|---|
| mimeType | string Required. The MIME type of the format requested for this export. For a list of supported MIME types, see Export MIME types for Google Workspace documents . |


### Request body


The request body must be empty.


### Response body


If successful, this method returns the file content as bytes.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `
          https://www.googleapis.com/auth/drive.file`
- `
          https://www.googleapis.com/auth/drive.meet.readonly`
- `
          https://www.googleapis.com/auth/drive.readonly`


Some scopes are restricted and require a security assessment for your app to use them. For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-26 UTC."],[],[]]