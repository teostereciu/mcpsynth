# buy/browse/resources/item/methods/getItemByLegacyId

*Source: https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItemByLegacyId*

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

### Sample 1: Get Item Details Using a Legacy ID

### Sample 2: Get Item Details Using a Legacy ID and SKU

### Sample 3: Get Item Details and Additional Seller Details Using a Legacy ID

### Sample 4: Get Item Details and Item Charity Details Details Using a Legacy ID

#### Thank you for helping us to improve the eBay developer program.
GET/item/get_item_by_legacy_id
This method is a bridge between the eBay legacy APIs, such asShoppingandFinding, and the eBay Buy APIs. There are differences between how legacy APIs and RESTful APIs return the identifier of an "item" and what the item ID represents. This method lets you use the legacy item ids retrieve the details of a specific item, such as description, price, and other information the buyer needs to make a purchasing decision. It also returns the RESTfulitem_id, which you can use with all the Buy API  methods.For additional information about how to use legacy ids with the Buy APIs, refer toItem ID legacy API compatibility overviewin the Buying Integration guide.This method returns the item details and requires you to pass in either theitem_idof a non-variation item or theitem_idvalues for both the parent and child of an item group.Note:An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.ThefieldgroupsURI parameter lets you control what is returned in the response:SettingfieldgroupstoPRODUCTadds additional fields to the default response that return information about the product of the item.Setting thefieldgroupstoADDITIONAL_SELLER_DETAILSadds an additional field to the response that returns the seller's user ID.Setting thefieldgroupstoCHARITY_DETAILSadds additional fields to the response that return charity information associated with the item, if applicable.Thesefieldgroupscan be used independently or at the same time. For additional information, refer tofieldgroups.RestrictionsFor a list of supported sites and other restrictions, refer toAPI Restrictions.eBay Partner Network:In order to be commissioned for your sales, you must use the URL returned in theitemAffiliateWebUrlfield to forward your buyer to the ebay.com site.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
Important!Alegacy_item_idvalue must always be passed in when specifying alegacy_variation_idvalue.
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Conditional
Occurrence:Strongly Recommended
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
An array of containers with the URLs for the images that are in addition to the primary image.  The primary image is returned in theimage.imageUrlfield.Occurrence:Conditional
Reserved for future use.Occurrence:Conditional
The URL of the image.Occurrence:Conditional
A list of add-on services that may be selected for the item or that may apply automatically.Occurrence:Conditional
This field indicates whether the add-on service must be selected for the item.Occurrence:Conditional
The amount charged for the add-on service.Occurrence:Conditional
The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
The ID number of the add-on service.Occurrence:Conditional
The type of add-on service, such asAUTHENTICITY_GUARANTEE.Occurrence:Conditional
This indicates if the item is for  adults only. For more information about adult-only items on eBay, seeAdult items policyfor sellers andAdult-Only items on eBayfor buyers.Occurrence:Always
Occurrence:Always
(Primary Item Aspect) The age group for which the product is recommended. For example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
A container for information about whether an item, or the item group when returned for thegetItemsByItemGroupmethod, is qualified for the Authenticity Guarantee program.Note:TheAUTHENTICITY_GUARANTEEvalue being returned by thegetItemsByItemGroupmethod indicates that at least one item in the item group supports this program, but doesn't guarantee that the program is available to all items in the item group. To verify if the Authenticity Program is indeed available for the item that you are interested in, grab theitems.itemIdvalue for that item and use thegetItemmethod. This method will return specific details on that particular item, including whether or not the Authenticity Guarantee Program is available for the item. Look for thequalifiedProgramsarray andauthenticityGuaranteecontainer in thegetItemresponse for this information.Under the Authenticity Guarantee program, the seller ships a purchased item to a a third-party authenticator who inspects the item and provides an authentication card for it before the item is shipped to the buyer. If the buyer returns the item, the authenticator first verifies that it is the same item in the same condition before returning it to the seller.Note:Refer to theAuthenticity Guaranteepage for more information.Occurrence:Conditional
An indication that the item is qualified for the Authenticity Guarantee program.Occurrence:Conditional
The URL to the Authenticity Guarantee program terms of use.Occurrence:Conditional
A container for information about whether an item is from a verified seller.Occurrence:Conditional
An indication that the item is from a verified seller.Occurrence:Conditional
The URL to the Authenticity Verification program terms of use.Occurrence:Conditional
A list of available coupons for the item.Note:The Browse API only acknowledges item-level coupons. This array will only return coupons linked with an item. Store-level coupons offered by sellers across their entire store will not be returned.Occurrence:Conditional
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
The IDs of every category in the item path, separated by pipe characters, starting with the top level parent category.For example, if an item belongs to the top level category Home and Garden (category ID 11700), followed by Home Improvement (159907), Heating, Cooling and Air (69197), and Thermostats (115947), the field would return the value:11700|159907|69197|115947.Occurrence:Always
Text that shows the category hierarchy of the item. For example: Computers/Tablets & Networking, Laptops & Netbooks, PC Laptops & NetbooksOccurrence:Always
This container returns any applicable charity information associated with the specified item.This container is only returned if thefieldgroupsquery parameter is set toCHARITY_DETAILS.Occurrence:Conditional
The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds from the item.Occurrence:Conditional
The percentage of the purchase price of the item that the charitable organization (identified in thecharityOrgIdfield) will receive for each sale.Occurrence:Conditional
The details of the charity's logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
The name of the charity organization.Occurrence:Conditional
The URL to the charity's eBay page.Occurrence:Conditional
(Primary Item Aspect) Text describing the color of the item.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
A short text description for the condition of the item, such as New or Used. For a list of condition names, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
A full text description for the condition of the item. This field elaborates on the value specified in theconditionfield and provides full details for the condition of the item.Occurrence:Conditional
This array is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that indicate details about a particular condition of an item.Note:Condition descriptors are currently only available for the following trading card categories:Non-Sport Trading Card SinglesCCG Individual CardsSports Trading Card SinglesOccurrence:Conditional
The name of a condition descriptor. The value(s) for this condition descriptor is returned in the associatedvaluesarray.Occurrence:Conditional
This array displays the value(s) for a condition descriptor (denoted by the associatednamefield), as well as any other additional information about the condition of the item.Occurrence:Conditional
Additional information about the condition of an item as it relates to a condition descriptor. This array elaborates on the value specified in thecontentfield and provides additional details about the condition of an item.Occurrence:Conditional
The value for the condition descriptor indicated in the associatednamefield.Occurrence:Conditional
The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The container that returns the current highest bid for an auction item. The value (string) field shows the dollar value of the current highest bid, and the currency (3-digit ISO code) field denotes the currency associated with that bid value. This container will only be returned for auction items.Occurrence:Conditional
The full description of the item that was created by the seller. This can be plain text or rich content and can be very large.Occurrence:Always
The Eco Participation fee, a fee paid by the buyer that is applied to the cost of the eventual disposal of the purchased item. The fee is remitted in full to the eco organization.Currently, this value is required for electronic devices and furniture.Occurrence:Conditional
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
Hazardous materials labels for the item.Occurrence:Conditional
Additional information about the hazardous materials labels.Occurrence:Conditional
An array of hazard pictograms that apply to the item.Occurrence:Conditional
The description of the hazard pictogram, such as Flammable.Occurrence:Conditional
The ID of the hazard pictogram.Occurrence:Conditional
The URL of the hazard pictogram.Occurrence:Conditional
The signal word for the hazardous materials label (such as Danger or Warning).Occurrence:Conditional
The ID of the signal word for the hazardous materials label.Occurrence:Conditional
An array of hazard statements for the item.Occurrence:Conditional
A description of the nature of the hazard, such as whether the material is toxic if swallowed.Occurrence:Conditional
The ID of the hazard statement.Occurrence:Conditional
The URL of the primary image of the item. The other images of the item are returned in theadditionalImagescontainer.Occurrence:Always
A value oftrueindicates that the seller requires immediate payment from the buyer when purchasing an item.Note:It is possible for this field to be set totrue, but not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyers purchases that involve the Best Offer feature, or for offline transactions.Occurrence:Always
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
The ID of the eBay marketplace where the item is listed.Occurrence:Always
An array of containers that show the complete list of the aspect name/value pairs that describe the variation of the item.Occurrence:Conditional
The text representing the name of the aspect for the name/value pair, such as Color.Occurrence:Conditional
This indicates if the value being returned is a string or an array of values.Valid Values:STRING- Indicates the value returned is a string.STRING_ARRAY- Indicates the value returned is an array of strings.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The value of the aspect for the name/value pair, such as Red.Occurrence:Conditional
The number of items in a lot. In other words, a lot size is the number of items that are being sold together.A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot,  such as the package of batteries shown in the example below.ItemLot DefinitionLot SizeA package of 24 AA batteriesA box of 10 packages10A P235/75-15 Goodyear tire4 tires4Fashion Jewelry RingsPackage of 100 assorted rings100Note:Lots are not supported in all categories.Occurrence:Conditional
Contact information for the manufacturer of the product.Occurrence:Conditional
The first line of the product manufacturer's street address.Occurrence:Conditional
The second line of the product manufacturer's street address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.Occurrence:Conditional
The city of the product manufacturer's street address.Occurrence:Conditional
The company name of the product manufacturer.Occurrence:Conditional
The contact URL of the product manufacturer.Occurrence:Conditional
The country name of the product manufacturer's street address.Occurrence:Conditional
The county of the product manufacturer's street address.Occurrence:Conditional
The product manufacturer's business email address.Occurrence:Conditional
The product manufacturer's business phone number.Occurrence:Conditional
The postal code of the product manufacturer's street address.Occurrence:Conditional
The state or province of the product manufacturer's street address.Occurrence:Conditional
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
The container that returns details of a primary item group (parent ID of an item group). An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.Note:This container is returned only if theitem_idin the request is for an item group (items with variations, such as color and size).Occurrence:Conditional
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
This container provides product safety labels which were provided by the seller, for the listing.ThegetProductSafetyLabelsmethod of theSell Metadata APIcan be used to retrieve the full set of available Product Safety pictogram labels and safety statements.Occurrence:Conditional
An array of seller provided comma-separated string values that provides identifier, URL, and description for one or more pictograms associated with the listing.Occurrence:Conditional
The description of the safety label pictogram.Occurrence:Conditional
The identifier of the safety label pictogram.Occurrence:Conditional
The URL of the safety label pictogram.Occurrence:Conditional
A description of the nature of the product safety label statement.Occurrence:Conditional
The identifier of the product safety label statement.Occurrence:Conditional
An array of the qualified programs available for the item, or for the item group when returned for thegetItemsByItemGroupmethod, such as EBAY_PLUS, AUTHENTICITY_GUARANTEE, and AUTHENTICITY_VERIFICATION.Note:TheAUTHENTICITY_GUARANTEEvalue being returned by thegetItemsByItemGroupmethod indicates that at least one item in the item group supports this program, but doesn't guarantee that the program is available to all items in the item group. To verify if the Authenticity Program is indeed available for the item that you are interested in, grab theitems.itemIdvalue for that item and use thegetItemmethod. This method will return specific details on that particular item, including whether or not the Authenticity Guarantee Program is available for the item. Look for thequalifiedProgramsarray andauthenticityGuaranteecontainer in thegetItemresponse for this information.eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings. Sellers must commit to next-day delivery of those items.Note:eBay Plus is only available as a listing feature on the eBay Australia marketplace.The eBayAuthenticity Guaranteeprogram enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.Occurrence:Conditional
The maximum number for a specific item that one buyer can purchase.Occurrence:Conditional
A score that describes how easy it is to repair the product. Score values range from 0.1 (hardest to repair) to 10.0 (easiest), always including a single decimal place.Occurrence:Conditional
This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.Note:This is returned only for auctions that have a reserve price.Occurrence:Conditional
If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.
Note:This is returned only for auctions that have a reserve price.
This array provides information about one or more EU-based Responsible Persons or entities associated with the listing.Occurrence:Conditional
The first line of the Responsible Person's street address.Occurrence:Conditional
The second line of the Responsible Person's address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.Occurrence:Conditional
The city of the Responsible Person's street address.Occurrence:Conditional
The name of the Responsible Person or entity.Occurrence:Conditional
The contact URL of the Responsible Person or entity.Occurrence:Conditional
The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
The country name of the Responsible Person's street address.Occurrence:Conditional
The county of the Responsible Person's street address.Occurrence:Conditional
The email of the Responsible Person's street address.Occurrence:Conditional
The phone number of the Responsible Person's street address.Occurrence:Conditional
The postal code of the Responsible Person's street address.Occurrence:Conditional
The state or province of the Responsible Person's street address.Occurrence:Conditional
The type(s) associated with the Responsible Person or entity.Occurrence:Conditional
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
A list of the custom policies that are applied to a listing.Occurrence:Conditional
The seller-defined description of the policy.Occurrence:Conditional
The seller-defined label for an individual custom policy.Occurrence:Conditional
The type of custom policy, such as PRODUCT_COMPLIANCE or TAKE_BACK.Occurrence:Conditional
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
The number of users that have added the item to their watch list.Note:This field is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields that you want access to Watch Count data in the Browse API.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
For more on warnings, plus the codes of other common warnings, seeHandling errors.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns the details of a specific item, which isnotpart of a multi-variation listing, using the legacyItemIDvalue. 
      The call returns the RESTitemIdfor the item. This ID can be used with allBrowseandOrderAPI calls.
