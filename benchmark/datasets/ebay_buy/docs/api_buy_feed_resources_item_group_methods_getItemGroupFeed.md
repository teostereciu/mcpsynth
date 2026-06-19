# buy/feed/resources/item_group/methods/getItemGroupFeed

*Source: https://developer.ebay.com/api-docs/buy/feed/resources/item_group/methods/getItemGroupFeed*

---

### Combining the Item Group and Item feed files

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

### Sample 1: Download the Daily Item Group Feed File

### Sample 2: Download the Weekly Bootstrap Item Group Feed File

#### Thank you for helping us to improve the eBay developer program.
GET/item_group
This method lets you download a TSV_GZIP (tab separated value gzip)Item Groupfeed file. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.There are two types of item group feed files generated:A dailyItem Groupfeed file containing the item group variation information associated with items returned in theItemfeed file for a specific day, category, and marketplace. (feed_scope=NEWLY_LISTED)A weeklyItem Group Bootstrapfeed file containing all the item group variation information associated with items returned in theItem Bootstrapfeed file for all the items in a specific category.  (feed_scope=ALL_ACTIVE)Note:Filters are applied to the feed files. For details, seeFeed File Filters.  When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.Note:The downloaded file will be gzipped automatically, so there is no reason to supplyAccept-Encoding:gzipas a header. If this header is supplied, the downloaded file will be compressed twice, and this has no extra benefit.The contents of these feed files are based on the contents of the corresponding dailyItemorItem Bootstrapfeed file. When a newItemorItem Bootstrapfeed file is generated, the service reads the file and if an item in the file has aprimaryItemGroupIdvalue, which indicates the item is part of an item group, it uses that value to return the item group (parent item) information for that item in the correspondingItem GrouporItem Group Bootstrapfeed file.This information includes the  name/value pair of the aspects of the items in this group returned in thevariesByLocalizedAspectscolumn. For example, if the item was a shirt some of the variation names could be Size, Color, etc. Also the images for the various aspects are returned in theadditionalImageUrlscolumn.The first line in any feed file is the header, which labels the columns and indicates the order of the values on each line.  Each header is described in theResponse fieldssection.Combining the Item Group and Item feed filesTheItem GrouporItem Group Bootstrapfeed file contains details about the item group (parent item), including the item group IDitemGroupId. You match the value ofitemGroupIdfrom theItem Groupfeed file with the value ofprimaryItemGroupIdfrom the corresponding dailyItemorItem Bootstrapfeed file.Downloading feed filesItem Group feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using theRangerequest header. Thecontent-rangeresponse header indicates where in the full resource this partial chunk of data belongs  and the total number of bytes in the file. For more information about using these headers, seeRetrieve a gzip feed file.Note:A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.RestrictionsFor a list of supported sites and other restrictions, seeAPI Restrictions.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
Thedateis required only for the dailyItem Groupfeed file. If you specify a date for theItem Group Bootstrapfile (feed_scope=ALL_ACTIVE), the date is ignored and the latest file is returned. The date theItem Group Bootstrapfeed file was generated is returned in theLast-Modifiedresponse header.
TheItem Groupfeed files are generated every day and there are 14 daily files available.
There is a 48 hour latency when generating the files. This means on July 10, the latest feed file you can download is July 8.
Occurrence:Optional
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Strongly Recommended
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.item.feed
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
SeeHTTP response headersfor details.
Important: The successful response of this call isalwaysaTSV_GZIP file. However, the response is shown as JSON fields for each column so that the value returned in each column can be explained. The order in which the response fields are listed is the order of the columns in the feed file.
The container for the array of items groups returned by thegetItemGroupFeedmethod. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values for each item. The header labels match the fields that are described in theResponse fieldssection.Occurrence:Always
Occurrence:Always
The unique identifier for the item group. This ID is returned in theprimaryItemGroupIdcolumn of theItem Feedfile.Occurrence:Always
The item group type. For example:SELLER_DEFINED_VARIATIONS, indicates that the item group was created by the seller.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Always
Important!This field no longer returns values and is scheduled for deprecation.
The seller created title of the item group. This text is an escaped string when special characters are present, using the following rules:
For example
Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\Tracking
Marvel Legends HULK 8"Figure Avengers Age of Ultron Studios 6"Series
"Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\\Tracking"
"Marvel Legends HULK 8\"Figure Avengers Age of Ultron Studios 6\"Series"
A pipe separated (|) list of the aspect (variation) names for this item group. The aspect name is Base64 encoded.Note:This column can contain multiple values.Encoded Format:aspectName|aspectNameEncoded Example(The delimiters areemphasized):Q29sb3I=|U2l6ZQ==Decoded:Color|SizeOccurrence:Always
Encoded Format:aspectName|aspectName
Encoded Example(The delimiters areemphasized):Q29sb3I=|U2l6ZQ==
Decoded:Color|Size
The URL to the primary image of the item. The other images of the item group are returned in theadditionalImageUrlscolumn.Occurrence:Always
A pipe separated (|) list of URLs for the additional images for the item group. These images are in addition to the primary image, which is returned in theimageUrlcolumn.Note:This column can contain multiple values.Occurrence:Conditional
Occurrence:Conditional
A boolean that indicates whether the images can be altered. If the value istrue, you cannot modify the image.Note:Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only.Occurrence:Always
Note:Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns a GZIP file containing the item group information for items in the Item feed (September 18, 2017 in the 
      Cameras & Photo category) that were associated with an item group.
