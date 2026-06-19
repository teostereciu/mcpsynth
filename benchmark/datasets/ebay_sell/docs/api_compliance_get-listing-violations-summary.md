# getListingViolationsSummary

This call returns listing violation counts for a seller. A user can pass in one or more compliance types through the <strong>compliance_type</strong> query parameter. See <a href="/api-docs/sell/compliance/types/com:ComplianceTypeEnum">ComplianceTypeEnum</a> for more information on the supported listing compliance types. Listing violations are returned for multiple marketplaces if the seller sells on multiple eBay marketplaces.<br /><br /> <span class="tablenote"><strong>Note:</strong> Only a canned response, with counts for all listing compliance types, is returned in the Sandbox environment. Due to this limitation, the <strong>compliance_type</strong> query parameter (if used) will not have an effect on the response. </span>

## Endpoint

```
GET /listing_violation_summary
```

## API

Compliance API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **compliance_type**: <span class="tablenote"><b>Note:</b> The <a href="https://developer.ebay.com/api-docs/sell/compliance/types/com:ComplianceTypeEnum" target="_blank" rel="noopener">ASPECTS_ADOPTION</a> compliance type has been deprecated and will be decommissioned on September 9th, 2025.</span><br>This query parameter specifies the compliance type(s) of the listing violation counts being retrieved. <br><br>See <a href="/api-docs/sell/compliance/types/com:ComplianceTypeEnum">ComplianceTypeEnum</a> for more information on the supported compliance types that can be passed in here. <br><br>If more than one compliance type value is used, delimit these values with a comma. If no compliance type values are passed in, the listing count for all compliance types will be returned. <br /><br /> <span class="tablenote"><strong>Note:</strong> Only a canned response, with counts for all listing compliance types, is returned in the Sandbox environment. Due to this limitation, the <strong>compliance_type</strong> query parameter (if used) will not have an effect on the response. </span> (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace. <br><br>Supported values for this header can be found in the <a href="/api-docs/sell/compliance/types/bas:MarketplaceIdEnum">MarketplaceIdEnum</a> type definition. (Type: `string`)

## Response

**200**: Success

**204**: No Content

## Example

```bash
curl -X GET \
  https://api.ebay.com/listing_violation_summary \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

listing_violation_summary

## Reference

- [eBay Compliance API Documentation](https://developer.ebay.com/api-docs/sell/compliance/overview.html)
