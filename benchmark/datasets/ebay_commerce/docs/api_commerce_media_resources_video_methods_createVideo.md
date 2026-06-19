# commerce/media/resources/video/methods/createVideo

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/video/methods/createVideo*

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

### Sample 1: Create a video

#### Thank you for helping us to improve the eBay developer program.
This method creates a video resource. When using this method, specify thetitle,size, andclassificationof the video resource to be created.Descriptionis an optional field for this method.Tip:SeeAdding a video to your listingin the eBay Seller Center for details about video formatting requirements and restrictions, or visit the relevant eBay site help pages for the region in which the listings will be posted.When a video resource is successfully created, the method returns the HTTP Status Code201 Created.The method also returns the location response header containing thevideo ID, which you can use to retrieve the video.Note:There is no ability to edit metadata on videos at this time. There is also no method to delete videos.To upload a created video to a created video resource, use theuploadVideomethod.Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
This method is supported in Sandbox environment. To access the endpoint, just replace theapim.ebay.comroot URI withapim.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value isITEM.Occurrence:Required
The description of the video.Occurrence:Optional
Occurrence:Optional
The size, in bytes, of the video content.Max:157,286,400 bytesOccurrence:Required
The title of the video.Occurrence:Required
SeeHTTP response headersfor details.
This call has no payload.
This call has no field definitions.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample creates a video given atitle,size, andclassificationas metadata.
The inputs are thetitle,size,classification, and (optionally)description.
POSThttps://apim.ebay.com/commerce/media/v1_beta/video
The output is an HTTP status. If the call is successful, the video will be created and the video ID is returned in theLocationheader.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
classification | array ofClassification | The intended use for this video content. Currently, videos can only be added and associated with eBay listings, so the only supported value isITEM.Occurrence:Required
description | string | The description of the video.Occurrence:Optional
size | integer | The size, in bytes, of the video content.Max:157,286,400 bytesOccurrence:Required
title | string | The title of the video.Occurrence:Required
[/TABLE]

[TABLE]
Location | The created video resource location and the uniquevideo ID.
[/TABLE]

[TABLE]
201 | Created
400 | Bad Request
403 | Forbidden
500 | Internal Server Error
[/TABLE]

[TABLE]
190000 | API_MEDIA | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
190002 | API_MEDIA | REQUEST | Missing or invalid size. Size (in bytes) is required.
190003 | API_MEDIA | REQUEST | Maximum size exceeded for supported uploads. Please refer to documentation.
190004 | API_MEDIA | REQUEST | Title length exceeded. Please refer to documentation.
190005 | API_MEDIA | REQUEST | Description length exceeded. Please refer to documentation.
190006 | API_MEDIA | REQUEST | Title is required.
190013 | API_MEDIA | REQUEST | Unauthorized access.
190014 | API_MEDIA | REQUEST | A video classification is required.
190016 | API_MEDIA | REQUEST | Markups are not permitted in the video title.
190017 | API_MEDIA | REQUEST | Markups are not permitted in the video description.
[/TABLE]