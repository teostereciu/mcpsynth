# getInventoryItemGroup

This call retrieves the inventory item group for a given <strong>inventoryItemGroupKey</strong> value. The <strong>inventoryItemGroupKey</strong> value is passed in at the end of the call URI.

## Endpoint

```
GET /inventory_item_group/{inventoryItemGroupKey}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **inventoryItemGroupKey** (required): This path parameter specifies the unique identifier of the inventory item group being retrieved. This value is assigned by the seller when an inventory item group is created. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/InventoryItemGroup`

## Example

```bash
curl -X GET \
  https://api.ebay.com/inventory_item_group/{inventoryItemGroupKey} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

inventory_item_group

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
