# updateBid

This method updates the bid percentage (also known as the "ad rate") for the specified ad in the specified campaign. <p>In the request, supply the <b>campaign_id</b> and <b>ad_id</b> as path parameters, and supply the new <b>bidPercentage</b> value in the payload of the call.</p>  <p>Call <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns">getCampaigns</a> to retrieve a seller's current campaign IDs and call <a href="/api-docs/sell/marketing/resources/ad/methods/getAds">getAds</a> to get their ad IDs.</p><span class="tablenote"><b>Note:</b> This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See <a href="/api-docs/sell/static/marketing/pl-overview.html#funding-model">Funding Models</a> in the <i>Promoted Listings Playbook</i> for more information.</span>

## Endpoint

```
POST /ad_campaign/{campaign_id}/ad/{ad_id}/update_bid
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **ad_id** (required): This path parameter specifies the unique identifier of the ad for which the bid percentage is being updated.<br><br> Use the <a href="/api-docs/sell/marketing/resources/ad/methods/getAds" target="_blank">getAds</a> method to retrieve ad IDs. (Type: `string`)
- **campaign_id** (required): This path parameter specifies the unique eBay-assigned identifier of the ad campaign associated with the ad being updated.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve campaign IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/UpdateBidPercentageRequest`


## Response

**204**: No content

## Example

```bash
curl -X POST \
  https://api.ebay.com/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

ad

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
