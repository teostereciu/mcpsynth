# updateItemPriceMarkdownPromotion

<span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay help pages. Sell Marketing API documentation has been updated to reflect this product name change, but note that no API interface changes have been made.</span><br>This method updates the specified item price markdown discount with the new configuration that you supply in the payload of the request. Specify the discount you want to update using the <b>promotion_id</b> path parameter. Call <a href="/api-docs/sell/marketing/resources/promotion/methods/getPromotions">getPromotions</a> to retrieve the IDs of a seller's discounts.<br><br>When updating a discount, supply all the fields that you used to configure the original discount (and not just the fields you are updating). eBay replaces the specified discount with the values you supply in the update request and if you don't pass a field that currently has a value, the update request fails.  <br><br>The parameters you are allowed to update with this request depend on the status of the discount you're updating:  <ul><li>DRAFT or SCHEDULED discounts: You can update any of the parameters in these discounts that have not yet started to run, including the <b>discountRules</b>.</li> <li>RUNNING discounts: You can change the <b>endDate</b> and the item's inventory but you cannot change the discount or the start date.</li> <li>ENDED discounts: Nothing can be changed.</li></ul>

## Endpoint

```
PUT /item_price_markdown/{promotion_id}
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **promotion_id** (required): This path parameter takes a concatenation of the ID of the discount you want to update plus the marketplace ID on which the discount is hosted. Concatenate the two values by separating them with an "at sign" (<b>@</b>). <br><br>The ID of the discount (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the discount is created. The Marketplace ID is the ENUM value of eBay marketplace where the discount is hosted.<br><br> Use the <a href="/api-docs/sell/marketing/resources/promotion/methods/getPromotions">getPromotions</a> method to retrieve promotion Ids. See <a href="/api-docs/sell/marketing/types/ba:MarketplaceIdEnum">MarketplaceIdEnum</a> for supported Marketplace ID values.<br><br><b>Example:</b> <code>1********5@EBAY_US</code> (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/ItemPriceMarkdown`


## Response

**200**: Success

Response includes JSON with relevant data.

**204**: Success

## Example

```bash
curl -X PUT \
  https://api.ebay.com/item_price_markdown/{promotion_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

item_price_markdown

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
