# commerce/charity/resources/charity_org/methods/getCharityOrg

*Source: https://developer.ebay.com/api-docs/commerce/charity/resources/charity_org/methods/getCharityOrg*

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

### Sample 1: Retrieve Charitable Organization Details

#### Thank you for helping us to improve the eBay developer program.
GET/charity_org/{charity_org_id}
This call is used to retrieve detailed information about supported charitable organizations. It allows users to retrieve the details for a specific charitable organization using its charity organization ID.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The ID of the charitable organization.Occurrence:Always
Occurrence:Always
The description of the charitable organization.Occurrence:Conditional
Occurrence:Conditional
The location details of the charitable organization.Occurrence:Conditional
The address of the charitable organization.Occurrence:Conditional
The city of the charitable organization.Occurrence:Conditional
The state or province of the charitable organization.Occurrence:Conditional
The postal code of the charitable organization.Occurrence:Conditional
The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
The geo-coordinates of the charitable organization.Occurrence:Conditional
The latitude component of the geographic coordinate.Occurrence:Conditional
The longitude component of the geographic coordinate.Occurrence:Conditional
The logo of the charitable organization.Occurrence:Conditional
The height of the logo image.Occurrence:Conditional
The URL to the logo image location.Occurrence:Conditional
The width of the logo image.Occurrence:Conditional
The mission statement of the charitable organization.Occurrence:Conditional
The name of the charitable organization.Occurrence:Always
The registration ID for the charitable organization.Note:For the US marketplace, this is the EIN.Occurrence:Conditional
The link to the website for the charitable organization.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves detailed information for a supported charitable organization based on its charity ID.
The input is thecharity_org_idURI parameter. There is no payload with this request.
GEThttps://api.ebay.com/commerce/charity/v1/charity_org/302
If the call is successful, the charitable organization details for the specified charity ID are returned.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
charity_org_id | string | The unique ID of the charitable organization.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-MARKETPLACE-ID | string | A header used to specify the eBay marketplace ID.Valid Values:EBAY_GBandEBAY_USOccurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
charityOrgId | string | The ID of the charitable organization.Occurrence:Always
description | string | The description of the charitable organization.Occurrence:Conditional
location | Location | The location details of the charitable organization.Occurrence:Conditional
location.address | Address | The address of the charitable organization.Occurrence:Conditional
location.address.city | string | The city of the charitable organization.Occurrence:Conditional
location.address.stateOrProvince | string | The state or province of the charitable organization.Occurrence:Conditional
location.address.postalCode | string | The postal code of the charitable organization.Occurrence:Conditional
location.address.country | CountryCodeEnum | The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
location.geoCoordinates | GeoCoordinates | The geo-coordinates of the charitable organization.Occurrence:Conditional
location.geoCoordinates.latitude | number | The latitude component of the geographic coordinate.Occurrence:Conditional
location.geoCoordinates.longitude | number | The longitude component of the geographic coordinate.Occurrence:Conditional
logoImage | Image | The logo of the charitable organization.Occurrence:Conditional
logoImage.height | string | The height of the logo image.Occurrence:Conditional
logoImage.imageUrl | string | The URL to the logo image location.Occurrence:Conditional
logoImage.width | string | The width of the logo image.Occurrence:Conditional
missionStatement | string | The mission statement of the charitable organization.Occurrence:Conditional
name | string | The name of the charitable organization.Occurrence:Always
registrationId | string | The registration ID for the charitable organization.Note:For the US marketplace, this is the EIN.Occurrence:Conditional
website | string | The link to the website for the charitable organization.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
165000 | API_CHARITY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
165001 | API_CHARITY | REQUEST | Invalid, missing or unsupported marketplace. Please refer to documentation.
165002 | API_CHARITY | REQUEST | Charity Org Id is invalid or missing.
[/TABLE]