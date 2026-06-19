# Issue Refund

<div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including <b>issueRefund</b>. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br> This method allows a seller to issue a full or partial refund to a buyer for an order. Full or partial refunds can be issued at the order level or line item level.<br><br>The refunds issued through this method are processed asynchronously, so the refund will not show as 'Refunded' right away. A seller will have to make a subsequent <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrder" target="_blank">getOrder</a> call to check the status of the refund.  The status of an order refund can be found in the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.paymentSummary.refunds.refundStatus" target="_blank">paymentSummary.refunds.refundStatus</a> field of the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrder" target="_blank">getOrder</a> response.

## Endpoint

```
POST /order/{order_id}/issue_refund
```

## API

Fulfillment API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **order_id** (required): This path parameter is used to specify the unique identifier of the order associated with a refund.<br><br>Use the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrders" target="_blank ">getOrders</a> method to retrieve order IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/IssueRefundRequest`


## Response

**200**: OK

Response schema: `#/components/schemas/Refund`

## Example

```bash
curl -X POST \
  https://api.ebay.com/order/{order_id}/issue_refund \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

order

## Reference

- [eBay Fulfillment API Documentation](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
