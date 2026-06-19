# getCustomPolicies

This method retrieves the list of custom policies defined for a seller's account. To limit the returned custom policies, specify the <b>policy_types</b> query parameter.

## Endpoint

```
GET /custom_policy/
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **policy_types**: This query parameter specifies the type of custom policies to be returned.<br><br>Multiple policy types may be requested in a single call by providing a comma-delimited set of all policy types to be returned.<br><br><span class="tablenote"><strong>Note:</strong> Omitting this query parameter from a request will also return policies of all policy types.</span><br> See the <a href="/api-docs/sell/account/types/api:CustomPolicyTypeEnum" target="_blank ">CustomPolicyTypeEnum</a> type for a list of supported values. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/CustomPolicyResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/custom_policy/ \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

custom_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
