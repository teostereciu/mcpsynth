# commerce/media/resources/image/methods/getImage

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/image/methods/getImage*

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

### Sample 1: Get Image Details

#### Thank you for helping us to improve the eBay developer program.
GET/image/{image_id}
This method retrieves an EPS image URL and its expiration details for the unique identifier specified in the path parameterimage_id. Use the retrieved EPS image URL to add the image to a listing through theInventory APIor theTrading API. SeeManaging imagesfor additional details.Note:If a user inputs a validimage_idas a path parameter but the EPS image associated with that ID has expired, the call will fail and a404 Not Foundstatus code will be returned.
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
The date and time when an unused EPS image will expire and be removed from the EPS server, in Coordinated Universal Time (UTC). As long as an EPS image is being used in an active listing, that image will remain on the EPS server and be accessible.Occurrence:Always
Occurrence:Always
The EPS URL to access the uploaded image. This URL will be used in listing calls to add the image to a listing.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the details of an image, including the image url and expiration date.
The input isimage_id. There is no payload with this request.
GEThttps://apim.ebay.com/commerce/media/v1_beta/image/p***************a
If the call is successful, the details of the image will be retrieved.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
image_id | string | This path parameter is the unique identifier of a created image. Use the value returned in the location header of the method used to create the image (createImageFromFileorcreateImageFromUrl, as applicable).Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
expirationDate | string | The date and time when an unused EPS image will expire and be removed from the EPS server, in Coordinated Universal Time (UTC). As long as an EPS image is being used in an active listing, that image will remain on the EPS server and be accessible.Occurrence:Always
imageUrl | string | The EPS URL to access the uploaded image. This URL will be used in listing calls to add the image to a listing.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
190000 | API_MEDIA | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
190013 | API_MEDIA | REQUEST | Unauthorized access.
190200 | API_MEDIA | REQUEST | The image resource was not found.
[/TABLE]