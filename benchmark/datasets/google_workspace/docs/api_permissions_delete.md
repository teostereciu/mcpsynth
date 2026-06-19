# Method: permissions.delete

*Source: https://developers.google.com/drive/api/reference/rest/v3/permissions/delete*

---

# Method: permissions.delete


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Deletes a permission. For more information, see [Share files, folders, and drives](https://developers.google.com/workspace/drive/api/guides/manage-sharing).


**Warning:** Concurrent permissions operations on the same file aren't supported; only the last update is applied.


### HTTP request


`DELETE https://www.googleapis.com/drive/v3/files/{fileId}/permissions/{permissionId}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| fileId | string The ID of the file or shared drive. |
| permissionId | string The ID of the permission. |


### Query parameters


| Parameters |
|---|
| supportsAllDrives | boolean Whether the requesting application supports both My Drives and shared drives. |
| supportsTeamDrives (deprecated) | boolean Deprecated: Use supportsAllDrives instead. |
| useDomainAdminAccess | boolean Issue the request as a domain administrator. If set to true , and if the following additional conditions are met, the requester is granted access: The file ID parameter refers to a shared drive. The requester is an administrator of the domain to which the shared drive belongs. For more information, see Manage shared drives as domain administrators . |
| enforceExpansiveAccess (deprecated) | boolean Deprecated: All requests use the expansive access rules. |


### Request body


The request body must be empty.


### Response body


If successful, the response body is an empty JSON object.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `
          https://www.googleapis.com/auth/drive.file`


Some scopes are restricted and require a security assessment for your app to use them. For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]]