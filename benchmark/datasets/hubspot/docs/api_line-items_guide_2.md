# CRM API | Line items

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/line-items/guide*

---

Line Items

# CRM API | Line items

In HubSpot, line items represent individual instances of products on a deal, quote, or other object. The line items endpoints allow you to manage and sync this data.

Scope requirements

In HubSpot, line items are individual instances of [products](/docs/api-reference/latest/crm/objects/products/guide). When a product is attached to a deal or quote, it becomes a line item. You can also create standalone line items that aren’t based on an existing product. The line items endpoints allow you to manage this data and sync it between HubSpot and other systems. **Example use case:** when creating a set of [quotes](/docs/api-reference/latest/crm/objects/quotes/guide) for sales reps to send to potential buyers, you can use this API to create standalone line items per quote, as well as line items based on existing products.

##

​

Create a line item

To create a line item, make a `POST` request to `/crm/objects/2026-03/line_items`. In the request body, include the line item’s details, such as name, quantity, and price. You may also want to include additional data in the request body:

  * To create a line item based on an existing product (created through the [products API](/docs/api-reference/latest/crm/objects/products/guide) or [in HubSpot](https://knowledge.hubspot.com/products/create-and-manage-products)), include `hs_product_id` in the request body.
  * To include the tax rate for your line item, include its ID as the `hs_tax_rate_group_id` within the `properties` field of the request body.
  * You can also associate the line item with deals, quotes, invoices, payment links, or subscriptions by including an `associations` array in the request body. For example, the request body below would create a line item named “New standalone line item” that’s associated with a deal (ID: `12345`).


    {
      "properties": {
        "price": 10,
        "quantity": 1,
        "name": "New standalone line item",
        "hs_tax_rate_group_id": "2148420997"
      },
      "associations": [
        {
          "to": {
            "id": 12345
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 20
            }
          ]
        }
      ]
    }


**Please note:**

  * Line items belong to one single parent object. If associating objects, line items should be individual to each object. For example, if you’re creating a deal and a quote, you should create one set of line items for the deal, and another set for the quote. This will help streamline CRM data across objects and prevent unexpected data loss when needing to modify line items (e.g., deleting a quote will delete the quote’s line items, and if those line items are associated with a deal, the deal’s line items will also be deleted).
  * The `price` specified within the `properties` field cannot be negative.
  * The line items _Term_ property (`hs_recurring_billing_period`) accepts [ISO-8601 period formats](https://docs.oracle.com/javase/8/docs/api/java/time/Period.html) of PnYnMnD and PnW.


##

​

Tiered pricing

Line items support the same tiered pricing model as products. You can create a tiered pricing line item in two ways:

  * **Based on an existing product:** include `hs_product_id` in the request body. The tiered pricing properties are inherited from the product.
  * **Directly on the line item:** include `hs_pricing_model`, `hs_tier_ranges`, and `hs_tier_prices` in the `properties` object of the request body, using the same format as products.

Learn more about [tiered pricing properties and models](/docs/api-reference/latest/crm/objects/products/guide#tiered-pricing) in the products API guide, including single-currency and multi-currency examples.

**Please note:** do not set the `price` property when using tiered pricing properties on a line item. The line item price will be set based on the tiered pricing properties instead.

To retrieve all tiered pricing properties for a given line item, make a `GET` request to `/crm/objects/2026-03/line_item/{lineItemId}?properties=hs_pricing_model,hs_tier_ranges,hs_tier_prices` The response will include the tiered pricing properties:


    {
      "id": "53810745416",
      "properties": {
        "createdate": "2026-03-31T19:16:50.063Z",
        "hs_lastmodifieddate": "2026-03-31T19:16:51.187Z",
        "hs_object_id": "53810745416",
        "hs_pricing_model": "graduated",
        "hs_tier_prices": "[{\"index\":0,\"price\":100},{\"index\":1,\"price\":90},{\"index\":2,\"price\":80}]",
        "hs_tier_ranges": "[{\"start\":0,\"end\":99},{\"start\":100,\"end\":199},{\"start\":200}]"
      },
      "createdAt": "2026-03-31T19:16:50.063Z",
      "updatedAt": "2026-03-31T19:16:51.187Z",
      "archived": false
    }


##

​

Retrieve a line item

You can retrieve line items individually or in bulk.

  * To retrieve a specific line item, make a `GET` request to `/crm/objects/2026-03/line_items/{lineItemId}` where `lineItemId` is the ID of the line item.
  * To retrieve all line items, make a `GET` request to `/crm/objects/2026-03/line_items`.

In the request URL, you can include the following parameters:

Parameter| Description
---|---
`properties`| A comma-separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a line item doesn’t have a value, it will be returned as `null`.
`propertiesWithHistory`| A comma-separated list of the properties to be returned along with their history of previous values. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a line item doesn’t have a value, it will be returned as `null`.

##

​

Update a line item

To update a line item, make a `PATCH` request to `/crm/objects/2026-03/line_items/{lineItemId}`, where `lineItemId` is the ID of the line item. In the request body, include the property values that you want to update. You cannot update associations through this method. Instead, use the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide). For example, your request body might look similar to the following:


    {
      "properties": {
        "price": 25,
        "quantity": 3,
        "name": "Updated line item"
      }
    }


##

​

Delete a line item

To delete a line item, make a `DELETE` request to `/crm/objects/2026-03/line_items/{lineItemId}`, where `lineItemId` is the ID of the line item.

##

​

Line item properties

When managing your line item data, you may want to use some of the common properties in the table below. To get all line item properties, make a `GET` request to `crm/properties/2026-03/line_items`. Learn more about using the [properties API](/docs/api-reference/latest/crm/properties/guide).

Property name| Label in UI| Description
---|---|---
`name`| Name| The name of the line item.
`description`| Description| Full description of the product.
`hs_sku`| SKU| Unique product identifier.
`hs_recurring_billing_start_date`| Billing start date| Recurring billing start date for a line item.
`hs_recurring_billing_end_date`| Billing end date| Recurring billing end date for a line item.
`recurringbillingfrequency`| Billing frequency| How often a line item with recurring billing is billed. It informs the pricing calculation for deals and quotes. Line items with one-time billing aren’t included.
`quantity`| Quantity| How many units of a product are included in this line item.
`price`| Unit price| The cost of the product.
`amount`| Net price| The total cost of the line item (i.e., the quantity times the unit price).
`hs_line_item_currency_code`| Currency| Currency code for the line item.

##

​

Retrieve tax rates

You can apply a tax rate to individual line items (e.g., a MA Sales tax of 6.25%). Once you [configure your tax rate library](https://knowledge.hubspot.com/products/create-and-use-taxes#add-a-tax-rate-to-the-tax-library) in your HubSpot account, you can then make a `GET` request to `/tax-rates/v1/tax-rates` to fetch all tax rates, or `/tax-rates/v1/tax-rates/{taxRateId}` to fetch a tax rate by its ID. Your app will need to authorize the `tax_rates.read` scope to make this request. The resulting response will resemble the following:


    {
      "name": "MA Sales tax 2025",
      "percentageRate": 6.25,
      "label": "Sales Tax",
      "active": true,
      "id": "2148420997",
      "createdAt": "2024-12-12T23:20:39.923Z",
      "updatedAt": "2024-12-12T23:20:39.923Z"
    }


Each tax rate object will include the following properties:

Property name| Description
---|---
`name`| The internal descriptor for the tax rate.
`percentageRate`| The value of the tax rate, expressed as a percentage.
`label`| The buyer-facing descriptor of the tax rate, shown on the quote, invoice, or other parent objects.
`active`| A boolean that denotes whether the tax rate can be applied to a new quote or invoice. You might set this to `false` for a previous year’s tax rate that’s no longer applicable.
`id`| The ID of the tax rate.
`createdAt`| An ISO 8601 timestamp denoting when the tax rate was created.
`updatedAt`| An ISO 8601 timestamp denoting when the tax rate was last updated.

Once you have the ID of the tax rate you want to apply, provide that `id` for the `hs_tax_rate_group_id` within the `properties` field when creating a line item. Learn more about creating line items in the section above.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)