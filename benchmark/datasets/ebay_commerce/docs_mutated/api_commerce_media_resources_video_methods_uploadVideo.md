# commerce/media/resources/video/methods/uploadVideo

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/video/methods/uploadVideo*

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

### Sample 1: Upload a Video

#### Thank you for helping us to improve the eBay developer program.
POST/video/{video_id}/upload
This method associates the specified file with the specifiedvideo IDand uploads the input file. After the file has been uploaded the processing of the file begins.Note:The size of the video to be uploaded must exactly match the size of the video's input stream that was set in thecreateVideomethod. If the sizes do not match, the video will not upload successfully.When a video is successfully uploaded, it returns the HTTP Status Code200 OK.The status flow isPENDING_UPLOAD>PROCESSING>LIVE,PROCESSING_FAILED, orBLOCKED. After a video upload is successfully completed, the status will show asPROCESSINGuntil the video reaches one of the terminal states ofLIVE,BLOCKED, orPROCESSING_FAILED. If the size information (in bytes) provided is incorrect, the API will throw an error.Tip:SeeAdding a video to your listingin the eBay Seller Center for details about video formatting requirements and restrictions, or visit the relevant eBay site help pages for the region in which the listings will be posted.To retrieve an uploaded video, use thegetVideomethod.Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
This method is supported in Sandbox environment. To access the endpoint, just replace theapim.ebay.comroot URI withapim.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Strongly Recommended
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
Note:This method has no request payload. Instead, a video file is uploaded to the endpoint. The input stream source must be an .mp4 file of the type MPEG-4 Part 10 or Advanced Video Coding (MPEG-4 AVC).
This call has no payload.
This call has no field definitions.
This call has no response headers.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample uploads a selected video file using a created video ID.
The inputs are thevideo_idand a specified video file.
POSThttps://apim.ebay.com/commerce/media/v1_beta/video/f******************************a/upload
The output is an HTTP status. If the call is successful, the video will be uploaded.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
video_id | string | The unique identifier of the video to be uploaded.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Length | string | Use this header to specify the content length for the upload. Use Content-Range: bytes {1}-{2}/{3} and Content-Length:{4} headers.Note:This header is optional and is only required forresumableuploads (when an upload is interrupted and must be resumed from a certain point).Occurrence:Strongly Recommended
Content-Range | string | Use this header to specify the content range for the upload. The Content-Range should be of the following bytes ((?:[0-9]+-[0-9]+)|\\\\*)/([0-9]+|\\\\*) pattern.Note:This header is optional and is only required forresumableuploads (when an upload is interrupted and must be resumed from a certain point).Occurrence:Strongly Recommended
Content-Type | string | Use this header to specify the content type for the upload. The Content-Type should be set toapplication/octet-stream.Occurrence:Required
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
403 | Forbidden
404 | Not Found
409 | Conflict
411 | Content Length Required
416 | Range Not Satisfiable
500 | Internal Server Error
[/TABLE]

[TABLE]
190000 | API_MEDIA | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
190001 | API_MEDIA | REQUEST | The specified video_Id does not exist.
190007 | API_MEDIA | REQUEST | The content length does not match the content size specified.
190008 | API_MEDIA | REQUEST | The content length is required.
190009 | API_MEDIA | REQUEST | The Content-Range specified is incorrect. Use Content-Range: bytes {1}}-{2}/{3} and Content-Length:{4} headers.
190010 | API_MEDIA | REQUEST | The video's Content-Range is invalid. The Content-Range should be of the following bytes ((?:[0-9]+-[0-9]+)|\\\\*)/([0-9]+|\\\\*) pattern.
190011 | API_MEDIA | REQUEST | The video is already uploaded.
190012 | API_MEDIA | REQUEST | The content length of the video is invalid.
190013 | API_MEDIA | REQUEST | Unauthorized access.
190015 | API_MEDIA | REQUEST | The uploaded content must match the video size.
[/TABLE]