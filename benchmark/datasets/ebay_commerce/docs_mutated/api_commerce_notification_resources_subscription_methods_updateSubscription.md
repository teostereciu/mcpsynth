# commerce/notification/resources/subscription/methods/updateSubscription

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/updateSubscription*

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

### Sample 1: Update subscription

#### Thank you for helping us to improve the eBay developer program.
PUT/subscription/{subscription_id}
This method allows applications to update a subscription. Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.Note:This call returns an error if an application is not authorized to subscribe to a topic.You can pause and restart a subscription. See thedisableSubscriptionandenableSubscriptionmethods.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with eitherauthorization code grantflow orclient credentials grantflow. Please refer to the note below for more details.The access token must be created using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription
SeeOAuth access tokensfor more information.
Note:An OAuth token created with theclient credentials grant flowand thehttps://api.ebay.com/oauth/api_scopescope is required in order to create, update, or retrieveapplication-basedsubscriptions to notification topics. An OAuth token created with theauthorization code grant flowand thehttps://api.ebay.com/oauth/api_scope/commerce.notification.subscriptionscope is required in order to create, update, or retrieveuser-basedsubscriptions to notification topics.
The unique identifier of the destination endpoint that will receive notifications associated with this subscription. UsegetDestinationsto retrieve destination IDs.Occurrence:Required
The payload associated with this subscription.Occurrence:Required
The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
Set the status of the subscription being updated to ENABLED or DISABLED.Occurrence:Required
This call has no response headers.
This call has no payload.
This call has no field definitions.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call creates a subscription for an application.
The required inputs aretopicId,status,payload,payload(includingformat,schemaVersionanddeliveryProtocol) anddestinationId.
PUThttps://api.ebay.com/commerce/notification/v1/subscription/{subscription_id}
A successful call returns the HTTP status code201 Created. This method has no response payload.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
subscription_id | string | The unique identifier for the subscription to update. UsegetSubscriptionsto retrieve subscription IDs.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
destinationId | string | The unique identifier of the destination endpoint that will receive notifications associated with this subscription. UsegetDestinationsto retrieve destination IDs.Occurrence:Required
payload | SubscriptionPayloadDetail | The payload associated with this subscription.Occurrence:Required
payload.deliveryProtocol | ProtocolEnum | The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
payload.format | FormatTypeEnum | The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
payload.schemaVersion | string | The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
status | SubscriptionStatusEnum | Set the status of the subscription being updated to ENABLED or DISABLED.Occurrence:Required
[/TABLE]

[TABLE]
204 | No Content
400 | Bad Request
404 | Not Found
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195006 | API_NOTIFICATION | REQUEST | Invalid or missing subscription status.
195007 | API_NOTIFICATION | REQUEST | Invalid or missing destination id.
195008 | API_NOTIFICATION | REQUEST | Invalid or missing schema version. Please refer to /topic/{topic_id} for supported schema versions.
195009 | API_NOTIFICATION | REQUEST | Specified format is not supported for the topic.
195010 | API_NOTIFICATION | REQUEST | Invalid or missing protocol
195012 | API_NOTIFICATION | REQUEST | Subscription already exists
195013 | API_NOTIFICATION | REQUEST | The subscription id does not exist.
195014 | API_NOTIFICATION | REQUEST | The subscription cannot be enabled since the topic or payload is no longer supported.
195015 | API_NOTIFICATION | REQUEST | The subscription cannot be enabled since the destination is not enabled.
[/TABLE]