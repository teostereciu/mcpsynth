# commerce/notification/resources/destination/methods/getDestination

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/getDestination*

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

### Sample 1: Get destinations

#### Thank you for helping us to improve the eBay developer program.
GET/destination/{destination_id}
This method allows applications to fetch the details for a destination. The details include the destination name, status, and configuration, including the endpoint and verification token.
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
The configuration associated with this destination.Occurrence:Always
Occurrence:Always
The endpoint for this destination.Note:The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address orlocalhostin its path.Occurrence:Always
The verification token associated with this endpoint.Note:The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-); no other characters are allowed.Occurrence:Always
The unique identifier for the destination.Occurrence:Always
The name associated with this destination.Occurrence:Conditional
Occurrence:Conditional
The status for this destination.Note:TheMARKED_DOWNvalue is set by eBay systems and cannot be used in a create or update call by applications.Valid values:ENABLEDDISABLEDMARKED_DOWNOccurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call retrieves the details and status of the specified destination.
The input isdestination_id.
GEThttps://api.ebay.com/commerce/notification/v1/destination/{destination_id}
If the call is successful, thedestinationId,name,status, anddeliveryConfigare returned.
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
destination_id | string | The unique identifier of the destination to retrieve. UsegetDestinationsto retrieve destination IDs.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
deliveryConfig | DeliveryConfig | The configuration associated with this destination.Occurrence:Always
deliveryConfig.endpoint | string | The endpoint for this destination.Note:The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address orlocalhostin its path.Occurrence:Always
deliveryConfig.verificationToken | string | The verification token associated with this endpoint.Note:The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-); no other characters are allowed.Occurrence:Always
destinationId | string | The unique identifier for the destination.Occurrence:Always
name | string | The name associated with this destination.Occurrence:Conditional
status | DestinationStatusEnum | The status for this destination.Note:TheMARKED_DOWNvalue is set by eBay systems and cannot be used in a create or update call by applications.Valid values:ENABLEDDISABLEDMARKED_DOWNOccurrence:Always
[/TABLE]

[TABLE]
200 | OK
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195022 | API_NOTIFICATION | REQUEST | Invalid or missing destination id.
[/TABLE]