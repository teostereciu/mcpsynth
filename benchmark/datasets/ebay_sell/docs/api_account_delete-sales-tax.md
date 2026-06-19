# deleteSalesTax

This call deletes a sales-tax table entry for a jurisdiction. Specify the jurisdiction to delete using the <b>countryCode</b> and <b>jurisdictionId</b> path parameters.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span>

## Endpoint

```
DELETE /sales_tax/{countryCode}/{jurisdictionId}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **countryCode** (required): This path parameter specifies the two-letter <a href="https://www.iso.org/iso-3166-country-codes.html " title="https://www.iso.org " target="_blank">ISO 3166</a> code for the country whose sales tax table entry you want to delete.<br><br><span class="tablenote"><b>Note:</b> Sales-tax tables are available only for the US and Canada marketplaces. Therefore, the only supported values are:<ul><li><code>US</code></li><li><code>CA</code></li></ul></span> (Type: `string`)
- **jurisdictionId** (required): This path parameter specifies the ID of the sales tax jurisdiction whose table entry you want to delete.<br><br>Valid jurisdiction IDs can be retrieved using the <a href="/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions" target="_blank ">getSalesTaxJurisdiction</a> method of the Metadata API.<br><br><span class="tablenote"><b>Note:</b> When <code>countryCode</code> is set to <code>US</code>, the only supported values for <code>jurisdictionId</code> are:<ul><li><code>AS</code> (American Samoa)</li><li><code>GU</code> (Guam)</li><li><code>MP</code> (Northern Mariana Islands)</li><li><code>PW</code> (Palau)</li><li><code>VI</code> (US Virgin Islands)</li></ul></span> (Type: `string`)

## Response

**204**: Success

## Example

```bash
curl -X DELETE \
  https://api.ebay.com/sales_tax/{countryCode}/{jurisdictionId} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

sales_tax

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
