# sendOfferToInterestedBuyers

This method sends eligible buyers offers to purchase items in a listing at a discount.  <br><br>When a buyer has shown <i>interest</i> in a listing, they become "eligible" to receive a seller-initiated offer to purchase the item(s).  <br><br>Sellers use <a href="/api-docs/sell/negotiation/resources/offer/methods/findEligibleItems">findEligibleItems</a> to get the set of listings that have interested buyers. If a listing has interested buyers, sellers can use this method (<b>sendOfferToInterestedBuyers</b>) to send an offer to the buyers who are interested in the listing. The offer gives buyers the ability to purchase the associated listings at a discounted price.  <br><br>For details about how to create seller offers to buyers, see <a href="/api-docs/sell/static/marketing/offers-to-buyers.html" title="Selling Integration Guide">Sending offers to buyers</a>.

## Endpoint

```
POST /send_offer_to_interested_buyers
```

## API

Negotiation API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): The eBay marketplace on which your listings with "eligible" buyers appear.  <br><br>For a complete list of supported marketplaces, see <a href="/api-docs/sell/negotiation/overview.html#requirements" title="Negotiation API Overview">Negotiation API requirements and restrictions</a>. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/CreateOffersRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/SendOfferToInterestedBuyersCollectionResponse`

## Example

```bash
curl -X POST \
  https://api.ebay.com/send_offer_to_interested_buyers \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

offer

## Reference

- [eBay Negotiation API Documentation](https://developer.ebay.com/api-docs/sell/negotiation/overview.html)
