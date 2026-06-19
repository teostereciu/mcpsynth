# commerce/notification/resources/destination/methods/updateDestination

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/updateDestination*

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

### Sample 1: Update a destination

#### Thank you for helping us to improve the eBay developer program.
PUT/destination/{destination_id}
This method allows applications to update a destination.Note:The destination should be created and ready to respond with the expectedchallengeResponsefor the endpoint to be registered successfully. Refer to theNotification API overviewfor more information.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This container is used to specify the destination endpoint and verification token associated with this endpoint.Occurrence:Required
The endpoint for this destination.Note:The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address orlocalhostin its path.Occurrence:Required
The verification token associated with this endpoint.Note:The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-); no other characters are allowed.Occurrence:Required
The seller-specified name for the destination endpoint.Occurrence:Optional
Occurrence:Optional
This field sets the status for the destination endpoint asENABLEDorDISABLED.Note:TheMARKED_DOWNvalue is set by eBay systems and cannot be used in a create or update call by applications.Occurrence:Required
This call has no response headers.
This call has no payload.
This call has no field definitions.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call updates a destination.
The inputs are the optionalname, and the requireddeliveryConfigincluding the endpointand theverificationToken
PUThttps://api.ebay.com/commerce/notification/v1/destination/{destination_id}
A successful call returns the HTTP status code204 No Content. This method has no response payload.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
destination_id | string | The unique identifier for the destination.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
deliveryConfig | DeliveryConfig | This container is used to specify the destination endpoint and verification token associated with this endpoint.Occurrence:Required
deliveryConfig.endpoint | string | The endpoint for this destination.Note:The provided endpoint URL should use the HTTPS protocol, and it should not contain an internal IP address orlocalhostin its path.Occurrence:Required
deliveryConfig.verificationToken | string | The verification token associated with this endpoint.Note:The provided verification token must be between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-); no other characters are allowed.Occurrence:Required
name | string | The seller-specified name for the destination endpoint.Occurrence:Optional
status | DestinationStatusEnum | This field sets the status for the destination endpoint asENABLEDorDISABLED.Note:TheMARKED_DOWNvalue is set by eBay systems and cannot be used in a create or update call by applications.Occurrence:Required
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
195016 | API_NOTIFICATION | REQUEST | Invalid name. Markups or lengths greater than 64 not supported
195017 | API_NOTIFICATION | REQUEST | Invalid or missing endpoint.
195018 | API_NOTIFICATION | REQUEST | Invalid or missing destination status. Supported values:[ENABLED,DISABLED]
195019 | API_NOTIFICATION | REQUEST | Invalid or missing verification token for this endpoint.
195020 | API_NOTIFICATION | REQUEST | Challenge verification failed for requested endpoint
195021 | API_NOTIFICATION | REQUEST | Destination exists for this endpoint
195022 | API_NOTIFICATION | REQUEST | Invalid or missing destination id.
[/TABLE]