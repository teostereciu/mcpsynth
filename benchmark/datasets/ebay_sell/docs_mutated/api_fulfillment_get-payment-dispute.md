# Get Payment Dispute Details

This method retrieves detailed information on a specific payment dispute. The payment dispute identifier is passed in as path parameter at the end of the call URI.<br><br>Below is a summary of the information that is retrieved:<ul><li>Current status of payment dispute</li><li>Amount of the payment dispute</li><li>Reason the payment dispute was opened</li><li>Order and line items associated with the payment dispute</li><li>Seller response options if an action is currently required on the payment dispute</li><li>Details on the results of the payment dispute if it has been closed</li><li>Details on any evidence that was provided by the seller to fight the payment dispute</li></ul>

## Endpoint

```
GET /payment_dispute/{payment_dispute_id}
```

## API

Fulfillment API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **payment_dispute_id** (required): This parameter is used to specify the unique identifier of the payment dispute being retrieved.<br><br> Use the <a href="/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDisputeSummaries" target="_blank ">getPaymentDisputeSummaries</a> method to retrieve payment dispute IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/PaymentDispute`

## Example

```bash
curl -X GET \
  https://api.ebay.com/payment_dispute/{payment_dispute_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payment_dispute

## Reference

- [eBay Fulfillment API Documentation](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
