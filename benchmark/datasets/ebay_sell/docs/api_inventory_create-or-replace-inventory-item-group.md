# createOrReplaceInventoryItemGroup

<span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reached, the seller will be blocked from revising the item until the next calendar day.</span><br>This call creates a new inventory item group or updates an existing inventory item group. It is up to sellers whether they want to create a complete inventory item group record right from the start, or sellers can provide only some information with the initial <strong>createOrReplaceInventoryItemGroup</strong> call, and then make one or more additional <strong>createOrReplaceInventoryItemGroup</strong> calls to complete the inventory item group record. Upon first creating an inventory item group record, the only required elements are  the <strong>inventoryItemGroupKey</strong> identifier in the call URI, and the members of the inventory item group specified through the <strong>variantSKUs</strong> array in the request payload.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#inventory_item_group " target="_blank">Inventory item group fields</a> for a list of fields required to publish an offer.</p></span></div><br><span class="tablenote"><b>Note:</b> In addition to the <code>authorization</code> header, which is required for all Inventory API calls, this call also requires the <code>Content-Type</code> and <code>Content-Language</code> headers. See the <a href="/api-docs/sell/inventory/resources/inventory_item_group/methods/createOrReplaceInventoryItemGroup#h3-request-headers">HTTP request headers</a> for more information.</span><br>In the case of updating/replacing an existing inventory item group, this call does a complete replacement of the existing inventory item group record, so all fields (including the member SKUs) that make up the inventory item group are required, regardless of whether their values changed. So, when replacing/updating an inventory item group record, it is advised that the seller run a <strong>getInventoryItemGroup</strong> call for that inventory item group to see all of its current values/settings/members before attempting to update the record. And if changes are made to an inventory item group that is part of a live, multiple-variation eBay listing, these changes automatically update the eBay listing. For example, if a SKU value is removed from the inventory item group, the corresponding product variation will be removed from the eBay listing as well.<br><br>In addition to the required inventory item group identifier and member SKUs, other key information that is set with this call include: <ul> <li>Title and description of the inventory item group. The string values provided in these fields will actually become the listing title and listing description of the listing once the first SKU of the inventory item group is published successfully</li> <li>Common aspects that inventory items in the group share</li> <li>Product aspects that vary within each product variation</li> <li>Links to images demonstrating the variations of the product, and these images should correspond to the product aspect that is set with the <strong>variesBy.aspectsImageVariesBy</strong> field</li> </ul><br><span class="tablenote"><b>Note:</b> For more information, see <a href="/api-docs/sell/static/inventory/inventory-item-groups.html" target="_blank">Creating and managing inventory item groups</a>.</span>

## Endpoint

```
PUT /inventory_item_group/{inventoryItemGroupKey}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **inventoryItemGroupKey** (required): This path parameter specifies the unique identifier of the inventory item group being created or updated. This identifier is defined by the seller.<br><br>This value cannot be changed once it is set.<br><br><b>Max Length:</b> 50 (Type: `string`)

## Headers

- **Content-Language** (required): This header sets the natural language that will be used in the field values of the request payload. For example, the value passed in this header should be <code>en-US</code> for English or <code>de-DE</code> for German.<br><br>For more information on the Content-Language header, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/InventoryItemGroup`


## Response

**200**: Success

Response schema: `#/components/schemas/BaseResponse`

**201**: Created

Response schema: `#/components/schemas/BaseResponse`

**204**: No Content

## Example

```bash
curl -X PUT \
  https://api.ebay.com/inventory_item_group/{inventoryItemGroupKey} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

inventory_item_group

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
