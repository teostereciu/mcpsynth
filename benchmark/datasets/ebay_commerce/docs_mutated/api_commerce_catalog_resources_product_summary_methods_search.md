# commerce/catalog/resources/product_summary/methods/search

*Source: https://developer.ebay.com/api-docs/commerce/catalog/resources/product_summary/methods/search*

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

### Sample 1: Search for Products by Keyword

### Sample 2: Search for Products by Category

### Sample 3: Search for Aspect Refinements Based on a Keyword

### Sample 4: Search for Products Based on a Keyword and Filtered by Aspect

### Sample 5: Search for Products Based on a GTIN

### Sample 6: Search for Products Based on an MPN

#### Thank you for helping us to improve the eBay developer program.
GET/product_summary/search
This method searches for and retrieves summaries of one or more products in the eBay catalog that match the search criteria provided by a seller. The seller can use the summaries to select the product in the eBay catalog that corresponds to the item that the seller wants to offer for sale. When a corresponding product is found and adopted by the seller, eBay will use the product information to populate the item listing. The criteria supported bysearchinclude keywords, product categories, and category aspects. To see the full details of a selected product, use thegetProductcall.In addition to product summaries, this method can also be used to identifyrefinements, which help you to better pinpoint the product you're looking for. A refinement consists of one or moreaspectvalues and a count of the number of times that each value has been used in previous eBay listings. An aspect is a property (e.g. color or size) of an eBay category, used by sellers to provide details about the items they're listing. Therefinementcontainer is returned when you include thefieldGroupsquery parameter in the request with a value ofASPECT_REFINEMENTSorFULL.ExampleA seller wants to find a product that is "gray" in color, but doesn't know what term the manufacturer uses for that color. It might beSilver,Brushed Nickel,Pewter, or evenGrey. The returnedrefinementcontainer identifies all aspects that have been used in past listings for products that match your search criteria, along with all of the values those aspects have taken, and the number of times each value was used. You can use this data to present the seller with a histogram of the values of each aspect. The seller can see which color values have been used in the past, and how frequently they have been used, and selects the most likely value or values for their product. You issue thesearchmethod again with those values in theaspect_filterparameter to narrow down the collection of products returned by the call.Although all query parameters are optional, this method must include at least theqparameter, or thecategory_ids,gtin, ormpnparameter with a valid value. If you provide more than one of these parameters, they will be combined with a logical AND to further refine the returned collection of matching products.Note:This method requires that certain special characters in the query parameters be percent-encoded:(space)=%20,=%2C:=%3A[=%5B]=%5D{=%7B|=%7C}=%7DThis requirement applies to all query parameter values. However, for readability, method examples and samples in this documentation will not use the encoding.This method returns product summaries rather than the full details of the products. To retrieve the full details of a product, use thegetProductmethod with an ePID.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Conditional
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly
SeeOAuth access tokensfor more information.
Note:Only thesell.inventoryscope is required for selling applications, and only thecommerce.catalog.readonlyscope is required for buying applications.
This call has no payload.
This call has no field definitions.
This call has no response headers.
This field is reserved for internal or future use.Occurrence:NA
Occurrence:NA
The number of product summaries returned in the response. This is theresult set, a subset of the full collection of products that match the search or filter criteria of this call. If thelimitquery parameter was included in the request, this field will have the same value.Default:50Occurrence:Always
Occurrence:Always
Returned ifthefieldGroupsquery parameter was omitted from the request, or if it was included with a value ofMATCHING_PRODUCTSorFULL. This container provides an array of product summaries in the current result set for products that match the combination of theq,category_id, andaspect_filterparameters that were provided in the request. Each product summary includes information about the product's identifiers, product images, aspects, the product page URL, and thegetProductURL for retrieving the product details.Occurrence:Conditional
Contains information about additional images associated with this product. For the primary image, see theimagecontainer.Occurrence:Conditional
The height of the image in pixels.Occurrence:Conditional
The eBay Picture Services (EPS) URL of the image.Occurrence:Always
The width of the image in pixels.Occurrence:Conditional
Contains an array of the category aspects and their values that are associated with this product.Occurrence:Conditional
The localized name of this category aspect.Occurrence:Conditional
A list of the localized values of this category aspect.Occurrence:Conditional
The manufacturer's brand name for this product.Occurrence:Conditional
A list of all European Article Numbers (EANs) that identify this product.Occurrence:Conditional
The eBay product ID of this product.Occurrence:Always
A list of all GTINs that identify this product. This includes all of the values returned in theean,isbn, andupcfields.Occurrence:Conditional
Contains information about the primary image of this product. For more images of this product, see theadditionalImagescontainer.Occurrence:Always
A list of all International Standard Book Numbers (ISBNs) that identify this product.Occurrence:Conditional
A list of all Manufacturer Product Number (MPN) values that the manufacturer uses to identify this product.Occurrence:Conditional
The URI of thegetProductcall request that retrieves this product's details.Occurrence:Always
The URL for this product's eBay product page.Occurrence:Conditional
The title of this product on eBay.Occurrence:Always
A list of Universal Product Codes (UPCs) that identify this product.Occurrence:Conditional
Returned only ifthefieldGroupsquery parameter was included in the request with a value ofASPECT_REFINEMENTSorFULL.An aspect is a property of a category, used by sellers to provide details about the items they're listing. For example, theCell Phones & Smartphonescategory (#9355) includes aStorage Capacityaspect.This container provides information about the distribution of values of a set of category aspects. The category aspects are those associated with the category that eBay determines is most likely to cover the products that match the search criteria.Occurrence:Conditional
Contains information about one or more aspects that are associated with the category identified bydominantCategoryId.Occurrence:Conditional
Contains information about one or more values of the category aspect identified bylocalizedAspectName.Occurrence:Conditional
The localized value of the category aspect identified byrefinement.aspectDistributions.localizedAspectName.Occurrence:Conditional
The number of times the value oflocalizedAspectValuehas been used for eBay product listings. By comparing this quantity to thematchCountfor other values of the same aspect, you can present a histogram of the values to sellers, who can use that information to select which aspect value is most appropriate for their product. You can then include the user-selected value in the thesearchcall'saspect_filterparameter to refine your search.Occurrence:Conditional
A HATEOAS reference that further refines the search with this particularlocalizedAspectValue.Occurrence:Conditional
The localized name of an aspect that is associated with the category identified bydominantCategoryId.Occurrence:Conditional
The ID of the category that eBay determines is most likely to cover the products matching the search criteria.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns a set of eBay products that match the keyword.
The inputs are the query parametersq, which is the keyword, andlimit.
      There is no payload with this request.
