# commerce/identity/resources/user/methods/getUser

*Source: https://developer.ebay.com/api-docs/commerce/identity/resources/user/methods/getUser*

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

### Sample 1: Retrieve Public Information about an Individual

### Sample 2: Retrieve Public Information about a Business

#### Thank you for helping us to improve the eBay developer program.
This method retrieves the account profile information for an authenticated user, which requires aUser access token. What is returned is controlled by thescopes.For a business account you use the default scopecommerce.identity.readonly, which returns all the fields in thebusinessAccountcontainer. These are returned  because this is all public information.For an individual account, the fields returned in theindividualAccountcontainer are based on the scope you use. Using the default scope, only public information, such as eBay user ID, are returned. For details about what each scope returns, see theIdentity API Overview.In the Sandbox, this API returns mock data.Note:You must use the correct scope or scopes for the data you want returned.
For a business account you use the default scopecommerce.identity.readonly, which returns all the fields in thebusinessAccountcontainer. These are returned  because this is all public information.
For an individual account, the fields returned in theindividualAccountcontainer are based on the scope you use. Using the default scope, only public information, such as eBay user ID, are returned. For details about what each scope returns, see theIdentity API Overview.
In the Sandbox, this API returns mock data.Note:You must use the correct scope or scopes for the data you want returned.
This method is supported in Sandbox environment. To access the endpoint, just replace theapiz.ebay.comroot URI withapiz.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/commerce.identity.readonly
SeeOAuth access tokensfor more information.
Note:For details on what each scope returns, see theIdentity API Overview.
This call has no payload.
This call has no field definitions.
This call has no response headers.
Indicates the user account type. This is determined when the user registers with eBay. If they register for a business account, this value will be BUSINESS. If they register for a private account, this value will be INDIVIDUAL. This designation is required by the tax laws in the following countries:EBAY_AT, EBAY_BE, EBAY_CH, EBAY_DE, EBAY_ES, EBAY_FR, EBAY_GB, EBAY_IE, EBAY_IT, EBAY_PLValid Values:BUSINESS or INDIVIDUALCode so that your app gracefully handles any future changes to this list.Occurrence:Always
Occurrence:Always
The container that returns the business account information of the user.Occurrence:Conditional
Occurrence:Conditional
The container that returns the address of the business account.Occurrence:Conditional
The first line of the street address.Occurrence:Conditional
The second line of the street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
The city of the address.Occurrence:Conditional
The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
The county of the address.Occurrence:Conditional
The postal code of the address.Occurrence:Conditional
The state or province of the address.Occurrence:Conditional
An additional name that is used for their business on eBay. The business name is returned in thenamefield.Occurrence:Conditional
The email address of the business account.Occurrence:Conditional
The business name associated with the user's eBay account.Occurrence:Conditional
The container that returns the contact details of the person who is the primary contact for this account.Occurrence:Conditional
The first name of the contact person.Occurrence:Conditional
The last name of the contact person.Occurrence:Conditional
The container that returns the primary phone number for the business account.Occurrence:Conditional
The two-letterISO 3166standard of the country to which the phone number belongs.Occurrence:Conditional
The numeric string representing the phone number.Occurrence:Conditional
The type of phone service.Valid Values:MOBILE or LAND_LINECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The container that returns the secondary phone number for the business account.Occurrence:Conditional
The business website address associated with the eBay account.Occurrence:Conditional
The account information of the user.Occurrence:Conditional
The eBay user's registration email address.Occurrence:Conditional
The eBay user's first name.Occurrence:Conditional
The eBay user's last name.Occurrence:Conditional
The container that returns the eBay user's primary phone number information.Occurrence:Conditional
The container that returns the eBay user's address information.Occurrence:Conditional
The container that returns the eBay user's secondary phone number information.Occurrence:Conditional
The eBay site on which the account is registered.Occurrence:Always
Indicates the user's account status. Possible values:CONFIRMED,UNCONFIRMED,ACCOUNTONHOLDandUNDETERMINED.Occurrence:Always
The eBay immutable user ID of the user's account and can always be used to identify the user.Occurrence:Always
The user name, which was specified by the user when they created the account.Note:This value can be changed by the user.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
Note:For response examples for each scope, see theIdentity API Overview.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns the user's public account profile information.
There are no inputs or request payload. The scope used wascommerce.identity.readonly.
GEThttps://apiz.ebay.com/commerce/identity/v1/user/
The output is the public profile information for the user.
This sample returns the user's account profile and business information.
There are no inputs or request payload.  The scope used wascommerce.identity.readonly.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Output container/field | Type | Description
accountType | AccountTypeEnum | Indicates the user account type. This is determined when the user registers with eBay. If they register for a business account, this value will be BUSINESS. If they register for a private account, this value will be INDIVIDUAL. This designation is required by the tax laws in the following countries:EBAY_AT, EBAY_BE, EBAY_CH, EBAY_DE, EBAY_ES, EBAY_FR, EBAY_GB, EBAY_IE, EBAY_IT, EBAY_PLValid Values:BUSINESS or INDIVIDUALCode so that your app gracefully handles any future changes to this list.Occurrence:Always
businessAccount | BusinessAccount | The container that returns the business account information of the user.Occurrence:Conditional
businessAccount.address | Address | The container that returns the address of the business account.Occurrence:Conditional
businessAccount.address.addressLine1 | string | The first line of the street address.Occurrence:Conditional
businessAccount.address.addressLine2 | string | The second line of the street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
businessAccount.address.city | string | The city of the address.Occurrence:Conditional
businessAccount.address.country | CountryCodeEnum | The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
businessAccount.address.county | string | The county of the address.Occurrence:Conditional
businessAccount.address.postalCode | string | The postal code of the address.Occurrence:Conditional
businessAccount.address.stateOrProvince | string | The state or province of the address.Occurrence:Conditional
businessAccount.doingBusinessAs | string | An additional name that is used for their business on eBay. The business name is returned in thenamefield.Occurrence:Conditional
businessAccount.email | string | The email address of the business account.Occurrence:Conditional
businessAccount.name | string | The business name associated with the user's eBay account.Occurrence:Conditional
businessAccount.primaryContact | Contact | The container that returns the contact details of the person who is the primary contact for this account.Occurrence:Conditional
businessAccount.primaryContact.firstName | string | The first name of the contact person.Occurrence:Conditional
businessAccount.primaryContact.lastName | string | The last name of the contact person.Occurrence:Conditional
businessAccount.primaryPhone | Phone | The container that returns the primary phone number for the business account.Occurrence:Conditional
businessAccount.primaryPhone.countryCode | string | The two-letterISO 3166standard of the country to which the phone number belongs.Occurrence:Conditional
businessAccount.primaryPhone.number | string | The numeric string representing the phone number.Occurrence:Conditional
businessAccount.primaryPhone.phoneType | string | The type of phone service.Valid Values:MOBILE or LAND_LINECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
businessAccount.secondaryPhone | Phone | The container that returns the secondary phone number for the business account.Occurrence:Conditional
businessAccount.secondaryPhone.countryCode | string | The two-letterISO 3166standard of the country to which the phone number belongs.Occurrence:Conditional
businessAccount.secondaryPhone.number | string | The numeric string representing the phone number.Occurrence:Conditional
businessAccount.secondaryPhone.phoneType | string | The type of phone service.Valid Values:MOBILE or LAND_LINECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
businessAccount.website | string | The business website address associated with the eBay account.Occurrence:Conditional
individualAccount | IndividualAccount | The account information of the user.Occurrence:Conditional
individualAccount.email | string | The eBay user's registration email address.Occurrence:Conditional
individualAccount.firstName | string | The eBay user's first name.Occurrence:Conditional
individualAccount.lastName | string | The eBay user's last name.Occurrence:Conditional
individualAccount.primaryPhone | Phone | The container that returns the eBay user's primary phone number information.Occurrence:Conditional
individualAccount.primaryPhone.countryCode | string | The two-letterISO 3166standard of the country to which the phone number belongs.Occurrence:Conditional
individualAccount.primaryPhone.number | string | The numeric string representing the phone number.Occurrence:Conditional
individualAccount.primaryPhone.phoneType | string | The type of phone service.Valid Values:MOBILE or LAND_LINECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
individualAccount.registrationAddress | Address | The container that returns the eBay user's address information.Occurrence:Conditional
individualAccount.registrationAddress.addressLine1 | string | The first line of the street address.Occurrence:Conditional
individualAccount.registrationAddress.addressLine2 | string | The second line of the street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
individualAccount.registrationAddress.city | string | The city of the address.Occurrence:Conditional
individualAccount.registrationAddress.country | CountryCodeEnum | The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
individualAccount.registrationAddress.county | string | The county of the address.Occurrence:Conditional
individualAccount.registrationAddress.postalCode | string | The postal code of the address.Occurrence:Conditional
individualAccount.registrationAddress.stateOrProvince | string | The state or province of the address.Occurrence:Conditional
individualAccount.secondaryPhone | Phone | The container that returns the eBay user's secondary phone number information.Occurrence:Conditional
individualAccount.secondaryPhone.countryCode | string | The two-letterISO 3166standard of the country to which the phone number belongs.Occurrence:Conditional
individualAccount.secondaryPhone.number | string | The numeric string representing the phone number.Occurrence:Conditional
individualAccount.secondaryPhone.phoneType | string | The type of phone service.Valid Values:MOBILE or LAND_LINECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
registrationMarketplaceId | MarketplaceIdEnum | The eBay site on which the account is registered.Occurrence:Always
status | UserStatusEnum | Indicates the user's account status. Possible values:CONFIRMED,UNCONFIRMED,ACCOUNTONHOLDandUNDETERMINED.Occurrence:Always
userId | string | The eBay immutable user ID of the user's account and can always be used to identify the user.Occurrence:Always
username | string | The user name, which was specified by the user when they created the account.Note:This value can be changed by the user.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
140000 | API_IDENTITY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
[/TABLE]