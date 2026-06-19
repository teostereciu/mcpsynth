# getCustomerServiceMetricTask

<p>Use this method to retrieve customer service metric task details for the specified task. The input is <strong>task_id</strong>.</p>

## Endpoint

```
GET /customer_service_metric_task/{task_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **task_id** (required): This path parameter is the unique identifier of the customer service metric task being retrieved.<br><br>Use the <a href="/api-docs/sell/feed/resources/customer_service_metric_task/methods/getCustomerServiceMetricTasks">getCustomerServiceMetricTasks</a> method to retrieve task IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/ServiceMetricsTask`

## Example

```bash
curl -X GET \
  https://api.ebay.com/customer_service_metric_task/{task_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

customer_service_metric_task

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