The inputs arefeed_scope=NEWLY_LISTEDandcategory_idURI parameters.The request parameters are:Rangebytes=0-10485760andX-EBAY-C-MARKETPLACE-IDEBAY_US.
       For more information about using these headers, seeHTTP request headers.
GEThttps://api.ebay.com/buy/feed/v1_beta/item_group?feed_scope=NEWLY_LISTED&category_id=625&date=20180418
If the call is successful, the portion of the file specified by theRangeheader, is returned. The call returns a 206 HTTP status and theContent-rangebytes=0-10485760/251658240response header.
This sample returns the latest weeklyItem Group Bootstrapfeed file. It contains the item group variation information for the items in the correspondingItem Bootstrapfeed file that were associated with an item group.Note:Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The item groups in the file are for the items that were in the specified category on Sunday.
The inputs arefeed_scope=ALL_ACTIVE,category_id, anddateURI parameters.The request parameters are:Rangebytes=0-10485760andX-EBAY-C-MARKETPLACE-IDEBAY_US.
       For more information about using these headers, seeHTTP request headers.
Related topics
If you need help, contactDeveloper Technical Support.
- A dailyItem Groupfeed file containing the item group variation information associated with items returned in theItemfeed file for a specific day, category, and marketplace. (feed_scope=NEWLY_LISTED)
- A weeklyItem Group Bootstrapfeed file containing all the item group variation information associated with items returned in theItem Bootstrapfeed file for all the items in a specific category.  (feed_scope=ALL_ACTIVE)
- NEWLY_LISTED- Returns theItem Groupfeed file containing the  item group variation information for items in the dailyItemfeed file that were associated with an item group.The items in this type ofItemfeed file are items that were listed on the day specified by thedateparameter in the category specified by thecategory_idparameter.
- ALL_ACTIVE- Returns the weeklyItem Group Bootstrapfile containing the item group  variation information for items in the weeklyItem Bootstrapfeed file that were associated with an item group. The items are Good 'Til Cancelled items in the category specified by thecategory_idparameter.Note:Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The item groups in the file are for the items that were in the specified category on Sunday.Occurrence:Required
- Required only whenfeed_scope=NEWLY_LISTED
- Must be within 3-14 days in the past
- Double quotes (") and backslashes (\) in the Title are escaped with a backslash (\) character
- If there are any tabs (\t), double quotes ("), or backslashes (\) in the Title, the entire Title will be wrapped in double quotes.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
feed_scope | string | This query parameter specifies the type of file to return.Valid Values:NEWLY_LISTED- Returns theItem Groupfeed file containing the  item group variation information for items in the dailyItemfeed file that were associated with an item group.The items in this type ofItemfeed file are items that were listed on the day specified by thedateparameter in the category specified by thecategory_idparameter.ALL_ACTIVE- Returns the weeklyItem Group Bootstrapfile containing the item group  variation information for items in the weeklyItem Bootstrapfeed file that were associated with an item group. The items are Good 'Til Cancelled items in the category specified by thecategory_idparameter.Note:Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The item groups in the file are for the items that were in the specified category on Sunday.Occurrence:Required
category_id | string | This query parameter specifies eBay top-level category ID of the items to be returned in the feed file.The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplaces, you can use the Taxonomy APIgetCategoryTreemethod. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by thecategoryTreeNodeLevelfield.For example:"categoryTreeNodeLevel": 1For details seeGet Categories for Buy APIs.Restriction:Must be a top-level category other than Real Estate. Items listed under Real Estate L1 categories are excluded from all feeds in all marketplaces.Occurrence:Required
date | string | This query parameter specifies the date of the dailyItem Groupfeed file (feed_scope=NEWLY_LISTED) you want.Thedateis required only for the dailyItem Groupfeed file. If you specify a date for theItem Group Bootstrapfile (feed_scope=ALL_ACTIVE), the date is ignored and the latest file is returned. The date theItem Group Bootstrapfeed file was generated is returned in theLast-Modifiedresponse header.TheItem Groupfeed files are generated every day and there are 14 daily files available.There is a 48 hour latency when generating the files. This means on July 10, the latest feed file you can download is July 8.Note:The generated files are stored using MST (US Mountain Standard Time), which is -7 hours UTC time.Format:yyyyMMddRequirements:Required only whenfeed_scope=NEWLY_LISTEDMust be within 3-14 days in the pastOccurrence:Optional
[/TABLE]

[TABLE]
Header | Type | Description
Accept | string | The formats that the client accepts for the response.A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate error codes that are returned in JSON format.Default:application/json,text/tab-separated-valuesOccurrence:Required
X-EBAY-C-MARKETPLACE-ID | string | The ID of the eBay marketplace where the item is hosted. This value is case sensitive.For example:X-EBAY-C-MARKETPLACE-ID = EBAY_USFor a list of supported sites see,API Restrictions.Occurrence:Required
Range | string | This header specifies the range in bytes of the chunks of the gzip file being returned.Format:bytes=startpos-endposFor example, the following retrieves the first 10 MBs of the feed file.Range bytes=0-10485760For more information about using this header, seeRetrieving a gzip feed file.Maximum:100 MB (10MB in the Sandbox)Occurrence:Strongly Recommended
[/TABLE]

[TABLE]
Content-range | Thecontent-rangeresponse header indicates where in the full resource this partial chunk of data belongs. It returns the lower and upper values in bytes (specified by theRangeheader) of the chunk and the total size of the file being downloaded in bytes.Maximum range: 100 MBThe following is an example of acontent-rangeresponse, where 0-10 is the lower and upper limit in bytes and 1000 is the total size of the file in bytes.0-10/1000The following example of acontent-rangeresponse indicates the value of theRangeheader is invalid and a 416 status code is returned.*/1000For more information and examples, seeRetrieving a gzip feed file.
Last-Modified | Returns the generated date of the feed file, which will be the latest file available. For example:Last-ModifiedWed, 21 Oct 2015 07:28:00 GMT
[/TABLE]

[TABLE]
Output container/field | Type | Description
itemGroups | array ofItemGroup | The container for the array of items groups returned by thegetItemGroupFeedmethod. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values for each item. The header labels match the fields that are described in theResponse fieldssection.Occurrence:Always
itemGroups.itemGroupId | string | The unique identifier for the item group. This ID is returned in theprimaryItemGroupIdcolumn of theItem Feedfile.Occurrence:Always
itemGroups.itemGroupType | string | The item group type. For example:SELLER_DEFINED_VARIATIONS, indicates that the item group was created by the seller.Code so that your app gracefully handles any future changes to this list.Important!This field no longer returns values and is scheduled for deprecation.Occurrence:Always
itemGroups.title | string | The seller created title of the item group. This text is an escaped string when special characters are present, using the following rules:Double quotes (") and backslashes (\) in the Title are escaped with a backslash (\) characterIf there are any tabs (\t), double quotes ("), or backslashes (\) in the Title, the entire Title will be wrapped in double quotes.For exampleBefore:Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\TrackingMarvel Legends HULK 8"Figure Avengers Age of Ultron Studios 6"SeriesAfter:"Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W\\Tracking""Marvel Legends HULK 8\"Figure Avengers Age of Ultron Studios 6\"Series"Occurrence:Always
itemGroups.variesByLocalizedAspects | string | A pipe separated (|) list of the aspect (variation) names for this item group. The aspect name is Base64 encoded.Note:This column can contain multiple values.Encoded Format:aspectName|aspectNameEncoded Example(The delimiters areemphasized):Q29sb3I=|U2l6ZQ==Decoded:Color|SizeOccurrence:Always
itemGroups.imageUrl | string | The URL to the primary image of the item. The other images of the item group are returned in theadditionalImageUrlscolumn.Occurrence:Always
itemGroups.additionalImageUrls | string | A pipe separated (|) list of URLs for the additional images for the item group. These images are in addition to the primary image, which is returned in theimageUrlcolumn.Note:This column can contain multiple values.Occurrence:Conditional
itemGroups.imageAlteringProhibited | boolean | A boolean that indicates whether the images can be altered. If the value istrue, you cannot modify the image.Note:Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only.Occurrence:Always
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