# getOrder

Use this call to retrieve the contents of an order based on its unique identifier, <i>orderId</i>. This value was returned in the <b> getOrders</b> call's <b>orders.orderId</b> field when you searched for orders by creation date, modification date, or fulfillment status. Include the optional <b>fieldGroups</b> query parameter set to <code>TAX_BREAKDOWN</code> to return a breakdown of the taxes and fees. <br><br> The returned <b>Order</b> object contains information you can use to create and process fulfillments, including: <ul> <li>Information about the buyer and seller</li> <li>Information about the order's line items</li> <li> The plans for packaging, addressing and shipping the order</li> <li>The status of payment, packaging, addressing, and shipping the order</li> <li>A summary of monetary amounts specific to the order such as pricing, payments, and shipping costs</li> <li>A summary of applied taxes and fees, and optionally a breakdown of each </li></ul>

## Endpoint

```
GET /order/{orderId}
```

## API

Fulfillment API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **orderId** (required): This path parameter is used to specify the unique identifier of the order being retrieved.<br><br> Use the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrders" target="_blank ">getOrders</a> method to retrieve order IDs. Order ID values are also shown in My eBay/Seller Hub.<br><br><span class="tablenote"><strong>Note:</strong> <b>getOrders</b> can return orders up to two years old. Do not provide the <b>orderId</b> for an order created more than two years in the past.</span> (Type: `string`)

## Query Parameters

- **fieldGroups**: This parameter lets you control what is returned in the response.<br><br><span class="tablenote"><b>Note:</b> The only presently supported value is <code>TAX_BREAKDOWN</code>. This field group adds addition fields to the response that return a breakdown of taxes and fees.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Order`

## Example

```bash
curl -X GET \
  https://api.ebay.com/order/{orderId} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

order

## Reference

- [eBay Fulfillment API Documentation](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
