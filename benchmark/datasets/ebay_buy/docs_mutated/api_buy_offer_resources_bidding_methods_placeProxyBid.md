# buy/offer/resources/bidding/methods/placeProxyBid

*Source: https://developer.ebay.com/api-docs/buy/offer/resources/bidding/methods/placeProxyBid*

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

### Sample 1: Place a Proxy Bid

#### Thank you for helping us to improve the eBay developer program.
POST/bidding/{listing_id}/place_proxy_bid
This method uses auser access tokento place a proxy bid for the buyer on a specific auction item. The item must offerAUCTIONas one of thebuyingOptions.To place a bid, you pass in the item ID of the auction as a URI parameter and the buyer's maximum bid amount (maxAmount) in the payload.   By placing a proxy bid, the buyer is agreeing to purchase the item if they win the auction.After this bid is placed, if someone else outbids the buyer a bid, eBay automatically bids again for the buyer up to the amount of their maximum bid. When the bid exceeds the buyer's maximum bid, eBay will notify them that they have been outbid.To find auctions, you can use theBrowse API to searchfor items and use a search_filter to return only auction items. For example:/buy/browse/v1/item_summary/search?q=iphone&search_filter=buyingOptions:{AUCTION}RestrictionsFor a list of supported sites and other restrictions, seeAPI Restrictions.
After this bid is placed, if someone else outbids the buyer a bid, eBay automatically bids again for the buyer up to the amount of their maximum bid. When the bid exceeds the buyer's maximum bid, eBay will notify them that they have been outbid.To find auctions, you can use theBrowse API to searchfor items and use a search_filter to return only auction items. For example:/buy/browse/v1/item_summary/search?q=iphone&search_filter=buyingOptions:{AUCTION}
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.offer.auction
SeeOAuth access tokensfor more information.
The amount of the proxy bid to be placed. This is the maximum amount the buyer is willing to pay for the item.Note:Currency for the bid must be the currency specified by the seller when listing the item.VAT (value added tax) does not need to be added to the proxy bid amount even if VAT applies.Occurrence:Required
The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Required
The monetary amount.Occurrence:Required
Specifies whether the buyer wants to give their consent to bid on adult-only items. For a buyer to bid on an adult-only item, you must collect their consent using this field, and they must agree to the Terms of Use.For more information about adult-only items on eBay, seeAdult-Only items on eBay.Default:falseOccurrence:Optional
For more information about adult-only items on eBay, seeAdult-Only items on eBay.
Default:false
Occurrence:Optional
The type that defines the fields for buyer consent to bid on adult-only items.This field must be included in theplaceProxyBidrequest and set totrueif the buyer is bidding on anadult-onlyitem.For more information about adult-only items on eBay, seeAdult-Only items on eBay.Occurrence:Conditional
Occurrence:Conditional
This call has no response headers.
Identifier of the proxy bid created by the request. This indicates that the bid was placed and is not used for anything else.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
Places a bid for a buyer on an auction item.
The input is theitem_idpassed in as a URI paramater and the buyer's maximum bid in the payload.
POSThttps://api.ebay.com/buy/offer/v1_beta/bidding/v1|2**********2|0/place_proxy_bid
This call places the bid for the buyer and returns theproxyBidId.
Related topics
If you need help, contactDeveloper Technical Support.
- Currency for the bid must be the currency specified by the seller when listing the item.
- VAT (value added tax) does not need to be added to the proxy bid amount even if VAT applies.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
listing_id | string | This path parameter specifies the unique eBay RESTful identifier of an item you want to bid on.This ID is returned by theBrowseandFeed BetaAPI methods.RESTful Item ID Example:v1|2**********2|0For more information about item ID for RESTful APIs, see theLegacy API compatibilitysection of theBuy APIs Overview.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
X-EBAY-C-MARKETPLACE-ID | string | The ID of the eBay marketplace where the buyer is based. This value is case sensitive.For example:X-EBAY-C-MARKETPLACE-ID = EBAY_USFor a list of supported sites see,API Restrictions.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
maxAmount | Amount | The amount of the proxy bid to be placed. This is the maximum amount the buyer is willing to pay for the item.Note:Currency for the bid must be the currency specified by the seller when listing the item.VAT (value added tax) does not need to be added to the proxy bid amount even if VAT applies.Occurrence:Required
maxAmount.currency | CurrencyCodeEnum | The three-letterISO 4217code representing the currency of the amount in thevaluefield.Occurrence:Required
maxAmount.value | string | The monetary amount.Occurrence:Required
userConsent | UserConsent | Specifies whether the buyer wants to give their consent to bid on adult-only items. For a buyer to bid on an adult-only item, you must collect their consent using this field, and they must agree to the Terms of Use.For more information about adult-only items on eBay, seeAdult-Only items on eBay.Default:falseOccurrence:Optional
userConsent.adultOnlyItem | boolean | The type that defines the fields for buyer consent to bid on adult-only items.This field must be included in theplaceProxyBidrequest and set totrueif the buyer is bidding on anadult-onlyitem.For more information about adult-only items on eBay, seeAdult-Only items on eBay.Occurrence:Conditional
[/TABLE]

