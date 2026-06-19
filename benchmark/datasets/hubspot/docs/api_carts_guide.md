# CRM API | Carts

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/carts/guide*

---

Carts

# CRM API | Carts

Create and manage ecommerce cart data.

Scope requirements

Use the carts API to create and manage data related to ecommerce purchases in HubSpot. This can be especially useful for keeping HubSpot data synced with external ecommerce platforms, such as Shopify and NetSuite. For example, use the API to sync cart data with Shopify, including associating the cart with an order and contact record.

##

​

Create carts

To create a cart, make a `POST` request to `crm/v3/objects/cart`. In the request body, you can include the `properties` and `associations` objects to set property values and associate the cart with other CRM objects (e.g., contacts and line items). Learn more about order properties and associations below.

###

​

Properties

Cart details are stored in cart properties. HubSpot provides a set of default cart properties, but you can also create your own custom properties using the [properties API](/docs/api-reference/legacy/crm/properties/guide). To include properties when creating a cart, add them as fields in a `properties` object in the request body.For example, the request body below would create a cart with some basic product details based on the information provided by the buyer at checkout.


    {
      "properties": {
        "hs_cart_name": "name-of-cart",
        "hs_external_cart_id": "1234567890",
        "hs_external_status": "pending",
        "hs_source_store": "name-of-store",
        "hs_total_price": "500",
        "hs_currency_code": "USD",
        "hs_cart_discount": "12",
        "hs_tax": "36.25",
        "hs_shipping_cost": "0",
        "hs_tags": "frames, lenses"
      }
    }


The response will include the information you provided during creation along with a few other default properties.


    {
      "id": "55262618747",
      "properties": {
        "hs_cart_discount": "12",
        "hs_cart_name": "name-of-cart",
        "hs_external_cart_id": "1234567890",
        "hs_created_by_user_id": "959199",
        "hs_createdate": "2024-04-11T20:42:01.734Z",
        "hs_currency_code": "USD",
        "hs_exchange_rate": "1.0",
        "hs_external_status": "pending",
        "hs_homecurrency_amount": "500.0",
        "hs_lastmodifieddate": "2024-04-11T20:42:01.734Z",
        "hs_object_id": "55262618747",
        "hs_object_source": "CRM_UI",
        "hs_object_source_id": "userId:959199",
        "hs_object_source_label": "CRM_UI",
        "hs_object_source_user_id": "959199",
        "hs_shipping_cost": "0",
        "hs_source_store": "name-of-store",
        "hs_tags": "frames, lenses",
        "hs_tax": "36.25",
        "hs_total_price": "500",
        "hs_updated_by_user_id": "959199"
      },
      "createdAt": "2024-04-11T20:42:01.734Z",
      "updatedAt": "2024-04-11T20:42:01.734Z",
      "archived": false
    }


###

​

Associations

You can associate carts with other HubSpot CRM objects at creation by including an `associations` object. You can also use the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide) to update existing carts after creation. In the `associations` array, include the following fields:

Fields| Type| Description
---|---|---
`toObjectId`| String| The ID of the record that you want to associate the cart with.
`associationTypeId`| String| A unique identifier to indicate the association type between the cart and the other object. Below are the CRM objects that you can associate orders with, along with their `associationTypeId`:

  * [Contacts](/docs/api-reference/legacy/crm/objects/contacts/guide): `586`
  * [Deals](/docs/api-reference/legacy/crm/objects/deals/guide): `1347`
  * [Discounts](/docs/api-reference/legacy/crm/objects/discounts/guide): `588`
  * [Line items](/docs/api-reference/legacy/crm/objects/line-items/guide): `590`
  * [Orders](/docs/api-reference/legacy/crm/objects/orders/guide): `592`
  * [Quotes](/docs/api-reference/legacy/crm/objects/quotes/guide): `732`
  * [Tasks](/docs/api-reference/legacy/crm/activities/tasks/guide): `728`
  * [Tickets](/docs/api-reference/legacy/crm/objects/tickets/guide): `594`

