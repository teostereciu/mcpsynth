# getStoreTasks

This method retrieves the status of all async store tasks for a store. Every task is set as FAILED or COMPLETED once it's execution time reaches 24 hours.

## Endpoint

```
GET /store/tasks
```

## API

Stores API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Response

**200**: OK

Response schema: `#/components/schemas/GetStoreTasksResponseType`

## Example

```bash
curl -X GET \
  https://api.ebay.com/store/tasks \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

store

## Reference

- [eBay Stores API Documentation](https://developer.ebay.com/api-docs/sell/stores/overview.html)