GEThttps://api.ebay.com/commerce/catalog/v1_beta/product_summary/search?query=drone&page_size=3
If the call is successful, 3 product summaries will be returned in the result set.
This sample returns a set of eBay products in theCell Phones & Smartphonescategory.
The input is thecategory_idsquery parameter.
      There is no payload with this request.
This call searches the catalog for theiphonekeyword. Based on the results of that search, it returns the aspect refinements for the dominant category (Cell Phones & Smartphones) of products that contain the keyword.
If the call is successful, all aspects that apply to the dominant category of the products identified by the keyword will be returned in the result set, with counts of all values of those aspects that have been used.
If the call is successful, 3 iPhone product summaries in the color Black will be returned in the result set.
This call searches the catalog for thegtinvalue of0813917020203. Based on the results of that search, it returns all product summaries of the product identified by the provided GTIN.
The input is thegtinquery parameter.
      There is no payload with this request.
GEThttp://api.ebay.com/commerce/catalog/v1_beta/product_summary/search?gtin=0813917020203
If the call is successful, the product summaries for the item identified by the specified GTIN (NEST thermostat model T3017US) will be returned in the result set.
This call searches the catalog for thempnvalue of3710RW. Based on the results of that search, it returns all product summaries of the product identified by the provided MPN.
The input is thempnquery parameter.
      There is no payload with this request.
