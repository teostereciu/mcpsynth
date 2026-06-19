# getFulfillmentPolicies

This method retrieves all the fulfillment policies configured for the marketplace you specify using the <code>market_id</code> query parameter.

## Endpoint

```
GET /fulfillment_policy
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **market_id** (required): This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (Type: `string`)

## Headers

- **Content-Language**: Get the correct policies for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get the policies for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank">HTTP request headers</a>. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/FulfillmentPolicyResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/fulfillment_policy \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

fulfillment_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
