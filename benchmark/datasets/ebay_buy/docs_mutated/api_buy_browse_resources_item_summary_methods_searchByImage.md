# buy/browse/resources/item_summary/methods/searchByImage

*Source: https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/searchByImage*

---

### URL Encoding for Parameters

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

### Sample 1: Search for Items by Image

#### Thank you for helping us to improve the eBay developer program.
POST/item_summary/search_by_image
This method searches for eBay items based on a image and retrieves summaries of the items. You pass in a Base64 image in the request payload and can refine the search by category, or with other available filters.To get the Base64 image string, you can use sites such ashttps://codebeautify.org/image-to-base64-converter.This method also supports the following:Filtering by the value of one or multiple fields, such as listing format, item condition, price range, location, and more. For the fields supported by this method, refer to thefilterparameter.Filtering by item aspects using theaspect_filterparameter.For details and examples of these capabilities, refer toBrowse APIin the Buying Integration Guide.URL Encoding for ParametersQuery parameter values need to be URL encoded. For details, refer toURL encoding query parameter values. For readability, code examples in this document have not been URL encoded.RestrictionsThis method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, refer toAPI Restrictions.eBay Partner Network:In order to receive a commission for your sales, you must use the URL returned in theitemAffiliateWebUrlfield to forward your buyer to the ebay.com site.
This method is not supported in Sandbox environment.
Important!The value to be passed in ascharity_idsis that returned in theregistrationIdfield.
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
Occurrence:Conditional
Occurrence:Strongly Recommended
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
The Base64 string of the image.To get the Base64 image string, you can use sites such ashttps://codebeautify.org/image-to-base64-converter.Occurrence:Required
This call has no response headers.
The auto-corrected inputs.Occurrence:Conditional
The automatically spell-corrected keyword from the request.Occurrence:Conditional
The URI of the current page of results.The following example of thesearchmethod returns items 1 thru 5 from the list of items found.https://api.ebay.com/buy/v1/item_summary/search?q=shirt&max_results=5&skip=0Occurrence:Always
Occurrence:Always
An array of the items on this page. The items are sorted according to the sorting method specified in the request.Occurrence:Conditional
An array of containers with the URLs for the images that are in addition to the primary image. The primary image is returned in theimage.imageUrlfield.Occurrence:Conditional
Reserved for future use.Occurrence:Conditional
The URL of the image.Occurrence:Conditional
This indicates if the item is for adults only. For more information about adult-only items on eBay, refer to theAdult items policy.Occurrence:Conditional
This boolean attribute indicates if coupons are available for the item.Note:The Browse API only acknowledges item-level coupons. This field will only be returned as true if a coupon is linked with an item. It does not recognize store-level coupons offered by sellers across their entire store.Occurrence:Conditional
This integer value indicates the total number of bids that have been placed for an auction item. This field is only returned for auction items.Occurrence:Conditional
A comma separated list of all the purchase options available for the item.Values Returned:FIXED_PRICEIndicates the buyer can purchase the item for a set price using theBuy It Nowbutton.AUCTIONIndicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.BEST_OFFERItems where the buyer can send the seller a price they are willing to pay for the item. The seller can accept, reject, or send a counter offer. For additional information about Best Offer, refer toAdding Best Offer to your listing and sending offers to buyers.CLASSIFIED_ADIndicates that the final sales transaction is to be completed outside of the eBay environment.Occurrence:Conditional
This array returns the name and ID of each category associated with the item, including top level, branch, and leaf categories.Occurrence:Conditional
The unique identifier of the category.Occurrence:Conditional
The name of the category.Occurrence:Conditional
This indicates how well an item matches thecompatibility_filterproduct attributes.Valid Values:EXACTPOSSIBLEOccurrence:Conditional
This container returns only the product attributes that are compatible with the item. These attributes were specified in thecompatibility_filterin the request. This means that if you passed in 5 attributes and only 4 are compatible, only those 4 are returned. If none of the attributes are compatible, this container is not returned.Occurrence:Conditional
The name of the product attribute that as been translated to the language of the site.Occurrence:Conditional
The name of the product attribute, such as Make, Model, Year, etc.Occurrence:Conditional
The value for thenameattribute, such asBMW,R1200GS,2011, etc.Occurrence:Conditional
The text describing the condition of the item, such asNeworUsed. For a list of condition names, refer toItem Condition IDs and Names.Occurrence:Conditional
The identifier of the condition of the item. For example,1000is the identifier forNEW. For a list of condition names and IDs, refer toItem Condition IDs and Names.Occurrence:Conditional
This container returns the current highest bid for an auction item. Thevaluefield shows the dollar value of the current highest bid, and thecurrencyfield (3-digit ISO code) denotes the currency associated with that bid value. This field is only returned for auction items.Occurrence:Conditional
The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
This container returns the distance away that the item is from thepickupPostalCodevalue that was supplied in the method request. This container is only returned if the "local pickup" search_filter fields are used in the request.Occurrence:Conditional
This value shows the unit of measurement used to measure the distance between the location of the item and the buyer's location. This value is typicallymiorkm.Occurrence:Conditional
This value indicates the distance (measured in the measurement unit in theunitOfMeasurefield) between the item location and the buyer's location.Occurrence:Conditional
This indicates theEuropean energy efficiencyrating (EEK) of the item. Energy efficiency ratings apply to products listed by commercial vendors in electronics categories only.Currently, this field is only applicable for the Germany site, and is returned only if the seller specifies the energy efficiency rating through item specifics at listing time. Rating values includeA+++,A++,A+,A,B,C,D,E,F, andG.Occurrence:Conditional
An ePID is the eBay product identifier of a product from the eBay product catalog.  This indicates the product in which the item belongs.Occurrence:Conditional
The URL to the primary image of the item.Occurrence:Conditional
The URL to the View Item page of the item which includes the affiliate tracking ID.Note:In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.TheitemAffiliateWebUrlis returned only if:The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.Occurrence:Conditional
The date and time when the item listing was created. This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.This field is always returned withitemSummaries.Occurrence:Conditional
A timestamp that indicates the date and time a listing is scheduled to end.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Note:This field is returned only for item groups.Occurrence:Conditional
The indicates the item group type. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Currently only theSELLER_DEFINED_VARIATIONSis supported and indicates this is an item group created by the seller.Note:This field is returned only for item groups.Occurrence:Conditional
The URI for the Browse APIgetItemmethod, which can be used to retrieve more details about items in the search results.Occurrence:Conditional
The unique RESTful identifier of the item.Occurrence:Conditional
This container returns the location of the item. This container consists of fields you typically see for an address, including postal code, county, state/province, street address, city, and country (2-digit ISO code).Occurrence:Conditional
The first line of the street address.Occurrence:Conditional
The second line of the street address. This field may contain such values as an apartment or suite number.Occurrence:Conditional
The city in which the item is located.Restriction:This field is populated in thesearchmethod responseonlywhenfieldgroups=EXTENDED.Occurrence:Conditional
The two-letterISO 3166standard code that indicates the country in which the item is located.Occurrence:Conditional
The county in which the item is located.Occurrence:Conditional
The postal code (or zip code in US) where the item is located. Sellers set a postal code for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned initemLocation.postalCodevia the API.Occurrence:Conditional
The state or province in which the item is located.Occurrence:Conditional
The date and time when the listing was first made available. This date will be retained if an item is relisted. This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.This timestamp is used to order_by the response when thesort=newlyListedparameter is used.This field is always returned withitemSummaries.Occurrence:Conditional
The URL to the View Item page of the item. This enables you to include a "Report Item on eBay" hyperlink that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.Occurrence:Conditional
The leaf category IDs of the item. When the item belongs to two leaf categories, the ID values are returned in the order primary, secondary.Occurrence:Conditional
The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Conditional
The ID of the eBay marketplace on which the seller listed the item.Occurrence:Conditional
This container is returned if the item is eligible for a seller discount and contains the item's original price, and the seller discount amount and percentage.Occurrence:Conditional
This container returns the monetary amount of the seller discount.Occurrence:Conditional
This field expresses the percentage of the seller discount based on the value in theoriginalPricecontainer.Occurrence:Conditional
Indicates the pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects the way and where the discounted price can be displayed.Occurrence:Conditional
This container returns the local pickup options available to the buyer. This container is returned only if the user is searching for local pickup items and set the local pickup filters in the method request.Occurrence:Conditional
The price of the item after it has been converted into another currency.The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must do one or more of the following to view VAT-inclusive pricing:Pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB)Pass thecontextualLocationvalues for the supported marketplace in theX-EBAY-C-ENDUSERCTXrequest headerSpecify the supported marketplace using thedeliveryCountryfilterURI parameter (such asfilter=deliveryCountry:GB)Note:For more information on VAT, refer toYour VAT Obligations in the UK & EU.Occurrence:Conditional
Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.Occurrence:Conditional
This field is returned astrueif the listing is part of a Promoted Listing campaign. Promoted Listings are available toAbove StandardandTop Ratedsellers with recent sales activity.Note:Priority Listing is returned only with a Best Match order_by and will not be returned for other order_by options.Occurrence:Conditional
An array of the qualified programs available for the item, such asEBAY_PLUS,AUTHENTICITY_GUARANTEE, andAUTHENTICITY_VERIFICATION.eBay Plus is a premium account option for buyers, which provides benefits such as fast, free domestic shipping and free returns on selected items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings. Sellers must commit to next-day delivery of those items.Note:eBay Plus is only available as a listing feature on the eBay Australia marketplace.The eBayAuthenticity Guaranteeprogram enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.Occurrence:Conditional
This container returns basic information about the seller of the item, such as name, feedback score, etc.Occurrence:Conditional
The percentage of the total positive feedback.Occurrence:Conditional
The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Conditional
Indicates if the seller is a business or an individual. This is determined when the seller registers with eBay:If they register for a business account, this value will beBUSINESS.If they register for a private account, this value will beINDIVIDUAL.This designation is required by the tax laws in some countries.This field is returned only on the following sites:EBAY_AT, EBAY_BE, EBAY_CH, EBAY_DE, EBAY_ES, EBAY_FR, EBAY_GB, EBAY_IE, EBAY_IT, EBAY_PLValid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
The user name created by the seller for use on eBay.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Conditional
This container returns the shipping options available to ship the item.Occurrence:Conditional
Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.Occurrence:Conditional
The end date of the delivery window (latest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header.Note:Estimated delivery dates are not returned for CBT items.Occurrence:Conditional
The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header.Note:Estimated delivery dates are not returned for CBT items.Occurrence:Conditional
This is the estimated price to ship the item.The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must do one or more of the following to see VAT-inclusive pricing:Pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB)Pass thecontextualLocationvalues for the supported marketplace in theX-EBAY-C-ENDUSERCTXrequest headerSpecify the supported marketplace using thedeliveryCountryfilterURI parameter (such asfilter=deliveryCountry:GB)Note:For more information on VAT, refer toYour VAT Obligations in the UK & EU.Occurrence:Conditional
Indicates the type of shipping used to ship the item. Possible values areFIXED(flat-rate shipping) andCALCULATED(shipping cost calculated based on item and buyer location).Occurrence:Conditional
This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.) Sometimes the title does not provide enough information but the description is too big. Surfacing theshortDescriptioncan often provide buyers with the additional information that could help them make a buying decision.For example:"title": "Petrel U42W FPV Drone RC Quadcopter w/HD Camera Live Video One Key Off / Landing","shortDescription": "1 U42W Quadcopter. Syma X5SW-V3 Wifi FPV RC Drone Quadcopter 2.4Ghz 6-Axis Gyro with Headless Mode. Syma X20 Pocket Drone 2.4Ghz Mini RC Quadcopter Headless Mode Altitude Hold. One Key Take Off / Landing function: allow beginner to easy to fly the drone without any skill.",Restriction:This field is returned by thesearchmethod only whenfieldgroups=EXTENDED.Occurrence:Conditional
An array of thumbnail images for the item.Occurrence:Conditional
The seller-created title of the item.Maximum Length:80 charactersOccurrence:Conditional
This indicates if the item is a top-rated plus item. There are three benefits of a top-rated plus item: a  minimum 30-day money-back return policy; shipping the item in 1 business day with tracking provided; and the added comfort of knowing that this item is from an experienced seller with the highest buyer ratings. For more information, refer toLook for Top Rated Plus ItemsandSeller performance overview.Occurrence:Conditional
The URL to the image that shows the information on the tyre label.Occurrence:Conditional
The price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item. This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The number of users that have added the item to their watch list.Note:This field is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields indicating that you want access to Watch Count data in the Browse API.Occurrence:Conditional
The value of thelimitparameter submitted in the request, which is the maximum number of items to return on a page, from the result set. A result set is the complete set of items returned by the method.Occurrence:Always
The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set.The following example of thesearchmethod returns items 5 thru 10 from the list of items found.https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&max_results=5&skip=10Occurrence:Conditional
This value indicates theoffsetused for current page of items being returned. Assume the initial request used anoffsetof0and alimitof3. Then in the first page of results, this value would be0, and items 1-3 are returned. For the second page, this value is3and so on.Occurrence:Always
The URI for the previous page of results. This is returned if there is a previous page of results from the result set.The following example of thesearchmethod returns items 1 thru 5 from the list of items found, which would be the first set of items returned.https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&max_results=5&skip=0Occurrence:Conditional
The container for all the search refinements.Occurrence:Conditional
An array of containers for the all the aspect refinements.Occurrence:Conditional
An array of containers for the various values of the aspect and the match count, and a HATEOAS reference (refinementHref) for this aspect.Occurrence:Conditional
The value of an aspect. For example, Red is a value for the aspect Color.Occurrence:Always
The number of items with this aspect.Occurrence:Always
A HATEOAS reference for this aspect.Occurrence:Always
The name of an aspect, such asBrand,Color, etc.Occurrence:Conditional
An array of containers for the all the buying option refinements.Occurrence:Conditional
The container that returns the buying option type. This will be AUCTION, FIXED_PRICE, CLASSIFIED_AD, or a combination of these options. For details, seebuyingOptions.Occurrence:Always
The number of items having this buying option.Occurrence:Always
The HATEOAS reference for this buying option.Occurrence:Always
An array of containers for the all the category refinements.Occurrence:Conditional
The unique identifier of the category.Occurrence:Always
The name of the category, such asBaby & Toddler Clothing.Occurrence:Always
The number of items in this category.Occurrence:Always
The HATEOAS reference of this category.Occurrence:Always
An array of containers for the all the condition refinements.Occurrence:Conditional
The identifier of the condition. For example,1000is the identifier forNEW.Occurrence:Conditional
The number of items having the condition.Occurrence:Always
The HATEOAS reference of this condition.Occurrence:Always
The identifier of the category that most of the items are part of.Occurrence:Always
The total number of items that match the input criteria.Note:totalis just an indicator of the number of listings for a given query. It could vary based on the number of listings with variations included in the result. It is strongly recommended thattotalnot be used in pagination use cases. Instead, usenextto determine the results on the next page.Occurrence:Always
The container with all the warnings for the request.Occurrence:Conditional
This string value indicates the error category. There are three categories of errors:request errors,application errors, andsystem errors.Occurrence:Always
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
For more on warnings, plus the codes of other common warnings, seeHandling errors.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call searches for items using an image ID.
The Base64 ID of an image, which in this case is an image of a drill, in the request payload. There are no URI parameters required.
POSThttps://api.ebay.com/buy/browse/v1/item_summary/search_by_image?&max_results=3&order_by=-price
This call returns items that are similar to the image ID submitted order_by by price from smallest to largest.
Related topics
If you need help, contactDeveloper Technical Support.

