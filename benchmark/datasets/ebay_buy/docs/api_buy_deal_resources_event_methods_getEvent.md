# buy/deal/resources/event/methods/getEvent

*Source: https://developer.ebay.com/api-docs/buy/deal/resources/event/methods/getEvent*

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

### Sample 1: Retrieve Event Details

#### Thank you for helping us to improve the eBay developer program.
GET/event/{event_id}
This method retrieves the details for an eBay event. The result set contains detailed information associated with the specified event ID, such as applicable coupons, start and end dates, and event terms.RestrictionsThis method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, seeAPI Restrictions.eBay Partner Network:In order to receive a commission for your sales, you must use the URL returned in theitemAffiliateWebUrlfield to forward your buyer to the ebay.com site.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Optional
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.deal
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
A list of coupons associated with the event.Occurrence:Conditional
Occurrence:Conditional
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
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the details associated with the specified event ID.
The input is theevent_idURI parameter. There is no payload with this request.
GEThttps://api.ebay.com/buy/deal/v1/event/5**********2
If the call is successful, the details associated with the specified event will be returned.
Related topics
If you need help, contactDeveloper Technical Support.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
event_id | string | This path parameters specifies the unique identifier for the eBay event being retrieved.Use thegetEventsmethod to retrieve event IDs.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-ENDUSERCTX | string | This header is required to support revenue sharing for eBay Partner Network and to improve the accuracy of shipping and delivery time estimations.For additional information, refer toUse request headerssection of the Buying Integration Guide.Occurrence:Optional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the eBay marketplace.SeeHTTP request headersfor supported marketplace ID values.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
applicableCoupons | array ofCoupon | A list of coupons associated with the event.Occurrence:Conditional
applicableCoupons.redemptionCode | string | The coupon code.Occurrence:Conditional
applicableCoupons.terms | Terms | The terms of use associated with the coupon.Occurrence:Conditional
applicableCoupons.terms.fullText | string | A full-text description of the terms.Occurrence:Conditional
applicableCoupons.terms.summary | string | A summarized description of the terms.Occurrence:Conditional
description | string | The event description.Occurrence:Conditional
endDate | string | The end date for the event.Occurrence:Conditional
eventAffiliateWebUrl | string | The URL of the View Event page for the event, which includes the affiliate tracking ID.Occurrence:Conditional
eventId | string | The unique identifier for the event.Occurrence:Conditional
eventWebUrl | string | The web URL for the event.Occurrence:Conditional
images | array ofImage | The images for the event.Occurrence:Conditional
images.height | string | The height of the image.Occurrence:Conditional
images.imageUrl | string | The relative path to the image location.Occurrence:Conditional
images.text | string | The text associated with the image.Occurrence:Conditional
images.width | string | The width of the image.Occurrence:Conditional
startDate | string | The start date for the event.Occurrence:Conditional
terms | Terms | The terms associated with the event.Occurrence:Conditional
terms.fullText | string | A full-text description of the terms.Occurrence:Conditional
terms.summary | string | A summarized description of the terms.Occurrence:Conditional
title | string | The title of the event.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
180000 | API_DEAL | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
180004 | API_DEAL | REQUEST | The event Id is invalid for the requested marketplace.
180009 | API_DEAL | REQUEST | Not authorized. Please contact developer support for assistance.
[/TABLE]