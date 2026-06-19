# createFromShippingQuote

This method creates a shipment based on the <b>shippingQuoteId</b> and <b>rateId</b> values supplied in the request. The rate identified by the <b>rateId</b> value specifies the carrier and service for the package shipment, and the rate ID must be contained in the shipping quote identified by the <b>shippingQuoteId</b> value. Call <b>createShippingQuote</b> to retrieve a set of live shipping rates.<br><br><span class="tablenote"><b>Note:</b> The Logistics API only supports USPS shipping rates and labels.</span><br/>When you create a shipment, eBay generates a shipping label that you can download and use to ship your package.<br/><br/>In a <b>createFromShippingQuote</b> request, sellers can include a list of shipping options they want to add to the base service quoted in the selected rate. The list of available shipping options is specific to each quoted rate and if available, the options are listed in the rate container of the shipping quote.<br/><br/>In addition to a configurable return-to location and other details about the shipment, the response to this method includes:<ul><li>The shipping carrier and service to be used for the package shipment</li><li>A list of selected shipping options, if any</li><li>The shipment tracking number</li><li>The total shipping cost (the sum cost of the base shipping service and any added options)</li></ul>When you create a shipment, your billing agreement account is charged the sum of the <b>baseShippingCost</b> and the total cost of any additional shipping options you might have selected. Use the URL returned in <b>labelDownloadURL</b> field, or call <b>downloadLabelFile</b> with the <b>shipmentId</b> value from the response, to download a shipping label for your package.<br/><br/><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Sellers must set up their payment method before they can use this method to create a shipment and the associated shipping label.</p></div><h3 id="ba">Set up a billing agreement</h3>Prior to using this method to create a shipment, sellers must first set up their billing agreement. Failure to do so will return <code>Error 90030 Payment could not be completed.</code><br/><br/>The preferred method for sellers to set up their billing agreement is to go to <a href="https://gslblui.ebay.com/gslblui/payments " target="_blank">Set up billing agreement</a> and follow the on-screen directions.<br/><br/>Alternatively, sellers can do the following:<ul><li>Go to https://www.ebay.com/ship/single/{order_id}, where {order_id} is that of the order for which the label is being printed.</li><li>When prompted, select <b>PayPal</b>.</li><li>Verify that <b>Save PayPal for future purchases</b> is selected.</li><li>Click <b>Set up Payments</b> which will open PayPal in a pop-up window.</li><li>Log in using <i>PayPal credentials</i>, and then follow the on-screen prompts to set up the billing agreement.</li><li>Once the agreement has been set up, sellers can leave this page as there is no need to actually print a label.</li></ul>

## Endpoint

```
POST /shipment/create_from_shipping_quote
```

## API

Logistics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)
- **X-EBAY-C-MARKETPLACE-ID** (required): This header parameter specifies the eBay marketplace for the shipment being created.<br><br>For a list of valid values, refer to the section <a href="/api-docs/static/rest-request-components.html#marketpl" target="_blank">Marketplace ID Values</a> in the <b>Using eBay RESTful APIs</b> guide. (Type: `string`)

### Request Body

See schema: `#/components/schemas/CreateShipmentFromQuoteRequest`


## Response

**201**: Created

Response schema: `#/components/schemas/Shipment`

## Example

```bash
curl -X POST \
  https://api.ebay.com/shipment/create_from_shipping_quote \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipment

## Reference

- [eBay Logistics API Documentation](https://developer.ebay.com/api-docs/sell/logistics/overview.html)
