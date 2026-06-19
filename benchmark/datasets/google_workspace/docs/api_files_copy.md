# Method: files.copy

*Source: https://developers.google.com/drive/api/reference/rest/v3/files/copy*

---

# Method: files.copy


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Creates a copy of a file and applies any requested updates with patch semantics. For more information, see [Create and manage files](https://developers.google.com/workspace/drive/api/guides/create-file).


### HTTP request


`POST https://www.googleapis.com/drive/v3/files/{fileId}/copy`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| fileId | string The ID of the file. |


### Query parameters


| Parameters |
|---|
| enforceSingleParent (deprecated) | boolean Deprecated: Copying files into multiple folders is no longer supported. Use shortcuts instead. |
| ignoreDefaultVisibility | boolean Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. |
| keepRevisionForever | boolean Whether to set the keepForever field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. |
| ocrLanguage | string A language hint for OCR processing during image import (ISO 639-1 code). |
| supportsAllDrives | boolean Whether the requesting application supports both My Drives and shared drives. |
| supportsTeamDrives (deprecated) | boolean Deprecated: Use supportsAllDrives instead. |
| includePermissionsForView | string Specifies which additional view's permissions to include in the response. Only published is supported. |
| includeLabels | string A comma-separated list of IDs of labels to include in the labelInfo part of the response. |


### Request body


The request body contains an instance of `File`.


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
          https://www.googleapis.com/auth/drive.photos.readonly`


Some scopes are restricted and require a security assessment for your app to use them. For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-26 UTC."],[],[]]