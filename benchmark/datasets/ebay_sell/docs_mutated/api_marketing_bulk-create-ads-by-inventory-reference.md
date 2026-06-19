# bulkCreateAdsByInventoryReference

This method adds multiple listings that are managed with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inventory API</a> to an existing Promoted Listings campaign.<br /><br />For general strategy campaigns using the Cost Per Sale (CPS) model, bulk ads may be directly created for the listing.<br /><br />For each listing specified in the request, this method:<br /><ul><li>Creates an ad for the listing.</li> <li>Sets the bid percentage (also known as the <i>ad rate</i>) for the ads created.</li> <li>Associates the ads created with the specified campaign.</li></ul><br />To create ads for a listing, specify their <b>inventoryReferenceId</b> and <b>inventoryReferenceType</b>, plus the <b>bidPercentage</b> for the ad in the payload of the request. Specify the campaign to which you want to associate the ads using the <b>campaign_id</b> path parameter.<br /><br /><span class="tablenote"><b>Note:</b> This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See <a href="/api-docs/sell/static/marketing/pl-overview.html#funding-model">Funding Models</a> in the <i>Promoted Listings Playbook</i> for more information.</span><br /><br />Use <a href="/api-docs/sell/marketing/resources/campaign/methods/createCampaign">createCampaign</a> to create a new campaign and use <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to get a list of existing campaigns.

## Endpoint

```
POST /ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign for which to associated the ads being created.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/BulkCreateAdsByInventoryReferenceRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/BulkCreateAdsByInventoryReferenceResponse`

**207**: Multi Status

## Example

```bash
curl -X POST \
  https://api.ebay.com/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
