# commerce/notification/resources/subscription/methods/getSubscriptions

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/getSubscriptions*

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

### Sample 1: Get subscriptions

#### Thank you for helping us to improve the eBay developer program.
GET/subscription
This method allows applications to retrieve a list of all subscriptions. The list returned is a paginated collection of subscription resources.Subscriptions allow applications to express interest in notifications and keep receiving the information relevant to their business.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Optional
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
The path to the call URI that produced the current page of results.Occurrence:Always
Occurrence:Always
The value of the limit parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.Note:Though this parameter is not required to be submitted in the request, the parameter defaults to20if omitted.Default:20Occurrence:Always
The URL to access the next set of results. This field includes acontinuation_token. Noprevfield is returned, but this value is persistent during the session so that you can use it to return to the next page.This field is not returned if fewer records than specified by thelimitfield are returned.Occurrence:Conditional
Occurrence:Conditional
The subscriptions that match the search criteria.Occurrence:Conditional
The creation date for this subscription.Occurrence:Conditional
The unique identifier for the destination associated with this subscription.Occurrence:Conditional
The unique identifier for the filter associated with this subscription.Occurrence:Conditional
The payload associated with this subscription.Occurrence:Conditional
The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
Occurrence:Required
The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
The status of this subscription.Occurrence:Conditional
The unique identifier for the subscription.Occurrence:Conditional
The unique identifier for the topic associated with this subscription.Occurrence:Conditional
The total number of matches for the search criteria.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This method retrieves an array containing the details and status of all subscriptions limited by the authorization scope.
The input specifies the optionallimitandcontinuation_tokenquery parameters. Since no limit is specified in this request, the default value of20is used.
GEThttps://api.ebay.com/commerce/notification/v1/subscription
The output is an array of subscriptions and their details such as thesubscriptionId,topicId,status,creationDate,payload, anddestinationId.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
limit | string | The maximum number of subscriptions to return per page from the result set.Min:10Max:100Default:20Occurrence:Optional
continuation_token | string | This string value can be used to return the next page in the result set. The string to use here is returned in the next field of the current page of results.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
href | string | The path to the call URI that produced the current page of results.Occurrence:Always
limit | integer | The value of the limit parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.Note:Though this parameter is not required to be submitted in the request, the parameter defaults to20if omitted.Default:20Occurrence:Always
next | string | The URL to access the next set of results. This field includes acontinuation_token. Noprevfield is returned, but this value is persistent during the session so that you can use it to return to the next page.This field is not returned if fewer records than specified by thelimitfield are returned.Occurrence:Conditional
subscriptions | array ofSubscription | The subscriptions that match the search criteria.Occurrence:Conditional
subscriptions.creationDate | string | The creation date for this subscription.Occurrence:Conditional
subscriptions.destinationId | string | The unique identifier for the destination associated with this subscription.Occurrence:Conditional
subscriptions.filterId | string | The unique identifier for the filter associated with this subscription.Occurrence:Conditional
subscriptions.payload | SubscriptionPayloadDetail | The payload associated with this subscription.Occurrence:Conditional
subscriptions.payload.deliveryProtocol | ProtocolEnum | The supported delivery protocol of the notification topic.Note:HTTPSis currently the only supported delivery protocol of all notification topics.Occurrence:Required
subscriptions.payload.format | FormatTypeEnum | The supported data format of the payload.Note:JSON is currently the only supported format for all notification topics.Occurrence:Required
subscriptions.payload.schemaVersion | string | The supported schema version for the notification topic. See thesupportedPayloads.schemaVersionfield for the topic ingetTopicsorgetTopicresponse.Occurrence:Required
subscriptions.status | SubscriptionStatusEnum | The status of this subscription.Occurrence:Conditional
subscriptions.subscriptionId | string | The unique identifier for the subscription.Occurrence:Conditional
subscriptions.topicId | string | The unique identifier for the topic associated with this subscription.Occurrence:Conditional
total | integer | The total number of matches for the search criteria.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195004 | API_NOTIFICATION | REQUEST | Invalid limit. Supported ranges 10 - 100.
195005 | API_NOTIFICATION | REQUEST | Invalid continuation token.
[/TABLE]