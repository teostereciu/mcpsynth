# findEligibleItems

This method evaluates a seller's current listings and returns the set of IDs that are eligible for a seller-initiated discount offer to a buyer.  <br><br>A listing ID is returned only when one or more buyers have shown an "interest" in the listing.  <br><br>If any buyers have shown interest in a listing, the seller can initiate a "negotiation" with them by calling <a href="/api-docs/sell/negotiation/resources/offer/methods/sendOfferToInterestedBuyers">sendOfferToInterestedBuyers</a>, which sends all interested buyers a message that offers the listing at a discount.  <br><br>For details about how to create seller offers to buyers, see <a href="/api-docs/sell/static/marketing/offers-to-buyers.html" title="Selling Integration Guide">Sending offers to buyers</a>.

## Endpoint

```
GET /find_eligible_items
```

## API

Negotiation API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **limit**: This query parameter specifies the maximum number of items to return from the result set on a page in the paginated response.<br><br><b>Minimum:</b> 1<br><br><b>Maximum:</b> 200<br><br><b>Default: </b>10 (Type: `string`)
- **offset**: This query parameter specifies the number of results to skip in the result set before returning the first result in the paginated response.  <br><br>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 results from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set. <br><br><b>Default:</b> 0 (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): The eBay marketplace on which you want to search for eligible listings. <br><br>For a complete list of supported marketplaces, see <a href="/api-docs/sell/negotiation/overview.html#requirements" title="Negotiation API Overview">Negotiation API requirements and restrictions</a>. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/PagedEligibleItemCollection`

**204**: No Content

## Example

```bash
curl -X GET \
  https://api.ebay.com/find_eligible_items \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

offer

## Reference

- [eBay Negotiation API Documentation](https://developer.ebay.com/api-docs/sell/negotiation/overview.html)
