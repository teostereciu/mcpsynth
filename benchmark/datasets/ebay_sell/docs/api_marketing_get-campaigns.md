# getCampaigns

This method retrieves the details for all of the seller's defined campaigns. Request parameters can be used to retrieve a specific campaign, such as the campaign's name, the start and end date, the channel, the status, and the funding model (i.e., Cost Per Sale (CPS) or Cost Per Click (CPC)). <p>You can filter the result set by a campaign name, end date range, start date range, campaign channel, or campaign status. You can also paginate the records returned from the result set using the <b>limit</b> query parameter, and control which records to return using the  <b>offset</b> parameter.</p>

## Endpoint

```
GET /ad_campaign
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **campaign_name**: This query parameter specifies the name of the campaign being retrieved. The results are filtered to include only the campaign by the specified name.<br><br> Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getCampaigns" target="_blank">getCampaigns</a> method to retrieve a list of a seller's campaign names.<br /><br /><b>Note: </b>The results might be null if other filters exclude the campaign with this name. <br /><br /><b>Maximum: </b> 1 campaign name (Type: `string`)
- **campaign_status**: This query parameter specifies the status of the campaign(s) being retrieved.<br><br><span class="tablenote"><b>Note:</b> The results might not include all the campaigns with this status if other filters exclude them.</span><br><b>Valid values:</b> See <a href="/api-docs/sell/marketing/types/pls:CampaignStatusEnum">CampaignStatusEnum</a> <br /><br /><b>Maximum: </b> 1 status (Type: `string`)
- **campaign_targeting_types**: This query parameter specifies the targeting type of the campaign(s) to be retrieved.<br><br>The results will be filtered to only include campaigns with the specified targeting type. If not specified, all campaigns matching other filter parameters will be returned. The results might not include these campaigns if other search conditions exclude them.<br><br><b>Valid values:</b> See <a href="/api-docs/sell/marketing/types/pls:CampaignTargetingTypeEnum">CampaignTargetingTypeEnum</a> (Type: `string`)
- **channels**: This query parameter specifies the channel for the campaign(s) being retrieved.<br><br>The results will be filtered to only include campaigns with the specified channel. If not specified, all campaigns matching other filter parameters will be returned. The results might not include these campaigns if other search conditions exclude them.<br /><br /><b>Valid Values:</b> See <a href="/api-docs/sell/marketing/types/pls:ChannelEnum">ChannelEnum</a> (Type: `string`)
- **end_date_range**: This query parameter specifies the range of a campaign's end date. The results are filtered to include only campaigns with an end date that is within specified range. <br><br><b>Valid format (UTC)</b>: <ul><li><code> yyyy-MM-ddThh:mm:ssZ..yyyy-MM-ddThh:mm:ssZ </code>  (campaign ends within this range)</li><li><code>yyyy-MM-ddThh:mm:ssZ..</code> (campaign ends on or after this date)</li><li><code>..yyyy-MM-ddThh:mm:ssZ </code> (campaign ends on or before this date)</li><li><code>2016-09-08T00:00.00.000Z..2016-09-09T00:00:00Z</code> (campaign ends on September 08, 2016)</li></ul><br><span class="tablenote"><b>Note:</b>The results might not include all the campaigns ending on this date if other filters exclude them.</span> (Type: `string`)
- **funding_strategy**: This query parameter specifies the funding strategy for the campaign(s) being retrieved.<br /><br />The results will be filtered to only include campaigns with the specified funding model. If not specified, all campaigns matching the other filter parameters will be returned. The results might not include these campaigns if other search conditions exclude them.<br /><br /><b>Valid Values:</b> See <a href="/api-docs/sell/marketing/types/pls:FundingModelEnum">FundingModelEnum</a> (Type: `string`)
- **limit**: <p>This query parameter specifies the maximum number of campaigns to return on a page in the paginated response.</p>  <b>Default: </b>10<br><br><b>Maximum: </b> 500 (Type: `string`)
- **offset**: This query parameter specifies the number of campaigns to skip in the result set before returning the first report in the paginated response.<br><br>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set.<br><br> <b>Default:</b> 0 (Type: `string`)
- **start_date_range**: This query parameter specifies the range of a campaign's start date in which to filter the results. The results are filtered to include only campaigns with a start date that is equal to this date or is within specified range.<br><br><b>Valid format (UTC): </b> <ul><li><code>yyyy-MM-ddThh:mm:ssZ..yyyy-MM-ddThh:mm:ssZ</code> (starts within this range)</li><li><code>yyyy-MM-ddThh:mm:ssZ</code> (campaign starts on or after this date)</li><li><code>..yyyy-MM-ddThh:mm:ssZ </code>(campaign starts on or before this date)</li><li><code>2016-09-08T00:00.00.000Z..2016-09-09T00:00:00Z</code> (campaign starts on September 08, 2016)</li></ul><br><span class="tablenote"><b>Note:</b> The results might not include all the campaigns with this start date if other filters exclude them.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/CampaignPagedCollectionResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

campaign

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
