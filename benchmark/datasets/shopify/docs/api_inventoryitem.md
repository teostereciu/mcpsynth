# InventoryItem

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/inventoryitem*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# InventoryItem

Ask assistant

Requires `inventory` access scope.

**Requires `inventory` access scope.:**

An inventory item represents a physical good. It holds essential information about the physical good, including its SKU and whether its inventory is tracked.

There is a 1:1 relationship between a product variant and an inventory item. Each product variant includes the ID of its related inventory item. You can use the inventory item ID to query the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource to retrieve the location and quantity for an inventory item.

Use the InventoryItem resource together with the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) and [Location](/api/admin-rest/latest/resources/location) resources to manage a store's inventory across multiple locations.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/inventory_items.json?ids=808950810,39072856,457924702](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items?ids=808950810,39072856,457924702)

Retrieves a detailed list for inventory items by IDs

[inventoryItems](/docs/api/admin-graphql/latest/queries/inventoryItems?example=retrieves-a-detailed-list-for-inventory-items-by-ids)

  * [get/admin/api/latest/inventory_items/{inventory_item_id}.json](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items-inventory-item-id)

Retrieves a single inventory item by ID

[inventoryItem](/docs/api/admin-graphql/latest/queries/inventoryItem)

  * [put/admin/api/latest/inventory_items/{inventory_item_id}.json](/docs/api/admin-rest/latest/resources/inventoryitem#put-inventory-items-inventory-item-id)

Updates an existing inventory item

[inventoryItemUpdate](/docs/api/admin-graphql/latest/mutations/inventoryItemUpdate?example=updates-an-existing-inventory-item)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/inventoryitem#resource-object)

## The InventoryItem resource

[Anchor to ](/docs/api/admin-rest/latest/resources/inventoryitem#resource-object-properties)

### Properties

* * *

cost

->[unitCost](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.unitCost)

The unit cost of the inventory item. The shop's default currency is used.

* * *

country_code_of_origin

->[countryCodeOfOrigin](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryCodeOfOrigin)

The country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) of where the item came from.

* * *

country_harmonized_system_codes

->[countryHarmonizedSystemCodes](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes)

An array of country-specific [Harmonized System](https://en.wikipedia.org/wiki/Harmonized_System) (HS) codes for the item. Used to determine duties when shipping the inventory item to certain countries.

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the inventory item was created.

* * *

harmonized_system_code

->[harmonizedSystemCode](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.harmonizedSystemCode)

The general [Harmonized System](https://en.wikipedia.org/wiki/Harmonized_System) (HS) code for the inventory item. Used if a country-specific HS code (`countryHarmonizedSystemCode`) is not available.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.id)

The ID of the inventory item.

* * *

province_code_of_origin

->[provinceCodeOfOrigin](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.provinceCodeOfOrigin)

The province code ([ISO 3166-2 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-2)) of where the item came from. The province code is only used if the shipping provider for the inventory item is Canada Post.

* * *

sku

->[sku](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.sku)

The unique SKU (stock keeping unit) of the inventory item. Case-sensitive string.

* * *

tracked

->[tracked](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.tracked)

Whether inventory levels are tracked for the item. If true, then the inventory quantity changes are tracked by Shopify.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.updatedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the inventory item was last modified.

* * *

requires_shipping

->[requiresShipping](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.requiresShipping)

Whether a customer needs to provide a shipping address when placing an order containing the inventory item.

* * *

Was this section helpful?

YesNo

{}

## The InventoryItem resource

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

{

"cost": "25.00",

"country_code_of_origin": "FR",

"country_harmonized_system_codes": [

{

"harmonized_system_code": "1234561111",

"country_code": "CA"

},

{

"harmonized_system_code": "1234562222",

"country_code": "US"

}

],

"created_at": "2012-08-24T14:01:47-04:00",

"harmonized_system_code": 123456,

"id": 450789469,

"province_code_of_origin": "QC",

"sku": "IPOD2008PINK",

"tracked": true,

"updated_at": "2012-08-24T14:01:47-04:00",

"requires_shipping": true

}

* * *

##

[Anchor to GET request, Retrieves a detailed list for inventory items by IDs](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items?ids=808950810,39072856,457924702)

get

Retrieves a detailed list for inventory items by IDs

[inventoryItems](/docs/api/admin-graphql/latest/queries/inventoryItems?example=retrieves-a-detailed-list-for-inventory-items-by-ids)

Retrieves a list that will display details for the inventory item IDs you specify. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a detailed list for inventory items by IDs](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items?ids=808950810,39072856,457924702-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

ids

required**required**

≤ 100**≤ 100**

Show only inventory items specified by a comma-separated list of IDs.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-inventory-items?ids=808950810,39072856,457924702-examples](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items?ids=808950810,39072856,457924702-examples)Examples

Retrieves a detailed list for inventory items by IDs

Query parameters

ids=808950810,39072856,457924702

required**required**

≤ 100**≤ 100**

Show only inventory items specified by a comma-separated list of IDs.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/inventory_items.json?ids=808950810,39072856,457924702

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items.json?ids=808950810%2C39072856%2C457924702" \

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

34

35

36

37

38

39

40

41

42

43

44

45

46

47

HTTP/1.1 200 OK

{

"inventory_items": [

{

"id": 39072856,

"sku": "IPOD2008GREEN",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"requires_shipping": true,

"cost": "25.00",

"country_code_of_origin": null,

"province_code_of_origin": null,

"harmonized_system_code": null,

"tracked": true,

"country_harmonized_system_codes": [],

"admin_graphql_api_id": "gid://shopify/InventoryItem/39072856"

},

{

"id": 457924702,

"sku": "IPOD2008BLACK",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"requires_shipping": true,

"cost": "25.00",

"country_code_of_origin": null,

"province_code_of_origin": null,

"harmonized_system_code": null,

"tracked": true,

"country_harmonized_system_codes": [],

"admin_graphql_api_id": "gid://shopify/InventoryItem/457924702"

},

{

"id": 808950810,

"sku": "IPOD2008PINK",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"requires_shipping": true,

"cost": "25.00",

"country_code_of_origin": null,

"province_code_of_origin": null,

"harmonized_system_code": null,

"tracked": true,

"country_harmonized_system_codes": [],

"admin_graphql_api_id": "gid://shopify/InventoryItem/808950810"

}

]

}

### examples

  * #### Retrieves a detailed list for inventory items by IDs

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items.json?ids=808950810%2C39072856%2C457924702" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryItem.all({
          session: session,
          ids: "808950810,39072856,457924702",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryItem.all(
          session: test_session,
          ids: "808950810,39072856,457924702",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryItem.all({
          session: session,
          ids: "808950810,39072856,457924702",
        });

#### response

        HTTP/1.1 200 OK{"inventory_items":[{"id":39072856,"sku":"IPOD2008GREEN","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","requires_shipping":true,"cost":"25.00","country_code_of_origin":null,"province_code_of_origin":null,"harmonized_system_code":null,"tracked":true,"country_harmonized_system_codes":[],"admin_graphql_api_id":"gid://shopify/InventoryItem/39072856"},{"id":457924702,"sku":"IPOD2008BLACK","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","requires_shipping":true,"cost":"25.00","country_code_of_origin":null,"province_code_of_origin":null,"harmonized_system_code":null,"tracked":true,"country_harmonized_system_codes":[],"admin_graphql_api_id":"gid://shopify/InventoryItem/457924702"},{"id":808950810,"sku":"IPOD2008PINK","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","requires_shipping":true,"cost":"25.00","country_code_of_origin":null,"province_code_of_origin":null,"harmonized_system_code":null,"tracked":true,"country_harmonized_system_codes":[],"admin_graphql_api_id":"gid://shopify/InventoryItem/808950810"}]}


* * *

##

[Anchor to GET request, Retrieves a single inventory item by ID](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items-inventory-item-id)

get

Retrieves a single inventory item by ID

[inventoryItem](/docs/api/admin-graphql/latest/queries/inventoryItem)

Retrieves a single inventory item by ID

###

[Anchor to Parameters of Retrieves a single inventory item by ID](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items-inventory-item-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

inventory_item_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-inventory-items-inventory-item-id-examples](/docs/api/admin-rest/latest/resources/inventoryitem#get-inventory-items-inventory-item-id-examples)Examples

Retrieve an inventory item by ID

Path parameters

inventory_item_id=808950810

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/inventory_items/808950810.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items/808950810.json" \

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

HTTP/1.1 200 OK

{

"inventory_item": {

"id": 808950810,

"sku": "IPOD2008PINK",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"requires_shipping": true,

"cost": "25.00",

"country_code_of_origin": null,

"province_code_of_origin": null,

"harmonized_system_code": null,

"tracked": true,

"country_harmonized_system_codes": [],

"admin_graphql_api_id": "gid://shopify/InventoryItem/808950810"

}

}

### examples

  * #### Retrieve an inventory item by ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items/808950810.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.InventoryItem.find({
          session: session,
          id: 808950810,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::InventoryItem.find(
          session: test_session,
          id: 808950810,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.InventoryItem.find({
          session: session,
          id: 808950810,
        });

#### response

        HTTP/1.1 200 OK{"inventory_item":{"id":808950810,"sku":"IPOD2008PINK","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","requires_shipping":true,"cost":"25.00","country_code_of_origin":null,"province_code_of_origin":null,"harmonized_system_code":null,"tracked":true,"country_harmonized_system_codes":[],"admin_graphql_api_id":"gid://shopify/InventoryItem/808950810"}}


* * *

##

[Anchor to PUT request, Updates an existing inventory item](/docs/api/admin-rest/latest/resources/inventoryitem#put-inventory-items-inventory-item-id)

put

Updates an existing inventory item

[inventoryItemUpdate](/docs/api/admin-graphql/latest/mutations/inventoryItemUpdate?example=updates-an-existing-inventory-item)

Updates an existing inventory item

###

[Anchor to Parameters of Updates an existing inventory item](/docs/api/admin-rest/latest/resources/inventoryitem#put-inventory-items-inventory-item-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

inventory_item_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-inventory-items-inventory-item-id-examples](/docs/api/admin-rest/latest/resources/inventoryitem#put-inventory-items-inventory-item-id-examples)Examples

Update an inventory item's SKU

Path parameters

inventory_item_id=808950810

string**string**

required**required**

Request body

inventory_item

Inventory_item resource**Inventory_item resource**

Show inventory_item properties

inventory_item.id:808950810

read-only**read-only**

The ID of the inventory item.

inventory_item.sku:"new sku"

->[sku](/docs/api/admin-graphql/latest/input-objects/InventoryItemInput#fields-sku)

The unique SKU (stock keeping unit) of the inventory item. Case-sensitive string.

Update an inventory item's unit cost

Path parameters

inventory_item_id=808950810

string**string**

required**required**

Request body

inventory_item

Inventory_item resource**Inventory_item resource**

Show inventory_item properties

inventory_item.id:808950810

read-only**read-only**

The ID of the inventory item.

inventory_item.cost:"25.00"

->[cost](/docs/api/admin-graphql/latest/input-objects/InventoryItemInput#fields-cost)

The unit cost of the inventory item. The shop's default currency is used.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/inventory_items/808950810.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"inventory_item":{"id":808950810,"sku":"new sku"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items/808950810.json" \

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

11

12

13

14

15

16

17

HTTP/1.1 200 OK

{

"inventory_item": {

"id": 808950810,

"sku": "new sku",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T19:34:22-05:00",

"requires_shipping": true,

"cost": "25.00",

"country_code_of_origin": null,

"province_code_of_origin": null,

"harmonized_system_code": null,

"tracked": true,

"country_harmonized_system_codes": [],

"admin_graphql_api_id": "gid://shopify/InventoryItem/808950810"

}

}

### examples

  * #### Update an inventory item's SKU

#####

        curl -d '{"inventory_item":{"id":808950810,"sku":"new sku"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items/808950810.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_item = new admin.rest.resources.InventoryItem({session: session});

        inventory_item.id = 808950810;
        inventory_item.sku = "new sku";
        await inventory_item.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_item = ShopifyAPI::InventoryItem.new(session: test_session)
        inventory_item.id = 808950810
        inventory_item.sku = "new sku"
        inventory_item.save!

#####

        // Session is built by the OAuth process

        const inventory_item = new shopify.rest.InventoryItem({session: session});
        inventory_item.id = 808950810;
        inventory_item.sku = "new sku";
        await inventory_item.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"inventory_item":{"id":808950810,"sku":"new sku","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:34:22-05:00","requires_shipping":true,"cost":"25.00","country_code_of_origin":null,"province_code_of_origin":null,"harmonized_system_code":null,"tracked":true,"country_harmonized_system_codes":[],"admin_graphql_api_id":"gid://shopify/InventoryItem/808950810"}}

  * #### Update an inventory item's unit cost

#####

        curl -d '{"inventory_item":{"id":808950810,"cost":"25.00"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/inventory_items/808950810.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const inventory_item = new admin.rest.resources.InventoryItem({session: session});

        inventory_item.id = 808950810;
        inventory_item.cost = "25.00";
        await inventory_item.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        inventory_item = ShopifyAPI::InventoryItem.new(session: test_session)
        inventory_item.id = 808950810
        inventory_item.cost = "25.00"
        inventory_item.save!

#####

        // Session is built by the OAuth process

        const inventory_item = new shopify.rest.InventoryItem({session: session});
        inventory_item.id = 808950810;
        inventory_item.cost = "25.00";
        await inventory_item.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"inventory_item":{"id":808950810,"sku":"IPOD2008PINK","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","requires_shipping":true,"cost":"25.00","country_code_of_origin":null,"province_code_of_origin":null,"harmonized_system_code":null,"tracked":true,"country_harmonized_system_codes":[],"admin_graphql_api_id":"gid://shopify/InventoryItem/808950810"}}