Related topics
If you need help, contactDeveloper Technical Support.
- If the keywords are separated by a comma (e.g.iPhone,256GB), the query returns products that haveiPhoneAND256GB.
- If the keywords are separated by a space (e.g."iPhone ipad"or"iPhone, ipad"), the query ignores any commas and returns products that haveiPhoneORiPad.
- ASPECT_REFINEMENTS— This returns therefinementcontainer, which includes the category aspect and aspect value distributions that apply to the returned products. For example, if you searched forFord Mustang, some of the category aspects might beModel Year,Exterior Color,Vehicle Mileage, and so on.Note:Aspects are category specific.
- FULL— This returns all the refinement containers and all the matching products. This value overrides the other values, which will be ignored.
- MATCHING_PRODUCTS— This returns summaries for all products that match the values you provide for theqandcategory_idsparameters. This does not affect your use of theASPECT_REFINEMENTSvalue, which you can use in the same call.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
query | string | A string consisting of one or more keywords to use to search for products in the eBay catalog.Note:This method searches the following product record fields:title,description,brand, andaspects.localizedName, which do not include product IDs. Wildcard characters (e.g.*) are not allowed.The keywords are handled as follows:If the keywords are separated by a comma (e.g.iPhone,256GB), the query returns products that haveiPhoneAND256GB.If the keywords are separated by a space (e.g."iPhone ipad"or"iPhone, ipad"), the query ignores any commas and returns products that haveiPhoneORiPad.Note:Although all query parameters are optional, this method must include at least theqparameter, or thecategory_ids,gtin, ormpnparameter with a valid value.You cannot use theqparameter in the same method with either thegtinparameter or thempnparameter.Occurrence:Optional
gtin | array ofstring | A string consisting of one or more comma-separated Global Trade Item Numbers (GTINs) that identify products to search for. Currently the GTIN values can include EAN, ISBN, and UPC identifier types.Note:Although all query parameters are optional, this method must include at least theqparameter, or thecategory_ids,gtin, ormpnparameter with a valid value.You cannot use thegtinparameter in the same method with either theqparameter or theaspect_filterparameter.Occurrence:Optional
mpn | array ofstring | A string consisting of one or more comma-separated Manufacturer Part Numbers (MPNs) that identify products to search for. This method will return all products that have one of the specified MPNs.MPNs are defined by manufacturers for their own products, and are therefore certain to be unique only within a given brand. However, many MPNs do turn out to be globally unique.Note:Although all query parameters are optional, this method must include at least theqparameter, or thecategory_ids,gtin, ormpnparameter with a valid value.You cannot use thempnparameter in the same method with either theqparameter or theaspect_filterparameter.Occurrence:Optional
category_id | array ofstring | Important:Currently, only the firstcategory_idvalue is accepted.One or more comma-separated category identifiers for narrowing down the collection of products returned by this call.Note:This parameter requires a valid category ID value. You can use the Taxonomy API'sgetCategorySuggestionsmethod to retrieve appropriate category IDs for your product based on keywords.The syntax for this parameter is as follows:category_id=category_id1,category_id2,.Here is an example of a method with thecategory_idsparameter:GET https://api.ebay.com/commerce/catalog/v1_beta/product_summary/search?category_id=178893Note:Although all query parameters are optional, this method must include at least theqparameter, or thecategory_ids,gtin, ormpnparameter with a valid value.If you provide only thecategory_idsparameter, you cannot specify a top-level (L1) category.Occurrence:Optional
aspects | AspectFilter | An eBay category and one or more aspects of that category, with the values that can be used to narrow down the collection of products returned by this call.Aspects are product attributes that can represent different types of information for different products. Every product has aspects, but different products have different sets of aspects.You can determine appropriate values for the aspects by first submitting this method without this parameter. It will return either theproductSummaries.aspectscontainer, therefinement.aspectDistributionscontainer, or both, depending on the value of thefieldgroupsparameter in the request. TheproductSummaries.aspectscontainer provides the category aspects and their values that are associated with each returned product. Therefinement.aspectDistributionscontainer provides information about the distribution of values of the set of category aspects associated with the specified categories. In both cases sellers can select from among the returned aspects to use with this parameter.Note:You can also use the Taxonomy API'sgetItemAspectsForCategorymethod to retrieve detailed information about aspects and their values that are appropriate for your selected category.The syntax for theaspect_filterparameter is as follows (on several lines for readability;categoryIdis required):aspects=categoryId:category_id,aspect1:{valueA|valueB|...},aspect2:{valueC|valueD|...},.A matching product must be within the specified category, and it must have least one of the values identified for every specified aspect.Note:Aspect names and values are case sensitive.Here is an example of anaspect_filterparameter in which9355is the category ID,Coloris an aspect of that category, andBlackandWhiteare possible values of that aspect (on several lines for readability):GET https://api.ebay.com/commerce/catalog/v1_beta/product_summary/search?aspects=categoryId:9355,Color:{White|Black}Here is theaspect_filterwith required URL encoding and a second aspect (on several lines for readability):GET https://api.ebay.com/commerce/catalog/v1_beta/product_summary/search?aspects=categoryId:9355,Color:%7BWhite%7CBlack%7D,Storage%20Capacity:%128GB%7C256GB%7DNote:You cannot use theaspect_filterparameter in the same method with either thegtinparameter or thempnparameter.Occurrence:Optional
field_groups | array ofstring | The type of information to return in the response.Important:This parameter may not produce valid results if you also provide more than one value for thecategory_idsparameter. It is recommended that you avoid using this combination.Valid Values:ASPECT_REFINEMENTS— This returns therefinementcontainer, which includes the category aspect and aspect value distributions that apply to the returned products. For example, if you searched forFord Mustang, some of the category aspects might beModel Year,Exterior Color,Vehicle Mileage, and so on.Note:Aspects are category specific.FULL— This returns all the refinement containers and all the matching products. This value overrides the other values, which will be ignored.MATCHING_PRODUCTS— This returns summaries for all products that match the values you provide for theqandcategory_idsparameters. This does not affect your use of theASPECT_REFINEMENTSvalue, which you can use in the same call.Code so that your app gracefully handles any future changes to this list.Default:MATCHING_PRODUCTSOccurrence:Optional
page_size | string | The number of product summaries to return. This is theresult set, a subset of the full collection of products that match the search or filter criteria of this call.Maximum:200Default:50Occurrence:Optional
offset | string | This parameter is reserved for internal or future use.Occurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-MARKETPLACE-ID | string | This method also uses theX-EBAY-C-MARKETPLACE-IDheader to identify the seller's eBay marketplace. It is required for allsupported marketplaces, except EBAY_US, which is the default.Occurrence:Conditional
[/TABLE]

