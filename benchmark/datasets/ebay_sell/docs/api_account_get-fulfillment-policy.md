# getFulfillmentPolicy

This method retrieves the complete details of a fulfillment policy. Supply the ID of the policy you want to retrieve using the <b>fulfillmentPolicyId</b> path parameter.

## Endpoint

```
GET /fulfillment_policy/{fulfillmentPolicyId}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **fulfillmentPolicyId** (required): This path parameter specifies the ID of the fulfillment policy you want to retrieve.<br><br> This ID can be retrieved for a fulfillment policy by using the <a href="/api-docs/sell/account/resources/fulfillment_policy/methods/getFulfillmentPolicies" target="_blank ">getFulfillmentPolicies</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/FulfillmentPolicy`

## Example

```bash
curl -X GET \
  https://api.ebay.com/fulfillment_policy/{fulfillmentPolicyId} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

fulfillment_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
