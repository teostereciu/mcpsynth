# Method: files.get

*Source: https://developers.google.com/drive/api/reference/rest/v3/files/get*

---

# Method: files.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Gets a file's metadata or content by ID. For more information, see [Search for files and folders](https://developers.google.com/workspace/drive/api/guides/search-files).

If you provide the URL parameter `alt=media`, then the response includes the file contents in the response body. Downloading content with `alt=media` only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [files.export](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/export) instead. For more information, see [Download and export files](https://developers.google.com/workspace/drive/api/guides/manage-downloads).


### HTTP request


`GET https://www.googleapis.com/drive/v3/files/{fileId}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| fileId | string The ID of the file. |


### Query parameters


| Parameters |
|---|
| acknowledgeAbuse | boolean Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when the alt parameter is set to media and the user is the owner of the file or an organizer of the shared drive in which the file resides. |
| supportsAllDrives | boolean Whether the requesting application supports both My Drives and shared drives. |
| supportsTeamDrives (deprecated) | boolean Deprecated: Use supportsAllDrives instead. |
| includePermissionsForView | string Specifies which additional view's permissions to include in the response. Only published is supported. |
| includeLabels | string A comma-separated list of IDs of labels to include in the labelInfo part of the response. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `File`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `
          https://www.googleapis.com/auth/drive.appdata`
- `
          https://www.googleapis.com/auth/drive.file`
- `
          https://www.googleapis.com/auth/drive.meet.readonly`
- `
          https://www.googleapis.com/auth/drive.metadata`
- `
          https://www.googleapis.com/auth/drive.metadata.readonly`
- `
          https://www.googleapis.com/auth/drive.photos.readonly`
- `
          https://www.googleapis.com/auth/drive.readonly`


Some scopes are restricted and require a security assessment for your app to use them. For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]]