# buy/feed/resources/item_priority/methods/getItemPriorityFeed

*Source: https://developer.ebay.com/api-docs/buy/feed/resources/item_priority/methods/getItemPriorityFeed*

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

### Sample 1: Download a Priority Item Feed File

#### Thank you for helping us to improve the eBay developer program.
GET/item_priority
Using this method, you can download a TSV_GZIP (tab separated value gzip)Item Priorityfeed file, which allows you to track changes (deltas) in the status of your priority items, such as when an item is added or removed from a campaign.  The delta feed tracks the changes to the status of items within a category you specify in the input URI. You can also specify a specific date for the feed you want returned.Important!You must consume the daily feeds (Item,Item Group) before consuming theItem Priorityfeed. This ensures that your inventory is up to date.Note:The downloaded file will be gzipped automatically, so there is no reason to supplyAccept-Encoding:gzipas a header. If this header is supplied, the downloaded file will be compressed twice, and this has no extra benefit.Downloading feed filesNote:Filters are applied to the feed files. For details, seeFeed File Filters. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.Priority Item feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using theRangerequest header. TheContent-rangeresponse header indicates where in the full resource this partial chunk of data belongs  and the total number of bytes in the file. For more information about using these headers, seeRetrieve a gzip feed file.In addition to the API, there is an open sourceFeed SDKwritten in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.Note:A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.RestrictionsFor a list of supported sites and other restrictions, seeAPI Restrictions.
Important!You must consume the daily feeds (Item,Item Group) before consuming theItem Priorityfeed. This ensures that your inventory is up to date.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.item.feed
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
SeeHTTP response headersfor details.
Important: The successful response of this call isalwaysaTSV_GZIP file. However, the response is shown as JSON fields for each column so that the value returned in each column can be explained. The order in which the response fields are listed is the order of the columns in the feed file.
The container for the array of items returned by thegetItemPriorityFeedmethod. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values on each line. The header labels match the fields that are described in theResponse fieldssection.Occurrence:Always
Occurrence:Always
The unique identifier of an item in eBay RESTful format. An example would bev1|1********2|4********2.Occurrence:Always
EPN (eBay Partner Network) publishers append this value to their affiliate tracking URL when using an EPN tracking link to track changes that occur to Priority Listing items.Example:_trkparms=ispr%3D1&amdata=enc%3AAQAFAAAAkB1DmsmXf%2BqZ%2BCEMGdebW6oR75GCMdBmc4MCQ%2FCEPqgKHbT0jdWhPwfY5LdUs6HTaP0eBlwKE7Smy2eDslewF7l3xjwWxjqwzNAnsYgxn2PiGkTKbiQSQytFUiymdtANpk1qOnBOoMGMK%2BWsji7jYlvySSs9o9s24TxD6RqWZpNrltzOU7mfnv3H40SZ3YESzg%3D%3DSeeCreating an EPN Tracking Linkfor information on EPN tracking links.Occurrence:Conditional
Occurrence:Conditional
Status change indicator of the listing.Values:ADDED_TO_CAMPAIGNREMOVED_FROM_CAMPAIGNTRACKING_PAYLOAD_REFRESHEDNote:When a listing is removed from the campaign,PriorityListingPayloadwill be empty.When multiple status changes are returned for a listing, thechangeMetadatavalue will be a pipe-separated string (e.g.,ADDED_TO_CAMPAIGN|TRACKING_PAYLOAD_REFRESHED).To use the returned value, you will need to separate the string by pipe (|).Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns a GZIP file with the priority items in the Cameras & Photo category whose statuses changed on July 18, 2021. In this example, the size of the file being returned is 142MB (148897792 bytes) and the requestRangeheader specifies to return the first 10MB (10485760 bytes).
The inputs are acategory_idof625(Cameras & Photo) and adatein the formatyyyyMMdd.The request 
      parameters are:Rangebytes=0-10485760andX-EBAY-C-MARKETPLACE-IDEBAY_US. For more information about using these headers, 
      seeHTTP request headers.