To see a list of all association types, check out the [associations API documentation](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values). Or, you can retrieve each value by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

For example, the `POST` request body below would create a cart that’s associated with a specific contact and two line items.


    {
      "associations": [
        {
          "to": {
            "id": 301
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 586
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
              "associationTypeId": 590
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
              "associationTypeId": 590
            }
          ]
        }
      ],
      "properties": {
        "hs_external_cart_id": "1234567890",
        "hs_external_status": "pending",
        "hs_source_store": "name-of-store",
        "hs_total_price": "500",
        "hs_currency_code": "USD",
        "hs_tax": "36.25",
        "hs_tags": "donuts, bagels"
      }
    }


##

​

Retrieve carts

Depending on the information you need, there are a few ways to retrieve carts:

  * To retrieve all carts, make a `GET` request to `/crm/v3/objects/cart`.
  * To retrieve a specific cart, make a `GET` request to the above URL and specify a cart ID. For example: `/crm/v3/objects/cart/44446244097`.
  * To retrieve carts that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. Learn more about [searching the CRM](/docs/api-reference/legacy/crm/search-the-crm#make-a-search-request).

The response will include a few default properties, including the create date, last modified date.


    {
      "id": "55226265370",
      "properties": {
        "hs_createdate": "2024-04-10T18:59:32.441Z",
        "hs_lastmodifieddate": "2024-04-10T18:59:32.441Z",
        "hs_object_id": "55226265370"
      },
      "createdAt": "2024-04-10T18:59:32.441Z",
      "updatedAt": "2024-04-10T18:59:32.441Z",
      "archived": false
    }


To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below: `/crm/v3/objects/cart?properties=hs_external_cart_id&hs_external_status`


    {
      "results": [
        {
          "id": "55226265370",
          "properties": {
            "hs_createdate": "2024-04-10T18:59:32.441Z",
            "hs_external_cart_id": "1234567890",
            "hs_lastmodifieddate": "2024-04-10T18:59:32.441Z",
            "hs_object_id": "55226265370"
          },
          "createdAt": "2024-04-10T18:59:32.441Z",
          "updatedAt": "2024-04-10T18:59:32.441Z",
          "archived": false
        },
        {
          "id": "55262618747",
          "properties": {
            "hs_createdate": "2024-04-11T20:42:01.734Z",
            "hs_external_cart_id": "8675309",
            "hs_lastmodifieddate": "2024-04-11T20:42:01.734Z",
            "hs_object_id": "55262618747"
          },
          "createdAt": "2024-04-11T20:42:01.734Z",
          "updatedAt": "2024-04-11T20:42:01.734Z",
          "archived": false
        }
      ]
    }


To view all available cart properties, use the [properties API](/docs/api-reference/legacy/crm/properties/guide) by making a `GET` request to `crm/v3/properties/cart`. Learn more about cart properties.

###

​

Search for carts by properties

You can use the search endpoint to retrieve carts that meet a specific set of [filter criteria](/docs/api-reference/legacy/crm/search-the-crm#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body. For example, to search for all carts placed at a specific store, you would make a `POST` request to `crm/v3/objects/cart/search` with the following request body:


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_source_store",
              "value": "Cat Cafe - Portland",
              "operator": "EQ"
            }
          ]
        }
      ],
      "properties": ["hs_external_cart_id", "hs_source_store"]
    }


###

​

Retrieve a cart with associations

To retrieve a cart and the contact associated with it, make a `GET` request to: `crm/v3/objects/cart/{cartId}/associations/contact` This will return the IDs of the currently associated contact, along with meta information about the association type.


    {
      "results": [
        {
          "id": "301",
          "type": "cart_to_contact"
        }
      ]
    }


