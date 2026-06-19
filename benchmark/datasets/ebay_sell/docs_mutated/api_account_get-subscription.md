# getSubscription

This method retrieves a list of subscriptions associated with the seller account.

## Endpoint

```
GET /subscription
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **limit**: This field is for future use. (Type: `string`)
- **continuation_token**: This field is for future use. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/SubscriptionResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/subscription \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

subscription

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
