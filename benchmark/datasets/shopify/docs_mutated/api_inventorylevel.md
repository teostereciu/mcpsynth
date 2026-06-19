# InventoryLevel

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/inventorylevel*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# InventoryLevel

Ask assistant

Requires `inventory` access scope.

**Requires `inventory` access scope.:**

An inventory level represents the quantities of an inventory item for a location.

Each inventory level belongs to one inventory item and has one location. For every location where an inventory item can be stocked, there's an inventory level that represents the inventory item's quantities relating to that location.

Before you begin updating inventory, it's helpful to understand the relationships between the inventory resources:

  * **[Product Variant](/api/admin-rest/latest/resources/product-variant)** : Contains merchandising information, such as price, description, and images. Think of this as the product information that you might want a customer to see.

All product variants have a 1:1 relationship with their associated inventory item. Each product variant has one inventory item, and that inventory item belongs only to that product variant.

  * **[InventoryItem](/api/admin-rest/latest/resources/inventoryitem)** : Contains information about the physical product, such as its SKU. Think of this as the back-end information used for managing inventory, shipping, and fulfillments.

Inventory items are associated with one or many inventory levels. An inventory item will have an inventory level for each location where the item is stocked.

  * **[InventoryLevel](/api/admin-rest/latest/resources/inventorylevel)** : Represents the actual quantity of an item that is available.

Inventory levels connect one inventory item to one location. Each inventory level holds the available quantity for its inventory item at the associated location.

  * **[Location](/api/admin-rest/latest/resources/location)** : Represents a geographical location where a merchant does business, such as a retail store or warehouse.

Locations can have many inventory levels. Each location has one inventory level for each inventory item that the location stocks.


## How an order affects inventory

When a product variant that Shopify tracks is included in an order, Shopify decrements the inventory for that variant. Shopify doesn't know which location the item will be fulfilled from, so Shopify decrements the inventory level at the location that has the lowest ID.

Note

Orders placed through Shopify POS are associated with the location where the sale was made. For those orders, inventory is decremented at that location.

**Note:** Orders placed through Shopify POS are associated with the location where the sale was made. For those orders, inventory is decremented at that location.

When an order is fulfilled, the fulfillment includes the ID of the location where the fulfillment is taking place. Shopify checks whether the fulfillment location matches the original location where stock was decremented, and then adjusts the inventory if necessary:

  * If the fulfillment location matches the original location, then no action is needed.
  * If the fulfillment location doesn't match the original location, then Shopify decrements the inventory level at the fulfillment location and increments the inventory level at the original location.


### Example: Inventory adjustments for a simple order

An online store uses two warehouses to stock product inventory: one in Los Angeles (ID: `6884556842`), and one in New York (ID: `13968834616`). One of the store's products is a hat that's stocked at both locations with the following inventory levels:

  * Los Angeles: 8
  * New York: 6


A customer places an order for a hat. The Los Angeles location has the lowest ID, so Shopify decrements the item's inventory level at that location:

  * Los Angeles: 7
  * New York: 6


The order is actually fulfilled from the New York location. When the fulfillment is created, it includes the ID for the New York location. Shopify compares the fulfillment location ID to the original location and finds that they're different. Shopify then increments the inventory level at the Los Angeles location, and decrements the inventory level at the New York location:

  * Los Angeles: 8
  * New York: 5


## Inventory levels and fulfillment service locations

A fulfillment service [location](/api/admin-rest/latest/resources/location) has a 1:1 relationship with a third-party fulfillment service. When an app [creates a new fulfillment service](/api/admin-rest/latest/resources/fulfillmentservice) on a store, Shopify automatically creates a location that's associated with that fulfillment service. The FulfillmentService resource has a `location_id` property, which identifies the associated location.

An inventory item connected to a fulfillment service location can't be connected to any other locations at the same time:

### Connecting an inventory item to a fulfillment service location

When you work with items that have been or will be connected a fulfillment location, you should include `"relocate_if_necessary": true` in the body of the request. There are two situations where you might do this:

  * connecting an inventory item to a fulfillment service location and disconnecting it from all standard locations
  * connecting an inventory item to one or more standard locations and disconnecting it from a fulfillment service location


If `relocate_if_necessary` is `true`, then all inventory for the item is relocated to the new location and disconnected from any other locations. If a fulfillment service location is involved but `relocate_if_necessary` is `false`, then the connection will fail. If no fulfillment service is involved, then the property is ignored and no inventory is relocated.