[TABLE]
Output container/field | Type | Description
href | string | This field is reserved for internal or future use.Occurrence:NA
page_size | integer | The number of product summaries returned in the response. This is theresult set, a subset of the full collection of products that match the search or filter criteria of this call. If thelimitquery parameter was included in the request, this field will have the same value.Default:50Occurrence:Always
next | string | This field is reserved for internal or future use.Occurrence:NA
offset | integer | This field is reserved for internal or future use.Occurrence:NA
prev | string | This field is reserved for internal or future use.Occurrence:NA
productSummaries | array ofProductSummary | Returned ifthefieldGroupsquery parameter was omitted from the request, or if it was included with a value ofMATCHING_PRODUCTSorFULL. This container provides an array of product summaries in the current result set for products that match the combination of theq,category_id, andaspect_filterparameters that were provided in the request. Each product summary includes information about the product's identifiers, product images, aspects, the product page URL, and thegetProductURL for retrieving the product details.Occurrence:Conditional
productSummaries.additionalImages | array ofImage | Contains information about additional images associated with this product. For the primary image, see theimagecontainer.Occurrence:Conditional
productSummaries.additionalImages.height | integer | The height of the image in pixels.Occurrence:Conditional
productSummaries.additionalImages.imageUrl | string | The eBay Picture Services (EPS) URL of the image.Occurrence:Always
productSummaries.additionalImages.width | integer | The width of the image in pixels.Occurrence:Conditional
productSummaries.aspects | array ofAspect | Contains an array of the category aspects and their values that are associated with this product.Occurrence:Conditional
productSummaries.aspects.localizedName | string | The localized name of this category aspect.Occurrence:Conditional
productSummaries.aspects.localizedValues | array ofstring | A list of the localized values of this category aspect.Occurrence:Conditional
productSummaries.brand | string | The manufacturer's brand name for this product.Occurrence:Conditional
productSummaries.ean | array ofstring | A list of all European Article Numbers (EANs) that identify this product.Occurrence:Conditional
productSummaries.epid | string | The eBay product ID of this product.Occurrence:Always
productSummaries.gtin | array ofstring | A list of all GTINs that identify this product. This includes all of the values returned in theean,isbn, andupcfields.Occurrence:Conditional
productSummaries.image | Image | Contains information about the primary image of this product. For more images of this product, see theadditionalImagescontainer.Occurrence:Always
productSummaries.image.height | integer | The height of the image in pixels.Occurrence:Conditional
productSummaries.image.imageUrl | string | The eBay Picture Services (EPS) URL of the image.Occurrence:Always
productSummaries.image.width | integer | The width of the image in pixels.Occurrence:Conditional
productSummaries.isbn | array ofstring | A list of all International Standard Book Numbers (ISBNs) that identify this product.Occurrence:Conditional
productSummaries.mpn | array ofstring | A list of all Manufacturer Product Number (MPN) values that the manufacturer uses to identify this product.Occurrence:Conditional
productSummaries.productHref | string | The URI of thegetProductcall request that retrieves this product's details.Occurrence:Always
productSummaries.productWebUrl | string | The URL for this product's eBay product page.Occurrence:Conditional
productSummaries.title | string | The title of this product on eBay.Occurrence:Always
productSummaries.upc | array ofstring | A list of Universal Product Codes (UPCs) that identify this product.Occurrence:Conditional
refinement | Refinement | Returned only ifthefieldGroupsquery parameter was included in the request with a value ofASPECT_REFINEMENTSorFULL.An aspect is a property of a category, used by sellers to provide details about the items they're listing. For example, theCell Phones & Smartphonescategory (#9355) includes aStorage Capacityaspect.This container provides information about the distribution of values of a set of category aspects. The category aspects are those associated with the category that eBay determines is most likely to cover the products that match the search criteria.Occurrence:Conditional
refinement.aspectDistributions | array ofAspectDistribution | Contains information about one or more aspects that are associated with the category identified bydominantCategoryId.Occurrence:Conditional
refinement.aspectDistributions.aspectValueDistributions | array ofAspectValueDistribution | Contains information about one or more values of the category aspect identified bylocalizedAspectName.Occurrence:Conditional
refinement.aspectDistributions.aspectValueDistributions.localizedAspectValue | string | The localized value of the category aspect identified byrefinement.aspectDistributions.localizedAspectName.Occurrence:Conditional
refinement.aspectDistributions.aspectValueDistributions.matchCount | integer | The number of times the value oflocalizedAspectValuehas been used for eBay product listings. By comparing this quantity to thematchCountfor other values of the same aspect, you can present a histogram of the values to sellers, who can use that information to select which aspect value is most appropriate for their product. You can then include the user-selected value in the thesearchcall'saspect_filterparameter to refine your search.Occurrence:Conditional
refinement.aspectDistributions.aspectValueDistributions.refinementHref | string | A HATEOAS reference that further refines the search with this particularlocalizedAspectValue.Occurrence:Conditional
refinement.aspectDistributions.localizedAspectName | string | The localized name of an aspect that is associated with the category identified bydominantCategoryId.Occurrence:Conditional
refinement.dominantCategoryId | string | The ID of the category that eBay determines is most likely to cover the products matching the search criteria.Occurrence:Conditional
total | integer | This field is reserved for internal or future use.Occurrence:NA
[/TABLE]

