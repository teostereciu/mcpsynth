# buy/browse/resources/item/methods/getItems

*Source: https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItems*

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

### Sample 1: Retrieve Item Details Using Multiple Item IDs

### Sample 2: Retrieve Item Details Using Multiple Item Group IDs

#### Thank you for helping us to improve the eBay developer program.
This method retrieves the details about specific items that buyers need to make a purchasing decision.Note:This is a(Limited Release)available only to select Partners.For this method, only the following fields are returned:bidCount,currentBidPrice,eligibleForInlineCheckout,enabledForGuestCheckout,estimatedAvailabilities,gtin,immediatePay,itemAffiliateWebUrl,itemCreationDate,itemEndDate,itemId,itemWebUrl,legacyItemId,minimumPriceToBid,price,priorityListing,reservePriceMet,sellerItemRevision,taxes,topRatedBuyingExperience, anduniqueBidderCount.The arrayshippingOptions, which comprises multiple fields, is also returned if theX-EBAY-C-ENDUSERCTXheader is supplied.RestrictionsFor a list of supported sites and other restrictions, refer toAPI Restrictions.eBay Partner Network:In order to be commissioned for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Conditional
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Strongly Recommended
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.item.bulk
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
An arraylist of all the items.Occurrence:Conditional
An array of containers with the URLs for the images that are in addition to the primary image.  The primary image is returned in theimage.imageUrlfield.Occurrence:Conditional
Reserved for future use.Occurrence:Conditional
The URL of the image.Occurrence:Conditional
This indicates if the item is for  adults only. For more information about adult-only items on eBay, seeAdult items policyfor sellers andAdult-Only items on eBayfor buyers.Occurrence:Always
Occurrence:Always
(Primary Item Aspect) The age group for which the product is recommended. For example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
A container for information about whether an item is qualified for the Authenticity Guarantee program.Under the Authenticity Guarantee program, the seller ships a purchased item to a a third-party authenticator who inspects the item and provides an authentication card for it before the item is shipped to the buyer. If the buyer returns the item, the authenticator first verifies that it is the same item in the same condition before returning it to the seller.Note:Refer to theAuthenticity Guaranteepage for more information.Occurrence:Conditional
An indication that the item is qualified for the Authenticity Guarantee program.Occurrence:Conditional
The URL to the Authenticity Guarantee program terms of use.Occurrence:Conditional
An indication that the item is from a verified seller.Occurrence:Conditional
The URL to the Authenticity Verification program terms of use.Occurrence:Conditional
A list of available coupons for the item.Occurrence:Conditional
The limitations or restrictions of the coupon.Occurrence:Conditional
This timestamp provides the expiration date of the coded coupon.Occurrence:Conditional
The discount amount after the coupon is applied.Occurrence:Conditional
The list of valid currencies. EachISO 4217currency code includes the currency name followed by the numeric value.For example, the Canadian Dollar code (CAD) would take the following form:Canadian Dollar, 124.Occurrence:Conditional
The value of the discounted amount.Occurrence:Conditional
The type of discount that the coupon applies.Occurrence:Conditional
A description of the coupon.Note:The value returned in thetermsWebUrlfield should appear for all experiences when displaying coupons. The value in theavailableCoupons.messagefield must also be included if returned in the API response.Occurrence:Conditional
The coupon code.Occurrence:Conditional
The URL to the coupon terms of use.Note:The value returned in thetermsWebUrlfield should appear for all experiences when displaying coupons. The value in theavailableCoupons.messagefield must also be included if returned in the API response.Occurrence:Conditional
This integer value indicates the total number of bids that have been placed against an auction item. This field is returned only for auction items.Occurrence:Conditional
(Primary Item Aspect) The name brand of the item, such as Nike, Apple, etc.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
A comma separated list of all the purchase options available for the item. The values returned are:FIXED_PRICE- Indicates the buyer can purchase the item for a set price using the Buy It Now button.AUCTION- Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.BEST_OFFER- Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, seeMaking a Best Offer.CLASSIFIED_AD- Indicates that the final sales transaction is to be completed outside of the eBay environment.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The ID of the leaf category for this item. A leaf category is the lowest level in that category and has no children.Occurrence:Always
Text that shows the category hierarchy of the item. For example: Computers/Tablets & Networking, Laptops & Netbooks, PC Laptops & NetbooksOccurrence:Always
(Primary Item Aspect) Text describing the color of the item.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
This container returns any applicable charity information associated with the specified item.This container is only returned if thefieldgroupsquery parameter is set toCHARITY_DETAILS.Occurrence:Conditional
The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds from the item.Occurrence:Conditional
The percentage of the purchase price of the item that the charitable organization (identified in thecharityOrgIdfield) will receive for each sale.Occurrence:Conditional
The details of the charity's logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
The name of the charity organization.Occurrence:Conditional
The URL to the charity's eBay page.Occurrence:Conditional
A short text description for the condition of the item, such as New or Used. For a list of condition names, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
A full text description for the condition of the item. This field elaborates on the value specified in theconditionfield and provides full details for the condition of the item.Occurrence:Conditional
The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The container that returns the current highest bid for an auction item. The value (string) field shows the dollar value of the current highest bid, and the currency (3-digit ISO code) field denotes the currency associated with that bid value. This container will only be returned for auction items.Occurrence:Conditional
The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
The full description of the item that was created by the seller. This can be plain text or rich content and can be very large.Occurrence:Always
This field indicates if the item can be purchased using the BuyOrder API.If the value of this field istrue, this indicates that the item can be purchased using theOrder API.If the value of this field isfalse, this indicates that the item cannot be purchased using theOrder APIand must be purchased on the eBay site.Occurrence:Always
This indicates if the item can be purchased using Guest Checkout in theOrder API. You can use this flag to exclude items from your inventory that are not eligible for Guest Checkout, such as gift cards.Occurrence:Always
This indicates theEuropean energy efficiencyrating (EEK) of the item. This field is returned only if the seller specified the energy efficiency rating.The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.When the manufacturer's specifications for this item are available, the link to this information is returned in theproductFicheWebUrlfield.Occurrence:Conditional
An EPID is the eBay product identifier of a product from the eBay product catalog.  This indicates the product in which the item belongs.Occurrence:Conditional
The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Occurrence:Conditional
This field is return only when the seller sets their 'display item quantity' preference toDisplay "More than 10 available" in your listing (if applicable). The value of this field will be "10", which is the threshold value.Code so that your app gracefully handles any future changes to this value.Occurrence:Conditional
An array of available delivery options.Valid Values:SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, PICKUP_DROP_OFF, or DIGITAL_DELIVERYCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
An enumeration value representing the inventory status of this item.Note:Be sure to review theitemEndDatefield to determine whether the item is available for purchase.Valid Values:IN_STOCK, LIMITED_STOCK, or OUT_OF_STOCKCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The estimated number of this item that have been sold.Occurrence:Conditional
(Primary Item Aspect) The gender for the item. This is used for items that could vary by gender, such as clothing. For example: male, female, or unisex. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
The unique Global Trade Item number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
The URL of the primary image of the item. The other images of the item are returned in theadditionalImagescontainer.Occurrence:Always
A value oftrueindicates that the seller requires immediate payment from the buyer when purchasing an item.Note:It is possible for this field to be set totrue, but not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyers' purchases that involve the Best Offer feature, or for offline transactions.Occurrence:Always
The ePID (eBay Product ID of a product from the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.If the seller provided an ePID for the item, the seller's value is returned in theepidfield.Note:This field is returned only for authorized Partners.Occurrence:Conditional
The URL to the View Item page of the item which includes the affiliate tracking ID.Note:In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.TheitemAffiliateWebUrlis only returned if:The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.Occurrence:Conditional
A timestamp that indicates the date and time an item listing was created.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
A timestamp that indicates the date and time an auction listing will end.If a fixed-price listing has ended, this field indicates the date and time the listing ended.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
The unique RESTful identifier of the item.Occurrence:Always
The physical location of the item.Occurrence:Conditional
The first line of the street address.Note:This is conditionally returned in theitemLocationfield.Occurrence:Conditional
The second line of the street address. This field is not always used, but can be used for "Suite Number" or "Apt Number".Occurrence:Conditional
The city of the address.Occurrence:Always
The two-letterISO 3166standard code for the country of the address.Occurrence:Always
The county of the address.Occurrence:Conditional
The postal code (or zip code in US) code of the address. Sellers set a postal code (or zip code in US) for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned initemLocation.postalCodevia the API.Occurrence:Conditional
The state or province of the address.Note:This is conditionally returned in theitemLocationfield.Occurrence:Conditional
The URL of the View Item page of the item. This enables you to include a "Report Item on eBay" link that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.Occurrence:Always
The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Always
An array of containers that show the complete list of the aspect name/value pairs that describe the variation of the item.Occurrence:Conditional
The text representing the name of the aspect for the name/value pair, such as Color.Occurrence:Conditional
This indicates if the value being returned is a string or an array of values.Valid Values:STRING- Indicates the value returned is a string.STRING_ARRAY- Indicates the value returned is an array of strings.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The value of the aspect for the name/value pair, such as Red.Occurrence:Conditional
The number of items in a lot. In other words, a lot size is the number of items that are being sold together.A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot,  such as the package of batteries shown in the example below.ItemLot DefinitionLot SizeA package of 24 AA batteriesA box of 10 packages10A P235/75-15 Goodyear tire4 tires4Fashion Jewelry RingsPackage of 100 assorted rings100Note:Lots are not supported in all categories.Occurrence:Conditional
The original price and the discount amount and percentage.Occurrence:Conditional
This container returns the monetary amount of the seller discount.Occurrence:Conditional
This field expresses the percentage of the seller discount based on the value in theoriginalPricecontainer.Occurrence:Conditional
Indicates the pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects the way and where the discounted price can be displayed.Occurrence:Conditional
(Primary Item Aspect) Text describing what the item is made of. For example, silk. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
The minimum price of the next bid, which means to place a bid it must be equal to or greater than this amount. If the auction hasn't received any bids, the minimum bid price is the same as the starting bid. Otherwise, the minimum bid price is equal to the current bid plus the bid increment.  For details about bid increments, seeAutomatic bidding.Occurrence:Conditional
The manufacturer's part number, which is a unique number that identifies a specific product. To identify the product, this is always used along with brand.Occurrence:Conditional
(Primary Item Aspect) Text describing the pattern used on the item. For example, paisley. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
The payment methods for the item, including the payment method types, brands, and instructions for the buyer.Occurrence:Conditional
The payment method type, such as credit card or cash.Occurrence:Conditional
The payment method brands, including the payment method brand type and logo image.Occurrence:Conditional
The payment method brand, such as Visa or PayPal.Occurrence:Conditional
The details of the logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
The payment instructions for the buyer, such ascash in personorcontact seller.Occurrence:Conditional
The seller instructions to the buyer, such asaccepts credit cardsorsee description.Occurrence:Conditional
The cost of just the item. This amount does not include any adjustments such as discounts or shipping costs.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.Occurrence:Conditional
The container that returns details of a primary item group (parent ID of an item group). An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.Note:This container is returned if theitem_idin the request is for an item group (items with variations, such as color and size). This container is also returned on a request foritem_group_ids.Occurrence:Conditional
An array of containers with the URLs for images that are in addition to the primary image of the item group.  The primary image is returned in theitemGroupImagefield.Occurrence:Conditional
The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
The URL of the primary image of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
The container that returns the product rating details, such as review count, rating histogram, and average rating.Occurrence:Conditional
The average rating given to a product based on customer reviews.Occurrence:Conditional
An array of containers for the product rating histograms that shows the review counts and the product rating.Occurrence:Conditional
The total number of user ratings that the product has received.Occurrence:Conditional
This is the average rating for the product. As part of a product review, users rate the product. Products are rated from one star (terrible) to five stars (excellent), with each star having a corresponding point value - one star gets 1 point, two stars get 2 points, and so on. If a product had one four-star rating and one five-star rating, its average rating would be4.5, and this is the value that would appear in this field.Occurrence:Conditional
The total number of reviews for the item.Occurrence:Conditional
This field is returned astrueif the listing is part of a Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent sales activity.For more information, seePromoted Listings.Occurrence:Always
The container that returns the product information of the item.Occurrence:Conditional
An array of containers with the URLs for the product images that are in addition to the primary image.Occurrence:Conditional
An array of product identifiers associated with the item. This container is returned if the seller has associated the eBay Product Identifier (ePID) with the item and in the requestfieldgroupsis set toPRODUCT.Occurrence:Conditional
An array of product identifier/value pairs for the product associated with the item. This is returned if the seller has associated the eBay Product Identifier (ePID) with the item and the request hasfieldgroupsset toPRODUCT.The following table shows what is returned, based on the item information provided by the seller, whenfieldgroupsis set toPRODUCT.ePID ProvidedProduct ID(s) ProvidedResponseNoNoTheAdditionalProductIdentitycontainer isnotreturned.NoYesTheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.YesNoTheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product.YesYesTheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.Occurrence:Conditional
The type of product identifier, such as UPC and EAN.Occurrence:Conditional
The product identifier value.Occurrence:Conditional
An array of containers for the product aspects. Each group contains the aspect group name and the aspect name/value pairs.Occurrence:Conditional
An array of the name/value pairs for the aspects of the product. For example: BRAND/AppleOccurrence:Conditional
The text representing the value of the aspect for the name/value pair, such as Apple.Occurrence:Conditional
The name of a group of aspects.In the following example,Product IdentifiersandProcessare product aspect group names. Under the group name are the product aspect name/value pairs.Product IdentifiersBrand/AppleProduct Family/iMacProcessorProcessor Type/IntelProcessor Speed/3.10Occurrence:Conditional
The brand associated with product. To identify the product, this is always used along with MPN (manufacturer part number).Occurrence:Conditional
The rich description of an eBay product, which might contain HTML.Occurrence:Conditional
An array of all the possible GTINs values associated with the product. A GTIN is a unique Global Trade Item number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
The primary image of the product. This is often a stock photo.Occurrence:Conditional
An array of all possible MPN values associated with the product. A MPNs is manufacturer part number of the product. To identify the product, this is always used along with brand.Occurrence:Conditional
The title of the product.Occurrence:Conditional
The URL of a page containing the manufacturer's specification of this item, which helps buyers make a purchasing decision. This information is available only for items that include the European energy efficiency rating (EEK) but is not available forallitems with an EEK rating and is returned only if this information is available. The EEK rating of the item is returned in theenergyEfficiencyClassfield.Occurrence:Conditional
An array of the qualified programs available for the item, such as EBAY_PLUS, AUTHENTICITY_GUARANTEE, and AUTHENTICITY_VERIFICATION.eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings. Sellers must commit to next-day delivery of those items.Note:eBay Plus is only available as a listing feature on the eBay Australia marketplace.The eBayAuthenticity Guaranteeprogram enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.Occurrence:Conditional
The maximum number for a specific item that one buyer can purchase.Occurrence:Conditional
This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.Note:This is returned only for auctions that have a reserve price.Occurrence:Conditional
If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.
Note:This is returned only for auctions that have a reserve price.
The container that returns an overview of the seller's return policy.Occurrence:Conditional
This indicates if the seller has enabled the Extended Holiday Returns feature on the item. Extended Holiday Returns are only applicable during the US holiday season, and gives buyers extra time to return an item. This 'extra time' will typically extend beyond what is set through thereturnPeriodvalue.Occurrence:Conditional
An enumeration value that indicates how a buyer is refunded when an item is returned.Valid Values:MONEY_BACK or MERCHANDISE_CREDITCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
This string field indicates the restocking fee percentage that the seller has set on the item. Sellers have the option of setting no restocking fee for an item, or they can set the percentage to 10, 15, or 20 percent. So, if the cost of the item was $100, and the restocking percentage was 20 percent, the buyer would be charged $20 to return that item, so instead of receiving a $100 refund, they would receive $80 due to the restocking fee.Occurrence:Conditional
Text written by the seller describing what the buyer needs to do in order to return the item.Occurrence:Conditional
An enumeration value that indicates the alternative methods for a full refund when an item is returned. This field is returned if the seller offers the buyer an item replacement or exchange instead of a monetary refund.Valid Values:REPLACEMENT-  Indicates that the buyer has the option of receiving money back for the returned item, or they can choose to have the seller replace the item with an identical item.EXCHANGE- Indicates that the buyer has the option of receiving money back for the returned item, or they can exchange the item for another similar item.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The amount of time the buyer has to return the item after the purchase date.Occurrence:Conditional
An enumeration value that indicates the units of the time span (e.g.,HOURS). The enumeration value in this field defines the period of time being used to measure the duration.Refer toTimeDurationUnitEnumfor the list of supported values.Occurrence:Conditional
Retrieves the duration of the time span (no units). The value in this field indicates the number of years, months, days, hours, or minutes in the defined period.Occurrence:Conditional
Indicates whether the seller accepts returns for the item.Occurrence:Conditional
This enumeration value indicates whether the buyer or seller is responsible for return shipping costs when an item is returned.Valid Values:SELLER- Indicates the seller will pay for the shipping costs to return the item.BUYER- Indicates the buyer will pay for the shipping costs to return the item.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The container that returns basic and detailed about the seller of the item, such as name, feedback score, and contact information.Occurrence:Always
The percentage of the total positive feedback.Occurrence:Always
The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Always
This indicates if the seller is a business or an individual. This is determined when the seller registers with eBay. If they register for a business account, this value will beBUSINESS. If they register for a private account, this value will beINDIVIDUAL. This designation is required by the tax laws in the following countries:This field is applicable only on the following marketplaces:EBAY_ATEBAY_BEEBAY_CHEBAY_DEEBAY_ESEBAY_FREBAY_GBEBAY_IEEBAY_ITEBAY_PLNote:This field will be returned empty on unsupported marketplaces.Valid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
The container with the seller's contact info and fields that are required by law.Occurrence:Conditional
The seller's business email address.Occurrence:Conditional
The seller' business fax number.Occurrence:Conditional
This is a free-form string created by the seller. This is information often found on business cards, such as address. This is information used by some countries.Occurrence:Conditional
The seller's first name.Occurrence:Conditional
The seller's last name.Occurrence:Conditional
The name of the seller's business.Occurrence:Conditional
The seller's business phone number.Occurrence:Conditional
The seller's registration number. This is information used by some countries.Occurrence:Conditional
The container that returns the seller's address to be used to contact them.Occurrence:Conditional
The first line of the street address.Occurrence:Conditional
The name of the country of the address.Occurrence:Conditional
The name of the county of the address.Occurrence:Conditional
The postal code of the address.Occurrence:Conditional
The state or province of the address.Occurrence:Always
An array of the seller's VAT (value added tax) IDs and the issuing country. VAT is a tax added by some European countries.Occurrence:Conditional
The two-letterISO 3166standard of the country issuing the seller's VAT (value added tax) ID. VAT is a tax added by some European countries.Occurrence:Conditional
The seller's VAT (value added tax) ID. VAT is a tax added by some European countries.Occurrence:Conditional
Provides required information about the manufacturer and/or supplier of the item.Occurrence:Conditional
The company name of the registered Economic Operator.Occurrence:Conditional
The first line of the registered Economic Operator's street address.Occurrence:Conditional
The second line, if any, of the registered Economic Operator's street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
The city of the registered Economic Operator's street address.Occurrence:Conditional
The state or province of the registered Economic Operator's street address.Occurrence:Conditional
The postal code of the registered Economic Operator's street address.Occurrence:Conditional
The two-letterISO 3166standard abbreviation of the country of the registered Economic Operator's address.Occurrence:Conditional
The registered Economic Operator's business phone number.Occurrence:Conditional
The registered Economic Operator's business email address.Occurrence:Conditional
The Waste Electrical and Electronic Equipment (WEEE) registration number required for any seller to place electrical and electronic equipment on the market in Germany. This manufacturer number is assigned to the first distributors of electrical and electronic equipment and comprises a country code and an 8-digit sequence of digits (e.g. “WEEE Reg. No. DE 12345678”).Occurrence:Conditional
The unique identifier of an eBay user across all eBay sites. This value does not change, even when a user changes their username.Occurrence:Conditional
The user name created by the seller for use on eBay.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Always
An identifier generated/incremented when a seller revises the item. There are two types of item revisions:Seller changes, such as changing the titleeBay system changes, such as changing the quantity when an item is purchasedThis ID is changedonlywhen the seller makes a change to the item. This means you cannot use this value to determine if the quantity has changed.Occurrence:Conditional
An array of shipping options containers that have the details about cost, carrier, etc. of one shipping option.Note:For items with calculated shipping, this array is only returned if theX-EBAY-C-ENDUSERCTXheader is supplied.Occurrence:Conditional
Any per item additional shipping costs for a multi-item purchase. For example, let's say the shipping cost for a power cord is $3. But for an additional cord, the shipping cost is only $1. So if you bought 3 cords, theshippingCostwould be $3 and this value would be $2 ($1 for each additional item).Occurrence:Conditional
The deadline date that the item must be purchased by in order to be received by the buyer within the delivery window (maxEstimatedDeliveryDateandminEstimatedDeliveryDatefields). This field is returned only for items that are eligible for 'Same Day Handling'. For these items, the value of this field is what is displayed in theDeliveryline on the View Item page.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Occurrence:Conditional
If the item is being shipped by the eBayGlobal Shipping program, this field returnsGLOBAL_SHIPPING.If the item is being shipped using the eBay International Shipping program, this field returnsINTERNATIONAL_SHIPPING.Otherwise, this field is null.Occurrence:Conditional
Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.Occurrence:Conditional
TheGlobal Shipping Programimport charges for this item.Occurrence:Conditional
The end date of the delivery window (latest projected delivery date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include the location of where the item is be shipped in thecontextualLocationvalues of theX-EBAY-C-ENDUSERCTXrequest header.Occurrence:Conditional
The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include the location of where the item is be shipped in thecontextualLocationvalues of theX-EBAY-C-ENDUSERCTXrequest header.Occurrence:Conditional
The number of items used when calculating the estimation information.This field will reflect the value input in thequantity_for_shipping_estimatequery parameter.Occurrence:Conditional
The name of the shipping provider, such as FedEx, or USPS.Occurrence:Always
The final shipping cost for all the items after all discounts are applied.This container will reflect the cost for the quantity specified through thequantity_for_shipping_estimatequery parameter.Note:The cost does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive cost. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
Indicates the class of the shipping cost.Valid Values:FIXED or CALCULATEDCode so that your app gracefully handles any future changes to this list.Occurrence:Always
The type of shipping service. For example, USPS First Class.Occurrence:Always
The container that returns the country and postal code of where the item is to be shipped. These values come from thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header. If the header is not submitted, marketplace is used.Occurrence:Conditional
The two-letterISO 3166standard of the country for where the item is to be shipped.Occurrence:Conditional
The zip code (postal code) for where the item is to be shipped.Occurrence:Conditional
Any trademark symbol, such as ™ or ®, that needs to be shown in superscript next to the shipping service name.Occurrence:Conditional
The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.Occurrence:Always
The container that returns the geographic regions to be included and excluded that define where the item can be shipped.Occurrence:Conditional
An array of containers that express the large geographical regions, countries, state/provinces, or special locations within a country where the seller is not willing to ship to.Occurrence:Conditional
The unique identifier of the shipping region. The value returned here is dependent on the correspondingregionTypevalue. TheregionIdvalue for a region does not vary based on the eBay marketplace. However, the correspondingregionNamevalue for a region is a localized, text-based description of the shipping region.If theregionTypevalue isWORLDWIDE, theregionIdvalue will also beWORLDWIDE.If theregionTypevalue isWORLD_REGION, theregionIdvalue will be one of the following:AFRICA,AMERICAS,ASIA,AUSTRALIA,CENTRAL_AMERICA_AND_CARIBBEAN,EUROPE,EUROPEAN_UNION,GREATER_CHINA,MIDDLE_EAST,NORTH_AMERICA,OCEANIA,SOUTH_AMERICA,SOUTHEAST_ASIAorCHANNEL_ISLANDS.If theregionTypevalue isCOUNTRY, theregionIdvalue will be the two-letter code for the country, as defined in theISO 3166standard.If theregionTypevalue isSTATE_OR_PROVINCE, theregionIdvalue will either be the two-letter code for US states and DC (as defined on thisSocial Security Administrationpage), or the two-letter code for Canadian provinces (as defined by thisCanada Postpage).If theregionTypevalue isCOUNTRY_REGION, theregionIdvalue may be one of following:_AH(if a seller is not willing to ship to Alaska/Hawaii),_PR(if the seller is not willing to ship to US Protectorates),_AP(if seller is not willing to ship to a US Army or Fleet Post Office), andPO_BOX(if the seller is not willing to ship to a Post Office Box).Occurrence:Conditional
A localized text string that indicates the name of the shipping region. The value returned here is dependent on the correspondingregionTypevalue.If theregionTypevalue isWORLDWIDE, theregionNamevalue will showWorldwide.If theregionTypevalue isWORLD_REGION, theregionNamevalue will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.If theregionTypevalue isCOUNTRY, theregionNamevalue will be a localized text string for any country in the world.If theregionTypevalue isSTATE_OR_PROVINCE, theregionNamevalue will be a localized text string for any US state or Canadian province.If theregionTypevalue isCOUNTRY_REGION, theregionNamevalue may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.Occurrence:Conditional
An enumeration value that indicates the level or type of shipping region.Valid Values:COUNTRY_REGION- Indicates the region is a domestic region or special location within a country.STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.WORLD_REGION- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.WORLDWIDE- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.For more detail on the actualregionName/regionIdvalues that will be returned based on theregionTypevalue, see theregionIdand/orregionNamefield descriptions.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.).Occurrence:Conditional
(Primary Item Aspect) The size of the item. For example, '7' for a size 7 shoe. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
(Primary Item Aspect) The sizing system of the country.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Valid Values:AU (Australia),BR (Brazil),CN (China),DE (Germany),EU (European Union),FR (France),IT (Italy),JP (Japan),MX (Mexico),US (USA),UK (United Kingdom)Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
(Primary Item Aspect) Text describing a size group in which the item would be included, such as regular, petite, plus, big-and-tall or maternity. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
A subtitle is optional and allows the seller to provide more information about the product, possibly including keywords that may assist with search results.Occurrence:Conditional
The container for the tax information for the item.Occurrence:Conditional
This field is only returned iftrue, and indicates that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence.Occurrence:Conditional
This indicates if tax was applied for the cost of the item.Occurrence:Conditional
This indicates if tax is applied for the shipping cost.Occurrence:Conditional
The container that returns the tax jurisdiction.Occurrence:Conditional
The region of the tax jurisdiction.Occurrence:Conditional
An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The identifier of the tax jurisdiction.Occurrence:Conditional
The percentage of tax.Occurrence:Conditional
This field indicates the type of tax that may be collected for the item.Occurrence:Conditional
The seller-created title of the item.Maximum Length:80 charactersOccurrence:Always
This indicates if the item a top-rated plus item. There are three benefits of a top-rated plus item: a  minimum 30-day money-back return policy, shipping the items in 1 business day with tracking provided, and the added comfort of knowing this item is from experienced sellers with the highest buyer ratings. See theTop Rated Plus ItemsandBecoming a Top Rated Seller and qualifying for Top Rated Plushelp topics for more information.Occurrence:Conditional
The URL to the image that shows the information on the tyre label.Occurrence:Conditional
This integer value indicates the number of different eBay users who have placed one or more bids on an auction item. This field is only applicable to auction items.Occurrence:Conditional
This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item.  This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The total number of items retrieved.Occurrence:Conditional
An array of warning messages. These types of errors do not prevent the method from executing but should be checked.Occurrence:Conditional
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
This sample returns a query on item IDs. These item IDs are returned in theitemIDfield.
The input isitem_idsURI parameter, which specifies the item ID of the item.
GEThttps://api.ebay.com/buy/browse/v1/item?item_ids=v1|1**********7|0,v1|2**********4|0
In this example, a query is run on multiple item group IDs.
This sample returns a query on multiple item group IDs. This ID is returned in theitem group IDfield.
The input isitem_group_IDsURI parameter, which specifies the group ID of the items.
GEThttps://api.ebay.com/buy/browse/v1/item?item_group_ids=2**********0,2**********6
Related topics
If you need help, contactDeveloper Technical Support.

```
v1|2**********2|0
```

```
v1|1**********2|4**********2
```

```
3**********9
```
- When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.
- When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.
- To retrieve theitemAffiliateWebUrlfield in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, seeHeader for affiliate information.
- If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for theshippingOptioncontainer, which includes shipping costs and delivery estimates, to be returned. For more information, seeHeader for shipping information accuracy.
- FIXED_PRICE- Indicates the buyer can purchase the item for a set price using the Buy It Now button.
- AUCTION- Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.
- BEST_OFFER- Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, seeMaking a Best Offer.
- CLASSIFIED_AD- Indicates that the final sales transaction is to be completed outside of the eBay environment.
- If the value of this field istrue, this indicates that the item can be purchased using theOrder API.
- If the value of this field isfalse, this indicates that the item cannot be purchased using theOrder APIand must be purchased on the eBay site.
- Display "More than 10 available" in your listing (if applicable)If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.
- Display the exact quantity in your itemsIf the seller enables this preference, theavailabilityThresholdTypeandavailabilityThresholdfields are not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.Note:Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity.
- If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.
- If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.
- The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.
- The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.
- STRING- Indicates the value returned is a string.
- STRING_ARRAY- Indicates the value returned is an array of strings.
- REPLACEMENT-  Indicates that the buyer has the option of receiving money back for the returned item, or they can choose to have the seller replace the item with an identical item.
- EXCHANGE- Indicates that the buyer has the option of receiving money back for the returned item, or they can exchange the item for another similar item.
- SELLER- Indicates the seller will pay for the shipping costs to return the item.
- BUYER- Indicates the buyer will pay for the shipping costs to return the item.
- EBAY_AT
- EBAY_BE
- EBAY_CH
- EBAY_DE
- EBAY_ES
- EBAY_FR
- EBAY_GB
- EBAY_IE
- EBAY_IT
- EBAY_PL
- Seller changes, such as changing the title
- eBay system changes, such as changing the quantity when an item is purchased
- COUNTRY_REGION- Indicates the region is a domestic region or special location within a country.
- STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.
- COUNTRY- Indicates the region is a single country.
- WORLD_REGION- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.
- WORLDWIDE- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
item_ids | array ofstring | A comma separated list of the unique identifiers of the items to retrieve (maximum 20).Note:In any given request, eitheritem_idsoritem_group_idscan be retrieved. Attempting to retrieve both will result in an error.RESTful Item ID Format:v1|#|#For a single SKU listing, pass in the item ID:v1|2**********2|0For a multi-SKU listing, pass in the identifier of the variation:v1|1**********2|4**********2For more information about item IDs for RESTful APIs, refer toItem ID legacy API compatibility overviewin theBuying Integration Guide.Occurrence:Conditional
item_group_ids | array ofstring | A comma separated list of the unique identifiers of the item groups being retrieved (maximum 10).Note:In any given request, eitheritem_idsoritem_group_idscan be retrieved. Attempting to retrieve both will result in an error.RESTful Group Item ID Format:############For example:3**********9Occurrence:Conditional
quantity_for_shipping_estimate | integer | This query parameter sets the item quantity to be used when calculating the shipping estimate information returned in theshippingOptionscontainer of the response.This value must be a positive integer value and should not exceed the quantity available in the listing. This field is not recommended for auction listings, as they will always have a quantity of 1.Occurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
Accept-Language | string | This header is used to indicate the natural language and locale preferred by the user for the response.This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.Occurrence:Conditional
X-EBAY-C-ENDUSERCTX | string | This header is can be used in following two situations:To retrieve theitemAffiliateWebUrlfield in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, seeHeader for affiliate information.If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for theshippingOptioncontainer, which includes shipping costs and delivery estimates, to be returned. For more information, seeHeader for shipping information accuracy.Occurrence:Optional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.Note:If the marketplace ID value is invalid or missing, the default value ofEBAY_USis used.SeeMarketplaceIdEnumfor a list of supported marketplaces.Default:EBAY_USOccurrence:Strongly Recommended
[/TABLE]

[TABLE]
Output container/field | Type | Description
items | array ofCoreItem | An arraylist of all the items.Occurrence:Conditional
items.additionalImages | array ofImage | An array of containers with the URLs for the images that are in addition to the primary image.  The primary image is returned in theimage.imageUrlfield.Occurrence:Conditional
items.additionalImages.height | integer | Reserved for future use.Occurrence:Conditional
items.additionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
items.additionalImages.width | integer | Reserved for future use.Occurrence:Conditional
items.adultOnly | boolean | This indicates if the item is for  adults only. For more information about adult-only items on eBay, seeAdult items policyfor sellers andAdult-Only items on eBayfor buyers.Occurrence:Always
items.ageGroup | string | (Primary Item Aspect) The age group for which the product is recommended. For example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.authenticityGuarantee | AuthenticityGuaranteeProgram | A container for information about whether an item is qualified for the Authenticity Guarantee program.Under the Authenticity Guarantee program, the seller ships a purchased item to a a third-party authenticator who inspects the item and provides an authentication card for it before the item is shipped to the buyer. If the buyer returns the item, the authenticator first verifies that it is the same item in the same condition before returning it to the seller.Note:Refer to theAuthenticity Guaranteepage for more information.Occurrence:Conditional
items.authenticityGuarantee.description | string | An indication that the item is qualified for the Authenticity Guarantee program.Occurrence:Conditional
items.authenticityGuarantee.termsWebUrl | string | The URL to the Authenticity Guarantee program terms of use.Occurrence:Conditional
items.authenticityVerification | AuthenticityVerificationProgram | A container for information about whether an item is from a verified seller.Occurrence:Conditional
items.authenticityVerification.description | string | An indication that the item is from a verified seller.Occurrence:Conditional
items.authenticityVerification.termsWebUrl | string | The URL to the Authenticity Verification program terms of use.Occurrence:Conditional
items.availableCoupons | array ofAvailableCoupon | A list of available coupons for the item.Occurrence:Conditional
items.availableCoupons.constraint | CouponConstraint | The limitations or restrictions of the coupon.Occurrence:Conditional
items.availableCoupons.constraint.expirationDate | string | This timestamp provides the expiration date of the coded coupon.Occurrence:Conditional
items.availableCoupons.discountAmount | Amount | The discount amount after the coupon is applied.Occurrence:Conditional
items.availableCoupons.discountAmount.currency | CurrencyCodeEnum | The list of valid currencies. EachISO 4217currency code includes the currency name followed by the numeric value.For example, the Canadian Dollar code (CAD) would take the following form:Canadian Dollar, 124.Occurrence:Conditional
items.availableCoupons.discountAmount.value | string | The value of the discounted amount.Occurrence:Conditional
items.availableCoupons.discountType | CouponDiscountType | The type of discount that the coupon applies.Occurrence:Conditional
items.availableCoupons.message | string | A description of the coupon.Note:The value returned in thetermsWebUrlfield should appear for all experiences when displaying coupons. The value in theavailableCoupons.messagefield must also be included if returned in the API response.Occurrence:Conditional
items.availableCoupons.redemptionCode | string | The coupon code.Occurrence:Conditional
items.availableCoupons.termsWebUrl | string | The URL to the coupon terms of use.Note:The value returned in thetermsWebUrlfield should appear for all experiences when displaying coupons. The value in theavailableCoupons.messagefield must also be included if returned in the API response.Occurrence:Conditional
items.bidCount | integer | This integer value indicates the total number of bids that have been placed against an auction item. This field is returned only for auction items.Occurrence:Conditional
items.brand | string | (Primary Item Aspect) The name brand of the item, such as Nike, Apple, etc.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.buyingOptions | array ofstring | A comma separated list of all the purchase options available for the item. The values returned are:FIXED_PRICE- Indicates the buyer can purchase the item for a set price using the Buy It Now button.AUCTION- Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.BEST_OFFER- Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, seeMaking a Best Offer.CLASSIFIED_AD- Indicates that the final sales transaction is to be completed outside of the eBay environment.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.categoryId | string | The ID of the leaf category for this item. A leaf category is the lowest level in that category and has no children.Occurrence:Always
items.categoryPath | string | Text that shows the category hierarchy of the item. For example: Computers/Tablets & Networking, Laptops & Netbooks, PC Laptops & NetbooksOccurrence:Always
items.color | string | (Primary Item Aspect) Text describing the color of the item.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.charityTerms | ItemCharityTerms | This container returns any applicable charity information associated with the specified item.This container is only returned if thefieldgroupsquery parameter is set toCHARITY_DETAILS.Occurrence:Conditional
items.charityTerms.charityOrgId | string | The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds from the item.Occurrence:Conditional
items.charityTerms.donationPercentage | number | The percentage of the purchase price of the item that the charitable organization (identified in thecharityOrgIdfield) will receive for each sale.Occurrence:Conditional
items.charityTerms.LogoImage | Image | The details of the charity's logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
items.charityTerms.LogoImage.height | integer | Reserved for future use.Occurrence:Conditional
items.charityTerms.LogoImage.imageUrl | string | The URL of the image.Occurrence:Conditional
items.charityTerms.LogoImage.width | integer | Reserved for future use.Occurrence:Conditional
items.charityTerms.name | string | The name of the charity organization.Occurrence:Conditional
items.charityTerms.website | string | The URL to the charity's eBay page.Occurrence:Conditional
items.condition | string | A short text description for the condition of the item, such as New or Used. For a list of condition names, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.conditionDescription | string | A full text description for the condition of the item. This field elaborates on the value specified in theconditionfield and provides full details for the condition of the item.Occurrence:Conditional
items.conditionId | string | The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.currentBidPrice | ConvertedAmount | The container that returns the current highest bid for an auction item. The value (string) field shows the dollar value of the current highest bid, and the currency (3-digit ISO code) field denotes the currency associated with that bid value. This container will only be returned for auction items.Occurrence:Conditional
items.currentBidPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.currentBidPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.currentBidPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.currentBidPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.description | string | The full description of the item that was created by the seller. This can be plain text or rich content and can be very large.Occurrence:Always
items.eligibleForInlineCheckout | boolean | This field indicates if the item can be purchased using the BuyOrder API.If the value of this field istrue, this indicates that the item can be purchased using theOrder API.If the value of this field isfalse, this indicates that the item cannot be purchased using theOrder APIand must be purchased on the eBay site.Occurrence:Always
items.enabledForGuestCheckout | boolean | This indicates if the item can be purchased using Guest Checkout in theOrder API. You can use this flag to exclude items from your inventory that are not eligible for Guest Checkout, such as gift cards.Occurrence:Always
items.energyEfficiencyClass | string | This indicates theEuropean energy efficiencyrating (EEK) of the item. This field is returned only if the seller specified the energy efficiency rating.The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.When the manufacturer's specifications for this item are available, the link to this information is returned in theproductFicheWebUrlfield.Occurrence:Conditional
items.epid | string | An EPID is the eBay product identifier of a product from the eBay product catalog.  This indicates the product in which the item belongs.Occurrence:Conditional
items.estimatedAvailabilities | array ofEstimatedAvailability | The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Occurrence:Conditional
items.estimatedAvailabilities.availabilityThreshold | integer | This field is return only when the seller sets their 'display item quantity' preference toDisplay "More than 10 available" in your listing (if applicable). The value of this field will be "10", which is the threshold value.Code so that your app gracefully handles any future changes to this value.Occurrence:Conditional
items.estimatedAvailabilities.availabilityThresholdType | AvailabilityThresholdEnum | This field is return only when the seller sets theirDisplay Item Quantitypreference toDisplay "More than 10 available" in your listing (if applicable). The value of this field will beMORE_THAN. This indicates that the seller has more than the 'quantity display preference', which is 10, in stock for this item.The following are the display item quantity preferences the seller can set.Display "More than 10 available" in your listing (if applicable)If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.Display the exact quantity in your itemsIf the seller enables this preference, theavailabilityThresholdTypeandavailabilityThresholdfields are not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.Note:Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity.Code so that your app gracefully handles any future changes to these preferences.Occurrence:Conditional
items.estimatedAvailabilities.deliveryOptions | array ofDeliveryOptionsEnum | An array of available delivery options.Valid Values:SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, PICKUP_DROP_OFF, or DIGITAL_DELIVERYCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.estimatedAvailabilities.estimatedAvailabilityStatus | AvailabilityStatusEnum | An enumeration value representing the inventory status of this item.Note:Be sure to review theitemEndDatefield to determine whether the item is available for purchase.Valid Values:IN_STOCK, LIMITED_STOCK, or OUT_OF_STOCKCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.estimatedAvailabilities.estimatedAvailableQuantity | integer | The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Note:To see if a listing is available for purchase, review theitemEndDateandestimatedAvailablityStatusfields. If the item has anEndDatein the past, or theestimatedAvailabilityStatusisOUT_OF_STOCK, the item is unavailable for purchase.Occurrence:Conditional
items.estimatedAvailabilities.estimatedRemainingQuantity | integer | The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Note:To see if a listing is available for purchase, review theitemEndDateandestimatedAvailablityStatusfields. If the item has anEndDatein the past, or theestimatedAvailabilityStatusisOUT_OF_STOCK, the item is unavailable for purchase.Occurrence:Conditional
items.estimatedAvailabilities.estimatedSoldQuantity | integer | The estimated number of this item that have been sold.Occurrence:Conditional
items.gender | string | (Primary Item Aspect) The gender for the item. This is used for items that could vary by gender, such as clothing. For example: male, female, or unisex. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.gtin | string | The unique Global Trade Item number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
items.image | Image | The URL of the primary image of the item. The other images of the item are returned in theadditionalImagescontainer.Occurrence:Always
items.image.height | integer | Reserved for future use.Occurrence:Conditional
items.image.imageUrl | string | The URL of the image.Occurrence:Conditional
items.image.width | integer | Reserved for future use.Occurrence:Conditional
items.immediatePay | boolean | A value oftrueindicates that the seller requires immediate payment from the buyer when purchasing an item.Note:It is possible for this field to be set totrue, but not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyers' purchases that involve the Best Offer feature, or for offline transactions.Occurrence:Always
items.inferredEpid | string | The ePID (eBay Product ID of a product from the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.If the seller provided an ePID for the item, the seller's value is returned in theepidfield.Note:This field is returned only for authorized Partners.Occurrence:Conditional
items.itemAffiliateWebUrl | string | The URL to the View Item page of the item which includes the affiliate tracking ID.Note:In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.TheitemAffiliateWebUrlis only returned if:The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.Occurrence:Conditional
items.itemCreationDate | string | A timestamp that indicates the date and time an item listing was created.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
items.itemEndDate | string | A timestamp that indicates the date and time an auction listing will end.If a fixed-price listing has ended, this field indicates the date and time the listing ended.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
items.itemId | string | The unique RESTful identifier of the item.Occurrence:Always
items.itemLocation | Address | The physical location of the item.Occurrence:Conditional
items.itemLocation.addressLine1 | string | The first line of the street address.Note:This is conditionally returned in theitemLocationfield.Occurrence:Conditional
items.itemLocation.addressLine2 | string | The second line of the street address. This field is not always used, but can be used for "Suite Number" or "Apt Number".Occurrence:Conditional
items.itemLocation.city | string | The city of the address.Occurrence:Always
items.itemLocation.country | CountryCodeEnum | The two-letterISO 3166standard code for the country of the address.Occurrence:Always
items.itemLocation.county | string | The county of the address.Occurrence:Conditional
items.itemLocation.postalCode | string | The postal code (or zip code in US) code of the address. Sellers set a postal code (or zip code in US) for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned initemLocation.postalCodevia the API.Occurrence:Conditional
items.itemLocation.stateOrProvince | string | The state or province of the address.Note:This is conditionally returned in theitemLocationfield.Occurrence:Conditional
items.itemWebUrl | string | The URL of the View Item page of the item. This enables you to include a "Report Item on eBay" link that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.Occurrence:Always
items.legacyItemId | string | The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Always
items.localizedAspects | array ofTypedNameValue | An array of containers that show the complete list of the aspect name/value pairs that describe the variation of the item.Occurrence:Conditional
items.localizedAspects.name | string | The text representing the name of the aspect for the name/value pair, such as Color.Occurrence:Conditional
items.localizedAspects.type | ValueTypeEnum | This indicates if the value being returned is a string or an array of values.Valid Values:STRING- Indicates the value returned is a string.STRING_ARRAY- Indicates the value returned is an array of strings.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.localizedAspects.value | string | The value of the aspect for the name/value pair, such as Red.Occurrence:Conditional
items.lotSize | integer | The number of items in a lot. In other words, a lot size is the number of items that are being sold together.A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot,  such as the package of batteries shown in the example below.ItemLot DefinitionLot SizeA package of 24 AA batteriesA box of 10 packages10A P235/75-15 Goodyear tire4 tires4Fashion Jewelry RingsPackage of 100 assorted rings100Note:Lots are not supported in all categories.Occurrence:Conditional | Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size
A package of 24 AA batteries | A box of 10 packages | 10
A P235/75-15 Goodyear tire | 4 tires | 4
Fashion Jewelry Rings | Package of 100 assorted rings | 100
items.marketingPrice | MarketingPrice | The original price and the discount amount and percentage.Occurrence:Conditional
items.marketingPrice.discountAmount | ConvertedAmount | This container returns the monetary amount of the seller discount.Occurrence:Conditional
items.marketingPrice.discountAmount.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.marketingPrice.discountAmount.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.marketingPrice.discountAmount.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.marketingPrice.discountAmount.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.marketingPrice.discountPercentage | string | This field expresses the percentage of the seller discount based on the value in theoriginalPricecontainer.Occurrence:Conditional
items.marketingPrice.originalPrice | ConvertedAmount | This container returns the monetary amount of the item without the discount.Occurrence:Conditional
items.marketingPrice.originalPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.marketingPrice.originalPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.marketingPrice.originalPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.marketingPrice.originalPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.marketingPrice.priceTreatment | PriceTreatmentEnum | Indicates the pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects the way and where the discounted price can be displayed.Occurrence:Conditional
items.material | string | (Primary Item Aspect) Text describing what the item is made of. For example, silk. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.minimumPriceToBid | ConvertedAmount | The minimum price of the next bid, which means to place a bid it must be equal to or greater than this amount. If the auction hasn't received any bids, the minimum bid price is the same as the starting bid. Otherwise, the minimum bid price is equal to the current bid plus the bid increment.  For details about bid increments, seeAutomatic bidding.Occurrence:Conditional
items.minimumPriceToBid.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.minimumPriceToBid.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.minimumPriceToBid.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.minimumPriceToBid.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.mpn | string | The manufacturer's part number, which is a unique number that identifies a specific product. To identify the product, this is always used along with brand.Occurrence:Conditional
items.pattern | string | (Primary Item Aspect) Text describing the pattern used on the item. For example, paisley. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.paymentMethods | array ofPaymentMethod | The payment methods for the item, including the payment method types, brands, and instructions for the buyer.Occurrence:Conditional
items.paymentMethods.paymentMethodType | PaymentMethodTypeEnum | The payment method type, such as credit card or cash.Occurrence:Conditional
items.paymentMethods.paymentMethodBrands | array ofPaymentMethodBrand | The payment method brands, including the payment method brand type and logo image.Occurrence:Conditional
items.paymentMethods.paymentMethodBrands.paymentMethodBrandType | PaymentMethodBrandEnum | The payment method brand, such as Visa or PayPal.Occurrence:Conditional
items.paymentMethods.paymentMethodBrands.logoImage | Image | The details of the logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
items.paymentMethods.paymentMethodBrands.logoImage.height | integer | Reserved for future use.Occurrence:Conditional
items.paymentMethods.paymentMethodBrands.logoImage.imageUrl | string | The URL of the image.Occurrence:Conditional
items.paymentMethods.paymentMethodBrands.logoImage.width | integer | Reserved for future use.Occurrence:Conditional
items.paymentMethods.paymentInstructions | array ofPaymentInstructionEnum | The payment instructions for the buyer, such ascash in personorcontact seller.Occurrence:Conditional
items.paymentMethods.sellerInstructions | array ofSellerInstructionEnum | The seller instructions to the buyer, such asaccepts credit cardsorsee description.Occurrence:Conditional
items.price | ConvertedAmount | The cost of just the item. This amount does not include any adjustments such as discounts or shipping costs.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
items.price.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.price.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.price.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.price.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.priceDisplayCondition | PriceDisplayConditionEnum | Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.Occurrence:Conditional
items.primaryItemGroup | ItemGroupSummary | The container that returns details of a primary item group (parent ID of an item group). An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.Note:This container is returned if theitem_idin the request is for an item group (items with variations, such as color and size). This container is also returned on a request foritem_group_ids.Occurrence:Conditional
items.primaryItemGroup.itemGroupAdditionalImages | array ofImage | An array of containers with the URLs for images that are in addition to the primary image of the item group.  The primary image is returned in theitemGroupImagefield.Occurrence:Conditional
items.primaryItemGroup.itemGroupAdditionalImages.height | integer | Reserved for future use.Occurrence:Conditional
items.primaryItemGroup.itemGroupAdditionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
items.primaryItemGroup.itemGroupAdditionalImages.width | integer | Reserved for future use.Occurrence:Conditional
items.primaryItemGroup.itemGroupHref | string | The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
items.primaryItemGroup.itemGroupId | string | The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
items.primaryItemGroup.itemGroupImage | Image | The URL of the primary image of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
items.primaryItemGroup.itemGroupImage.height | integer | Reserved for future use.Occurrence:Conditional
items.primaryItemGroup.itemGroupImage.imageUrl | string | The URL of the image.Occurrence:Conditional
items.primaryItemGroup.itemGroupImage.width | integer | Reserved for future use.Occurrence:Conditional
items.primaryItemGroup.itemGroupTitle | string | The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
items.primaryItemGroup.itemGroupType | ItemGroupTypeEnum | An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
items.primaryProductReviewRating | ReviewRating | The container that returns the product rating details, such as review count, rating histogram, and average rating.Occurrence:Conditional
items.primaryProductReviewRating.averageRating | string | The average rating given to a product based on customer reviews.Occurrence:Conditional
items.primaryProductReviewRating.ratingHistograms | array ofRatingHistogram | An array of containers for the product rating histograms that shows the review counts and the product rating.Occurrence:Conditional
items.primaryProductReviewRating.ratingHistograms.count | integer | The total number of user ratings that the product has received.Occurrence:Conditional
items.primaryProductReviewRating.ratingHistograms.rating | string | This is the average rating for the product. As part of a product review, users rate the product. Products are rated from one star (terrible) to five stars (excellent), with each star having a corresponding point value - one star gets 1 point, two stars get 2 points, and so on. If a product had one four-star rating and one five-star rating, its average rating would be4.5, and this is the value that would appear in this field.Occurrence:Conditional
items.primaryProductReviewRating.reviewCount | integer | The total number of reviews for the item.Occurrence:Conditional
items.priorityListing | boolean | This field is returned astrueif the listing is part of a Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent sales activity.For more information, seePromoted Listings.Occurrence:Always
items.product | Product | The container that returns the product information of the item.Occurrence:Conditional
items.product.additionalImages | array ofImage | An array of containers with the URLs for the product images that are in addition to the primary image.Occurrence:Conditional
items.product.additionalImages.height | integer | Reserved for future use.Occurrence:Conditional
items.product.additionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
items.product.additionalImages.width | integer | Reserved for future use.Occurrence:Conditional
items.product.additionalProductIdentities | array ofAdditionalProductIdentity | An array of product identifiers associated with the item. This container is returned if the seller has associated the eBay Product Identifier (ePID) with the item and in the requestfieldgroupsis set toPRODUCT.Occurrence:Conditional
items.product.additionalProductIdentities.productIdentity | array ofProductIdentity | An array of product identifier/value pairs for the product associated with the item. This is returned if the seller has associated the eBay Product Identifier (ePID) with the item and the request hasfieldgroupsset toPRODUCT.The following table shows what is returned, based on the item information provided by the seller, whenfieldgroupsis set toPRODUCT.ePID ProvidedProduct ID(s) ProvidedResponseNoNoTheAdditionalProductIdentitycontainer isnotreturned.NoYesTheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.YesNoTheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product.YesYesTheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.Occurrence:Conditional | ePID Provided | Product ID(s) Provided | Response | No | No | TheAdditionalProductIdentitycontainer isnotreturned. | No | Yes | TheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer. | Yes | No | TheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product. | Yes | Yes | TheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
ePID Provided | Product ID(s) Provided | Response
No | No | TheAdditionalProductIdentitycontainer isnotreturned.
No | Yes | TheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
Yes | No | TheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product.
Yes | Yes | TheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
items.product.additionalProductIdentities.productIdentity.identifierType | string | The type of product identifier, such as UPC and EAN.Occurrence:Conditional
items.product.additionalProductIdentities.productIdentity.identifierValue | string | The product identifier value.Occurrence:Conditional
items.product.aspectGroups | array ofAspectGroup | An array of containers for the product aspects. Each group contains the aspect group name and the aspect name/value pairs.Occurrence:Conditional
items.product.aspectGroups.aspects | array ofAspect | An array of the name/value pairs for the aspects of the product. For example: BRAND/AppleOccurrence:Conditional
items.product.aspectGroups.aspects.localizedName | string | The text representing the name of the aspect for the name/value pair, such as Brand.Occurrence:Conditional
items.product.aspectGroups.aspects.localizedValues | array ofstring | The text representing the value of the aspect for the name/value pair, such as Apple.Occurrence:Conditional
items.product.aspectGroups.localizedGroupName | string | The name of a group of aspects.In the following example,Product IdentifiersandProcessare product aspect group names. Under the group name are the product aspect name/value pairs.Product IdentifiersBrand/AppleProduct Family/iMacProcessorProcessor Type/IntelProcessor Speed/3.10Occurrence:Conditional
items.product.brand | string | The brand associated with product. To identify the product, this is always used along with MPN (manufacturer part number).Occurrence:Conditional
items.product.description | string | The rich description of an eBay product, which might contain HTML.Occurrence:Conditional
items.product.gtins | array ofstring | An array of all the possible GTINs values associated with the product. A GTIN is a unique Global Trade Item number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
items.product.image | Image | The primary image of the product. This is often a stock photo.Occurrence:Conditional
items.product.image.height | integer | Reserved for future use.Occurrence:Conditional
items.product.image.imageUrl | string | The URL of the image.Occurrence:Conditional
items.product.image.width | integer | Reserved for future use.Occurrence:Conditional
items.product.mpns | array ofstring | An array of all possible MPN values associated with the product. A MPNs is manufacturer part number of the product. To identify the product, this is always used along with brand.Occurrence:Conditional
items.product.title | string | The title of the product.Occurrence:Conditional
items.productFicheWebUrl | string | The URL of a page containing the manufacturer's specification of this item, which helps buyers make a purchasing decision. This information is available only for items that include the European energy efficiency rating (EEK) but is not available forallitems with an EEK rating and is returned only if this information is available. The EEK rating of the item is returned in theenergyEfficiencyClassfield.Occurrence:Conditional
items.qualifiedPrograms | array ofstring | An array of the qualified programs available for the item, such as EBAY_PLUS, AUTHENTICITY_GUARANTEE, and AUTHENTICITY_VERIFICATION.eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings. Sellers must commit to next-day delivery of those items.Note:eBay Plus is only available as a listing feature on the eBay Australia marketplace.The eBayAuthenticity Guaranteeprogram enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.Occurrence:Conditional
items.quantityLimitPerBuyer | integer | The maximum number for a specific item that one buyer can purchase.Occurrence:Conditional
items.reservePriceMet | boolean | This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.Note:This is returned only for auctions that have a reserve price.Occurrence:Conditional
items.returnTerms | ItemReturnTerms | The container that returns an overview of the seller's return policy.Occurrence:Conditional
items.returnTerms.extendedHolidayReturnsOffered | boolean | This indicates if the seller has enabled the Extended Holiday Returns feature on the item. Extended Holiday Returns are only applicable during the US holiday season, and gives buyers extra time to return an item. This 'extra time' will typically extend beyond what is set through thereturnPeriodvalue.Occurrence:Conditional
items.returnTerms.refundMethod | RefundMethodEnum | An enumeration value that indicates how a buyer is refunded when an item is returned.Valid Values:MONEY_BACK or MERCHANDISE_CREDITCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.returnTerms.restockingFeePercentage | string | This string field indicates the restocking fee percentage that the seller has set on the item. Sellers have the option of setting no restocking fee for an item, or they can set the percentage to 10, 15, or 20 percent. So, if the cost of the item was $100, and the restocking percentage was 20 percent, the buyer would be charged $20 to return that item, so instead of receiving a $100 refund, they would receive $80 due to the restocking fee.Occurrence:Conditional
items.returnTerms.returnInstructions | string | Text written by the seller describing what the buyer needs to do in order to return the item.Occurrence:Conditional
items.returnTerms.returnMethod | ReturnMethodEnum | An enumeration value that indicates the alternative methods for a full refund when an item is returned. This field is returned if the seller offers the buyer an item replacement or exchange instead of a monetary refund.Valid Values:REPLACEMENT-  Indicates that the buyer has the option of receiving money back for the returned item, or they can choose to have the seller replace the item with an identical item.EXCHANGE- Indicates that the buyer has the option of receiving money back for the returned item, or they can exchange the item for another similar item.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.returnTerms.returnPeriod | TimeDuration | The amount of time the buyer has to return the item after the purchase date.Occurrence:Conditional
items.returnTerms.returnPeriod.unit | TimeDurationUnitEnum | An enumeration value that indicates the units of the time span (e.g.,HOURS). The enumeration value in this field defines the period of time being used to measure the duration.Refer toTimeDurationUnitEnumfor the list of supported values.Occurrence:Conditional
items.returnTerms.returnPeriod.value | integer | Retrieves the duration of the time span (no units). The value in this field indicates the number of years, months, days, hours, or minutes in the defined period.Occurrence:Conditional
items.returnTerms.returnsAccepted | boolean | Indicates whether the seller accepts returns for the item.Occurrence:Conditional
items.returnTerms.returnShippingCostPayer | ReturnShippingCostPayerEnum | This enumeration value indicates whether the buyer or seller is responsible for return shipping costs when an item is returned.Valid Values:SELLER- Indicates the seller will pay for the shipping costs to return the item.BUYER- Indicates the buyer will pay for the shipping costs to return the item.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.seller | SellerDetail | The container that returns basic and detailed about the seller of the item, such as name, feedback score, and contact information.Occurrence:Always
items.seller.feedbackPercentage | string | The percentage of the total positive feedback.Occurrence:Always
items.seller.feedbackScore | integer | The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Always
items.seller.sellerAccountType | string | This indicates if the seller is a business or an individual. This is determined when the seller registers with eBay. If they register for a business account, this value will beBUSINESS. If they register for a private account, this value will beINDIVIDUAL. This designation is required by the tax laws in the following countries:This field is applicable only on the following marketplaces:EBAY_ATEBAY_BEEBAY_CHEBAY_DEEBAY_ESEBAY_FREBAY_GBEBAY_IEEBAY_ITEBAY_PLNote:This field will be returned empty on unsupported marketplaces.Valid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
items.seller.sellerLegalInfo | SellerLegalInfo | The container with the seller's contact info and fields that are required by law.Occurrence:Conditional
items.seller.sellerLegalInfo.email | string | The seller's business email address.Occurrence:Conditional
items.seller.sellerLegalInfo.fax | string | The seller' business fax number.Occurrence:Conditional
items.seller.sellerLegalInfo.imprint | string | This is a free-form string created by the seller. This is information often found on business cards, such as address. This is information used by some countries.Occurrence:Conditional
items.seller.sellerLegalInfo.legalContactFirstName | string | The seller's first name.Occurrence:Conditional
items.seller.sellerLegalInfo.legalContactLastName | string | The seller's last name.Occurrence:Conditional
items.seller.sellerLegalInfo.name | string | The name of the seller's business.Occurrence:Conditional
items.seller.sellerLegalInfo.phone | string | The seller's business phone number.Occurrence:Conditional
items.seller.sellerLegalInfo.registrationNumber | string | The seller's registration number. This is information used by some countries.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress | LegalAddress | The container that returns the seller's address to be used to contact them.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.addressLine1 | string | The first line of the street address.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.addressLine2 | string | The second line of the street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.city | string | The city of the address.Occurrence:Always
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.country | CountryCodeEnum | The two-letterISO 3166standard code for the country of the address.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.countryName | string | The name of the country of the address.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.county | string | The name of the county of the address.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.postalCode | string | The postal code of the address.Occurrence:Conditional
items.seller.sellerLegalInfo.sellerProvidedLegalAddress.stateOrProvince | string | The state or province of the address.Occurrence:Always
items.seller.sellerLegalInfo.termsOfService | string | This is a free-form string created by the seller. This is the seller's terms or condition, which is in addition to the seller's return policies.Occurrence:Conditional
items.seller.sellerLegalInfo.vatDetails | array ofVatDetail | An array of the seller's VAT (value added tax) IDs and the issuing country. VAT is a tax added by some European countries.Occurrence:Conditional
items.seller.sellerLegalInfo.vatDetails.issuingCountry | CountryCodeEnum | The two-letterISO 3166standard of the country issuing the seller's VAT (value added tax) ID. VAT is a tax added by some European countries.Occurrence:Conditional
items.seller.sellerLegalInfo.vatDetails.vatId | string | The seller's VAT (value added tax) ID. VAT is a tax added by some European countries.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator | EconomicOperator | Provides required information about the manufacturer and/or supplier of the item.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.companyName | string | The company name of the registered Economic Operator.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.addressLine1 | string | The first line of the registered Economic Operator's street address.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.addressLine2 | string | The second line, if any, of the registered Economic Operator's street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.city | string | The city of the registered Economic Operator's street address.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.stateOrProvince | string | The state or province of the registered Economic Operator's street address.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.postalCode | string | The postal code of the registered Economic Operator's street address.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.country | string | The two-letterISO 3166standard abbreviation of the country of the registered Economic Operator's address.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.phone | string | The registered Economic Operator's business phone number.Occurrence:Conditional
items.seller.sellerLegalInfo.economicOperator.email | string | The registered Economic Operator's business email address.Occurrence:Conditional
items.seller.sellerLegalInfo.weeeNumber | string | The Waste Electrical and Electronic Equipment (WEEE) registration number required for any seller to place electrical and electronic equipment on the market in Germany. This manufacturer number is assigned to the first distributors of electrical and electronic equipment and comprises a country code and an 8-digit sequence of digits (e.g. “WEEE Reg. No. DE 12345678”).Occurrence:Conditional
items.seller.userId | string | The unique identifier of an eBay user across all eBay sites. This value does not change, even when a user changes their username.Occurrence:Conditional
items.seller.username | string | The user name created by the seller for use on eBay.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Always
items.sellerItemRevision | string | An identifier generated/incremented when a seller revises the item. There are two types of item revisions:Seller changes, such as changing the titleeBay system changes, such as changing the quantity when an item is purchasedThis ID is changedonlywhen the seller makes a change to the item. This means you cannot use this value to determine if the quantity has changed.Occurrence:Conditional
items.shippingOptions | array ofShippingOption | An array of shipping options containers that have the details about cost, carrier, etc. of one shipping option.Note:For items with calculated shipping, this array is only returned if theX-EBAY-C-ENDUSERCTXheader is supplied.Occurrence:Conditional
items.shippingOptions.additionalShippingCostPerUnit | ConvertedAmount | Any per item additional shipping costs for a multi-item purchase. For example, let's say the shipping cost for a power cord is $3. But for an additional cord, the shipping cost is only $1. So if you bought 3 cords, theshippingCostwould be $3 and this value would be $2 ($1 for each additional item).Occurrence:Conditional
items.shippingOptions.additionalShippingCostPerUnit.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.shippingOptions.additionalShippingCostPerUnit.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.shippingOptions.additionalShippingCostPerUnit.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.shippingOptions.additionalShippingCostPerUnit.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.shippingOptions.cutOffDateUsedForEstimate | string | The deadline date that the item must be purchased by in order to be received by the buyer within the delivery window (maxEstimatedDeliveryDateandminEstimatedDeliveryDatefields). This field is returned only for items that are eligible for 'Same Day Handling'. For these items, the value of this field is what is displayed in theDeliveryline on the View Item page.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Occurrence:Conditional
items.shippingOptions.fulfilledThrough | FulfilledThroughEnum | If the item is being shipped by the eBayGlobal Shipping program, this field returnsGLOBAL_SHIPPING.If the item is being shipped using the eBay International Shipping program, this field returnsINTERNATIONAL_SHIPPING.Otherwise, this field is null.Occurrence:Conditional
items.shippingOptions.guaranteedDelivery | boolean | Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.Occurrence:Conditional
items.shippingOptions.importCharges | ConvertedAmount | TheGlobal Shipping Programimport charges for this item.Occurrence:Conditional
items.shippingOptions.importCharges.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.shippingOptions.importCharges.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.shippingOptions.importCharges.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.shippingOptions.importCharges.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.shippingOptions.maxEstimatedDeliveryDate | string | The end date of the delivery window (latest projected delivery date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include the location of where the item is be shipped in thecontextualLocationvalues of theX-EBAY-C-ENDUSERCTXrequest header.Occurrence:Conditional
items.shippingOptions.minEstimatedDeliveryDate | string | The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include the location of where the item is be shipped in thecontextualLocationvalues of theX-EBAY-C-ENDUSERCTXrequest header.Occurrence:Conditional
items.shippingOptions.quantityUsedForEstimate | integer | The number of items used when calculating the estimation information.This field will reflect the value input in thequantity_for_shipping_estimatequery parameter.Occurrence:Conditional
items.shippingOptions.shippingCarrierCode | string | The name of the shipping provider, such as FedEx, or USPS.Occurrence:Always
items.shippingOptions.shippingCost | ConvertedAmount | The final shipping cost for all the items after all discounts are applied.This container will reflect the cost for the quantity specified through thequantity_for_shipping_estimatequery parameter.Note:The cost does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive cost. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
items.shippingOptions.shippingCost.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.shippingOptions.shippingCost.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.shippingOptions.shippingCost.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.shippingOptions.shippingCost.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.shippingOptions.shippingCostType | string | Indicates the class of the shipping cost.Valid Values:FIXED or CALCULATEDCode so that your app gracefully handles any future changes to this list.Occurrence:Always
items.shippingOptions.shippingServiceCode | string | The type of shipping service. For example, USPS First Class.Occurrence:Always
items.shippingOptions.shipToLocationUsedForEstimate | ShipToLocation | The container that returns the country and postal code of where the item is to be shipped. These values come from thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header. If the header is not submitted, marketplace is used.Occurrence:Conditional
items.shippingOptions.shipToLocationUsedForEstimate.country | CountryCodeEnum | The two-letterISO 3166standard of the country for where the item is to be shipped.Occurrence:Conditional
items.shippingOptions.shipToLocationUsedForEstimate.postalCode | string | The zip code (postal code) for where the item is to be shipped.Occurrence:Conditional
items.shippingOptions.trademarkSymbol | string | Any trademark symbol, such as ™ or ®, that needs to be shown in superscript next to the shipping service name.Occurrence:Conditional
items.shippingOptions.type | string | The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.Occurrence:Always
items.shipToLocations | ShipToLocations | The container that returns the geographic regions to be included and excluded that define where the item can be shipped.Occurrence:Conditional
items.shipToLocations.regionExcluded | array ofShipToRegion | An array of containers that express the large geographical regions, countries, state/provinces, or special locations within a country where the seller is not willing to ship to.Occurrence:Conditional
items.shipToLocations.regionExcluded.regionId | string | The unique identifier of the shipping region. The value returned here is dependent on the correspondingregionTypevalue. TheregionIdvalue for a region does not vary based on the eBay marketplace. However, the correspondingregionNamevalue for a region is a localized, text-based description of the shipping region.If theregionTypevalue isWORLDWIDE, theregionIdvalue will also beWORLDWIDE.If theregionTypevalue isWORLD_REGION, theregionIdvalue will be one of the following:AFRICA,AMERICAS,ASIA,AUSTRALIA,CENTRAL_AMERICA_AND_CARIBBEAN,EUROPE,EUROPEAN_UNION,GREATER_CHINA,MIDDLE_EAST,NORTH_AMERICA,OCEANIA,SOUTH_AMERICA,SOUTHEAST_ASIAorCHANNEL_ISLANDS.If theregionTypevalue isCOUNTRY, theregionIdvalue will be the two-letter code for the country, as defined in theISO 3166standard.If theregionTypevalue isSTATE_OR_PROVINCE, theregionIdvalue will either be the two-letter code for US states and DC (as defined on thisSocial Security Administrationpage), or the two-letter code for Canadian provinces (as defined by thisCanada Postpage).If theregionTypevalue isCOUNTRY_REGION, theregionIdvalue may be one of following:_AH(if a seller is not willing to ship to Alaska/Hawaii),_PR(if the seller is not willing to ship to US Protectorates),_AP(if seller is not willing to ship to a US Army or Fleet Post Office), andPO_BOX(if the seller is not willing to ship to a Post Office Box).Occurrence:Conditional
items.shipToLocations.regionExcluded.regionName | string | A localized text string that indicates the name of the shipping region. The value returned here is dependent on the correspondingregionTypevalue.If theregionTypevalue isWORLDWIDE, theregionNamevalue will showWorldwide.If theregionTypevalue isWORLD_REGION, theregionNamevalue will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.If theregionTypevalue isCOUNTRY, theregionNamevalue will be a localized text string for any country in the world.If theregionTypevalue isSTATE_OR_PROVINCE, theregionNamevalue will be a localized text string for any US state or Canadian province.If theregionTypevalue isCOUNTRY_REGION, theregionNamevalue may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.Occurrence:Conditional
items.shipToLocations.regionExcluded.regionType | RegionTypeEnum | An enumeration value that indicates the level or type of shipping region.Valid Values:COUNTRY_REGION- Indicates the region is a domestic region or special location within a country.STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.WORLD_REGION- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.WORLDWIDE- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.For more detail on the actualregionName/regionIdvalues that will be returned based on theregionTypevalue, see theregionIdand/orregionNamefield descriptions.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.shipToLocations.regionIncluded | array ofShipToRegion | An array of containers that express the large geographical regions, countries, or state/provinces within a country where the seller is willing to ship to. Prospective buyers must look at the shipping regions under this container, as well as the shipping regions that are under theregionExcludedto see where the seller is willing to ship items. Sellers can specify that they ship 'Worldwide', but then add several large geographical regions (e.g. Asia, Oceania, Middle East) to the exclusion list, or sellers can specify that they ship to Europe and Africa, but then add several individual countries to the exclusion list.Occurrence:Conditional
items.shipToLocations.regionIncluded.regionId | string | The unique identifier of the shipping region. The value returned here is dependent on the correspondingregionTypevalue. TheregionIdvalue for a region does not vary based on the eBay marketplace. However, the correspondingregionNamevalue for a region is a localized, text-based description of the shipping region.If theregionTypevalue isWORLDWIDE, theregionIdvalue will also beWORLDWIDE.If theregionTypevalue isWORLD_REGION, theregionIdvalue will be one of the following:AFRICA,AMERICAS,ASIA,AUSTRALIA,CENTRAL_AMERICA_AND_CARIBBEAN,EUROPE,EUROPEAN_UNION,GREATER_CHINA,MIDDLE_EAST,NORTH_AMERICA,OCEANIA,SOUTH_AMERICA,SOUTHEAST_ASIAorCHANNEL_ISLANDS.If theregionTypevalue isCOUNTRY, theregionIdvalue will be the two-letter code for the country, as defined in theISO 3166standard.If theregionTypevalue isSTATE_OR_PROVINCE, theregionIdvalue will either be the two-letter code for US states and DC (as defined on thisSocial Security Administrationpage), or the two-letter code for Canadian provinces (as defined by thisCanada Postpage).If theregionTypevalue isCOUNTRY_REGION, theregionIdvalue may be one of following:_AH(if a seller is not willing to ship to Alaska/Hawaii),_PR(if the seller is not willing to ship to US Protectorates),_AP(if seller is not willing to ship to a US Army or Fleet Post Office), andPO_BOX(if the seller is not willing to ship to a Post Office Box).Occurrence:Conditional
items.shipToLocations.regionIncluded.regionName | string | A localized text string that indicates the name of the shipping region. The value returned here is dependent on the correspondingregionTypevalue.If theregionTypevalue isWORLDWIDE, theregionNamevalue will showWorldwide.If theregionTypevalue isWORLD_REGION, theregionNamevalue will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.If theregionTypevalue isCOUNTRY, theregionNamevalue will be a localized text string for any country in the world.If theregionTypevalue isSTATE_OR_PROVINCE, theregionNamevalue will be a localized text string for any US state or Canadian province.If theregionTypevalue isCOUNTRY_REGION, theregionNamevalue may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.Occurrence:Conditional
items.shipToLocations.regionIncluded.regionType | RegionTypeEnum | An enumeration value that indicates the level or type of shipping region.Valid Values:COUNTRY_REGION- Indicates the region is a domestic region or special location within a country.STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.WORLD_REGION- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.WORLDWIDE- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.For more detail on the actualregionName/regionIdvalues that will be returned based on theregionTypevalue, see theregionIdand/orregionNamefield descriptions.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.shortDescription | string | This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.).Occurrence:Conditional
items.size | string | (Primary Item Aspect) The size of the item. For example, '7' for a size 7 shoe. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.sizeSystem | string | (Primary Item Aspect) The sizing system of the country.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Valid Values:AU (Australia),BR (Brazil),CN (China),DE (Germany),EU (European Union),FR (France),IT (Italy),JP (Japan),MX (Mexico),US (USA),UK (United Kingdom)Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.sizeType | string | (Primary Item Aspect) Text describing a size group in which the item would be included, such as regular, petite, plus, big-and-tall or maternity. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
items.subtitle | string | A subtitle is optional and allows the seller to provide more information about the product, possibly including keywords that may assist with search results.Occurrence:Conditional
items.taxes | array ofTaxes | The container for the tax information for the item.Occurrence:Conditional
items.taxes.ebayCollectAndRemitTax | boolean | This field is only returned iftrue, and indicates that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence.Occurrence:Conditional
items.taxes.includedInPrice | boolean | This indicates if tax was applied for the cost of the item.Occurrence:Conditional
items.taxes.shippingAndHandlingTaxed | boolean | This indicates if tax is applied for the shipping cost.Occurrence:Conditional
items.taxes.taxJurisdiction | TaxJurisdiction | The container that returns the tax jurisdiction.Occurrence:Conditional
items.taxes.taxJurisdiction.region | Region | The region of the tax jurisdiction.Occurrence:Conditional
items.taxes.taxJurisdiction.region.regionName | string | A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level or at the country level in the case of VAT tax.Occurrence:Conditional
items.taxes.taxJurisdiction.region.regionType | RegionTypeEnum | An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.taxes.taxJurisdiction.taxJurisdictionId | string | The identifier of the tax jurisdiction.Occurrence:Conditional
items.taxes.taxPercentage | string | The percentage of tax.Occurrence:Conditional
items.taxes.taxType | TaxType | This field indicates the type of tax that may be collected for the item.Occurrence:Conditional
items.title | string | The seller-created title of the item.Maximum Length:80 charactersOccurrence:Always
items.topRatedBuyingExperience | boolean | This indicates if the item a top-rated plus item. There are three benefits of a top-rated plus item: a  minimum 30-day money-back return policy, shipping the items in 1 business day with tracking provided, and the added comfort of knowing this item is from experienced sellers with the highest buyer ratings. See theTop Rated Plus ItemsandBecoming a Top Rated Seller and qualifying for Top Rated Plushelp topics for more information.Occurrence:Conditional
items.tyreLabelImageUrl | string | The URL to the image that shows the information on the tyre label.Occurrence:Conditional
items.uniqueBidderCount | integer | This integer value indicates the number of different eBay users who have placed one or more bids on an auction item. This field is only applicable to auction items.Occurrence:Conditional
items.unitPrice | ConvertedAmount | This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
items.unitPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
items.unitPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
items.unitPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
items.unitPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
items.unitPricingMeasure | string | The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item.  This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
total | integer | The total number of items retrieved.Occurrence:Conditional
warnings | array ofErrorDetailV3 | An array of warning messages. These types of errors do not prevent the method from executing but should be checked.Occurrence:Conditional
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
Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size
A package of 24 AA batteries | A box of 10 packages | 10
A P235/75-15 Goodyear tire | 4 tires | 4
Fashion Jewelry Rings | Package of 100 assorted rings | 100
[/TABLE]

[TABLE]
ePID Provided | Product ID(s) Provided | Response
No | No | TheAdditionalProductIdentitycontainer isnotreturned.
No | Yes | TheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
Yes | No | TheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product.
Yes | Yes | TheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
[/TABLE]

[TABLE]
200 | Success
400 | Bad Request
404 | Not Found
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
11000 | API_BROWSE | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
11001 | API_BROWSE | REQUEST | The specified item ID was not found.
11002 | API_BROWSE | REQUEST | The specified item group was not found.
11004 | API_BROWSE | REQUEST | The item group is not available. This can be for many reasons, such as when the listing is being updated by the seller. Wait a few minutes and try the call again.
11005 | API_BROWSE | REQUEST | The item group ID is invalid. Use {itemHref} to get the item details.
11008 | API_BROWSE | REQUEST | The item group is not available. This can be for many reasons, such as when the listing is being updated by the seller. Wait a few minutes and try the call again.
11011 | API_BROWSE | REQUEST | The marketplace value {marketplaceId} is not supported. The supported values are: {allowedMarketplaces}
11012 | API_BROWSE | REQUEST | The specified item IDs are invalid, or the format of the specified values are invalid.
11013 | API_BROWSE | REQUEST | The specified group IDs are invalid, or the format of the specified values are invalid.
11014 | API_BROWSE | REQUEST | An item_ids and an item_group_ids list cannot be used at same time. Please use only one of these lists.
11015 | API_BROWSE | REQUEST | The maximum number of item IDs has been exceeded. Please reduce the number of item IDs to {maxAllowedItemIds} or less.
11016 | API_BROWSE | REQUEST | The maximum number of item group IDs has been exceeded. Please reduce the number of item group ids to {maxAllowedItemGroupIds} or less.
11017 | API_BROWSE | REQUEST | An item_ids or an item_group_ids list is required. Please use one of these lists.
11019 | API_BROWSE | REQUEST | The quantity_for_shipping_estimate value {quantityForShippingEstimate} is invalid. Please enter a positive value.
[/TABLE]

[TABLE]
11502 | API_BROWSE | APPLICATION | There was a problem extracting product information for this item. Please try again.
11508 | API_BROWSE | APPLICATION | This seller is currently away. If you make a purchase, please allow additional time for your order to be processed.
11509 | API_BROWSE | APPLICATION | This seller is currently away until {sellerReturnDate}. If you make a purchase, please allow additional time for your order to be processed.
11510 | API_BROWSE | APPLICATION | There was a problem calculating the shipping cost. Please try again.
[/TABLE]