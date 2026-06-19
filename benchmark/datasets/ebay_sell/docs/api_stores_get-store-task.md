# getStoreTask

This method retrieves the current status of a recent store operation. The unique identifier of the task is passed in as a path parameter.

## Endpoint

```
GET /store/tasks/{task_id}
```

## API

Stores API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **task_id** (required): The unique identifier of an eBay Store async task. A taskId value is returned in the response of other successful calls. (e.g.addStoreCategory, moveStoreCategory, deleteStoreCategory). (Type: `string`)

## Response

**200**: OK

Response schema: `#/components/schemas/GetStoreTaskResponseType`

## Example

```bash
curl -X GET \
  https://api.ebay.com/store/tasks/{task_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

store

## Reference

- [eBay Stores API Documentation](https://developer.ebay.com/api-docs/sell/stores/overview.html)
