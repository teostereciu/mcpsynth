# Order

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/order*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Order

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

An order is a customer's request to purchase one or more products from a shop. You can create, retrieve, update, and delete orders using the Order resource.

#### Usage notes

  * When you create an order through the API, no payment information is collected, and no transaction is performed.
  * After an order is created, you can change only a few of its attributes using the API. You can't change the items or the quantities in an order using the REST API, but you can change them using the [GraphQL Admin API](/apps/fulfillment/order-management-apps/order-editing).
  * You can add [metafields](/docs/api/admin-rest/current/resources/metafield) to the Order resource.
  * You can allow merchants to create orders manually by using the [DraftOrder resource](/docs/api/admin-rest/current/resources/draftorder).


Caution

You can't use the Order resource to create a new checkout for an individual store. To create a checkout, you need to use the [Checkout API](/docs/api/admin-rest/current/resources/checkout) or an SDK powered by the [Storefront API](/docs/api/storefront), such as the [JavaScript Buy SDK](/docs/custom-storefronts/additional-sdks/js-buy), [iOS Buy SDK](/docs/custom-storefronts/mobile-kit/buy-sdk-ios), or [Android Buy SDK](/docs/custom-storefronts/mobile-kit/buy-sdk-android).

**Caution:**

You can't use the Order resource to create a new checkout for an individual store. To create a checkout, you need to use the [Checkout API](/docs/api/admin-rest/current/resources/checkout) or an SDK powered by the [Storefront API](/docs/api/storefront), such as the [JavaScript Buy SDK](/docs/custom-storefronts/additional-sdks/js-buy), [iOS Buy SDK](/docs/custom-storefronts/mobile-kit/buy-sdk-ios), or [Android Buy SDK](/docs/custom-storefronts/mobile-kit/buy-sdk-android).

Caution

Only the last 60 days' worth of orders from a store are accessible from the Order resource by default. If you want to access older orders, then you need to [request access to all orders](/api/usage/access-scopes#orders-permissions). If your app is granted access, then you can add the `read_all_orders` scope to your app along with `read_orders` or `write_orders`.

Only use this data if it's required for your app's functionality. Shopify will restrict [access to scopes](/api/usage/access-scopes) for apps that don't have a legitimate use for the associated data.

**Caution:**

Only the last 60 days' worth of orders from a store are accessible from the Order resource by default. If you want to access older orders, then you need to [request access to all orders](/api/usage/access-scopes#orders-permissions). If your app is granted access, then you can add the `read_all_orders` scope to your app along with `read_orders` or `write_orders`.

Only use this data if it's required for your app's functionality. Shopify will restrict [access to scopes](/api/usage/access-scopes) for apps that don't have a legitimate use for the associated data.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/orders.json](/docs/api/admin-rest/latest/resources/order#post-orders)

Create an order

[customerCreate](/docs/api/admin-graphql/latest/mutations/customerCreate)

[orderCreate](/docs/api/admin-graphql/latest/mutations/orderCreate)

  * [post/admin/api/latest/orders/{order_id}/cancel.json](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-cancel)

Cancel an order

[orderCancel](/docs/api/admin-graphql/latest/mutations/orderCancel?example=cancel-an-order)

  * [post/admin/api/latest/orders/{order_id}/close.json](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-close)

Close an order

[orderClose](/docs/api/admin-graphql/latest/mutations/orderClose?example=close-an-order)

  * [post/admin/api/latest/orders/{order_id}/open.json](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-open)

Re-open a closed order

