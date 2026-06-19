# commerce/notification/resources/subscription/methods/testSubscription

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/testSubscription*

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

### Sample 1: Test a subscription

#### Thank you for helping us to improve the eBay developer program.
POST/subscription/{subscription_id}/test
This method triggers a mocked test payload that includes a notification ID, publish date, and so on. Use this method to test your subscription end-to-end.You can create the subscription in disabled mode, test it using this method, and when everything is ready, you can enable the subscription (see theenableSubscriptionmethod).Note:Use thenotificationIdto tell the difference between a test payload and a real payload.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
This request requires an access token created with eitherauthorization code grantflow orclient credentials grantflow. Please refer to the note below for more details.The access token must be created using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The unique identifier for the notification for this test message.Occurrence:Conditional
Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
Triggers a mocked test payload to the destination.
The only input is thesubscription_idas a path parameter.
POSThttps://api.ebay.com/commerce/notification/v1/subscription/{subscription_id}/test
A successful call returns the HTTP status code202 Acceptedand thenotificationId.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
subscription_id | string | The unique identifier of the subscription to test. UsegetSubscriptionsto retrieve subscription IDs.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
notificationId | string | The unique identifier for the notification for this test message.Occurrence:Conditional
[/TABLE]

[TABLE]
202 | Accepted
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195013 | API_NOTIFICATION | REQUEST | The subscription id does not exist.
[/TABLE]