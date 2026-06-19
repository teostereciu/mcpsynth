# bulkUpdateAdsStatusByListingId

<span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy program. For information about how to request access to this program, refer to <a href="/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests " target="_blank "> Priority Strategy Access Requests</a> in the Promoted Listings Playbook. To determine if a seller qualifies for priority strategy, use the <a href="/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility " target="_blank ">getAdvertisingEligibility</a> method in Account API.</span><br />This method works with listings created with either the <a href="/Devzone/XML/docs/Reference/eBay/index.html">Trading API</a> or the <a href="/api-docs/sell/inventory/resources/methods">Inventory API</a>.<br /><br />The method updates the status of ads in bulk, based on listing ID values.<br /><br />Specify the <b>campaign_id</b> as a path parameter and supply a set of listing IDs with their updated <b>adStatus</b> values in the request body. An eBay listing ID is generated when a listing is created with the Trading API.<br /><br />Get the campaign IDs for a seller by calling <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> and call <a href="/api-docs/sell/marketing/resources/ad/methods/getAds">getAds</a> to retrieve a list of seller inventory reference IDs.

## Endpoint

```
POST /ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ads being updated.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/BulkUpdateAdStatusByListingIdRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/BulkAdUpdateStatusByListingIdResponse`

**207**: Multi Status

## Example

```bash
curl -X POST \
  https://api.ebay.com/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
