# buy/feed/resources/item/methods/getItemFeed

*Source: https://developer.ebay.com/api-docs/buy/feed/resources/item/methods/getItemFeed*

---

### Downloading feed files

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

### Sample 1: Download the Daily Item Feed File

### Sample 2: Download the Weekly Bootstrap Item Feed File

#### Thank you for helping us to improve the eBay developer program.
This method lets you download a TSV_GZIP (tab separated value gzip)Itemfeed file. The feed file contains all the items fromallthe child categories of the specified category.  The first line of the file is the header, which labels the columns and indicates the order of the values on each line.  Each header is described in theResponse fieldssection.There are two types of item feed files generated:A dailyItemfeed file containing all the newly listed items for a specific category, date, and marketplace (feed_scope=NEWLY_LISTED)A weeklyItem Bootstrapfeed file containingallthe items in a specific category and marketplace (feed_scope=ALL_ACTIVE)Note:Filters are applied to the feed files. For details, seeFeed File Filters. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.Note:The downloaded file will be gzipped automatically, so there is no reason to supplyAccept-Encoding:gzipas a header. If this header is supplied, the downloaded file will be compressed twice, and this has no extra benefit.Downloading feed filesItem feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using theRangerequest header. TheContent-rangeresponse header indicates where in the full resource this partial chunk of data belongs  and the total number of bytes in the file.For more information about using these headers, seeRetrieve a gzip feed file.In addition to the API, there is an open sourceFeed SDKwritten in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.Note:A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.RestrictionsFor a list of supported sites and other restrictions, seeAPI Restrictions.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.item.feed
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
SeeHTTP response headersfor details.
Important: The successful response of this call isalwaysaTSV_GZIP file. However, the response is shown as JSON fields for each column so that the value returned in each column can be explained. The order in which the response fields are listed is the order of the columns in the feed file.
The container for the array of items returned by thegetItemFeedmethod. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values on each line. The header labels match the fields that are described in theResponse fieldssection.Occurrence:Conditional
Occurrence:Conditional
The unique identifier of an item in eBay RESTful format. An example would bev1|1**********2|4**********2.Occurrence:Always
Occurrence:Always
The seller created title of the item. This text is an escaped string when special characters are present, using the following rules:
For example
Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\Tracking
Marvel Legends HULK 8"Figure Avengers Age of Ultron Studios 6"Series
"Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\\Tracking"
"Marvel Legends HULK 8\"Figure Avengers Age of Ultron Studios 6\"Series"
The URL to the primary image of the item.  This is the URL of the largest image available based on what the seller submitted.Occurrence:Always
The label of the category. For example:Toys & Hobbies|Action Figures|Comic Book HeroesOccurrence:Always
The ID of the category of the item. For example: The ID for Toys & Hobbies|Action Figures|Comic Book Heroes is158671.Occurrence:Always
A comma separated list of the purchase options available for the item. Currently the only supported option isFIXED_PRICE.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Always
Important!This field no longer returns values and is scheduled for deprecation.
The seller's eBay user name.Occurrence:Always
The percentage of the seller's total positive feedback.Occurrence:Always
The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Always
The unique Global Trade Item Number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
The name brand of the item, such as Nike, Apple, etc.Occurrence:Conditional
The manufacturer part number, which is a number that is used in combination withbrandto identify a product.Occurrence:Conditional
The eBay product identifier of a product from the eBay product catalog. You can use this value in the Browse APIsearchmethod to retrieve items for this product and in theMarketing APImethods to retrieve 'also viewed' and 'also bought' products to encourage up-selling and cross-selling.Occurrence:Conditional
The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The text describing the condition of the item. For a list of condition names, seeItem Condition IDs and Names.Occurrence:Conditional
The price of the item, which can be a discounted price. If it is discounted, information about the discount is returned in theoriginalPriceValue,originalPriceCurrency,discountAmount, anddiscountPercentagecolumns.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The currency used for the price of the item. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Always
The unique identifier for the item group that contains this item. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
The item group type. Supported value:SELLER_DEFINED_VARIATIONS, indicates that the item group was created by the seller.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
A timestamp that indicates the date and time an auction listing will end.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
An identifier generated/incremented when a seller revises the item. There are two types of item revisions:Seller changes, such as changing the titleeBay system changes, such as changing the quantity when an item is purchasedThis ID is changedonlywhen the seller makes a change to the item.Occurrence:Conditional
The country where the item is physically located.Occurrence:Conditional
A semicolon separated list of the name/value pairs for the aspects of the item, which are Base64 encoded. The aspect label is separated by a pipe (|), the aspect name and value are separated by a colon (:) and the name/value pairs are separated by a semicolon (;).Example without LabelEncoded Format:encodedName:encodedValue;encodedName:encodedValue;encodedName:encodedValueEncoded Example(The delimiters areemphasized):U2l6ZQ==:WEw=;Q29sb3I=:UmVk;U2xlZXZlcw==:TG9uZw==Decoded:Size:XL;Color:Red;Sleeves:LongExample with LabelEncoded Format:encodedLabel|encodedName:encodedValue;encodedName:encodedValue;encodedLabel|Encoded Example(The delimiters areemphasized):UHJvZHVjdCBJZGVudGlmaWVycw==|R1RJTg==:MDE5MDE5ODA2NjYzMw==;QlJBTkQ=:QXBwbGU=;UHJvZHVjdCBLZXkgRmVhdHVyZXM=|TW9kZWw=:aVBob25lIDc=Decoded:Product Identifiers|GTIN:0190198066633;BRAND:Apple;Product Key Features|Model:iPhone 7Note:The separators (|  :  ;) arenotencoded. You must decode each label, name, and value separately. You cannot decode the entire string.For more information, seeEncoded Aspectsin the Buying Integration Guide.Occurrence:Conditional
Example without Label
Encoded Format:encodedName:encodedValue;encodedName:encodedValue;encodedName:encodedValue
Encoded Example(The delimiters areemphasized):U2l6ZQ==:WEw=;Q29sb3I=:UmVk;U2xlZXZlcw==:TG9uZw==
Decoded:Size:XL;Color:Red;Sleeves:Long
Example with Label
Encoded Format:encodedLabel|encodedName:encodedValue;encodedName:encodedValue;encodedLabel|
Encoded Example(The delimiters areemphasized):UHJvZHVjdCBJZGVudGlmaWVycw==|R1RJTg==:MDE5MDE5ODA2NjYzMw==;QlJBTkQ=:QXBwbGU=;UHJvZHVjdCBLZXkgRmVhdHVyZXM=|TW9kZWw=:aVBob25lIDc=
Decoded:Product Identifiers|GTIN:0190198066633;BRAND:Apple;Product Key Features|Model:iPhone 7
Note:The separators (|  :  ;) arenotencoded. You must decode each label, name, and value separately. You cannot decode the entire string.
For more information, seeEncoded Aspectsin the Buying Integration Guide.
An enumeration value representing the eBay status of the seller.Valid Values:TOP_RATED,ABOVE_STANDARD, or an empty value.An empty value indicates a return of anything other thanTOP_RATEDorABOVE_STANDARD.Code so that your app gracefully handles any future changes to this list.Occurrence:Always
An enumeration value representing the item's availability (possibility of being purchased).Values:AVAILABLETEMPORARILY_UNAVAILABLEUNAVAILABLECode so that your app gracefully handles any future changes to this list.Occurrence:Always
A boolean that indicates whether the images can be altered. If the value istrue, you cannot modify the image.Note:Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only.Occurrence:Always
Note:Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only.
The estimated quantity of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is very difficult to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Note:If the seller of an item has the available threshold setting turned on, the value of this field will be null, and the availability of the item will instead be expressed through theavailabilityThresholdTypeandavailabilityThresholdfields.Note:To see if a listing is available for purchase, review theitemEndDateandestimatedAvailablityStatusfields. If the item has anEndDatein the past, or theestimatedAvailabilityStatusisOUT_OF_STOCK, the item is unavailable for purchase.Occurrence:Conditional
This column has a value only when the seller sets their availability threshold preference. The value of this column will showMORE_THAN, which indicates that the seller has more than the available threshold preference in stock for this item. Because the quantity of an item can change several times within a second, it is very difficult to return the exact quantity.Note:This field and theavailabilityThresholdfield will be returned as null if the actual quantity meets or drops below the threshold value, and then the buyer will want to look at the value in theestimatedAvailableQuantityfield.Occurrence:Conditional
Indicates whether the seller accepts returns for the item.Occurrence:Always
The amount of days that the buyer has to return the item after the purchase date. For example, if this value is '30', the return period is 30 days.Occurrence:Conditional
An enumeration value that indicates the period of time being used to measure the duration, such as business days, months, or years.TimeDurationUnitEnumis a common type shared by multiple eBay APIs and fields to express the time unit, but for return period duration, this value will always beDAY.Occurrence:Conditional
An enumeration value that indicates how a buyer is refunded when an item is returned.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
An enumeration value that indicates the alternative methods for a full refund when an item is returned. This column will have data if the seller offers the buyer an item replacement or exchange instead of a monetary refund.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The party responsible for the return shipping costs when an item is returned.Valid Values:BUYERorSELLERCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
This field is returned empty. For a list of payment methods available for a marketplace, see eBay help pages or the actual View Item page.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Always
A comma-separated list of available delivery options. This column lets you search_filter out items than cannot be shipped to the buyer.Valid Values: SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, and PICKUP_DROP_OFF.Code so that your app gracefully handles any future changes to this list.Occurrence:Always
A pipe (|) separated alphabetical list of the geographic countries and regions where the seller will ship the item.If a region is specified, you will need to subtract any countries and regions returned in theshipToExcludedRegionscolumn to fully understand where the seller will ship.The COUNTRY: list is separated from the REGION: list with a semicolon (;).Format Example:COUNTRY:US|BM|GL|MX|PM;REGION:AFRICA|ASIA|CENTRAL_AMERICA_AND_CARIBBEAN|EUROPE|MIDDLE_EAST|OCEANIA|SOUTH_AMERICA|SOUTHEAST_ASIA;Country Values:The two-letterISO 3166standard code of the country.Region Values:AFRICA, AMERICAS, ANTARCTIC, ARCTIC, ASIA, AUSTRALIA, CENTRAL_AMERICA_AND_CARIBBEAN, EUROPE, EURO_UNION, GREATER_CHINA, MIDDLE_EAST, NORTH_AMERICA, OCEANIA, REST_OF_ASIA, SOUTHEAST_ASIA, SOUTH_AMERICA, WORLDWIDECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
The ePID (eBay Product ID of a product in the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.If the seller actually provided an ePID at listing time for the item, the ePID value is returned in theepidcolumn instead.Occurrence:Conditional
The GTIN (Global Trade Item Number) of the product as defined byhttps://www.gtin.info, which as been programmatically determined by eBay. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.If the seller provided a GTIN for the item, the seller's value is returned in thegtincolumn.Occurrence:Conditional
The name brand for the item, such as Nike or Apple, which has been programmatically determined by eBay. To identify the product, this is always used along withMPN.If the seller provided a brand for the item, the seller's value is returned in thebrandcolumn.Occurrence:Conditional
The MPN (Manufacturer's Part Number) for the item, which has been programmatically determined by eBay. To identify the product, this is always used along withbrand.If the seller provided a MPN for the item, the seller's value is returned in thempncolumn.Occurrence:Conditional
A pipe separated (|) list of URLs for the additional images of the item. These images are in addition to the primary image, which is returned in theimageUrlcolumn.Note:This column can contain multiple values.Occurrence:Conditional
The original selling price of the item. This lets you surface a strikethrough price for the item.Occurrence:Conditional
The currency of theoriginalPriceValueof the item and thediscountAmount.Occurrence:Conditional
The calculated amount of the discount (originalPriceValue-priceValue). For example,  iforiginalPriceValueis 70 andpriceValueis 56, this value would be 14.Note:The currency shown inoriginalPriceCurrencyis used for bothdiscountAmountandoriginalPriceCurrency.Occurrence:Conditional
Note:The currency shown inoriginalPriceCurrencyis used for bothdiscountAmountandoriginalPriceCurrency.
The calculated discount percentage. For example, iforiginalPriceValueis 70 anddiscountAmountis 14, this value will be 20.Occurrence:Conditional
Indicates theEuropean energy efficiencyrating (EEK) of the item. Data is returned in this column only if the seller specified the energy efficiency rating.The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.To retrieve the manufacturer's specifications for this item, when they are available, use thegetItemmethod in the Browse API. The information is returned in theproductFicheWebUrlfield.Occurrence:Conditional
A pipe separated list of the qualified programs available for the item.Valid Values:EBAY_PLUS: Indicates an item is eligible for eBay Plus. eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items.Note:eBay Plus is available only to buyers in Germany, Austria, and Australia marketplaces.AUTHENTICITY_GUARANTEE: Indicates that the item is eligible for the eBay Authenticity Guarantee program. This program enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.FEATURED: Indicates that an item is eligible to be placed in a Focus Category. Focus Categories are specific categories dedicated to a certain type of product that allow a seller to better reach their target audience and increase their sales.Occurrence:Conditional
The number of items in a lot. In other words, a lot size is the number of items that are being sold together.A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot,  such as the package of batteries shown in the example below.For example:ItemLot DefinitionLot SizeA package of 24 AA batteriesA box of 10 packages10A P235/75-15 Goodyear tire4 tires4Fashion Jewelry RingsPackage of 100 assorted rings100Note:Lots are not supported in all categories.Occurrence:Conditional
The unit of measurement used for the package dimensions, such as INCH, FEET, CENTIMETER, or METER.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The width of the shipping package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The height of the shipping package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The length of the shipping package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The unit of measurement used for the package weight, such as POUND, KILOGRAM, OUNCE, or GRAM.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The weight of the package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The name of the shipping provider, such as FedEx, or USPS.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The type of shipping service. For example, USPS First Class.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.Occurrence:Conditional
The final shipping cost for all the items after all discounts are applied.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Conditional
Indicates the class of the shipping cost.Valid Values:FIXED or CALCULATED.Occurrence:Conditional
Any per item additional shipping costs for a multi-item purchase. For example, let's say the shipping cost for a power cord is $3. But for an additional cord, the shipping cost is only $1. So if you bought 3 cords, theshippingCostwould be $3 and this value would be $2 ($1 for each additional item).Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
The number of items used when calculating the estimation information.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item.  This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Always
A pipe-separated list of alerts available for the item.For example, if theDELAYED_DELIVERYalert was returned for an item, it would indicate a delay in shipping by the seller.Occurrence:Conditional
A string value that specifies whether the seller is a business or an individual. This is determined when the seller registers with eBay. If the seller registers for a business account, the value returned in this field will beBUSINESS. If the seller registers for a private account, the value returned in this field will beINDIVIDUAL.Note:This designation is required by the tax laws in some countries.This field is applicable only on the following marketplaces:EBAY_ATEBAY_BEEBAY_CHEBAY_DEEBAY_ESEBAY_FREBAY_GBEBAY_IEEBAY_ITEBAY_PLNote:This field will be returned empty on unsupported marketplaces.Valid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
The URL to the image that shows the information on the tyre label.Occurrence:Conditional
EPN (eBay Partner Network) publishers append this value to their affiliate tracking URL when using an EPN tracking link to track changes that occur to Priority Listing items.Example:amdata=enc%3AAQAFAAAAkB1DmsmXf%2BqZ%2BCEMGdebW6oR75GCMdBmc4MCQ%2FCEPqgKHbT0jdWhPwfY5LdUs6HTaP0eBlwKE7Smy2eDslewF7l3xjwWxjqwzNAnsYgxn2PiGkTKbiQSQytFUiymdtANpk1qOnBOoMGMK%2BWsji7jYlvySSs9o9s24TxD6RqWZpNrltzOU7mfnv3H40SZ3YESzg%3D%3DSeeCreating an EPN Tracking Linkfor information on EPN tracking links.Occurrence:Conditional
A timestamp indicating when the item was created.Format:UTCyyyy-MM-ddThh:mm:ss.sssZOccurrence:Always
The URL of the View Item page of the item.For example:Single SKU:https://www.ebay.de/itm/2********0MSKU:https://www.ebay.com/itm/2********9?var=5********2Occurrence:Conditional
URL to the gallery or default image of the item. The other images of the item are returned in theadditionalImageUrlsfield.For examplehttps://i.ebayimg.com/00/s/M********w/z/W********p/$_1.JPG?set_id=8********FOccurrence:Conditional
The URL of the View Item page of the item, with the affiliate tracking ID appended to it.For examplehttps://www.ebay.de/itm/2********0?mkevt=1&mkcid=1&mkrid=707-53477-19255-0&campid=CAMPAIGNID&toolid=2***6&customid=CUSTOMIDOccurrence:Conditional
The age group that the product is recommended for.Valid values:newborn,infant,toddler,kids,adult.Occurrence:Conditional
The color of the item.Occurrence:Conditional
Text describing the pattern used on the item. For example, paisley.Note:All the item aspects, including this aspect, are returned in the localizedAspects container.Occurrence:Conditional
The size of the item.Occurrence:Conditional
In cases where items could vary by gender, this specifies for which gender the product is intended. Possible values include male, female, and unisex.Occurrence:Conditional
The material that the item is made of.Occurrence:Conditional
For an item that is priced by the unit, the total number of units that are on offer. For example, if the item is priced by the meter and 50 cm is on offer, thetotalUnitswould be 0.5 m.Occurrence:Conditional
The amount of the Eco Participation Fee, a fee paid toward the eventual disposal of the purchased item.Occurrence:Conditional
The currency in which the Eco Participation Fee for the item is paid.Occurrence:Conditional
The seller-defined label of the TAKE_BACK custom policy for the item. A TAKE_BACK policy describes the seller's regulatory responsibility to take back a purchased item for disposal when the buyer purchases a new one.Occurrence:Conditional
The seller-defined description of the TAKE_BACK custom policy for the item.Occurrence:Conditional
The ID of the signal word for the hazardous material.Occurrence:Conditional
The localized signal word for the hazardous material, such as 'Danger'.Occurrence:Conditional
The IDs of hazardous material statements, separated by the pipe symbol. For example:H200|H221Occurrence:Conditional
The Base64 encoded descriptions of hazardous material statements, separated by the pipe symbol. For example:encoded(Unstable explosives)|encoded(Flammable gas)Occurrence:Conditional
The IDs of hazardous material pictograms, separated by the pipe symbol. For example:SGH01|SGH02Occurrence:Conditional
The image URLs of hazardous material pictograms, separated by the pipe symbol. For example:https://img1|https://img2Occurrence:Conditional
Base64 encoded additional information about the hazardous material.Occurrence:Conditional
A score that describes how easy it is to repair the product. Score values range from 0.1 (hardest to repair) to 10.0 (easiest), always including a single decimal place.Occurrence:Conditional
Note:Condition descriptors are currently only available for the following trading card categories:Non-Sport Trading Card SinglesCCG Individual CardsSports Trading Card SinglesThis field contains a list of the name/value pairs for the condition descriptors of the item, which are Base64 encoded. The descriptors are separated as follows:Name and value pairs are separated by a colon :Name:ValueBase64 encoding the above pair yieldsTmFtZQ==:VmFsdWU=Multiple descriptors are separated by a semicolon;Name1:Value1;Name2:Value2Base64 encoding the above multiple descriptors yieldsTmFtZTE=:VmFsdWUx;TmFtZTI=:VmFsdWUyMultiple values are separated by a pipe|Name1:Value1|Value2|Value3;Name2:Value1|Value2|Value3Base64 encoding the above multiple values (for multiple descriptors) yieldsTmFtZTE=:VmFsdWUx|VmFsdWUy|VmFsdWUz;TmFtZTI=:VmFsdWUx|VmFsdWUy|VmFsdWUzNote:The separators (: ; |) are not encoded. You must decode each name, and value or values separately. You cannot decode the entire string.Thenameandvalueare numeric IDs that map to the name and value, respectively, of a condition descriptor. A condition descriptor name-value pair provides more information about an item's condition in a structured way. Descriptors are name-value attributes that can be either from a closed set or open text. For more information on the numeric IDs and their text equivalents, use thegetItemConditionPoliciesmethod of theMetadata API.Occurrence:Conditional
The unique identifier of an eBay user across all eBay sites. This value does not change, even when a user changes their username.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns a GZIP file with items listed on September 18, 2018 in the Cameras & Photo category. In this example, the size of the file being returned is 240MB (251658240 bytes) and the requestRangeheader specifies to return the first 10MB (10485760 bytes).
The inputs arefeed_scope=NEWLY_LISTED,category_id, anddateURI parameters.The request parameters are:Rangebytes=0-10485760andX-EBAY-C-MARKETPLACE-IDEBAY_US.
       For more information about using these headers, seeHTTP request headers.
GEThttps://api.ebay.com/buy/feed/v1_beta/item?feed_scope=NEWLY_LISTED&category_id=625&date=20180918
If the call is successful, the portion of the file specified by theRangeheader, is returned. The call returns a 206 HTTP status and theContent-rangebytes=0-10485760/251658240response header.
This sample returns the latest weeklyItem Bootstrapfeed file. It contains all the 'Good 'Til Cancelled' items in the category specified.Note:Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The items in the file are the items that were in the specified category on Sunday.
The inputs arefeed_scope=ALL_ACTIVEandcategory_idURI parameters.The request parameters are:Rangebytes=0-10485760andX-EBAY-C-MARKETPLACE-IDEBAY_US.
       For more information about using these headers, seeHTTP request headers.
Related topics
If you need help, contactDeveloper Technical Support.
- A dailyItemfeed file containing all the newly listed items for a specific category, date, and marketplace (feed_scope=NEWLY_LISTED)
- A weeklyItem Bootstrapfeed file containingallthe items in a specific category and marketplace (feed_scope=ALL_ACTIVE)
- NEWLY_LISTED- Returns the dailyItemfeed file containing all Good 'Til Cancelled items that were listed on the day specified by thedateparameter in the category specified by thecategory_idparameter.
- ALL_ACTIVE- Returns the weeklyItem Bootstrapfeed file containing all the Good 'Til Cancelled items in the category specified by thecategory_idparameter.Note:Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The items in the file are the items that were in the specified category on Sunday.
- Required whenfeed_scope=NEWLY_LISTED
- Must be within 3-14 days in the past
- Double quotes (") and backslashes (\) in the Title are escaped with a backslash (\) character
- If there are any tabs (\t), double quotes ("), or backslashes (\) in the Title, the entire Title will be wrapped in double quotes.
- Seller changes, such as changing the title
- eBay system changes, such as changing the quantity when an item is purchased
- AVAILABLE
- TEMPORARILY_UNAVAILABLE
- UNAVAILABLE
- EBAY_PLUS: Indicates an item is eligible for eBay Plus. eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items.Note:eBay Plus is available only to buyers in Germany, Austria, and Australia marketplaces.
- AUTHENTICITY_GUARANTEE: Indicates that the item is eligible for the eBay Authenticity Guarantee program. This program enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.
- FEATURED: Indicates that an item is eligible to be placed in a Focus Category. Focus Categories are specific categories dedicated to a certain type of product that allow a seller to better reach their target audience and increase their sales.
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
- Non-Sport Trading Card Singles
- CCG Individual Cards
- Sports Trading Card Singles
- Name and value pairs are separated by a colon :Name:ValueBase64 encoding the above pair yieldsTmFtZQ==:VmFsdWU=
- Multiple descriptors are separated by a semicolon;Name1:Value1;Name2:Value2Base64 encoding the above multiple descriptors yieldsTmFtZTE=:VmFsdWUx;TmFtZTI=:VmFsdWUy
- Multiple values are separated by a pipe|Name1:Value1|Value2|Value3;Name2:Value1|Value2|Value3Base64 encoding the above multiple values (for multiple descriptors) yieldsTmFtZTE=:VmFsdWUx|VmFsdWUy|VmFsdWUz;TmFtZTI=:VmFsdWUx|VmFsdWUy|VmFsdWUz
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
feed_scope | string | This query parameter specifies the type of feed file to return.Valid Values:NEWLY_LISTED- Returns the dailyItemfeed file containing all Good 'Til Cancelled items that were listed on the day specified by thedateparameter in the category specified by thecategory_idparameter.ALL_ACTIVE- Returns the weeklyItem Bootstrapfeed file containing all the Good 'Til Cancelled items in the category specified by thecategory_idparameter.Note:Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The items in the file are the items that were in the specified category on Sunday.Occurrence:Required
category_id | string | This query parameter specifies the eBay top-level category ID of the items to be returned in the feed file.The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplace, you can use the Taxonomy APIgetCategoryTreemethod. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by thecategoryTreeNodeLevelfield.For example:"categoryTreeNodeLevel": 1For details seeGet Categories for Buy APIs.Restriction:Must be a top-level (L1) category other than Real Estate. Items listed under Real Estate L1 categories are excluded from all feeds in all marketplaces.Occurrence:Required
date | string | This query parameter specifies the date of the dailyItemfeed file (feed_scope=NEWLY_LISTED) you want to retrieve.Thedateis required only for the dailyItemfeed file. If you specify a date for theItem Bootstrapfile (feed_scope=ALL_ACTIVE), the date is ignored and the latest file is returned. The date theItem Bootstrapfeed file was generated is returned in theLast-Modifiedresponse header.TheItemfeed files are generated every day and there are 14 daily files available.Note:The dailyItemfeed files are available each day after 9AM MST (US Mountain Standard Time), which is -7 hours UTC time.There is a 48 hour latency when generating theItemfeed files. This means you can download the file for July 10th on July 12 after 9AM MST.For categories with a large number of items, the latency can be up to 72 hours.Format:yyyyMMddRequirements:Required whenfeed_scope=NEWLY_LISTEDMust be within 3-14 days in the pastOccurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
Accept | string | The formats that the client accepts for the response.A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format.Default:application/json,text/tab-separated-valuesOccurrence:Required
X-EBAY-C-MARKETPLACE-ID | string | The ID of the eBay marketplace where the item is hosted. This value is case sensitive.For example:X-EBAY-C-MARKETPLACE-ID = EBAY_USFor a list of supported sites see,API Restrictions.Occurrence:Required
Range | string | This header specifies the range in bytes of the chunks of the gzip file being returned.Format:bytes=startpos-endposFor example, the following retrieves the first 10 MBs of the feed file.Range bytes=0-10485760For more information about using this header, seeRetrieving a gzip feed file.Maximum:100 MB (10MB in the Sandbox)Occurrence:Required
[/TABLE]

[TABLE]
Content-range | Thecontent-rangeresponse header indicates where in the full resource this partial chunk of data belongs. It returns the lower and upper values in bytes (specified by theRangeheader) of the chunk and the total size of the file being downloaded in bytes.Maximum range: 100 MBThe following is an example of acontent-rangeresponse, where 0-10 is the lower and upper max_results in bytes and 1000 is the total size of the file in bytes.0-10/1000The following example of acontent-rangeresponse indicates the value of theRangeheader is invalid and a 416 status code is returned.*/1000For more information and examples, seeRetrieving a gzip feed file.
Last-Modified | Returns the generated date of the feed file, which will be the latest file available. For example:Last-ModifiedWed, 21 Oct 2015 07:28:00 GMT
[/TABLE]

[TABLE]
Output container/field | Type | Description
items | array ofItem | The container for the array of items returned by thegetItemFeedmethod. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values on each line. The header labels match the fields that are described in theResponse fieldssection.Occurrence:Conditional
items.itemId | string | The unique identifier of an item in eBay RESTful format. An example would bev1|1**********2|4**********2.Occurrence:Always
items.title | string | The seller created title of the item. This text is an escaped string when special characters are present, using the following rules:Double quotes (") and backslashes (\) in the Title are escaped with a backslash (\) characterIf there are any tabs (\t), double quotes ("), or backslashes (\) in the Title, the entire Title will be wrapped in double quotes.For exampleBefore:Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\TrackingMarvel Legends HULK 8"Figure Avengers Age of Ultron Studios 6"SeriesAfter:"Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\\Tracking""Marvel Legends HULK 8\"Figure Avengers Age of Ultron Studios 6\"Series"Occurrence:Always
items.imageUrl | string | The URL to the primary image of the item.  This is the URL of the largest image available based on what the seller submitted.Occurrence:Always
items.category | string | The label of the category. For example:Toys & Hobbies|Action Figures|Comic Book HeroesOccurrence:Always
items.categoryId | string | The ID of the category of the item. For example: The ID for Toys & Hobbies|Action Figures|Comic Book Heroes is158671.Occurrence:Always
items.buyingOptions | string | A comma separated list of the purchase options available for the item. Currently the only supported option isFIXED_PRICE.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Always
items.sellerUsername | string | The seller's eBay user name.Occurrence:Always
items.sellerFeedbackPercentage | string | The percentage of the seller's total positive feedback.Occurrence:Always
items.sellerFeedbackScore | string | The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.Occurrence:Always
items.gtin | string | The unique Global Trade Item Number of the item as defined byhttps://www.gtin.info. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.Occurrence:Conditional
items.brand | string | The name brand of the item, such as Nike, Apple, etc.Occurrence:Conditional
items.mpn | string | The manufacturer part number, which is a number that is used in combination withbrandto identify a product.Occurrence:Conditional
items.epid | string | The eBay product identifier of a product from the eBay product catalog. You can use this value in the Browse APIsearchmethod to retrieve items for this product and in theMarketing APImethods to retrieve 'also viewed' and 'also bought' products to encourage up-selling and cross-selling.Occurrence:Conditional
items.conditionId | string | The identifier of the condition of the item. For example, 1000 is the identifier for NEW. For a list of condition names and IDs, seeItem Condition IDs and Names.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.condition | string | The text describing the condition of the item. For a list of condition names, seeItem Condition IDs and Names.Occurrence:Conditional
items.priceValue | string | The price of the item, which can be a discounted price. If it is discounted, information about the discount is returned in theoriginalPriceValue,originalPriceCurrency,discountAmount, anddiscountPercentagecolumns.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
items.priceCurrency | CurrencyCodeEnum | The currency used for the price of the item. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Always
items.primaryItemGroupId | string | The unique identifier for the item group that contains this item. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.Occurrence:Conditional
items.primaryItemGroupType | string | The item group type. Supported value:SELLER_DEFINED_VARIATIONS, indicates that the item group was created by the seller.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.itemEndDate | string | A timestamp that indicates the date and time an auction listing will end.This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into the local time of the buyer.Occurrence:Conditional
items.sellerItemRevision | string | An identifier generated/incremented when a seller revises the item. There are two types of item revisions:Seller changes, such as changing the titleeBay system changes, such as changing the quantity when an item is purchasedThis ID is changedonlywhen the seller makes a change to the item.Occurrence:Conditional
items.itemLocationCountry | string | The country where the item is physically located.Occurrence:Conditional
items.localizedAspects | string | A semicolon separated list of the name/value pairs for the aspects of the item, which are Base64 encoded. The aspect label is separated by a pipe (|), the aspect name and value are separated by a colon (:) and the name/value pairs are separated by a semicolon (;).Example without LabelEncoded Format:encodedName:encodedValue;encodedName:encodedValue;encodedName:encodedValueEncoded Example(The delimiters areemphasized):U2l6ZQ==:WEw=;Q29sb3I=:UmVk;U2xlZXZlcw==:TG9uZw==Decoded:Size:XL;Color:Red;Sleeves:LongExample with LabelEncoded Format:encodedLabel|encodedName:encodedValue;encodedName:encodedValue;encodedLabel|Encoded Example(The delimiters areemphasized):UHJvZHVjdCBJZGVudGlmaWVycw==|R1RJTg==:MDE5MDE5ODA2NjYzMw==;QlJBTkQ=:QXBwbGU=;UHJvZHVjdCBLZXkgRmVhdHVyZXM=|TW9kZWw=:aVBob25lIDc=Decoded:Product Identifiers|GTIN:0190198066633;BRAND:Apple;Product Key Features|Model:iPhone 7Note:The separators (|  :  ;) arenotencoded. You must decode each label, name, and value separately. You cannot decode the entire string.For more information, seeEncoded Aspectsin the Buying Integration Guide.Occurrence:Conditional
items.sellerTrustLevel | SellerTrustLevelEnum | An enumeration value representing the eBay status of the seller.Valid Values:TOP_RATED,ABOVE_STANDARD, or an empty value.An empty value indicates a return of anything other thanTOP_RATEDorABOVE_STANDARD.Code so that your app gracefully handles any future changes to this list.Occurrence:Always
items.availability | AvailabilityEnum | An enumeration value representing the item's availability (possibility of being purchased).Values:AVAILABLETEMPORARILY_UNAVAILABLEUNAVAILABLECode so that your app gracefully handles any future changes to this list.Occurrence:Always
items.imageAlteringProhibited | boolean | A boolean that indicates whether the images can be altered. If the value istrue, you cannot modify the image.Note:Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only.Occurrence:Always
items.estimatedAvailableQuantity | integer | The estimated quantity of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is very difficult to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.Note:If the seller of an item has the available threshold setting turned on, the value of this field will be null, and the availability of the item will instead be expressed through theavailabilityThresholdTypeandavailabilityThresholdfields.Note:To see if a listing is available for purchase, review theitemEndDateandestimatedAvailablityStatusfields. If the item has anEndDatein the past, or theestimatedAvailabilityStatusisOUT_OF_STOCK, the item is unavailable for purchase.Occurrence:Conditional
items.availabilityThresholdType | AvailabilityThresholdEnum | This column has a value only when the seller sets their availability threshold preference. The value of this column will showMORE_THAN, which indicates that the seller has more than the available threshold preference in stock for this item. Because the quantity of an item can change several times within a second, it is very difficult to return the exact quantity.Note:This field and theavailabilityThresholdfield will be returned as null if the actual quantity meets or drops below the threshold value, and then the buyer will want to look at the value in theestimatedAvailableQuantityfield.Occurrence:Conditional
items.availabilityThreshold | integer | This column has a value only when the seller sets their availability threshold preference. The value of this column will be "10", which is the threshold value.Note:This field and theavailabilityThresholdTypefield will be returned as null if the actual quantity meets or drops below the threshold value, and then the buyer will want to look at the value in theestimatedAvailableQuantityfield.Occurrence:Conditional
items.returnsAccepted | boolean | Indicates whether the seller accepts returns for the item.Occurrence:Always
items.returnPeriodValue | integer | The amount of days that the buyer has to return the item after the purchase date. For example, if this value is '30', the return period is 30 days.Occurrence:Conditional
items.returnPeriodUnit | TimeDurationUnitEnum | An enumeration value that indicates the period of time being used to measure the duration, such as business days, months, or years.TimeDurationUnitEnumis a common type shared by multiple eBay APIs and fields to express the time unit, but for return period duration, this value will always beDAY.Occurrence:Conditional
items.refundMethod | RefundMethodEnum | An enumeration value that indicates how a buyer is refunded when an item is returned.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.returnMethod | ReturnMethodEnum | An enumeration value that indicates the alternative methods for a full refund when an item is returned. This column will have data if the seller offers the buyer an item replacement or exchange instead of a monetary refund.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.returnShippingCostPayer | ReturnShippingCostPayerEnum | The party responsible for the return shipping costs when an item is returned.Valid Values:BUYERorSELLERCode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.acceptedPaymentMethods | string | This field is returned empty. For a list of payment methods available for a marketplace, see eBay help pages or the actual View Item page.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Always
items.deliveryOptions | DeliveryOptionsEnum | A comma-separated list of available delivery options. This column lets you search_filter out items than cannot be shipped to the buyer.Valid Values: SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, and PICKUP_DROP_OFF.Code so that your app gracefully handles any future changes to this list.Occurrence:Always
items.shipToIncludedRegions | string | A pipe (|) separated alphabetical list of the geographic countries and regions where the seller will ship the item.If a region is specified, you will need to subtract any countries and regions returned in theshipToExcludedRegionscolumn to fully understand where the seller will ship.The COUNTRY: list is separated from the REGION: list with a semicolon (;).Format Example:COUNTRY:US|BM|GL|MX|PM;REGION:AFRICA|ASIA|CENTRAL_AMERICA_AND_CARIBBEAN|EUROPE|MIDDLE_EAST|OCEANIA|SOUTH_AMERICA|SOUTHEAST_ASIA;Country Values:The two-letterISO 3166standard code of the country.Region Values:AFRICA, AMERICAS, ANTARCTIC, ARCTIC, ASIA, AUSTRALIA, CENTRAL_AMERICA_AND_CARIBBEAN, EUROPE, EURO_UNION, GREATER_CHINA, MIDDLE_EAST, NORTH_AMERICA, OCEANIA, REST_OF_ASIA, SOUTHEAST_ASIA, SOUTH_AMERICA, WORLDWIDECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.shipToExcludedRegions | string | A pipe (|) separated alphabetical list of the geographic countries and regions where the item cannot be shipped.These countries and regions refine (restrict) theshipToIncludedRegionslist.  The COUNTRY: list is separated from the REGION: list with a semicolon (;).Format Example:COUNTRY:US|BM|GL|MX|PM;REGION:AFRICA|ASIA|CENTRAL_AMERICA_AND_CARIBBEAN|EUROPE|MIDDLE_EAST|OCEANIA|SOUTH_AMERICA|SOUTHEAST_ASIA;Country Values:The two-letterISO 3166standard code of the country.Region Values:AFRICA, AMERICAS, ANTARCTIC, ARCTIC, ASIA, AUSTRALIA, CENTRAL_AMERICA_AND_CARIBBEAN, EUROPE, EURO_UNION, GREATER_CHINA, MIDDLE_EAST, NORTH_AMERICA, OCEANIA, REST_OF_ASIA, SOUTHEAST_ASIA, SOUTH_AMERICA, WORLDWIDECode so that your app gracefully handles any future changes to this list.Occurrence:Conditional
items.inferredEpid | string | The ePID (eBay Product ID of a product in the eBay product catalog) for the item, which has been programmatically determined by eBay using the item's title, aspects, and other data.If the seller actually provided an ePID at listing time for the item, the ePID value is returned in theepidcolumn instead.Occurrence:Conditional
items.inferredGtin | string | The GTIN (Global Trade Item Number) of the product as defined byhttps://www.gtin.info, which as been programmatically determined by eBay. This can be a UPC (Universal Product Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.If the seller provided a GTIN for the item, the seller's value is returned in thegtincolumn.Occurrence:Conditional
items.inferredBrand | string | The name brand for the item, such as Nike or Apple, which has been programmatically determined by eBay. To identify the product, this is always used along withMPN.If the seller provided a brand for the item, the seller's value is returned in thebrandcolumn.Occurrence:Conditional
items.inferredMpn | string | The MPN (Manufacturer's Part Number) for the item, which has been programmatically determined by eBay. To identify the product, this is always used along withbrand.If the seller provided a MPN for the item, the seller's value is returned in thempncolumn.Occurrence:Conditional
items.inferredLocalizedAspects | string | A semicolon separated list of the name/value pairs for the aspects of the item, which are Base64 encoded. These aspects have been programmatically determined by eBay. If the seller provided aspects for the item, the seller's values are returned in thelocalizedAspectscolumn.The aspect label is separated by a pipe (|), the aspect name and value are separated by a colon (:) and the name/value pairs are separated by a semicolon (;).Example without LabelEncoded Format:encodedName:encodedValue;encodedName:encodedValue;encodedName:encodedValueEncoded Example(The delimiters areemphasized):U2l6ZQ==:WEw=;Q29sb3I=:UmVk;U2xlZXZlcw==:TG9uZw==Decoded:Size:XL;Color:Red;Sleeves:LongExample with LabelEncoded Format:encodedLabel|encodedName:encodedValue;encodedName:encodedValue;encodedLabel|Encoded Example(The delimiters areemphasized):UHJvZHVjdCBJZGVudGlmaWVycw==|R1RJTg==:MDE5MDE5ODA2NjYzMw==;QlJBTkQ=:QXBwbGU=;UHJvZHVjdCBLZXkgRmVhdHVyZXM=|TW9kZWw=:aVBob25lIDc=Decoded:Product Identifiers|GTIN:0190198066633;BRAND:Apple;Product Key Features|Model:iPhone 7Note:The separators (|  :  ;) arenotencoded. You must decode each label, name, and value separately. You cannot decode the entire string.For more information, seeEncoded Aspectsin the Buying Integration Guide.Occurrence:Conditional
items.additionalImageUrls | string | A pipe separated (|) list of URLs for the additional images of the item. These images are in addition to the primary image, which is returned in theimageUrlcolumn.Note:This column can contain multiple values.Occurrence:Conditional
items.originalPriceValue | string | The original selling price of the item. This lets you surface a strikethrough price for the item.Occurrence:Conditional
items.originalPriceCurrency | CurrencyCodeEnum | The currency of theoriginalPriceValueof the item and thediscountAmount.Occurrence:Conditional
items.discountAmount | string | The calculated amount of the discount (originalPriceValue-priceValue). For example,  iforiginalPriceValueis 70 andpriceValueis 56, this value would be 14.Note:The currency shown inoriginalPriceCurrencyis used for bothdiscountAmountandoriginalPriceCurrency.Occurrence:Conditional
items.discountPercentage | string | The calculated discount percentage. For example, iforiginalPriceValueis 70 anddiscountAmountis 14, this value will be 20.Occurrence:Conditional
items.energyEfficiencyClass | string | Indicates theEuropean energy efficiencyrating (EEK) of the item. Data is returned in this column only if the seller specified the energy efficiency rating.The rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the least efficient. This rating helps buyers choose between various models.To retrieve the manufacturer's specifications for this item, when they are available, use thegetItemmethod in the Browse API. The information is returned in theproductFicheWebUrlfield.Occurrence:Conditional
items.qualifiedPrograms | string | A pipe separated list of the qualified programs available for the item.Valid Values:EBAY_PLUS: Indicates an item is eligible for eBay Plus. eBay Plus is a premium account option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected items.Note:eBay Plus is available only to buyers in Germany, Austria, and Australia marketplaces.AUTHENTICITY_GUARANTEE: Indicates that the item is eligible for the eBay Authenticity Guarantee program. This program enables third-party authenticators to perform authentication verification inspections on items such as watches and sneakers.FEATURED: Indicates that an item is eligible to be placed in a Focus Category. Focus Categories are specific categories dedicated to a certain type of product that allow a seller to better reach their target audience and increase their sales.Occurrence:Conditional
items.lotSize | integer | The number of items in a lot. In other words, a lot size is the number of items that are being sold together.A lot is a set of two or more items included in a single listing that must be purchased together in a single order line item. All the items in the lot are the same but there can be multiple items in a single lot,  such as the package of batteries shown in the example below.For example:ItemLot DefinitionLot SizeA package of 24 AA batteriesA box of 10 packages10A P235/75-15 Goodyear tire4 tires4Fashion Jewelry RingsPackage of 100 assorted rings100Note:Lots are not supported in all categories.Occurrence:Conditional | Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size
A package of 24 AA batteries | A box of 10 packages | 10
A P235/75-15 Goodyear tire | 4 tires | 4
Fashion Jewelry Rings | Package of 100 assorted rings | 100
items.lengthUnitOfMeasure | LengthUnitOfMeasureEnum | The unit of measurement used for the package dimensions, such as INCH, FEET, CENTIMETER, or METER.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.packageWidth | string | The width of the shipping package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.packageHeight | string | The height of the shipping package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.packageLength | string | The length of the shipping package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.weightUnitOfMeasure | WeightUnitOfMeasureEnum | The unit of measurement used for the package weight, such as POUND, KILOGRAM, OUNCE, or GRAM.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.packageWeight | string | The weight of the package that contains the item.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.shippingCarrierCode | string | The name of the shipping provider, such as FedEx, or USPS.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.shippingServiceCode | string | The type of shipping service. For example, USPS First Class.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.shippingType | string | The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.Occurrence:Conditional
items.shippingCost | string | The final shipping cost for all the items after all discounts are applied.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see the VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Conditional
items.shippingCostType | string | Indicates the class of the shipping cost.Valid Values:FIXED or CALCULATED.Occurrence:Conditional
items.additionalShippingCostPerUnit | string | Any per item additional shipping costs for a multi-item purchase. For example, let's say the shipping cost for a power cord is $3. But for an additional cord, the shipping cost is only $1. So if you bought 3 cords, theshippingCostwould be $3 and this value would be $2 ($1 for each additional item).Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.quantityUsedForEstimate | integer | The number of items used when calculating the estimation information.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Conditional
items.unitPrice | string | This is the price per unit for the item. Some European countries require listings for certain types of products to include the price per unit so buyers can accurately compare prices.For example:"unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
items.unitPricingMeasure | string | The designation, such as size, weight, volume, count, etc., that was used to specify the quantity of the item.  This helps buyers compare prices.For example, the following tells the buyer that the item is 7.99 per 100 grams."unitPricingMeasure": "100g","unitPrice": {"value": "7.99","currency": "GBP"Occurrence:Conditional
items.legacyItemId | string | The unique identifier of the eBay listing that contains the item. This is the traditional/legacy ID that is often seen in the URL of the listing View Item page.Occurrence:Always
items.alerts | string | A pipe-separated list of alerts available for the item.For example, if theDELAYED_DELIVERYalert was returned for an item, it would indicate a delay in shipping by the seller.Occurrence:Conditional
items.sellerAccountType | string | A string value that specifies whether the seller is a business or an individual. This is determined when the seller registers with eBay. If the seller registers for a business account, the value returned in this field will beBUSINESS. If the seller registers for a private account, the value returned in this field will beINDIVIDUAL.Note:This designation is required by the tax laws in some countries.This field is applicable only on the following marketplaces:EBAY_ATEBAY_BEEBAY_CHEBAY_DEEBAY_ESEBAY_FREBAY_GBEBAY_IEEBAY_ITEBAY_PLNote:This field will be returned empty on unsupported marketplaces.Valid Values:BUSINESSorINDIVIDUALOccurrence:Conditional
items.tyreLabelImageUrl | string | The URL to the image that shows the information on the tyre label.Occurrence:Conditional
items.priorityListingPayload | string | EPN (eBay Partner Network) publishers append this value to their affiliate tracking URL when using an EPN tracking link to track changes that occur to Priority Listing items.Example:amdata=enc%3AAQAFAAAAkB1DmsmXf%2BqZ%2BCEMGdebW6oR75GCMdBmc4MCQ%2FCEPqgKHbT0jdWhPwfY5LdUs6HTaP0eBlwKE7Smy2eDslewF7l3xjwWxjqwzNAnsYgxn2PiGkTKbiQSQytFUiymdtANpk1qOnBOoMGMK%2BWsji7jYlvySSs9o9s24TxD6RqWZpNrltzOU7mfnv3H40SZ3YESzg%3D%3DSeeCreating an EPN Tracking Linkfor information on EPN tracking links.Occurrence:Conditional
items.itemCreationDate | string | A timestamp indicating when the item was created.Format:UTCyyyy-MM-ddThh:mm:ss.sssZOccurrence:Always
items.itemWebUrl | string | The URL of the View Item page of the item.For example:Single SKU:https://www.ebay.de/itm/2********0MSKU:https://www.ebay.com/itm/2********9?var=5********2Occurrence:Conditional
items.defaultImageUrl | string | URL to the gallery or default image of the item. The other images of the item are returned in theadditionalImageUrlsfield.For examplehttps://i.ebayimg.com/00/s/M********w/z/W********p/$_1.JPG?set_id=8********FOccurrence:Conditional
items.itemAffiliateWebUrl | string | The URL of the View Item page of the item, with the affiliate tracking ID appended to it.For examplehttps://www.ebay.de/itm/2********0?mkevt=1&mkcid=1&mkrid=707-53477-19255-0&campid=CAMPAIGNID&toolid=2***6&customid=CUSTOMIDOccurrence:Conditional
items.ageGroup | string | The age group that the product is recommended for.Valid values:newborn,infant,toddler,kids,adult.Occurrence:Conditional
items.color | string | The color of the item.Occurrence:Conditional
items.pattern | string | Text describing the pattern used on the item. For example, paisley.Note:All the item aspects, including this aspect, are returned in the localizedAspects container.Occurrence:Conditional
items.size | string | The size of the item.Occurrence:Conditional
items.gender | string | In cases where items could vary by gender, this specifies for which gender the product is intended. Possible values include male, female, and unisex.Occurrence:Conditional
items.material | string | The material that the item is made of.Occurrence:Conditional
items.totalUnits | string | For an item that is priced by the unit, the total number of units that are on offer. For example, if the item is priced by the meter and 50 cm is on offer, thetotalUnitswould be 0.5 m.Occurrence:Conditional
items.ecoParticipationFeeValue | string | The amount of the Eco Participation Fee, a fee paid toward the eventual disposal of the purchased item.Occurrence:Conditional
items.ecoParticipationFeeCurrency | string | The currency in which the Eco Participation Fee for the item is paid.Occurrence:Conditional
items.takeBackPolicyLabel | string | The seller-defined label of the TAKE_BACK custom policy for the item. A TAKE_BACK policy describes the seller's regulatory responsibility to take back a purchased item for disposal when the buyer purchases a new one.Occurrence:Conditional
items.takeBackPolicyDescription | string | The seller-defined description of the TAKE_BACK custom policy for the item.Occurrence:Conditional
items.hazmatSignalWordId | string | The ID of the signal word for the hazardous material.Occurrence:Conditional
items.hazmatSignalWord | string | The localized signal word for the hazardous material, such as 'Danger'.Occurrence:Conditional
items.hazmatStatementIds | string | The IDs of hazardous material statements, separated by the pipe symbol. For example:H200|H221Occurrence:Conditional
items.hazmatStatementDescriptions | string | The Base64 encoded descriptions of hazardous material statements, separated by the pipe symbol. For example:encoded(Unstable explosives)|encoded(Flammable gas)Occurrence:Conditional
items.hazmatPictogramIds | string | The IDs of hazardous material pictograms, separated by the pipe symbol. For example:SGH01|SGH02Occurrence:Conditional
items.hazmatPictogramDescriptions | string | The Base64 encoded descriptions of hazardous material pictograms, separated by the pipe symbol. For example:encoded(exploding bomb)|encoded(flame)Occurrence:Conditional
items.hazmatPictogramImageUrls | string | The image URLs of hazardous material pictograms, separated by the pipe symbol. For example:https://img1|https://img2Occurrence:Conditional
items.hazmatAdditionalInformation | string | Base64 encoded additional information about the hazardous material.Occurrence:Conditional
items.repairScore | string | A score that describes how easy it is to repair the product. Score values range from 0.1 (hardest to repair) to 10.0 (easiest), always including a single decimal place.Occurrence:Conditional
items.conditionDescriptors | string | Note:Condition descriptors are currently only available for the following trading card categories:Non-Sport Trading Card SinglesCCG Individual CardsSports Trading Card SinglesThis field contains a list of the name/value pairs for the condition descriptors of the item, which are Base64 encoded. The descriptors are separated as follows:Name and value pairs are separated by a colon :Name:ValueBase64 encoding the above pair yieldsTmFtZQ==:VmFsdWU=Multiple descriptors are separated by a semicolon;Name1:Value1;Name2:Value2Base64 encoding the above multiple descriptors yieldsTmFtZTE=:VmFsdWUx;TmFtZTI=:VmFsdWUyMultiple values are separated by a pipe|Name1:Value1|Value2|Value3;Name2:Value1|Value2|Value3Base64 encoding the above multiple values (for multiple descriptors) yieldsTmFtZTE=:VmFsdWUx|VmFsdWUy|VmFsdWUz;TmFtZTI=:VmFsdWUx|VmFsdWUy|VmFsdWUzNote:The separators (: ; |) are not encoded. You must decode each name, and value or values separately. You cannot decode the entire string.Thenameandvalueare numeric IDs that map to the name and value, respectively, of a condition descriptor. A condition descriptor name-value pair provides more information about an item's condition in a structured way. Descriptors are name-value attributes that can be either from a closed set or open text. For more information on the numeric IDs and their text equivalents, use thegetItemConditionPoliciesmethod of theMetadata API.Occurrence:Conditional
items.sellerUserId | string | The unique identifier of an eBay user across all eBay sites. This value does not change, even when a user changes their username.Occurrence:Conditional
[/TABLE]

[TABLE]
Item | Lot Definition | Lot Size | A package of 24 AA batteries | A box of 10 packages | 10 | A P235/75-15 Goodyear tire | 4 tires | 4 | Fashion Jewelry Rings | Package of 100 assorted rings | 100
Item | Lot Definition | Lot Size
A package of 24 AA batteries | A box of 10 packages | 10
A P235/75-15 Goodyear tire | 4 tires | 4
Fashion Jewelry Rings | Package of 100 assorted rings | 100
[/TABLE]

[TABLE]
200 | Success
204 | No ContentThis code is returned when there are no items that meet the criteria for this feed file. SeeFeed File Filtersfor details.
206 | Partial Content
400 | Bad request
403 | Forbidden
404 | Not found
416 | Range not satisfiable
500 | Internal server error
[/TABLE]

[TABLE]
13000 | API_FEED | REQUEST | The request contains data that is invalid. Correct the request and submit the call again. For help, see the API Reference documentation for this call.
13003 | API_FEED | REQUEST | The 'feed_scope' {feed_scope} submitted is invalid. Valid values: {feedScopes}
13004 | API_FEED | REQUEST | The 'category_id' {category_id} submitted is invalid. See the API documentation for help on how to find category IDs.
13005 | API_FEED | REQUEST | The 'date' {feedDate} submitted is invalid. Either the date format is wrong, or the files are not available for the specific date. Valid values: {earliestDate} to {latestDate} in the past. The format is yyyyMMdd.
13006 | API_FEED | APPLICATION | There was a problem with an eBay internal system or process. Wait a few minutes and retry the call. If that doesn't work, contact eBay Support.
13007 | API_FEED | REQUEST | The feed file requested cannot be found. It is possible the file requested is in the process of being generated. Either change the date or try the call again later.
13009 | API_FEED | REQUEST | The mandatory 'feed_scope' query parameter is missing. Valid values: {feedScopes}
13010 | API_FEED | REQUEST | The mandatory 'category_id' query parameter is missing.
13011 | API_FEED | REQUEST | The mandatory 'date' query parameter is missing. Valid values: {earliestDate} to {latestDate} days in the past. The format is yyyyMMdd.
13012 | API_FEED | REQUEST | The marketplace Id {marketplaceId} is invalid. Valid values: {allowedMarketplaces}
13013 | API_FEED | REQUEST | The mandatory 'X-EBAY-C-MARKETPLACE-ID' header is missing. Valid values: {allowedMarketplaces}
13014 | API_FEED | REQUEST | The marketplace Id {marketplaceId} is not supported. Valid values: {allowedMarketplaces}
13015 | API_FEED | REQUEST | The mandatory 'Range' request header is missing. For help, see the API Reference documentation for this call.
13016 | API_FEED | REQUEST | The 'Range' request header format is invalid. Format: 'bytes=start position-end position'.  For help, see the API Reference documentation for this call.
13017 | API_FEED | REQUEST | The 'Range' header is invalid. Please verify that the start and end positions are correct. For help, see the API Reference documentation for this call.
13018 | API_FEED | REQUEST | The start position in the range header is invalid.
13019 | API_FEED | REQUEST | The end position in the range header is invalid.
13022 | API_FEED | REQUEST | The 'category_id' {category_id} submitted is not supported.
13023 | API_FEED | BUSINESS | Insufficient permissions to access this API for the marketplace {marketplaceId}. Please contact eBay Technical Support for further assistance.
13024 | API_FEED | BUSINESS | Insufficient permissions to access this API for the category {category_id}. Please contact eBay Technical Support for further assistance.
[/TABLE]