```
/buy/browse/v1/item_summary/search?charity_ids=13-1788491,300108469
```

```
/buy/browse/v1/item_summary/searchByImage?category_ids=29792
```

```
/buy/browse/v1/item_summary/searchByImage?q=keyword&fieldgroups=ASPECT_REFINEMENTS
```

```
/buy/browse/v1/item_summary/search?q=shirt&search_filter=price:[10..50]
```

```
/buy/browse/v1/item_summary/search?q=shirt&category_ids=15724&aspect_filter=categoryId:15724,Color:{Red}
```

```
/buy/browse/v1/item_summary/search?q=shirt&fieldgroups=ASPECT_REFINEMENTS
```

```
/buy/browse/v1/item_summary/search?max_results=50&category_ids=3034&search_filter=buyingOptions:{AUCTION|FIXED_PRICE}&aspect_filter=categoryId:3034,Brand:{Bed\|Stü|Nike}
```

```
https://api.ebay.com/buy/v1/item_summary/search?q=shirt&max_results=5&skip=0
```

```
"title": "Petrel U42W FPV Drone RC Quadcopter w/HD Camera Live Video One Key Off / Landing","shortDescription": "1 U42W Quadcopter. Syma X5SW-V3 Wifi FPV RC Drone Quadcopter 2.4Ghz 6-Axis Gyro with Headless Mode. Syma X20 Pocket Drone 2.4Ghz Mini RC Quadcopter Headless Mode Altitude Hold. One Key Take Off / Landing function: allow beginner to easy to fly the drone without any skill.",
```

