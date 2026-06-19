# createShippingFulfillment

When you group an order's line items into one or more packages, each package requires a corresponding plan for handling, addressing, and shipping; this is a <i>shipping fulfillment</i>. For each package, execute this call once to generate a shipping fulfillment associated with that package. <br><br> <span class="tablenote"><strong>Note:</strong> A single line item in an order can consist of multiple units of a purchased item, and one unit can consist of multiple parts or components. Although these components might be provided by the manufacturer in separate packaging, the seller must include all components of a given line item in the same package.</span> <br><br>Before using this call for a given package, you must determine which line items are in the package. If the package has been shipped, you should provide the date of shipment in the request. If not provided, it will default to the current date and time.

## Endpoint

```
POST /order/{orderId}/shipping_fulfillment
```

## API

Fulfillment API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **orderId** (required): This path parameter is used to specify the unique identifier of the order associated with the shipping fulfillment being created.<br><br> Use the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrders" target="_blank ">getOrders</a> method to retrieve order IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/ShippingFulfillmentDetails`


## Response

**201**: Created. The call also returns the following location response header: <br><br><code>{ENV}/sell/fulfillment/v1/order/{ORDERID}/shipping_fulfillment/{FULFILLMENTID}</code> <br><br>The <code>ENV</code> string is the HTTPS path to the same eBay supported environment in which this call was issued. The <code>ORDERID</code> parameter is the unique identifier of the order addressed by this call; for example, <code>01-03955-36441</code>. The <code>FULFILLMENTID</code> parameter identifies the newly created fulfillment; for example, <code>9405509699937003457459</code>. Use this Get Fulfillment URI to retrieve the contents of the new fulfillment.

Response includes JSON with relevant data.

## Example

```bash
curl -X POST \
  https://api.ebay.com/order/{orderId}/shipping_fulfillment \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipping_fulfillment

## Reference

- [eBay Fulfillment API Documentation](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