GEThttps://api.ebay.com/buy/feed/v1_beta/item_priority?category_id=625&date=20210718
If the call is successful, the portion of theItem Priorityfeed file specified by theRangeheader is returned.The call returns a 206 HTTP status and theContent-rangebytes=0-10485760/148897792response header.
Related topics
If you need help, contactDeveloper Technical Support.
- ADDED_TO_CAMPAIGN
- REMOVED_FROM_CAMPAIGN
- TRACKING_PAYLOAD_REFRESHED
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
category_id | string | This query parameter specifies the eBay top-level category ID of the items to be returned in the feed file.The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplaces, you can use the Taxonomy APIgetCategoryTreemethod. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by thecategoryTreeNodeLevelfield.For example:"categoryTreeNodeLevel": 1For details seeGet the eBay categories of a marketplace.Restriction:Must be a top-level category other than Real Estate. Items listed under Real Estate L1 categories are excluded from all feeds in all marketplaces.Occurrence:Required
date | string | This query parameter specifies the date of the feed you want returned.This can be up to 14 days in the past but cannot be set to a date in the future.Format:yyyyMMddNote:The dailyItemfeed files are available each day after 9AM MST (US Mountain Standard Time), which is -7 hours UTC time.There is a 48 hour latency when generating theItemfeed files. This means you can download the file for July 10th on July 12 after 9AM MST.For categories with a large number of items, the latency can be up to 72 hours.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Accept | string | The formats that the client accepts for the response.A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate error codes that are returned in JSON format.Default:application/json,text/tab-separated-valuesOccurrence:Required
X-EBAY-C-MARKETPLACE-ID | string | The ID of the eBay marketplace where the item is hosted. This value is case sensitive.For example:X-EBAY-C-MARKETPLACE-ID = EBAY_USFor a list of supported sites see,Buy API Support by Marketplace.Occurrence:Required
Range | string | Header specifying content range to be retrieved. Only supported range is bytes.Example:bytes = 0-102400.Occurrence:Required
[/TABLE]

[TABLE]
Content-range | The content range for the current request. Typically in the format :0-100/1000where0-100is the content length of the current response and1000is the total content length. In case of a416status code, content-range would be*/1000, which denotes an invalid range header.
Last-Modified | Signifies the date when the files are generated.For example:Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT.
[/TABLE]

[TABLE]
Output container/field | Type | Description
itemDelta | array ofItemPriority | The container for the array of items returned by thegetItemPriorityFeedmethod. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values on each line. The header labels match the fields that are described in theResponse fieldssection.Occurrence:Always
itemDelta.itemId | string | The unique identifier of an item in eBay RESTful format. An example would bev1|1********2|4********2.Occurrence:Always
itemDelta.priorityListingPayload | string | EPN (eBay Partner Network) publishers append this value to their affiliate tracking URL when using an EPN tracking link to track changes that occur to Priority Listing items.Example:_trkparms=ispr%3D1&amdata=enc%3AAQAFAAAAkB1DmsmXf%2BqZ%2BCEMGdebW6oR75GCMdBmc4MCQ%2FCEPqgKHbT0jdWhPwfY5LdUs6HTaP0eBlwKE7Smy2eDslewF7l3xjwWxjqwzNAnsYgxn2PiGkTKbiQSQytFUiymdtANpk1qOnBOoMGMK%2BWsji7jYlvySSs9o9s24TxD6RqWZpNrltzOU7mfnv3H40SZ3YESzg%3D%3DSeeCreating an EPN Tracking Linkfor information on EPN tracking links.Occurrence:Conditional
itemDelta.changeMetadata | string | Status change indicator of the listing.Values:ADDED_TO_CAMPAIGNREMOVED_FROM_CAMPAIGNTRACKING_PAYLOAD_REFRESHEDNote:When a listing is removed from the campaign,PriorityListingPayloadwill be empty.When multiple status changes are returned for a listing, thechangeMetadatavalue will be a pipe-separated string (e.g.,ADDED_TO_CAMPAIGN|TRACKING_PAYLOAD_REFRESHED).To use the returned value, you will need to separate the string by pipe (|).Occurrence:Always
[/TABLE]

[TABLE]
200 | Success
204 | No Content
206 | Partial Content
400 | Bad request
403 | Forbidden
404 | Not found
416 | Range not satisfiable
500 | Internal server error
[/TABLE]

[TABLE]
13000 | API_FEED | REQUEST | The request contains data that is invalid. Correct the request and submit the call again. For help, see the API Reference documentation for this call.
13004 | API_FEED | REQUEST | The 'category_id' {category_id} submitted is invalid. See the API documentation for help on how to find category IDs.
13005 | API_FEED | REQUEST | The 'date' {feedDate} submitted is invalid. Either the date format is wrong, or the files are not available for the specific date. Valid values: {earliestDate} to {latestDate} in the past. The format is yyyyMMdd.
13006 | API_FEED | APPLICATION | There was a problem with an eBay internal system or process. Wait a few minutes and retry the call. If that doesn't work, contact eBay Support.
13007 | API_FEED | REQUEST | The feed file requested cannot be found. It is possible the file requested is in the process of being generated. Either change the date or try the call again later.
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
13023 | API_FEED | BUSINESS | Insufficient permissions to access this API for the marketplace {marketplaceId}. Please contact eBay Technical support for further assistance.
13024 | API_FEED | BUSINESS | Insufficient permissions to access this API for the category {category_id}. Please contact eBay Technical support for further assistance.
[/TABLE]