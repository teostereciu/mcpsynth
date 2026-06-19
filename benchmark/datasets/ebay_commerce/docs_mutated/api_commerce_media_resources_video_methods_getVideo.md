# commerce/media/resources/video/methods/getVideo

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/video/methods/getVideo*

---

## Input

### Resource URI

### URI parameters

### HTTP request headers

### OAuth scope

### Request payload

### Request fields

## Output

### HTTP response headers

### Response payload

### Response fields

### HTTP status codes

## Error codes

## Warnings

## Samples

### Sample 1: Get Video Details

#### Thank you for helping us to improve the eBay developer program.
GET/video/{video_id}
This method retrieves a video's metadata and content given a specifiedvideo ID. The method returns thetitle,size,classification,description,video ID,playList,status,status message(if any),expiration  date, andthumbnailimage of the retrieved video.The video'stitle,size,classification, anddescriptionare set using thecreateVideomethod.The video'splayListcontains two URLs that link to instances of the streaming video based on the supported protocol.Thestatusfield contains the current status of the video. After a video upload is successfully completed, the video'sstatuswill show asPROCESSINGuntil the video reaches one of the terminal states ofLIVE,BLOCKEDorPROCESSING_FAILED.If a video's processing fails, it could be because the file is corrupted, is too large, or its size doesn't match what was provided in the metadata. Refer to the error messages to determine the cause of the video's failure to upload.Thestatus messagewill indicate why a video was blocked from uploading.If a video is not being used on an active listing, itsexpiration dateis automatically set to 30 days after the video's initial upload.The video'sthumbnailimage is automatically generated when the video is created.
The video'stitle,size,classification, anddescriptionare set using thecreateVideomethod.
The video'splayListcontains two URLs that link to instances of the streaming video based on the supported protocol.
Thestatusfield contains the current status of the video. After a video upload is successfully completed, the video'sstatuswill show asPROCESSINGuntil the video reaches one of the terminal states ofLIVE,BLOCKEDorPROCESSING_FAILED.If a video's processing fails, it could be because the file is corrupted, is too large, or its size doesn't match what was provided in the metadata. Refer to the error messages to determine the cause of the video's failure to upload.Thestatus messagewill indicate why a video was blocked from uploading.If a video is not being used on an active listing, itsexpiration dateis automatically set to 30 days after the video's initial upload.The video'sthumbnailimage is automatically generated when the video is created.
If a video's processing fails, it could be because the file is corrupted, is too large, or its size doesn't match what was provided in the metadata. Refer to the error messages to determine the cause of the video's failure to upload.
Thestatus messagewill indicate why a video was blocked from uploading.
If a video is not being used on an active listing, itsexpiration dateis automatically set to 30 days after the video's initial upload.The video'sthumbnailimage is automatically generated when the video is created.
The video'sthumbnailimage is automatically generated when the video is created.
This method is supported in Sandbox environment. To access the endpoint, just replace theapim.ebay.comroot URI withapim.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value isITEM.Occurrence:Always
Occurrence:Always
The description of the video. The video description is an optional field that can be set using thecreateVideomethod.Occurrence:Conditional
Occurrence:Conditional
The date and time when an unused video will expire and be removed from the eBay Video Services server, in Coordinated Universal Time (UTC).As long as a video is being used in an active listing, that video will remain on the server and be accessible. If a video is not being used on an active listing, its expiration date is automatically set to 30 days after the video's initial upload.Occurrence:Conditional
The video moderation information that is returned if a video is blocked by moderators.Tip:SeeVideo moderation and restrictionsin the eBay Seller Center for details about video moderation.If the video status isBLOCKED, ensure that the video complies with eBay's video formatting and content guidelines. Afterwards, begin the video creation and upload procedure anew using thecreateVideoanduploadVideomethods.Occurrence:Conditional
The reason(s) why the specified video was blocked by moderators.Occurrence:Conditional
The playlist created for the uploaded video, which provides the streaming video URLs to play the video. The supported streaming video protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming). The playlist will only be generated if a video is successfully uploaded with a status ofLIVE.Occurrence:Conditional
The playable URL for this video.Occurrence:Conditional
The protocol for the video playlist. Supported protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming).Occurrence:Conditional
The size, in bytes, of the video content.Occurrence:Always
The status of the current video resource.Occurrence:Conditional
ThestatusMessagefield contains additional information on the status. For example, information on why processing might have failed or if the video was blocked.Occurrence:Conditional
The URL of the thumbnail image of the video. The thumbnail image's URL must be an eBayPictureURL (EPS URL).Occurrence:Conditional
The URL of the image's location.Occurrence:Conditional
The title of the video.Occurrence:Always
The unique ID of the video.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the details of a video, including the title, size, classification, description, video ID, playList, status, status message (if any), expiration date, and thumbnail image.
The input isvideo_id. There is no payload with this request.
GEThttps://apim.ebay.com/commerce/media/v1_beta/video/f******************************a
If the call is successful, details of the video will be retrieved.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
video_id | string | The unique identifier of the video to be retrieved.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
classification | array ofClassification | The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value isITEM.Occurrence:Always
description | string | The description of the video. The video description is an optional field that can be set using thecreateVideomethod.Occurrence:Conditional
expirationDate | string | The date and time when an unused video will expire and be removed from the eBay Video Services server, in Coordinated Universal Time (UTC).As long as a video is being used in an active listing, that video will remain on the server and be accessible. If a video is not being used on an active listing, its expiration date is automatically set to 30 days after the video's initial upload.Occurrence:Conditional
moderation | Moderation | The video moderation information that is returned if a video is blocked by moderators.Tip:SeeVideo moderation and restrictionsin the eBay Seller Center for details about video moderation.If the video status isBLOCKED, ensure that the video complies with eBay's video formatting and content guidelines. Afterwards, begin the video creation and upload procedure anew using thecreateVideoanduploadVideomethods.Occurrence:Conditional
moderation.rejectReasons | array ofRejectReasonEnum | The reason(s) why the specified video was blocked by moderators.Occurrence:Conditional
playLists | array ofPlay | The playlist created for the uploaded video, which provides the streaming video URLs to play the video. The supported streaming video protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming). The playlist will only be generated if a video is successfully uploaded with a status ofLIVE.Occurrence:Conditional
playLists.playUrl | string | The playable URL for this video.Occurrence:Conditional
playLists.protocol | ProtocolEnum | The protocol for the video playlist. Supported protocols are DASH (Dynamic Adaptive Streaming over HTTP) and HLS (HTTP Live Streaming).Occurrence:Conditional
size | integer | The size, in bytes, of the video content.Occurrence:Always
status | VideoStatusEnum | The status of the current video resource.Occurrence:Conditional
statusMessage | string | ThestatusMessagefield contains additional information on the status. For example, information on why processing might have failed or if the video was blocked.Occurrence:Conditional
thumbnail | Image | The URL of the thumbnail image of the video. The thumbnail image's URL must be an eBayPictureURL (EPS URL).Occurrence:Conditional
thumbnail.imageUrl | string | The URL of the image's location.Occurrence:Conditional
title | string | The title of the video.Occurrence:Always
videoId | string | The unique ID of the video.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
190000 | API_MEDIA | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
190001 | API_MEDIA | REQUEST | The specified video_Id does not exist.
190013 | API_MEDIA | REQUEST | Unauthorized access.
[/TABLE]