[TABLE]
Output container/field | Type | Description
proxyBidId | string | Identifier of the proxy bid created by the request. This indicates that the bid was placed and is not used for anything else.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | OK
400 | Bad request
404 | Not found
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
120000 | API_OFFER | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
120001 | API_OFFER | REQUEST | The item ID {listing_id} was not found. Check that this is an active auction item ID.
120002 | API_OFFER | BUSINESS | The auction was ended because the item was purchased with Buy It Now (fixed_price).
120003 | API_OFFER | BUSINESS | A seller cannot place a bid.
120004 | API_OFFER | BUSINESS | You are not eligible to bid on this item.
120005 | API_OFFER | BUSINESS | The bid price cannot be greater than the Buy It Now price.
120006 | API_OFFER | BUSINESS | You are not eligible to bid on this item due to seller restrictions.
120007 | API_OFFER | REQUEST | The bid amount is too high.
120008 | API_OFFER | BUSINESS | The bid amount is too low.
120009 | API_OFFER | BUSINESS | The bid currency needs to match the item price currency.
120010 | API_OFFER | BUSINESS | You cannot lower your proxy bid.
120011 | API_OFFER | REQUEST | The bid amount exceeds the max_results.
120012 | API_OFFER | BUSINESS | The auction has ended.
120013 | API_OFFER | REQUEST | The bid amount is missing or invalid.
120014 | API_OFFER | REQUEST | The bid currency is invalid. Refer to the documentation for a list of currency codes.
120015 | API_OFFER | REQUEST | The X-EBAY-C-MARKETPLACE-ID header is missing. This is a required header.
120016 | API_OFFER | REQUEST | The maximum bid amount is missing.
120017 | API_OFFER | REQUEST | The Marketplace {marketplaceId} is not supported. Supported values are {allowedMarketplaces}.
120018 | API_OFFER | REQUEST | For this auction, the bid amount cannot have decimals.
120019 | API_OFFER | BUSINESS | You must be pre-approval to bid on this auction.
120020 | API_OFFER | BUSINESS | A user agreement acceptance is required for this auction.
120021 | API_OFFER | BUSINESS | You are not authorized to bid on adult items. See the eBay help on adult items.
120022 | API_OFFER | BUSINESS | A privacy user agreement is required for this auction.
120023 | API_OFFER | BUSINESS | This is a business to business only auction.
120024 | API_OFFER | BUSINESS | The item is currently unavailable.
120025 | API_OFFER | BUSINESS | The bid was blocked because you have exceeded the item purchased max_results.
120026 | API_OFFER | BUSINESS | The bid was blocked due to a seller restriction based on your feedback score.
120027 | API_OFFER | BUSINESS | The bid was blocked due to a seller restriction on the shipping location.
120028 | API_OFFER | BUSINESS | The auction is restricted to users with a linked PayPal accounts.
120029 | API_OFFER | BUSINESS | There has been a buyer policy violation.
120030 | API_OFFER | BUSINESS | The bid was blocked due to unpaid items.
120031 | API_OFFER | BUSINESS | This requires credit card verification.
120032 | API_OFFER | REQUEST | This requires the user's consent for adult items.
[/TABLE]