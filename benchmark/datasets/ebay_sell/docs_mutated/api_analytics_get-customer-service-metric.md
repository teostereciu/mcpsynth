# getCustomerServiceMetric

Use this method to retrieve a seller's performance and rating for the customer service metric.  <br><br>Control the response from the <b>getCustomerServiceMetric</b> method using the following path and query parameters: <ul><li><b>customer_service_metric_type</b> controls the type of customer service transactions evaluated for the metric rating.</li> <li><b>evaluation_type</b> controls the period you want to review.</li> <li><b>evaluation_marketplace_id</b> specifies the target marketplace for the evaluation.</li></ul> Currently, metric data is returned for only peer benchmarking. For details on the workings of peer benchmarking, see <a href="https://www.ebay.com/help/policies/selling-policies/seller-performance-policy/service-metrics-policy?id=4769" title="eBay Help pages" target="_blank">Service metrics policy</a>.  <br><br>For details on using and understanding the response from this method, see <a href="/api-docs/sell/static/performance/customer-service-metric.html" title="Selling Integration Guide">Interpreting customer service metric ratings</a>.

## Endpoint

```
GET /customer_service_metric/{customer_service_metric_type}/{evaluation_type}
```

## API

Analytics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **customer_service_metric_type** (required): Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are:<br> <ul><li><code>ITEM_NOT_AS_DESCRIBED</code></li><li><code>ITEM_NOT_RECEIVED</code></li></ul> (Type: `string`)
- **evaluation_type** (required): Use this path parameter to specify the evaluation period to use for the performance metrics. See <a href="/api-docs/sell/analytics/types/api:EvaluationTypeEnum" target="_blank"> EvaluationTypeEnum</a> for more information on the supported values. (Type: `string`)

## Query Parameters

- **evaluation_marketplace_id** (required): Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data.  <br><br>For the list of supported marketplaces, see <a href="/api-docs/sell/analytics/static/overview.html#requirements" title="Analytics API Overview" target="_blank">Analytics API requirements and restrictions</a>. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/GetCustomerServiceMetricResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/customer_service_metric/{customer_service_metric_type}/{evaluation_type} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

customer_service_metric

## Reference

- [eBay Analytics API Documentation](https://developer.ebay.com/api-docs/sell/analytics/overview.html)
