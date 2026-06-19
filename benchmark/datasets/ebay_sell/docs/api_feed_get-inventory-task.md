# getInventoryTask

This method retrieves the task details and status of the specified inventory-related task. The input is <strong>task_id</strong>.

## Endpoint

```
GET /inventory_task/{task_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **task_id** (required): This path parameter is the unique identifier of the inventory task being retrieved.<br><br> Use the <a href="/api-docs/sell/feed/resources/inventory_task/methods/getInventoryTasks">getInventoryTasks</a> method to retrieve inventory task IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/InventoryTask`

## Example

```bash
curl -X GET \
  https://api.ebay.com/inventory_task/{task_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

inventory_task

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
