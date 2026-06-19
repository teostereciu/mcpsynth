# commerce/notification/resources/destination/methods/deleteDestination

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/destination/methods/deleteDestination*

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

### Sample 1: Delete a destination

#### Thank you for helping us to improve the eBay developer program.
DELETE/destination/{destination_id}
This method provides applications a way to delete a destination.The same destination ID can be used by many destinations.Trying to delete an active destination results in an error. You can disable a subscription, and when the destination is no longer in use, you can delete it.
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
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call deletes the specified destination.
The only input is thedestination_idas a path parameter.
DELETEhttps://api.ebay.com/commerce/notification/v1/destination/{destination_id}
A successful call returns the HTTP status code204 No content. This method has no response payload.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
destination_id | string | The unique identifier of the destination to delete. Only disabled or marked down destinations can be deleted, and enabled destinations cannot be deleted. UsegetDestinationorgetDestinationsto see the current status of a destination.Occurrence:Required
[/TABLE]

[TABLE]
204 | No Content
404 | Not Found
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195022 | API_NOTIFICATION | REQUEST | Invalid or missing destination id.
195024 | API_NOTIFICATION | REQUEST | Destination is in use and cannot be deleted.
[/TABLE]