# commerce/notification/resources/subscription/methods/createSubscription

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/createSubscription*

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

### Sample 1: Create subscription

#### Thank you for helping us to improve the eBay developer program.
POST/subscription
This method allows applications to create a subscription for a topic and supported schema version. Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.Each application and topic-schema pairing to a subscription should have a 1:1 cardinality.You can create the subscription in disabled mode, test it (see thetestmethod), and when everything is ready, you can enable the subscription (see theenableSubscriptionmethod).Note:If an application is not authorized to subscribe to a topic, for example, if your authorization does not include the list of scopes required for the topic, an error code of 195011 is returned.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with eitherauthorization code grantflow orclient credentials grantflow. Please refer to the note below for more details.The access token must be created using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription
SeeOAuth access tokensfor more information.
Note:An OAuth token created with theclient credentials grant flowand thehttps://api.ebay.com/oauth/api_scopescope is required in order to create, update, or retrieveapplication-basedsubscriptions to notification topics. An OAuth token created with theauthorization code grant flowand thehttps://api.ebay.com/oauth/api_scope/commerce.notification.subscriptionscope is required in order to create, update, or retrieveuser-basedsubscriptions to notification topics.
The unique identifier of the destination endpoint that will receive notifications associated with this subscription. Use thegetDestinationsmethod to retrieve destination IDs.Occurrence:Required
The payload associated with the notification topic. UsegetTopicsorgetTopicto get the supported payload for the topic.Occurrence:Required
The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
Set the status of the subscription toENABLEDorDISABLED.Occurrence:Required
The unique identifier of the notification topic to subscribe to. UsegetTopicsto get topic IDs.Occurrence:Required
SeeHTTP response headersfor details.
This call has no payload.
This call has no field definitions.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call creates a subscription for an application.
The required inputs aretopicId,status,payload,payload(includingformat,schemaVersionanddeliveryProtocol) anddestinationId.
POSThttps://api.ebay.com/commerce/notification/v1/subscription
A successful call returns the HTTP status code201 Created. This method has no response payload.
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
destinationId | string | The unique identifier of the destination endpoint that will receive notifications associated with this subscription. Use thegetDestinationsmethod to retrieve destination IDs.Occurrence:Required
payload | SubscriptionPayloadDetail | The payload associated with the notification topic. UsegetTopicsorgetTopicto get the supported payload for the topic.Occurrence:Required
payload.deliveryProtocol | ProtocolEnum | The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
payload.format | FormatTypeEnum | The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
payload.schemaVersion | string | The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
status | SubscriptionStatusEnum | Set the status of the subscription toENABLEDorDISABLED.Occurrence:Required
topicId | string | The unique identifier of the notification topic to subscribe to. UsegetTopicsto get topic IDs.Occurrence:Required
[/TABLE]

[TABLE]
Location | The  subscription resource created.
[/TABLE]

[TABLE]
201 | Created
400 | Bad Request
403 | Forbidden
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195003 | API_NOTIFICATION | REQUEST | Please provide configurations required for notifications. Refer to /config
195006 | API_NOTIFICATION | REQUEST | Invalid or missing subscription status.
195007 | API_NOTIFICATION | REQUEST | Invalid or missing destination id.
195008 | API_NOTIFICATION | REQUEST | Invalid or missing schema version. Please refer to /topic/{topic_id} for supported schema versions.
195009 | API_NOTIFICATION | REQUEST | Specified format is not supported for the topic.
195010 | API_NOTIFICATION | REQUEST | Invalid or missing protocol
195011 | API_NOTIFICATION | REQUEST | Not authorized for this topic.
195012 | API_NOTIFICATION | REQUEST | Subscription already exists
195015 | API_NOTIFICATION | REQUEST | The subscription cannot be enabled since the destination is not enabled.
195027 | API_NOTIFICATION | REQUEST | Invalid or missing topic id.
[/TABLE]