[orderOpen](/docs/api/admin-graphql/latest/mutations/orderOpen?example=re-open-a-closed-order)

  * [get/admin/api/latest/orders.json?status=any](/docs/api/admin-rest/latest/resources/order#get-orders?status=any)

Retrieve a list of orders

[orders](/docs/api/admin-graphql/latest/queries/orders?example=retrieve-a-list-of-orders)

  * [get/admin/api/latest/orders/{order_id}.json?fields=id,line_items,name,total_price](/docs/api/admin-rest/latest/resources/order#get-orders-order-id?fields=id,line-items,name,total-price)

Retrieve a specific order

[order](/docs/api/admin-graphql/latest/queries/order?example=retrieve-a-specific-order)

  * [get/admin/api/latest/orders/count.json?status=any](/docs/api/admin-rest/latest/resources/order#get-orders-count?status=any)

Retrieve an order count

[ordersCount](/docs/api/admin-graphql/latest/queries/ordersCount?example=retrieve-an-order-count)

  * [put/admin/api/latest/orders/{order_id}.json](/docs/api/admin-rest/latest/resources/order#put-orders-order-id)

Update an order

[orderUpdate](/docs/api/admin-graphql/latest/mutations/orderUpdate)

  * [del/admin/api/latest/orders/{order_id}.json](/docs/api/admin-rest/latest/resources/order#delete-orders-order-id)

Delete an order

[orderDelete](/docs/api/admin-graphql/latest/mutations/orderDelete?example=delete-an-order)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/order#resource-object)

## The Order resource

[Anchor to ](/docs/api/admin-rest/latest/resources/order#resource-object-properties)

### Properties

* * *

app_id

integer**integer**

read-only**read-only**

->[app](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.app)

The ID of the app that created the order.

* * *

billing_address

[](/apps/store/data-protection/protected-customer-data)

object**object**

CustomerAddress**CustomerAddress**

->[billingAddress](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.billingAddress)

The mailing address associated with the payment method. This address is an optional field that won't be available on orders that do not require a payment method. It has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city, town, or village of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the billing address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the billing address.
  * **longitude** : The longitude of the billing address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the region (for example, province, state, or prefecture) of the billing address.
  * **province_code** : The alphanumeric abbreviation of the region of the billing address.
  * **zip** : The postal code (for example, zip, postcode, or Eircode) of the billing address.


* * *

browser_ip

string**string**

ip**ip**

read-only**read-only**

->[clientIp](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.clientIp)

The IP address of the browser used by the customer when they placed the order. Both IPv4 and IPv6 are supported.

* * *

buyer_accepts_marketing

boolean**boolean**

->[customerAcceptsMarketing](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.customerAcceptsMarketing)

Whether the customer consented to receive email updates from the shop.

* * *

cancel_reason

string**string**

->[cancelReason](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.cancelReason)

The reason why the order was canceled. Valid values:

Show cancel_reason properties

  * **customer** : The customer canceled the order.
  * **fraud** : The order was fraudulent.
  * **inventory** : Items in the order were not in inventory.
  * **declined** : The payment was declined.
  * **other** : A reason not in this list.


* * *

cancelled_at

string**string**

ISO 8601**ISO 8601**

read-only**read-only**

->[cancelledAt](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.cancelledAt)

The date and time when the order was canceled. Returns `null` if the order isn't canceled.

* * *

cart_token

string**string**

deprecated**deprecated**

A unique value when referencing the cart that's associated with the order.

* * *

checkout_token

string**string**

deprecated**deprecated**

A unique value when referencing the checkout that's associated with the order.

* * *

client_details

object**object**

read-only**read-only**

->[customerJourneySummary](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.customerJourneySummary)

Information about the browser that the customer used when they placed their order:

Show client_details properties

  * **accept_language** : The languages and locales that the browser understands.
  * **browser_height** : The browser screen height in pixels, if available.
  * **browser_ip** : The browser IP address.
  * **browser_width** : The browser screen width in pixels, if available.
  * **session_hash** : A hash of the session.
  * **user_agent** : Details of the browsing client, including software and operating versions.


* * *

closed_at

boolean**boolean**

ISO 8601**ISO 8601**

read-only**read-only**

->[closedAt](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.closedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the order was closed. Returns `null` if the order isn't closed.

* * *

company

object**object**

read-only**read-only**

->[purchasingEntity](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.purchasingEntity)

Represents information about the purchasing company for the order. `null` will be returned if there is no purchasing company.

* * *

confirmation_number

string**string**

read-only**read-only**

->[confirmationNumber](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.confirmationNumber)

A randomly generated alpha-numeric identifier for the order that may be shown to the customer instead of the sequential order name. This value isn't guaranteed to be unique.

* * *

Show 73 hidden fields

Was this section helpful?

YesNo

{}

## The Order resource

999

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

{

"app_id": 1966818,

"billing_address": {

"address1": "2259 Park Ct",

"address2": "Apartment 5",

"city": "Drayton Valley",

"company": null,

"country": "Canada",

"first_name": "Christopher",

"last_name": "Gorski",

"phone": "(555)555-5555",

"province": "Alberta",

"zip": "T0E 0M0",

"name": "Christopher Gorski",

"province_code": "AB",

"country_code": "CA",

"latitude": "45.41634",

"longitude": "-75.6868"

},

"browser_ip": "216.191.105.146",

"buyer_accepts_marketing": false,

"cancel_reason": "customer",

"cancelled_at": null,

"cart_token": "68778783ad298f1c80c3bafcddeea",

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": "en-US,en;q=0.9",

"browser_height": 1320,

"browser_ip": "216.191.105.146",

"browser_width": 1280,

"session_hash": "9ad4d1f4e6a8977b9dd98eed1e477643",

"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

},

"closed_at": "2008-01-10T11:00:00-05:00",

"company": {

"id": 182772,

* * *

##

[Anchor to POST request, Create an order](/docs/api/admin-rest/latest/resources/order#post-orders)

post

Create an order

[customerCreate](/docs/api/admin-graphql/latest/mutations/customerCreate)

[orderCreate](/docs/api/admin-graphql/latest/mutations/orderCreate)

Requires `orders` access scope.

**Requires `orders` access scope.:**

Creates an order.

By default, product inventory is not claimed when creating an order.

There are additional optional parameters that can be specified in the body of the request when creating an order:

  * **inventory_behaviour** : The behaviour to use when updating inventory. (default: `bypass`)
    * **bypass** : Do not claim inventory.
    * **decrement_ignoring_policy** : Ignore the product's inventory policy and claim inventory.
    * **decrement_obeying_policy** : Follow the product's inventory policy and claim inventory, if possible.
  * **send_receipt** : Whether to send an order confirmation to the customer. (default: `false`)


Note

If you're working on a private app and order confirmations are still being sent to the customer when `send_receipt` is set to `false`, then you need to disable the Storefront API from the private app's page in the Shopify admin.

**Note:**

If you're working on a private app and order confirmations are still being sent to the customer when `send_receipt` is set to `false`, then you need to disable the Storefront API from the private app's page in the Shopify admin.

  * **send_fulfillment_receipt** : Whether to send a shipping confirmation to the customer. (default: `false`)


Note

If you are including **shipping_address** or **billing_address** , make sure to pass both **first_name** and **last_name**. Otherwise both these addresses will be ignored.

**Usage notes:**
If you're using this endpoint with a trial or Partner development store, then you can create no more than 5 new orders per minute.

**Note:**

If you are including **shipping_address** or **billing_address** , make sure to pass both **first_name** and **last_name**. Otherwise both these addresses will be ignored.

**Usage notes:**
If you're using this endpoint with a trial or Partner development store, then you can create no more than 5 new orders per minute.

###

[Anchor to Parameters of Create an order](/docs/api/admin-rest/latest/resources/order#post-orders-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-orders-examples](/docs/api/admin-rest/latest/resources/order#post-orders-examples)Examples

Create a comprehensive order

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"title":"Big Brown Bear Boots","price":74.99,"grams":"1300","quantity":3,"tax_lines":[{"price":13.5,"rate":0.06,"title":"State tax"}]}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


order.total_tax:13.5

string**string**

price**price**

The sum of the prices for all tax lines applied to the order in the shop currency, including refunded and removed tax lines.

order.currency:"EUR"

string**string**

ISO 4217**ISO 4217**

read-only**read-only**

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the shop currency.

Create a partially paid order with a new customer and addresses

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"variant_id":447654529,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


order.customer:{"first_name":"Paul","last_name":"Norman","email":"paul.norman@example.com"}[](/apps/store/data-protection/protected-customer-data)

object**object**

Customer**Customer**

Information about the customer. The order might not have a customer and apps should not depend on the existence of a `customer` object. This value might be `null` if the order was created through Shopify POS. For more information about the `customer` object, see the [Customer resource](/docs/admin-api/rest/reference/customers/customer).

order.billing_address:{"first_name":"John","last_name":"Smith","address1":"123 Fake Street","phone":"555-555-5555","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"}[](/apps/store/data-protection/protected-customer-data)

object**object**

CustomerAddress**CustomerAddress**

->[billingAddress](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-billingAddress)

The mailing address associated with the payment method. This address is an optional field that won't be available on orders that do not require a payment method. It has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city, town, or village of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the billing address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the billing address.
  * **longitude** : The longitude of the billing address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the region (for example, province, state, or prefecture) of the billing address.
  * **province_code** : The alphanumeric abbreviation of the region of the billing address.
  * **zip** : The postal code (for example, zip, postcode, or Eircode) of the billing address.


order.shipping_address:{"first_name":"Jane","last_name":"Smith","address1":"123 Fake Street","phone":"777-777-7777","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"}[](/apps/store/data-protection/protected-customer-data)

object**object**

CustomerAddress**CustomerAddress**

->[shippingAddress](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-shippingAddress)

The mailing address to where the order will be shipped. This address is optional and will not be available on orders that do not require shipping. It has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city, town, or village of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the shipping address.
  * **first_name** : The first name of the person associated with the shipping address.
  * **last_name** : The last name of the person associated with the shipping address.
  * **latitude** : The latitude of the shipping address.
  * **longitude** : The longitude of the shipping address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the region (for example, province, state, or prefecture) of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the region of the shipping address.
  * **zip** : The postal code (for example, zip, postcode, or Eircode) of the shipping address.


order.email:"jane@example.com"[](/apps/store/data-protection/protected-customer-data)

string**string**

email**email**

->[email](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-email)

The customer's email address.

order.payment_status:"partially_paid"

string**string**

read-only**read-only**

The status of payments associated with the order. Can only be set when the order is created. Valid values:

Show payment_status properties

  * **pending** : The payments are pending. Payment might fail in this state. Check again to confirm whether the payments have been paid successfully.
  * **authorized** : The payments have been authorized.
  * **partially_paid** : The order has been partially paid.
  * **paid** : The payments have been paid.
  * **partially_refunded** : The payments have been partially refunded.
  * **refunded** : The payments have been refunded.
  * **voided** : The payments have been voided.


Create a pending order with an existing customer

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"variant_id":447654529,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


order.customer:{"id":207119551}[](/apps/store/data-protection/protected-customer-data)

object**object**

Customer**Customer**

Information about the customer. The order might not have a customer and apps should not depend on the existence of a `customer` object. This value might be `null` if the order was created through Shopify POS. For more information about the `customer` object, see the [Customer resource](/docs/admin-api/rest/reference/customers/customer).

order.payment_status:"pending"

string**string**

read-only**read-only**

The status of payments associated with the order. Can only be set when the order is created. Valid values:

Show payment_status properties

  * **pending** : The payments are pending. Payment might fail in this state. Check again to confirm whether the payments have been paid successfully.
  * **authorized** : The payments have been authorized.
  * **partially_paid** : The order has been partially paid.
  * **paid** : The payments have been paid.
  * **partially_refunded** : The payments have been partially refunded.
  * **refunded** : The payments have been refunded.
  * **voided** : The payments have been voided.


Create a simple order and fulfill it

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.email:"foo@example.com"[](/apps/store/data-protection/protected-customer-data)

string**string**

email**email**

->[email](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-email)

The customer's email address.

order.shipping_status:"fulfilled"

string**string**

The order's status in terms of fulfilled line items. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource for a more granular view. Valid values:

Show shipping_status properties

  * **fulfilled** : Every line item in the order has been fulfilled.
  * **null** : None of the line items in the order have been fulfilled.
  * **partial** : At least one line item in the order has been fulfilled.
  * **restocked** : Every line item in the order has been restocked and the order canceled.


order.fulfillments:[{"location_id":24826418}]

array**array**

An array of fulfillments associated with the order. For more information, see the [Fulfillment API](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment).

order.line_items:[{"variant_id":447654529,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


Create a simple order with only a product variant ID and no optional parameters

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"variant_id":447654529,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


Create a simple order without sending an order receipt or a fulfillment receipt

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.email:"foo@example.com"[](/apps/store/data-protection/protected-customer-data)

string**string**

email**email**

->[email](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-email)

The customer's email address.

order.shipping_status:"fulfilled"

string**string**

The order's status in terms of fulfilled line items. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource for a more granular view. Valid values:

Show shipping_status properties

  * **fulfilled** : Every line item in the order has been fulfilled.
  * **null** : None of the line items in the order have been fulfilled.
  * **partial** : At least one line item in the order has been fulfilled.
  * **restocked** : Every line item in the order has been restocked and the order canceled.


order.line_items:[{"variant_id":447654529,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


Create a simple order, sending an order confirmation and a shipping confirmation to the customer

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.email:"foo@example.com"[](/apps/store/data-protection/protected-customer-data)

string**string**

email**email**

->[email](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-email)

The customer's email address.

order.shipping_status:"fulfilled"

string**string**

The order's status in terms of fulfilled line items. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource for a more granular view. Valid values:

Show shipping_status properties

  * **fulfilled** : Every line item in the order has been fulfilled.
  * **null** : None of the line items in the order have been fulfilled.
  * **partial** : At least one line item in the order has been fulfilled.
  * **restocked** : Every line item in the order has been restocked and the order canceled.


order.line_items:[{"variant_id":457924702,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


Create an order and apply a discount

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"variant_id":447654529,"quantity":1}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


order.email:"jane@example.com"[](/apps/store/data-protection/protected-customer-data)

string**string**

email**email**

->[email](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-email)

The customer's email address.

order.phone:"18885551234"[](/apps/store/data-protection/protected-customer-data)

string**string**

->[phone](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-phone)

The customer's phone number for receiving SMS notifications.

order.billing_address:{"first_name":"John","last_name":"Smith","address1":"123 Fake Street","phone":"555-555-5555","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"}[](/apps/store/data-protection/protected-customer-data)

object**object**

CustomerAddress**CustomerAddress**

->[billingAddress](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-billingAddress)

The mailing address associated with the payment method. This address is an optional field that won't be available on orders that do not require a payment method. It has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city, town, or village of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the billing address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the billing address.
  * **longitude** : The longitude of the billing address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the region (for example, province, state, or prefecture) of the billing address.
  * **province_code** : The alphanumeric abbreviation of the region of the billing address.
  * **zip** : The postal code (for example, zip, postcode, or Eircode) of the billing address.


order.shipping_address:{"first_name":"Jane","last_name":"Smith","address1":"123 Fake Street","phone":"777-777-7777","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"}[](/apps/store/data-protection/protected-customer-data)

object**object**

CustomerAddress**CustomerAddress**

->[shippingAddress](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-shippingAddress)

The mailing address to where the order will be shipped. This address is optional and will not be available on orders that do not require shipping. It has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city, town, or village of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the shipping address.
  * **first_name** : The first name of the person associated with the shipping address.
  * **last_name** : The last name of the person associated with the shipping address.
  * **latitude** : The latitude of the shipping address.
  * **longitude** : The longitude of the shipping address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the region (for example, province, state, or prefecture) of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the region of the shipping address.
  * **zip** : The postal code (for example, zip, postcode, or Eircode) of the shipping address.


order.payment_status:"paid"

string**string**

read-only**read-only**

The status of payments associated with the order. Can only be set when the order is created. Valid values:

Show payment_status properties

  * **pending** : The payments are pending. Payment might fail in this state. Check again to confirm whether the payments have been paid successfully.
  * **authorized** : The payments have been authorized.
  * **partially_paid** : The order has been partially paid.
  * **paid** : The payments have been paid.
  * **partially_refunded** : The payments have been partially refunded.
  * **refunded** : The payments have been refunded.
  * **voided** : The payments have been voided.


order.discount_codes:[{"code":"FAKE30","amount":"9.00","type":"percentage"}]

array**array**

->[discountCode](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-discountCode)

A list of discounts applied to the order.

Note

When creating an order, only the first Discount Code supplied in this field is applied to the Order.

**Note:**

When creating an order, only the first Discount Code supplied in this field is applied to the Order.

Each discount object includes the following properties:

Show discount_codes properties

  * **amount** : The amount that's deducted from the order total. When you create an order, this value is the percentage or monetary amount to deduct. After the order is created, this property returns the calculated amount.
  * **code** : When the associated discount application is of type `code`, this property returns the discount code that was entered at checkout. Otherwise this property returns the title of the discount that was applied.
  * **type** : The type of discount. Default value: `fixed_amount`. Valid values:
    * `fixed_amount`: Applies `amount` as a unit of the store's currency. For example, if `amount` is 30 and the store's currency is USD, then 30 USD is deducted from the order total when the discount is applied.
    * `percentage`: Applies a discount of `amount` as a percentage of the order total.
    * `shipping`: Applies a free shipping discount on orders that have a shipping rate less than or equal to `amount`. For example, if `amount` is 30, then the discount will give the customer free shipping for any shipping rate that is less than or equal to $30.


Create an order with tax lines split across taxable line items

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"title":"Red Leather Coat","price":129.99,"grams":"1700","quantity":1},{"title":"Blue Suede Shoes","price":85.95,"grams":"750","quantity":1,"taxable":false},{"title":"Raspberry Beret","price":19.99,"grams":"320","quantity":2}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


order.tax_lines:[{"price":10.2,"rate":0.06,"title":"State tax"},{"price":4.25,"rate":0.025,"title":"County tax"}]

array**array**

->[taxLines](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-taxLines)

An array of tax line objects, each of which details a tax applicable to the order. Each object has the following properties:

Show tax_lines properties

  * **price** : The amount added to the order for this tax in the shop currency after discounts are applied.
  * **rate** : The rate of tax to be applied.
  * **title** : The name of the tax.
  * **channel_liable** : Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.

When creating an order through the API, tax lines can be specified on the order or the line items but not both. Tax lines specified on the order are split across the _taxable_ line items in the created order.

order.total_tax:14.45

string**string**

price**price**

The sum of the prices for all tax lines applied to the order in the shop currency, including refunded and removed tax lines.

Creating an order with tax lines both on line items and on the order fails and returns an error

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.line_items:[{"title":"Clicky Keyboard","price":99.99,"grams":"600","quantity":1,"tax_lines":[{"price":1,"rate":0.01,"title":"Keyboard tax"}]}][](/apps/store/data-protection/protected-customer-data)

array**array**

A list of line item objects, each containing information about an item in the order. Each object has the following properties:

Show line_items properties

  * **attributed_staffs** : The staff members attributed to the line item.
    * `id`: The id of the staff member.
    * `quantity`: The quantity of the line item attributed to the staff member.
  * **fulfillable_quantity** : The amount available to fulfill, calculated as follows:

        _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

  * **fulfillment_service** : The handle of a fulfillment service that stocks the product variant belonging to a line item.

This is the handle of a third-party fulfillment service in the following scenarios:

**Scenario 1**

    1. The product variant is stocked by a single fulfillment service.
    2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

**Scenario 2**

    1. Multiple fulfillment services stock the product variant.
    2. The last time that the line item was unfulfilled, it was awaiting fulfillment by a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.

If none of the above conditions are met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect inventory items to locations](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Altering the locations which stock a product variant won't change the value of this field for existing orders.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

  * **shipping_status** : How far along an order is in terms line items fulfilled. Valid values: `null`, `fulfilled`, `partial`, and `not_eligible`.
  * **grams** : The weight of the item in grams.
  * **id** : The ID of the line item.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **product_id** : The ID of the product that the line item belongs to. Can be `null` if the original product associated with the order is deleted at a later date.
  * **quantity** : The number of items that were purchased.
  * **current_quantity** : The line item's quantity, minus the removed quantity.
  * **requires_shipping** : Whether the item requires shipping.
  * **sku** : The item's SKU (stock keeping unit).
  * **title** : The title of the product.
  * **variant_id** : The ID of the product variant.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.
  * **name** : The name of the product variant.
  * **gift_card** : Whether the item is a gift card. If `true`, then the item is not taxed or considered for shipping charges.
  * **properties** : An array of custom information for the item that has been added to the cart. Often used to provide product customization options.
  * **taxable** : Whether the item was taxable.
  * **tax_lines** : A list of tax line objects, each of which details a tax applied to the item.
    * `title`: The name of the tax.
    * `price`: The amount added to the order for this tax in the shop currency after discounts are applied.
    * `price_set`: The amount added to the order for this tax in shop and presentment currencies after discounts are applied.
    * `rate`: The tax rate applied to the order to calculate the tax price.
    * `channel_liable`: Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.
  * **tip_payment_gateway** : The payment gateway used to tender the tip, such as `shopify_payments`. Present only on tips.
  * **tip_payment_method** : The payment method used to tender the tip, such as `Visa`. Present only on tips.
  * **total_discount** : The total amount of the discount allocated to the line item in the shop currency. This field must be explicitly set using draft orders, Shopify scripts, or the API. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **origin_location** : The location of the line item’s fulfillment origin. This field is due to be **deprecated**. Consider using [' "FulfillmentOrder#assigned_location_id](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) instead.
    * `id`: The location ID of the line item’s fulfillment origin. Used by Shopify to calculate applicable taxes. This is not the ID of the location where the order was placed. You can use the [FulfillmentOrder](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder) resource to determine the location an item will be sourced from.
    * `country_code`: The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the item's supplier.
    * `province_code`: The alphanumeric abbreviation for the region of the item's supplier.
    * `name`: The name of the item's supplier.
    * `address1`: The street address of the item's supplier.
    * `address2`: The suite number of the item's supplier.
    * `city`: The city of the item's supplier.
    * `zip`: The zip of the item's supplier.
  * **duties** : A list of duty objects, each containing information about a duty on the line item.


order.tax_lines:[{"price":6,"rate":0.06,"title":"State tax"}]

array**array**

->[taxLines](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput#fields-taxLines)

An array of tax line objects, each of which details a tax applicable to the order. Each object has the following properties:

Show tax_lines properties

  * **price** : The amount added to the order for this tax in the shop currency after discounts are applied.
  * **rate** : The rate of tax to be applied.
  * **title** : The name of the tax.
  * **channel_liable** : Whether the channel that submitted the tax line is liable for remitting. A value of `null` indicates unknown liability for the tax line.

When creating an order through the API, tax lines can be specified on the order or the line items but not both. Tax lines specified on the order are split across the _taxable_ line items in the created order.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"order":{"line_items":[{"title":"Big Brown Bear Boots","price":74.99,"grams":"1300","quantity":3,"tax_lines":[{"price":13.5,"rate":0.06,"title":"State tax"}]}],"transactions":[{"kind":"sale","status":"success","amount":238.47}],"total_tax":13.5,"currency":"EUR"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

999

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

HTTP/1.1 201 Created

{

"order": {

"id": 1073460004,

"admin_graphql_api_id": "gid://shopify/Order/1073460004",

"app_id": 755357713,

"browser_ip": null,

"buyer_accepts_marketing": false,

"cancel_reason": null,

"cancelled_at": null,

"cart_token": null,

"checkout_id": null,

"checkout_token": null,

"client_details": null,

"closed_at": null,

"confirmation_number": "UQVCRCXYY",

"confirmed": true,

"contact_email": null,

"created_at": "2026-01-09T17:28:06-05:00",

"currency": "EUR",

"current_subtotal_price": "224.97",

"current_subtotal_price_set": {

"shop_money": {

"amount": "224.97",

"currency_code": "EUR"

},

"presentment_money": {

"amount": "224.97",

"currency_code": "EUR"

}

},

"current_total_additional_fees_set": null,

"current_total_discounts": "0.00",

"current_total_discounts_set": {

"shop_money": {

"amount": "0.00",

### examples

  * #### Create a comprehensive order

#####

        curl -d '{"order":{"line_items":[{"title":"Big Brown Bear Boots","price":74.99,"grams":"1300","quantity":3,"tax_lines":[{"price":13.5,"rate":0.06,"title":"State tax"}]}],"transactions":[{"kind":"sale","status":"success","amount":238.47}],"total_tax":13.5,"currency":"EUR"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "title": "Big Brown Bear Boots",
            "price": 74.99,
            "grams": "1300",
            "quantity": 3,
            "tax_lines": [
              {
                "price": 13.5,
                "rate": 0.06,
                "title": "State tax"
              }
            ]
          }
        ];
        order.transactions = [
          {
            "kind": "sale",
            "status": "success",
            "amount": 238.47
          }
        ];
        order.total_tax = 13.5;
        order.currency = "EUR";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "title" => "Big Brown Bear Boots",
            "price" => 74.99,
            "grams" => "1300",
            "quantity" => 3,
            "tax_lines" => [
              {
                "price" => 13.5,
                "rate" => 0.06,
                "title" => "State tax"
              }
            ]
          }
        ]
        order.transactions = [
          {
            "kind" => "sale",
            "status" => "success",
            "amount" => 238.47
          }
        ]
        order.total_tax = 13.5
        order.currency = "EUR"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "title": "Big Brown Bear Boots",
            "price": 74.99,
            "grams": "1300",
            "quantity": 3,
            "tax_lines": [
              {
                "price": 13.5,
                "rate": 0.06,
                "title": "State tax"
              }
            ]
          }
        ];
        order.transactions = [
          {
            "kind": "sale",
            "status": "success",
            "amount": 238.47
          }
        ];
        order.total_tax = 13.5;
        order.currency = "EUR";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460004,"admin_graphql_api_id":"gid://shopify/Order/1073460004","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"UQVCRCXYY","confirmed":true,"contact_email":null,"created_at":"2026-01-09T17:28:06-05:00","currency":"EUR","current_subtotal_price":"224.97","current_subtotal_price_set":{"shop_money":{"amount":"224.97","currency_code":"EUR"},"presentment_money":{"amount":"224.97","currency_code":"EUR"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"EUR"},"presentment_money":{"amount":"0.00","currency_code":"EUR"}},"current_total_duties_set":null,"current_total_price":"238.47","current_total_price_set":{"shop_money":{"amount":"238.47","currency_code":"EUR"},"presentment_money":{"amount":"238.47","currency_code":"EUR"}},"current_total_tax":"13.50","current_total_tax_set":{"shop_money":{"amount":"13.50","currency_code":"EUR"},"presentment_money":{"amount":"13.50","currency_code":"EUR"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"","estimated_taxes":false,"payment_status":"paid","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/1fb2f6028df9ea4b66dbd4166330c550/authenticate?key=ae9af978b8a422b4d3fb4818a8eef6eb","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[""],"phone":null,"po_number":null,"presentment_currency":"EUR","processed_at":"2026-01-09T17:28:06-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"224.97","subtotal_price_set":{"shop_money":{"amount":"224.97","currency_code":"EUR"},"presentment_money":{"amount":"224.97","currency_code":"EUR"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"13.50","rate":0.06,"title":"State tax","price_set":{"shop_money":{"amount":"13.50","currency_code":"EUR"},"presentment_money":{"amount":"13.50","currency_code":"EUR"}},"channel_liable":false}],"taxes_included":false,"test":false,"token":"1fb2f6028df9ea4b66dbd4166330c550","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"EUR"},"presentment_money":{"amount":"0.00","currency_code":"EUR"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"EUR"},"presentment_money":{"amount":"0.00","currency_code":"EUR"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"EUR"},"presentment_money":{"amount":"0.00","currency_code":"EUR"}},"total_line_items_price":"224.97","total_line_items_price_set":{"shop_money":{"amount":"224.97","currency_code":"EUR"},"presentment_money":{"amount":"224.97","currency_code":"EUR"}},"total_outstanding":"0.00","total_price":"238.47","total_price_set":{"shop_money":{"amount":"238.47","currency_code":"EUR"},"presentment_money":{"amount":"238.47","currency_code":"EUR"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"EUR"},"presentment_money":{"amount":"0.00","currency_code":"EUR"}},"total_tax":"13.50","total_tax_set":{"shop_money":{"amount":"13.50","currency_code":"EUR"},"presentment_money":{"amount":"13.50","currency_code":"EUR"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:06-05:00","user_id":null,"billing_address":null,"customer":null,"discount_applications":[],"fulfillments":[],"line_items":[{"id":1071823243,"admin_graphql_api_id":"gid://shopify/LineItem/1071823243","attributed_staffs":[],"current_quantity":3,"fulfillable_quantity":3,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":1300,"name":"Big Brown Bear Boots","price":"74.99","price_set":{"shop_money":{"amount":"74.99","currency_code":"EUR"},"presentment_money":{"amount":"74.99","currency_code":"EUR"}},"product_exists":false,"product_id":null,"properties":[],"quantity":3,"requires_shipping":true,"sku":null,"taxable":true,"title":"Big Brown Bear Boots","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"EUR"},"presentment_money":{"amount":"0.00","currency_code":"EUR"}},"variant_id":null,"variant_inventory_management":null,"variant_title":null,"vendor":null,"tax_lines":[{"channel_liable":false,"price":"13.50","price_set":{"shop_money":{"amount":"13.50","currency_code":"EUR"},"presentment_money":{"amount":"13.50","currency_code":"EUR"}},"rate":0.06,"title":"State tax"}],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Create a partially paid order with a new customer and addresses

#####

        curl -d '{"order":{"line_items":[{"variant_id":447654529,"quantity":1}],"customer":{"first_name":"Paul","last_name":"Norman","email":"paul.norman@example.com"},"billing_address":{"first_name":"John","last_name":"Smith","address1":"123 Fake Street","phone":"555-555-5555","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"},"shipping_address":{"first_name":"Jane","last_name":"Smith","address1":"123 Fake Street","phone":"777-777-7777","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"},"email":"jane@example.com","transactions":[{"kind":"authorization","status":"success","amount":50.0}],"payment_status":"partially_paid"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        order.customer = {
          "first_name": "Paul",
          "last_name": "Norman",
          "email": "paul.norman@example.com"
        };
        order.billing_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "555-555-5555",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.shipping_address = {
          "first_name": "Jane",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "777-777-7777",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.email = "jane@example.com";
        order.transactions = [
          {
            "kind": "authorization",
            "status": "success",
            "amount": 50.0
          }
        ];
        order.payment_status = "partially_paid";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        order.customer = {
          "first_name" => "Paul",
          "last_name" => "Norman",
          "email" => "paul.norman@example.com"
        }
        order.billing_address = {
          "first_name" => "John",
          "last_name" => "Smith",
          "address1" => "123 Fake Street",
          "phone" => "555-555-5555",
          "city" => "Fakecity",
          "province" => "Ontario",
          "country" => "Canada",
          "zip" => "K2P 1L4"
        }
        order.shipping_address = {
          "first_name" => "Jane",
          "last_name" => "Smith",
          "address1" => "123 Fake Street",
          "phone" => "777-777-7777",
          "city" => "Fakecity",
          "province" => "Ontario",
          "country" => "Canada",
          "zip" => "K2P 1L4"
        }
        order.email = "jane@example.com"
        order.transactions = [
          {
            "kind" => "authorization",
            "status" => "success",
            "amount" => 50.0
          }
        ]
        order.payment_status = "partially_paid"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        order.customer = {
          "first_name": "Paul",
          "last_name": "Norman",
          "email": "paul.norman@example.com"
        };
        order.billing_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "555-555-5555",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.shipping_address = {
          "first_name": "Jane",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "777-777-7777",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.email = "jane@example.com";
        order.transactions = [
          {
            "kind": "authorization",
            "status": "success",
            "amount": 50.0
          }
        ];
        order.payment_status = "partially_paid";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460007,"admin_graphql_api_id":"gid://shopify/Order/1073460007","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"I8A1KK1DQ","confirmed":true,"contact_email":"jane@example.com","created_at":"2026-01-09T17:28:25-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"jane@example.com","estimated_taxes":false,"payment_status":"partially_paid","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/ca390c6a919f7aa5985ff4705427df5e/authenticate?key=459186caea03aa97e5038391bef41ef7","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[""],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:28:25-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"ca390c6a919f7aa5985ff4705427df5e","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"149.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:25-05:00","user_id":null,"billing_address":{"first_name":"John","address1":"123 Fake Street","phone":"555-555-5555","city":"Fakecity","zip":"K2P 1L4","province":"Ontario","country":"Canada","last_name":"Smith","address2":null,"company":null,"latitude":null,"longitude":null,"name":"John Smith","country_code":"CA","province_code":"ON"},"customer":{"id":1073339522,"created_at":"2026-01-09T17:28:25-05:00","updated_at":"2026-01-09T17:28:25-05:00","first_name":"John","last_name":"Smith","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":null,"tags":"","email":"paul.norman@example.com","phone":null,"currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/1073339522","default_address":{"id":1053317342,"customer_id":1073339522,"first_name":"Jane","last_name":"Smith","company":null,"address1":"123 Fake Street","address2":null,"city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4","phone":"777-777-7777","name":"Jane Smith","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}},"discount_applications":[],"fulfillments":[],"line_items":[{"id":1071823245,"admin_graphql_api_id":"gid://shopify/LineItem/1071823245","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":{"first_name":"Jane","address1":"123 Fake Street","phone":"777-777-7777","city":"Fakecity","zip":"K2P 1L4","province":"Ontario","country":"Canada","last_name":"Smith","address2":null,"company":null,"latitude":null,"longitude":null,"name":"Jane Smith","country_code":"CA","province_code":"ON"},"shipping_lines":[]}}

  * #### Create a pending order with an existing customer

#####

        curl -d '{"order":{"line_items":[{"variant_id":447654529,"quantity":1}],"customer":{"id":207119551},"payment_status":"pending"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        order.customer = {
          "id": 207119551
        };
        order.payment_status = "pending";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        order.customer = {
          "id" => 207119551
        }
        order.payment_status = "pending"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        order.customer = {
          "id": 207119551
        };
        order.payment_status = "pending";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073459997,"admin_graphql_api_id":"gid://shopify/Order/1073459997","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"FTPY26I8W","confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2026-01-09T17:27:18-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"pending","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/e6b7ca8d37791e671be9e845b783268e/authenticate?key=7bf575da119662b7e142f5ba5f7a5fa5","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:27:18-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"e6b7ca8d37791e671be9e845b783268e","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"199.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:18-05:00","user_id":null,"billing_address":null,"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:27:19-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[],"fulfillments":[],"line_items":[{"id":1071823235,"admin_graphql_api_id":"gid://shopify/LineItem/1071823235","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Create a simple order and fulfill it

#####

        curl -d '{"order":{"email":"foo@example.com","shipping_status":"fulfilled","fulfillments":[{"location_id":24826418}],"line_items":[{"variant_id":447654529,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.email = "foo@example.com";
        order.shipping_status = "fulfilled";
        order.fulfillments = [
          {
            "location_id": 24826418
          }
        ];
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.email = "foo@example.com"
        order.shipping_status = "fulfilled"
        order.fulfillments = [
          {
            "location_id" => 24826418
          }
        ]
        order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.email = "foo@example.com";
        order.shipping_status = "fulfilled";
        order.fulfillments = [
          {
            "location_id": 24826418
          }
        ];
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460002,"admin_graphql_api_id":"gid://shopify/Order/1073460002","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"LFLTJW845","confirmed":true,"contact_email":"foo@example.com","created_at":"2026-01-09T17:27:44-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"foo@example.com","estimated_taxes":false,"payment_status":"paid","shipping_status":"fulfilled","landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/f7ee3b69d8d7ccf68fe6da3a95084dea/authenticate?key=b83b17d1454048869accfbc83136f4ea","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:27:44-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"f7ee3b69d8d7ccf68fe6da3a95084dea","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"199.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:44-05:00","user_id":null,"billing_address":null,"customer":{"id":1073339519,"created_at":"2026-01-09T17:27:44-05:00","updated_at":"2026-01-09T17:27:44-05:00","first_name":null,"last_name":null,"state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":null,"tags":"","email":"foo@example.com","phone":null,"currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/1073339519"},"discount_applications":[],"fulfillments":[{"id":1069019887,"admin_graphql_api_id":"gid://shopify/Fulfillment/1069019887","created_at":"2026-01-09T17:27:44-05:00","location_id":24826418,"name":"#1002.1","order_id":1073460002,"origin_address":{},"receipt":{},"service":"shipwire-app","shipment_status":null,"status":"success","tracking_company":null,"tracking_number":null,"tracking_numbers":[],"tracking_url":null,"tracking_urls":[],"updated_at":"2026-01-09T17:27:44-05:00","line_items":[{"id":1071823241,"admin_graphql_api_id":"gid://shopify/LineItem/1071823241","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":0,"fulfillment_service":"shipwire-app","shipping_status":"fulfilled","gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}]}],"line_items":[{"id":1071823241,"admin_graphql_api_id":"gid://shopify/LineItem/1071823241","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":0,"fulfillment_service":"shipwire-app","shipping_status":"fulfilled","gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Create a simple order with only a product variant ID and no optional parameters

#####

        curl -d '{"order":{"line_items":[{"variant_id":447654529,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460009,"admin_graphql_api_id":"gid://shopify/Order/1073460009","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"RR9NX55QQ","confirmed":true,"contact_email":null,"created_at":"2026-01-09T17:28:36-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"","estimated_taxes":false,"payment_status":"paid","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/ea607eef90712e7a761f45d5b7004cb6/authenticate?key=c707a7897b887460b29436239a83d25e","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:28:36-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"ea607eef90712e7a761f45d5b7004cb6","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"199.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:36-05:00","user_id":null,"billing_address":null,"customer":null,"discount_applications":[],"fulfillments":[],"line_items":[{"id":1071823249,"admin_graphql_api_id":"gid://shopify/LineItem/1071823249","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Create a simple order without sending an order receipt or a fulfillment receipt

#####

        curl -d '{"order":{"email":"foo@example.com","shipping_status":"fulfilled","line_items":[{"variant_id":447654529,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.email = "foo@example.com";
        order.shipping_status = "fulfilled";
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.email = "foo@example.com"
        order.shipping_status = "fulfilled"
        order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.email = "foo@example.com";
        order.shipping_status = "fulfilled";
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460003,"admin_graphql_api_id":"gid://shopify/Order/1073460003","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"YAZYEWP9F","confirmed":true,"contact_email":"foo@example.com","created_at":"2026-01-09T17:27:46-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"foo@example.com","estimated_taxes":false,"payment_status":"paid","shipping_status":"fulfilled","landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/c13183f7628942e08d889b1d58fde982/authenticate?key=01f11f9c75240569ca227dcd739709b0","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:27:46-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"c13183f7628942e08d889b1d58fde982","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"199.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:46-05:00","user_id":null,"billing_address":null,"customer":{"id":1073339520,"created_at":"2026-01-09T17:27:46-05:00","updated_at":"2026-01-09T17:27:47-05:00","first_name":null,"last_name":null,"state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":null,"tags":"","email":"foo@example.com","phone":null,"currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/1073339520"},"discount_applications":[],"fulfillments":[{"id":1069019888,"admin_graphql_api_id":"gid://shopify/Fulfillment/1069019888","created_at":"2026-01-09T17:27:47-05:00","location_id":24826418,"name":"#1002.1","order_id":1073460003,"origin_address":{},"receipt":{},"service":"shipwire-app","shipment_status":null,"status":"success","tracking_company":null,"tracking_number":null,"tracking_numbers":[],"tracking_url":null,"tracking_urls":[],"updated_at":"2026-01-09T17:27:47-05:00","line_items":[{"id":1071823242,"admin_graphql_api_id":"gid://shopify/LineItem/1071823242","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":0,"fulfillment_service":"shipwire-app","shipping_status":"fulfilled","gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}]}],"line_items":[{"id":1071823242,"admin_graphql_api_id":"gid://shopify/LineItem/1071823242","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":0,"fulfillment_service":"shipwire-app","shipping_status":"fulfilled","gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Create a simple order, sending an order confirmation and a shipping confirmation to the customer

#####

        curl -d '{"order":{"email":"foo@example.com","shipping_status":"fulfilled","send_receipt":true,"send_fulfillment_receipt":true,"line_items":[{"variant_id":457924702,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.email = "foo@example.com";
        order.shipping_status = "fulfilled";
        order.send_receipt = true;
        order.send_fulfillment_receipt = true;
        order.line_items = [
          {
            "variant_id": 457924702,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.email = "foo@example.com"
        order.shipping_status = "fulfilled"
        order.send_receipt = true
        order.send_fulfillment_receipt = true
        order.line_items = [
          {
            "variant_id" => 457924702,
            "quantity" => 1
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.email = "foo@example.com";
        order.shipping_status = "fulfilled";
        order.send_receipt = true;
        order.send_fulfillment_receipt = true;
        order.line_items = [
          {
            "variant_id": 457924702,
            "quantity": 1
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073459989,"admin_graphql_api_id":"gid://shopify/Order/1073459989","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"AZN5TU3Z7","confirmed":true,"contact_email":"foo@example.com","created_at":"2026-01-09T17:26:23-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"foo@example.com","estimated_taxes":false,"payment_status":"paid","shipping_status":"fulfilled","landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/79c8c8bcafd76a38e7d0307f62b454ab/authenticate?key=bdca4444b1c28b5136baa7ffc38dee34","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:26:23-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"79c8c8bcafd76a38e7d0307f62b454ab","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"199.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:23-05:00","user_id":null,"billing_address":null,"customer":{"id":1073339514,"created_at":"2026-01-09T17:26:23-05:00","updated_at":"2026-01-09T17:26:24-05:00","first_name":null,"last_name":null,"state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":null,"tags":"","email":"foo@example.com","phone":null,"currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/1073339514"},"discount_applications":[],"fulfillments":[{"id":1069019883,"admin_graphql_api_id":"gid://shopify/Fulfillment/1069019883","created_at":"2026-01-09T17:26:23-05:00","location_id":655441491,"name":"#1002.1","order_id":1073459989,"origin_address":{},"receipt":{},"service":"manual","shipment_status":null,"status":"success","tracking_company":null,"tracking_number":null,"tracking_numbers":[],"tracking_url":null,"tracking_urls":[],"updated_at":"2026-01-09T17:26:23-05:00","line_items":[{"id":1071823227,"admin_graphql_api_id":"gid://shopify/LineItem/1071823227","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":"fulfilled","gift_card":false,"grams":567,"name":"IPod Nano - 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}]}],"line_items":[{"id":1071823227,"admin_graphql_api_id":"gid://shopify/LineItem/1071823227","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":"fulfilled","gift_card":false,"grams":567,"name":"IPod Nano - 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Create an order and apply a discount

#####

        curl -d '{"order":{"line_items":[{"variant_id":447654529,"quantity":1}],"email":"jane@example.com","phone":"18885551234","billing_address":{"first_name":"John","last_name":"Smith","address1":"123 Fake Street","phone":"555-555-5555","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"},"shipping_address":{"first_name":"Jane","last_name":"Smith","address1":"123 Fake Street","phone":"777-777-7777","city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4"},"transactions":[{"kind":"sale","status":"success","amount":50.0}],"payment_status":"paid","discount_codes":[{"code":"FAKE30","amount":"9.00","type":"percentage"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        order.email = "jane@example.com";
        order.phone = "18885551234";
        order.billing_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "555-555-5555",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.shipping_address = {
          "first_name": "Jane",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "777-777-7777",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.transactions = [
          {
            "kind": "sale",
            "status": "success",
            "amount": 50.0
          }
        ];
        order.payment_status = "paid";
        order.discount_codes = [
          {
            "code": "FAKE30",
            "amount": "9.00",
            "type": "percentage"
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        order.email = "jane@example.com"
        order.phone = "18885551234"
        order.billing_address = {
          "first_name" => "John",
          "last_name" => "Smith",
          "address1" => "123 Fake Street",
          "phone" => "555-555-5555",
          "city" => "Fakecity",
          "province" => "Ontario",
          "country" => "Canada",
          "zip" => "K2P 1L4"
        }
        order.shipping_address = {
          "first_name" => "Jane",
          "last_name" => "Smith",
          "address1" => "123 Fake Street",
          "phone" => "777-777-7777",
          "city" => "Fakecity",
          "province" => "Ontario",
          "country" => "Canada",
          "zip" => "K2P 1L4"
        }
        order.transactions = [
          {
            "kind" => "sale",
            "status" => "success",
            "amount" => 50.0
          }
        ]
        order.payment_status = "paid"
        order.discount_codes = [
          {
            "code" => "FAKE30",
            "amount" => "9.00",
            "type" => "percentage"
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        order.email = "jane@example.com";
        order.phone = "18885551234";
        order.billing_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "555-555-5555",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.shipping_address = {
          "first_name": "Jane",
          "last_name": "Smith",
          "address1": "123 Fake Street",
          "phone": "777-777-7777",
          "city": "Fakecity",
          "province": "Ontario",
          "country": "Canada",
          "zip": "K2P 1L4"
        };
        order.transactions = [
          {
            "kind": "sale",
            "status": "success",
            "amount": 50.0
          }
        ];
        order.payment_status = "paid";
        order.discount_codes = [
          {
            "code": "FAKE30",
            "amount": "9.00",
            "type": "percentage"
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460011,"admin_graphql_api_id":"gid://shopify/Order/1073460011","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"PXRRCK0G0","confirmed":true,"contact_email":"jane@example.com","created_at":"2026-01-09T17:28:43-05:00","currency":"USD","current_subtotal_price":"181.09","current_subtotal_price_set":{"shop_money":{"amount":"181.09","currency_code":"USD"},"presentment_money":{"amount":"181.09","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"17.91","current_total_discounts_set":{"shop_money":{"amount":"17.91","currency_code":"USD"},"presentment_money":{"amount":"17.91","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"181.09","current_total_price_set":{"shop_money":{"amount":"181.09","currency_code":"USD"},"presentment_money":{"amount":"181.09","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"FAKE30","amount":"17.91","type":"percentage"}],"duties_included":false,"email":"jane@example.com","estimated_taxes":false,"payment_status":"paid","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/59b4b5079d687bba69233c72237f0ec7/authenticate?key=1ae80adc944217fc74965759d44bc4a7","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[""],"phone":"+18885551234","po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:28:43-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"181.09","subtotal_price_set":{"shop_money":{"amount":"181.09","currency_code":"USD"},"presentment_money":{"amount":"181.09","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"59b4b5079d687bba69233c72237f0ec7","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"17.91","total_discounts_set":{"shop_money":{"amount":"17.91","currency_code":"USD"},"presentment_money":{"amount":"17.91","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"131.09","total_price":"181.09","total_price_set":{"shop_money":{"amount":"181.09","currency_code":"USD"},"presentment_money":{"amount":"181.09","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:44-05:00","user_id":null,"billing_address":{"first_name":"John","address1":"123 Fake Street","phone":"555-555-5555","city":"Fakecity","zip":"K2P 1L4","province":"Ontario","country":"Canada","last_name":"Smith","address2":null,"company":null,"latitude":null,"longitude":null,"name":"John Smith","country_code":"CA","province_code":"ON"},"customer":{"id":1073339523,"created_at":"2026-01-09T17:28:43-05:00","updated_at":"2026-01-09T17:28:44-05:00","first_name":"John","last_name":"Smith","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":null,"tags":"","email":"jane@example.com","phone":null,"currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/1073339523","default_address":{"id":1053317344,"customer_id":1073339523,"first_name":"Jane","last_name":"Smith","company":null,"address1":"123 Fake Street","address2":null,"city":"Fakecity","province":"Ontario","country":"Canada","zip":"K2P 1L4","phone":"777-777-7777","name":"Jane Smith","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}},"discount_applications":[{"target_type":"line_item","type":"manual","value":"9.0","value_type":"percentage","allocation_method":"across","target_selection":"all","title":"FAKE30","description":"FAKE30"}],"fulfillments":[],"line_items":[{"id":1071823251,"admin_graphql_api_id":"gid://shopify/LineItem/1071823251","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[{"amount":"17.91","amount_set":{"shop_money":{"amount":"17.91","currency_code":"USD"},"presentment_money":{"amount":"17.91","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[],"shipping_address":{"first_name":"Jane","address1":"123 Fake Street","phone":"777-777-7777","city":"Fakecity","zip":"K2P 1L4","province":"Ontario","country":"Canada","last_name":"Smith","address2":null,"company":null,"latitude":null,"longitude":null,"name":"Jane Smith","country_code":"CA","province_code":"ON"},"shipping_lines":[]}}

  * #### Create an order with tax lines split across taxable line items

#####

        curl -d '{"order":{"line_items":[{"title":"Red Leather Coat","price":129.99,"grams":"1700","quantity":1},{"title":"Blue Suede Shoes","price":85.95,"grams":"750","quantity":1,"taxable":false},{"title":"Raspberry Beret","price":19.99,"grams":"320","quantity":2}],"tax_lines":[{"price":10.2,"rate":0.06,"title":"State tax"},{"price":4.25,"rate":0.025,"title":"County tax"}],"total_tax":14.45}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "title": "Red Leather Coat",
            "price": 129.99,
            "grams": "1700",
            "quantity": 1
          },
          {
            "title": "Blue Suede Shoes",
            "price": 85.95,
            "grams": "750",
            "quantity": 1,
            "taxable": false
          },
          {
            "title": "Raspberry Beret",
            "price": 19.99,
            "grams": "320",
            "quantity": 2
          }
        ];
        order.tax_lines = [
          {
            "price": 10.2,
            "rate": 0.06,
            "title": "State tax"
          },
          {
            "price": 4.25,
            "rate": 0.025,
            "title": "County tax"
          }
        ];
        order.total_tax = 14.45;
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "title" => "Red Leather Coat",
            "price" => 129.99,
            "grams" => "1700",
            "quantity" => 1
          },
          {
            "title" => "Blue Suede Shoes",
            "price" => 85.95,
            "grams" => "750",
            "quantity" => 1,
            "taxable" => false
          },
          {
            "title" => "Raspberry Beret",
            "price" => 19.99,
            "grams" => "320",
            "quantity" => 2
          }
        ]
        order.tax_lines = [
          {
            "price" => 10.2,
            "rate" => 0.06,
            "title" => "State tax"
          },
          {
            "price" => 4.25,
            "rate" => 0.025,
            "title" => "County tax"
          }
        ]
        order.total_tax = 14.45
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "title": "Red Leather Coat",
            "price": 129.99,
            "grams": "1700",
            "quantity": 1
          },
          {
            "title": "Blue Suede Shoes",
            "price": 85.95,
            "grams": "750",
            "quantity": 1,
            "taxable": false
          },
          {
            "title": "Raspberry Beret",
            "price": 19.99,
            "grams": "320",
            "quantity": 2
          }
        ];
        order.tax_lines = [
          {
            "price": 10.2,
            "rate": 0.06,
            "title": "State tax"
          },
          {
            "price": 4.25,
            "rate": 0.025,
            "title": "County tax"
          }
        ];
        order.total_tax = 14.45;
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"order":{"id":1073460008,"admin_graphql_api_id":"gid://shopify/Order/1073460008","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"JTCT03DPG","confirmed":true,"contact_email":null,"created_at":"2026-01-09T17:28:28-05:00","currency":"USD","current_subtotal_price":"255.92","current_subtotal_price_set":{"shop_money":{"amount":"255.92","currency_code":"USD"},"presentment_money":{"amount":"255.92","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"270.37","current_total_price_set":{"shop_money":{"amount":"270.37","currency_code":"USD"},"presentment_money":{"amount":"270.37","currency_code":"USD"}},"current_total_tax":"14.45","current_total_tax_set":{"shop_money":{"amount":"14.45","currency_code":"USD"},"presentment_money":{"amount":"14.45","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"","estimated_taxes":false,"payment_status":"paid","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/c874f759c9d7742fac61020a76db2814/authenticate?key=dc86790b7dc16fd7df149183831a2a63","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:28:28-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"255.92","subtotal_price_set":{"shop_money":{"amount":"255.92","currency_code":"USD"},"presentment_money":{"amount":"255.92","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"10.20","rate":0.06,"title":"State tax","price_set":{"shop_money":{"amount":"10.20","currency_code":"USD"},"presentment_money":{"amount":"10.20","currency_code":"USD"}},"channel_liable":false},{"price":"4.25","rate":0.025,"title":"County tax","price_set":{"shop_money":{"amount":"4.25","currency_code":"USD"},"presentment_money":{"amount":"4.25","currency_code":"USD"}},"channel_liable":false}],"taxes_included":false,"test":false,"token":"c874f759c9d7742fac61020a76db2814","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"255.92","total_line_items_price_set":{"shop_money":{"amount":"255.92","currency_code":"USD"},"presentment_money":{"amount":"255.92","currency_code":"USD"}},"total_outstanding":"270.37","total_price":"270.37","total_price_set":{"shop_money":{"amount":"270.37","currency_code":"USD"},"presentment_money":{"amount":"270.37","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"14.45","total_tax_set":{"shop_money":{"amount":"14.45","currency_code":"USD"},"presentment_money":{"amount":"14.45","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:28-05:00","user_id":null,"billing_address":null,"customer":null,"discount_applications":[],"fulfillments":[],"line_items":[{"id":1071823246,"admin_graphql_api_id":"gid://shopify/LineItem/1071823246","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":1700,"name":"Red Leather Coat","price":"129.99","price_set":{"shop_money":{"amount":"129.99","currency_code":"USD"},"presentment_money":{"amount":"129.99","currency_code":"USD"}},"product_exists":false,"product_id":null,"properties":[],"quantity":1,"requires_shipping":true,"sku":null,"taxable":true,"title":"Red Leather Coat","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":null,"variant_inventory_management":null,"variant_title":null,"vendor":null,"tax_lines":[{"channel_liable":false,"price":"7.81","price_set":{"shop_money":{"amount":"7.81","currency_code":"USD"},"presentment_money":{"amount":"7.81","currency_code":"USD"}},"rate":0.06,"title":"State tax"},{"channel_liable":false,"price":"3.26","price_set":{"shop_money":{"amount":"3.26","currency_code":"USD"},"presentment_money":{"amount":"3.26","currency_code":"USD"}},"rate":0.025,"title":"County tax"}],"duties":[],"discount_allocations":[]},{"id":1071823247,"admin_graphql_api_id":"gid://shopify/LineItem/1071823247","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":750,"name":"Blue Suede Shoes","price":"85.95","price_set":{"shop_money":{"amount":"85.95","currency_code":"USD"},"presentment_money":{"amount":"85.95","currency_code":"USD"}},"product_exists":false,"product_id":null,"properties":[],"quantity":1,"requires_shipping":true,"sku":null,"taxable":false,"title":"Blue Suede Shoes","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":null,"variant_inventory_management":null,"variant_title":null,"vendor":null,"tax_lines":[],"duties":[],"discount_allocations":[]},{"id":1071823248,"admin_graphql_api_id":"gid://shopify/LineItem/1071823248","attributed_staffs":[],"current_quantity":2,"fulfillable_quantity":2,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":320,"name":"Raspberry Beret","price":"19.99","price_set":{"shop_money":{"amount":"19.99","currency_code":"USD"},"presentment_money":{"amount":"19.99","currency_code":"USD"}},"product_exists":false,"product_id":null,"properties":[],"quantity":2,"requires_shipping":true,"sku":null,"taxable":true,"title":"Raspberry Beret","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":null,"variant_inventory_management":null,"variant_title":null,"vendor":null,"tax_lines":[{"channel_liable":false,"price":"2.39","price_set":{"shop_money":{"amount":"2.39","currency_code":"USD"},"presentment_money":{"amount":"2.39","currency_code":"USD"}},"rate":0.06,"title":"State tax"},{"channel_liable":false,"price":"0.99","price_set":{"shop_money":{"amount":"0.99","currency_code":"USD"},"presentment_money":{"amount":"0.99","currency_code":"USD"}},"rate":0.025,"title":"County tax"}],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}}

  * #### Creating an order with tax lines both on line items and on the order fails and returns an error

#####

        curl -d '{"order":{"line_items":[{"title":"Clicky Keyboard","price":99.99,"grams":"600","quantity":1,"tax_lines":[{"price":1.0,"rate":0.01,"title":"Keyboard tax"}]}],"tax_lines":[{"price":6.0,"rate":0.06,"title":"State tax"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.line_items = [
          {
            "title": "Clicky Keyboard",
            "price": 99.99,
            "grams": "600",
            "quantity": 1,
            "tax_lines": [
              {
                "price": 1.0,
                "rate": 0.01,
                "title": "Keyboard tax"
              }
            ]
          }
        ];
        order.tax_lines = [
          {
            "price": 6.0,
            "rate": 0.06,
            "title": "State tax"
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.line_items = [
          {
            "title" => "Clicky Keyboard",
            "price" => 99.99,
            "grams" => "600",
            "quantity" => 1,
            "tax_lines" => [
              {
                "price" => 1.0,
                "rate" => 0.01,
                "title" => "Keyboard tax"
              }
            ]
          }
        ]
        order.tax_lines = [
          {
            "price" => 6.0,
            "rate" => 0.06,
            "title" => "State tax"
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.line_items = [
          {
            "title": "Clicky Keyboard",
            "price": 99.99,
            "grams": "600",
            "quantity": 1,
            "tax_lines": [
              {
                "price": 1.0,
                "rate": 0.01,
                "title": "Keyboard tax"
              }
            ]
          }
        ];
        order.tax_lines = [
          {
            "price": 6.0,
            "rate": 0.06,
            "title": "State tax"
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"order":["Tax lines must be associated with either order or line item but not both"]}}


* * *

##

[Anchor to POST request, Cancel an order](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-cancel)

post

Cancel an order

[orderCancel](/docs/api/admin-graphql/latest/mutations/orderCancel?example=cancel-an-order)

Requires ANY of the following access scopes: `buyer_membership_orders`, `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `buyer_membership_orders`, `orders`, `marketplace_orders`.:**

Caution

For multi-currency orders, the `currency` property is required whenever the `amount` property is provided. For more information, refer to the [_Transaction resource_](/api/admin-rest/latest/resources/transaction).

**Caution:**

For multi-currency orders, the `currency` property is required whenever the `amount` property is provided. For more information, refer to the [_Transaction resource_](/api/admin-rest/latest/resources/transaction).

Cancels an order. Orders that are paid and have fulfillments can't be canceled.

###

[Anchor to Parameters of Cancel an order](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-cancel-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

amount

string**string**

The amount to refund. If set, Shopify attempts to refund the specified amount, depending on its status. Shopify refunds through a manual gateway in cases where the original transaction was not made in Shopify. Refunds through a manual gateway are recorded as a refund on Shopify, but the customer is not refunded.

* * *

currency

The currency of the refund that's issued when the order is canceled. Required for multi-currency orders whenever the `amount` property is provided.

* * *

email

[](/apps/store/data-protection/protected-customer-data)

boolean**boolean**

default false**default false**

Whether to send an email to the customer notifying them of the cancellation.

* * *

reason

string**string**

default other**default other**

The reason for the order cancellation. Valid values: `customer`, `inventory`, `fraud`, `declined`, and `other`.)

* * *

refund

refund**refund**

The refund transactions to perform. Required for some more complex refund situations. For more information, see the [Refund API](/docs/admin-api/rest/reference/orders/refund#create-{{ current_version }}).

* * *

restock

boolean**boolean**

ISO 4217**ISO 4217**

deprecated**deprecated**

default false**default false**

Whether to restock refunded items back to your store's inventory.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-orders-order-id-cancel-examples](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-cancel-examples)Examples

Cancel an order

Path parameters

order_id=450789469

string**string**

required**required**

Cancel and refund an order using the `amount` property

Path parameters

order_id=450789469

string**string**

required**required**

Request body

amount

Amount resource**Amount resource**

Show amount properties

amount:"10.00"

string**string**

The amount to refund. If set, Shopify attempts to refund the specified amount, depending on its status. Shopify refunds through a manual gateway in cases where the original transaction was not made in Shopify. Refunds through a manual gateway are recorded as a refund on Shopify, but the customer is not refunded.

currency:"USD"

The currency of the refund that's issued when the order is canceled. Required for multi-currency orders whenever the `amount` property is provided.

Cancel and refund an order using the `refund` property

Path parameters

order_id=450789469

string**string**

required**required**

Request body

refund

Refund resource**Refund resource**

Show refund properties

refund:{"note":"Customer made a mistake","shipping":{"full_refund":true},"refund_line_items":[{"line_item_id":466157049,"quantity":1,"restock_type":"cancel","location_id":24826418}],"transactions":[{"parent_id":1068278544,"amount":"10.00","kind":"refund","gateway":"bogus"},{"parent_id":1068278545,"amount":"100.00","kind":"refund","gateway":"gift_card"}]}

refund**refund**

The refund transactions to perform. Required for some more complex refund situations. For more information, see the [Refund API](/docs/admin-api/rest/reference/orders/refund#create-{{ current_version }}).

Canceling an order that is paid and has fulfillments fails with an error

Path parameters

order_id=450789469

string**string**

required**required**

When an order has multiple refundable transactions, refunding an amount less than its net payment without a `refund` property fails with an error

Path parameters

order_id=450789469

string**string**

required**required**

Request body

amount

Amount resource**Amount resource**

Show amount properties

amount:"109.00"

string**string**

The amount to refund. If set, Shopify attempts to refund the specified amount, depending on its status. Shopify refunds through a manual gateway in cases where the original transaction was not made in Shopify. Refunds through a manual gateway are recorded as a refund on Shopify, but the customer is not refunded.

currency:"USD"

The currency of the refund that's issued when the order is canceled. Required for multi-currency orders whenever the `amount` property is provided.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders/450789469/cancel.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/cancel.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9999

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

HTTP/1.1 200 OK

{

"order": {

"id": 450789469,

"admin_graphql_api_id": "gid://shopify/Order/450789469",

"app_id": null,

"browser_ip": "0.0.0.0",

"buyer_accepts_marketing": false,

"cancel_reason": "other",

"cancelled_at": "2026-01-09T17:26:44-05:00",

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"checkout_id": 901414060,

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": null,

"browser_height": null,

"browser_ip": "0.0.0.0",

"browser_width": null,

"session_hash": null,

"user_agent": null

},

"closed_at": null,

"confirmation_number": null,

"confirmed": true,

"contact_email": "bob.norman@mail.example.com",

"created_at": "2008-01-10T11:00:00-05:00",

"currency": "USD",

"current_subtotal_price": "195.67",

"current_subtotal_price_set": {

"shop_money": {

"amount": "195.67",

"currency_code": "USD"

},

"presentment_money": {

"amount": "195.67",

"currency_code": "USD"

### examples

  * #### Cancel an order

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.cancel({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.cancel(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.cancel({});

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":"other","cancelled_at":"2026-01-09T17:26:44-05:00","cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:44-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]},"notice":"Order has been canceled"}

  * #### Cancel and refund an order using the <code>amount</code> property

#####

        curl -d '{"amount":"10.00","currency":"USD"}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.cancel({
          body: {"amount": "10.00", "currency": "USD"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.cancel(
          session: test_session,
          body: {"amount" => "10.00", "currency" => "USD"},
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.cancel({
          body: {"amount": "10.00", "currency": "USD"},
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":"other","cancelled_at":"2026-01-09T17:27:37-05:00","cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"587.00","current_subtotal_price_set":{"shop_money":{"amount":"587.00","currency_code":"USD"},"presentment_money":{"amount":"587.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"10.00","current_total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"598.94","current_total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"current_total_tax":"11.94","current_total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"598.94","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:37-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":929361473,"admin_graphql_api_id":"gid://shopify/Refund/929361473","created_at":"2026-01-09T17:27:36-05:00","note":"Order canceled","order_id":450789469,"processed_at":"2026-01-09T17:27:36-05:00","restock":false,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":null,"order_adjustments":[],"transactions":[{"id":1068278541,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278541","amount":"10.00","authorization":null,"created_at":"2026-01-09T17:27:36-05:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":"Bogus Gateway: Forced success","order_id":450789469,"parent_id":1068278540,"payment_id":"c901414060.3","processed_at":"2026-01-09T17:27:36-05:00","receipt":{},"source_name":"755357713","status":"success","test":true,"user_id":null}],"refund_line_items":[{"id":1058498321,"line_item_id":466157049,"location_id":null,"quantity":1,"restock_type":"no_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}},{"id":1058498322,"line_item_id":518995019,"location_id":null,"quantity":1,"restock_type":"no_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":1058498323,"line_item_id":703073504,"location_id":null,"quantity":1,"restock_type":"no_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]},"notice":"Order has been canceled"}

  * #### Cancel and refund an order using the <code>refund</code> property

#####

        curl -d '{"refund":{"note":"Customer made a mistake","shipping":{"full_refund":true},"refund_line_items":[{"line_item_id":466157049,"quantity":1,"restock_type":"cancel","location_id":24826418}],"transactions":[{"parent_id":1068278544,"amount":"10.00","kind":"refund","gateway":"bogus"},{"parent_id":1068278545,"amount":"100.00","kind":"refund","gateway":"gift_card"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.cancel({
          body: {"refund": {"note": "Customer made a mistake", "shipping": {"full_refund": true}, "refund_line_items": [{"line_item_id": 466157049, "quantity": 1, "restock_type": "cancel", "location_id": 24826418}], "transactions": [{"parent_id": 1068278544, "amount": "10.00", "kind": "refund", "gateway": "bogus"}, {"parent_id": 1068278545, "amount": "100.00", "kind": "refund", "gateway": "gift_card"}]}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.cancel(
          session: test_session,
          body: {"refund" => {"note" => "Customer made a mistake", "shipping" => {"full_refund" => true}, "refund_line_items" => [{"line_item_id" => 466157049, "quantity" => 1, "restock_type" => "cancel", "location_id" => 24826418}], "transactions" => [{"parent_id" => 1068278544, "amount" => "10.00", "kind" => "refund", "gateway" => "bogus"}, {"parent_id" => 1068278545, "amount" => "100.00", "kind" => "refund", "gateway" => "gift_card"}]}},
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.cancel({
          body: {"refund": {"note": "Customer made a mistake", "shipping": {"full_refund": true}, "refund_line_items": [{"line_item_id": 466157049, "quantity": 1, "restock_type": "cancel", "location_id": 24826418}], "transactions": [{"parent_id": 1068278544, "amount": "10.00", "kind": "refund", "gateway": "bogus"}, {"parent_id": 1068278545, "amount": "100.00", "kind": "refund", "gateway": "gift_card"}]}},
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":"other","cancelled_at":"2026-01-09T17:27:51-05:00","cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"587.00","current_subtotal_price_set":{"shop_money":{"amount":"587.00","currency_code":"USD"},"presentment_money":{"amount":"587.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"10.00","current_total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"598.94","current_total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"current_total_tax":"11.94","current_total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus","gift_card"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"598.94","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:51-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":929361474,"admin_graphql_api_id":"gid://shopify/Refund/929361474","created_at":"2026-01-09T17:27:50-05:00","note":"Order canceled","order_id":450789469,"processed_at":"2026-01-09T17:27:50-05:00","restock":false,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":null,"order_adjustments":[{"id":1030976845,"amount":"89.64","amount_set":{"shop_money":{"amount":"89.64","currency_code":"USD"},"presentment_money":{"amount":"89.64","currency_code":"USD"}},"kind":"refund_discrepancy","order_id":450789469,"reason":"Refund discrepancy","refund_id":929361474,"tax_amount":"0.00","tax_amount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}}}],"transactions":[{"id":1068278546,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278546","amount":"10.00","authorization":null,"created_at":"2026-01-09T17:27:50-05:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":"Bogus Gateway: Forced success","order_id":450789469,"parent_id":1068278544,"payment_id":"c901414060.4","processed_at":"2026-01-09T17:27:50-05:00","receipt":{},"source_name":"755357713","status":"success","test":true,"user_id":null},{"id":1068278547,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278547","amount":"100.00","authorization":null,"created_at":"2026-01-09T17:27:50-05:00","currency":"USD","device_id":null,"error_code":null,"gateway":"gift_card","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":1068278545,"payment_id":"c901414060.5","processed_at":"2026-01-09T17:27:50-05:00","receipt":{"gift_card_id":1035197676,"gift_card_last_characters":"0d0d"},"source_name":"755357713","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":1058498324,"line_item_id":466157049,"location_id":null,"quantity":1,"restock_type":"no_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]},"notice":"Order has been canceled"}

  * #### Canceling an order that is paid and has fulfillments fails with an error

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.cancel({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.cancel(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.cancel({});

#### response

        HTTP/1.1 422 Unprocessable Entity{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:52-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"success","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:27:52-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]},"error":"Cannot cancel a paid and fulfilled order"}

  * #### When an order has multiple refundable transactions, refunding an amount less than its net payment without a <code>refund</code> property fails with an error

#####

        curl -d '{"amount":"109.00","currency":"USD"}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.cancel({
          body: {"amount": "109.00", "currency": "USD"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.cancel(
          session: test_session,
          body: {"amount" => "109.00", "currency" => "USD"},
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.cancel({
          body: {"amount": "109.00", "currency": "USD"},
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"587.00","current_subtotal_price_set":{"shop_money":{"amount":"587.00","currency_code":"USD"},"presentment_money":{"amount":"587.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"10.00","current_total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"598.94","current_total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"current_total_tax":"11.94","current_total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus","gift_card"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"488.94","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:15-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]},"error":"Refund parameter required to process refund"}


* * *

##

[Anchor to POST request, Close an order](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-close)

post

Close an order

[orderClose](/docs/api/admin-graphql/latest/mutations/orderClose?example=close-an-order)

Requires `orders` access scope.

**Requires `orders` access scope.:**

Closes an order. A closed order is one that has no more work to be done. All items have been fulfilled or refunded.

###

[Anchor to Parameters of Close an order](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-close-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-orders-order-id-close-examples](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-close-examples)Examples

Close an order

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders/450789469/close.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/close.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9999

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

HTTP/1.1 200 OK

{

"order": {

"id": 450789469,

"admin_graphql_api_id": "gid://shopify/Order/450789469",

"app_id": null,

"browser_ip": "0.0.0.0",

"buyer_accepts_marketing": false,

"cancel_reason": null,

"cancelled_at": null,

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"checkout_id": 901414060,

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": null,

"browser_height": null,

"browser_ip": "0.0.0.0",

"browser_width": null,

"session_hash": null,

"user_agent": null

},

"closed_at": "2026-01-09T17:28:10-05:00",

"confirmation_number": null,

"confirmed": true,

"contact_email": "bob.norman@mail.example.com",

"created_at": "2008-01-10T11:00:00-05:00",

"currency": "USD",

"current_subtotal_price": "195.67",

"current_subtotal_price_set": {

"shop_money": {

"amount": "195.67",

"currency_code": "USD"

},

"presentment_money": {

"amount": "195.67",

"currency_code": "USD"

### examples

  * #### Close an order

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/close.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.close({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.close(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.close({});

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":"2026-01-09T17:28:10-05:00","confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:10-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}


* * *

##

[Anchor to POST request, Re-open a closed order](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-open)

post

Re-open a closed order

[orderOpen](/docs/api/admin-graphql/latest/mutations/orderOpen?example=re-open-a-closed-order)

Requires `orders` access scope.

**Requires `orders` access scope.:**

Re-opens a closed order

###

[Anchor to Parameters of Re-open a closed order](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-open-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-orders-order-id-open-examples](/docs/api/admin-rest/latest/resources/order#post-orders-order-id-open-examples)Examples

Re-open a closed order

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders/450789469/open.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/open.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9999

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

HTTP/1.1 200 OK

{

"order": {

"id": 450789469,

"admin_graphql_api_id": "gid://shopify/Order/450789469",

"app_id": null,

"browser_ip": "0.0.0.0",

"buyer_accepts_marketing": false,

"cancel_reason": null,

"cancelled_at": null,

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"checkout_id": 901414060,

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": null,

"browser_height": null,

"browser_ip": "0.0.0.0",

"browser_width": null,

"session_hash": null,

"user_agent": null

},

"closed_at": null,

"confirmation_number": null,

"confirmed": true,

"contact_email": "bob.norman@mail.example.com",

"created_at": "2008-01-10T11:00:00-05:00",

"currency": "USD",

"current_subtotal_price": "195.67",

"current_subtotal_price_set": {

"shop_money": {

"amount": "195.67",

"currency_code": "USD"

},

"presentment_money": {

"amount": "195.67",

"currency_code": "USD"

### examples

  * #### Re-open a closed order

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/open.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        await order.open({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.open(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        await order.open({});

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:04-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}


* * *

##

[Anchor to GET request, Retrieve a list of orders](/docs/api/admin-rest/latest/resources/order#get-orders?status=any)

get

Retrieve a list of orders

[orders](/docs/api/admin-graphql/latest/queries/orders?example=retrieve-a-list-of-orders)

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace_orders`.:**

Retrieves a list of orders that meet the specified criteria. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieve a list of orders](/docs/api/admin-rest/latest/resources/order#get-orders?status=any-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

attribution_app_id

string**string**

Show orders attributed to a certain app, specified by the app ID. Set as `current` to show orders for the app currently consuming the API.

* * *

created_at_max

date**date**

ISO 8601**ISO 8601**

Show orders created at or before date.

* * *

created_after

date**date**

ISO 8601**ISO 8601**

Show orders created at or after date.

* * *

fields

string**string**

Retrieve only certain fields, specified by a comma-separated list of fields names.

* * *

payment_status

string**string**

default any**default any**

Filter orders by their financial status.

Show payment_status properties

  * **authorized** : Show only authorized orders

  * **pending** : Show only pending orders

  * **paid** : Show only paid orders

  * **partially_paid** : Show only partially paid orders

  * **refunded** : Show only refunded orders

  * **voided** : Show only voided orders

  * **partially_refunded** : Show only partially refunded orders

  * **any** : Show orders of any financial status.

  * **unpaid** : Show authorized and partially paid orders.


* * *

shipping_status

string**string**

default any**default any**

Filter orders by their fulfillment status.

Show shipping_status properties

  * **shipped** : Show orders that have been shipped. Returns orders with `shipping_status` of `fulfilled`.

  * **partial** : Show partially shipped orders.

  * **unshipped** : Show orders that have not yet been shipped. Returns orders with `shipping_status` of `null`.

  * **any** : Show orders of any fulfillment status.

  * **unfulfilled** : Returns orders with `shipping_status` of `null` or `partial`.


* * *

ids

string**string**

Retrieve only orders specified by a comma-separated list of order IDs.

* * *

count

integer**integer**

int32**int32**

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show on a page.

* * *

name

string**string**

Filter orders by `name`.

* * *

processed_at_max

date**date**

ISO 8601**ISO 8601**

Show orders imported at or before date.

* * *

processed_at_min

date**date**

ISO 8601**ISO 8601**

Show orders imported at or after date.

* * *

Show 4 hidden fields

###

[Anchor to Response of Retrieve a list of orders](/docs/api/admin-rest/latest/resources/order#get-orders?status=any-Response)Response

* * *

Returns an array of Order objects

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders?status=any-examples](/docs/api/admin-rest/latest/resources/order#get-orders?status=any-examples)Examples

Retrieve all orders

Query parameters

status=any

enum**enum**

default open**default open**

Filter orders by their status.

Show status properties

  * **open** : Show only open orders.

  * **closed** : Show only closed orders.

  * **cancelled** : Show only canceled orders.

  * **any** : Show orders of any status, including archived orders.


Retrieve all orders after the specified ID

Query parameters

after_id=123

integer**integer**

ISO 8601**ISO 8601**

Show orders after the specified ID.

Retrieve all orders but show only certain properties

Query parameters

fields=created_at,id,name,total-price

string**string**

Retrieve only certain fields, specified by a comma-separated list of fields names.

Retrieve orders last updated after 2005-07-31 15:57:11 in the EDT timezone

Query parameters

updated_at_min=2005-07-31T15:57:11-04:00

date**date**

ISO 8601**ISO 8601**

Show orders last updated at or after date.

Retrieve orders that have authorized payments ready to be captured

Query parameters

payment_status=authorized

string**string**

default any**default any**

Filter orders by their financial status.

Show payment_status properties

  * **authorized** : Show only authorized orders

  * **pending** : Show only pending orders

  * **paid** : Show only paid orders

  * **partially_paid** : Show only partially paid orders

  * **refunded** : Show only refunded orders

  * **voided** : Show only voided orders

  * **partially_refunded** : Show only partially refunded orders

  * **any** : Show orders of any financial status.

  * **unpaid** : Show authorized and partially paid orders.


Retrieve specific orders

Query parameters

ids=1073459993

string**string**

Retrieve only orders specified by a comma-separated list of order IDs.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders.json?status=any

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?status=any" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9999

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

HTTP/1.1 200 OK

{

"orders": [

{

"id": 450789469,

"admin_graphql_api_id": "gid://shopify/Order/450789469",

"app_id": null,

"browser_ip": "0.0.0.0",

"buyer_accepts_marketing": false,

"cancel_reason": null,

"cancelled_at": null,

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"checkout_id": 901414060,

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": null,

"browser_height": null,

"browser_ip": "0.0.0.0",

"browser_width": null,

"session_hash": null,

"user_agent": null

},

"closed_at": null,

"confirmation_number": null,

"confirmed": true,

"contact_email": "bob.norman@mail.example.com",

"created_at": "2008-01-10T11:00:00-05:00",

"currency": "USD",

"current_subtotal_price": "195.67",

"current_subtotal_price_set": {

"shop_money": {

"amount": "195.67",

"currency_code": "USD"

},

"presentment_money": {

"amount": "195.67",

### examples

  * #### Retrieve all orders

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?status=any" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.all({
          session: session,
          status: "any",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.all(
          session: test_session,
          status: "any",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.all({
          session: session,
          status: "any",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}

  * #### Retrieve all orders after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?after_id=123" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.all({
          session: session,
          after_id: "123",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.all(
          session: test_session,
          after_id: "123",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.all({
          session: session,
          after_id: "123",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}

  * #### Retrieve all orders but show only certain properties

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?fields=created_at%2Cid%2Cname%2Ctotal-price" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.all({
          session: session,
          fields: "created_at,id,name,total-price",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.all(
          session: test_session,
          fields: "created_at,id,name,total-price",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.all({
          session: session,
          fields: "created_at,id,name,total-price",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"created_at":"2008-01-10T11:00:00-05:00","name":"#1001","total_price":"598.94"}]}

  * #### Retrieve orders last updated after 2005-07-31 15:57:11 in the EDT timezone

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?updated_at_min=2005-07-31T15%3A57%3A11-04%3A00" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.all({
          session: session,
          updated_at_min: "2005-07-31T15:57:11-04:00",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.all(
          session: test_session,
          updated_at_min: "2005-07-31T15:57:11-04:00",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.all({
          session: session,
          updated_at_min: "2005-07-31T15:57:11-04:00",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}

  * #### Retrieve orders that have authorized payments ready to be captured

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?payment_status=authorized" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.all({
          session: session,
          payment_status: "authorized",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.all(
          session: test_session,
          payment_status: "authorized",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.all({
          session: session,
          payment_status: "authorized",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"authorized","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:27-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}

  * #### Retrieve specific orders

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders.json?ids=1073459993" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.all({
          session: session,
          ids: "1073459993",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.all(
          session: test_session,
          ids: "1073459993",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.all({
          session: session,
          ids: "1073459993",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":1073459993,"admin_graphql_api_id":"gid://shopify/Order/1073459993","app_id":755357713,"browser_ip":null,"buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":null,"checkout_id":null,"checkout_token":null,"client_details":null,"closed_at":null,"confirmation_number":"I3VTFWLZM","confirmed":true,"contact_email":null,"created_at":"2026-01-09T17:26:48-05:00","currency":"USD","current_subtotal_price":"199.00","current_subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"0.00","current_total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.00","current_total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"current_total_tax":"0.00","current_total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[],"duties_included":false,"email":"","estimated_taxes":false,"payment_status":"paid","shipping_status":null,"landing_site":null,"landing_site_ref":null,"location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1002","note":null,"note_attributes":[],"number":2,"order_number":1002,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b7b87226d90398b993e80552447fa882/authenticate?key=4e33b13c4f27d60288878bc59f29cf09","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":[],"phone":null,"po_number":null,"presentment_currency":"USD","processed_at":"2026-01-09T17:26:48-05:00","reference":null,"referring_site":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subtotal_price":"199.00","subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[],"taxes_included":false,"test":false,"token":"b7b87226d90398b993e80552447fa882","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"0.00","total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_line_items_price":"199.00","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_outstanding":"199.00","total_price":"199.00","total_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"0.00","total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:48-05:00","user_id":null,"billing_address":null,"customer":null,"discount_applications":[],"fulfillments":[],"line_items":[{"id":1071823231,"admin_graphql_api_id":"gid://shopify/LineItem/1071823231","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":567,"name":"IPod Touch 8GB - Black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":921728736,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2009BLACK","taxable":true,"title":"IPod Touch 8GB","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":447654529,"variant_inventory_management":"shopify","variant_title":"Black","vendor":"Apple","tax_lines":[],"duties":[],"discount_allocations":[]}],"payment_terms":null,"refunds":[],"shipping_address":null,"shipping_lines":[]}]}


* * *

##

[Anchor to GET request, Retrieve a specific order](/docs/api/admin-rest/latest/resources/order#get-orders-order-id?fields=id,line-items,name,total-price)

get

Retrieve a specific order

[order](/docs/api/admin-graphql/latest/queries/order?example=retrieve-a-specific-order)

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace_orders`.:**

Retrieve an order by specifying the ID. All fields of an order are returned unless specific fields are named. The GET orders endpoint returns open orders by default.

###

[Anchor to Parameters of Retrieve a specific order](/docs/api/admin-rest/latest/resources/order#get-orders-order-id?fields=id,line-items,name,total-price-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

fields

string**string**

Retrieve only certain fields, specified by a comma-separated list of fields names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id?fields=id,line-items,name,total-price-examples](/docs/api/admin-rest/latest/resources/order#get-orders-order-id?fields=id,line-items,name,total-price-examples)Examples

Get only particular fields

Query parameters

fields=id,line_items,name,total_price

string**string**

Retrieve only certain fields, specified by a comma-separated list of fields names.

Retrieve a single order

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469.json?fields=id,line_items,name,total_price

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json?fields=id%2Cline_items%2Cname%2Ctotal_price" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

999

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

HTTP/1.1 200 OK

{

"order": {

"id": 450789469,

"name": "#1001",

"total_price": "598.94",

"line_items": [

{

"id": 466157049,

"admin_graphql_api_id": "gid://shopify/LineItem/466157049",

"current_quantity": 0,

"fulfillable_quantity": 0,

"fulfillment_service": "manual",

"shipping_status": null,

"gift_card": false,

"grams": 200,

"name": "IPod Nano - 8gb - green",

"price": "199.00",

"price_set": {

"shop_money": {

"amount": "199.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "199.00",

"currency_code": "USD"

}

},

"product_exists": true,

"product_id": 632910392,

"properties": [

{

"name": "Custom Engraving Front",

"value": "Happy Birthday"

},

{

### examples

  * #### Get only particular fields

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json?fields=id%2Cline_items%2Cname%2Ctotal_price" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.find({
          session: session,
          id: 450789469,
          fields: "id,line_items,name,total_price",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.find(
          session: test_session,
          id: 450789469,
          fields: "id,line_items,name,total_price",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.find({
          session: session,
          id: 450789469,
          fields: "id,line_items,name,total_price",
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"name":"#1001","total_price":"598.94","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}]}}

  * #### Retrieve a single order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.find({
          session: session,
          id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.find(
          session: test_session,
          id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.find({
          session: session,
          id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}


* * *

##

[Anchor to GET request, Retrieve an order count](/docs/api/admin-rest/latest/resources/order#get-orders-count?status=any)

get

Retrieve an order count

[ordersCount](/docs/api/admin-graphql/latest/queries/ordersCount?example=retrieve-an-order-count)

Requires `orders` access scope.

**Requires `orders` access scope.:**

Retrieve the total number of orders that meet the specified criteria.

###

[Anchor to Parameters of Retrieve an order count](/docs/api/admin-rest/latest/resources/order#get-orders-count?status=any-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

date**date**

ISO 8601**ISO 8601**

Orders created before date specified.

* * *

created_after

date**date**

ISO 8601**ISO 8601**

Orders created after date specified.

* * *

payment_status

string**string**

default any**default any**

Orders of a given financial status.

Show payment_status properties

  * **authorized** : Authorized orders.

  * **pending** : Pending orders.

  * **paid** : Paid orders.

  * **partially_paid** : Partially paid orders.

  * **refunded** : Refunded orders.

  * **voided** : Voided orders.

  * **partially_refunded** : Partially refunded orders.

  * **any** : Orders of any financial status.

  * **unpaid** : Authorized and partially paid orders.


* * *

shipping_status

string**string**

default any**default any**

Orders of a given fulfillment status.

Show shipping_status properties

  * **shipped** : Orders that have been shipped. Returns orders with `shipping_status` of `fulfilled`.

  * **partial** : Partially shipped orders.

  * **unshipped** : Orders that have not yet been shipped. Returns orders with `shipping_status` of `null`.

  * **any** : Orders of any fulfillment status.

  * **unfulfilled** : Orders with `shipping_status` of `null` or `partial`.


* * *

status

string**string**

default open**default open**

Orders of a given status.

Show status properties

  * **open** : Open orders.

  * **closed** : Closed orders.

  * **any** : Orders of any status.


* * *

updated_at_max

date**date**

ISO 8601**ISO 8601**

Orders last updated before date specified.

* * *

updated_at_min

date**date**

ISO 8601**ISO 8601**

Orders last updated after date specified.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-count?status=any-examples](/docs/api/admin-rest/latest/resources/order#get-orders-count?status=any-examples)Examples

Count all orders

Query parameters

status=any

string**string**

default open**default open**

Orders of a given status.

Show status properties

  * **open** : Open orders.

  * **closed** : Closed orders.

  * **any** : Orders of any status.


Count orders that have authorized payments ready to be captured

Query parameters

payment_status=authorized

string**string**

default any**default any**

Orders of a given financial status.

Show payment_status properties

  * **authorized** : Authorized orders.

  * **pending** : Pending orders.

  * **paid** : Paid orders.

  * **partially_paid** : Partially paid orders.

  * **refunded** : Refunded orders.

  * **voided** : Voided orders.

  * **partially_refunded** : Partially refunded orders.

  * **any** : Orders of any financial status.

  * **unpaid** : Authorized and partially paid orders.


Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/count.json?status=any

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/count.json?status=any" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

3

4

HTTP/1.1 200 OK

{

"count": 1

}

### examples

  * #### Count all orders

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/count.json?status=any" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.count({
          session: session,
          status: "any",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.count(
          session: test_session,
          status: "any",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.count({
          session: session,
          status: "any",
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Count orders that have authorized payments ready to be captured

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/count.json?payment_status=authorized" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.count({
          session: session,
          payment_status: "authorized",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.count(
          session: test_session,
          payment_status: "authorized",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.count({
          session: session,
          payment_status: "authorized",
        });

#### response

        HTTP/1.1 200 OK{"count":1}


* * *

##

[Anchor to PUT request, Update an order](/docs/api/admin-rest/latest/resources/order#put-orders-order-id)

put

Update an order

[orderUpdate](/docs/api/admin-graphql/latest/mutations/orderUpdate)

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace_orders`.:**

This operation allows for updating properties of an order including `buyer_accepts_marketing`, `email`, `phone`, `note`, `tags`, `metafields` and `shipping_address_attributes`.

It is not for editing the items of an order.

Note

After an order is created, you can change only a few of its attributes using the API. You can't change the items or the quantities in an order using the REST API, but you can change them using the [GraphQL Admin API](/apps/fulfillment/order-management-apps/order-editing).

**Note:**

After an order is created, you can change only a few of its attributes using the API. You can't change the items or the quantities in an order using the REST API, but you can change them using the [GraphQL Admin API](/apps/fulfillment/order-management-apps/order-editing).

###

[Anchor to Parameters of Update an order](/docs/api/admin-rest/latest/resources/order#put-orders-order-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-orders-order-id-examples](/docs/api/admin-rest/latest/resources/order#put-orders-order-id-examples)Examples

Add a metafield to an order

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

Add a note to order

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.note:"Customer contacted us about a custom engraving on this iPod"

string**string**

->[note](/docs/api/admin-graphql/latest/input-objects/OrderInput#fields-note)

An optional note that a shop owner can attach to the order.

Add note attributes to an order

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.note_attributes:[{"name":"colour","value":"red"}]

array**array**

->[customAttributes](/docs/api/admin-graphql/latest/input-objects/OrderInput#fields-customAttributes)

Extra information that is added to the order. Appears in the **Additional details** section of an order details page. Each array entry must contain a hash with `name` and `value` keys.

Change an order's email address

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.email:"a-different@email.com"[](/apps/store/data-protection/protected-customer-data)

string**string**

email**email**

->[email](/docs/api/admin-graphql/latest/input-objects/OrderInput#fields-email)

The customer's email address.

Change an order's phone number

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.phone:"+15145556677"[](/apps/store/data-protection/protected-customer-data)

string**string**

The customer's phone number for receiving SMS notifications.

Change whether the customer accepts marketing

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.buyer_accepts_marketing:true

boolean**boolean**

Whether the customer consented to receive email updates from the shop.

Remove the customer from an order

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.customer:null[](/apps/store/data-protection/protected-customer-data)

object**object**

Customer**Customer**

Information about the customer. The order might not have a customer and apps should not depend on the existence of a `customer` object. This value might be `null` if the order was created through Shopify POS. For more information about the `customer` object, see the [Customer resource](/docs/admin-api/rest/reference/customers/customer).

Update an order's tags

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.tags:"External, Inbound, Outbound"

string**string**

->[tags](/docs/api/admin-graphql/latest/input-objects/OrderInput#fields-tags)

Tags attached to the order, formatted as a string of comma-separated values. Tags are additional short descriptors, commonly used for filtering and searching. Each individual tag is limited to 40 characters in length.

Update the shipping address of an order

Path parameters

order_id=450789469

string**string**

required**required**

Request body

order[](/apps/store/data-protection/protected-customer-data)

Order resource**Order resource**

Show order properties

order.id:450789469

integer**integer**

read-only**read-only**

The ID of the order, used for API purposes. This is different from the `order_number` property, which is the ID used by the shop owner and customer.'

order.shipping_address:{"address1":"123 Ship Street","city":"Shipsville"}[](/apps/store/data-protection/protected-customer-data)

object**object**

CustomerAddress**CustomerAddress**

->[shippingAddress](/docs/api/admin-graphql/latest/input-objects/OrderInput#fields-shippingAddress)

The mailing address to where the order will be shipped. This address is optional and will not be available on orders that do not require shipping. It has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city, town, or village of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the shipping address.
  * **first_name** : The first name of the person associated with the shipping address.
  * **last_name** : The last name of the person associated with the shipping address.
  * **latitude** : The latitude of the shipping address.
  * **longitude** : The longitude of the shipping address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the region (for example, province, state, or prefecture) of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the region of the shipping address.
  * **zip** : The postal code (for example, zip, postcode, or Eircode) of the shipping address.


Was this section helpful?

YesNo

put

## /admin/api/2026-01/orders/450789469.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"order":{"id":450789469,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9999

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

HTTP/1.1 200 OK

{

"order": {

"id": 450789469,

"admin_graphql_api_id": "gid://shopify/Order/450789469",

"app_id": null,

"browser_ip": "0.0.0.0",

"buyer_accepts_marketing": false,

"cancel_reason": null,

"cancelled_at": null,

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"checkout_id": 901414060,

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": null,

"browser_height": null,

"browser_ip": "0.0.0.0",

"browser_width": null,

"session_hash": null,

"user_agent": null

},

"closed_at": null,

"confirmation_number": null,

"confirmed": true,

"contact_email": "bob.norman@mail.example.com",

"created_at": "2008-01-10T11:00:00-05:00",

"currency": "USD",

"current_subtotal_price": "195.67",

"current_subtotal_price_set": {

"shop_money": {

"amount": "195.67",

"currency_code": "USD"

},

"presentment_money": {

"amount": "195.67",

"currency_code": "USD"

### examples

  * #### Add a metafield to an order

#####

        curl -d '{"order":{"id":450789469,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.metafields = [
          {
            "key" => "new",
            "value" => "newvalue",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:28:27-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Add a note to order

#####

        curl -d '{"order":{"id":450789469,"note":"Customer contacted us about a custom engraving on this iPod"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.note = "Customer contacted us about a custom engraving on this iPod";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.note = "Customer contacted us about a custom engraving on this iPod"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.note = "Customer contacted us about a custom engraving on this iPod";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":"Customer contacted us about a custom engraving on this iPod","note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:59-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Add note attributes to an order

#####

        curl -d '{"order":{"id":450789469,"note_attributes":[{"name":"colour","value":"red"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.note_attributes = [
          {
            "name": "colour",
            "value": "red"
          }
        ];
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.note_attributes = [
          {
            "name" => "colour",
            "value" => "red"
          }
        ]
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.note_attributes = [
          {
            "name": "colour",
            "value": "red"
          }
        ];
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"colour","value":"red"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:31-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Change an order's email address

#####

        curl -d '{"order":{"id":450789469,"email":"a-different@email.com"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.email = "a-different@email.com";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.email = "a-different@email.com"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.email = "a-different@email.com";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"a-different@email.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"a-different@email.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:08-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Change an order's phone number

#####

        curl -d '{"order":{"id":450789469,"phone":"+15145556677"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.phone = "+15145556677";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.phone = "+15145556677"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.phone = "+15145556677";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+15145556677","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:58-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Change whether the customer accepts marketing

#####

        curl -d '{"order":{"id":450789469,"buyer_accepts_marketing":true}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.buyer_accepts_marketing = true;
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.buyer_accepts_marketing = true
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.buyer_accepts_marketing = true;
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":true,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:41-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Remove the customer from an order

#####

        curl -d '{"order":{"id":450789469,"customer":null}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.customer = null;
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.customer = nil
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.customer = null;
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:51-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":null,"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Update an order's tags

#####

        curl -d '{"order":{"id":450789469,"tags":"External, Inbound, Outbound"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.tags = "External, Inbound, Outbound";
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.tags = "External, Inbound, Outbound"
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.tags = "External, Inbound, Outbound";
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"External, Inbound, Outbound","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:27:06-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}

  * #### Update the shipping address of an order

#####

        curl -d '{"order":{"id":450789469,"shipping_address":{"address1":"123 Ship Street","city":"Shipsville"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order = new admin.rest.resources.Order({session: session});

        order.id = 450789469;
        order.shipping_address = {
          "address1": "123 Ship Street",
          "city": "Shipsville"
        };
        await order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order = ShopifyAPI::Order.new(session: test_session)
        order.id = 450789469
        order.shipping_address = {
          "address1" => "123 Ship Street",
          "city" => "Shipsville"
        }
        order.save!

#####

        // Session is built by the OAuth process

        const order = new shopify.rest.Order({session: session});
        order.id = 450789469;
        order.shipping_address = {
          "address1": "123 Ship Street",
          "city": "Shipsville"
        };
        await order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"order":{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2026-01-09T17:26:45-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T17:04:11-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T17:04:11-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T17:04:11-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"123 Ship Street","phone":"+1(502)-459-2181","city":"Shipsville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}}


* * *

##

[Anchor to DELETE request, Delete an order](/docs/api/admin-rest/latest/resources/order#delete-orders-order-id)

del

Delete an order

[orderDelete](/docs/api/admin-graphql/latest/mutations/orderDelete?example=delete-an-order)

Requires `orders` access scope.

**Requires `orders` access scope.:**

Deletes an order. Orders that interact with an online gateway can't be deleted.

###

[Anchor to Parameters of Delete an order](/docs/api/admin-rest/latest/resources/order#delete-orders-order-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-orders-order-id-examples](/docs/api/admin-rest/latest/resources/order#delete-orders-order-id-examples)Examples

Delete an order

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/orders/450789469.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

  * #### Delete an order

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Order.delete({
          session: session,
          id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Order.delete(
          session: test_session,
          id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Order.delete({
          session: session,
          id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{}