```
"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"
```

```
https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&max_results=5&skip=10
```
- Filtering by the value of one or multiple fields, such as listing format, item condition, price range, location, and more. For the fields supported by this method, refer to thefilterparameter.
- Filtering by item aspects using theaspect_filterparameter.
- In the US, this is theEmployer Identification Number (EIN).
- In the UK, this is the Charity Registration Number (CRN), commonly calledCharity Number.
- Search for a supported charity using the Charity API'sgetCharityOrgsmethod.Important!The value to be passed in ascharity_idsis that returned in theregistrationIdfield.
- Search for a supported charity by visitingCharity Search. Click on the charity's name to display its information. The EIN number is included in the charity's information block at the top of the page.For example, the charity ID forAmerican Red Cross, is530196605.
- ASPECT_REFINEMENTSThis field group adds theaspectDistributionscontainer to the response.Note:Information returned byASPECT_REFINEMENTSis category specific.
- BUYING_OPTION_REFINEMENTSThis field group adds thebuyingOptionDistributionscontainer to the response.
- CATEGORY_REFINEMENTSThis field group adds thecategoryDistributionscontainer to the response.
- CONDITION_REFINEMENTSThis field group adds theconditionDistributionscontainers, such asNEW,USED, etc., to the response. Within these groups are multiple states of the condition.For example,NEWcan beNew without tag,New in box,New without box, etc.
- EXTENDEDThis field group adds the following fields to the response:shortDescriptionitemLocation.city
- MATCHING_ITEMS(default value)This field group is intended to be used with one or more of the refinement values listed above. This is used to return the specified refinements and all matching items.
- FULLThis field group returns all refinement containers and all matching items.
- shortDescription
- itemLocation.city
- Visiting theCategory Changes page
- Using the Taxonomy API. Refer toGet Categories for Buy APIsfor complete information.
- Issuing the following call to retrieve thedominantCategoryIdfor an item:/buy/browse/v1/item_summary/searchByImage?q=keyword&fieldgroups=ASPECT_REFINEMENTS
- Ifoffsetis 0 andlimitis 10, the method will retrieve items 1-10 from the list of items returned
- Ifoffsetis 10 andlimitis 10, the method will retrieve items 11-20 from the list of items returned.
- Once as a URI parameter in thecategory_idsfield
- Once as part of theaspect_filterfield
- When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.
- When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.
- FIXED_PRICEIndicates the buyer can purchase the item for a set price using theBuy It Nowbutton.
- AUCTIONIndicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.
- BEST_OFFERItems where the buyer can send the seller a price they are willing to pay for the item. The seller can accept, reject, or send a counter offer. For additional information about Best Offer, refer toAdding Best Offer to your listing and sending offers to buyers.
- CLASSIFIED_ADIndicates that the final sales transaction is to be completed outside of the eBay environment.
- EXACT
- POSSIBLE
- The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.
- The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.
- Pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB)
- Pass thecontextualLocationvalues for the supported marketplace in theX-EBAY-C-ENDUSERCTXrequest header
- Specify the supported marketplace using thedeliveryCountryfilterURI parameter (such asfilter=deliveryCountry:GB)
- If they register for a business account, this value will beBUSINESS.
- If they register for a private account, this value will beINDIVIDUAL.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
charity_ids | array ofstring | The charity ID filters results to return only those items associated with the specified charity.Note:charity_idsis only supported by the US and UK marketplaces.Charity ID is a charity's unique identification number:In the US, this is theEmployer Identification Number (EIN).In the UK, this is the Charity Registration Number (CRN), commonly calledCharity Number.charity_idsmay be retrieved/determined as follows:Search for a supported charity using the Charity API'sgetCharityOrgsmethod.Important!The value to be passed in ascharity_idsis that returned in theregistrationIdfield.Search for a supported charity by visitingCharity Search. Click on the charity's name to display its information. The EIN number is included in the charity's information block at the top of the page.For example, the charity ID forAmerican Red Cross, is530196605.Up to 20 comma-separatedcharity_idsmay be specified in each query. Additionally,charity_idsmay be combined withcategory_idsand/orqkeyword values to further search_filter returned results.A sample query usingcharity_idsis:/buy/browse/v1/item_summary/search?charity_ids=13-1788491,300108469Occurrence:Optional
fieldgroups | array ofstring | A comma-separated list of values that controls what is returned in the response. The default isMATCHING_ITEMS, which returns the items that match the keyword or category specified. The other values return data that can be used to create histograms or provide additional information.Valid Values:ASPECT_REFINEMENTSThis field group adds theaspectDistributionscontainer to the response.Note:Information returned byASPECT_REFINEMENTSis category specific.BUYING_OPTION_REFINEMENTSThis field group adds thebuyingOptionDistributionscontainer to the response.CATEGORY_REFINEMENTSThis field group adds thecategoryDistributionscontainer to the response.CONDITION_REFINEMENTSThis field group adds theconditionDistributionscontainers, such asNEW,USED, etc., to the response. Within these groups are multiple states of the condition.For example,NEWcan beNew without tag,New in box,New without box, etc.EXTENDEDThis field group adds the following fields to the response:shortDescriptionitemLocation.cityMATCHING_ITEMS(default value)This field group is intended to be used with one or more of the refinement values listed above. This is used to return the specified refinements and all matching items.FULLThis field group returns all refinement containers and all matching items.Default:MATCHING_ITEMSOccurrence:Optional
category_ids | array ofstring | The category ID is used to max_results the results that are returned. This field may pass in one category ID or a comma separated list of IDs as illustrated in the following examples:/buy/browse/v1/item_summary/searchByImage?category_ids=29792/buy/browse/v1/item_summary/searchByImage?category_ids=267,29792Note:Currently, you can pass in only one category ID per request.To refine the set of information that is returned,category_idsmay be combined with other available filters.Because the list of eBay category IDs is not published and category IDs are not the same across all eBay marketplaces, category IDs may be determined by:Visiting theCategory Changes pageUsing the Taxonomy API. Refer toGet Categories for Buy APIsfor complete information.Issuing the following call to retrieve thedominantCategoryIdfor an item:/buy/browse/v1/item_summary/searchByImage?q=keyword&fieldgroups=ASPECT_REFINEMENTSOccurrence:Optional
search_filter | array ofFilterField | An array of field filters that can be used to max_results/customize the result set.Refer toBuy API Field Filtersfor the information about available filters.For example, to search_filter shirts based on a specific range of prices, include the search_filter illustrated here:/buy/browse/v1/item_summary/search?q=shirt&search_filter=price:[10..50]Filters may also be combined within a single request as illustrated in the sample below which further refines results to return only those shirts available from specific sellers:/buy/browse/v1/item_summary/search?q=shirt&search_filter=price:[10..50],sellers:{rpseller|bigSal}Note:Refer toBuy API Field Filtersfor additional information and examples of all supported filters.Occurrence:Optional
order_by | array ofSortField | Note:This call currently returns results in a best-match order. This query parameter presently has no practical use.Occurrence:Optional
max_results | string | The number of items from the result set returned in a single page.Note:If a value is set in thelimitfield, the value ofoffsetmust be either zero or a multiple of thelimitvalue. An error is returned for invalidoffsetvalues.Note:This method can return a maximum of 10,000 items in one results set.Min:1Max:200Default:50Occurrence:Optional
skip | string | Specifies the number of items to skip in the result set. This is used with thelimitfield to control the pagination of the output.For example:Ifoffsetis 0 andlimitis 10, the method will retrieve items 1-10 from the list of items returnedIfoffsetis 10 andlimitis 10, the method will retrieve items 11-20 from the list of items returned.Note:The value ofoffsetmust be either zero or a multiple of the value set in thelimitfield. An error is returned for invalidoffsetvalues.Note:This method can return a maximum of 10,000 items in one results set.Min: 0Max:9,999Default:0Occurrence:Optional
aspect_filter | AspectFilter | This field lets you search_filter by item aspects. The aspect name/value pairs and category, which is required, is used to max_results the results to specific aspects of the item. For example, in a clothing category one aspect pair would be Color/Red.Note:The category ID must be specifiedtwice:Once as a URI parameter in thecategory_idsfieldOnce as part of theaspect_filterfieldThese two valuesmustbe the same.For example, to return items for a woman's red shirt, issue the following request:/buy/browse/v1/item_summary/search?q=shirt&category_ids=15724&aspect_filter=categoryId:15724,Color:{Red}To get a list of the aspect pairs and the category, which is returned in thedominantCategoryIdfield, setfieldgroupstoASPECT_REFINEMENTSas illustrated here:/buy/browse/v1/item_summary/search?q=shirt&fieldgroups=ASPECT_REFINEMENTSNote:The pipe symbol is used as a delimiter between aspect search_filter values. If a value contains a pipe symbol (for example, the brand name 'Bed|Stü'), you must enter a backslash before the pipe character to prevent it from being evaluated as a delimiter.The following example illustrates the correct format for entering two brand names as aspect search_filter values, one of which contains a pipe symbol:/buy/browse/v1/item_summary/search?max_results=50&category_ids=3034&search_filter=buyingOptions:{AUCTION|FIXED_PRICE}&aspect_filter=categoryId:3034,Brand:{Bed\|Stü|Nike}Occurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
Accept-Language | string | This header is used to indicate the natural language and locale preferred by the user for the response.This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.Occurrence:Conditional
X-EBAY-C-ENDUSERCTX | string | This header is required to support revenue sharing for eBay Partner Network and to improve the accuracy of shipping and delivery time estimations.For additional information, refer toUse request headersin theBuying Integration Guide.Occurrence:Optional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.Note:If the marketplace ID value is invalid or missing, the default value ofEBAY_USis used.SeeMarketplaceIdEnumfor a list of supported marketplaces.Default:EBAY_USOccurrence:Strongly Recommended
[/TABLE]

