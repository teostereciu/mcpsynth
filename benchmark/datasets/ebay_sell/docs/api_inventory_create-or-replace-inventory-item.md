# createOrReplaceInventoryItem

<span class="tablenote"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls.</span><br><span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call creates a new inventory item record or replaces an existing inventory item record. It is up to sellers whether they want to create a complete inventory item record right from the start, or sellers can provide only some information with the initial <strong>createOrReplaceInventoryItem</strong> call, and then make one or more additional <strong>createOrReplaceInventoryItem</strong> calls to complete all required fields for the inventory item record and prepare it for publishing. Upon first creating an inventory item record, only the SKU value in the call path is required.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#inventory_item " target="_blank">Inventory item fields</a> for a list of fields required to publish an offer.</p></span></div><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/inventory_item/methods/createOrReplaceInventoryItem#h3-request-headers">HTTP request headers</a> for more information.</span><br> In the case of replacing an existing inventory item record, the <strong>createOrReplaceInventoryItem</strong> call will do a complete replacement of the existing inventory item record, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a <strong>getInventoryItem</strong> call to retrieve the full inventory item record and see all of its current values/settings before attempting to update the record. And if changes are made to an inventory item that is part of one or more active eBay listings, a successful call will automatically update these eBay listings. <br><br>The key information that is set with the <strong>createOrReplaceInventoryItem</strong> call include: <ul> <li>Seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value. This SKU value is passed in at the end of the call URI</li> <li>Condition of the item</li> <li>Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated.</li> <li>Quantity of the inventory item that is available for purchase</li> <li>Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge.</li> </ul> <p>In addition to the <code>authorization</code> header, which is required for all eBay REST API calls, the <strong>createOrReplaceInventoryItem</strong> call also requires the <code>Content-Language</code> header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be <code>en-US</code>. To view other supported <code>Content-Language</code> values, and to read more about all supported HTTP headers for eBay REST API calls, see the <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank">HTTP request headers</a> topic in the <strong>Using eBay RESTful APIs</strong> document.</p><p>For those who prefer to create or update numerous inventory item records with one call (up to 25 at a time), the <strong>bulkCreateOrReplaceInventoryItem</strong> method can be used.</p>

## Endpoint

```
PUT /inventory_item/{sku}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **sku** (required): This path parameter specifies the seller-defined SKU value for the inventory item being created or updated. SKU values must be unique across the seller's inventory. <br><br><strong>Max length</strong>: 50 (Type: `string`)

## Headers

- **Content-Language** (required): This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/InventoryItem`


## Response

**200**: Success

Response schema: `#/components/schemas/BaseResponse`

**201**: Created

Response schema: `#/components/schemas/BaseResponse`

**204**: No Content

## Example

```bash
curl -X PUT \
  https://api.ebay.com/inventory_item/{sku} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

inventory_item

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
