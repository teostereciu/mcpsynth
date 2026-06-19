# createShippingQuote

The <b>createShippingQuote</b> method returns a <i>shipping quote </i> that contains a list of live "rates."  <br><br>Each rate represents an offer made by a shipping carrier for a specific service and each offer has a live quote for the base service cost. Rates have a time window in which they are "live," and rates expire when their purchase window ends. If offered by the carrier, rates can include shipping options (and their associated prices), and users can add any offered shipping option to the base service should they desire.  Also, depending on the services required, rates can also include pickup and delivery windows.<br><br><span class="tablenote"><b>Note:</b> The Logistics API only supports USPS shipping rates and labels.</span><br>Each rate is for a single package and is based on the following information: <ul><li>The shipping origin</li> <li>The shipping destination</li> <li>The package size (weight and dimensions)</li></ul>  Rates are identified by a unique eBay-assigned <b>rateId</b> and rates are based on price points, pickup and delivery time frames, and other user requirements. Because each rate offered must be compliant with the eBay shipping program, all rates reflect eBay-negotiated prices.  <br><br>The various rates returned in a shipping quote offer the user a choice from which they can choose a shipping service that best fits their needs. Select the rate for your shipment and using the associated <b>rateId</b>, call <b>createFromShippingQuote</b> to create a shipment and generate a shipping label that you can use to ship the package.

## Endpoint

```
POST /shipping_quote
```

## API

Logistics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header parameter specifies the eBay marketplace for the shipping quote that is being created.<br><br>For a list of valid values, refer to the section <a href="/api-docs/static/rest-request-components.html#marketpl" target="_blank">Marketplace ID Values</a> in the <b>Using eBay RESTful APIs</b> guide. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/ShippingQuoteRequest`


## Response

**201**: Created

Response schema: `#/components/schemas/ShippingQuote`

## Example

```bash
curl -X POST \
  https://api.ebay.com/shipping_quote \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipping_quote

## Reference

- [eBay Logistics API Documentation](https://developer.ebay.com/api-docs/sell/logistics/overview.html)