[TABLE]
Input container/field | Type | Description
image | string | The Base64 string of the image.To get the Base64 image string, you can use sites such ashttps://codebeautify.org/image-to-base64-converter.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
autoCorrections | AutoCorrections | The auto-corrected inputs.Occurrence:Conditional
autoCorrections.q | string | The automatically spell-corrected keyword from the request.Occurrence:Conditional
href | string | The URI of the current page of results.The following example of thesearchmethod returns items 1 thru 5 from the list of items found.https://api.ebay.com/buy/v1/item_summary/search?q=shirt&max_results=5&skip=0Occurrence:Always
itemSummaries | array ofItemSummary | An array of the items on this page. The items are sorted according to the sorting method specified in the request.Occurrence:Conditional
itemSummaries.additionalImages | array ofImage | An array of containers with the URLs for the images that are in addition to the primary image. The primary image is returned in theimage.imageUrlfield.Occurrence:Conditional
itemSummaries.additionalImages.height | integer | Reserved for future use.Occurrence:Conditional
itemSummaries.additionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
itemSummaries.additionalImages.width | integer | Reserved for future use.Occurrence:Conditional
itemSummaries.adultOnly | boolean | This indicates if the item is for adults only. For more information about adult-only items on eBay, refer to theAdult items policy.Occurrence:Conditional
itemSummaries.availableCoupons | boolean | This boolean attribute indicates if coupons are available for the item.Note:The Browse API only acknowledges item-level coupons. This field will only be returned as true if a coupon is linked with an item. It does not recognize store-level coupons offered by sellers across their entire store.Occurrence:Conditional
itemSummaries.bidCount | integer | This integer value indicates the total number of bids that have been placed for an auction item. This field is only returned for auction items.Occurrence:Conditional
itemSummaries.buyingOptions | array ofstring | A comma separated list of all the purchase options available for the item.Values Returned:FIXED_PRICEIndicates the buyer can purchase the item for a set price using theBuy It Nowbutton.AUCTIONIndicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.BEST_OFFERItems where the buyer can send the seller a price they are willing to pay for the item. The seller can accept, reject, or send a counter offer. For additional information about Best Offer, refer toAdding Best Offer to your listing and sending offers to buyers.CLASSIFIED_ADIndicates that the final sales transaction is to be completed outside of the eBay environment.Occurrence:Conditional
itemSummaries.categories | array ofCategory | This array returns the name and ID of each category associated with the item, including top level, branch, and leaf categories.Occurrence:Conditional
itemSummaries.categories.categoryId | string | The unique identifier of the category.Occurrence:Conditional
itemSummaries.categories.categoryName | string | The name of the category.Occurrence:Conditional
itemSummaries.compatibilityMatch | CompatibilityMatchEnum | This indicates how well an item matches thecompatibility_filterproduct attributes.Valid Values:EXACTPOSSIBLEOccurrence:Conditional
itemSummaries.compatibilityProperties | array ofCompatibilityProperty | This container returns only the product attributes that are compatible with the item. These attributes were specified in thecompatibility_filterin the request. This means that if you passed in 5 attributes and only 4 are compatible, only those 4 are returned. If none of the attributes are compatible, this container is not returned.Occurrence:Conditional
itemSummaries.compatibilityProperties.localizedName | string | The name of the product attribute that as been translated to the language of the site.Occurrence:Conditional
itemSummaries.compatibilityProperties.name | string | The name of the product attribute, such as Make, Model, Year, etc.Occurrence:Conditional
itemSummaries.compatibilityProperties.value | string | The value for thenameattribute, such asBMW,R1200GS,2011, etc.Occurrence:Conditional
itemSummaries.condition | string | The text describing the condition of the item, such asNeworUsed. For a list of condition names, refer toItem Condition IDs and Names.Occurrence:Conditional
itemSummaries.conditionId | string | The identifier of the condition of the item. For example,1000is the identifier forNEW. For a list of condition names and IDs, refer toItem Condition IDs and Names.Occurrence:Conditional
itemSummaries.currentBidPrice | ConvertedAmount | This container returns the current highest bid for an auction item. Thevaluefield shows the dollar value of the current highest bid, and thecurrencyfield (3-digit ISO code) denotes the currency associated with that bid value. This field is only returned for auction items.Occurrence:Conditional
itemSummaries.currentBidPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
itemSummaries.currentBidPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
itemSummaries.currentBidPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
itemSummaries.currentBidPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
itemSummaries.distanceFromPickupLocation | TargetLocation | This container returns the distance away that the item is from thepickupPostalCodevalue that was supplied in the method request. This container is only returned if the "local pickup" search_filter fields are used in the request.Occurrence:Conditional
itemSummaries.distanceFromPickupLocation.unitOfMeasure | string | This value shows the unit of measurement used to measure the distance between the location of the item and the buyer's location. This value is typicallymiorkm.Occurrence:Conditional
itemSummaries.distanceFromPickupLocation.value | string | This value indicates the distance (measured in the measurement unit in theunitOfMeasurefield) between the item location and the buyer's location.Occurrence:Conditional
itemSummaries.energyEfficiencyClass | string | This indicates theEuropean energy efficiencyrating (EEK) of the item. Energy efficiency ratings apply to products listed by commercial vendors in electronics categories only.Currently, this field is only applicable for the Germany site, and is returned only if the seller specifies the energy efficiency rating through item specifics at listing time. Rating values includeA+++,A++,A+,A,B,C,D,E,F, andG.Occurrence:Conditional
itemSummaries.epid | string | An ePID is the eBay product identifier of a product from the eBay product catalog.  This indicates the product in which the item belongs.Occurrence:Conditional
itemSummaries.image | Image | The URL to the primary image of the item.Occurrence:Conditional
itemSummaries.image.height | integer | Reserved for future use.Occurrence:Conditional
itemSummaries.image.imageUrl | string | The URL of the image.Occurrence:Conditional
itemSummaries.image.width | integer | Reserved for future use.Occurrence:Conditional
itemSummaries.itemAffiliateWebUrl | string | The URL to the View Item page of the item which includes the affiliate tracking ID.Note:In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.TheitemAffiliateWebUrlis returned only if:The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.Occurrence:Conditional
itemSummaries.itemCreationDate | string | The date and time when the item listing was created. This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.This field is always returned withitemSummaries.Occurrence:Conditional
itemSummaries.itemEndDate | string | A timestamp that indicates the date and time a listing is scheduled to end.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
itemSummaries.itemGroupHref | string | The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Note:This field is returned only for item groups.Occurrence:Conditional
itemSummaries.itemGroupType | string | The indicates the item group type. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Currently only theSELLER_DEFINED_VARIATIONSis supported and indicates this is an item group created by the seller.Note:This field is returned only for item groups.Occurrence:Conditional
itemSummaries.itemHref | string | The URI for the Browse APIgetItemmethod, which can be used to retrieve more details about items in the search results.Occurrence:Conditional
itemSummaries.itemId | string | The unique RESTful identifier of the item.Occurrence:Conditional
itemSummaries.itemLocation | ItemLocationImpl | This container returns the location of the item. This container consists of fields you typically see for an address, including postal code, county, state/province, street address, city, and country (2-digit ISO code).Occurrence:Conditional
itemSummaries.itemLocation.addressLine1 | string | The first line of the street address.Occurrence:Conditional
itemSummaries.itemLocation.addressLine2 | string | The second line of the street address. This field may contain such values as an apartment or suite number.Occurrence:Conditional
itemSummaries.itemLocation.city | string | The city in which the item is located.Restriction:This field is populated in thesearchmethod responseonlywhenfieldgroups=EXTENDED.Occurrence:Conditional
itemSummaries.itemLocation.country | CountryCodeEnum | The two-letterISO 3166standard code that indicates the country in which the item is located.Occurrence:Conditional
itemSummaries.itemLocation.county | string | The county in which the item is located.Occurrence:Conditional
itemSummaries.itemLocation.postalCode | string | The postal code (or zip code in US) where the item is located. Sellers set a postal code for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned initemLocation.postalCodevia the API.Occurrence:Conditional
itemSummaries.itemLocation.stateOrProvince | string | The state or province in which the item is located.Occurrence:Conditional
itemSummaries.itemOriginDate | string | The date and time when the listing was first made available. This date will be retained if an item is relisted. This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.This timestamp is used to order_by the response when thesort=newlyListedparameter is used.This field is always returned withitemSummaries.Occurrence:Conditional
itemSummaries.itemWebUrl | string | The URL to the View Item page of the item. This enables you to include a "Report Item on eBay" hyperlink that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.Occurrence:Conditional
itemSummaries.leafCategoryIds | array ofstring | The leaf category IDs of the item. When the item belongs to two leaf categories, the ID values are returned in the order primary, secondary.Occurrence:Conditional
itemSummaries.legacyItemId | string | The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Conditional
itemSummaries.listingMarketplaceId | MarketplaceIdEnum | The ID of the eBay marketplace on which the seller listed the item.Occurrence:Conditional
itemSummaries.marketingPrice | MarketingPrice | This container is returned if the item is eligible for a seller discount and contains the item's original price, and the seller discount amount and percentage.Occurrence:Conditional
itemSummaries.marketingPrice.discountAmount | ConvertedAmount | This container returns the monetary amount of the seller discount.Occurrence:Conditional
itemSummaries.marketingPrice.discountAmount.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
itemSummaries.marketingPrice.discountAmount.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
itemSummaries.marketingPrice.discountAmount.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
itemSummaries.marketingPrice.discountAmount.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
itemSummaries.marketingPrice.discountPercentage | string | This field expresses the percentage of the seller discount based on the value in theoriginalPricecontainer.Occurrence:Conditional
itemSummaries.marketingPrice.originalPrice | ConvertedAmount | This container returns the monetary amount of the item without the discount.Occurrence:Conditional
itemSummaries.marketingPrice.originalPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
itemSummaries.marketingPrice.originalPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
itemSummaries.marketingPrice.originalPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
itemSummaries.marketingPrice.originalPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
itemSummaries.marketingPrice.priceTreatment | PriceTreatmentEnum | Indicates the pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects the way and where the discounted price can be displayed.Occurrence:Conditional
itemSummaries.pickupOptions | array ofPickupOptionSummary | This container returns the local pickup options available to the buyer. This container is returned only if the user is searching for local pickup items and set the local pickup filters in the method request.Occurrence:Conditional
itemSummaries.pickupOptions.pickupLocationType | string | This container returns the local pickup options available to the buyer. Possible values areARRANGED_LOCATIONandSTORE.Occurrence:Conditional
itemSummaries.price | ConvertedAmount | The price of the item after it has been converted into another currency.The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must do one or more of the following to view VAT-inclusive pricing:Pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB)Pass thecontextualLocationvalues for the supported marketplace in theX-EBAY-C-ENDUSERCTXrequest headerSpecify the supported marketplace using thedeliveryCountryfilterURI parameter (such asfilter=deliveryCountry:GB)Note:For more information on VAT, refer toYour VAT Obligations in the UK & EU.Occurrence:Conditional
itemSummaries.price.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
itemSummaries.price.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
itemSummaries.price.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
itemSummaries.price.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
itemSummaries.priceDisplayCondition | PriceDisplayConditionEnum | Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.Occurrence:Conditional
itemSummaries.priorityListing | boolean | This field is returned astrueif the listing is part of a Promoted Listing campaign. Promoted Listings are available toAbove StandardandTop Ratedsellers with recent sales activity.Note:Priority Listing is returned only with a Best Match order_by and will not be returned for other order_by options.Occurrence:Conditional
itemSummaries.qualifiedPrograms | array ofstring | An array of the qualified programs available for the item, such asEBAY_PLUS,AUTHENTICITY_GUARANTEE, andAUTHENTICITY_VERIFICATION.eBay Plus is a premium account option for buyers, which provides benefits such as fast, free domestic shipping and free returns on selected items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings. Sellers must commit to next-day delivery of those items.Note:eBay Plus is only available as a listing feature on the eBay Australia marketplace.The eBayAuthenticity Guaranteeprogram enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.Occurrence:Conditional
itemSummaries.seller | Seller | This container returns basic information about the seller of the item, such as name, feedback score, etc.Occurrence:Conditional
itemSummaries.seller.feedbackPercentage | string | The percentage of the total positive feedback.Occurrence:Conditional
itemSummaries.seller.feedbackScore | integer | The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Conditional
itemSummaries.seller.sellerAccountType | string | Indicates if the seller is a business or an individual. This is determined when the seller registers with eBay:If they register for a business account, this value will beBUSINESS.If they register for a private account, this value will beINDIVIDUAL.This designation is required by the tax laws in some countries.This field is returned only on the following sites:EBAY_AT, EBAY_BE, EBAY_CH, EBAY_DE, EBAY_ES, EBAY_FR, EBAY_GB, EBAY_IE, EBAY_IT, EBAY_PLValid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
itemSummaries.seller.username | string | The user name created by the seller for use on eBay.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Conditional
itemSummaries.shippingOptions | array ofShippingOptionSummary | This container returns the shipping options available to ship the item.Occurrence:Conditional
itemSummaries.shippingOptions.guaranteedDelivery | boolean | Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.Occurrence:Conditional
itemSummaries.shippingOptions.maxEstimatedDeliveryDate | string | The end date of the delivery window (latest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header.Note:Estimated delivery dates are not returned for CBT items.Occurrence:Conditional
itemSummaries.shippingOptions.minEstimatedDeliveryDate | string | The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header.Note:Estimated delivery dates are not returned for CBT items.Occurrence:Conditional
itemSummaries.shippingOptions.shippingCost | ConvertedAmount | This is the estimated price to ship the item.The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must do one or more of the following to see VAT-inclusive pricing:Pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB)Pass thecontextualLocationvalues for the supported marketplace in theX-EBAY-C-ENDUSERCTXrequest headerSpecify the supported marketplace using thedeliveryCountryfilterURI parameter (such asfilter=deliveryCountry:GB)Note:For more information on VAT, refer toYour VAT Obligations in the UK & EU.Occurrence:Conditional
itemSummaries.shippingOptions.shippingCost.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
itemSummaries.shippingOptions.shippingCost.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
itemSummaries.shippingOptions.shippingCost.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
itemSummaries.shippingOptions.shippingCost.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
itemSummaries.shippingOptions.shippingCostType | string | Indicates the type of shipping used to ship the item. Possible values areFIXED(flat-rate shipping) andCALCULATED(shipping cost calculated based on item and buyer location).Occurrence:Conditional
itemSummaries.shortDescription | string | This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.) Sometimes the title does not provide enough information but the description is too big. Surfacing theshortDescriptioncan often provide buyers with the additional information that could help them make a buying decision.For example:"title": "Petrel U42W FPV Drone RC Quadcopter w/HD Camera Live Video One Key Off / Landing","shortDescription": "1 U42W Quadcopter. Syma X5SW-V3 Wifi FPV RC Drone Quadcopter 2.4Ghz 6-Axis Gyro with Headless Mode. Syma X20 Pocket Drone 2.4Ghz Mini RC Quadcopter Headless Mode Altitude Hold. One Key Take Off / Landing function: allow beginner to easy to fly the drone without any skill.",Restriction:This field is returned by thesearchmethod only whenfieldgroups=EXTENDED.Occurrence:Conditional
itemSummaries.thumbnailImages | array ofImage | An array of thumbnail images for the item.Occurrence:Conditional
itemSummaries.thumbnailImages.height | integer | Reserved for future use.Occurrence:Conditional
itemSummaries.thumbnailImages.imageUrl | string | The URL of the image.Occurrence:Conditional
itemSummaries.thumbnailImages.width | integer | Reserved for future use.Occurrence:Conditional
itemSummaries.title | string | The seller-created title of the item.Maximum Length:80 charactersOccurrence:Conditional
itemSummaries.topRatedBuyingExperience | boolean | This indicates if the item is a top-rated plus item. There are three benefits of a top-rated plus item: a  minimum 30-day money-back return policy; shipping the item in 1 business day with tracking provided; and the added comfort of knowing that this item is from an experienced seller with the highest buyer ratings. For more information, refer toLook for Top Rated Plus ItemsandSeller performance overview.Occurrence:Conditional
itemSummaries.tyreLabelImageUrl | string | The URL to the image that shows the information on the tyre label.Occurrence:Conditional
itemSummaries.unitPrice | ConvertedAmount | The price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
itemSummaries.unitPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
itemSummaries.unitPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
itemSummaries.unitPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
itemSummaries.unitPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
itemSummaries.unitPricingMeasure | string | The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item. This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
itemSummaries.watchCount | integer | The number of users that have added the item to their watch list.Note:This field is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields indicating that you want access to Watch Count data in the Browse API.Occurrence:Conditional
max_results | integer | The value of thelimitparameter submitted in the request, which is the maximum number of items to return on a page, from the result set. A result set is the complete set of items returned by the method.Occurrence:Always
next | string | The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set.The following example of thesearchmethod returns items 5 thru 10 from the list of items found.https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&max_results=5&skip=10Occurrence:Conditional
skip | integer | This value indicates theoffsetused for current page of items being returned. Assume the initial request used anoffsetof0and alimitof3. Then in the first page of results, this value would be0, and items 1-3 are returned. For the second page, this value is3and so on.Occurrence:Always
prev | string | The URI for the previous page of results. This is returned if there is a previous page of results from the result set.The following example of thesearchmethod returns items 1 thru 5 from the list of items found, which would be the first set of items returned.https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&max_results=5&skip=0Occurrence:Conditional
refinement | Refinement | The container for all the search refinements.Occurrence:Conditional
refinement.aspectDistributions | array ofAspectDistribution | An array of containers for the all the aspect refinements.Occurrence:Conditional
refinement.aspectDistributions.aspectValueDistributions | array ofAspectValueDistribution | An array of containers for the various values of the aspect and the match count, and a HATEOAS reference (refinementHref) for this aspect.Occurrence:Conditional
refinement.aspectDistributions.aspectValueDistributions.localizedAspectValue | string | The value of an aspect. For example, Red is a value for the aspect Color.Occurrence:Always
refinement.aspectDistributions.aspectValueDistributions.matchCount | integer | The number of items with this aspect.Occurrence:Always
refinement.aspectDistributions.aspectValueDistributions.refinementHref | string | A HATEOAS reference for this aspect.Occurrence:Always
refinement.aspectDistributions.localizedAspectName | string | The name of an aspect, such asBrand,Color, etc.Occurrence:Conditional
refinement.buyingOptionDistributions | array ofBuyingOptionDistribution | An array of containers for the all the buying option refinements.Occurrence:Conditional
refinement.buyingOptionDistributions.buyingOption | string | The container that returns the buying option type. This will be AUCTION, FIXED_PRICE, CLASSIFIED_AD, or a combination of these options. For details, seebuyingOptions.Occurrence:Always
refinement.buyingOptionDistributions.matchCount | integer | The number of items having this buying option.Occurrence:Always
refinement.buyingOptionDistributions.refinementHref | string | The HATEOAS reference for this buying option.Occurrence:Always
refinement.categoryDistributions | array ofCategoryDistribution | An array of containers for the all the category refinements.Occurrence:Conditional
refinement.categoryDistributions.categoryId | string | The unique identifier of the category.Occurrence:Always
refinement.categoryDistributions.categoryName | string | The name of the category, such asBaby & Toddler Clothing.Occurrence:Always
refinement.categoryDistributions.matchCount | integer | The number of items in this category.Occurrence:Always
refinement.categoryDistributions.refinementHref | string | The HATEOAS reference of this category.Occurrence:Always
refinement.conditionDistributions | array ofConditionDistribution | An array of containers for the all the condition refinements.Occurrence:Conditional
refinement.conditionDistributions.condition | string | The text describing the condition of the item, such asNeworUsed. For a list of condition names, refer toItem Condition IDs and Names.Occurrence:Conditional
refinement.conditionDistributions.conditionId | string | The identifier of the condition. For example,1000is the identifier forNEW.Occurrence:Conditional
refinement.conditionDistributions.matchCount | integer | The number of items having the condition.Occurrence:Always
refinement.conditionDistributions.refinementHref | string | The HATEOAS reference of this condition.Occurrence:Always
refinement.dominantCategoryId | string | The identifier of the category that most of the items are part of.Occurrence:Always
total | integer | The total number of items that match the input criteria.Note:totalis just an indicator of the number of listings for a given query. It could vary based on the number of listings with variations included in the result. It is strongly recommended thattotalnot be used in pagination use cases. Instead, usenextto determine the results on the next page.Occurrence:Always
warnings | array ofErrorDetailV3 | The container with all the warnings for the request.Occurrence:Conditional
warnings.category | string | This string value indicates the error category. There are three categories of errors:request errors,application errors, andsystem errors.Occurrence:Always
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
12000 | API_BROWSE | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
12004 | API_BROWSE | REQUEST | The 'skip' value cannot be negative.
12005 | API_BROWSE | REQUEST | The 'skip' value must be an integer.
12006 | API_BROWSE | REQUEST | The 'max_results' value should be between 1 and 200 (inclusive).
12007 | API_BROWSE | REQUEST | The 'max_results' value must be an integer value.
12013 | API_BROWSE | BUSINESS | Top level category browsing is not allowed. Please provide keywords or more filters for the applied top level category.
12019 | API_BROWSE | BUSINESS | Currently, the {marketplaceId} marketplace is not supported. The supported Marketplaces are: {allowedMarketplaces} .
12020 | API_BROWSE | BUSINESS | The 'fieldgroups' value {fieldgroups} is invalid when multiple 'category_ids' are specified. Either change the call to have only one value in 'category_ids' or remove the 'fieldgroups'.
12025 | API_BROWSE | REQUEST | The 'charity_ids' field has exceeded the maximum max_results of 20.
12026 | API_BROWSE | REQUEST | The 'charity_ids' field is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}.
12029 | API_BROWSE | REQUEST | The maximum number of listings that can be retrieved is 10,000, so your skip value must be less than 10,000. If 10,000 or more listings are matching your search criteria, consider narrowing the scope of your search.
12030 | API_BROWSE | REQUEST | The number of categories in the request has exceeded the max_results. Please reduce the number of categories to {allowedMaxCategories} or less.
12032 | API_BROWSE | REQUEST | The number of sellers in the search_filter has exceeded the max_results. Please reduce the number of sellers to 250 or fewer.
12033 | API_BROWSE | REQUEST | The 'qualifiedPrograms' search_filter for {filterValue} requires valid 'deliveryPostalCode' and 'deliveryCountry' search_filter values.
12034 | API_BROWSE | REQUEST | The 'buyingOptions' search_filter value {filterValue} is not supported for the order_by by {sortOption}. For the supported values, refer to the API call documentation.
12500 | API_BROWSE | REQUEST | This image search results in a response that is too large to return. Either change the image or add additional query parameters and/or filters.
12501 | API_BROWSE | REQUEST | The image data is empty, is not Base64 encoded, or is invalid.
12507 | API_BROWSE | REQUEST | To search_filter by 'guaranteedDeliveryInDays', you must include 'deliveryCountry'.
12508 | API_BROWSE | REQUEST | To search_filter by 'guaranteedDeliveryInDays', you must include 'deliveryPostalCode' for the 'deliveryCountry'.
12509 | API_BROWSE | REQUEST | The 'guaranteedDeliveryInDays' value {guaranteedDeliveryInDays} is invalid for 'deliveryCountry' value {deliveryCountry}.  Valid values for 'guaranteedDeliveryInDays' for {deliveryCountry} must be in the range of {rangeLowerBound} to {rangeUpperBound} inclusive.
12510 | API_BROWSE | REQUEST | The 'guaranteedDeliveryInDays' search_filter is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}
12512 | API_BROWSE | REQUEST | The 'qualifiedPrograms' search_filter for {filterValue} is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}
12513 | API_BROWSE | BUSINESS | The 'priorityListing' search_filter for {filterValue} is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}
12514 | API_BROWSE | BUSINESS | The 'priorityListing' search_filter is not supported for the specified order_by option. Refer to the API call documentation.
12515 | API_BROWSE | REQUEST | The 'skip' value must be either zero or a multiple of the 'max_results' value.
[/TABLE]

