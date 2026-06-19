# getAdGroups

<span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy program. For information about how to request access to this program, refer to <a href="/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests " target="_blank "> Priority Strategy Access Requests</a> in the Promoted Listings Playbook. To determine if a seller qualifies for priority strategy, use the <a href="/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility " target="_blank ">getAdvertisingEligibility</a> method in Account API.</span><br />This method retrieves ad groups for the specified campaigns.<br /><br />Each campaign can only have <b>one</b> ad group.<br /><br />In the request, supply the <b>campaign_ids</b> as path parameters.<br /><br />Call <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to retrieve a list of the current campaign IDs for a seller.

## Endpoint

```
GET /ad_campaign/{campaign_id}/ad_group
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ad groups being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Query Parameters

- **ad_group_status**: A comma-separated list of ad group statuses. The results will be filtered to only include the given statuses of the ad group.<br><br> See <a href="/api-docs/sell/marketing/types/pls:AdGroupStatusEnum" target="_blank">AdGroupStatusEnum</a> for supported values. (Type: `string`)
- **limit**: The number of results, from the current result set, to be returned in a single page. (Type: `string`)
- **offset**: The number of results that will be skipped in the result set. This is used with the <b>limit</b> field to control the pagination of the output.<br /><br />For example, if the <b>offset</b> is set to <code>0</code> and the <b>limit</b> is set to <code>10</code>, the method will retrieve items 1 through 10 from the list of items returned. If the <b>offset</b> is set to <code>10</code> and the <b>limit</b> is set to <code>10</code>, the method will retrieve items 11 through 20 from the list of items returned.<br><br><b>Default</b>: <code>0</code> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/AdGroupPagedCollectionResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign/{campaign_id}/ad_group \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad_group

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
