# suggestBids

<span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy program. For information about how to request access to this program, refer to <a href="/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests " target="_blank "> Priority Strategy Access Requests</a> in the Promoted Listings Playbook. To determine if a seller qualifies for priority strategy, use the <a href="/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility " target="_blank ">getAdvertisingEligibility</a> method in Account API.</span><br />This method allows sellers to retrieve the suggested bids for input keywords and match type.

## Endpoint

```
POST /ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **ad_group_id** (required): This path parameter specifies the unique identifier of the ad group containing the keywords for which the bid suggestions will be provided.<br><br> Use the <a href="/api-docs/sell/marketing/resources/ad_group/methods/getAdGroups" target="_blank">getAdGroups</a> method to retrieve ad group IDs. (Type: `string`)
- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the keywords for which bid suggestions will be provided.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/TargetedBidRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/TargetedBidsPagedCollection`

## Example

```bash
curl -X POST \
  https://api.ebay.com/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad_group

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
