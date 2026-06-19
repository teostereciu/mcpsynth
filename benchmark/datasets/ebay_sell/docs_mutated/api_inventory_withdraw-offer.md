# withdrawOffer

This call is used to end a single-variation listing that is associated with the specified offer. This call is used in place of the <strong>deleteOffer</strong> call if the seller only wants to end the listing associated with the offer but does not want to delete the offer object. With this call, the offer object remains, but it goes into the unpublished state, and will require a <strong>publishOffer</strong> call to relist the offer.<br><br>To end a multiple-variation listing that is associated with an inventory item group, the <strong>withdrawOfferByInventoryItemGroup</strong> method can be used. This call only ends the multiple-variation listing associated with an inventory item group but does not delete the inventory item group object, nor does it delete any of the offers associated with the inventory item group, but instead all of these offers go into the unpublished state.

## Endpoint

```
POST /offer/{offerId}/withdraw
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **offerId** (required): This path parameter specifies the unique identifier of the offer that is to be withdrawn.<br><br>Use the <a href="/api-docs/sell/inventory/resources/offer/methods/getOffers">getOffers</a> method to retrieve offer IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/WithdrawResponse`

## Example

```bash
curl -X POST \
  https://api.ebay.com/offer/{offerId}/withdraw \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

offer

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
