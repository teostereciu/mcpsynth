# suggestBudget

<span class="tablenote"><b>Note:</b> This method is only supported for Promoted Offsite campaigns. Sellers can use the <a href="/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility" target="_blank ">getAdvertisingEligibility</a> method of the <a href="//api-docs/sell/account/overview.html" target="_blank ">Account API v1</a> to determine if they are eligible for offsite campaigns.</span><br>This method allows sellers to retrieve the suggested budget for an offsite campaign.

## Endpoint

```
GET /ad_campaign/suggest_budget
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br><span class="tablenote"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span><br>See <a href="/api-docs/sell/marketing/types/ba:MarketplaceIdEnum" target="_blank ">MarketplaceIdEnum</a> for supported values. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/SuggestBudgetResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/ad_campaign/suggest_budget \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

campaign

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
