# bulkGetInventoryItem

This call retrieves up to 25 inventory item records. The SKU value of each inventory item record to retrieve is specified in the request payload.<br><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> header. See the <a href="/api-docs/sell/inventory/resources/inventory_item/methods/bulkGetInventoryItem#h3-request-headers">HTTP request headers</a> for more information.</span><br>For those who prefer to retrieve only one inventory item record by SKU value, the <strong>getInventoryItem</strong> method can be used. To retrieve all inventory item records defined on the seller's account, the <strong>getInventoryItems</strong> method can be used (with pagination control if desired).

## Endpoint

```
POST /bulk_get_inventory_item
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/BulkGetInventoryItem`


## Response

**200**: Success

Response schema: `#/components/schemas/BulkGetInventoryItemResponse`

**207**: Multi-Status

## Example

```bash
curl -X POST \
  https://api.ebay.com/bulk_get_inventory_item \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

inventory_item

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
