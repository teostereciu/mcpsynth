# getAdsByInventoryReference

This method retrieves Promoted Listings ads associated with listings that are managed with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inventory API</a> from the specified campaign.<br /><br />Supply the <b>campaign_id</b> as a path parameter and use query parameters to specify the <b>inventory_reference_id</b> and <b>inventory_reference_type</b> pairs.<br /><br />In the Inventory API, an <i>inventory reference ID</i> is either a seller-defined <b>SKU</b> value or an <b>inventoryItemGroupKey</b> (a seller-defined ID for an inventory item group, which is an entity that's used in the Inventory API to create a multiple-variation listing). To indicate a listing managed by the Inventory API, you must always specify both an <b>inventory_reference_id</b> and the associated <b>inventory_reference_type</b>.<br /><br />Call <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to retrieve all of the seller's the current campaign IDs.<br /><br /><span class="tablenote"><b>Note:</b> This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See <a href="/api-docs/sell/static/marketing/pl-overview.html#funding-model">Funding Models</a> in the <i>Promoted Listings Playbook</i> for more information.</span>

## Endpoint

```
GET /ad_campaign/{campaign_id}/get_ads_by_inventory_reference
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ads being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Query Parameters

- **inventory_reference_id** (required): This query parameter specifies the unique identifier of a single-item listing or a multi-variation listing.<br><br>To retrieve an ad for a single-item listing, set the <b>inventoryReferenceType</b> value to <code>INVENTORY_ITEM</code> and specify an item ID or a SKU (if the SKU is defined in the listing).<br><br>To retrieve an ad for a multi-variation listing, set the <b>inventoryReferenceType</b> value to <code>INVENTORY_ITEM_GROUP</code> and specify the item ID for the multi-variation listing or the <b>inventoryitemGroupKey</b> value as defined in the Inventory API. (Type: `string`)
- **inventory_reference_type** (required): This query parameter specifies the type of the item the <b>inventory_reference_id</b> references.<br><br>See <a href="/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum" target="_blank">InventoryReferenceType</a> for supported values. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Ads`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign/{campaign_id}/get_ads_by_inventory_reference \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
