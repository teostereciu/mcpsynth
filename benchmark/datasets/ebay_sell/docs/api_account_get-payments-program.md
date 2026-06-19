# getPaymentsProgram

<span class="tablenote"><b>Note:</b> This method is no longer applicable, as all seller accounts globally have been enabled for the new eBay payment and checkout flow.</span><br>This method returns whether or not the user is opted-in to the specified payments program. Sellers opt-in to payments programs by marketplace and you use the <b>marketplace_id</b> path parameter to specify the marketplace of the status flag you want returned.

## Endpoint

```
GET /payments_program/{marketplace_id}/{payments_program_type}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **marketplace_id** (required): This path parameter specifies the eBay marketplace of the payments program for which you want to retrieve the seller's status. (Type: `string`)
- **payments_program_type** (required): This path parameter specifies the payments program whose status is returned by the call. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/PaymentsProgramResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/payments_program/{marketplace_id}/{payments_program_type} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payments_program

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
