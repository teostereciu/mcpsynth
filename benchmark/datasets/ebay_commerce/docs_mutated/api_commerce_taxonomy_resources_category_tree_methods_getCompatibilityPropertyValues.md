# commerce/taxonomy/resources/category_tree/methods/getCompatibilityPropertyValues

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCompatibilityPropertyValues*

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

### Sample 1: Get 2018 Honda Models

### Sample 2: Get 2018 Ferrari Trims

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/get_compatibility_property_values
This call retrieves applicable compatible vehicle property values based on the specified eBay marketplace, specified eBay category, and filters used in the request. Compatible vehicle properties are returned in thecompatibilityProperties.namefield of agetCompatibilityPropertiesresponse.One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified through the requiredcompatibility_propertyfilter. Then, the user has the option of further restricting the compatible vehicle property values that are returned in the response by specifying one or more compatible vehicle property name/value pairs through thefilterquery parameter.See the documentation inURI parameterssection for more information on using thecompatibility_propertyandfilterquery parameters together to customize the data that is retrieved.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
This array contains all compatible vehicle property values that match the specified eBay marketplace, specified eBay category, and filters in the request. If thecompatibility_propertyparameter value in the request is 'Trim', each value returned in eachvaluefield will be a different vehicle trim, applicable to any filters that are set in thefilterquery parameter of the request, and also based on the eBay marketplace and category specified in the call request.Occurrence:Always
Occurrence:Always
Eachvaluefield shows one applicable compatible vehicle property value. The values that are returned will depend on the specified eBay marketplace, specified eBay category, and filters in the request.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the available Honda models for 2018 that are used on the eBay US marketplace to define a motor vehicle that is compatible with a motor vehicle part or accessory.
Thecategory_tree_idvalue is passed in as a path parameter, and this value identifies the eBay marketplace. Thecategory_idvalue is passed in as a query parameter, and the eBay category must be a category that supports parts compatibility. 'Model' is specified as thecompatibility_property, and '2018' and 'Honda' are specified as the 'Year' and 'Make' values, respectively.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/100/get_compatibility_property_values?compatibility_property=Model&category_id=33559&filter=Year:2018,Make:Honda
A successful call returns an array of all available 2018 Honda models for eBay US and eBay category '33559'. Thevaluefields show the actual names that should be used for 'Model' when searching for or defining a motor vehicle that is compatible with a motor vehicle part or accesory.
This sample retrieves the available Ferrari trims for 2018 that are used on the eBay US Motors marketplace to define a motor vehicle that is compatible with a motor vehicle part or accessory.
Related topics
If you need help, contactDeveloper Technical Support.

```
GET https://api.ebay.com/commerce/taxonomy/v1/category_tree/100/get_compatibility_property_values?category_id=6016&compatibility_property=Trim&filter=Year:2018,Make:Toyota,Model:Camry
```

```
filter=Year:2022,Make:Audi,Model:A4,BodyStyle:AWD B9 8W5\,8WD
```
- eBay US: 0
- eBay Motors US: 100
- eBay Canada: 2
- eBay UK: 3
- eBay Germany: 77
- eBay Australia: 15
- eBay France: 71
- eBay Italy: 101
- eBay Spain: 186
- Set thecompatibility_propertyfilter tocompatibility_property=Trim
- Include the following name/value filters using onefilterparameter:Year:2022Make:AudiModel:A4BodyStyle:AWD B9 8W5\,8WD
- Year:2022
- Make:Audi
- Model:A4
- BodyStyle:AWD B9 8W5\,8WD
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | This is the unique identifier of the category tree. The following is the list ofcategory_tree_idvalues and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and thecategory_idvalue, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcycles.eBay US: 0eBay Motors US: 100eBay Canada: 2eBay UK: 3eBay Germany: 77eBay Australia: 15eBay France: 71eBay Italy: 101eBay Spain: 186Occurrence:Required
compatibility_property | string | One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified in this required filter. Compatible vehicle properties are returned in thecompatibilityProperties.namefield of agetCompatibilityPropertiesresponse.For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set this filter as follows:compatibility_property=Trimand then include the following three name/value filters through onefilterparameter:filter=Year:2018,Make:Toyota,Model:Camry.So, putting this all together, the URI would look something like this:GET https://api.ebay.com/commerce/taxonomy/v1/category_tree/100/get_compatibility_property_values?category_id=6016&compatibility_property=Trim&filter=Year:2018,Make:Toyota,Model:CamryOccurrence:Required
category_id | string | The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcycles.ThegetAutomotivePartsCompatibilityPoliciesmethod of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that support parts compatibility for vehicles.Occurrence:Required
filter | ConstraintFilter | One or more compatible vehicle property name/value pairs are passed in through this query parameter. The compatible vehicle property name and corresponding value are delimited with a colon (:), such asfilter=Year:2018, and multiple compatible vehicle property name/value pairs are delimited with a comma (,).Note:Commas are used as delimiters between filter values. If a value includes a comma (e.g.,BodyStyle:AWD B9 8W5,C8WD) youmustinclude a backslash (\) immediately before the comma to prevent it from being evaluated as a delimiter.As with all query parameter values, the filter parameters must be URL encoded. For more information about encoding request parameters, refer toURL encoding query parameter values.For example, to retrieve all vehicle trims for a 2022 Audi A4:Set thecompatibility_propertyfilter tocompatibility_property=TrimInclude the following name/value filters using onefilterparameter:Year:2022Make:AudiModel:A4BodyStyle:AWD B9 8W5\,8WDThe resulting comma-separated filter query parameter is:filter=Year:2022,Make:Audi,Model:A4,BodyStyle:AWD B9 8W5\,8WDThe following sample shows the same filter but with URL encoding for the blank spaces.GET https://api.ebay.com/commerce/taxonomy/v1/category_tree/100/get_compatibility_property_values?category_id=6016&compatibility_property=Trim&filter=Year:2022,Make:Audi,Model:A4,BodyStyle:AWD%20B9%208W5%5C%2C8WDNote:While not required, it is strongly recommended that users page_size the size of the result set by using thefilterquery parameter. Failure to do so may result in a timeout error if too much data is attempted to be returned.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
compatibilityPropertyValues | array ofCompatibilityPropertyValue | This array contains all compatible vehicle property values that match the specified eBay marketplace, specified eBay category, and filters in the request. If thecompatibility_propertyparameter value in the request is 'Trim', each value returned in eachvaluefield will be a different vehicle trim, applicable to any filters that are set in thefilterquery parameter of the request, and also based on the eBay marketplace and category specified in the call request.Occurrence:Always
compatibilityPropertyValues.value | string | Eachvaluefield shows one applicable compatible vehicle property value. The values that are returned will depend on the specified eBay marketplace, specified eBay category, and filters in the request.Occurrence:Always
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
62100 | API_TAXONOMY | REQUEST | The filter format is invalid. For more information, see the API call reference documentation.
62101 | API_TAXONOMY | REQUEST | This category ID is disabled for parts compatibility.
62102 | API_TAXONOMY | REQUEST | The compatibility property is invalid.
62103 | API_TAXONOMY | REQUEST | The CategoryTreeId is not supported.
62104 | API_TAXONOMY | REQUEST | Missing compatibility property.
[/TABLE]