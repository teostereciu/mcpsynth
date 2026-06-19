# getAds

This method retrieves Promoted Listings ads that are associated with listings created with either the <a href="/Devzone/XML/docs/Reference/eBay/index.html" title="Trading API Reference">Trading API</a> or the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inventory API</a>. <p>The method retrieves ads related to the specified campaign. Specify the Promoted Listings campaign to target with the <b>campaign_id</b> path parameter.</p>  <p>Because of the large number of possible results, you can use query parameters to paginate the result set by specifying a <b>limit</b>, which dictates how many ads to return on each page of the response. You can also specify how many ads to skip in the result set before returning the first result using the <b>offset</b> path parameter.</p>  <p>Call <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to retrieve the current campaign IDs for the seller.</p>

## Endpoint

```
GET /ad_campaign/{campaign_id}/ad
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ads being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Query Parameters

- **ad_group_ids**: A comma-separated list of ad group IDs. The results will be filtered to only include active ads for these ad groups.<br><br>Use the <a href="/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups" target="_blank">getAdGroups</a> method to retrieve the ad group ID for the ad group.<br /><br /><span class="tablenote"><b>Note:</b> This field only applies to the Cost Per Click (CPC) funding model; it does not apply to the Cost Per Sale (CPS) funding model.</span> (Type: `string`)
- **ad_status**: A comma-separated list of ad statuses. The results will be filtered to only include the given statuses of the ad. If none are provided, all ads are returned.<br><br>See <a href="/api-docs/sell/marketing/types/pls:AdStatusEnum" target="_blank">AdStatusEnum</a> for supported values. (Type: `string`)
- **limit**: Specifies the maximum number of ads to return on a page in the paginated response.<br><br><b>Default: </b>10 <br><br><b>Maximum:</b> 500 (Type: `string`)
- **listing_ids**: A comma-separated list of listing IDs. <br><br><span class="tablenote"><b>Note:</b> The response includes only active ads. The results do not include listing IDs that are excluded by other conditions.</span> (Type: `string`)
- **offset**: Specifies the number of ads to skip in the result set before returning the first ad in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set.</p> <p><b>Default:</b> 0</p> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/AdPagedCollectionResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign/{campaign_id}/ad \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
