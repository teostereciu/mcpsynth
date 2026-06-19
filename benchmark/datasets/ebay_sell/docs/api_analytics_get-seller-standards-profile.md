# getSellerStandardsProfile

This call retrieves a single standards profile for the associated seller.  <br><br>A <i>standards profile </i> is a set of eBay seller metrics and the seller's associated compliance values (either <code>TOP_RATED</code>, <code>ABOVE_STANDARD</code>, or <code>BELOW_STANDARD</code>).  <br><br>A seller can have multiple profiles distinguished by two criteria, a "program" and a "cycle." A profile's <i>program </i> is one of three regions where the seller may have done business, or <code>PROGRAM_GLOBAL</code> to indicate all marketplaces where the seller has done business. The <i>cycle</i> value specifies whether the standards compliance values were determined at the last official eBay evaluation (<code>CURRENT</code>) or at the time of the request (<code>PROJECTED</code>). Both cycle and a program values are required URI parameters for this method.

## Endpoint

```
GET /seller_standards_profile/{program}/{cycle}
```

## API

Analytics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **cycle** (required): This path parameter is used to specify the cycle for which metrics and metadata will be retrieved.<br><br>See <a href="/api-docs/sell/analytics/types/ssp:CycleTypeEnum" target="_blank">CycleTypeEnum</a> for a list of supported values. (Type: `string`)
- **program** (required): This path parameter is used to specify the seller standards program for which metrics and metadata will be retrieved. <br><br>See <a href="/api-docs/sell/analytics/types/ssp:ProgramEnum" target="_blank">ProgramEnum</a> for a list of supported values. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/StandardsProfile`

**204**: No content

## Example

```bash
curl -X GET \
  https://api.ebay.com/seller_standards_profile/{program}/{cycle} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

seller_standards_profile

## Reference

- [eBay Analytics API Documentation](https://developer.ebay.com/api-docs/sell/analytics/overview.html)