[TABLE]
200 | Success
204 | No Content
400 | Bad Request
403 | Forbidden
500 | Internal Server Error
[/TABLE]

[TABLE]
75000 | API_CATALOG | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
75001 | API_CATALOG | REQUEST | The call must have a valid 'query', or 'category_id' or 'gtin' or 'mpn' query parameter.
75004 | API_CATALOG | REQUEST | The 'page_size' value should be between 1 and 200 (inclusive).
75006 | API_CATALOG | REQUEST | Top level category browsing is not allowed. Please provide keywords or more filters for the applied top level category.
75007 | API_CATALOG | REQUEST | Currently, the {marketplaceId} marketplace is not supported. The supported Marketplaces are: {allowedMarketplaces} .
75008 | API_CATALOG | REQUEST | The 'field_groups' value {field_groups} is invalid. The supported field_groups are: {supportedFieldgroups}
75012 | API_CATALOG | REQUEST | The aspects format is invalid. For more information, see the API call reference documentation.
75013 | API_CATALOG | REQUEST | The 'aspects' query parameter must include a categoryId. For more information, see the API call reference documentation.
75014 | API_CATALOG | REQUEST | The categoryId in 'aspects' query parameter is invalid. For more information, see the API call reference documentation.
75015 | API_CATALOG | REQUEST | Insufficient permissions to fulfill the request.
75017 | API_CATALOG | REQUEST | The specified GTIN value is invalid.
75018 | API_CATALOG | REQUEST | The call must be made with either 'query' or 'gtin/mpn'.
75019 | API_CATALOG | REQUEST | The call with 'gtin/mpn' cannot be made with aspects.
[/TABLE]