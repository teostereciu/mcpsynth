# bulkDeleteAdsByInventoryReference

This method works with listings created with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inventory API</a>.<br /><br />The method deletes a set of ads, as specified by a list of inventory reference IDs, from the specified campaign. <i>Inventory reference IDs</i> are seller-defined IDs that are used with the Inventory API</a>.<br /><br />Pass the <b>campaign_id</b> as a path parameter and populate the payload with a list of <b>inventoryReferenceId</b> and <b>inventoryReferenceType</b> pairs that you want to delete.<br /><br />Get the campaign IDs for a seller by calling <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> and call <a href="/api-docs/sell/marketing/resources/ad/methods/getAds">getAds</a> to get a list of the seller's inventory reference IDs.<br /><br /><span class="tablenote"><b>Note:</b> This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See <a href="/api-docs/sell/static/marketing/pl-overview.html#funding-model">Funding Models</a> in the <i>Promoted Listings Playbook</i> for more information.</span>

## Endpoint

```
POST /ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign for which to delete a set of ads.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/BulkDeleteAdsByInventoryReferenceRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/BulkDeleteAdsByInventoryReferenceResponse`

**207**: Multi Status

## Example

```bash
curl -X POST \
  https://api.ebay.com/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
