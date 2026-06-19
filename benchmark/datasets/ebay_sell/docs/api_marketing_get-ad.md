# getAd

This method retrieves the specified ad from the specified campaign.  <p>In the request, supply the <b>campaign_id</b> and <b>ad_id</b> as path parameters.</p> <p>Call <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to retrieve a list of the seller's current campaign IDs and call <a href="/api-docs/sell/marketing/resources/ad/methods/getAds">getAds</a> to retrieve their current ad IDs.</p>

## Endpoint

```
GET /ad_campaign/{campaign_id}/ad/{ad_id}
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **ad_id** (required): This path parameter specifies the unique identifier of the ad being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/ad/methods/getAds" target="_blank">getAds</a> method to retrieve ad IDs. (Type: `string`)
- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ad being retrieved.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Ad`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign/{campaign_id}/ad/{ad_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
