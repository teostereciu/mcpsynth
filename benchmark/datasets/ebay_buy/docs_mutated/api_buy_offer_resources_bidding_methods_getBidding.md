# buy/offer/resources/bidding/methods/getBidding

*Source: https://developer.ebay.com/api-docs/buy/offer/resources/bidding/methods/getBidding*

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

### Sample 1: Retrieve Bidding Information

#### Thank you for helping us to improve the eBay developer program.
GET/bidding/{listing_id}
This method retrieves the bidding details that are specific to the buyer of the specified auction. This must be an auction where the buyer has already placed a bid.To retrieve the bidding information you use auser access tokenand pass in the item ID of the auction. You can also retrieve general bidding details about the auction, such as minimum bid price and the count of unique bidders, using theBrowse APIgetItemsmethod.RestrictionsFor a list of supported sites and other restrictions, seeAPI Restrictions.
For a list of supported sites and other restrictions, seeAPI Restrictions.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.offer.auction
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The date the auction will end.Occurrence:Always
Occurrence:Always
An enumeration value that represents the current state of the auction, such asACTIVEorENDED.If this value isENDEDand the value ofhighBidderistrue, this indicates the buyer has won the auction.Occurrence:Always
The number of proxy bids that have been placed for the auction.Occurrence:Always
The amount of the highest bid, which is the current price of the item.Occurrence:Always
The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Always
The monetary amount.Occurrence:Always
The buyer's proxy bid, which is themaxAmountspecified in the request.Occurrence:Always
The maximum amount the buyer is willing to pay for the item.Occurrence:Always
Identifier of a specific proxy bid.Occurrence:Always
Indicates if the buyer is the highest bidder.If the value isfalse, this indicates that either the buyer has not bid on this item or has been out-bid.If this value istrue, this indicates the buyer is winning the auction and if the value ofauctionStatusisENDED, this indicates the buyer has won the auction.Occurrence:Always
The eBay RESTful identifier of an item being bid on, which was submitted in the request.Occurrence:Always
This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.Note:This is returned only for auctions that have a reserve price.Occurrence:Conditional
If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.
Note:This is returned only for auctions that have a reserve price.
Occurrence:Conditional
The suggested bid amount for the next bid.Note:These are generated suggestions and do not guarantee the buyer will win the bid. This means these suggestions do not take into account the max bid amount of other bidders. The buyer can be outbid even if they submit the highest suggested bid.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
Retrieves the bidding information for a specific auction where the buyer has placed at least one bid.
The input is theitem_idpassed in as a URI paramater.
GEThttps://api.ebay.com/buy/offer/v1_beta/bidding/v1|2**********2|0
This call returns the bidding information of a specific auction, such as if the buyer is the high bidder, thecurrentPrice,reservePriceMet,suggestedBidAmounts, etc.
Related topics
If you need help, contactDeveloper Technical Support.
- If the value isfalse, this indicates that either the buyer has not bid on this item or has been out-bid.
- If this value istrue, this indicates the buyer is winning the auction and if the value ofauctionStatusisENDED, this indicates the buyer has won the auction.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
listing_id | string | This path parameter specifies the unique eBay RESTful identifier of an item for which you want the buyer's bidding information.This ID is returned by theBrowseandFeedAPI methods.RESTful Item ID example:v1|2**********2|0For more information about item ID for RESTful APIs, see theLegacy API compatibilitysection of theBuy APIs Overview.Restriction:The buyer must have placed a bid for this item.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-MARKETPLACE-ID | string | The ID of the eBay marketplace where the buyer is based. This value is case sensitive.For example:X-EBAY-C-MARKETPLACE-ID = EBAY_USFor a list of supported sites see,API Restrictions.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
auctionEndDate | string | The date the auction will end.Occurrence:Always
auctionStatus | AuctionStatusEnum | An enumeration value that represents the current state of the auction, such asACTIVEorENDED.If this value isENDEDand the value ofhighBidderistrue, this indicates the buyer has won the auction.Occurrence:Always
bidCount | integer | The number of proxy bids that have been placed for the auction.Occurrence:Always
currentPrice | Amount | The amount of the highest bid, which is the current price of the item.Occurrence:Always
currentPrice.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Always
currentPrice.value | string | The monetary amount.Occurrence:Always
currentProxyBid | ProxyBid | The buyer's proxy bid, which is themaxAmountspecified in the request.Occurrence:Always
currentProxyBid.maxAmount | Amount | The maximum amount the buyer is willing to pay for the item.Occurrence:Always
currentProxyBid.maxAmount.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Always
currentProxyBid.maxAmount.value | string | The monetary amount.Occurrence:Always
currentProxyBid.proxyBidId | string | Identifier of a specific proxy bid.Occurrence:Always
highBidder | boolean | Indicates if the buyer is the highest bidder.If the value isfalse, this indicates that either the buyer has not bid on this item or has been out-bid.If this value istrue, this indicates the buyer is winning the auction and if the value ofauctionStatusisENDED, this indicates the buyer has won the auction.Occurrence:Always
itemId | string | The eBay RESTful identifier of an item being bid on, which was submitted in the request.Occurrence:Always
reservePriceMet | boolean | This indicates if the reserve price of the item has been met. A reserve price is set by the seller and is the minimum amount the seller is willing to sell the item for.If the highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the item is not sold.Note:This is returned only for auctions that have a reserve price.Occurrence:Conditional
suggestedBidAmounts | array ofAmount | The suggested bid amount for the next bid.Note:These are generated suggestions and do not guarantee the buyer will win the bid. This means these suggestions do not take into account the max bid amount of other bidders. The buyer can be outbid even if they submit the highest suggested bid.Occurrence:Conditional
suggestedBidAmounts.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Always
suggestedBidAmounts.value | string | The monetary amount.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
120000 | API_OFFER | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
120001 | API_OFFER | REQUEST | The item ID {listing_id} was not found. Check that this is an active auction item ID.
120015 | API_OFFER | REQUEST | The X-EBAY-C-MARKETPLACE-ID header is missing. This is a required header.
120017 | API_OFFER | REQUEST | The Marketplace {marketplace_id} is not supported. Supported values are [marketplace_ids].
120033 | API_OFFER | REQUEST | There is no bidding activity for this auction (item ID {listing_id}).
[/TABLE]