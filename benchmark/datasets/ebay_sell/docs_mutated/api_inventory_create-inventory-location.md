# createInventoryLocation

<p>Use this call to create a new inventory location. In order to create and publish an offer (and create an eBay listing), a seller must have at least one location, as every offer must be associated with at least one location.</p><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span>Publish offer note: Fields may be optional or conditionally required when calling this method, but become required when publishing the offer to create an active listing. For this method, see <a href="/api-docs/sell/static/inventory/publishing-offers.html#location " target="_blank">Location fields</a> for a list of fields required to publish an offer.</p></span></div><p>Upon first creating an inventory location, only a seller-defined location identifier and a physical location is required, and once set, these values can not be changed. The unique identifier value (<i>merchantLocationKey</i>) is passed in at the end of the call URI. This <i>merchantLocationKey</i> value will be used in other Inventory Location calls to identify the location to perform an action against.</p><p>When creating an inventory location, the <b>locationTypes</b> can be specified to define the function of a location. At this time, the following <b>locationTypes</b> are supported:<ul><li><b>Fulfillment center</b> locations are used by sellers selling products through the Multi-warehouse program to get improved estimated delivery dates on their listings. A full address is required when creating a fulfillment center location, as well as the <b>fulfillmentCenterSpecifications</b> of the location. For more information on using the fulfillment center location type to get improved delivery dates, see <a href="/api-docs/sell/static/inventory/multi-warehouse-program.html" target="_blank ">Multi-warehouse program</a>.</li><li><b>Warehouse</b> locations are used for traditional shipping. A full street address is not needed, but the <b>postalCode</b> and <b>country</b> OR <b>city</b>, <b>stateOrProvince</b>, and <b>country</b> of the location must be provided.</li><li><b>Store</b> locations are generally used by merchants selling product through the In-Store Pickup program. A full address is required when creating a store location.</li></ul></p><p>Note that all inventory locations are "enabled" by default when they are created, and you must specifically disable them (by passing in a value of <code>DISABLED</code> in the <strong>merchantLocationStatus</strong> field) if you want them to be set to the disabled state. The seller's inventory cannot be loaded to inventory locations in the disabled state.</p><p>Unless one or more errors and/or warnings occur with the call, there is no response payload for this call. A successful call will return an HTTP status value of <i>204 No Content</i>.</p>

## Endpoint

```
POST /location/{merchantLocationKey}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **merchantLocationKey** (required): This path parameter specifies the unique, seller-defined key (ID) for an inventory location.<br><br><b>Max length</b>: 36 (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/InventoryLocationFull`


## Response

**204**: No Content

## Example

```bash
curl -X POST \
  https://api.ebay.com/location/{merchantLocationKey} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

location

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
