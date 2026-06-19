# getAdGroup

<span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy program. For information about how to request access to this program, refer to <a href="/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests " target="_blank "> Priority Strategy Access Requests</a> in the Promoted Listings Playbook. To determine if a seller qualifies for priority strategy, use the <a href="/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility " target="_blank ">getAdvertisingEligibility</a> method in Account API.</span><br />This method retrieves the details of a specified ad group, such as the ad group’s default bid and status.<br /><br />In the request, specify the <b>campaign_id</b> and <b>ad_group_id</b> as path parameters.<br /><br />Call <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to retrieve a list of the current campaign IDs for a seller and call <a href="/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups">getAdGroups</a> for the ad group ID of the ad group you wish to retrieve.

## Endpoint

```
GET /ad_campaign/{campaign_id}/ad_group/{ad_group_id}
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **ad_group_id** (required): This path parameter specifies the unique identifier of the ad group being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/ad_group/methods/getAdGroups" target="_blank">getAdGroups</a> method to retrieve ad group IDs. (Type: `string`)
- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ad group being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/AdGroup`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign/{campaign_id}/ad_group/{ad_group_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad_group

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
