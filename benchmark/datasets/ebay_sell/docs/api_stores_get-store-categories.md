# getStoreCategories

This method is used to retrieve the category hierarchy for an eBay user's store.<br><br><span class="tablenote"><strong>Note:</strong> Three levels of store categories are supported.</span>

## Endpoint

```
GET /store/categories
```

## API

Stores API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Response

**200**: OK

Response schema: `#/components/schemas/GetStoreCategoriesResponseType`

## Example

```bash
curl -X GET \
  https://api.ebay.com/store/categories \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

store

## Reference

- [eBay Stores API Documentation](https://developer.ebay.com/api-docs/sell/stores/overview.html)