The input is alegacy_item_idURI parameter. There is no payload with this request.
GEThttps://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?legacy_item_id=2**********2
The output is the details of the item and the RESTitemId(v1|2**********2|0).
This sample returns the details of specific item, which is part of a multi-variation listing, using the legacyItemIDvalue and associatedSKUvalue of an item. These values 
      are returned by the legacyTradingandShoppingAPIs. 
      It also returns the RESTitemIdfor the item. This ID can be used with allBrowseandOrderAPI calls.
The input islegacy_item_idandlegacy_variation_SKUURI parameter. There is no payload with this request.
The input is alegacy_item_id, and thefieldgroupsURI parameter is set toADDITIONAL_SELLER_DETAILS. There is no payload with this request.
Related topics
If you need help, contactDeveloper Technical Support.

```
browse/v1/item/get_item_by_legacy_id?legacy_item_id=1**********9
```
- SettingfieldgroupstoPRODUCTadds additional fields to the default response that return information about the product of the item.
- Setting thefieldgroupstoADDITIONAL_SELLER_DETAILSadds an additional field to the response that returns the seller's user ID.
- Setting thefieldgroupstoCHARITY_DETAILSadds additional fields to the response that return charity information associated with the item, if applicable.
- PRODUCTThis field group adds theproductcontainer to the response.
- ADDITIONAL_SELLER_DETAILSThis field group adds theuserIdfield to the response.
- CHARITY_DETAILSThis field group adds the thecharityTermscontainer to the response, if applicable.
- When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.
- When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.
- To retrieve theitemAffiliateWebUrlfield in the response, the ePN affiliate can pass in their affiliate credentials using this header. For more information, seeHeader for affiliate information.
- If the listing is using calculated or flat-rate shipping with shipping rate tables, the user can use this header to provide country and postal code in order for theshippingOptioncontainer, which includes shipping costs and delivery estimates, to be returned. For more information, seeHeader for shipping information accuracy.
- FIXED_PRICE- Indicates the buyer can purchase the item for a set price using the Buy It Now button.
- AUCTION- Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.
- BEST_OFFER- Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, seeMaking a Best Offer.
- CLASSIFIED_AD- Indicates that the final sales transaction is to be completed outside of the eBay environment.
- Non-Sport Trading Card Singles
- CCG Individual Cards
- Sports Trading Card Singles
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
legacy_item_id | string | This query parameter is the unique identifier that specifies the item being retrieved.Note:When passing in the ID for a multi-variation listing, you must also use thelegacy_variation_idfield and pass in the ID of the specific item variation. If not, all variation within the multi-SKU listing will be retrieved.The following is an example of using the value of theItemIDfield for a specific item to get the RESTfulitemIdvalue.browse/v1/item/get_item_by_legacy_id?legacy_item_id=1**********9Occurrence:Required
legacy_variation_id | string | This query parameter specifies the legacy item ID of a specific item in a multi-variation listing, such as that for thered shirt size Litem.Important!Alegacy_item_idvalue must always be passed in when specifying alegacy_variation_idvalue.Occurrence:Optional
legacy_variation_sku | string | This query parameter specifies the legacy SKU of an item. SKUs are the unique identifiers of an item created by the seller.The following is an example of using the value of theItemIDandSKUfields to get the RESTfulitemIdvalue.browse/v1/item/get_item_by_legacy_id?legacy_item_id=1**********9&legacy_variation_sku=V**********MImportant!Alegacy_item_idvalue must always be passed in when specifying alegacy_variation_skuvalue.Occurrence:Optional
fieldgroups | array ofstring | This field controls what is returned in the response. If this field is not set, the method returns all details about the item. Multiplefieldgroupscan be set.Valid Values:PRODUCTThis field group adds theproductcontainer to the response.ADDITIONAL_SELLER_DETAILSThis field group adds theuserIdfield to the response.CHARITY_DETAILSThis field group adds the thecharityTermscontainer to the response, if applicable.Occurrence:Optional
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
additionalImages | array ofImage | An array of containers with the URLs for the images that are in addition to the primary image.  The primary image is returned in theimage.imageUrlfield.Occurrence:Conditional
additionalImages.height | integer | Reserved for future use.Occurrence:Conditional
additionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
additionalImages.width | integer | Reserved for future use.Occurrence:Conditional
addonServices | array ofAddonService | A list of add-on services that may be selected for the item or that may apply automatically.Occurrence:Conditional
addonServices.selection | AddonServiceSelectionEnum | This field indicates whether the add-on service must be selected for the item.Occurrence:Conditional
addonServices.serviceFee | ConvertedAmount | The amount charged for the add-on service.Occurrence:Conditional
addonServices.serviceFee.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
addonServices.serviceFee.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
addonServices.serviceFee.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
addonServices.serviceFee.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
addonServices.serviceId | string | The ID number of the add-on service.Occurrence:Conditional
addonServices.serviceType | AddonServiceTypeEnum | The type of add-on service, such asAUTHENTICITY_GUARANTEE.Occurrence:Conditional
adultOnly | boolean | This indicates if the item is for  adults only. For more information about adult-only items on eBay, seeAdult items policyfor sellers andAdult-Only items on eBayfor buyers.Occurrence:Always
ageGroup | string | (Primary Item Aspect) The age group for which the product is recommended. For example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
authenticityGuarantee | AuthenticityGuaranteeProgram | A container for information about whether an item, or the item group when returned for thegetItemsByItemGroupmethod, is qualified for the Authenticity Guarantee program.Note:TheAUTHENTICITY_GUARANTEEvalue being returned by thegetItemsByItemGroupmethod indicates that at least one item in the item group supports this program, but doesn't guarantee that the program is available to all items in the item group. To verify if the Authenticity Program is indeed available for the item that you are interested in, grab theitems.itemIdvalue for that item and use thegetItemmethod. This method will return specific details on that particular item, including whether or not the Authenticity Guarantee Program is available for the item. Look for thequalifiedProgramsarray andauthenticityGuaranteecontainer in thegetItemresponse for this information.Under the Authenticity Guarantee program, the seller ships a purchased item to a a third-party authenticator who inspects the item and provides an authentication card for it before the item is shipped to the buyer. If the buyer returns the item, the authenticator first verifies that it is the same item in the same condition before returning it to the seller.Note:Refer to theAuthenticity Guaranteepage for more information.Occurrence:Conditional
authenticityGuarantee.description | string | An indication that the item is qualified for the Authenticity Guarantee program.Occurrence:Conditional
authenticityGuarantee.termsWebUrl | string | The URL to the Authenticity Guarantee program terms of use.Occurrence:Conditional
authenticityVerification | AuthenticityVerificationProgram | A container for information about whether an item is from a verified seller.Occurrence:Conditional
authenticityVerification.description | string | An indication that the item is from a verified seller.Occurrence:Conditional
authenticityVerification.termsWebUrl | string | The URL to the Authenticity Verification program terms of use.Occurrence:Conditional
availableCoupons | array ofAvailableCoupon | A list of available coupons for the item.Note:The Browse API only acknowledges item-level coupons. This array will only return coupons linked with an item. Store-level coupons offered by sellers across their entire store will not be returned.Occurrence:Conditional
availableCoupons.constraint | CouponConstraint | The limitations or restrictions of the coupon.Occurrence:Conditional
availableCoupons.constraint.expirationDate | string | This timestamp provides the expiration date of the coded coupon.Occurrence:Conditional
availableCoupons.discountAmount | Amount | The discount amount after the coupon is applied.Occurrence:Conditional
availableCoupons.discountAmount.currency | CurrencyCodeEnum | The list of valid currencies. EachISO 4217currency code includes the currency name followed by the numeric value.For example, the Canadian Dollar code (CAD) would take the following form:Canadian Dollar, 124.Occurrence:Conditional
availableCoupons.discountAmount.value | string | The value of the discounted amount.Occurrence:Conditional
availableCoupons.discountType | CouponDiscountType | The type of discount that the coupon applies.Occurrence:Conditional
availableCoupons.message | string | A description of the coupon.Note:The value returned in thetermsWebUrlfield should appear for all experiences when displaying coupons. The value in theavailableCoupons.messagefield must also be included if returned in the API response.Occurrence:Conditional
availableCoupons.redemptionCode | string | The coupon code.Occurrence:Conditional
availableCoupons.termsWebUrl | string | The URL to the coupon terms of use.Note:The value returned in thetermsWebUrlfield should appear for all experiences when displaying coupons. The value in theavailableCoupons.messagefield must also be included if returned in the API response.Occurrence:Conditional
bidCount | integer | This integer value indicates the total number of bids that have been placed against an auction item. This field is returned only for auction items.Occurrence:Conditional
brand | string | (Primary Item Aspect) The name brand of the item, such as Nike, Apple, etc.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
buyingOptions | array ofstring | A comma separated list of all the purchase options available for the item. The values returned are:FIXED_PRICE- Indicates the buyer can purchase the item for a set price using the Buy It Now button.AUCTION- Indicates the buyer can place a bid for the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this item.BEST_OFFER- Indicates the buyer can send the seller a price they're willing to pay for the item. The seller can accept, reject, or send a counter offer. For more information on how this works, seeMaking a Best Offer.CLASSIFIED_AD- Indicates that the final sales transaction is to be completed outside of the eBay environment.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
categoryId | string | The ID of the leaf category for this item. A leaf category is the lowest level in that category and has no children.Occurrence:Always
categoryIdPath | string | The IDs of every category in the item path, separated by pipe characters, starting with the top level parent category.For example, if an item belongs to the top level category Home and Garden (category ID 11700), followed by Home Improvement (159907), Heating, Cooling and Air (69197), and Thermostats (115947), the field would return the value:11700|159907|69197|115947.Occurrence:Always
categoryPath | string | Text that shows the category hierarchy of the item. For example: Computers/Tablets & Networking, Laptops & Netbooks, PC Laptops & NetbooksOccurrence:Always
charityTerms | ItemCharityTerms | This container returns any applicable charity information associated with the specified item.This container is only returned if thefieldgroupsquery parameter is set toCHARITY_DETAILS.Occurrence:Conditional
charityTerms.charityOrgId | string | The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds from the item.Occurrence:Conditional
charityTerms.donationPercentage | number | The percentage of the purchase price of the item that the charitable organization (identified in thecharityOrgIdfield) will receive for each sale.Occurrence:Conditional
charityTerms.LogoImage | Image | The details of the charity's logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
charityTerms.LogoImage.height | integer | Reserved for future use.Occurrence:Conditional
charityTerms.LogoImage.imageUrl | string | The URL of the image.Occurrence:Conditional
charityTerms.LogoImage.width | integer | Reserved for future use.Occurrence:Conditional
charityTerms.name | string | The name of the charity organization.Occurrence:Conditional
charityTerms.website | string | The URL to the charity's eBay page.Occurrence:Conditional
color | string | (Primary Item Aspect) Text describing the color of the item.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
condition | string | A short text description for the condition of the item, such as New or Used. For a list of condition names, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
conditionDescription | string | A full text description for the condition of the item. This field elaborates on the value specified in theconditionfield and provides full details for the condition of the item.Occurrence:Conditional
conditionDescriptors | array ofConditionDescriptor | This array is used by the seller to provide additional information about the condition of an item in a structured format. Condition descriptors are name-value attributes that indicate details about a particular condition of an item.Note:Condition descriptors are currently only available for the following trading card categories:Non-Sport Trading Card SinglesCCG Individual CardsSports Trading Card SinglesOccurrence:Conditional
conditionDescriptors.name | string | The name of a condition descriptor. The value(s) for this condition descriptor is returned in the associatedvaluesarray.Occurrence:Conditional
conditionDescriptors.values | array ofConditionDescriptorValue | This array displays the value(s) for a condition descriptor (denoted by the associatednamefield), as well as any other additional information about the condition of the item.Occurrence:Conditional
conditionDescriptors.values.additionalInfo | array ofstring | Additional information about the condition of an item as it relates to a condition descriptor. This array elaborates on the value specified in thecontentfield and provides additional details about the condition of an item.Occurrence:Conditional
conditionDescriptors.values.content | string | The value for the condition descriptor indicated in the associatednamefield.Occurrence:Conditional
conditionId | string | The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
currentBidPrice | ConvertedAmount | The container that returns the current highest bid for an auction item. The value (string) field shows the dollar value of the current highest bid, and the currency (3-digit ISO code) field denotes the currency associated with that bid value. This container will only be returned for auction items.Occurrence:Conditional
currentBidPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
currentBidPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
currentBidPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
currentBidPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
description | string | The full description of the item that was created by the seller. This can be plain text or rich content and can be very large.Occurrence:Always
ecoParticipationFee | ConvertedAmount | The Eco Participation fee, a fee paid by the buyer that is applied to the cost of the eventual disposal of the purchased item. The fee is remitted in full to the eco organization.Currently, this value is required for electronic devices and furniture.Occurrence:Conditional
ecoParticipationFee.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
ecoParticipationFee.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
ecoParticipationFee.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
ecoParticipationFee.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
eligibleForInlineCheckout | boolean | This field indicates if the item can be purchased using the BuyOrder API.If the value of this field istrue, this indicates that the item can be purchased using theOrder API.If the value of this field isfalse, this indicates that the item cannot be purchased using theOrder APIand must be purchased on the eBay site.Occurrence:Always
enabledForGuestCheckout | boolean | This indicates if the item can be purchased using Guest Checkout in theOrder API. You can use this flag to exclude items from your inventory that are not eligible for Guest Checkout, such as gift cards.Occurrence:Always
energyEfficiencyClass | string | This indicates theEuropean energy efficiencyrating (EEK) of the item. This field is returned only if the seller specified the energy efficiency rating.The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.When the manufacturer's specifications for this item are available, the link to this information is returned in theproductFicheWebUrlfield.Occurrence:Conditional
epid | string | An EPID is the eBay product identifier of a product from the eBay product catalog.  This indicates the product in which the item belongs.Occurrence:Conditional
estimatedAvailabilities | array ofEstimatedAvailability | The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Occurrence:Conditional
estimatedAvailabilities.availabilityThreshold | integer | This field is return only when the seller sets their 'display item quantity' preference toDisplay "More than 10 available" in your listing (if applicable). The value of this field will be "10", which is the threshold value.Code so that your app gracefully handles any future changes to this value.Occurrence:Conditional
estimatedAvailabilities.availabilityThresholdType | AvailabilityThresholdEnum | This field is return only when the seller sets theirDisplay Item Quantitypreference toDisplay "More than 10 available" in your listing (if applicable). The value of this field will beMORE_THAN. This indicates that the seller has more than the 'quantity display preference', which is 10, in stock for this item.The following are the display item quantity preferences the seller can set.Display "More than 10 available" in your listing (if applicable)If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.Display the exact quantity in your itemsIf the seller enables this preference, theavailabilityThresholdTypeandavailabilityThresholdfields are not returned and the estimated quantity of the item is returned in theestimatedAvailableQuantityfield.Note:Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity.Code so that your app gracefully handles any future changes to these preferences.Occurrence:Conditional
estimatedAvailabilities.deliveryOptions | array ofDeliveryOptionsEnum | An array of available delivery options.Valid Values:SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, PICKUP_DROP_OFF, or DIGITAL_DELIVERYCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
estimatedAvailabilities.estimatedAvailabilityStatus | AvailabilityStatusEnum | An enumeration value representing the inventory status of this item.Note:Be sure to review theitemEndDatefield to determine whether the item is available for purchase.Valid Values:IN_STOCK, LIMITED_STOCK, or OUT_OF_STOCKCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
estimatedAvailabilities.estimatedAvailableQuantity | integer | The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Note:To see if a listing is available for purchase, review theitemEndDateandestimatedAvailablityStatusfields. If the item has anEndDatein the past, or theestimatedAvailabilityStatusisOUT_OF_STOCK, the item is unavailable for purchase.Occurrence:Conditional
estimatedAvailabilities.estimatedRemainingQuantity | integer | The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Note:To see if a listing is available for purchase, review theitemEndDateandestimatedAvailablityStatusfields. If the item has anEndDatein the past, or theestimatedAvailabilityStatusisOUT_OF_STOCK, the item is unavailable for purchase.Occurrence:Conditional
estimatedAvailabilities.estimatedSoldQuantity | integer | The estimated number of this item that have been sold.Occurrence:Conditional
gender | string | (Primary Item Aspect) The gender for the item. This is used for items that could vary by gender, such as clothing. For example: male, female, or unisex. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
gtin | string | The unique Global Trade Item number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
hazardousMaterialsLabels | HazardousMaterialsLabels | Hazardous materials labels for the item.Occurrence:Conditional
hazardousMaterialsLabels.additionalInformation | string | Additional information about the hazardous materials labels.Occurrence:Conditional
hazardousMaterialsLabels.pictograms | array ofHazardPictogram | An array of hazard pictograms that apply to the item.Occurrence:Conditional
hazardousMaterialsLabels.pictograms.pictogramDescription | string | The description of the hazard pictogram, such as Flammable.Occurrence:Conditional
hazardousMaterialsLabels.pictograms.pictogramId | string | The ID of the hazard pictogram.Occurrence:Conditional
hazardousMaterialsLabels.pictograms.pictogramUrl | string | The URL of the hazard pictogram.Occurrence:Conditional
hazardousMaterialsLabels.signalWord | string | The signal word for the hazardous materials label (such as Danger or Warning).Occurrence:Conditional
hazardousMaterialsLabels.signalWordId | string | The ID of the signal word for the hazardous materials label.Occurrence:Conditional
hazardousMaterialsLabels.statements | array ofHazardStatement | An array of hazard statements for the item.Occurrence:Conditional
hazardousMaterialsLabels.statements.statementDescription | string | A description of the nature of the hazard, such as whether the material is toxic if swallowed.Occurrence:Conditional
hazardousMaterialsLabels.statements.statementId | string | The ID of the hazard statement.Occurrence:Conditional
image | Image | The URL of the primary image of the item. The other images of the item are returned in theadditionalImagescontainer.Occurrence:Always
image.height | integer | Reserved for future use.Occurrence:Conditional
image.imageUrl | string | The URL of the image.Occurrence:Conditional
image.width | integer | Reserved for future use.Occurrence:Conditional
immediatePay | boolean | A value oftrueindicates that the seller requires immediate payment from the buyer when purchasing an item.Note:It is possible for this field to be set totrue, but not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyers purchases that involve the Best Offer feature, or for offline transactions.Occurrence:Always
inferredEpid | string | The ePID (eBay Product ID of a product from the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.If the seller provided an ePID for the item, the seller's value is returned in theepidfield.Note:This field is returned only for authorized Partners.Occurrence:Conditional
itemAffiliateWebUrl | string | The URL to the View Item page of the item which includes the affiliate tracking ID.Note:In order to receive commissions on sales, eBay Partner Network affiliates must use this URL to forward buyers to the listing on the eBay marketplace.TheitemAffiliateWebUrlis only returned if:The marketplace through which the item is being viewed is part of the eBay Partner Network. Currently Singapore (EBAY_SG) isnotsupported.For additional information, refer toeBay Partner Network.The seller enables affiliate tracking for the item by including theX-EBAY-C-ENDUSERCTXrequest header in the method.Occurrence:Conditional
itemCreationDate | string | A timestamp that indicates the date and time an item listing was created.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
itemEndDate | string | A timestamp that indicates the date and time an auction listing will end.If a fixed-price listing has ended, this field indicates the date and time the listing ended.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
itemId | string | The unique RESTful identifier of the item.Occurrence:Always
itemLocation | Address | The physical location of the item.Occurrence:Conditional
itemLocation.addressLine1 | string | The first line of the street address.Note:This is conditionally returned in theitemLocationfield.Occurrence:Conditional
itemLocation.addressLine2 | string | The second line of the street address. This field is not always used, but can be used for "Suite Number" or "Apt Number".Occurrence:Conditional
itemLocation.city | string | The city of the address.Occurrence:Always
itemLocation.country | CountryCodeEnum | The two-letterISO 3166standard code for the country of the address.Occurrence:Always
itemLocation.county | string | The county of the address.Occurrence:Conditional
itemLocation.postalCode | string | The postal code (or zip code in US) code of the address. Sellers set a postal code (or zip code in US) for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned initemLocation.postalCodevia the API.Occurrence:Conditional
itemLocation.stateOrProvince | string | The state or province of the address.Note:This is conditionally returned in theitemLocationfield.Occurrence:Conditional
itemWebUrl | string | The URL of the View Item page of the item. This enables you to include a "Report Item on eBay" link that takes the buyer to the View Item page on eBay. From there they can report any issues regarding this item to eBay.Occurrence:Always
legacyItemId | string | The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Always
listingMarketplaceId | MarketplaceIdEnum | The ID of the eBay marketplace where the item is listed.Occurrence:Always
localizedAspects | array ofTypedNameValue | An array of containers that show the complete list of the aspect name/value pairs that describe the variation of the item.Occurrence:Conditional
localizedAspects.name | string | The text representing the name of the aspect for the name/value pair, such as Color.Occurrence:Conditional
localizedAspects.type | ValueTypeEnum | This indicates if the value being returned is a string or an array of values.Valid Values:STRING- Indicates the value returned is a string.STRING_ARRAY- Indicates the value returned is an array of strings.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
localizedAspects.value | string | The value of the aspect for the name/value pair, such as Red.Occurrence:Conditional
lotSize | integer | The number of items in a lot. In other words, a lot size is the number of items that are being sold together.A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot,  such as the package of batteries shown in the example below.ItemLot DefinitionLot SizeA package of 24 AA batteriesA box of 10 packages10A P235/75-15 Goodyear tire4 tires4Fashion Jewelry RingsPackage of 100 assorted rings100Note:Lots are not supported in all categories.Occurrence:Conditional | Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size
A package of 24 AA batteries | A box of 10 packages | 10
A P235/75-15 Goodyear tire | 4 tires | 4
Fashion Jewelry Rings | Package of 100 assorted rings | 100
manufacturer | CompanyAddress | Contact information for the manufacturer of the product.Occurrence:Conditional
manufacturer.addressLine1 | string | The first line of the product manufacturer's street address.Occurrence:Conditional
manufacturer.addressLine2 | string | The second line of the product manufacturer's street address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.Occurrence:Conditional
manufacturer.city | string | The city of the product manufacturer's street address.Occurrence:Conditional
manufacturer.companyName | string | The company name of the product manufacturer.Occurrence:Conditional
manufacturer.contactUrl | string | The contact URL of the product manufacturer.Occurrence:Conditional
manufacturer.country | CountryCodeEnum | The two-letterISO 3166standard code for the country of the address.Occurrence:Conditional
manufacturer.countryName | string | The country name of the product manufacturer's street address.Occurrence:Conditional
manufacturer.county | string | The county of the product manufacturer's street address.Occurrence:Conditional
manufacturer.email | string | The product manufacturer's business email address.Occurrence:Conditional
manufacturer.phone | string | The product manufacturer's business phone number.Occurrence:Conditional
manufacturer.postalCode | string | The postal code of the product manufacturer's street address.Occurrence:Conditional
manufacturer.stateOrProvince | string | The state or province of the product manufacturer's street address.Occurrence:Conditional
marketingPrice | MarketingPrice | The original price and the discount amount and percentage.Occurrence:Conditional
marketingPrice.discountAmount | ConvertedAmount | This container returns the monetary amount of the seller discount.Occurrence:Conditional
marketingPrice.discountAmount.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
marketingPrice.discountAmount.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
marketingPrice.discountAmount.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
marketingPrice.discountAmount.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
marketingPrice.discountPercentage | string | This field expresses the percentage of the seller discount based on the value in theoriginalPricecontainer.Occurrence:Conditional
marketingPrice.originalPrice | ConvertedAmount | This container returns the monetary amount of the item without the discount.Occurrence:Conditional
marketingPrice.originalPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
marketingPrice.originalPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
marketingPrice.originalPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
marketingPrice.originalPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
marketingPrice.priceTreatment | PriceTreatmentEnum | Indicates the pricing treatment (discount) that was applied to the price of the item.Note:The pricing treatment affects the way and where the discounted price can be displayed.Occurrence:Conditional
material | string | (Primary Item Aspect) Text describing what the item is made of. For example, silk. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
minimumPriceToBid | ConvertedAmount | The minimum price of the next bid, which means to place a bid it must be equal to or greater than this amount. If the auction hasn't received any bids, the minimum bid price is the same as the starting bid. Otherwise, the minimum bid price is equal to the current bid plus the bid increment.  For details about bid increments, seeAutomatic bidding.Occurrence:Conditional
minimumPriceToBid.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
minimumPriceToBid.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
minimumPriceToBid.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
minimumPriceToBid.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
mpn | string | The manufacturer's part number, which is a unique number that identifies a specific product. To identify the product, this is always used along with brand.Occurrence:Conditional
pattern | string | (Primary Item Aspect) Text describing the pattern used on the item. For example, paisley. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
paymentMethods | array ofPaymentMethod | The payment methods for the item, including the payment method types, brands, and instructions for the buyer.Occurrence:Conditional
paymentMethods.paymentMethodType | PaymentMethodTypeEnum | The payment method type, such as credit card or cash.Occurrence:Conditional
paymentMethods.paymentMethodBrands | array ofPaymentMethodBrand | The payment method brands, including the payment method brand type and logo image.Occurrence:Conditional
paymentMethods.paymentMethodBrands.paymentMethodBrandType | PaymentMethodBrandEnum | The payment method brand, such as Visa or PayPal.Occurrence:Conditional
paymentMethods.paymentMethodBrands.logoImage | Image | The details of the logo image, such as the size and URL.Note:Currently, only theimageUrlis populated.Occurrence:Conditional
paymentMethods.paymentMethodBrands.logoImage.height | integer | Reserved for future use.Occurrence:Conditional
paymentMethods.paymentMethodBrands.logoImage.imageUrl | string | The URL of the image.Occurrence:Conditional
paymentMethods.paymentMethodBrands.logoImage.width | integer | Reserved for future use.Occurrence:Conditional
paymentMethods.paymentInstructions | array ofPaymentInstructionEnum | The payment instructions for the buyer, such ascash in personorcontact seller.Occurrence:Conditional
paymentMethods.sellerInstructions | array ofSellerInstructionEnum | The seller instructions to the buyer, such asaccepts credit cardsorsee description.Occurrence:Conditional
price | ConvertedAmount | The cost of just the item. This amount does not include any adjustments such as discounts or shipping costs.Note:The price does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
price.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
price.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
price.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
price.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
priceDisplayCondition | PriceDisplayConditionEnum | Indicates when in the buying flow the item's price can appear for minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item.Occurrence:Conditional
primaryItemGroup | ItemGroupSummary | The container that returns details of a primary item group (parent ID of an item group). An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc.Note:This container is returned only if theitem_idin the request is for an item group (items with variations, such as color and size).Occurrence:Conditional
primaryItemGroup.itemGroupAdditionalImages | array ofImage | An array of containers with the URLs for images that are in addition to the primary image of the item group.  The primary image is returned in theitemGroupImagefield.Occurrence:Conditional
primaryItemGroup.itemGroupAdditionalImages.height | integer | Reserved for future use.Occurrence:Conditional
primaryItemGroup.itemGroupAdditionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
primaryItemGroup.itemGroupAdditionalImages.width | integer | Reserved for future use.Occurrence:Conditional
primaryItemGroup.itemGroupHref | string | The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
primaryItemGroup.itemGroupId | string | The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
primaryItemGroup.itemGroupImage | Image | The URL of the primary image of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
primaryItemGroup.itemGroupImage.height | integer | Reserved for future use.Occurrence:Conditional
primaryItemGroup.itemGroupImage.imageUrl | string | The URL of the image.Occurrence:Conditional
primaryItemGroup.itemGroupImage.width | integer | Reserved for future use.Occurrence:Conditional
primaryItemGroup.itemGroupTitle | string | The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
primaryItemGroup.itemGroupType | ItemGroupTypeEnum | An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
primaryProductReviewRating | ReviewRating | The container that returns the product rating details, such as review count, rating histogram, and average rating.Occurrence:Conditional
primaryProductReviewRating.averageRating | string | The average rating given to a product based on customer reviews.Occurrence:Conditional
primaryProductReviewRating.ratingHistograms | array ofRatingHistogram | An array of containers for the product rating histograms that shows the review counts and the product rating.Occurrence:Conditional
primaryProductReviewRating.ratingHistograms.count | integer | The total number of user ratings that the product has received.Occurrence:Conditional
primaryProductReviewRating.ratingHistograms.rating | string | This is the average rating for the product. As part of a product review, users rate the product. Products are rated from one star (terrible) to five stars (excellent), with each star having a corresponding point value - one star gets 1 point, two stars get 2 points, and so on. If a product had one four-star rating and one five-star rating, its average rating would be4.5, and this is the value that would appear in this field.Occurrence:Conditional
primaryProductReviewRating.reviewCount | integer | The total number of reviews for the item.Occurrence:Conditional
priorityListing | boolean | This field is returned astrueif the listing is part of a Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent sales activity.For more information, seePromoted Listings.Occurrence:Always
product | Product | The container that returns the product information of the item.Occurrence:Conditional
product.additionalImages | array ofImage | An array of containers with the URLs for the product images that are in addition to the primary image.Occurrence:Conditional
product.additionalImages.height | integer | Reserved for future use.Occurrence:Conditional
product.additionalImages.imageUrl | string | The URL of the image.Occurrence:Conditional
product.additionalImages.width | integer | Reserved for future use.Occurrence:Conditional
product.additionalProductIdentities | array ofAdditionalProductIdentity | An array of product identifiers associated with the item. This container is returned if the seller has associated the eBay Product Identifier (ePID) with the item and in the requestfieldgroupsis set toPRODUCT.Occurrence:Conditional
product.additionalProductIdentities.productIdentity | array ofProductIdentity | An array of product identifier/value pairs for the product associated with the item. This is returned if the seller has associated the eBay Product Identifier (ePID) with the item and the request hasfieldgroupsset toPRODUCT.The following table shows what is returned, based on the item information provided by the seller, whenfieldgroupsis set toPRODUCT.ePID ProvidedProduct ID(s) ProvidedResponseNoNoTheAdditionalProductIdentitycontainer isnotreturned.NoYesTheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.YesNoTheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product.YesYesTheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.Occurrence:Conditional | ePID Provided | Product ID(s) Provided | Response | No | No | TheAdditionalProductIdentitycontainer isnotreturned. | No | Yes | TheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer. | Yes | No | TheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product. | Yes | Yes | TheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
ePID Provided | Product ID(s) Provided | Response
No | No | TheAdditionalProductIdentitycontainer isnotreturned.
No | Yes | TheAdditionalProductIdentitycontainer isnotreturned but the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
Yes | No | TheAdditionalProductIdentitycontainer is returned listing the product identifiers of the product.
Yes | Yes | TheAdditionalProductIdentitycontainer is returned listing all the product identifiers of the product and the product identifiers specified by the seller are returned in thelocalizedAspectscontainer.
product.additionalProductIdentities.productIdentity.identifierType | string | The type of product identifier, such as UPC and EAN.Occurrence:Conditional
product.additionalProductIdentities.productIdentity.identifierValue | string | The product identifier value.Occurrence:Conditional
product.aspectGroups | array ofAspectGroup | An array of containers for the product aspects. Each group contains the aspect group name and the aspect name/value pairs.Occurrence:Conditional
product.aspectGroups.aspects | array ofAspect | An array of the name/value pairs for the aspects of the product. For example: BRAND/AppleOccurrence:Conditional
product.aspectGroups.aspects.localizedName | string | The text representing the name of the aspect for the name/value pair, such as Brand.Occurrence:Conditional
product.aspectGroups.aspects.localizedValues | array ofstring | The text representing the value of the aspect for the name/value pair, such as Apple.Occurrence:Conditional
product.aspectGroups.localizedGroupName | string | The name of a group of aspects.In the following example,Product IdentifiersandProcessare product aspect group names. Under the group name are the product aspect name/value pairs.Product IdentifiersBrand/AppleProduct Family/iMacProcessorProcessor Type/IntelProcessor Speed/3.10Occurrence:Conditional
product.brand | string | The brand associated with product. To identify the product, this is always used along with MPN (manufacturer part number).Occurrence:Conditional
product.description | string | The rich description of an eBay product, which might contain HTML.Occurrence:Conditional
product.gtins | array ofstring | An array of all the possible GTINs values associated with the product. A GTIN is a unique Global Trade Item number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
product.image | Image | The primary image of the product. This is often a stock photo.Occurrence:Conditional
product.image.height | integer | Reserved for future use.Occurrence:Conditional
product.image.imageUrl | string | The URL of the image.Occurrence:Conditional
product.image.width | integer | Reserved for future use.Occurrence:Conditional
product.mpns | array ofstring | An array of all possible MPN values associated with the product. A MPNs is manufacturer part number of the product. To identify the product, this is always used along with brand.Occurrence:Conditional
product.title | string | The title of the product.Occurrence:Conditional
productFicheWebUrl | string | The URL of a page containing the manufacturer's specification of this item, which helps buyers make a purchasing decision. This information is available only for items that include the European energy efficiency rating (EEK) but is not available forallitems with an EEK rating and is returned only if this information is available. The EEK rating of the item is returned in theenergyEfficiencyClassfield.Occurrence:Conditional
productSafetyLabels | ProductSafetyLabels | This container provides product safety labels which were provided by the seller, for the listing.ThegetProductSafetyLabelsmethod of theSell Metadata APIcan be used to retrieve the full set of available Product Safety pictogram labels and safety statements.Occurrence:Conditional
productSafetyLabels.pictograms | array ofProductSafetyLabelPictogram | An array of seller provided comma-separated string values that provides identifier, URL, and description for one or more pictograms associated with the listing.Occurrence:Conditional
productSafetyLabels.pictograms.pictogramDescription | string | The description of the safety label pictogram.Occurrence:Conditional
productSafetyLabels.pictograms.pictogramId | string | The identifier of the safety label pictogram.Occurrence:Conditional
productSafetyLabels.pictograms.pictogramUrl | string | The URL of the safety label pictogram.Occurrence:Conditional
productSafetyLabels.statements | array ofProductSafetyLabelStatement | An array of seller provided comma-separated string values that provide identifier and description for one or more product safety statements associated with the listing.Occurrence:Conditional
productSafetyLabels.statements.statementDescription | string | A description of the nature of the product safety label statement.Occurrence:Conditional
productSafetyLabels.statements.statementId | string | The identifier of the product safety label statement.Occurrence:Conditional
qualifiedPrograms | array ofstring | An array of the qualified programs available for the item, or for the item group when returned for thegetItemsByItemGroupmethod, such as EBAY_PLUS, AUTHENTICITY_GUARANTEE, and AUTHENTICITY_VERIFICATION.Note:TheAUTHENTICITY_GUARANTEEvalue being returned by thegetItemsByItemGroupmethod indicates that at least one item in the item group supports this program, but doesn't guarantee that the program is available to all items in the item group. To verify if the Authenticity Program is indeed available for the item that you are interested in, grab theitems.itemIdvalue for that item and use thegetItemmethod. This method will return specific details on that particular item, including whether or not the Authenticity Guarantee Program is available for the item. Look for thequalifiedProgramsarray andauthenticityGuaranteecontainer in thegetItemresponse for this information.eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings. Sellers must commit to next-day delivery of those items.Note:eBay Plus is only available as a listing feature on the eBay Australia marketplace.The eBayAuthenticity Guaranteeprogram enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.Occurrence:Conditional
quantityLimitPerBuyer | integer | The maximum number for a specific item that one buyer can purchase.Occurrence:Conditional
repairScore | string | A score that describes how easy it is to repair the product. Score values range from 0.1 (hardest to repair) to 10.0 (easiest), always including a single decimal place.Occurrence:Conditional
reservePriceMet | boolean | This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.Note:This is returned only for auctions that have a reserve price.Occurrence:Conditional
responsiblePersons | array ofResponsiblePerson | This array provides information about one or more EU-based Responsible Persons or entities associated with the listing.Occurrence:Conditional
responsiblePersons.addressLine1 | string | The first line of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.addressLine2 | string | The second line of the Responsible Person's address. This field is not always used, but can be used for secondary address information such as 'Suite Number' or 'Apt Number'.Occurrence:Conditional
responsiblePersons.city | string | The city of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.companyName | string | The name of the Responsible Person or entity.Occurrence:Conditional
responsiblePersons.contactUrl | string | The contact URL of the Responsible Person or entity.Occurrence:Conditional
responsiblePersons.country | CountryCodeEnum | The two-letterISO 3166standard of the country of the address.Occurrence:Conditional
responsiblePersons.countryName | string | The country name of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.county | string | The county of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.email | string | The email of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.phone | string | The phone number of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.postalCode | string | The postal code of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.stateOrProvince | string | The state or province of the Responsible Person's street address.Occurrence:Conditional
responsiblePersons.types | array ofResponsiblePersonTypeEnum | The type(s) associated with the Responsible Person or entity.Occurrence:Conditional
returnTerms | ItemReturnTerms | The container that returns an overview of the seller's return policy.Occurrence:Conditional
returnTerms.extendedHolidayReturnsOffered | boolean | This indicates if the seller has enabled the Extended Holiday Returns feature on the item. Extended Holiday Returns are only applicable during the US holiday season, and gives buyers extra time to return an item. This 'extra time' will typically extend beyond what is set through thereturnPeriodvalue.Occurrence:Conditional
returnTerms.refundMethod | RefundMethodEnum | An enumeration value that indicates how a buyer is refunded when an item is returned.Valid Values:MONEY_BACK or MERCHANDISE_CREDITCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
returnTerms.restockingFeePercentage | string | This string field indicates the restocking fee percentage that the seller has set on the item. Sellers have the option of setting no restocking fee for an item, or they can set the percentage to 10, 15, or 20 percent. So, if the cost of the item was $100, and the restocking percentage was 20 percent, the buyer would be charged $20 to return that item, so instead of receiving a $100 refund, they would receive $80 due to the restocking fee.Occurrence:Conditional
returnTerms.returnInstructions | string | Text written by the seller describing what the buyer needs to do in order to return the item.Occurrence:Conditional
returnTerms.returnMethod | ReturnMethodEnum | An enumeration value that indicates the alternative methods for a full refund when an item is returned. This field is returned if the seller offers the buyer an item replacement or exchange instead of a monetary refund.Valid Values:REPLACEMENT-  Indicates that the buyer has the option of receiving money back for the returned item, or they can choose to have the seller replace the item with an identical item.EXCHANGE- Indicates that the buyer has the option of receiving money back for the returned item, or they can exchange the item for another similar item.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
returnTerms.returnPeriod | TimeDuration | The amount of time the buyer has to return the item after the purchase date.Occurrence:Conditional
returnTerms.returnPeriod.unit | TimeDurationUnitEnum | An enumeration value that indicates the units of the time span (e.g.,HOURS). The enumeration value in this field defines the period of time being used to measure the duration.Refer toTimeDurationUnitEnumfor the list of supported values.Occurrence:Conditional
returnTerms.returnPeriod.value | integer | Retrieves the duration of the time span (no units). The value in this field indicates the number of years, months, days, hours, or minutes in the defined period.Occurrence:Conditional
returnTerms.returnsAccepted | boolean | Indicates whether the seller accepts returns for the item.Occurrence:Conditional
returnTerms.returnShippingCostPayer | ReturnShippingCostPayerEnum | This enumeration value indicates whether the buyer or seller is responsible for return shipping costs when an item is returned.Valid Values:SELLER- Indicates the seller will pay for the shipping costs to return the item.BUYER- Indicates the buyer will pay for the shipping costs to return the item.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
seller | SellerDetail | The container that returns basic and detailed about the seller of the item, such as name, feedback score, and contact information.Occurrence:Always
seller.feedbackPercentage | string | The percentage of the total positive feedback.Occurrence:Always
seller.feedbackScore | integer | The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Always
seller.sellerAccountType | string | This indicates if the seller is a business or an individual. This is determined when the seller registers with eBay. If they register for a business account, this value will beBUSINESS. If they register for a private account, this value will beINDIVIDUAL. This designation is required by the tax laws in the following countries:This field is applicable only on the following marketplaces:EBAY_ATEBAY_BEEBAY_CHEBAY_DEEBAY_ESEBAY_FREBAY_GBEBAY_IEEBAY_ITEBAY_PLNote:This field will be returned empty on unsupported marketplaces.Valid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
seller.sellerLegalInfo | SellerLegalInfo | The container with the seller's contact info and fields that are required by law.Occurrence:Conditional
seller.sellerLegalInfo.email | string | The seller's business email address.Occurrence:Conditional
seller.sellerLegalInfo.fax | string | The seller' business fax number.Occurrence:Conditional
seller.sellerLegalInfo.imprint | string | This is a free-form string created by the seller. This is information often found on business cards, such as address. This is information used by some countries.Occurrence:Conditional
seller.sellerLegalInfo.legalContactFirstName | string | The seller's first name.Occurrence:Conditional
seller.sellerLegalInfo.legalContactLastName | string | The seller's last name.Occurrence:Conditional
seller.sellerLegalInfo.name | string | The name of the seller's business.Occurrence:Conditional
seller.sellerLegalInfo.phone | string | The seller's business phone number.Occurrence:Conditional
seller.sellerLegalInfo.registrationNumber | string | The seller's registration number. This is information used by some countries.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress | LegalAddress | The container that returns the seller's address to be used to contact them.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.addressLine1 | string | The first line of the street address.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.addressLine2 | string | The second line of the street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.city | string | The city of the address.Occurrence:Always
seller.sellerLegalInfo.sellerProvidedLegalAddress.country | CountryCodeEnum | The two-letterISO 3166standard code for the country of the address.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.countryName | string | The name of the country of the address.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.county | string | The name of the county of the address.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.postalCode | string | The postal code of the address.Occurrence:Conditional
seller.sellerLegalInfo.sellerProvidedLegalAddress.stateOrProvince | string | The state or province of the address.Occurrence:Always
seller.sellerLegalInfo.termsOfService | string | This is a free-form string created by the seller. This is the seller's terms or condition, which is in addition to the seller's return policies.Occurrence:Conditional
seller.sellerLegalInfo.vatDetails | array ofVatDetail | An array of the seller's VAT (value added tax) IDs and the issuing country. VAT is a tax added by some European countries.Occurrence:Conditional
seller.sellerLegalInfo.vatDetails.issuingCountry | CountryCodeEnum | The two-letterISO 3166standard of the country issuing the seller's VAT (value added tax) ID. VAT is a tax added by some European countries.Occurrence:Conditional
seller.sellerLegalInfo.vatDetails.vatId | string | The seller's VAT (value added tax) ID. VAT is a tax added by some European countries.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator | EconomicOperator | Provides required information about the manufacturer and/or supplier of the item.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.companyName | string | The company name of the registered Economic Operator.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.addressLine1 | string | The first line of the registered Economic Operator's street address.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.addressLine2 | string | The second line, if any, of the registered Economic Operator's street address. This field is not always used, but can be used for 'Suite Number' or 'Apt Number'.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.city | string | The city of the registered Economic Operator's street address.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.stateOrProvince | string | The state or province of the registered Economic Operator's street address.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.postalCode | string | The postal code of the registered Economic Operator's street address.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.country | string | The two-letterISO 3166standard abbreviation of the country of the registered Economic Operator's address.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.phone | string | The registered Economic Operator's business phone number.Occurrence:Conditional
seller.sellerLegalInfo.economicOperator.email | string | The registered Economic Operator's business email address.Occurrence:Conditional
seller.sellerLegalInfo.weeeNumber | string | The Waste Electrical and Electronic Equipment (WEEE) registration number required for any seller to place electrical and electronic equipment on the market in Germany. This manufacturer number is assigned to the first distributors of electrical and electronic equipment and comprises a country code and an 8-digit sequence of digits (e.g. “WEEE Reg. No. DE 12345678”).Occurrence:Conditional
seller.userId | string | The unique identifier of an eBay user across all eBay sites. This value does not change, even when a user changes their username.Occurrence:Conditional
seller.username | string | The user name created by the seller for use on eBay.Note:Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place. For more information, please refer toData Handling Compliance.Occurrence:Always
sellerCustomPolicies | array ofSellerCustomPolicy | A list of the custom policies that are applied to a listing.Occurrence:Conditional
sellerCustomPolicies.description | string | The seller-defined description of the policy.Occurrence:Conditional
sellerCustomPolicies.label | string | The seller-defined label for an individual custom policy.Occurrence:Conditional
sellerCustomPolicies.type | SellerCustomPolicyTypeEnum | The type of custom policy, such as PRODUCT_COMPLIANCE or TAKE_BACK.Occurrence:Conditional
sellerItemRevision | string | An identifier generated/incremented when a seller revises the item. There are two types of item revisions:Seller changes, such as changing the titleeBay system changes, such as changing the quantity when an item is purchasedThis ID is changedonlywhen the seller makes a change to the item. This means you cannot use this value to determine if the quantity has changed.Occurrence:Conditional
shippingOptions | array ofShippingOption | An array of shipping options containers that have the details about cost, carrier, etc. of one shipping option.Note:For items with calculated shipping, this array is only returned if theX-EBAY-C-ENDUSERCTXheader is supplied.Occurrence:Conditional
shippingOptions.additionalShippingCostPerUnit | ConvertedAmount | Any per item additional shipping costs for a multi-item purchase. For example, let's say the shipping cost for a power cord is $3. But for an additional cord, the shipping cost is only $1. So if you bought 3 cords, theshippingCostwould be $3 and this value would be $2 ($1 for each additional item).Occurrence:Conditional
shippingOptions.additionalShippingCostPerUnit.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
shippingOptions.additionalShippingCostPerUnit.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
shippingOptions.additionalShippingCostPerUnit.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
shippingOptions.additionalShippingCostPerUnit.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
shippingOptions.cutOffDateUsedForEstimate | string | The deadline date that the item must be purchased by in order to be received by the buyer within the delivery window (maxEstimatedDeliveryDateandminEstimatedDeliveryDatefields). This field is returned only for items that are eligible for 'Same Day Handling'. For these items, the value of this field is what is displayed in theDeliveryline on the View Item page.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Occurrence:Conditional
shippingOptions.fulfilledThrough | FulfilledThroughEnum | If the item is being shipped by the eBayGlobal Shipping program, this field returnsGLOBAL_SHIPPING.If the item is being shipped using the eBay International Shipping program, this field returnsINTERNATIONAL_SHIPPING.Otherwise, this field is null.Occurrence:Conditional
shippingOptions.guaranteedDelivery | boolean | Although this field is still returned, it can be ignored since eBay Guaranteed Delivery is no longer a supported feature on any marketplace. This field may get removed from the schema in the future.Occurrence:Conditional
shippingOptions.importCharges | ConvertedAmount | TheGlobal Shipping Programimport charges for this item.Occurrence:Conditional
shippingOptions.importCharges.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
shippingOptions.importCharges.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
shippingOptions.importCharges.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
shippingOptions.importCharges.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
shippingOptions.maxEstimatedDeliveryDate | string | The end date of the delivery window (latest projected delivery date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include the location of where the item is be shipped in thecontextualLocationvalues of theX-EBAY-C-ENDUSERCTXrequest header.Occurrence:Conditional
shippingOptions.minEstimatedDeliveryDate | string | The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.Note:For the best accuracy, always include the location of where the item is be shipped in thecontextualLocationvalues of theX-EBAY-C-ENDUSERCTXrequest header.Occurrence:Conditional
shippingOptions.quantityUsedForEstimate | integer | The number of items used when calculating the estimation information.This field will reflect the value input in thequantity_for_shipping_estimatequery parameter.Occurrence:Conditional
shippingOptions.shippingCarrierCode | string | The name of the shipping provider, such as FedEx, or USPS.Occurrence:Always
shippingOptions.shippingCost | ConvertedAmount | The final shipping cost for all the items after all discounts are applied.This container will reflect the cost for the quantity specified through thequantity_for_shipping_estimatequery parameter.Note:The cost does include the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive cost. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
shippingOptions.shippingCost.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
shippingOptions.shippingCost.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
shippingOptions.shippingCost.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
shippingOptions.shippingCost.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
shippingOptions.shippingCostType | string | Indicates the class of the shipping cost.Valid Values:FIXED or CALCULATEDCode so that your app gracefully handles any future changes to this list.Occurrence:Always
shippingOptions.shippingServiceCode | string | The type of shipping service. For example, USPS First Class.Occurrence:Always
shippingOptions.shipToLocationUsedForEstimate | ShipToLocation | The container that returns the country and postal code of where the item is to be shipped. These values come from thecontextualLocationvalues in theX-EBAY-C-ENDUSERCTXrequest header. If the header is not submitted, marketplace is used.Occurrence:Conditional
shippingOptions.shipToLocationUsedForEstimate.country | CountryCodeEnum | The two-letterISO 3166standard of the country for where the item is to be shipped.Occurrence:Conditional
shippingOptions.shipToLocationUsedForEstimate.postalCode | string | The zip code (postal code) for where the item is to be shipped.Occurrence:Conditional
shippingOptions.trademarkSymbol | string | Any trademark symbol, such as ™ or ®, that needs to be shown in superscript next to the shipping service name.Occurrence:Conditional
shippingOptions.type | string | The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.Occurrence:Always
shipToLocations | ShipToLocations | The container that returns the geographic regions to be included and excluded that define where the item can be shipped.Occurrence:Conditional
shipToLocations.regionExcluded | array ofShipToRegion | An array of containers that express the large geographical regions, countries, state/provinces, or special locations within a country where the seller is not willing to ship to.Occurrence:Conditional
shipToLocations.regionExcluded.regionId | string | The unique identifier of the shipping region. The value returned here is dependent on the correspondingregionTypevalue. TheregionIdvalue for a region does not vary based on the eBay marketplace. However, the correspondingregionNamevalue for a region is a localized, text-based description of the shipping region.If theregionTypevalue isWORLDWIDE, theregionIdvalue will also beWORLDWIDE.If theregionTypevalue isWORLD_REGION, theregionIdvalue will be one of the following:AFRICA,AMERICAS,ASIA,AUSTRALIA,CENTRAL_AMERICA_AND_CARIBBEAN,EUROPE,EUROPEAN_UNION,GREATER_CHINA,MIDDLE_EAST,NORTH_AMERICA,OCEANIA,SOUTH_AMERICA,SOUTHEAST_ASIAorCHANNEL_ISLANDS.If theregionTypevalue isCOUNTRY, theregionIdvalue will be the two-letter code for the country, as defined in theISO 3166standard.If theregionTypevalue isSTATE_OR_PROVINCE, theregionIdvalue will either be the two-letter code for US states and DC (as defined on thisSocial Security Administrationpage), or the two-letter code for Canadian provinces (as defined by thisCanada Postpage).If theregionTypevalue isCOUNTRY_REGION, theregionIdvalue may be one of following:_AH(if a seller is not willing to ship to Alaska/Hawaii),_PR(if the seller is not willing to ship to US Protectorates),_AP(if seller is not willing to ship to a US Army or Fleet Post Office), andPO_BOX(if the seller is not willing to ship to a Post Office Box).Occurrence:Conditional
shipToLocations.regionExcluded.regionName | string | A localized text string that indicates the name of the shipping region. The value returned here is dependent on the correspondingregionTypevalue.If theregionTypevalue isWORLDWIDE, theregionNamevalue will showWorldwide.If theregionTypevalue isWORLD_REGION, theregionNamevalue will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.If theregionTypevalue isCOUNTRY, theregionNamevalue will be a localized text string for any country in the world.If theregionTypevalue isSTATE_OR_PROVINCE, theregionNamevalue will be a localized text string for any US state or Canadian province.If theregionTypevalue isCOUNTRY_REGION, theregionNamevalue may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.Occurrence:Conditional
shipToLocations.regionExcluded.regionType | RegionTypeEnum | An enumeration value that indicates the level or type of shipping region.Valid Values:COUNTRY_REGION- Indicates the region is a domestic region or special location within a country.STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.WORLD_REGION- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.WORLDWIDE- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.For more detail on the actualregionName/regionIdvalues that will be returned based on theregionTypevalue, see theregionIdand/orregionNamefield descriptions.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
shipToLocations.regionIncluded | array ofShipToRegion | An array of containers that express the large geographical regions, countries, or state/provinces within a country where the seller is willing to ship to. Prospective buyers must look at the shipping regions under this container, as well as the shipping regions that are under theregionExcludedto see where the seller is willing to ship items. Sellers can specify that they ship 'Worldwide', but then add several large geographical regions (e.g. Asia, Oceania, Middle East) to the exclusion list, or sellers can specify that they ship to Europe and Africa, but then add several individual countries to the exclusion list.Occurrence:Conditional
shipToLocations.regionIncluded.regionId | string | The unique identifier of the shipping region. The value returned here is dependent on the correspondingregionTypevalue. TheregionIdvalue for a region does not vary based on the eBay marketplace. However, the correspondingregionNamevalue for a region is a localized, text-based description of the shipping region.If theregionTypevalue isWORLDWIDE, theregionIdvalue will also beWORLDWIDE.If theregionTypevalue isWORLD_REGION, theregionIdvalue will be one of the following:AFRICA,AMERICAS,ASIA,AUSTRALIA,CENTRAL_AMERICA_AND_CARIBBEAN,EUROPE,EUROPEAN_UNION,GREATER_CHINA,MIDDLE_EAST,NORTH_AMERICA,OCEANIA,SOUTH_AMERICA,SOUTHEAST_ASIAorCHANNEL_ISLANDS.If theregionTypevalue isCOUNTRY, theregionIdvalue will be the two-letter code for the country, as defined in theISO 3166standard.If theregionTypevalue isSTATE_OR_PROVINCE, theregionIdvalue will either be the two-letter code for US states and DC (as defined on thisSocial Security Administrationpage), or the two-letter code for Canadian provinces (as defined by thisCanada Postpage).If theregionTypevalue isCOUNTRY_REGION, theregionIdvalue may be one of following:_AH(if a seller is not willing to ship to Alaska/Hawaii),_PR(if the seller is not willing to ship to US Protectorates),_AP(if seller is not willing to ship to a US Army or Fleet Post Office), andPO_BOX(if the seller is not willing to ship to a Post Office Box).Occurrence:Conditional
shipToLocations.regionIncluded.regionName | string | A localized text string that indicates the name of the shipping region. The value returned here is dependent on the correspondingregionTypevalue.If theregionTypevalue isWORLDWIDE, theregionNamevalue will showWorldwide.If theregionTypevalue isWORLD_REGION, theregionNamevalue will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.If theregionTypevalue isCOUNTRY, theregionNamevalue will be a localized text string for any country in the world.If theregionTypevalue isSTATE_OR_PROVINCE, theregionNamevalue will be a localized text string for any US state or Canadian province.If theregionTypevalue isCOUNTRY_REGION, theregionNamevalue may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.Occurrence:Conditional
shipToLocations.regionIncluded.regionType | RegionTypeEnum | An enumeration value that indicates the level or type of shipping region.Valid Values:COUNTRY_REGION- Indicates the region is a domestic region or special location within a country.STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.WORLD_REGION- Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.WORLDWIDE- Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.For more detail on the actualregionName/regionIdvalues that will be returned based on theregionTypevalue, see theregionIdand/orregionNamefield descriptions.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
shortDescription | string | This text string is derived from the item condition and the item aspects (such as size, color, capacity, model, brand, etc.).Occurrence:Conditional
size | string | (Primary Item Aspect) The size of the item. For example, '7' for a size 7 shoe. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
sizeSystem | string | (Primary Item Aspect) The sizing system of the country.  All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Valid Values:AU (Australia),BR (Brazil),CN (China),DE (Germany),EU (European Union),FR (France),IT (Italy),JP (Japan),MX (Mexico),US (USA),UK (United Kingdom)Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
sizeType | string | (Primary Item Aspect) Text describing a size group in which the item would be included, such as regular, petite, plus, big-and-tall or maternity. All the item aspects, including this aspect, are returned in thelocalizedAspectscontainer.Occurrence:Conditional
subtitle | string | A subtitle is optional and allows the seller to provide more information about the product, possibly including keywords that may assist with search results.Occurrence:Conditional
taxes | array ofTaxes | The container for the tax information for the item.Occurrence:Conditional
taxes.ebayCollectAndRemitTax | boolean | This field is only returned iftrue, and indicates that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence.Occurrence:Conditional
taxes.includedInPrice | boolean | This indicates if tax was applied for the cost of the item.Occurrence:Conditional
taxes.shippingAndHandlingTaxed | boolean | This indicates if tax is applied for the shipping cost.Occurrence:Conditional
taxes.taxJurisdiction | TaxJurisdiction | The container that returns the tax jurisdiction.Occurrence:Conditional
taxes.taxJurisdiction.region | Region | The region of the tax jurisdiction.Occurrence:Conditional
taxes.taxJurisdiction.region.regionName | string | A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level or at the country level in the case of VAT tax.Occurrence:Conditional
taxes.taxJurisdiction.region.regionType | RegionTypeEnum | An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCE- Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.COUNTRY- Indicates the region is a single country.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
taxes.taxJurisdiction.taxJurisdictionId | string | The identifier of the tax jurisdiction.Occurrence:Conditional
taxes.taxPercentage | string | The percentage of tax.Occurrence:Conditional
taxes.taxType | TaxType | This field indicates the type of tax that may be collected for the item.Occurrence:Conditional
title | string | The seller-created title of the item.Maximum Length:80 charactersOccurrence:Always
topRatedBuyingExperience | boolean | This indicates if the item a top-rated plus item. There are three benefits of a top-rated plus item: a  minimum 30-day money-back return policy, shipping the items in 1 business day with tracking provided, and the added comfort of knowing this item is from experienced sellers with the highest buyer ratings. See theTop Rated Plus ItemsandBecoming a Top Rated Seller and qualifying for Top Rated Plushelp topics for more information.Occurrence:Conditional
tyreLabelImageUrl | string | The URL to the image that shows the information on the tyre label.Occurrence:Conditional
uniqueBidderCount | integer | This integer value indicates the number of different eBay users who have placed one or more bids on an auction item. This field is only applicable to auction items.Occurrence:Conditional
unitPrice | ConvertedAmount | This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
unitPrice.convertedFromCurrency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in theconvertedFromValuefield. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency.Occurrence:Conditional
unitPrice.convertedFromValue | string | The monetary amount before any conversion is performed, in the currency specified by theconvertedFromCurrencyfield. This value is required or returned only if currency conversion/localization is required. Thevaluefield contains the converted amount of this value, in the currency specified by thecurrencyfield.Occurrence:Conditional
unitPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield. If currency conversion/localization is required, this is the post-conversion currency of the amount in thevaluefield.Default:The currency of the authenticated user's country.Occurrence:Conditional
unitPrice.value | string | The monetary amount in the currency specified by thecurrencyfield. If currency conversion/localization is required, this value is the converted amount, and theconvertedFromValuefield contains the amount in the original currency.Occurrence:Conditional
unitPricingMeasure | string | The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item.  This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
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
watchCount | integer | The number of users that have added the item to their watch list.Note:This field is restricted to applications that have been granted permission to access this feature. You must submit anApp Check ticketto request this access. In the App Check form, add a note to theApplication Title/Summaryand/orApplication Detailsfields that you want access to Watch Count data in the Browse API.Occurrence:Conditional
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
200 | OK
400 | Bad Request
404 | Not Found
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
11000 | API_BROWSE | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
11003 | API_BROWSE | REQUEST | The specified legacy item ID was not found.
11004 | API_BROWSE | REQUEST | The item is not available for purchase. This can be for many reasons, such as when the listing is being updated by the seller. Wait a few minutes and try the call again.
11006 | API_BROWSE | REQUEST | The legacy ID is invalid. Use {itemGroupHref} to get the item group details.
11009 | API_BROWSE | REQUEST | The legacy variation sku is invalid.
11010 | API_BROWSE | REQUEST | You cannot submit legacy_variation_sku and legacy_variation_id in the same request. For help, see the documentation.
11011 | API_BROWSE | REQUEST | The marketplace value {marketplaceId} is not supported. The supported values are: {allowedMarketplaces}
11019 | API_BROWSE | REQUEST | The quantity_for_shipping_estimate value {quantityForShippingEstimate} is invalid. Please enter a positive value.
11501 | API_BROWSE | REQUEST | The 'fieldgroups' value(s) are invalid: {fieldgroups}. The supported fieldgroups are: {supportedFieldgroups}
[/TABLE]

[TABLE]
11502 | API_BROWSE | APPLICATION | There was a problem extracting product information for this Item. Please try again.
11508 | API_BROWSE | APPLICATION | This seller is currently away. If you make a purchase, please allow additional time for your order to be processed.
11509 | API_BROWSE | APPLICATION | This seller is currently away until {sellerReturnDate}. If you make a purchase, please allow additional time for your order to be processed.
11510 | API_BROWSE | APPLICATION | There was a problem calculating the shipping cost. Please try again.
[/TABLE]