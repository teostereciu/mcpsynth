# getCurrencies

This method returns the default currency used by the eBay marketplace specified in the request. This is the currency that the seller should use when providing price data for this marketplace through listing APIs.

## Endpoint

```
GET /marketplace/{marketplace_id}/get_currencies
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **marketplace_id** (required): This path parameter specifies the eBay marketplace for which currency information is retrieved.<br><br>See the <a href="/api-docs/sell/metadata/types/bas:MarketplaceIdEnum" target="_blank">MarketplaceIdEnum</a> type for a list of supported eBay marketplace ID values. (Type: `string`)

## Headers

- **Accept-Language**: This header is required to retrieve metadata for the French Canada and French Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.<br><br><span class="tablenote"><b>Note:</b> If <code>EBAY_BE</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the Dutch Belgium marketplace.</span></li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code> and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li><span class="tablenote"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span></ul> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/GetCurrenciesResponse`

**204**: No Content

## Example

```bash
curl -X GET \
  https://api.ebay.com/marketplace/{marketplace_id}/get_currencies \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

marketplace

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