### Setting the inventory level at a fulfillment service location

When you set inventory for a location, the inventory item is connected to the location if they are not already connected. If the item has been or will be connected to a fulfillment service location, then you should include `"disconnect_if_necessary": true` in the body of the request. There are two situations where you might do this:

  * setting inventory for an inventory item at a fulfillment service location when the item is already connected to one or more standard locations
  * setting inventory for an inventory item at a standard location when the item is already connected to a fulfillment service location


The inventory at the new location is set to the value of the `available` property. The inventory for other locations is set to 0 and the locations are disconnected from the inventory item.

If `disconnect_if_necessary` is set to `false` when you set inventory at a location and a fulfillment service location is involved, then the action will fail. If no fulfillment service location is involved, then this property is ignored.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/inventory_levels/adjust.json](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-adjust)

Adjusts the inventory level of an inventory item at a location

[inventoryAdjustQuantities](/docs/api/admin-graphql/latest/mutations/inventoryAdjustQuantities?example=adjusts-the-inventory-level-of-an-inventory-item-at-a-location)

  * [post/admin/api/latest/inventory_levels/connect.json](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect)

Connects an inventory item to a location

[inventoryActivate](/docs/api/admin-graphql/latest/mutations/inventoryActivate?example=connects-an-inventory-item-to-a-location)

  * [post/admin/api/latest/inventory_levels/set.json](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-set)

Sets the inventory level for an inventory item at a location

