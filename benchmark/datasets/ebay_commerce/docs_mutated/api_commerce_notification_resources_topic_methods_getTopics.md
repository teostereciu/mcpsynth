# commerce/notification/resources/topic/methods/getTopics

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/topic/methods/getTopics*

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

### Sample 1: Get topics

#### Thank you for helping us to improve the eBay developer program.
This method returns a paginated collection of all supported topics, along with the details for the topics. This information includes supported schema versions, formats, and other metadata for the topics.Applications can subscribe to any of the topics for a supported schema version and format, limited by the authorization scopes required to subscribe to the topic.A topic specifies the type of information to be received and the data types associated with an event. An event occurs in the eBay system, such as when a user requests deletion or revokes access for an application. An event is an instance of an event type (topic).
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The path to the call URI that produced the current page of results.Occurrence:Always
Occurrence:Always
The value of the page_size parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.Note:Though this parameter is not required to be submitted in the request, the parameter defaults to20if omitted.Occurrence:Always
The URL to access the next set of results. This field includes acontinuation_token. Noprevfield is returned, but this value is persistent during the session so that you can use it to return to the next page.This field is not returned if fewer records than specified by thelimitfield are returned.Occurrence:Conditional
Occurrence:Conditional
An array of topics that match the specified criteria.Occurrence:Conditional
The authorization scopes required to subscribe to this topic.Occurrence:Conditional
The business context associated with this topic.Occurrence:Always
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
The total number of matches for the search criteria.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This method allows applications to browse the details and status of supported topics.
The input specifies the optionallimitandcontinuation_tokenquery parameters. Since no page_size is specified in this request, the default value of20is used.
GEThttps://api.ebay.com/commerce/notification/v1/topic
If the call is successful, the results including the following fields are returned:topicId,description,status,context,scope,supportedPayloads(includingformat,schemaVersion,deliveryProtocol, anddeprecated), andfilterable.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
page_size | string | The maximum number of notification topics to return per page from the result set.Min:10Max:100Default:20Occurrence:Optional
continuation_token | string | This string value can be used to return the next page in the result set. The string to use here is returned in thenextfield of the current page of results.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
href | string | The path to the call URI that produced the current page of results.Occurrence:Always
page_size | integer | The value of the page_size parameter submitted in the request, which is the maximum number of items to return per page, from the result set. A result set is the complete set of results returned by the method.Note:Though this parameter is not required to be submitted in the request, the parameter defaults to20if omitted.Occurrence:Always
next | string | The URL to access the next set of results. This field includes acontinuation_token. Noprevfield is returned, but this value is persistent during the session so that you can use it to return to the next page.This field is not returned if fewer records than specified by thelimitfield are returned.Occurrence:Conditional
topics | array ofTopic | An array of topics that match the specified criteria.Occurrence:Conditional
topics.authorizationScopes | array ofstring | The authorization scopes required to subscribe to this topic.Occurrence:Conditional
topics.context | ContextEnum | The business context associated with this topic.Occurrence:Always
topics.description | string | The description of the topic.Occurrence:Always
topics.filterable | boolean | The indicator of whether this topic is filterable or not.Occurrence:Always
topics.scope | ScopeEnum | The scope of this topic.Occurrence:Always
topics.status | StatusEnum | The status of this topic.Occurrence:Always
topics.supportedPayloads | array ofPayloadDetail | The supported payloads for this topic.Occurrence:Conditional
topics.supportedPayloads.deliveryProtocol | ProtocolEnum | The supported delivery protocols.Occurrence:Always
topics.supportedPayloads.deprecated | boolean | A deprecation indicator.Occurrence:Always
topics.supportedPayloads.format | array ofFormatTypeEnum | The supported format. Presently,JSONis the only supported format.Occurrence:Always
topics.supportedPayloads.schemaVersion | string | The supported schema version.Occurrence:Conditional
topics.topicId | string | The unique identifier for the topic.Occurrence:Always
total | integer | The total number of matches for the search criteria.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195004 | API_NOTIFICATION | REQUEST | Invalid page_size. Supported ranges 10 - 100.
195005 | API_NOTIFICATION | REQUEST | Invalid continuation token.
[/TABLE]