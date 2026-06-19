# deleteProductCompatibility

This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible product list. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

## Endpoint

```
DELETE /inventory_item/{seller_sku}/product_compatibility
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **seller_sku** (required): This path parameter specifies the SKU (stock keeping unit) of the inventory item that is associated with the product compatibility list that is being deleted.<br><br>Use the <a href="/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems" target="_blank ">getInventoryItems</a> method to retrieve SKU values. (Type: `string`)

## Response

**204**: No Content

## Example

```bash
curl -X DELETE \
  https://api.ebay.com/inventory_item/{seller_sku}/product_compatibility \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

product_compatibility

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
