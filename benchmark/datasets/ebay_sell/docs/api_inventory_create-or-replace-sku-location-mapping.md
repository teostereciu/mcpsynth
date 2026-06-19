# createOrReplaceSkuLocationMapping

This method allows sellers to map multiple fulfillment center locations to single-SKU listing, or to a single SKU within a multiple-variation listing. This allows eBay to leverage the location metadata associated with a seller’s fulfillment centers to calculate more accurate estimated delivery dates on their listing.<br><br><span class="tablenote"><b>Note:</b> While location mappings can be created for listings on any eBay marketplace, the improved delivery date estimate feature is currently only supported for US-based fulfillment centers shipping domestically within the US.</span><br>The listing for which the locations will be mapped is specified through the <b>listingId</b> and <b>sku</b> values associated with the item. Note that only a single SKU value can be identified; if the seller wishes to map locations to multiple/all SKU values in a multiple-variation listing, this method must be called for each of those SKUs within the listing.<br><br><span class="tablenote"><b>Note:</b> Sellers should keep track of <b>listingId</b>/<b>sku</b> pairs that have been used for location mapping, as there is no programmatic way to retrieve or delete these pairs at this time.</span><br>In the case of replacing/updating existing location mappings, this method will do a complete replacement of the location mappings associated with a SKU. This means that each existing location mappings that the seller wants to continue to associate with the SKU are required in the update call, regardless of if they are affected by the update.<br><br>This method is only supported for inventory locations that have <code>FULFILLMENT_CENTER</code> as one of their <b>locationTypes</b>. For more information on fulfillment center locations, see <a href="/api-docs/sell/static/inventory/multi-warehouse-program.html#create-location" target="_blank ">Create a fulfillment center location</a>.<br><br>For more information on location mapping features, see <a href="/api-docs/sell/static/inventory/multi-warehouse-program.html" target="_blank ">Multi-warehouse program</a> in the Selling Integration Guide.<br><br><span class="tablenote"><b>Note:</b> Only listings with SKU values are supported. Sellers using listings creating through the Trading API can add a SKU value to their single variation listing through the <a href="/Devzone/XML/docs/Reference/eBay/AddFixedPriceItem.html#Request.Item.SKU" target="_blank ">Item.SKU</a> field during listing creation or by using the <b>ReviseItem</b> family of calls.</span>

## Endpoint

```
PUT /listing/{listingId}/sku/{sku}/locations
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **listingId** (required): This path parameter specifies the unique identifier of the listing for which multiple fulfillment center locations will be mapped to a SKU within that listing.<br><br>Use the <a href="/api-docs/sell/inventory/resources/offer/methods/getOffers" target="_blank ">getOffers</a> method of the Inventory API or the <a href="/devzone/xml/docs/reference/ebay/getmyebayselling.html" target="_blank ">GetMyEbaySelling</a> method of the Trading API to retrieve all listing IDs for all active listings. (Type: `string`)
- **sku** (required): This path parameter specifies the seller-defined SKU value of the item/variation for which multiple fulfillment center locations will be mapped. This SKU value must be defined in the listing specified in <b>listingId</b> parameter.<br><br>Use the <a href="/api-docs/sell/inventory/resources/offer/methods/getOffers" target="_blank ">getOffers</a> method of the Inventory API or the <a href="/devzone/xml/docs/reference/ebay/getmyebayselling.html" target="_blank ">GetMyEbaySelling</a> method of the Trading API to retrieve all listing IDs for all active listings.<br><br><span class="tablenote"><b>Note:</b> SKU values can be updated by a seller at any time. If a seller updates a SKU value that is being used for location mapping, this change will not be reflected until the mapping is updated through the <b>createOrReplaceSkuLocationMapping</b> method.</span> (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/LocationMapping`


## Response

**204**: No Content

## Example

```bash
curl -X PUT \
  https://api.ebay.com/listing/{listingId}/sku/{sku}/locations \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

listing

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
