# getPaymentsProgramOnboarding

<span class="tablenote"><b>Note:</b> This method is no longer applicable, as all seller accounts globally have been enabled for the new eBay payment and checkout flow.</span><br>This method retrieves a seller's onboarding status for a payments program for a specified marketplace. The overall onboarding status of the seller and the status of each onboarding step is returned.

## Endpoint

```
GET /payments_program/{marketplace_id}/{payments_program_type}/onboarding
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **marketplace_id** (required): The eBay marketplace ID associated with the onboarding status to retrieve. (Type: `string`)
- **payments_program_type** (required): The type of payments program whose status is returned by the method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/PaymentsProgramOnboardingResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/payments_program/{marketplace_id}/{payments_program_type}/onboarding \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

onboarding

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
