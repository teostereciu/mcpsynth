# getOrderTask

This method retrieves the task details and status of the specified task. The input is <strong>task_id</strong>. <p>For details about how this method is used, see <a href="/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html">Working with Order Feeds</a> in the Selling Integration Guide.  </p>

## Endpoint

```
GET /order_task/{task_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **task_id** (required): This path parameter is the unique identifier of the order task being retrieved.<br><br>Use the <a href="/api-docs/sell/feed/resources/order_task/methods/getOrderTasks">getOrderTasks</a> method to retrieve order task IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/OrderTask`

## Example

```bash
curl -X GET \
  https://api.ebay.com/order_task/{task_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

order_task

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
