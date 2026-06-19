# commerce/notification/resources/subscription/methods/getSubscription

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/getSubscription*

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

### Sample 1: Get subscription

#### Thank you for helping us to improve the eBay developer program.
GET/subscription/{subscription_id}
This method allows applications to retrieve subscription details for the specified subscription.Specify the subscription to retrieve using thesubscription_id. Use thegetSubscriptionsmethod to browse all subscriptions if you do not know thesubscription_id.Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with eitherauthorization code grantflow orclient credentials grantflow. Please refer to the note below for more details.The access token must be created using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly
SeeOAuth access tokensfor more information.
Note:An OAuth token created with theclient credentials grant flowand thehttps://api.ebay.com/oauth/api_scopescope is required in order to create, update, or retrieveapplication-basedsubscriptions to notification topics. An OAuth token created with theauthorization code grant flowand thehttps://api.ebay.com/oauth/api_scope/commerce.notification.subscriptionscope is required in order to create, update, or retrieveuser-basedsubscriptions to notification topics.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The creation date for this subscription.Occurrence:Conditional
Occurrence:Conditional
The unique identifier for the destination associated with this subscription.Occurrence:Conditional
The unique identifier for the filter associated with this subscription.Occurrence:Conditional
The payload associated with this subscription.Occurrence:Conditional
The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
The status of this subscription.Occurrence:Conditional
The unique identifier for the subscription.Occurrence:Conditional
The unique identifier for the topic associated with this subscription.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This method allows applications or users to retrieve subscription details and status for the specified subscription (and application).
Ths input specifies thesubscription_id.
GEThttps://api.ebay.com/commerce/notification/v1/subscription/{subscription_id}
The output is a subscription and its details such as thesubscriptionId,topicId,status,creationDate,payload,destinationId, andfilterId.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
subscription_id | string | The unique identifier of the subscription to retrieve. UsegetSubscriptionsto retrieve subscription IDs.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
creationDate | string | The creation date for this subscription.Occurrence:Conditional
destinationId | string | The unique identifier for the destination associated with this subscription.Occurrence:Conditional
filterId | string | The unique identifier for the filter associated with this subscription.Occurrence:Conditional
payload | SubscriptionPayloadDetail | The payload associated with this subscription.Occurrence:Conditional
payload.deliveryProtocol | ProtocolEnum | The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
payload.format | FormatTypeEnum | The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
payload.schemaVersion | string | The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
status | SubscriptionStatusEnum | The status of this subscription.Occurrence:Conditional
subscriptionId | string | The unique identifier for the subscription.Occurrence:Conditional
topicId | string | The unique identifier for the topic associated with this subscription.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195013 | API_NOTIFICATION | REQUEST | The subscription id does not exist.
[/TABLE]