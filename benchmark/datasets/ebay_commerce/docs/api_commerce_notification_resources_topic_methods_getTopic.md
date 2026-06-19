# commerce/notification/resources/topic/methods/getTopic

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/topic/methods/getTopic*

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

### Sample 1: Get topic

#### Thank you for helping us to improve the eBay developer program.
GET/topic/{topic_id}
This method allows applications to retrieve details for the specified topic. This information includes supported schema versions, formats, and other metadata for the topic.Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).Specify the topic to retrieve using thetopic_idURI parameter.Note:Use thegetTopicsmethod to find a topic if you do not know the topic ID.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The authorization scopes required to subscribe to this topic.Occurrence:Conditional
Occurrence:Conditional
The business context associated with this topic.Occurrence:Always
Occurrence:Always
The description of the topic.Occurrence:Always
The indicator of whether this topic is filterable or not.Occurrence:Always
The scope of this topic.Occurrence:Always
The status of this topic.Occurrence:Always
The supported payloads for this topic.Occurrence:Conditional
The supported delivery protocols.Occurrence:Always
A deprecation indicator.Occurrence:Always
The supported format. Presently,JSONis the only supported format.Occurrence:Always
The supported schema version.Occurrence:Conditional
The unique identifier for the topic.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This method retrieves the topic resource which includes meta information for the topic.
The input is thetopic_id.
GEThttps://api.ebay.com/commerce/notification/v1/topic/{topic_id}
If the call is successful, the results including the following fields are returned:topicId,description,status,context,scope,supportedPayloads(includingformat,schemaVersion,deliveryProtocol, anddeprecated), andfilterable.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
topic_id | string | The unique identifier of the notification topic for which the details are retrieved. UsegetTopicsto retrieve the topic ID.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
authorizationScopes | array ofstring | The authorization scopes required to subscribe to this topic.Occurrence:Conditional
context | ContextEnum | The business context associated with this topic.Occurrence:Always
description | string | The description of the topic.Occurrence:Always
filterable | boolean | The indicator of whether this topic is filterable or not.Occurrence:Always
scope | ScopeEnum | The scope of this topic.Occurrence:Always
status | StatusEnum | The status of this topic.Occurrence:Always
supportedPayloads | array ofPayloadDetail | The supported payloads for this topic.Occurrence:Conditional
supportedPayloads.deliveryProtocol | ProtocolEnum | The supported delivery protocols.Occurrence:Always
supportedPayloads.deprecated | boolean | A deprecation indicator.Occurrence:Always
supportedPayloads.format | array ofFormatTypeEnum | The supported format. Presently,JSONis the only supported format.Occurrence:Always
supportedPayloads.schemaVersion | string | The supported schema version.Occurrence:Conditional
topicId | string | The unique identifier for the topic.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195002 | API_NOTIFICATION | REQUEST | Invalid or missing topic id.
[/TABLE]