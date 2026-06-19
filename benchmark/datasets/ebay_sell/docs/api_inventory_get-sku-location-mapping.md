# getSkuLocationMapping

This method allows sellers to retrieve the locations mapped to a specific SKU within a listing.<br><br>The <b>listingId</b> and <b>sku</b> of the listing are passed in as path parameters. This method only retrieves location mappings for a single SKU value; if a seller wishes to retrieve the location mappings for all items in a multiple-variation listing, this method must be called for each variation in the listing.<br><br>If there are fulfillment center locations mapped to the SKU, they will be returned in the <b>locations</b> array. If no locations are mapped to the SKU, status code <b>404 Not Found</b> will be returned.

## Endpoint

```
GET /listing/{listingId}/sku/{sku}/locations
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **listingId** (required): This path parameter specifies the unique identifier of the listing that the SKU belongs to for which all mapped locations will be retrieved.<br><br>Use the <a href="/api-docs/sell/inventory/resources/offer/methods/getOffers" target="_blank ">getOffers</a> method of the <b>Inventory API</b> or the <a href="/devzone/xml/docs/reference/ebay/getmyebayselling.html" target="_blank ">GetMyEbaySelling</a> method of the <b>Trading API</b> to retrieve all listing IDs for all active listings. (Type: `string`)
- **sku** (required): This path parameter specifies the seller-defined SKU value of the item/variation for which location mappings will be retrieved. This SKU value must be defined in the listing specified in <b>listingId</b> parameter<br><br>Use the <a href="/api-docs/sell/inventory/resources/offer/methods/getOffers" target="_blank ">getOffers</a> method of the <b>Inventory API</b> or the <a href="/devzone/xml/docs/reference/ebay/getmyebayselling.html" target="_blank ">GetMyEbaySelling</a> method of the <b>Trading API</b> to retrieve all SKUs for all active listings. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/LocationMapping`

## Example

```bash
curl -X GET \
  https://api.ebay.com/listing/{listingId}/sku/{sku}/locations \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

listing

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
