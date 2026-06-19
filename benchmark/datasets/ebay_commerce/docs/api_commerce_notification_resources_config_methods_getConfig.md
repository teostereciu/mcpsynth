# commerce/notification/resources/config/methods/getConfig

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/config/methods/getConfig*

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

### Sample 1: Retrieves a previously created configuration

#### Thank you for helping us to improve the eBay developer program.
This method allows applications to retrieve a previously created configuration.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
This field is used to add or modify an email address that will be used for Notification API alerts associated with the application.getConfigcan be used to get the email address currently being used for alerts.Occurrence:Required
Occurrence:Required
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves a previously created configuration.
There are no inputs for this sample.
GEThttps://api.ebay.com/commerce/notification/v1/config
If the call is successful, the configured alert email address is returned.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Output container/field | Type | Description
alertEmail | string | This field is used to add or modify an email address that will be used for Notification API alerts associated with the application.getConfigcan be used to get the email address currently being used for alerts.Occurrence:Required
[/TABLE]

[TABLE]
200 | OK
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195026 | API_NOTIFICATION | APPLICATION | Configuration Not Found.
[/TABLE]