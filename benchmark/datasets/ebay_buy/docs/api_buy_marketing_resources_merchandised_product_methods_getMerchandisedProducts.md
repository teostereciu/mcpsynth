# buy/marketing/resources/merchandised_product/methods/getMerchandisedProducts

*Source: https://developer.ebay.com/api-docs/buy/marketing/resources/merchandised_product/methods/getMerchandisedProducts*

---

### Restrictions

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

### Sample 1: Retrieve Best Selling Products

### Sample 2: Retrieve Best Selling Products by Aspect

#### Thank you for helping us to improve the eBay developer program.
GET/merchandised_product
This method returns an array of products based on the category and metric specified. This includes details of the product, such as the eBay product ID (EPID), title, and user reviews and ratings for the product. You can use theepidreturned by this method in the Browse APIsearchmethod to retrieve items for this product.RestrictionsTo testgetMerchandisedProductsin Sandbox, you must use category ID 9355 and the response will be mock data.For a list of supported sites and other restrictions, seeAPI Restrictions.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.marketing
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
An array of containers for the products.Occurrence:Conditional
Occurrence:Conditional
The average rating for the product based on eBay user ratings.Occurrence:Conditional
The eBay product identifier of a product from the eBay product catalog. You can use this value in the Browse APIsearchmethod to retrieve items for this product.Occurrence:Conditional
The container for the product image.Occurrence:Conditional
Reserved for future use.Occurrence:Conditional
The URL of the image.Occurrence:Conditional
An array of containers for the product market price details, such as condition and market price.Occurrence:Conditional
The name for the condition of the product. For example: NEWOccurrence:Conditional
An array of condition identifiers for the product.Occurrence:Conditional
The lowest priced active item for this product on eBay.Occurrence:Conditional
The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Conditional
The monetary amount, in the currency specified by thecurrencyfield.Occurrence:Conditional
An array of containers for ratings of the product aspects, such as "Is it a good value".Occurrence:Conditional
The number of eBay users that rated the product on this aspect.Occurrence:Conditional
The name of the rating aspect. Camping tent examples: Is it lightweight? or Is it easy to set up?Occurrence:Conditional
The answer or value of the rating aspect. Camping tent examples: Lightweight or Easy to set upOccurrence:Conditional
The container for the details of the aspect rating. The details show the aspect rating value, usually TRUE or FALSE and the user count and percentage.Occurrence:Conditional
The number of eBay users that choose this rating aspect value.Occurrence:Conditional
The percentage of the aspect rating value.ratingAspectDistributions.percentage=ratingAspectDistributions.count/ratingAspects.countOccurrence:Conditional
The rating aspect. For example: TRUE or FALSEOccurrence:Conditional
The total number of eBay users that rated the product.Occurrence:Conditional
The total number of eBay users that wrote a review for the product.Occurrence:Conditional
The title of the product.Occurrence:Conditional
The container with all the warnings for the input request.Occurrence:Conditional
This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.Occurrence:Always
Occurrence:Always
The name of the primary system where the error occurred. This is relevant for application errors.Occurrence:Always
A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.Occurrence:Always
An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.Occurrence:Conditional
A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.Occurrence:Conditional
A description of the condition that caused the error or warning.Occurrence:Always
An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.Occurrence:Conditional
This is the name of input field that caused an issue with the call request.Occurrence:Conditional
This is the actual value that was passed in for the element specified in thenamefield.Occurrence:Conditional
The name of the subdomain in which the error or warning occurred.Occurrence:NA
Occurrence:NA
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
The call retrieves the best selling cameras.
The inputs are thecategory_idand themetric_name.
GEThttps://api.ebay.com/buy/marketing/v1_beta/merchandised_product?category_id=31388&metric_name=BEST_SELLING
The output is an array of products and the details of the product, such as the eBay product Id (EPID), title, and user review and rating for the product.
The call retrieves the best selling Cannon cameras.
The inputs are thecategory_id, themetric_name, andaspect_filter, which refines the results to Cannon cameras.
Related topics
If you need help, contactDeveloper Technical Support.
- To testgetMerchandisedProductsin Sandbox, you must use category ID 9355 and the response will be mock data.
- For a list of supported sites and other restrictions, seeAPI Restrictions.
- Use theCategory Changes page.
- Use the Taxonomy API. For details seeGet Categories for Buy APIs.
- Use the Browse API and submit the following method to get thedominantCategoryIdfor an item./buy/browse/v1/item_summary/search?q=keyword&fieldgroups=ASPECT_REFINEMENTS
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
metric_name | string | This value filters the result set by the specified metric. Only products in this metric are returned.Note:Currently, the only metric supported isBEST_SELLING.Default:BEST_SELLINGMaximum:1Required:1Occurrence:Required
category_id | string | This query parameter limits the products returned to a specific eBay category.The list of eBay category IDs is not published and category IDs are not all the same across all the eBay maketplace. You can use the following techniques to find a category by site:Use theCategory Changes page.Use the Taxonomy API. For details seeGet Categories for Buy APIs.Use the Browse API and submit the following method to get thedominantCategoryIdfor an item./buy/browse/v1/item_summary/search?q=keyword&fieldgroups=ASPECT_REFINEMENTSMaximum:1Required:1Occurrence:Required
limit | string | This value specifies the maximum number of products to return in a result set.Note:Maximum value means the method will return uptothat many products per set, but it can be less than this value. If the number of products found is less than this value, the method will return all of the products matching the criteria.Default:8Maximum:100Occurrence:Optional
aspect_filter | MarketingAspectFilter | This value specifies the aspect name/value pairs used to further refine product results.For example:/buy/marketing/v1_beta/merchandised_product?category_id=31388&metric_name=BEST_SELLING&aspect_filter=Brand:CanonYou can use the Browse APIsearchmethod with thefieldgroups=ASPECT_REFINEMENTSfield to return the aspects of a product.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
merchandisedProducts | array ofMerchandisedProduct | An array of containers for the products.Occurrence:Conditional
merchandisedProducts.averageRating | string | The average rating for the product based on eBay user ratings.Occurrence:Conditional
merchandisedProducts.epid | string | The eBay product identifier of a product from the eBay product catalog. You can use this value in the Browse APIsearchmethod to retrieve items for this product.Occurrence:Conditional
merchandisedProducts.image | Image | The container for the product image.Occurrence:Conditional
merchandisedProducts.image.height | integer | Reserved for future use.Occurrence:Conditional
merchandisedProducts.image.imageUrl | string | The URL of the image.Occurrence:Conditional
merchandisedProducts.image.width | integer | Reserved for future use.Occurrence:Conditional
merchandisedProducts.marketPriceDetails | array ofMarketPriceDetail | An array of containers for the product market price details, such as condition and market price.Occurrence:Conditional
merchandisedProducts.marketPriceDetails.conditionGroup | string | The name for the condition of the product. For example: NEWOccurrence:Conditional
merchandisedProducts.marketPriceDetails.conditionIds | array ofstring | An array of condition identifiers for the product.Occurrence:Conditional
merchandisedProducts.marketPriceDetails.estimatedStartPrice | Amount | The lowest priced active item for this product on eBay.Occurrence:Conditional
merchandisedProducts.marketPriceDetails.estimatedStartPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Conditional
merchandisedProducts.marketPriceDetails.estimatedStartPrice.value | string | The monetary amount, in the currency specified by thecurrencyfield.Occurrence:Conditional
merchandisedProducts.ratingAspects | array ofRatingAspect | An array of containers for ratings of the product aspects, such as "Is it a good value".Occurrence:Conditional
merchandisedProducts.ratingAspects.count | integer | The number of eBay users that rated the product on this aspect.Occurrence:Conditional
merchandisedProducts.ratingAspects.description | string | The name of the rating aspect. Camping tent examples: Is it lightweight? or Is it easy to set up?Occurrence:Conditional
merchandisedProducts.ratingAspects.name | string | The answer or value of the rating aspect. Camping tent examples: Lightweight or Easy to set upOccurrence:Conditional
merchandisedProducts.ratingAspects.ratingAspectDistributions | array ofRatingAspectDistribution | The container for the details of the aspect rating. The details show the aspect rating value, usually TRUE or FALSE and the user count and percentage.Occurrence:Conditional
merchandisedProducts.ratingAspects.ratingAspectDistributions.count | integer | The number of eBay users that choose this rating aspect value.Occurrence:Conditional
merchandisedProducts.ratingAspects.ratingAspectDistributions.percentage | string | The percentage of the aspect rating value.ratingAspectDistributions.percentage=ratingAspectDistributions.count/ratingAspects.countOccurrence:Conditional
merchandisedProducts.ratingAspects.ratingAspectDistributions.value | string | The rating aspect. For example: TRUE or FALSEOccurrence:Conditional
merchandisedProducts.ratingCount | integer | The total number of eBay users that rated the product.Occurrence:Conditional
merchandisedProducts.reviewCount | integer | The total number of eBay users that wrote a review for the product.Occurrence:Conditional
merchandisedProducts.title | string | The title of the product.Occurrence:Conditional
warnings | array ofErrorDetailV3 | The container with all the warnings for the input request.Occurrence:Conditional
warnings.category | string | This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.Occurrence:Always
warnings.domain | string | The name of the primary system where the error occurred. This is relevant for application errors.Occurrence:Always
warnings.errorId | integer | A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.Occurrence:Always
warnings.inputRefIds | array ofstring | An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.Occurrence:Conditional
warnings.longMessage | string | A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.Occurrence:Conditional
warnings.message | string | A description of the condition that caused the error or warning.Occurrence:Always
warnings.outputRefIds | array ofstring | An array of reference IDs that identify the specific response elements most closely associated to the error or warning, if any.Occurrence:Conditional
warnings.parameters | array ofErrorParameterV3 | An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.Occurrence:Conditional
warnings.parameters.name | string | This is the name of input field that caused an issue with the call request.Occurrence:Conditional
warnings.parameters.value | string | This is the actual value that was passed in for the element specified in thenamefield.Occurrence:Conditional
warnings.subdomain | string | The name of the subdomain in which the error or warning occurred.Occurrence:NA
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
70000 | API_MARKETING | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
70001 | API_MARKETING | REQUEST | A metric_name is required to make the API call.
70002 | API_MARKETING | REQUEST | The metric_name {metric_name} is invalid.
70003 | API_MARKETING | REQUEST | A categoryId is required to make the API call.
70004 | API_MARKETING | REQUEST | The category id {categoryId} is invalid
70005 | API_MARKETING | REQUEST | The 'limit' value should be between 1 and 100 (inclusive).
70006 | API_MARKETING | REQUEST | The 'limit' value must be an integer value.
70007 | API_MARKETING | BUSINESS | The marketplace value {marketplace} is not supported. The supported values are: {marketplaces}.
[/TABLE]