# commerce/catalog/resources/product/methods/getProduct

*Source: https://developer.ebay.com/api-docs/commerce/catalog/resources/product/methods/getProduct*

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

### Sample 1: Get Product Details

#### Thank you for helping us to improve the eBay developer program.
GET/product/{epid}
This method retrieves details of the catalog product identified by the eBay product identifier (ePID) specified in the request. These details include the product's title and description, aspects and their values, associated images, applicable category IDs, and any recognized identifiers that apply to the product.For a new listing, you can use thesearchmethod to identify candidate products on which to base the listing, then use thegetProductmethod to present the full details of those candidate products to the seller to make a a final selection.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
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
Contains information about  additional images associated with this product. For the primary image, see theimagecontainer.Occurrence:Conditional
The height of the image in pixels.Occurrence:Conditional
The eBay Picture Services (EPS) URL of the image.Occurrence:Always
Occurrence:Always
The width of the image in pixels.Occurrence:Conditional
Contains an array of the category aspects and their values that are associated with this product.Occurrence:Conditional
The localized name of this category aspect.Occurrence:Conditional
A list of the localized values of this category aspect.Occurrence:Conditional
The manufacturer's brand name for this product.Occurrence:Conditional
The number of distinct motor vehicles that are compatible with the product.This field is only applicable for and will only be returned for Parts & Accessory products on the eBay US Motors marketplace.Occurrence:Conditional
The rich description of this product, which might contain HTML.Occurrence:Always
A list of all European Article Numbers (EANs) that identify this product.Occurrence:Conditional
The eBay product ID of this product.Occurrence:Always
A list of all GTINs that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.Occurrence:Conditional
Contains information about the primary image of this product. For more images of this product, see theadditionalImagescontainer.Occurrence:Always
A list of all International Standard Book Numbers (ISBNs) that identify this product.Occurrence:Conditional
A list of all MPN values that the manufacturer uses to identify this product.Occurrence:Conditional
A list of category IDs (other than the value ofprimaryCategoryId) for all the leaf categories to which this product might belong.Occurrence:Conditional
The identifier of the leaf category that eBay recommends using to list this product, based on previous listings of similar products. Products in the eBay catalog are not automatically associated with any particular category, but using an inappropriate category can make it difficult for prospective buyers to find the product. For other possible categories that might be used, seeotherApplicableCategoryIds.Occurrence:Always
The URL for this product's eBay product page.Occurrence:Conditional
The title of this product on eBay.Occurrence:Always
A list of Universal Product Codes (UPCs) that identify this product.Occurrence:Conditional
The current version number of this product record in the catalog.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns the details of the specified product by passing in the ePID of the product. The ePID was returned by thesearchcall in theproductSummaries.epidfield. You can also use the URI that was returned in thesearchcall'sproductSummaries.productHreffield.
The input is theepidURI parameter, which specifies the ePID of the product. There is no payload with this request.
GEThttps://api.ebay.com/commerce/catalog/v1_beta/product/232669172
The details are returned for the corresponding product titled "Apple iPhone 7 - 32GB - Black (Unlocked) A1660 (CDMA + GSM)." It also has aspects that are returned in theaspectscontainer.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
epid | string | The eBay product identifier (ePID) of the product being requested. This value can be discovered by issuing thesearchmethod and examining the value of theproductSummaries.epidfield for the desired returned product summary.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-MARKETPLACE-ID | string | This method also uses theX-EBAY-C-MARKETPLACE-IDheader to identify the seller's eBay marketplace. It is required for allsupported marketplaces, except EBAY_US, which is the default.Occurrence:Conditional
[/TABLE]

[TABLE]
Output container/field | Type | Description
additionalImages | array ofImage | Contains information about  additional images associated with this product. For the primary image, see theimagecontainer.Occurrence:Conditional
additionalImages.height | integer | The height of the image in pixels.Occurrence:Conditional
additionalImages.imageUrl | string | The eBay Picture Services (EPS) URL of the image.Occurrence:Always
additionalImages.width | integer | The width of the image in pixels.Occurrence:Conditional
aspects | array ofAspect | Contains an array of the category aspects and their values that are associated with this product.Occurrence:Conditional
aspects.localizedName | string | The localized name of this category aspect.Occurrence:Conditional
aspects.localizedValues | array ofstring | A list of the localized values of this category aspect.Occurrence:Conditional
brand | string | The manufacturer's brand name for this product.Occurrence:Conditional
compatibilityCount | integer | The number of distinct motor vehicles that are compatible with the product.This field is only applicable for and will only be returned for Parts & Accessory products on the eBay US Motors marketplace.Occurrence:Conditional
description | string | The rich description of this product, which might contain HTML.Occurrence:Always
ean | array ofstring | A list of all European Article Numbers (EANs) that identify this product.Occurrence:Conditional
epid | string | The eBay product ID of this product.Occurrence:Always
gtin | array ofstring | A list of all GTINs that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.Occurrence:Conditional
image | Image | Contains information about the primary image of this product. For more images of this product, see theadditionalImagescontainer.Occurrence:Always
image.height | integer | The height of the image in pixels.Occurrence:Conditional
image.imageUrl | string | The eBay Picture Services (EPS) URL of the image.Occurrence:Always
image.width | integer | The width of the image in pixels.Occurrence:Conditional
isbn | array ofstring | A list of all International Standard Book Numbers (ISBNs) that identify this product.Occurrence:Conditional
mpn | array ofstring | A list of all MPN values that the manufacturer uses to identify this product.Occurrence:Conditional
otherApplicableCategoryIds | array ofstring | A list of category IDs (other than the value ofprimaryCategoryId) for all the leaf categories to which this product might belong.Occurrence:Conditional
primaryCategoryId | string | The identifier of the leaf category that eBay recommends using to list this product, based on previous listings of similar products. Products in the eBay catalog are not automatically associated with any particular category, but using an inappropriate category can make it difficult for prospective buyers to find the product. For other possible categories that might be used, seeotherApplicableCategoryIds.Occurrence:Always
productWebUrl | string | The URL for this product's eBay product page.Occurrence:Conditional
title | string | The title of this product on eBay.Occurrence:Always
upc | array ofstring | A list of Universal Product Codes (UPCs) that identify this product.Occurrence:Conditional
version | string | The current version number of this product record in the catalog.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
75000 | API_CATALOG | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
75007 | API_CATALOG | REQUEST | Currently, the {marketplaceId} marketplace is not supported. The supported Marketplaces are: {allowedMarketplaces}.
75010 | API_CATALOG | REQUEST | The specified EPID value {epid} was not found.
75011 | API_CATALOG | REQUEST | The specified EPID value {epid} no longer exists. Its new value is {newepid}.
75015 | API_CATALOG | REQUEST | Insufficient permissions to fulfill the request.
75016 | API_CATALOG | REQUEST | The specified EPID value {epid} is no longer available.
[/TABLE]