# Get Payment Dispute Evidence File

This call retrieves a specific evidence file for a payment dispute. The following three identifying parameters are needed in the call URI:<ul><li><strong>payment_dispute_id</strong>: the identifier of the payment dispute. The identifier of each payment dispute is returned in the <strong>getPaymentDisputeSummaries</strong> response.</li><li><strong>evidence_id</strong>: the identifier of the evidential file set. The identifier of an evidential file set for a payment dispute is returned under the <strong>evidence</strong> array in the <strong>getPaymentDispute</strong> response.</li><li><strong>file_id</strong>: the identifier of an evidential file. This file must belong to the evidential file set identified through the <strong>evidence_id</strong> query parameter. The identifier of each evidential file is returned under the <strong>evidence.files</strong> array in the <strong>getPaymentDispute</strong> response.</li></ul><p>An actual binary file is returned if the call is successful. An error will occur if any of three identifiers are invalid.</p>

## Endpoint

```
GET /payment_dispute/{payment_dispute_id}/fetch_evidence_content
```

## API

Fulfillment API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **payment_dispute_id** (required): This path parameter is used to specify the unique identifier of the payment dispute associated with the evidence file being retrieved.<br><br> Use the <a href="/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDisputeSummaries" target="_blank ">getPaymentDisputeSummaries</a> method to retrieve payment dispute IDs. (Type: `string`)

## Query Parameters

- **evidence_id** (required): This query parameter is used to specify the unique identifier of the evidential file set.<br><br>The identifier of an evidential file set for a payment dispute is returned under the <strong>evidence</strong> array in the <a href="/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDispute" target="_blank ">getPaymentDispute</a> response. (Type: `string`)
- **file_id** (required): This query parameter is used to specify the unique identifier of an evidential file. This file must belong to the evidential file set identified through the <strong>evidence_id</strong> query parameter.<br><br>The identifier of each evidential file is returned under the <strong>evidence.files</strong> array in the <a href="/api-docs/sell/fulfillment/resources/payment_dispute/methods/getPaymentDispute" target="_blank ">getPaymentDispute</a> response. (Type: `string`)

## Response

**200**: Success

## Example

```bash
curl -X GET \
  https://api.ebay.com/payment_dispute/{payment_dispute_id}/fetch_evidence_content \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payment_dispute

## Reference

- [eBay Fulfillment API Documentation](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
