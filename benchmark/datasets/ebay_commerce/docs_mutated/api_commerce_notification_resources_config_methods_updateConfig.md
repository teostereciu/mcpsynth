# commerce/notification/resources/config/methods/updateConfig

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/config/methods/updateConfig*

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

### Sample 1: Creates a new configuration or updates a previously created configuration

#### Thank you for helping us to improve the eBay developer program.
This method allows applications to create a new configuration or update an existing configuration. This app-level configuration allows developers to set up alerts.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This field is used to add or modify an email address that will be used for Notification API alerts associated with the application.getConfigcan be used to get the email address currently being used for alerts.Occurrence:Required
This call has no response headers.
This call has no payload.
This call has no field definitions.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample creates a new configuration.
The input ispublic_key_id.
PUThttps://api.ebay.com/commerce/notification/v1/config
A successful call returns the HTTP status code204 No content. This method has no response payload.
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
alertEmail | string | This field is used to add or modify an email address that will be used for Notification API alerts associated with the application.getConfigcan be used to get the email address currently being used for alerts.Occurrence:Required
[/TABLE]

[TABLE]
204 | No Content
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195025 | API_NOTIFICATION | REQUEST | Invalid or missing email.
[/TABLE]