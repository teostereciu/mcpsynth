# commerce/notification/resources/subscription/methods/getSubscriptionFilter

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/getSubscriptionFilter*

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

### Sample 1: Get Subscription Filter

#### Thank you for helping us to improve the eBay developer program.
GET/subscription/{subscription_id}/filter/{filter_id}
This method allows applications to retrieve the filter details for the specified subscription filter.Specify the subscription filter to retrieve by using thesubscription_idand thefilter_idassociated with the subscription filter. Thefilter_idcan be found in the response body for thegetSubscriptionmethod, if there is a filter applied on the subscription.Filters allow applications to only be sent notifications that match a provided criteria. Notifications that do not match this criteria will not be sent to the destination.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The creation date for this subscription filter.Occurrence:Conditional
Occurrence:Conditional
The unique identifier for this subscription filter.Occurrence:Conditional
The content of this subscription filter as a validJSON Schema Core document(version 2020-12 or later). ThefilterSchemaprovided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications.Occurrence:Conditional
The status of this subscription filter.Occurrence:Conditional
The unique identifier for the subscription.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call retrieves the filter details for a specified subscription filter.
This input specifies thesubscription_idand thefilter_id.
GEThttps://api.ebay.com/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}
If the call is successful, the details about the subscription filter are returned, such as thesubscriptionId,filterId,filterSchema,filterStatus, andcreationDate.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
subscription_id | string | The unique identifier of the subscription associated with the filter. UsegetSubscriptionsto retrieve subscription IDs.Occurrence:Required
filter_id | string | The unique identifier of the subscription filter.  Filter ID values, if configured for a subscription, will be shown in thesubscriptions.filterIdfield ingetSubscriptionandgetSubscriptionresponses. The filter ID value is also returned in the Location response header when a filter is created withcreateSubscriptionFilter.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
creationDate | string | The creation date for this subscription filter.Occurrence:Conditional
filterId | string | The unique identifier for this subscription filter.Occurrence:Conditional
filterSchema | object | The content of this subscription filter as a validJSON Schema Core document(version 2020-12 or later). ThefilterSchemaprovided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications.Occurrence:Conditional
filterStatus | SubscriptionFilterStatus | The status of this subscription filter.Occurrence:Conditional
subscriptionId | string | The unique identifier for the subscription.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195013 | API_NOTIFICATION | REQUEST | The subscription id does not exist.
195028 | API_NOTIFICATION | REQUEST | The application is not authorized to access the specified subscription.
195029 | API_NOTIFICATION | REQUEST | Invalid subscription filter id.
195031 | API_NOTIFICATION | REQUEST | The specified subscription id does not match the specified filter id.
[/TABLE]