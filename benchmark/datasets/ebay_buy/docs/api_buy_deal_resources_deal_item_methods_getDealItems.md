# buy/deal/resources/deal_item/methods/getDealItems

*Source: https://developer.ebay.com/api-docs/buy/deal/resources/deal_item/methods/getDealItems*

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

### Sample 1: Retrieve Deal Items for a Specified Marketplace

#### Thank you for helping us to improve the eBay developer program.
GET/deal_item
This method retrieves a paginated set of deal items. The result set contains all deal items associated with the specified search criteria and marketplace ID.RestrictionsThis method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, seeAPI Restrictions.eBay Partner Network:In order to receive a commission for your sales, you must use the URL returned in theitemAffiliateWebUrlfield to forward your buyer to the ebay.com site.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.deal
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
A list of deal items that match the search criteria.Occurrence:Conditional
Occurrence:Conditional
The additional images for the deal item.Occurrence:Conditional
The height of the image.Occurrence:Conditional
The relative path to the image location.Occurrence:Conditional
The text associated with the image.Occurrence:Conditional
The width of the image.Occurrence:Conditional
The IDs of the ancestors for the primary category.Occurrence:Conditional
The ID of the leaf category for the deal item. A leaf category is the lowest level in a category and has no children.Occurrence:Conditional
A boolean value specifying whether the listing has commission.Occurrence:Conditional
The deal associated with the item with affiliate attribution.Occurrence:Conditional
The date after which the deal ends.Occurrence:Conditional
The date on which the deal starts.Occurrence:Conditional
The web URL for the deal associated with the item.Occurrence:Conditional
A string value specifying the Energy Efficiency class.Occurrence:Conditional
The primary image for the deal item.Occurrence:Conditional
The item web URL with affiliate attribution.Occurrence:Conditional
The unique identifier for the deal item group. This is the parent item ID for the seller-defined variations.Note:This field is returned for multiple-SKU items.Occurrence:Conditional
An enumeration value that indicates the type of item group. An item group contains items that have various aspect differences, such as color, size, or storage capacity.Occurrence:Conditional
The unique identifier for the deal item.Note:This field is only returned for single-SKU items.Occurrence:Conditional
The web URL for the deal item.Occurrence:Conditional
The legacy item ID associated with the deal item.Occurrence:Always
Occurrence:Always
The original price for the deal item, and the discount amount and percentage.Occurrence:Conditional
The monetary value of the seller discount.Occurrence:Conditional
The three-letterISO 4217code representing the currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
The monetary value, in the currency specified by thecurrencyfield.Occurrence:Conditional
The percentage of the seller discount based on the value returned in theoriginalPricefield.Occurrence:Conditional
The monetary value of the item prior to the discount.Occurrence:Conditional
The pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects how and where the discounted price can be displayed.Occurrence:Conditional
The price for the deal item.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Conditional
A list of programs applicable to the item.Occurrence:Conditional
The cost required to ship the deal item.Note:For items with calculated shipping, this array is only returned if theX-EBAY-C-ENDUSERCTXheader is supplied.Occurrence:Conditional
The final shipping cost for all items after all discounts are applied.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The class of the shipping cost.Valid Values:FIXEDorCALCULATEDCode so that your app gracefully handles any future changes to this list.Occurrence:Always
The title of the deal item.Occurrence:Conditional
The price per unit for the deal item. Some European countries require listings for certain types of products to include the price per unit so that buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The designation used to specify the quantity of the deal item, such as size, weight, volume, and count. This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The relative path to the current set of results.Occurrence:Conditional
The maximum number of items, from the current result set, returned on a single page.Default:20Occurrence:Conditional
The relative path to the next set of results.Occurrence:Conditional
The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Default:0Occurrence:Conditional
The relative path to the previous set of results.Occurrence:Conditional
The total number of matches for the search criteria.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves a paginated set of deal items associated with the specified search criteria and marketplace ID.
The inputs are thecategory_idsandlimitURI parameters. There is no payload with this request.
GEThttps://api.ebay.com/buy/deal/v1/deal_item?category_ids=257818&limit=1
If the call is successful, one deal item matching the specified search criteria and marketplace will be returned.
Related topics
If you need help, contactDeveloper Technical Support.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
limit | string | The maximum number of items, from the current result set, returned on a single page.Occurrence:Optional
offset | string | The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Default:0Occurrence:Optional
category_ids | string | This query parameter specifies the unique identifier of the eBay category for the search.For details seeGet Categories for Buy APIs.Occurrence:Optional
commissionable | string | This query parameter allows the response to filter by commissionable items.If set totrue, only commissionable items will be returned in the response. If set tofalse, commissionable items willnotbe returned in the response.Note:This filter is currently only supported for the US marketplace.Occurrence:Optional
delivery_country | string | This query parameter allows the response to only return items that can be shipped to the specified country (2-digit ISO code).Occurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-ENDUSERCTX | string | This header is required to support revenue sharing for eBay Partner Network and to improve the accuracy of shipping and delivery time estimations.For additional information, refer toUse request headerssection of the Buying Integration Guide.Occurrence:Optional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the eBay marketplace.SeeHTTP request headersfor supported marketplace ID values.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
dealItems | array ofDealItem | A list of deal items that match the search criteria.Occurrence:Conditional
dealItems.additionalImages | array ofImage | The additional images for the deal item.Occurrence:Conditional
dealItems.additionalImages.height | string | The height of the image.Occurrence:Conditional
dealItems.additionalImages.imageUrl | string | The relative path to the image location.Occurrence:Conditional
dealItems.additionalImages.text | string | The text associated with the image.Occurrence:Conditional
dealItems.additionalImages.width | string | The width of the image.Occurrence:Conditional
dealItems.categoryAncestorIds | array ofstring | The IDs of the ancestors for the primary category.Occurrence:Conditional
dealItems.categoryId | string | The ID of the leaf category for the deal item. A leaf category is the lowest level in a category and has no children.Occurrence:Conditional
dealItems.commissionable | boolean | A boolean value specifying whether the listing has commission.Occurrence:Conditional
dealItems.dealAffiliateWebUrl | string | The deal associated with the item with affiliate attribution.Occurrence:Conditional
dealItems.dealEndDate | string | The date after which the deal ends.Occurrence:Conditional
dealItems.dealStartDate | string | The date on which the deal starts.Occurrence:Conditional
dealItems.dealWebUrl | string | The web URL for the deal associated with the item.Occurrence:Conditional
dealItems.energyEfficiencyClass | string | A string value specifying the Energy Efficiency class.Occurrence:Conditional
dealItems.image | Image | The primary image for the deal item.Occurrence:Conditional
dealItems.image.height | string | The height of the image.Occurrence:Conditional
dealItems.image.imageUrl | string | The relative path to the image location.Occurrence:Conditional
dealItems.image.text | string | The text associated with the image.Occurrence:Conditional
dealItems.image.width | string | The width of the image.Occurrence:Conditional
dealItems.itemAffiliateWebUrl | string | The item web URL with affiliate attribution.Occurrence:Conditional
dealItems.itemGroupId | string | The unique identifier for the deal item group. This is the parent item ID for the seller-defined variations.Note:This field is returned for multiple-SKU items.Occurrence:Conditional
dealItems.itemGroupType | ItemGroupTypeEnum | An enumeration value that indicates the type of item group. An item group contains items that have various aspect differences, such as color, size, or storage capacity.Occurrence:Conditional
dealItems.itemId | string | The unique identifier for the deal item.Note:This field is only returned for single-SKU items.Occurrence:Conditional
dealItems.itemWebUrl | string | The web URL for the deal item.Occurrence:Conditional
dealItems.legacyItemId | string | The legacy item ID associated with the deal item.Occurrence:Always
dealItems.marketingPrice | MarketingPrice | The original price for the deal item, and the discount amount and percentage.Occurrence:Conditional
dealItems.marketingPrice.discountAmount | Amount | The monetary value of the seller discount.Occurrence:Conditional
dealItems.marketingPrice.discountAmount.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
dealItems.marketingPrice.discountAmount.value | string | The monetary value, in the currency specified by thecurrencyfield.Occurrence:Conditional
dealItems.marketingPrice.discountPercentage | string | The percentage of the seller discount based on the value returned in theoriginalPricefield.Occurrence:Conditional
dealItems.marketingPrice.originalPrice | Amount | The monetary value of the item prior to the discount.Occurrence:Conditional
dealItems.marketingPrice.originalPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
dealItems.marketingPrice.originalPrice.value | string | The monetary value, in the currency specified by thecurrencyfield.Occurrence:Conditional
dealItems.marketingPrice.priceTreatment | PriceTreatmentEnum | The pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects how and where the discounted price can be displayed.Occurrence:Conditional
dealItems.price | Amount | The price for the deal item.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Conditional
dealItems.price.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
dealItems.price.value | string | The monetary value, in the currency specified by thecurrencyfield.Occurrence:Conditional
dealItems.qualifiedPrograms | array ofProgramEnum | A list of programs applicable to the item.Occurrence:Conditional
dealItems.shippingOptions | array ofShippingOption | The cost required to ship the deal item.Note:For items with calculated shipping, this array is only returned if theX-EBAY-C-ENDUSERCTXheader is supplied.Occurrence:Conditional
dealItems.shippingOptions.shippingCost | Amount | The final shipping cost for all items after all discounts are applied.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
dealItems.shippingOptions.shippingCost.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
dealItems.shippingOptions.shippingCost.value | string | The monetary value, in the currency specified by thecurrencyfield.Occurrence:Conditional
dealItems.shippingOptions.shippingCostType | string | The class of the shipping cost.Valid Values:FIXEDorCALCULATEDCode so that your app gracefully handles any future changes to this list.Occurrence:Always
dealItems.title | string | The title of the deal item.Occurrence:Conditional
dealItems.unitPrice | Amount | The price per unit for the deal item. Some European countries require listings for certain types of products to include the price per unit so that buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
dealItems.unitPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
dealItems.unitPrice.value | string | The monetary value, in the currency specified by thecurrencyfield.Occurrence:Conditional
dealItems.unitPricingMeasure | string | The designation used to specify the quantity of the deal item, such as size, weight, volume, and count. This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
href | string | The relative path to the current set of results.Occurrence:Conditional
limit | integer | The maximum number of items, from the current result set, returned on a single page.Default:20Occurrence:Conditional
next | string | The relative path to the next set of results.Occurrence:Conditional
offset | integer | The number of items that will be skipped in the result set. This is used with thelimitfield to control the pagination of the output.For example, if theoffsetis set to0and thelimitis set to10, the method will retrieve items 1 through 10 from the list of items returned. If theoffsetis set to10and thelimitis set to10, the method will retrieve items 11 through 20 from the list of items returned.Default:0Occurrence:Conditional
prev | string | The relative path to the previous set of results.Occurrence:Conditional
total | integer | The total number of matches for the search criteria.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
403 | Forbidden
500 | Internal Server Error
[/TABLE]

[TABLE]
180000 | API_DEAL | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
180001 | API_DEAL | REQUEST | Invalid, missing or unsupported marketplace. Please refer to documentation.
180002 | API_DEAL | REQUEST | The specified limit is invalid. Maximum value supported is 100.
180003 | API_DEAL | REQUEST | The specified offset is invalid.
180005 | API_DEAL | REQUEST | category_ids length exceeded. Please check documentation for maximum values supported.
180007 | API_DEAL | REQUEST | Invalid or unsupported filter 'commissionable' for the requested marketplace. Please refer to documentation.
180009 | API_DEAL | REQUEST | Not authorized. Please contact developer support for assistance.
180010 | API_DEAL | REQUEST | Invalid filter for 'delivery_country'. Please refer to the documentation for supported values.
[/TABLE]