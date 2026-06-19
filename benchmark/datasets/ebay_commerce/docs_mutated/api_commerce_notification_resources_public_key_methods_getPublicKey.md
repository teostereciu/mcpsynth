# commerce/notification/resources/public_key/methods/getPublicKey

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/public_key/methods/getPublicKey*

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

### Sample 1: Retrieve a Public Key

#### Thank you for helping us to improve the eBay developer program.
GET/public_key/{public_key_id}
This method allows users to retrieve a public key using a specified key ID. The public key that is returned in the response payload is used to process and validate eBay notifications.The public key ID, which is a required request parameter for this method, is retrieved from the Base64-encodedX-EBAY-SIGNATUREheader that is included in the eBay notification.Important!The retrieved public key value should be cached for a temporary — but reasonable — amount of time (e.g., one-hour is recommended.) This key should not be requested for every notification since doing so can result in exceedingAPI call limitsif a large number of notification requests is received.Note:For more details about how to process eBay push notifications and validate notification message payloads, see theNotification API overview.
Important!The retrieved public key value should be cached for a temporary — but reasonable — amount of time (e.g., one-hour is recommended.) This key should not be requested for every notification since doing so can result in exceedingAPI call limitsif a large number of notification requests is received.
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
The algorithm associated with the public key that is returned, such as Elliptic Curve Digital Signature Algorithm (ECDSA).Occurrence:Always
Occurrence:Always
The digest associated with the public key that is returned, such as Secure Hash Algorithm 1 (SHA1).Occurrence:Always
The public key that is returned for the specified key ID.This value is used to validate the eBay push notification message payload.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves a public key using a specified key ID.
The input ispublic_key_id.
GEThttps://api.ebay.com/commerce/notification/v1/public_key/9936261a-7d7b-4621-a0f1-96ccb428af49
If the call is successful, the public key is returned for the specified key ID.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
public_key_id | string | The unique key ID that is used to retrieve the public key.Note:This is retrieved from theX-EBAY-SIGNATUREheader that is included with the push notification.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
algorithm | string | The algorithm associated with the public key that is returned, such as Elliptic Curve Digital Signature Algorithm (ECDSA).Occurrence:Always
digest | string | The digest associated with the public key that is returned, such as Secure Hash Algorithm 1 (SHA1).Occurrence:Always
key | string | The public key that is returned for the specified key ID.This value is used to validate the eBay push notification message payload.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195001 | API_NOTIFICATION | REQUEST | The specified key id is invalid.
[/TABLE]