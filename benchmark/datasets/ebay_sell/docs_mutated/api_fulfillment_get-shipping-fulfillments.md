# getShippingFulfillments

Use this call to retrieve the contents of all fulfillments currently defined for a specified order based on the order's unique identifier, <b>orderId</b>. This value is returned in the <b>getOrders</b> call's <b>members.orderId</b> field when you search for orders by creation date or shipment status.

## Endpoint

```
GET /order/{orderId}/shipping_fulfillment
```

## API

Fulfillment API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **orderId** (required): This path parameter is used to specify the unique identifier of the order associated with the shipping fulfillments being retrieved.<br><br>Use the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrders" target="_blank ">getOrders</a> method to retrieve order IDs. Order ID values are also shown in My eBay/Seller Hub. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/ShippingFulfillmentPagedCollection`

## Example

```bash
curl -X GET \
  https://api.ebay.com/order/{orderId}/shipping_fulfillment \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipping_fulfillment

## Reference

- [eBay Fulfillment API Documentation](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
