# commerce/media/resources/image/methods/createImageFromUrl

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/image/methods/createImageFromUrl*

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

### Sample 1: Create an image from a URL

#### Thank you for helping us to improve the eBay developer program.
POST/image/create_image_from_url
This method uploads a picture to eBay Picture Services (EPS) from the specified URL. Specify the location of the picture on an external web server through theimageUrlfield.All images must comply with eBay’s picture requirements, such as dimension and file size restrictions. For more information, seePicture policy. The image formats supported areJPG,GIF,PNG,BMP,TIFF,AVIF,HEIC, andWEBP. In addition, the provided URL must be secured using HTTPS (HTTP is not permitted). For more information, seeImage requirements.Note:Animated GIF, and multi-page PNG/TIFF files, are not supported. Any animation effect of supported formats will be lost upon upload.When an EPS image is successfully created, the method returns the HTTP Status Code201 Created. The method also returns the getImage URI in theLocationresponse header.Important!Make sure to capture the image ID URI returned in the responselocation headerprovided in the following format:https://apim.ebay.com/commerce/media/v1_beta/image/{image_id}You can capture the entire URI, or just save the{image_id}only. Pass the{image_id}as a path parameter in thegetImagemethod to return the value needed to associate an image to a listing using the Trading and Inventory APIs.SeeManaging imagesfor additional details.Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
All images must comply with eBay’s picture requirements, such as dimension and file size restrictions. For more information, seePicture policy. The image formats supported areJPG,GIF,PNG,BMP,TIFF,AVIF,HEIC, andWEBP. In addition, the provided URL must be secured using HTTPS (HTTP is not permitted). For more information, seeImage requirements.
Note:Animated GIF, and multi-page PNG/TIFF files, are not supported. Any animation effect of supported formats will be lost upon upload.
When an EPS image is successfully created, the method returns the HTTP Status Code201 Created. The method also returns the getImage URI in theLocationresponse header.
Important!Make sure to capture the image ID URI returned in the responselocation headerprovided in the following format:
https://apim.ebay.com/commerce/media/v1_beta/image/{image_id}
You can capture the entire URI, or just save the{image_id}only. Pass the{image_id}as a path parameter in thegetImagemethod to return the value needed to associate an image to a listing using the Trading and Inventory APIs.
SeeManaging imagesfor additional details.
Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
This method is supported in Sandbox environment. To access the endpoint, just replace theapim.ebay.comroot URI withapim.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
The image URL of the self-hosted picture to upload to eBay Picture Services (EPS). In addition to the picture requirements inPicture policy, the provided URL must be secured using HTTPS (HTTP is not permitted). For more information, seeImage requirements.Occurrence:Required
SeeHTTP response headersfor details.
The date and time when an unused EPS image will expire and be removed from the EPS server, in Coordinated Universal Time (UTC). As long as an EPS image is being used in an active listing, that image will remain on the EPS server and be accessible.Occurrence:Always
Occurrence:Always
The EPS URL to access the uploaded image. This URL will be used in listing calls to add the image to a listing.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample uploads a picture to eBay Picture Services (EPS) from the specified URL.
The URL of the image (imageUrl) is required when calling this method.
POSThttps://apim.ebay.com/commerce/media/v1_beta/image/create_image_from_url
If the call is successful, an HTTP status of201 Createdwill be returned alongside the following payload. If the call is successful, the image will be created and the image ID URI will be returned in theLocationheader.
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
imageUrl | string | The image URL of the self-hosted picture to upload to eBay Picture Services (EPS). In addition to the picture requirements inPicture policy, the provided URL must be secured using HTTPS (HTTP is not permitted). For more information, seeImage requirements.Occurrence:Required
[/TABLE]

[TABLE]
Location | The location response header contains the URI of the newly created image ID in the format:https://apim.ebay.com/commerce/media/v1_beta/image/{image_id}Capture this URI to use with thegetImagemethod. SeeManaging imagesfor more information.
[/TABLE]

[TABLE]
Output container/field | Type | Description
expirationDate | string | The date and time when an unused EPS image will expire and be removed from the EPS server, in Coordinated Universal Time (UTC). As long as an EPS image is being used in an active listing, that image will remain on the EPS server and be accessible.Occurrence:Always
imageUrl | string | The EPS URL to access the uploaded image. This URL will be used in listing calls to add the image to a listing.Occurrence:Always
[/TABLE]

[TABLE]
201 | Created
400 | Bad Request
403 | Forbidden
500 | Internal Server Error
[/TABLE]

[TABLE]
190000 | API_MEDIA | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
190013 | API_MEDIA | REQUEST | Unauthorized access.
190201 | API_MEDIA | REQUEST | The image file size is larger than the limit. Please refer to the documentation.
190202 | API_MEDIA | REQUEST | The supplied image dimensions exceed the limit. Please refer to the documentation.
190203 | API_MEDIA | REQUEST | The supplied image is in a format that is not supported. Please refer to the documentation for a list of supported formats.
190204 | API_MEDIA | REQUEST | No valid image can be downloaded from the provided imageUrl. Please refer to the documentation.
[/TABLE]