# Method: presentations.pages.getThumbnail

*Source: https://developers.google.com/slides/api/reference/rest/v1/presentations.pages/getThumbnail*

---

# Method: presentations.pages.getThumbnail


- HTTP request
- Path parameters
- Query parameters
- Request body
- Response body

- JSON representation
- Authorization scopes
- ThumbnailProperties

- JSON representation
- MimeType
- ThumbnailSize
- Try it!


Generates a thumbnail of the latest version of the specified page in the presentation and returns a URL to the thumbnail image.


This request counts as an [expensive read request](https://developers.google.com/workspace/slides/limits) for quota purposes.


### HTTP request


`GET https://slides.googleapis.com/v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Path parameters


| Parameters |
|---|
| presentationId | string The ID of the presentation to retrieve. |
| pageObjectId | string The object ID of the page whose thumbnail to retrieve. |


### Query parameters


| Parameters |
|---|
| thumbnailProperties | object ( ThumbnailProperties ) The thumbnail properties. |


### Request body


The request body must be empty.


### Response body


The thumbnail of a page.


If successful, the response body contains data with the following structure:


| JSON representation |
|---|
| { "width" : integer , "height" : integer , "contentUrl" : string } |


| Fields |
|---|
| width | integer The positive width in pixels of the thumbnail image. |
| height | integer The positive height in pixels of the thumbnail image. |
| contentUrl | string The content URL of the thumbnail image. The URL to the image has a default lifetime of 30 minutes. This URL is tagged with the account of the requester. Anyone with the URL effectively accesses the image as the original requester. Access to the image may be lost if the presentation's sharing settings change. The mime type of the thumbnail image is the same as specified in the GetPageThumbnailRequest . |


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/drive.readonly`
- `https://www.googleapis.com/auth/presentations`
- `https://www.googleapis.com/auth/presentations.readonly`


For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).


## ThumbnailProperties


Provides control over page thumbnail creation.


| JSON representation |
|---|
| { "mimeType" : enum ( MimeType ) , "thumbnailSize" : enum ( ThumbnailSize ) } |


| Fields |
|---|
| mimeType | enum ( MimeType ) The optional mime type of the thumbnail image. If you don't specify the mime type, the mime type defaults to PNG. |
| thumbnailSize | enum ( ThumbnailSize ) The optional thumbnail image size. If you don't specify the size, the server chooses a default size of the image. |


## MimeType


The mime type of the thumbnail image.


| Enums |
|---|
| PNG | The default mime type. |


## ThumbnailSize


The predefined thumbnail image sizes. Values here describe the width of the thumbnail image. When the page height is greater than the width, the width may be less than the specified size.


| Enums |
|---|
| THUMBNAIL_SIZE_UNSPECIFIED | The default thumbnail image size. The unspecified thumbnail size implies that the server chooses the size of the image in a way that might vary in the future. |
| LARGE | The thumbnail image width of 1600px. |
| MEDIUM | The thumbnail image width of 800px. |
| SMALL | The thumbnail image width of 200px. |


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-20 UTC."],[],[]]