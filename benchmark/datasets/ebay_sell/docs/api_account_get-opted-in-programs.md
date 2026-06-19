# getOptedInPrograms

This method gets a list of the seller programs that the seller has opted-in to.

## Endpoint

```
GET /program/get_opted_in_programs
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Response

**200**: Success

Response schema: `#/components/schemas/Programs`

## Example

```bash
curl -X GET \
  https://api.ebay.com/program/get_opted_in_programs \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

program

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
