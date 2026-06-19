# getPrivileges

This method retrieves the seller's current set of privileges, including whether or not the seller's eBay registration has been completed, as well as the details of their site-wide <b>sellingLimit</b> (the amount and quantity they can sell on a given day).

## Endpoint

```
GET /privilege
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Response

**200**: Success

Response schema: `#/components/schemas/SellingPrivileges`

## Example

```bash
curl -X GET \
  https://api.ebay.com/privilege \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

privilege

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