[inventorySetQuantities](/docs/api/admin-graphql/latest/mutations/inventorySetQuantities?example=sets-the-inventory-level-for-an-inventory-item-at-a-location)

  * [get/admin/api/latest/inventory_levels.json?location_ids=655441491](/docs/api/admin-rest/latest/resources/inventorylevel#get-inventory-levels?location-ids=655441491)

Retrieves a list of inventory levels

[inventoryItems](/docs/api/admin-graphql/latest/queries/inventoryItems)

  * [del/admin/api/latest/inventory_levels.json?inventory_item_id=808950810&location_id=655441491](/docs/api/admin-rest/latest/resources/inventorylevel#delete-inventory-levels?inventory-item-id=808950810&location-id=655441491)

Deletes an inventory level from a location

[inventoryDeactivate](/docs/api/admin-graphql/latest/mutations/inventoryDeactivate?example=deletes-an-inventory-level-from-a-location)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/inventorylevel#resource-object)

## The InventoryLevel resource

[Anchor to ](/docs/api/admin-rest/latest/resources/inventorylevel#resource-object-properties)

### Properties

* * *

available

->[quantity](/docs/api/admin-graphql/latest/objects/InventoryQuantity#field-InventoryQuantity.fields.quantity)

The available quantity of an inventory item at the inventory level's associated location. Returns `null` if the inventory item is not tracked.

* * *

inventory_item_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.id)

The ID of the inventory item associated with the inventory level. To find the ID of an inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

* * *

location_id

->[id](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id)

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/InventoryLevel#field-InventoryLevel.fields.updatedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the inventory level was last modified.

* * *

Was this section helpful?

YesNo

{}

## The InventoryLevel resource

9

1

2

3

4

5

6

{

"available": 6,

"inventory_item_id": 450789469,

"location_id": 40642626,

"updated_at": "2012-08-24T14:01:47-04:00"

}

* * *

##

[Anchor to POST request, Adjusts the inventory level of an inventory item at a location](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-adjust)

post

Adjusts the inventory level of an inventory item at a location

[inventoryAdjustQuantities](/docs/api/admin-graphql/latest/mutations/inventoryAdjustQuantities?example=adjusts-the-inventory-level-of-an-inventory-item-at-a-location)

Adjusts the inventory level of an inventory item at a single location

###

[Anchor to Parameters of Adjusts the inventory level of an inventory item at a location](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-adjust-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

available_adjustment

required**required**

The amount to adjust the available inventory quantity. Send negative values to subtract from the current available quantity. For example, `"available_adjustment": 2` increases the current available quantity by 2, and `"available_adjustment": -3`decreases the current available quantity by 3.

* * *

inventory_item_id

required**required**

The ID of the inventory item.

* * *

location_id

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

* * *

Was this section helpful?

YesNo

###

[Anchor to post-inventory-levels-adjust-examples](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-adjust-examples)Examples

Adjust the available quantity of an inventory item by 5 at a single location

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:655441491

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:808950810

required**required**

The ID of the inventory item.

available_adjustment:5

required**required**

The amount to adjust the available inventory quantity. Send negative values to subtract from the current available quantity. For example, `"available_adjustment": 2` increases the current available quantity by 2, and `"available_adjustment": -3`decreases the current available quantity by 3.

Adjusting inventory levels at a non-existent location fails and returns an error

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:655441491

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:808950810

required**required**

The ID of the inventory item.

available_adjustment:5

required**required**

The amount to adjust the available inventory quantity. Send negative values to subtract from the current available quantity. For example, `"available_adjustment": 2` increases the current available quantity by 2, and `"available_adjustment": -3`decreases the current available quantity by 3.

Adjusting inventory levels for an inventory item that is untracked fails and returns an error

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:655441491

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:808950810

required**required**

The ID of the inventory item.

available_adjustment:5

required**required**

The amount to adjust the available inventory quantity. Send negative values to subtract from the current available quantity. For example, `"available_adjustment": 2` increases the current available quantity by 2, and `"available_adjustment": -3`decreases the current available quantity by 3.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/inventory_levels/adjust.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"location_id":655441491,"inventory_item_id":808950810,"available_adjustment":5}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/adjust.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

HTTP/1.1 200 OK

{

"inventory_level": {

"inventory_item_id": 808950810,

"location_id": 655441491,

"available": 6,

"updated_at": "2026-01-09T19:36:10-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"

}

}

### examples

  * #### Adjust the available quantity of an inventory item by 5 at a single location

#####

        curl -d '{"location_id":655441491,"inventory_item_id":808950810,"available_adjustment":5}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/adjust.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.adjust({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available_adjustment": 5},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.adjust(
          session: test_session,
          body: {"location_id" => 655441491, "inventory_item_id" => 808950810, "available_adjustment" => 5},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.adjust({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available_adjustment": 5},
        });

#### response

        HTTP/1.1 200 OK{"inventory_level":{"inventory_item_id":808950810,"location_id":655441491,"available":6,"updated_at":"2026-01-09T19:36:10-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"}}

  * #### Adjusting inventory levels at a non-existent location fails and returns an error

#####

        curl -d '{"location_id":655441491,"inventory_item_id":808950810,"available_adjustment":5}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/adjust.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.adjust({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available_adjustment": 5},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.adjust(
          session: test_session,
          body: {"location_id" => 655441491, "inventory_item_id" => 808950810, "available_adjustment" => 5},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.adjust({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available_adjustment": 5},
        });

#### response

        HTTP/1.1 404 Not Found{"errors":"Not Found"}

  * #### Adjusting inventory levels for an inventory item that is untracked fails and returns an error

#####

        curl -d '{"location_id":655441491,"inventory_item_id":808950810,"available_adjustment":5}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/adjust.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.adjust({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available_adjustment": 5},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.adjust(
          session: test_session,
          body: {"location_id" => 655441491, "inventory_item_id" => 808950810, "available_adjustment" => 5},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.adjust({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available_adjustment": 5},
        });

#### response

        HTTP/1.1 422 Unprocessable Entity


* * *

##

[Anchor to POST request, Connects an inventory item to a location](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect)

post

Connects an inventory item to a location

[inventoryActivate](/docs/api/admin-graphql/latest/mutations/inventoryActivate?example=connects-an-inventory-item-to-a-location)

Connects an inventory item to a location by creating an inventory level at that location.

When connecting inventory items to locations, it's important to understand the rules around fulfillment service locations.

###

[Anchor to Parameters of Connects an inventory item to a location](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

inventory_item_id

required**required**

The ID of the inventory item.

* * *

location_id

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

* * *

relocate_if_necessary

default false**default false**

Whether inventory for any previously connected locations will be relocated. This property is ignored when no fulfillment service location is involved. For more information, refer to _Inventory levels and fulfillment service locations_.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-inventory-levels-connect-examples](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect-examples)Examples

Connect an inventory item to a location

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:844681632

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:457924702

required**required**

The ID of the inventory item.

Connecting an inventory item to a fulfillment service location without `"relocate_if_necessary": true` fails with a 422 error when permits_sku_sharing is false

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:611870435

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:808950810

required**required**

The ID of the inventory item.

Connecting an inventory item to a non-existent location fails and returns an error

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:123

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:457924702

required**required**

The ID of the inventory item.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/inventory_levels/connect.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"location_id":844681632,"inventory_item_id":457924702}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/connect.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

HTTP/1.1 201 Created

{

"inventory_level": {

"inventory_item_id": 457924702,

"location_id": 844681632,

"available": 0,

"updated_at": "2026-01-09T19:36:05-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/844681632?inventory_item_id=457924702"

}

}

### examples

  * #### Connect an inventory item to a location

#####

        curl -d '{"location_id":844681632,"inventory_item_id":457924702}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/connect.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.connect({
          body: {"location_id": 844681632, "inventory_item_id": 457924702},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.connect(
          session: test_session,
          body: {"location_id" => 844681632, "inventory_item_id" => 457924702},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.connect({
          body: {"location_id": 844681632, "inventory_item_id": 457924702},
        });

#### response

        HTTP/1.1 201 Created{"inventory_level":{"inventory_item_id":457924702,"location_id":844681632,"available":0,"updated_at":"2026-01-09T19:36:05-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/844681632?inventory_item_id=457924702"}}

  * #### Connecting an inventory item to a fulfillment service location without <code>"relocate_if_necessary": true</code> fails with a 422 error when permits_sku_sharing is false

#####

        curl -d '{"location_id":611870435,"inventory_item_id":808950810}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/connect.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.connect({
          body: {"location_id": 611870435, "inventory_item_id": 808950810},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.connect(
          session: test_session,
          body: {"location_id" => 611870435, "inventory_item_id" => 808950810},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.connect({
          body: {"location_id": 611870435, "inventory_item_id": 808950810},
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":["An item cannot be active at more than one location if one of them is a fulfillment service location."]}

  * #### Connecting an inventory item to a non-existent location fails and returns an error

#####

        curl -d '{"location_id":123,"inventory_item_id":457924702}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/connect.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.connect({
          body: {"location_id": 123, "inventory_item_id": 457924702},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.connect(
          session: test_session,
          body: {"location_id" => 123, "inventory_item_id" => 457924702},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.connect({
          body: {"location_id": 123, "inventory_item_id": 457924702},
        });

#### response

        HTTP/1.1 404 Not Found{"errors":"Not Found"}


* * *

##

[Anchor to POST request, Sets the inventory level for an inventory item at a location](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-set)

post

Sets the inventory level for an inventory item at a location

[inventorySetQuantities](/docs/api/admin-graphql/latest/mutations/inventorySetQuantities?example=sets-the-inventory-level-for-an-inventory-item-at-a-location)

Sets the inventory level for an inventory item at a location. If the specified location is not connected, it will be automatically connected first.

When connecting inventory items to locations, it's important to understand the rules around fulfillment service locations.

###

[Anchor to Parameters of Sets the inventory level for an inventory item at a location](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-set-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

available

required**required**

Sets the available inventory quantity.

* * *

inventory_item_id

required**required**

The ID of the inventory item associated with the inventory level. To find the ID of the inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

* * *

location_id

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

* * *

disconnect_if_necessary

default false**default false**

Whether inventory for any previously connected locations will be set to 0 and the locations disconnected. This property is ignored when no fulfillment service is involved. For more information, refer to _Inventory levels and fulfillment service locations_.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-inventory-levels-set-examples](/docs/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-set-examples)Examples

Set the available inventory at a location

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:655441491

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:808950810

required**required**

The ID of the inventory item associated with the inventory level. To find the ID of the inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

available:42

required**required**

Sets the available inventory quantity.

Setting an inventory item to a fulfillment service without `"disconnect_if_necessary": true` fails with a 422 error

Request body

location_id

Location_id resource**Location_id resource**

Show location_id properties

location_id:611870435

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

inventory_item_id:808950810

required**required**

The ID of the inventory item associated with the inventory level. To find the ID of the inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

available:42

required**required**

Sets the available inventory quantity.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/inventory_levels/set.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"location_id":655441491,"inventory_item_id":808950810,"available":42}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/set.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

HTTP/1.1 200 OK

{

"inventory_level": {

"inventory_item_id": 808950810,

"location_id": 655441491,

"available": 42,

"updated_at": "2026-01-09T19:35:56-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"

}

}

### examples

  * #### Set the available inventory at a location

#####

        curl -d '{"location_id":655441491,"inventory_item_id":808950810,"available":42}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/set.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.set({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available": 42},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.set(
          session: test_session,
          body: {"location_id" => 655441491, "inventory_item_id" => 808950810, "available" => 42},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.set({
          body: {"location_id": 655441491, "inventory_item_id": 808950810, "available": 42},
        });

#### response

        HTTP/1.1 200 OK{"inventory_level":{"inventory_item_id":808950810,"location_id":655441491,"available":42,"updated_at":"2026-01-09T19:35:56-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"}}

  * #### Setting an inventory item to a fulfillment service without <code>"disconnect_if_necessary": true</code> fails with a 422 error

#####

        curl -d '{"location_id":611870435,"inventory_item_id":808950810,"available":42}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels/set.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_level = new admin.rest.resources.InventoryLevel({session: session});

        await inventory_level.set({
          body: {"location_id": 611870435, "inventory_item_id": 808950810, "available": 42},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_level = ShopifyAPI::InventoryLevel.new(session: test_session)

        inventory_level.set(
          session: test_session,
          body: {"location_id" => 611870435, "inventory_item_id" => 808950810, "available" => 42},
        )

#####

        // Session is built by the OAuth process

        const inventory_level = new shopify.rest.InventoryLevel({session: session});

        await inventory_level.set({
          body: {"location_id": 611870435, "inventory_item_id": 808950810, "available": 42},
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":["An item cannot be active at more than one location if one of them is a fulfillment service location."]}


* * *

##

[Anchor to GET request, Retrieves a list of inventory levels](/docs/api/admin-rest/latest/resources/inventorylevel#get-inventory-levels?location-ids=655441491)

get

Retrieves a list of inventory levels

[inventoryItems](/docs/api/admin-graphql/latest/queries/inventoryItems)

Retrieves a list of inventory levels.

You must include `inventory_item_ids`, `location_ids`, or both as filter parameters.

**Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of inventory levels](/docs/api/admin-rest/latest/resources/inventorylevel#get-inventory-levels?location-ids=655441491-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

inventory_item_ids

≤ 50**≤ 50**

A comma-separated list of inventory item IDs. To find the ID of an inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

location_ids

≤ 50**≤ 50**

A comma-separated list of location IDs. To find the ID of a location, use the [Location resource](/api/admin-rest/latest/resources/location)

* * *

updated_at_min

Show inventory levels updated at or after date (format: 2019-03-19T01:21:44-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-inventory-levels?location-ids=655441491-examples](/docs/api/admin-rest/latest/resources/inventorylevel#get-inventory-levels?location-ids=655441491-examples)Examples

Retrieve inventory levels at a single location

Query parameters

location_ids=655441491

≤ 50**≤ 50**

A comma-separated list of location IDs. To find the ID of a location, use the [Location resource](/api/admin-rest/latest/resources/location)

Retrieve inventory levels for a single inventory item

Query parameters

inventory_item_ids=808950810

≤ 50**≤ 50**

A comma-separated list of inventory item IDs. To find the ID of an inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

Retrieve inventory levels for the specified inventory items and locations

Query parameters

inventory_item_ids=808950810,39072856

≤ 50**≤ 50**

A comma-separated list of inventory item IDs. To find the ID of an inventory item, use the [Inventory Item resource](/api/admin-rest/latest/resources/inventoryitem)

location_ids=655441491,487838322

≤ 50**≤ 50**

A comma-separated list of location IDs. To find the ID of a location, use the [Location resource](/api/admin-rest/latest/resources/location)

Retrieving inventory levels without specifying `location_ids` or `inventory_item_ids` fails and returns an error

Was this section helpful?

YesNo

get

## /admin/api/2026-01/inventory_levels.json?location_ids=655441491

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json?location_ids=655441491" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

HTTP/1.1 200 OK

{

"inventory_levels": [

{

"inventory_item_id": 49148385,

"location_id": 655441491,

"available": 2,

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/655441491?inventory_item_id=49148385"

},

{

"inventory_item_id": 808950810,

"location_id": 655441491,

"available": 1,

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"

},

{

"inventory_item_id": 457924702,

"location_id": 655441491,

"available": 4,

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/655441491?inventory_item_id=457924702"

},

{

"inventory_item_id": 39072856,

"location_id": 655441491,

"available": 3,

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/InventoryLevel/655441491?inventory_item_id=39072856"

}

]

}

### examples

  * #### Retrieve inventory levels at a single location

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json?location_ids=655441491" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryLevel.all({
          session: session,
          location_ids: "655441491",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryLevel.all(
          session: test_session,
          location_ids: "655441491",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryLevel.all({
          session: session,
          location_ids: "655441491",
        });

#### response

        HTTP/1.1 200 OK{"inventory_levels":[{"inventory_item_id":49148385,"location_id":655441491,"available":2,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=49148385"},{"inventory_item_id":808950810,"location_id":655441491,"available":1,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"},{"inventory_item_id":457924702,"location_id":655441491,"available":4,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=457924702"},{"inventory_item_id":39072856,"location_id":655441491,"available":3,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=39072856"}]}

  * #### Retrieve inventory levels for a single inventory item

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json?inventory_item_ids=808950810" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryLevel.all({
          session: session,
          inventory_item_ids: "808950810",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryLevel.all(
          session: test_session,
          inventory_item_ids: "808950810",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryLevel.all({
          session: session,
          inventory_item_ids: "808950810",
        });

#### response

        HTTP/1.1 200 OK{"inventory_levels":[{"inventory_item_id":808950810,"location_id":487838322,"available":9,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=808950810"},{"inventory_item_id":808950810,"location_id":655441491,"available":1,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"}]}

  * #### Retrieve inventory levels for the specified inventory items and locations

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json?inventory_item_ids=808950810%2C39072856&location_ids=655441491%2C487838322" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryLevel.all({
          session: session,
          inventory_item_ids: "808950810,39072856",
          location_ids: "655441491,487838322",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryLevel.all(
          session: test_session,
          inventory_item_ids: "808950810,39072856",
          location_ids: "655441491,487838322",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryLevel.all({
          session: session,
          inventory_item_ids: "808950810,39072856",
          location_ids: "655441491,487838322",
        });

#### response

        HTTP/1.1 200 OK{"inventory_levels":[{"inventory_item_id":808950810,"location_id":487838322,"available":9,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=808950810"},{"inventory_item_id":39072856,"location_id":487838322,"available":27,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=39072856"},{"inventory_item_id":808950810,"location_id":655441491,"available":1,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=808950810"},{"inventory_item_id":39072856,"location_id":655441491,"available":3,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/655441491?inventory_item_id=39072856"}]}

  * #### Retrieving inventory levels without specifying <code>location_ids</code> or <code>inventory_item_ids</code> fails and returns an error

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryLevel.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryLevel.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryLevel.all({
          session: session,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity


* * *

##

[Anchor to DELETE request, Deletes an inventory level from a location](/docs/api/admin-rest/latest/resources/inventorylevel#delete-inventory-levels?inventory-item-id=808950810&location-id=655441491)

del

Deletes an inventory level from a location

[inventoryDeactivate](/docs/api/admin-graphql/latest/mutations/inventoryDeactivate?example=deletes-an-inventory-level-from-a-location)

Deletes an inventory level of an inventory item at a location. Deleting an inventory level for an inventory item removes that item from the specified location. Every inventory item must have at least one inventory level. To move inventory to another location, first connect the inventory item to another location, and then delete the previous inventory level.

###

[Anchor to Parameters of Deletes an inventory level from a location](/docs/api/admin-rest/latest/resources/inventorylevel#delete-inventory-levels?inventory-item-id=808950810&location-id=655441491-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

inventory_item_id

required**required**

The ID for the inventory item.

* * *

location_id

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-inventory-levels?inventory-item-id=808950810&location-id=655441491-examples](/docs/api/admin-rest/latest/resources/inventorylevel#delete-inventory-levels?inventory-item-id=808950810&location-id=655441491-examples)Examples

Delete an inventory level

Query parameters

inventory_item_id=808950810

required**required**

The ID for the inventory item.

location_id=655441491

required**required**

The ID of the location that the inventory level belongs to. To find the ID of the location, use the [Location resource](/api/admin-rest/latest/resources/location)

Was this section helpful?

YesNo

del

## /admin/api/2026-01/inventory_levels.json?inventory_item_id=808950810&location_id=655441491

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json?inventory_item_id=808950810&location_id=655441491" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

HTTP/1.1 204 No Content

### examples

  * #### Delete an inventory level

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_levels.json?inventory_item_id=808950810&location_id=655441491" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryLevel.delete({
          session: session,
          inventory_item_id: "808950810",
          location_id: "655441491",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryLevel.delete(
          session: test_session,
          inventory_item_id: "808950810",
          location_id: "655441491",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryLevel.delete({
          session: session,
          inventory_item_id: "808950810",
          location_id: "655441491",
        });

#### response

        HTTP/1.1 204 No Content