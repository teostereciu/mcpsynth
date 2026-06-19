# CRM API | Orders

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/orders/guide*

---

Orders

# CRM API | Orders

Create and manage ecommerce order data.

Scope requirements

Use the orders API to create and manage data related to ecommerce purchases in HubSpot. This can be especially useful for keeping HubSpot data synced with external ecommerce platforms, such as Shopify and NetSuite. For example, when a buyer adds a set of products to their cart and makes a purchase, store that purchase as an individual order. You can then update that order with tracking information once the shipping label has been printed. Because this information is stored in a property, you can reference it in emails that you send to notify customers that their package is on the way.

##

​

Create orders

To create an order, make a `POST` request to `crm/v3/objects/order`. In the request body, you can include the `properties` and `associations` objects to set property values and associate the order with other CRM objects (e.g., contacts and line items). Learn more about order properties and associations below.

###

​

Properties

Order details are stored in order properties. HubSpot provides a set of default order properties, but you can also create your own custom properties using the [properties API](/docs/api-reference/legacy/crm/properties/guide). To include properties when creating an order, add them as fields in a `properties` object in the request body. For example, the request body below would create an order with some basic order and shipping details based on the information provided by the buyer at checkout.


    {
      "properties": {
        "hs_order_name": "Camping supplies",
        "hs_currency_code": "USD",
        "hs_source_store": "REI - Portland",
        "hs_fulfillment_status": "Packing",
        "hs_shipping_address_city": "Portland",
        "hs_shipping_address_state": "Maine",
        "hs_shipping_address_street": "123 Fake Street"
      }
    }


The response will include the information you provided during creation along with a few other default properties.


    {
      "id": "54805205097",
      "properties": {
        "hs_created_by_user_id": "959199",
        "hs_createdate": "2024-03-27T18:04:11.823Z",
        "hs_currency_code": "USD",
        "hs_exchange_rate": "1.0",
        "hs_fulfillment_status": "Packing",
        "hs_lastmodifieddate": "2024-03-27T18:04:11.823Z",
        "hs_object_id": "54805205097",
        "hs_object_source": "CRM_UI",
        "hs_object_source_id": "userId:959199",
        "hs_object_source_label": "CRM_UI",
        "hs_object_source_user_id": "959199",
        "hs_order_name": "Camping supplies",
        "hs_shipping_address_city": "Portland",
        "hs_shipping_address_state": "Maine",
        "hs_shipping_address_street": "123 Fake Street",
        "hs_source_store": "REI - Portland",
        "hs_updated_by_user_id": "959199"
      },
      "createdAt": "2024-03-27T18:04:11.823Z",
      "updatedAt": "2024-03-27T18:04:11.823Z",
      "archived": false
    }


###

​

Associations

You can associate the order with other HubSpot CRM objects at creation by including an `associations` array. You can also use the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide) to update existing orders after creation. In the `associations` array, include an object for each associated record using the following fields:

Fields| Type| Description
---|---|---
`toObjectId`| String| The ID of the record that you want to associate the order with.
`associationTypeId`| String| A unique identifier to indicate the association type between the order and the other object. Below are the CRM objects that you can associate orders with, along with their `associationTypeId`:

  * [Carts](/docs/api-reference/legacy/crm/objects/carts/guide): `593`
  * [Contacts](/docs/api-reference/legacy/crm/objects/contacts/guide): `507`
  * [Companies](/docs/api-reference/legacy/crm/objects/companies/guide): `509`
  * [Deals](/docs/api-reference/legacy/crm/objects/deals/guide): `512`
  * [Discounts](/docs/api-reference/legacy/crm/objects/discounts/guide): `519`
  * [Discount codes](https://knowledge.hubspot.com/payments/create-and-use-discount-codes): `521`
  * [Invoices](/docs/api-reference/legacy/crm/objects/invoices/guide): `518`
  * [Line items](/docs/api-reference/legacy/crm/objects/line-items/guide): `513`
  * [Payments](/docs/api-reference/legacy/crm/objects/commerce-payments/guide): `523`
  * [Quotes](/docs/api-reference/legacy/crm/objects/quotes/guide): `730`
  * [Subscriptions](/docs/api-reference/legacy/crm/objects/commerce-subscriptions/guide): `516`
  * [Tasks](/docs/api-reference/legacy/crm/activities/tasks/guide): `726`
  * [Tickets](/docs/api-reference/legacy/crm/objects/tickets/guide): `525`

To see a list of all association types, check out the [associations API documentation](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values). Or, you can retrieve each value by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

For example, the `POST` request body below would create an order that’s associated with a specific contact and two line items. Properties are also included below the associations for setting initial order information.


    {
      "associations": [
        {
          "to": {
            "id": 301
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 507
            }
          ]
        },
        {
          "to": {
            "id": 1243313490
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 513
            }
          ]
        },
        {
          "to": {
            "id": 1243557166
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 513
            }
          ]
        }
      ],
      "properties": {
        "hs_order_name": "Associated order",
        "hs_currency_code": "USD",
        "hs_source_store": "REI - Portland",
        "hs_fulfillment_status": "Packing",
        "hs_shipping_address_city": "Portland",
        "hs_shipping_address_state": "Maine",
        "hs_shipping_address_street": "123 Fake Street"
      }
    }


