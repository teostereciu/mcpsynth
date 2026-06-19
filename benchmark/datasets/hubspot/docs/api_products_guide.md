# CRM API | Products

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/products/guide*

---

Products

# CRM API | Products

In HubSpot, products represent the goods or services you sell. The products endpoints allow you to manage and sync this data.

Scope requirements

In HubSpot, products represent the goods or services you sell. Building a [product library](https://knowledge.hubspot.com/products/create-and-manage-products) allows you to quickly add products to deals, generate quotes, and report on product performance. The products endpoints allow you to manage this data and sync it between HubSpot and other systems. Products, along with companies, contacts, deals, tickets, line items, and quotes, are objects in the HubSpot CRM. Learn more about object properties, associations, relationships, and more in our [Understanding the CRM Objects](/docs/guides/crm/understanding-the-crm) guide. **Example use case:** so that sales reps can easily add goods and services to deals, quotes, and more, use the products API to import your product catalog into HubSpot.

##

​

Create a product

To create a product make a `POST` request to `crm/v3/objects/products`. In the request body, include a `properties` object containing any product properties that you’d like to set on create. You can later update a product’s properties through a `PATCH` request to the same endpoint. To see all available product properties, make a `GET` request to the [properties API](/docs/api-reference/legacy/crm/properties/guide). To retrieve product properties, the request URL will be `/crm/v3/properties/products`.


    {
      "properties": {
        "name": "Implementation Service",
        "price": "6000.00",
        "hs_sku": "123456",
        "description": "Onboarding service for data product",
        "hs_cost_of_goods_sold": "600.00",
        "hs_recurring_billing_period": "P12M"
      }
    }


Note that the value for `hs_recurring_billing_period` is formatted as `P#M`, where # is the number of months.

##

​

Associate products

Products themselves can’t be associated with other CRM objects. However, to associate a product’s information with a deal or a quote, you can create a [line item](/docs/api-reference/legacy/crm/objects/line-items/guide) based on that product. Line items are individual instances of products, and are a separate object from products so that you can tailor the goods and services on a deal or quote as needed without needing to update the product itself. For example, if you’re putting together a deal where one of your products is being sold, you’d first create a line item from the product, then associate it with the deal. You can either do this with two separate calls, or with one call that creates and associates the line item. Both options are shown below.

**Please note:** Line items belong to one single parent object. If associating objects, line items should be individual to each object. For example, if you’re creating a deal and a quote, you should create one set of line items for the deal, and another set for the quote. This will help streamline CRM data across objects and prevent unexpected data loss when needing to modify line items. For example, deleting a quote will also delete the quote’s line items. If those line items are also associated with a deal, the deal’s line items will also be deleted.

###

​

Create and associate a line item (multiple calls)

First, you’ll create a line item based on a product with the ID of `1234567`. For a full list of available line item properties, make a `GET` request to the [properties API](/docs/api-reference/legacy/crm/properties/guide). The URL for line items would be `crm/v3/properties/line_items`. Because you’re create the line item from an existing product, it will inherit property values from the product, such as price.


    {
      "properties": {
        "quantity": 1,
        "hs_object_id": "1234567", //the object ID of the product
        "name": "New line item (product-based)"
      }
    }


The response will return a line item ID which you can use to associate it with a deal using the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide). For this example, assume that the returned line item ID is `7791176460`. To associate the line item with an existing deal (ID: `14795354663`), you’ll make a `PUT` request to `/crm/v4/objects/line_items/7791176460/associations/default/deals/14795354663`. This request uses the default association type. A `200` response will return information similar to the following:


    {
      "status": "COMPLETE",
      "results": [
        {
          "from": {
            "id": "14795354663"
          },
          "to": {
            "id": "7791176460"
          },
          "associationSpec": {
            "associationCategory": "HUBSPOT_DEFINED",
            "associationTypeId": 19
          }
        },
        {
          "from": {
            "id": "7791176460"
          },
          "to": {
            "id": "14795354663"
          },
          "associationSpec": {
            "associationCategory": "HUBSPOT_DEFINED",
            "associationTypeId": 20
          }
        }
      ],
      "startedAt": "2023-12-21T20:06:52.083Z",
      "completedAt": "2023-12-21T20:06:52.192Z"
    }


In HubSpot, the deal record will display the line item in the _Line items_ card.

###

​

Create and associate a line item (single call)

To create a line item from an existing product and associate it with a deal using a single call, you can include an `associations` array in the line item create request. To create the line item, make a `POST` request to `crm/v3/objects/line_item`. Your request body will look similar to the following. Note that the `associationTypeId` for the line item-deal association is `20`. Learn more about [association types between different types of CRM records](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values).


    {
      "properties": {
        "quantity": 1,
        "hs_object_id": "1234567", //the object ID of the product
        "name": "New line item (product-based)"
      },
      "associations": [
        {
          "to": {
            "id": "14795354663"
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


A `200` response will return details about the new line item. In HubSpot, the deal record will display the line item in the _Line items_ card.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)