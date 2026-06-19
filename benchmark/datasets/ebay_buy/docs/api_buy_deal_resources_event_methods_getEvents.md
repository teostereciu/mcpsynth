# buy/deal/resources/event/methods/getEvents

*Source: https://developer.ebay.com/api-docs/buy/deal/resources/event/methods/getEvents*

---

### Restrictions

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

### Sample 1: Retrieve Events for a Specified Marketplace

#### Thank you for helping us to improve the eBay developer program.
This method returns paginated results containing all eBay events for the specified marketplace.RestrictionsThis method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, seeAPI Restrictions.eBay Partner Network:In order to receive a commission for your sales, you must use the URL returned in theitemAffiliateWebUrlfield to forward your buyer to the ebay.com site.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.deal
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
A list of results that match the search criteria.Occurrence:Conditional
Occurrence:Conditional
A list of coupons associated with the event.Occurrence:Conditional
The coupon code.Occurrence:Conditional
The terms of use associated with the coupon.Occurrence:Conditional
A full-text description of the terms.Occurrence:Conditional
A summarized description of the terms.Occurrence:Conditional
The event description.Occurrence:Conditional
The end date for the event.Occurrence:Conditional
The URL of the View Event page for the event, which includes the affiliate tracking ID.Occurrence:Conditional
The unique identifier for the event.Occurrence:Conditional
The web URL for the event.Occurrence:Conditional
The images for the event.Occurrence:Conditional
The height of the image.Occurrence:Conditional
The relative path to the image location.Occurrence:Conditional
The text associated with the image.Occurrence:Conditional
The width of the image.Occurrence:Conditional
The start date for the event.Occurrence:Conditional
The terms associated with the event.Occurrence:Conditional
The title of the event.Occurrence:Conditional
The relative path to the current set of results.Occurrence:Conditional
The maximum number of items, from the current result set, returned on a single page.Default:20Occurrence:Conditional
The relative path to the next set of results.Occurrence:Conditional
The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Default:0Occurrence:Conditional
The relative path to the previous set of results.Occurrence:Conditional
The total number of matches for the specified search criteria.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves a paginated set of events associated with the specified marketplace ID.
The input is thelimitURI parameter. There is no payload with this request.
GEThttps://api.ebay.com/buy/deal/v1/event?limit=1
If the call is successful, one event matching the specified marketplace will be returned.
Related topics
If you need help, contactDeveloper Technical Support.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
limit | string | The maximum number of items, from the current result set, returned on a single page.Default:20Maximum Value:100Occurrence:Optional
offset | string | The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Default:0Occurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-ENDUSERCTX | string | This header is required to support revenue sharing for eBay Partner Network and to improve the accuracy of shipping and delivery time estimations.For additional information, refer toUse request headerssection of the Buying Integration Guide.Occurrence:Optional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the eBay marketplace.SeeHTTP request headersfor supported marketplace ID values.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
events | array ofEvent | A list of results that match the search criteria.Occurrence:Conditional
events.applicableCoupons | array ofCoupon | A list of coupons associated with the event.Occurrence:Conditional
events.applicableCoupons.redemptionCode | string | The coupon code.Occurrence:Conditional
events.applicableCoupons.terms | Terms | The terms of use associated with the coupon.Occurrence:Conditional
events.applicableCoupons.terms.fullText | string | A full-text description of the terms.Occurrence:Conditional
events.applicableCoupons.terms.summary | string | A summarized description of the terms.Occurrence:Conditional
events.description | string | The event description.Occurrence:Conditional
events.endDate | string | The end date for the event.Occurrence:Conditional
events.eventAffiliateWebUrl | string | The URL of the View Event page for the event, which includes the affiliate tracking ID.Occurrence:Conditional
events.eventId | string | The unique identifier for the event.Occurrence:Conditional
events.eventWebUrl | string | The web URL for the event.Occurrence:Conditional
events.images | array ofImage | The images for the event.Occurrence:Conditional
events.images.height | string | The height of the image.Occurrence:Conditional
events.images.imageUrl | string | The relative path to the image location.Occurrence:Conditional
events.images.text | string | The text associated with the image.Occurrence:Conditional
events.images.width | string | The width of the image.Occurrence:Conditional
events.startDate | string | The start date for the event.Occurrence:Conditional
events.terms | Terms | The terms associated with the event.Occurrence:Conditional
events.terms.fullText | string | A full-text description of the terms.Occurrence:Conditional
events.terms.summary | string | A summarized description of the terms.Occurrence:Conditional
events.title | string | The title of the event.Occurrence:Conditional
href | string | The relative path to the current set of results.Occurrence:Conditional
limit | integer | The maximum number of items, from the current result set, returned on a single page.Default:20Occurrence:Conditional
next | string | The relative path to the next set of results.Occurrence:Conditional
offset | integer | The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Default:0Occurrence:Conditional
prev | string | The relative path to the previous set of results.Occurrence:Conditional
total | integer | The total number of matches for the specified search criteria.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
403 | Forbidden
500 | Internal Server Error
[/TABLE]

[TABLE]
180000 | API_DEAL | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
180001 | API_DEAL | REQUEST | Invalid, missing or unsupported marketplace. Please refer to documentation.
180002 | API_DEAL | REQUEST | The specified limit is invalid. Maximum value supported is 100.
180003 | API_DEAL | REQUEST | The specified offset is invalid.
180009 | API_DEAL | REQUEST | Not authorized. Please contact developer support for assistance.
[/TABLE]