##

​

Retrieve orders

Depending on the information you need, there are a few ways to retrieve orders:

  * To retrieve all orders, make a `GET` request to `/crm/v3/objects/order`.
  * To retrieve a specific order, make a `GET` request to the above URL and specify an order ID. For example: `/crm/v3/objects/order/44446244097`.
  * To retrieve orders that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. Learn more about [searching the CRM](/docs/api-reference/legacy/crm/search-the-crm#make-a-search-request).

The response will include a few default properties, including the create date, last modified date.


    {
      "results": [
        {
          "id": "54767113310",
          "properties": {
            "hs_createdate": "2024-03-26T20:02:34.935Z",
            "hs_lastmodifieddate": "2024-03-26T20:02:48.278Z",
            "hs_object_id": "54767113310"
          },
          "createdAt": "2024-03-26T20:02:34.935Z",
          "updatedAt": "2024-03-26T20:02:48.278Z",
          "archived": false
        },
        {
          "id": "54804869149",
          "properties": {
            "hs_createdate": "2024-03-27T17:39:16.122Z",
            "hs_lastmodifieddate": "2024-03-27T17:39:16.122Z",
            "hs_object_id": "54804869149"
          },
          "createdAt": "2024-03-27T17:39:16.122Z",
          "updatedAt": "2024-03-27T17:39:16.122Z",
          "archived": false
        }
      ]
    }


To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below: `/crm/v3/objects/order?properties=hs_order_name,hs_source_store`


    {
      "id": "54767113310",
      "properties": {
        "hs_createdate": "2024-03-26T20:02:34.935Z",
        "hs_lastmodifieddate": "2024-03-27T18:50:07.678Z",
        "hs_object_id": "54767113310",
        "hs_order_name": "Test API order 2",
        "hs_source_store": "REI - Portland"
      },
      "createdAt": "2024-03-26T20:02:34.935Z",
      "updatedAt": "2024-03-27T18:50:07.678Z",
      "archived": false
    }


To view all available order properties, you can query the [properties API](/docs/api-reference/legacy/crm/properties/guide) by making a `GET` request to `crm/v3/properties/order`. Learn more about order properties.

###

​

Search for orders by properties

You can use the search endpoint to retrieve orders that meet a specific set of [filter criteria](/docs/api-reference/legacy/crm/search-the-crm#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body. For example, to search for all orders placed at a specific store, you would make a `POST` request to `crm/v3/objects/order/search` with the following request body:


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_source_store",
              "value": "REI - Portland",
              "operator": "EQ"
            }
          ]
        }
      ],
      "properties": ["hs_order_name", "hs_source_store"]
    }


###

​

Retrieve an order with associations

To retrieve an order along with its associations, make a `GET` request to `crm/v3/objects/order/{orderId}/associations/{objectName}` For example, to retrieve an order and its associated contacts, you would use the following URL: `crm/v3/objects/order/{orderId}/associations/contact` This will return the IDs of the currently associated contacts, along with meta information about the association type.


    {
      "results": [
        {
          "id": "301",
          "type": "order_to_contact"
        },
        {
          "id": "1196316844",
          "type": "order_to_contact"
        }
      ]
    }


You could then use the returned IDs to request more information about the contacts through the [contacts API](/docs/api-reference/legacy/crm/objects/contacts/guide). For example, you could retrieve the contact using its ID by making a `GET` request to `crm/v3/objects/contacts/{contactId}`.


    {
      "id": "301",
      "properties": {
        "createdate": "2022-09-27T13:13:31.004Z",
        "email": "tom.bombadil@oldforest.com",
        "firstname": "Tom",
        "hs_object_id": "301",
        "lastmodifieddate": "2023-11- 07T17:14:00.841Z",
        "lastname": "Bombadil"
      },
      "createdAt": "2022-09-27T13:13:31.004Z",
      "updatedAt": "2023-11-07T17:14:00.841Z",
      "archived": false
    }


Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

##

​

Update orders

To update an order, make a `PATCH` request to `/crm/v3/objects/order/{orderId}`. In the request body, include a `properties` object containing the properties that you want to update. For example, if you wanted to update an order with the shipping tracking number, you could send the following request body:


    {
      "properties": {
        "hs_shipping_tracking_number": "123098521091"
      }
    }