[TABLE]
12002 | API_BROWSE | REQUEST | The {filterName} value is invalid. For the valid values, refer to the API call documentation.
12003 | API_BROWSE | REQUEST | A seller 'username' provided in the request filters is invalid.
12008 | API_BROWSE | REQUEST | The 'order_by' value is invalid. For the valid values, refer to the API call documentation.
12009 | API_BROWSE | REQUEST | The 'category_ids' query parameter is invalid.
12010 | API_BROWSE | REQUEST | There are four filters required for local pickup. 'pickupPostalCode','pickupCountry','pickupRadiusUnit','pickupRadius'. One or more is missing or invalid.
12011 | API_BROWSE | REQUEST | 'deliveryCountry' is a mandatory search_filter to provide a delivery location. 'deliveryPostalCode' is optional.
12012 | API_BROWSE | REQUEST | A valid 'price' search_filter and a valid 'priceCurrency' search_filter is necessary to search_filter based on price.
12014 | API_BROWSE | BUSINESS | The 'sellerAccountTypes' search_filter is not supported for the marketplace {marketplaceId}. Valid marketplaces are: {validMarketplaces}
12015 | API_BROWSE | REQUEST | The postal code search_filter value is invalid for the specified country and this search_filter was ignored.
12016 | API_BROWSE | REQUEST | The 'fieldgroups' value {fieldgroups} is invalid. For the valid values, refer to the API call reference documentation
12017 | API_BROWSE | REQUEST | The 'aspect_filter' query parameter must include a categoryId. For information, see the API call reference documentation.
12018 | API_BROWSE | REQUEST | The {aspectFilter} aspect_filter value is invalid. For information, see the API call reference documentation.
12024 | API_BROWSE | REQUEST | The 'charity_ids' value {charity_id} is invalid. For more information see the API call reference documentation.
12031 | API_BROWSE | REQUEST | The following search_filter(s) is/are not supported by this operation: {unsupportedFilters}. For more information see the API call reference documentation.
12511 | API_BROWSE | REQUEST | Either 'deliveryCountry' or 'deliveryPostalCode' is invalid, hence 'guaranteedDeliveryInDays' search_filter was ignored.
[/TABLE]