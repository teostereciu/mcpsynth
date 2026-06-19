# commerce/charity/resources/charity_org/methods/getCharityOrgs

*Source: https://developer.ebay.com/api-docs/commerce/charity/resources/charity_org/methods/getCharityOrgs*

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

### Sample 1: Search for Charitable Organizations by Query

### Sample 2: Search for Charitable Organizations by Registration ID

#### Thank you for helping us to improve the eBay developer program.
GET/charity_org
This call is used to search for supported charitable organizations. It allows users to search for a specific charitable organization, or for multiple charitable organizations, from a particular charitable domain and/or geographical region, or by using search criteria.The call returns paginated search results containing the charitable organizations that match the specified criteria.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The list of charitable organizations that match the search criteria.Occurrence:Conditional
Occurrence:Conditional
The ID of the charitable organization.Occurrence:Always
Occurrence:Always
The description of the charitable organization.Occurrence:Conditional
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
The relative path to the current set of results.Occurrence:Always
The number of items, from the result set, returned in a single page.Valid Values:1-100Default:20Occurrence:Conditional
The relative path to the next set of results.Occurrence:Conditional
The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Valid Values:0-10,000Default:0Occurrence:Conditional
The relative path to the previous set of results.Occurrence:Conditional
The total number of matches for the search criteria.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves paginated search results containing the charitable organizations that match the query string.
The inputs are theqandlimitURI parameters. There is no payload with this request.
GEThttps://api.ebay.com/commerce/charity/v1/charity_org/?q=red cross&limit=3
If the call is successful, three charitable organizations matching the specified criteria will be returned.
The input is theregistration_idsURI parameter. There is no payload with this request.
If the call is successful, the charitable organization matching the specified registration ID will be returned.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
q | string | A query string that matches the keywords in name, mission statement, or description.Occurrence:Optional
registration_ids | array ofstring | A comma-separated list of charitable organization registration IDs.Note:Do not specify this parameter for query-based searches. Specify either theqorregistration_idsparameter, but not both.Maximum Limit:20Occurrence:Optional
limit | string | The number of items, from the result set, returned in a single page.Valid Values:1-100Default:20Occurrence:Optional
offset | string | The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Valid Values:0-10,000Default:0Occurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-MARKETPLACE-ID | string | A header used to specify the eBay marketplace ID.Valid Values:EBAY_GBandEBAY_USOccurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
charityOrgs | array ofCharityOrg | The list of charitable organizations that match the search criteria.Occurrence:Conditional
charityOrgs.charityOrgId | string | The ID of the charitable organization.Occurrence:Always
charityOrgs.description | string | The description of the charitable organization.Occurrence:Conditional
charityOrgs.location | Location | The location details of the charitable organization.Occurrence:Conditional
charityOrgs.location.address | Address | The address of the charitable organization.Occurrence:Conditional
charityOrgs.location.address.city | string | The city of the charitable organization.Occurrence:Conditional
charityOrgs.location.address.stateOrProvince | string | The state or province of the charitable organization.Occurrence:Conditional
charityOrgs.location.address.postalCode | string | The postal code of the charitable organization.Occurrence:Conditional
charityOrgs.location.address.country | CountryCodeEnum | The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
charityOrgs.location.geoCoordinates | GeoCoordinates | The geo-coordinates of the charitable organization.Occurrence:Conditional
charityOrgs.location.geoCoordinates.latitude | number | The latitude component of the geographic coordinate.Occurrence:Conditional
charityOrgs.location.geoCoordinates.longitude | number | The longitude component of the geographic coordinate.Occurrence:Conditional
charityOrgs.logoImage | Image | The logo of the charitable organization.Occurrence:Conditional
charityOrgs.logoImage.height | string | The height of the logo image.Occurrence:Conditional
charityOrgs.logoImage.imageUrl | string | The URL to the logo image location.Occurrence:Conditional
charityOrgs.logoImage.width | string | The width of the logo image.Occurrence:Conditional
charityOrgs.missionStatement | string | The mission statement of the charitable organization.Occurrence:Conditional
charityOrgs.name | string | The name of the charitable organization.Occurrence:Always
charityOrgs.registrationId | string | The registration ID for the charitable organization.Note:For the US marketplace, this is the EIN.Occurrence:Conditional
charityOrgs.website | string | The link to the website for the charitable organization.Occurrence:Conditional
href | string | The relative path to the current set of results.Occurrence:Always
limit | integer | The number of items, from the result set, returned in a single page.Valid Values:1-100Default:20Occurrence:Conditional
next | string | The relative path to the next set of results.Occurrence:Conditional
offset | integer | The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Valid Values:0-10,000Default:0Occurrence:Conditional
prev | string | The relative path to the previous set of results.Occurrence:Conditional
total | integer | The total number of matches for the search criteria.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
165000 | API_CHARITY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
165001 | API_CHARITY | REQUEST | Invalid, missing or unsupported marketplace. Please refer to documentation.
165003 | API_CHARITY | REQUEST | The specified limit is invalid. Maximum value supported is 100.
165004 | API_CHARITY | REQUEST | The specified offset is invalid.
165005 | API_CHARITY | REQUEST | Please specify registration_ids OR query text for the search.
[/TABLE]