The response will include a set of default properties along with the property that you just set.


    {
      "id": "54767113310",
      "properties": {
        "hs_created_by_user_id": "959199",
        "hs_createdate": "2024-03-26T20:02:34.935Z",
        "hs_lastmodifieddate": "2024-03-27T20:03:05.890Z",
        "hs_object_id": "54767113310",
        "hs_shipping_tracking_number": "123098521091",
        "hs_updated_by_user_id": "959199"
      },
      "createdAt": "2024-03-26T20:02:34.935Z",
      "updatedAt": "2024-03-27T20:03:05.890Z",
      "archived": false
    }


To update the associations for an existing order, make a `PUT` request to `/crm/v3/objects/order/{orderId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. You can also use the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide).

See the associations section for `associationTypeId` values for order-to-object associations. You can also make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.To see all a list of all values, check out the [associations API documentation](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values).

For example, to associate an existing order with an existing payment, you would make a `PUT` request to the following URL: `/crm/v3/objects/order/{orderId}/associations/commerce_payments/{paymentId}/523` The response will return a set of default properties along with an `associations` object containing information about the association that you set.


    {
      "id": "54767113310",
      "properties": {
        "hs_createdate": "2024-03-26T20:02:34.935Z",
        "hs_lastmodifieddate": "2024-03-27T20:03:05.890Z",
        "hs_object_id": "54767113310"
      },
      "createdAt": "2024-03-26T20:02:34.935Z",
      "updatedAt": "2024-03-27T20:03:05.890Z",
      "archived": false,
      "associations": {
        "payments": {
          "results": [
            {
              "id": "50927296322",
              "type": "order_to_commerce_payment"
            }
          ]
        }
      }
    }


To remove an association from an existing order, make a `DELETE` request to the following URL: `/crm/v3/objects/order/{orderId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}` For example, if you wanted to remove an associated payment from an order, your request URL would be the following: `/crm/v3/objects/order/{orderId}/associations/commerce_payments/{paymentId}/523`

##

​

Order properties

When managing your order data, you may want to use some of the common properties in the table below. To get all order properties, make a `GET` request to `/crm/v3/properties/order`. Learn more about using the [properties API](/docs/api-reference/legacy/crm/properties/guide).

Property name| Label in UI| Description
---|---|---
`hs_order_name`| Name| The name of the order.
`hs_currency_code`| Currency Code| The currency that the order was placed in.
`hs_source_store`| Source Store| The store that the order came from.
`hs_fulfillment_status`| Fulfillment Status| The current fulfillment / shipping status of the order.
`hs_shipping_status_url`| Shipping Status URL| A URL for tracking the shipment status.
`hs_shipping_tracking_number`| Shipping Tracking Number| The tracking number for shipping.
`hs_shipping_address_street`| Shipping Street| The street address for shipping.
`hs_shipping_address_city`| Shipping City| The city in the shipping address.
`hs_shipping_address_postal_code`| Shipping ZIP/Postal Code| The zip code of the shipping address.
`hs_pipeline`| Pipeline| The pipeline that the order is in. Pipelines contain stages for tracking the order’s progress. Learn more about pipelines and stages below.
`hs_pipeline_stage`| Stage| The order’s progress within its current pipeline. Learn more about pipelines and stages below.

###

​

Pipelines and stages

To track an order’s progress, you can create pipelines with defined stages for each step of the fulfillment process. For example, you could create a pipeline for online orders with stages for when the order has been opened, paid, processed, shipped, cancelled, and refunded. Using the [pipelines API](/docs/api-reference/legacy/crm/pipelines/guide), you can create an order pipeline by making a `POST` request to `crm/v3/pipelines/order`. In the request body, you’ll include a `label` for the pipeline, `displayOrder` for the display in HubSpot, and a `stages` array with objects for each stage.


    {
      "label": "Online orders",
      "displayOrder": 0,
      "stages": [
        {
          "label": "Open",
          "displayOrder": 0,
          "metadata": {
            "state": "OPEN"
          }
        },
        {
          "label": "Paid",
          "displayOrder": 1,
          "metadata": {
            "state": "OPEN"
          }
        },
        {
          "label": "Processed",
          "displayOrder": 2,
          "metadata": {
            "state": "OPEN"
          }
        },
        {
          "label": "Shipped",
          "displayOrder": 3,
          "metadata": {
            "state": "CLOSED"
          }
        },
        {
          "label": "Cancelled",
          "displayOrder": 4,
          "metadata": {
            "state": "CLOSED"
          }
        },
        {
          "label": "Refunded",
          "displayOrder": 5,
          "metadata": {
            "state": "CLOSED"
          }
        }
      ]
    }


Parameter| Type| Description
---|---|---
`label`| String| The pipeline’s label as it should appear in HubSpot.
`displayOrder`| Number| The order for displaying the pipeline in HubSpot. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label.
`stages`| Array| An array containing the pipeline stages. Each stage is an object containing the following fields:

  * `label`: the stage’s label as it should appear in HubSpot.
  * `displayOrder`: the order in which the stage will appear in HubSpot.
  * `metadata`: configures whether the stage is in progress (`OPEN`) or complete (`CLOSED`) using the `state` field.


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)