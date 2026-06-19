# getPaymentPolicyByName

This method retrieves the details of a specific payment policy. Supply both the policy <code>name</code> and its associated <code>market_id</code> in the request query parameters.

## Endpoint

```
GET /payment_policy/get_by_policy_name
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **market_id** (required): This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (Type: `string`)
- **name** (required): This query parameter specifies the seller-defined name of the payment policy you want to retrieve.<br><br> This value can be retrieved for a payment policy by using the <a href="/api-docs/sell/account/resources/payment_policy/methods/getPaymentPolicies" target="_blank ">getPaymentPolicies</a> method. (Type: `string`)

## Headers

- **Content-Language**: Get the correct policy for a marketplace that supports multiple locales using the <code>Content-Language</code> request header. For example, get a policy for the French locale of the Canadian marketplace by specifying <code>fr-CA</code> for the <code>Content-Language</code> header. Likewise, target the Dutch locale of the Belgium marketplace by setting <code>Content-Language: nl-BE</code>. For details on header values, see <a href="/api-docs/static/rest-request-components.html#HTTP">HTTP request headers</a>. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/PaymentPolicy`

## Example

```bash
curl -X GET \
  https://api.ebay.com/payment_policy/get_by_policy_name \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payment_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