You can then use the returned IDs to request more information about the contact through the [contacts API](/docs/api-reference/legacy/crm/objects/contacts/guide). Using the above example response, you would make a `GET` request to `crm/v3/objects/contacts/301`.


    {
      "id": "301",
      "properties": {
        "createdate": "2022-09-27T13:13:31.004Z",
        "email": "tom.bombadil@oldforest.com",
        "firstname": "Tom",
        "hs_object_id": "301",
        "lastmodifieddate": "2023-11-07T17:14:00.841Z",
        "lastname": "Bombadil"
      },
      "createdAt": "2022-09-27T13:13:31.004Z",
      "updatedAt": "2023-11-07T17:14:00.841Z",
      "archived": false
    }


Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

##

​

Update carts

To update a cart, make a `PATCH` request to `/crm/v3/objects/cart/{cartId}`. In the request body, include a `properties` object containing the properties that you want to update. For example, if you wanted to update a cart after it’s been fulfilled, you could send the following request body:


    {
      "properties": {
        "hs_external_status": "fulfilled"
      }
    }


The response will include a set of default properties along with the property that you just set.


    {
      "id": "55263075218",
      "properties": {
        "hs_created_by_user_id": "959199",
        "hs_createdate": "2024-04-11T20:52:47.212Z",
        "hs_external_status": "fulfilled",
        "hs_lastmodifieddate": "2024-04-11T20:56:00.234Z",
        "hs_object_id": "55263075218",
        "hs_updated_by_user_id": "959199"
      },
      "createdAt": "2024-04-11T20:52:47.212Z",
      "updatedAt": "2024-04-11T20:56:00.234Z",
      "archived": false
    }


To update the associations for an existing cart, make a `PUT` request to `/crm/v3/objects/cart/{cartId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. You can also use the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide).

See the associations section for `associationTypeId` values for cart-to-object associations. You can also make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.To see all a list of all values, check out the [associations API documentation](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values).

For example, to associate a cart with an existing order, you would make a `PUT` request to the following URL: `/crm/v3/objects/cart/{cartId}/associations/order/{orderId}/592` The response will return a set of default properties along with an `associations` object containing information about the association that you set.


    {
      "id": "55262618747",
      "properties": {
        "hs_createdate": "2024-04-11T20:42:01.734Z",
        "hs_lastmodifieddate": "2024-04-11T20:42:01.734Z",
        "hs_object_id": "55262618747"
      },
      "createdAt": "2024-04-11T20:42:01.734Z",
      "updatedAt": "2024-04-11T20:42:01.734Z",
      "archived": false,
      "associations": {
        "orders": {
          "results": [
            {
              "id": "54807577390",
              "type": "cart_to_order"
            }
          ]
        }
      }
    }


To remove an association from an existing cart, make a `DELETE` request to the following URL: `/crm/v3/objects/cart/{cartId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}` For example, if you wanted to remove an associated line item from a cart, your request URL would be the following: `/crm/v3/objects/cart/{cartId}/associations/line_items/{lineItemId}/590`

##

​

Cart properties

When managing your cart data, you may want to use some of the common properties in the table below. To get all cart properties, make a `GET` request to `/crm/v3/properties/cart`. Learn more about using the [properties API](/docs/api-reference/legacy/crm/properties/guide).

Property name| Label in UI| Description
---|---|---
`hs_cart_name`| Name| The name in an external system.
`hs_external_cart_id`| Cart ID| Unique identifier from an external system.
`hs_source_store`| Source Store| Data used to identify which store the cart came from.
`hs_external_status`| Status| The current status of the cart.
`hs_cart_url`| Cart Url| The recovery URL that’s sent to a customer so they can revive an abandoned cart.
`hs_total_price`| Total Price| The sum total amount associated with the cart.
`hs_currency_code`| Currency Code| The currency code used in the cart.
`hs_cart_discount`| Cart Discount| Amount of discount in the cart.
`hs_tags`| Tags| A collection of tag strings for the cart.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)