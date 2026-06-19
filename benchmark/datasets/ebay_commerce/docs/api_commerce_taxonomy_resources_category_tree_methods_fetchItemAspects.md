# commerce/taxonomy/resources/category_tree/methods/fetchItemAspects

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/fetchItemAspects*

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

### Sample 1: Fetch Item Aspects for a Marketplace

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/fetch_item_aspects
This method returns a complete list of aspects for all of the leaf categories that belong to an eBay marketplace. The eBay marketplace is specified through thecategory_tree_idURI parameter.Note:A successful call returns a payload as a gzipped JSON file sent as a binary file using the content-type:application/octet-stream in the response. This file may be large (over 100 MB, compressed). Extract the JSON file from the compressed file with a utility that handles .gz or .gzip. The open sourceTaxonomy SDKcan be used to compare the aspect metadata that is returned in this response. TheTaxonomy SDKuses this call to surface changes (new, modified, and removed entities) between an updated version of a bulk downloaded file relative to a previous version.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/metadata.insights
SeeOAuth access tokensfor more information.
Note: The metadata.insights scope is conditional and is based on the App Check to gain access to the 'Buyer Demand Data'. Please refer torelevanceIndicator.
This call has no payload.
This call has no field definitions.
This call has no response headers.
Important: The response for this call isalwaysa JSON GZIP file. The response is shown as JSON fields so that they can be explained.
The unique identifier of the eBay category tree being requested.Occurrence:Always
Occurrence:Always
The version of the category tree that is returned in thecategoryTreeIdfield.Occurrence:Always
An array of aspects that are appropriate or necessary for accurately describing items in a particular leaf category.Occurrence:Always
The details that are appropriate or necessary to accurately define the category.Occurrence:Always
The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
The name of the category identified bycategoryId.Occurrence:Always
A list of aspect metadata that is used to describe the items in a particular leaf category.Occurrence:Conditional
Occurrence:Conditional
Information about the formatting, occurrence, and support of this aspect.Occurrence:Always
This value indicate if the aspect identified by theaspects.localizedAspectNamefield is a product aspect (relevant to catalog products in the category) or an item/instance aspect, which is an aspect whose value will vary based on a particular instance of the product.Occurrence:Conditional
The data type of this aspect.Occurrence:Always
A value oftrueindicates that this aspect can be used to help identify item variations.Occurrence:Always
Returned only ifthe value ofaspectDataTypeidentifies a data type that requires specific formatting. Currently, this field provides formatting hints as follows:DATE:YYYY,YYYYMM,YYYYMMDDNUMBER:int32,doubleOccurrence:Conditional
The maximum length of the item/instance aspect's value. The seller must make sure not to exceed this length when specifying the instance aspect's value for a product. This field is only returned for instance aspects.Occurrence:Conditional
The manner in which values of this aspect must be specified by the seller (as free text or by selecting from available options).Occurrence:Always
A value oftrueindicates that this aspect is required when offering items in the specified category.Occurrence:Always
The enumeration value returned in this field will indicate if the corresponding aspect is recommended or optional.Note:This field is always returned, even for hard-mandated/required aspects (whereaspectRequired: true). The value returned for required aspects will beRECOMMENDED, but they are actually required and a seller will be blocked from listing or revising an item without these aspects.Occurrence:Always
The expected date after which the aspect will be required.Note:The value returned in this field specifies only an approximate date, which may not reflect the actual date after which the aspect is required.Occurrence:Conditional
Indicates whether this aspect can accept single or multiple values for items in the specified category.Note:Up to 30 values can be supplied for aspects that accept multiple values.Occurrence:Always
Indicates additional data type requirements for the aspect. For example,NUMERIC_RANGEindicates that the aspect value must be in numeric range format.Note:Currently onlyNUMERIC_RANGEis supported.Occurrence:Conditional
A list of valid values for this aspect (for example:Red,Green, andBlue), along with any constraints on those values.Occurrence:Always
The localized value of this aspect.Note:This value is always localized for the specified marketplace.Occurrence:Always
Not returned ifthe value of thelocalizedValuefield can always be selected for this aspect of the specified category.Contains a list of the dependencies that identify when the value of thelocalizedValuefield is available for the current aspect. Each dependency specifies the values of another aspect of the same category (acontrolaspect), for which the current value of the current aspect can also be selected by the seller.Example:A shirt is available in three sizes and three colors, but only the Small and Medium sizes come in Green. Thus for the Color aspect, the value Green is constrained by its dependency on Size (the control aspect). Only when the Size aspect value is Small or Medium, can the Color aspect value of Green be selected by the seller.Occurrence:Conditional
The name of the control aspect on which the current aspect value depends.Occurrence:Conditional
Contains a list of the values of the control aspect on which this aspect's value depends. When the control aspect has any of the specified values, the current value of the current aspect will also be available.Occurrence:Conditional
The localized name of this aspect (for example:Colouron the eBay UK site).Note:This name is always localized for the specified marketplace.Occurrence:Always
The relevance of this aspect. This field is returned if eBay has data on how many searches have been performed for listings in the category using this item aspect.Note:This container is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields that you want access to 'Buyer Demand Data' in the Taxonomy API.Occurrence:Conditional
The number of recent searches (based on 30 days of data) for the aspect.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the item aspects for the specified eBay marketplace.
Thecategory_tree_idvalue is passed as a path parameter, and this value identifies the eBay marketplace.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/0/fetch_item_aspects
The output is an HTTP status. If the call is successful, the gzipped JSON file containing the item aspects for the specified eBay marketplace is downloaded.
Related topics
If you need help, contactDeveloper Technical Support.
- DATE:YYYY,YYYYMM,YYYYMMDD
- NUMBER:int32,double
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using thegetDefaultCategoryTreeIdmethod.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
categoryTreeId | string | The unique identifier of the eBay category tree being requested.Occurrence:Always
categoryTreeVersion | string | The version of the category tree that is returned in thecategoryTreeIdfield.Occurrence:Always
categoryAspects | array ofCategoryAspect | An array of aspects that are appropriate or necessary for accurately describing items in a particular leaf category.Occurrence:Always
categoryAspects.category | Category | The details that are appropriate or necessary to accurately define the category.Occurrence:Always
categoryAspects.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
categoryAspects.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
categoryAspects.aspects | array ofAspect | A list of aspect metadata that is used to describe the items in a particular leaf category.Occurrence:Conditional
categoryAspects.aspects.aspectConstraint | AspectConstraint | Information about the formatting, occurrence, and support of this aspect.Occurrence:Always
categoryAspects.aspects.aspectConstraint.aspectApplicableTo | array ofAspectApplicableToEnum | This value indicate if the aspect identified by theaspects.localizedAspectNamefield is a product aspect (relevant to catalog products in the category) or an item/instance aspect, which is an aspect whose value will vary based on a particular instance of the product.Occurrence:Conditional
categoryAspects.aspects.aspectConstraint.aspectDataType | AspectDataTypeEnum | The data type of this aspect.Occurrence:Always
categoryAspects.aspects.aspectConstraint.aspectEnabledForVariations | boolean | A value oftrueindicates that this aspect can be used to help identify item variations.Occurrence:Always
categoryAspects.aspects.aspectConstraint.aspectFormat | string | Returned only ifthe value ofaspectDataTypeidentifies a data type that requires specific formatting. Currently, this field provides formatting hints as follows:DATE:YYYY,YYYYMM,YYYYMMDDNUMBER:int32,doubleOccurrence:Conditional
categoryAspects.aspects.aspectConstraint.aspectMaxLength | integer | The maximum length of the item/instance aspect's value. The seller must make sure not to exceed this length when specifying the instance aspect's value for a product. This field is only returned for instance aspects.Occurrence:Conditional
categoryAspects.aspects.aspectConstraint.aspectMode | AspectModeEnum | The manner in which values of this aspect must be specified by the seller (as free text or by selecting from available options).Occurrence:Always
categoryAspects.aspects.aspectConstraint.aspectRequired | boolean | A value oftrueindicates that this aspect is required when offering items in the specified category.Occurrence:Always
categoryAspects.aspects.aspectConstraint.aspectUsage | AspectUsageEnum | The enumeration value returned in this field will indicate if the corresponding aspect is recommended or optional.Note:This field is always returned, even for hard-mandated/required aspects (whereaspectRequired: true). The value returned for required aspects will beRECOMMENDED, but they are actually required and a seller will be blocked from listing or revising an item without these aspects.Occurrence:Always
categoryAspects.aspects.aspectConstraint.expectedRequiredByDate | string | The expected date after which the aspect will be required.Note:The value returned in this field specifies only an approximate date, which may not reflect the actual date after which the aspect is required.Occurrence:Conditional
categoryAspects.aspects.aspectConstraint.itemToAspectCardinality | ItemToAspectCardinalityEnum | Indicates whether this aspect can accept single or multiple values for items in the specified category.Note:Up to 30 values can be supplied for aspects that accept multiple values.Occurrence:Always
categoryAspects.aspects.aspectConstraint.aspectAdvancedDataType | AspectAdvancedDataTypeEnum | Indicates additional data type requirements for the aspect. For example,NUMERIC_RANGEindicates that the aspect value must be in numeric range format.Note:Currently onlyNUMERIC_RANGEis supported.Occurrence:Conditional
categoryAspects.aspects.aspectValues | array ofAspectValue | A list of valid values for this aspect (for example:Red,Green, andBlue), along with any constraints on those values.Occurrence:Always
categoryAspects.aspects.aspectValues.localizedValue | string | The localized value of this aspect.Note:This value is always localized for the specified marketplace.Occurrence:Always
categoryAspects.aspects.aspectValues.valueConstraints | array ofValueConstraint | Not returned ifthe value of thelocalizedValuefield can always be selected for this aspect of the specified category.Contains a list of the dependencies that identify when the value of thelocalizedValuefield is available for the current aspect. Each dependency specifies the values of another aspect of the same category (acontrolaspect), for which the current value of the current aspect can also be selected by the seller.Example:A shirt is available in three sizes and three colors, but only the Small and Medium sizes come in Green. Thus for the Color aspect, the value Green is constrained by its dependency on Size (the control aspect). Only when the Size aspect value is Small or Medium, can the Color aspect value of Green be selected by the seller.Occurrence:Conditional
categoryAspects.aspects.aspectValues.valueConstraints.applicableForLocalizedAspectName | string | The name of the control aspect on which the current aspect value depends.Occurrence:Conditional
categoryAspects.aspects.aspectValues.valueConstraints.applicableForLocalizedAspectValues | array ofstring | Contains a list of the values of the control aspect on which this aspect's value depends. When the control aspect has any of the specified values, the current value of the current aspect will also be available.Occurrence:Conditional
categoryAspects.aspects.localizedAspectName | string | The localized name of this aspect (for example:Colouron the eBay UK site).Note:This name is always localized for the specified marketplace.Occurrence:Always
categoryAspects.aspects.relevanceIndicator | RelevanceIndicator | The relevance of this aspect. This field is returned if eBay has data on how many searches have been performed for listings in the category using this item aspect.Note:This container is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields that you want access to 'Buyer Demand Data' in the Taxonomy API.Occurrence:Conditional
categoryAspects.aspects.relevanceIndicator.searchCount | integer | The number of recent searches (based on 30 days of data) for the aspect.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | Success
400 | Bad Request
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62004 | API_TAXONOMY | REQUEST | The specified category tree ID was not found.
[/TABLE]