# Method: drives.get

*Source: https://developers.google.com/drive/api/reference/rest/v3/drives/get*

---

# Method: drives.get


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body
- Authorization scopes
- Try it!


Gets a shared drive's metadata by ID. For more information, see [Manage shared drives](https://developers.google.com/workspace/drive/api/guides/manage-shareddrives).


### HTTP request


`GET https://www.googleapis.com/drive/v3/drives/{driveId}`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| driveId | string The ID of the shared drive. |


### Query parameters


| Parameters |
|---|
| useDomainAdminAccess | boolean Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs. |


### Request body


The request body must be empty.


### Response body


If successful, the response body contains an instance of `Drive`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `
          https://www.googleapis.com/auth/drive.readonly`


Some scopes are restricted and require a security assessment for your app to use them. For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-13 UTC."],[],[]]