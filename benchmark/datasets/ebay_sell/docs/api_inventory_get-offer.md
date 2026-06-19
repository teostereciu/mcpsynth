# getOffer

This call retrieves a specific published or unpublished offer. The unique identifier of the offer (<strong>offerId</strong>) is passed in at the end of the call URI.<p>The <code>authorization</code> header is the only required HTTP header for this call. See the <strong>HTTP request headers</strong> section for more information.</p>

## Endpoint

```
GET /offer/{offerId}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **offerId** (required): This path parameter specifies the unique identifier of the offer that is to be retrieved.<br><br>Use the <a href="/api-docs/sell/inventory/resources/offer/methods/getOffers">getOffers</a> method to retrieve offer IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/EbayOfferDetailsWithAll`

## Example

```bash
curl -X GET \
  https://api.ebay.com/offer/{offerId} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

offer

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
