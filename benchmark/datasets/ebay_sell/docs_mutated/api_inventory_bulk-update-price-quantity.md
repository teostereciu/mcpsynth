# bulkUpdatePriceQuantity

This call is used by the seller to update the total ship-to-home quantity of one inventory item, and/or to update the price and/or quantity of one or more offers associated with one inventory item. Up to 25 offers associated with an inventory item may be updated with one <strong>bulkUpdatePriceQuantity</strong> call. Only one SKU (one product) can be updated per call.<br><br><span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> header. See the <a href="/api-docs/sell/inventory/resources/inventory_item/methods/bulkUpdatePriceQuantity#h3-request-headers">HTTP request headers</a> for more information.</span><br>The <strong>getOffers</strong> call can be used to retrieve all offers associated with a SKU. The seller will just pass in the correct SKU value through the <strong>seller_sku</strong> query parameter. To update an offer, the <strong>offerId</strong> value is required, and this value is returned in the <strong>getOffers</strong> call response. It is also useful to know which offers are unpublished and which ones are published. To get this status, look for the <strong>status</strong> value in the <strong>getOffers</strong> call response. Offers in the published state are live eBay listings, and these listings will be revised with a successful <strong>bulkUpdatePriceQuantity</strong> call.<br><br>An issue will occur if duplicate <strong>offerId</strong> values are passed through the same <strong>offers</strong> container, or if one or more of the specified offers are associated with different products/SKUs.<br><br><span class="tablenote"><strong>Note:</strong> For multiple-variation listings, it is recommended that the <strong>bulkUpdatePriceQuantity</strong> call be used to update price and quantity information for each SKU within that multiple-variation listing instead of using <strong>createOrReplaceInventoryItem</strong> calls to update the price and quantity for each SKU. Just remember that only one SKU (one product variation) can be updated per call.</span></p>

## Endpoint

```
POST /bulk_update_price_quantity
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/BulkPriceQuantity`


## Response

**200**: Success

Response schema: `#/components/schemas/BulkPriceQuantityResponse`

**207**: Multi-Status

## Example

```bash
curl -X POST \
  https://api.ebay.com/bulk_update_price_quantity \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

inventory_item

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
