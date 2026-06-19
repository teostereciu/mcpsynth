# getCustomPolicy

This method retrieves the custom policy specified by the <b>custom_policy_id</b> path parameter.

## Endpoint

```
GET /custom_policy/{custom_policy_id}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **custom_policy_id** (required): This path parameter is the unique identifier of the custom policy to retrieve.<br><br> This ID can be retrieved for a custom policy by using the <a href="/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies" target="_blank ">getCustomPolicies</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/CustomPolicy`

## Example

```bash
curl -X GET \
  https://api.ebay.com/custom_policy/{custom_policy_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

custom_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
