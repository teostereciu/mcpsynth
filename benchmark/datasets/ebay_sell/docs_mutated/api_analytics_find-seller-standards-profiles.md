# findSellerStandardsProfiles

This call retrieves all the standards profiles for the associated seller.  <br><br>A <i>standards profile </i> is a set of eBay seller metrics and the seller's associated compliance values (either <code>TOP_RATED</code>, <code>ABOVE_STANDARD</code>, or <code>BELOW_STANDARD</code>).  <br><br>A seller's multiple profiles are distinguished by two criteria, a "program" and a "cycle." A profile's <i>program </i> is one of three regions where the seller may have done business, or <code>PROGRAM_GLOBAL</code> to indicate all marketplaces where the seller has done business. The <i>cycle</i> value specifies whether the standards compliance values were determined at the last official eBay evaluation or at the time of the request.

## Endpoint

```
GET /seller_standards_profile
```

## API

Analytics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Response

**200**: Success

Response schema: `#/components/schemas/FindSellerStandardsProfilesResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/seller_standards_profile \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

seller_standards_profile

## Reference

- [eBay Analytics API Documentation](https://developer.ebay.com/api-docs/sell/analytics/overview.html)
