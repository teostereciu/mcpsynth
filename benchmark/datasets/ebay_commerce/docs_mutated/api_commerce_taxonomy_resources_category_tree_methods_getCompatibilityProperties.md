# commerce/taxonomy/resources/category_tree/methods/getCompatibilityProperties

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCompatibilityProperties*

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

### Sample 1: Get compatibility properties for US

### Sample 2: Get compatibility properties for Italy

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/get_compatibility_properties
This call retrieves the compatible vehicle aspects that are used to define a motor vehicle that is compatible with a motor vehicle part or accessory. The values that are retrieved here might include motor vehicle aspects such as 'Make', 'Model', 'Year', 'Engine', and 'Trim', and each of these aspects are localized for the eBay marketplace.Thecategory_tree_idvalue is passed in as a path parameter, and this value identifies the eBay category tree. Thecategory_idvalue is passed in as a query parameter, as this parameter is also required. The specified category must be a category that supports parts compatibility.At this time, this operation only supports parts and accessories listings for cars, trucks, and motorcycles (not boats, power sports, or any other vehicle types). Only the following eBay marketplaces support parts compatibility:eBay US (Motors and non-Motors categories)eBay Canada (Motors and non-Motors categories)eBay UKeBay GermanyeBay AustraliaeBay FranceeBay ItalyeBay Spain
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
This container consists of an array of all compatible vehicle properties applicable to the specified eBay marketplace and eBay category ID.Occurrence:Always
Occurrence:Always
This is the actual name of the compatible vehicle property as it is known on the specified eBay marketplace and in the eBay category. This is the string value that should be used in thecompatibility_propertyandfilterquery parameters of agetCompatibilityPropertyValuesrequest URI.Typical vehicle properties are 'Make', 'Model', 'Year', 'Engine', and 'Trim', but will vary based on the eBay marketplace and the eBay category.Occurrence:Always
This is the localized name of the compatible vehicle property. The language that is used will depend on the user making the call, or based on the language specified if theContent-LanguageHTTP header is used.In some instances, the string value in this field may be the same as the string in the correspondingnamefield.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the compatible vehicle aspects that are used on the eBay US marketplace to define a motor vehicle that is compatible with a motor vehicle part or accessory.
Thecategory_tree_idvalue is passed in as a path parameter, and this value identifies the eBay marketplace. Thecategory_idvalue is passed in as a query parameter, and the eBay category must be a category that supports parts compatibility.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/100/get_compatibility_properties?category_id=33733
A successful call returns an array of all compatible vehicle properties applicable to eBay US and eBay category '33733'. Thenamefields show the actual names of the compatible vehicle properties on the specified eBay marketplace and eBay category. These are the string values that should be used in thecompatibility_propertyandfilterquery parameters of agetCompatibilityPropertyValuesrequest URI.Typical vehicle properties on the eBay US marketplace are 'Year', 'Make', 'Model', 'Trim', and 'Engine'.ThelocalizedNamefields show the localized versions of the compatible vehicle properties. The language that is used will depend on the user making the call, or based on the language specified if theContent-LanguageHTTP header is used.In some instances, the string value in thelocalizedNamefield may be the same as the string in the correspondingnamefield.
Related topics
If you need help, contactDeveloper Technical Support.
- eBay US (Motors and non-Motors categories)
- eBay Canada (Motors and non-Motors categories)
- eBay UK
- eBay Germany
- eBay Australia
- eBay France
- eBay Italy
- eBay Spain
- eBay US: 0
- eBay Motors US: 100
- eBay Canada: 2
- eBay UK: 3
- eBay Germany: 77
- eBay Australia: 15
- eBay France: 71
- eBay Italy: 101
- eBay Spain: 186
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | This is the unique identifier of category tree. The following is the list ofcategory_tree_idvalues and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and thecategory_idvalue, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcycles.eBay US: 0eBay Motors US: 100eBay Canada: 2eBay UK: 3eBay Germany: 77eBay Australia: 15eBay France: 71eBay Italy: 101eBay Spain: 186Occurrence:Required
category_id | string | The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.ThegetAutomotivePartsCompatibilityPoliciesmethod of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that support parts compatibility for vehicles.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
compatibilityProperties | array ofCompatibilityProperty | This container consists of an array of all compatible vehicle properties applicable to the specified eBay marketplace and eBay category ID.Occurrence:Always
compatibilityProperties.name | string | This is the actual name of the compatible vehicle property as it is known on the specified eBay marketplace and in the eBay category. This is the string value that should be used in thecompatibility_propertyandfilterquery parameters of agetCompatibilityPropertyValuesrequest URI.Typical vehicle properties are 'Make', 'Model', 'Year', 'Engine', and 'Trim', but will vary based on the eBay marketplace and the eBay category.Occurrence:Always
compatibilityProperties.localizedName | string | This is the localized name of the compatible vehicle property. The language that is used will depend on the user making the call, or based on the language specified if theContent-LanguageHTTP header is used.In some instances, the string value in this field may be the same as the string in the correspondingnamefield.Occurrence:Always
[/TABLE]

[TABLE]
200 | Success
204 | No content
400 | Bad Request
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62004 | API_TAXONOMY | REQUEST | The specified category tree ID was not found.
62005 | API_TAXONOMY | REQUEST | The specified category ID does not belong to specified category tree.
62006 | API_TAXONOMY | REQUEST | Missing category ID.
62101 | API_TAXONOMY | REQUEST | This category ID is disabled for parts compatibility.
62103 | API_TAXONOMY | REQUEST | The CategoryTreeId is not supported.
[/TABLE]