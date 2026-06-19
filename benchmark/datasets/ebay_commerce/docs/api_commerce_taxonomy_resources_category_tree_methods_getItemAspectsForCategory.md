# commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory*

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

### Sample 1: Get aspects for a leaf category

### Sample 2: Get the expected required by date for an aspect

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/get_item_aspects_for_category
This call returns a list ofaspectsthat are appropriate or necessary for accurately describing items in the specified leaf category. Each aspect identifies an item attribute (for example, color,) for which the seller will be required or encouraged to provide a value (or variation values) when offering an item in that category on eBay.For each aspect,getItemAspectsForCategoryprovides complete metadata, including:The aspect's data type, format, and entry modeWhether the aspect is required in listingsWhether the aspect can be used for item variationsWhether the aspect accepts multiple values for an itemAllowed values for the aspectUse this information to construct an interface through which sellers can enter or select the appropriate values for their items or item variations. Once you collect those values, include them as product aspects when creating inventory items using the Inventory API.
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
A list of item aspects (for example, color) that are appropriate or necessary for accurately describing items in a particular leaf category. Each category has a different set of aspects and different requirements for aspect values. Sellers are required or encouraged to provide one or more acceptable values for each aspect when offering an item in that category on eBay.Occurrence:Always
Occurrence:Always
Information about the formatting, occurrence, and support of this aspect.Occurrence:Always
This value indicate if the aspect identified by theaspects.localizedAspectNamefield is a product aspect (relevant to catalog products in the category) or an item/instance aspect, which is an aspect whose value will vary based on a particular instance of the product.Occurrence:Conditional
Occurrence:Conditional
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
This sample returns an array of aspects that are appropriate or necessary for accurately describing items in the specified leaf category.
Use thecategory_tree_idpath parameter to specify the category tree, and use thecategory_idquery parameter to specify the leaf category for which to retrieve associated aspects.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/0/get_item_aspects_for_category?category_id=67726
A successful call returns a list of the aspects associated with category67726, including each aspect's data type, format, entry mode, cardinality, and support. It also returns a list of valid values for each aspect, including any constraints on the applicability of each value.
This sample retrieves an array of aspects for the specified leaf category, including the expected date after which aspects will be required.Note:The category specified in this sample is atestcategory used for example purposes only.
Note:The category specified in this sample is atestcategory used for example purposes only.
A successful call returns a list of aspects associated with category178090, including the expected date after which each aspect will be required, if available.
Related topics
If you need help, contactDeveloper Technical Support.
- The aspect's data type, format, and entry mode
- Whether the aspect is required in listings
- Whether the aspect can be used for item variations
- Whether the aspect accepts multiple values for an item
- Allowed values for the aspect
- DATE:YYYY,YYYYMM,YYYYMMDD
- NUMBER:int32,double
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using thegetDefaultCategoryTreeIdmethod.Occurrence:Required
category_id | string | The unique identifier of the leaf category for which aspects are being requested.Note:If thecategory_idsubmitted does not identify a leaf node of the tree, this call returns an error.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
aspects | array ofAspect | A list of item aspects (for example, color) that are appropriate or necessary for accurately describing items in a particular leaf category. Each category has a different set of aspects and different requirements for aspect values. Sellers are required or encouraged to provide one or more acceptable values for each aspect when offering an item in that category on eBay.Occurrence:Always
aspects.aspectConstraint | AspectConstraint | Information about the formatting, occurrence, and support of this aspect.Occurrence:Always
aspects.aspectConstraint.aspectApplicableTo | array ofAspectApplicableToEnum | This value indicate if the aspect identified by theaspects.localizedAspectNamefield is a product aspect (relevant to catalog products in the category) or an item/instance aspect, which is an aspect whose value will vary based on a particular instance of the product.Occurrence:Conditional
aspects.aspectConstraint.aspectDataType | AspectDataTypeEnum | The data type of this aspect.Occurrence:Always
aspects.aspectConstraint.aspectEnabledForVariations | boolean | A value oftrueindicates that this aspect can be used to help identify item variations.Occurrence:Always
aspects.aspectConstraint.aspectFormat | string | Returned only ifthe value ofaspectDataTypeidentifies a data type that requires specific formatting. Currently, this field provides formatting hints as follows:DATE:YYYY,YYYYMM,YYYYMMDDNUMBER:int32,doubleOccurrence:Conditional
aspects.aspectConstraint.aspectMaxLength | integer | The maximum length of the item/instance aspect's value. The seller must make sure not to exceed this length when specifying the instance aspect's value for a product. This field is only returned for instance aspects.Occurrence:Conditional
aspects.aspectConstraint.aspectMode | AspectModeEnum | The manner in which values of this aspect must be specified by the seller (as free text or by selecting from available options).Occurrence:Always
aspects.aspectConstraint.aspectRequired | boolean | A value oftrueindicates that this aspect is required when offering items in the specified category.Occurrence:Always
aspects.aspectConstraint.aspectUsage | AspectUsageEnum | The enumeration value returned in this field will indicate if the corresponding aspect is recommended or optional.Note:This field is always returned, even for hard-mandated/required aspects (whereaspectRequired: true). The value returned for required aspects will beRECOMMENDED, but they are actually required and a seller will be blocked from listing or revising an item without these aspects.Occurrence:Always
aspects.aspectConstraint.expectedRequiredByDate | string | The expected date after which the aspect will be required.Note:The value returned in this field specifies only an approximate date, which may not reflect the actual date after which the aspect is required.Occurrence:Conditional
aspects.aspectConstraint.itemToAspectCardinality | ItemToAspectCardinalityEnum | Indicates whether this aspect can accept single or multiple values for items in the specified category.Note:Up to 30 values can be supplied for aspects that accept multiple values.Occurrence:Always
aspects.aspectConstraint.aspectAdvancedDataType | AspectAdvancedDataTypeEnum | Indicates additional data type requirements for the aspect. For example,NUMERIC_RANGEindicates that the aspect value must be in numeric range format.Note:Currently onlyNUMERIC_RANGEis supported.Occurrence:Conditional
aspects.aspectValues | array ofAspectValue | A list of valid values for this aspect (for example:Red,Green, andBlue), along with any constraints on those values.Occurrence:Always
aspects.aspectValues.localizedValue | string | The localized value of this aspect.Note:This value is always localized for the specified marketplace.Occurrence:Always
aspects.aspectValues.valueConstraints | array ofValueConstraint | Not returned ifthe value of thelocalizedValuefield can always be selected for this aspect of the specified category.Contains a list of the dependencies that identify when the value of thelocalizedValuefield is available for the current aspect. Each dependency specifies the values of another aspect of the same category (acontrolaspect), for which the current value of the current aspect can also be selected by the seller.Example:A shirt is available in three sizes and three colors, but only the Small and Medium sizes come in Green. Thus for the Color aspect, the value Green is constrained by its dependency on Size (the control aspect). Only when the Size aspect value is Small or Medium, can the Color aspect value of Green be selected by the seller.Occurrence:Conditional
aspects.aspectValues.valueConstraints.applicableForLocalizedAspectName | string | The name of the control aspect on which the current aspect value depends.Occurrence:Conditional
aspects.aspectValues.valueConstraints.applicableForLocalizedAspectValues | array ofstring | Contains a list of the values of the control aspect on which this aspect's value depends. When the control aspect has any of the specified values, the current value of the current aspect will also be available.Occurrence:Conditional
aspects.localizedAspectName | string | The localized name of this aspect (for example:Colouron the eBay UK site).Note:This name is always localized for the specified marketplace.Occurrence:Always
aspects.relevanceIndicator | RelevanceIndicator | The relevance of this aspect. This field is returned if eBay has data on how many searches have been performed for listings in the category using this item aspect.Note:This container is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields that you want access to 'Buyer Demand Data' in the Taxonomy API.Occurrence:Conditional
aspects.relevanceIndicator.searchCount | integer | The number of recent searches (based on 30 days of data) for the aspect.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | Success
204 | No Content
400 | Bad Request
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62004 | API_TAXONOMY | REQUEST | The specified category tree ID was not found.
62005 | API_TAXONOMY | REQUEST | The specified category ID does not belong to specified category tree.
62006 | API_TAXONOMY | REQUEST | Missing category ID.
62008 | API_TAXONOMY | REQUEST | The specified category ID is the root for the category tree.
62009 | API_TAXONOMY | REQUEST | The specified category ID must be a leaf category.
[/TABLE]