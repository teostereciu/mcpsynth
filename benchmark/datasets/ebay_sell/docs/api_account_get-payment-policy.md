# getPaymentPolicy

This method retrieves the complete details of a payment policy. Supply the ID of the policy you want to retrieve using the <b>paymentPolicyId</b> path parameter.

## Endpoint

```
GET /payment_policy/{payment_policy_id}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **payment_policy_id** (required): This path parameter specifies the ID of the payment policy you want to retrieve. <br><br> This ID can be retrieved for a payment policy by using the <a href="/api-docs/sell/account/resources/payment_policy/methods/getPaymentPolicies" target="_blank ">getPaymentPolices</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/PaymentPolicy`

## Example

```bash
curl -X GET \
  https://api.ebay.com/payment_policy/{payment_policy_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payment_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
