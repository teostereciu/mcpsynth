# commerce/notification/resources/subscription/methods/deleteSubscriptionFilter

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/deleteSubscriptionFilter*

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

### Sample 1: Disables a Subscription Filter

#### Thank you for helping us to improve the eBay developer program.
DELETE/subscription/{subscription_id}/filter/{filter_id}
This method allows applications to disable the active filter on a subscription, so that a new subscription filter may be added.Note:Subscription filters inPENDINGstatus can not be disabled. However, a new filter can be created instead with thecreateSubscriptionFiltermethod and this new filter will override thePENDINGfilter.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription
SeeOAuth access tokensfor more information.
Note:An OAuth token created with theclient credentials grant flowand thehttps://api.ebay.com/oauth/api_scopescope is required in order to create, update, or retrieveapplication-basedsubscriptions to notification topics. An OAuth token created with theauthorization code grant flowand thehttps://api.ebay.com/oauth/api_scope/commerce.notification.subscriptionscope is required in order to create, update, or retrieveuser-basedsubscriptions to notification topics.
This call has no payload.
This call has no field definitions.
This call has no response headers.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This method allows applications to disable a subscription filter.
This input specifies thesubscription_idand thefilter_id.
DELETEhttps://api.ebay.com/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}
A successful call returns the HTTP status code204 No content. This method has no response payload.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
subscription_id | string | The unique identifier of the subscription associated with the filter to delete. UsegetSubscriptionsto retrieve subscription IDs.Occurrence:Required
filter_id | string | The unique identifier of the subscription filter to delete.  Filter ID values, if configured for a subscription, will be shown in thesubscriptions.filterIdfield ingetSubscriptionandgetSubscriptionresponses. The filter ID value is also returned in the Location response header when a filter is created withcreateSubscriptionFilter.Occurrence:Required
[/TABLE]

[TABLE]
204 | No Content
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195013 | API_NOTIFICATION | REQUEST | The subscription id does not exist.
195028 | API_NOTIFICATION | REQUEST | The application is not authorized to access the specified subscription.
195029 | API_NOTIFICATION | REQUEST | Invalid subscription filter id.
195030 | API_NOTIFICATION | REQUEST | The specified filter is either disabled or pending and cannot be deleted at this time. Only enabled filters may be deleted.
195031 | API_NOTIFICATION | REQUEST | The specified subscription id does not match the specified filter id.
[/TABLE]