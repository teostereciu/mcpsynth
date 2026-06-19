# getReturnPolicy

This method retrieves the complete details of the return policy specified by the <b>returnPolicyId</b> path parameter.

## Endpoint

```
GET /return_policy/{return_policy_id}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **return_policy_id** (required): This path parameter specifies the unique identifier of the return policy you want to retrieve. <br><br> This ID can be retrieved for a return policy by using the <a href="/api-docs/sell/account/resources/return_policy/methods/getReturnPolicies" target="_blank ">getReturnPolicies</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/ReturnPolicy`

## Example

```bash
curl -X GET \
  https://api.ebay.com/return_policy/{return_policy_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

return_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
