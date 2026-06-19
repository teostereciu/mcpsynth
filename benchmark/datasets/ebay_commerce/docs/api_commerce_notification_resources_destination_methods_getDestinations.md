# commerce/notification/resources/destination/methods/getDestinations

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/getDestinations*

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

### Sample 1: Browse the details and status of previously created destination details

#### Thank you for helping us to improve the eBay developer program.
GET/destination
This method allows applications to retrieve a paginated collection of destination resources and related details. The details include the destination names, statuses, and configurations, including the endpoints and verification tokens.
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
An array that contains the destination details.Occurrence:Conditional
Occurrence:Conditional
The configuration associated with this destination.Occurrence:Always
Occurrence:Always
The endpoint for this destination.Note:The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address orlocalhostin its path.Occurrence:Always
The verification token associated with this endpoint.Note:The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-); no other characters are allowed.Occurrence:Always
The unique identifier for the destination.Occurrence:Always
The name associated with this destination.Occurrence:Conditional
The status for this destination.Note:TheMARKED_DOWNvalue is set by eBay systems and cannot be used in a create or update call by applications.Valid values:ENABLEDDISABLEDMARKED_DOWNOccurrence:Always
The path to the call URI that produced the current page of results.Occurrence:Always
The number of records to show in the current response.Default:20Occurrence:Conditional
The URL to access the next set of results. This field includes acontinuation_token. Noprevfield is returned, but this value is persistent during the session so that you can use it to return to the next page.This field is not returned if fewer records than specified by thelimitfield are returned.Occurrence:Conditional
The total number of matches for the search criteria.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call retrieves the group of previously created destination details.
There are no required inputs.
GEThttps://api.ebay.com/commerce/notification/v1/destination
A successful call returns a list of the previously created destinations.
Related topics
If you need help, contactDeveloper Technical Support.
- ENABLED
- DISABLED
- MARKED_DOWN
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
limit | string | The maximum number of destinations to return per page from the result set.Min:10Max:100Default:20Occurrence:Optional
continuation_token | string | This string value can be used to return the next page in the result set. The string to use here is returned in thenextfield of the current page of results.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
destinations | array ofDestination | An array that contains the destination details.Occurrence:Conditional
destinations.deliveryConfig | DeliveryConfig | The configuration associated with this destination.Occurrence:Always
destinations.deliveryConfig.endpoint | string | The endpoint for this destination.Note:The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address orlocalhostin its path.Occurrence:Always
destinations.deliveryConfig.verificationToken | string | The verification token associated with this endpoint.Note:The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-); no other characters are allowed.Occurrence:Always
destinations.destinationId | string | The unique identifier for the destination.Occurrence:Always
destinations.name | string | The name associated with this destination.Occurrence:Conditional
destinations.status | DestinationStatusEnum | The status for this destination.Note:TheMARKED_DOWNvalue is set by eBay systems and cannot be used in a create or update call by applications.Valid values:ENABLEDDISABLEDMARKED_DOWNOccurrence:Always
href | string | The path to the call URI that produced the current page of results.Occurrence:Always
limit | integer | The number of records to show in the current response.Default:20Occurrence:Conditional
next | string | The URL to access the next set of results. This field includes acontinuation_token. Noprevfield is returned, but this value is persistent during the session so that you can use it to return to the next page.This field is not returned if fewer records than specified by thelimitfield are returned.Occurrence:Conditional
total | integer | The total number of matches for the search criteria.Occurrence:Conditional
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