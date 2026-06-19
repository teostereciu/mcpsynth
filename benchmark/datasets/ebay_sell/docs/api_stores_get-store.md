# getStore

This method is used to retrieve information for an eBay user's store such as store name, store URL, and description.

## Endpoint

```
GET /store
```

## API

Stores API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Response

**200**: OK

Response schema: `#/components/schemas/GetStoreResponseType`

## Example

```bash
curl -X GET \
  https://api.ebay.com/store \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

store

## Reference

- [eBay Stores API Documentation](https://developer.ebay.com/api-docs/sell/stores/overview.html)
