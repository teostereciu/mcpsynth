# updatePaymentPolicy

This method updates an existing payment policy. Specify the policy you want to update using the <b>payment_policy_id</b> path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.

## Endpoint

```
PUT /payment_policy/{payment_policy_id}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **payment_policy_id** (required): This path parameter specifies the ID of the payment policy you want to update. <br><br> This ID can be retrieved for a payment policy by using the <a href="/api-docs/sell/account/resources/payment_policy/methods/getPaymentPolicies" target="_blank ">getPaymentPolices</a> method. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/PaymentPolicyRequest`


## Response

**200**: OK

Response schema: `#/components/schemas/SetPaymentPolicyResponse`

## Example

```bash
curl -X PUT \
  https://api.ebay.com/payment_policy/{payment_policy_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payment_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
