# DraftOrder

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/draftorder*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# DraftOrder

Ask assistant

Requires `draft_orders` access scope.

**Requires `draft_orders` access scope.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

Merchants can use draft orders to create orders on behalf of their customers. Draft orders are useful for merchants that need to do the following tasks:

  * Create new orders for sales made by phone, in person, by chat, or elsewhere. When a merchant accepts payment for a draft order, an order is created.
  * Send invoices to customers to pay with a secure checkout link.
  * Use custom items to represent additional costs or products that aren't displayed in a shop's inventory.
  * Re-create orders manually from active sales channels.
  * Sell products at discount or wholesale rates.
  * Take pre-orders.


Note

The Draft Order resource doesn't expose reserve inventory information.

**Note:**

The Draft Order resource doesn't expose reserve inventory information.

**Caution:** Only use this data if it is necessary for the intended app functionality. Shopify retains the ability to restrict access to [API Access scopes](/api/usage/access-scopes) for apps not requiring legitimate use of the associated data.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/draft_orders.json](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders)

Create a new DraftOrder

[draftOrderCreate](/docs/api/admin-graphql/latest/mutations/draftOrderCreate)

  * [post/admin/api/latest/draft_orders/{draft_order_id}/send_invoice.json](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders-draft-order-id-send-invoice)

Send an invoice

[draftOrderInvoiceSend](/docs/api/admin-graphql/latest/mutations/draftOrderInvoiceSend?example=send-an-invoice)

  * [get/admin/api/latest/draft_orders.json](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders)

Retrieves a list of draft orders

[draftOrders](/docs/api/admin-graphql/latest/queries/draftOrders?example=retrieves-a-list-of-draft-orders)

  * [get/admin/api/latest/draft_orders/{draft_order_id}.json](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-draft-order-id)

Receive a single DraftOrder

[draftOrder](/docs/api/admin-graphql/latest/queries/draftOrder?example=receive-a-single-draftorder)

  * [get/admin/api/latest/draft_orders/count.json](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-count)

Receive a count of all DraftOrders

[draftOrdersCount](/docs/api/admin-graphql/latest/queries/draftOrdersCount)

  * [put/admin/api/latest/draft_orders/{draft_order_id}.json](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id)

Modify an existing DraftOrder

[draftOrderUpdate](/docs/api/admin-graphql/latest/mutations/draftOrderUpdate?example=modify-an-existing-draftorder)

  * [put/admin/api/latest/draft_orders/{draft_order_id}/complete.json](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id-complete)

Complete a draft order

[draftOrderComplete](/docs/api/admin-graphql/latest/mutations/draftOrderComplete?example=complete-a-draft-order)

  * [del/admin/api/latest/draft_orders/{draft_order_id}.json](/docs/api/admin-rest/latest/resources/draftorder#delete-draft-orders-draft-order-id)

Remove an existing DraftOrder

[draftOrderDelete](/docs/api/admin-graphql/latest/mutations/draftOrderDelete?example=remove-an-existing-draftorder)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/draftorder#resource-object)

## The DraftOrder resource

[Anchor to ](/docs/api/admin-rest/latest/resources/draftorder#resource-object-properties)

### Properties

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.id)

The ID of the draft order.

* * *

order_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.id)

The ID of the order that's created and associated with the draft order after the draft order is completed.

* * *

name

read-only**read-only**

->[name](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.name)

Name of the draft order.

* * *

customer

->[customer](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.customer)

The customer resource, which contains information about the customer. Learn more about loading and removing customers. For more information about the `customer` resource, see the [Customer](/api/admin-rest/current/resources/customer) documentation.

* * *

shipping_address

->[shippingAddress](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.shippingAddress)

The address to ship the order to. The `shipping_address` is optional and will not be available on orders that don't require shipping. The `shipping_address` resource has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code for the country of the shipping address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the shipping address.
  * **longitude** : The longitude of the shipping address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the state or province of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the state or province of the shipping address.
  * **zip** : The zip or postal code of the shipping address.


* * *

billing_address

->[billingAddress](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.billingAddress)

The mailing address associated with the payment method. This address is an optional field that won't be available on orders that do not require a payment method. The `billing_address` resource has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1 alpha-2 two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) for the country of the billing address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the billing address.
  * **longitude** : The longitude of the billing address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the billing address region, such as province, state, or prefecture.
  * **province_code** : The alphanumeric abbreviation of the region for the billing address.
  * **zip** : The postal code of the billing address, such as zip, postcode, or Eircode.


* * *

note

->[note2](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.note2)

The text of an optional note that a merchant can attach to the draft order.

* * *

note_attributes

->[customAttributes](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.customAttributes)

The extra information that's added to the order. The information appears in the**Additional details** section of an order details page. Each array entry must contain a hash with `name` and `value` keys.

* * *

email

->[email](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.email)

The customer's email address.

* * *

currency

read-only**read-only**

->[currencyCode](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.currencyCode)

The three letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency used for the payment.

* * *

invoice_sent_at

read-only**read-only**

->[invoiceSentAt](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.invoiceSentAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the invoice was emailed to the customer.

* * *

invoice_url

read-only**read-only**

->[invoiceUrl](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.invoiceUrl)

The URL for the invoice.

* * *

Show 16 hidden fields

Was this section helpful?

YesNo

{}

## The DraftOrder resource

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

"id": 450789469,

"order_id": {

"id": 456789101

},

"name": "#1001",

"customer": {

"id": 207119551,

"email": "bob.norman@mail.example.com",

"accepts_marketing": false,

"created_at": "2012-03-13T16:09:55-04:00",

"updated_at": "2012-03-13T16:09:55-04:00",

"first_name": "Bob",

"last_name": "Norman",

"orders_count": "1",

"state": "disabled",

"total_spent": "0.00",

"last_order_id": 450789469,

"note": null,

"verified_email": true,

"multipass_identifier": null,

"tax_exempt": false,

"tax_exemptions": {},

"phone": "+13125551212",

"tags": "loyal",

"last_order_name": "#1001",

"currency": "USD",

"addresses": {},

"admin_graphql_api_id": "gid://shopify/Customer/207119551",

"default_address": {}

},

"shipping_address": {

"address1": "123 Amoebobacterieae St",

"address2": "",

"city": "Ottawa",

"company": null,

* * *

##

[Anchor to POST request, Create a new DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders)

post

Create a new DraftOrder

[draftOrderCreate](/docs/api/admin-graphql/latest/mutations/draftOrderCreate)

Creates a draft order.

Using the `DraftOrder` resource you can create orders in draft state using product variant line items, or custom line items. To create a product variant draft order, provide the `variant_id`, `quantity` and `discount` properties. To create a custom line item, provide the `title`, `price`, `taxable`, and `quantity` properties.

Note

If you are using this endpoint with a Partner development store or a trial store, then you can only create five draft orders per minute.

**Note:**

If you are using this endpoint with a Partner development store or a trial store, then you can only create five draft orders per minute.

### Polling

When you create and update draft orders some calculations are done asynchronously, such as calculating shipping and taxes. There might be times when a draft order is created but these calculations haven't completed. In these cases, you need to poll the draft order until the calculations are finished. When a draft order requires polling, a `202 accepted` response code is returned along with `location` and `retry-after` response headers. The `location` header refers to the URL to be polled, and `retry-after` denotes the interval (in seconds) at which polling requests should be sent. When the draft order is ready, a `200 OK` response code will be returned.

### About custom shipping lines

You can use the DraftOrder resource to send orders with custom shipping lines. A custom shipping line includes a `title` and `price` with `handle` set to `Nil`. A shipping line with a carrier provided shipping rate (currently set via the Shopify admin) includes the shipping rate handle.

### Applying discounts

A draft order and its line items can have one discount each. Calculations for discounts are based on the setting of the `value_type` property, which can be set to either `fixed_amount` or `percentage`. For example, you can apply a fixed amount discount to a draft order to reduce the price by the specified `value` property. When you use a percentage discount, the discount `amount` property is the price multiplied by the `value` property. For line item discounts, the `value` property is applied per individual unit of the item, based on the line item's quantity.

**Calculating line item discount amounts**

For `fixed_amount` discounts, the total `amount` corresponds to the line item quantity times the value of the discount. For percentage discounts, the total `amount` corresponds to the following:

`amount = floor(price * quantity * value) / 100`, where `floor()` is the usual round down function.

For non-fractional currencies, this formula needs to use `round()` instead of `floor()`, and the division by 100 takes place inside the rounding, resulting in a non-fractional value. Otherwise, an error is returned.

`amount = round(price * quantity * value / 100)`

**Line item examples**

_Fixed amount discount_

For a $19.99 line item with quantity of 2 and with $5 dollars off, discount amount corresponds to $10 ($5 * 2):

`applied_discount: { "value_type": "fixed_amount", "value": 5, "amount": 10 }`

_Percentage discount_

For a $19.99 line item with quantity of 2 and with 15% off, discount amount corresponds to $5.99 (floor ($19.99 * 2 * 15) / 100):

`applied_discount: { "value_type": "percentage", "value": 15, "amount": 5.99 }`

### Loading and removing customers

You can load a customer to a draft order by sending the `customer_id` as part of the draft order resource. We recommend removing a customer from a draft order by making a POST request with the `Customer` resource set to `null`, without specifying an email, shipping address, or billing address. A customer can also be removed by setting `customer`, `email`, `shipping_address`, and `billing_address` to `null`.

###

[Anchor to Parameters of Create a new DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

customer_id

Used to load the customer. When a customer is loaded, the customer’s email address is also associated.

* * *

use_customer_default_address

boolean**boolean**

default false**default false**

An optional boolean that you can send as part of a draft order resource to load customer shipping information. Valid values: true or false.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-draft-orders-examples](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders-examples)Examples

Create a draft order with a discount

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"title":"Custom Tee","price":"20.00","quantity":2}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


draft_order.applied_discount:{"description":"Custom discount","value_type":"fixed_amount","value":"10.0","amount":"10.00","title":"Custom"}

->[appliedDiscount](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-appliedDiscount)

The discount applied to the line item or the draft order resource. Each draft order resource can have one `applied_discount` resource and each draft order line item can have its own `applied_discount`. The `applied_discount` resource has the following properties:

Show applied_discount properties

  * **title** : Title of the discount.
  * **description** : Reason for the discount.
  * **value** : The value of the discount. If the type of discount is `fixed_amount`, then it corresponds to a fixed dollar amount. If the type is `percentage`, then it corresponds to percentage.
  * **value_type** : The type of discount. Valid values: `percentage`, `fixed_amount`.
  * **amount** : The applied amount of the discount, based on the setting of `value_type`. For more information, see _Applying discounts_.


draft_order.customer:{"id":207119551}

The customer resource, which contains information about the customer. Learn more about loading and removing customers. For more information about the `customer` resource, see the [Customer](/api/admin-rest/current/resources/customer) documentation.

Create a draft order with a percent discount on a line item

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"title":"Custom Tee","price":"20.00","quantity":1,"applied_discount":{"description":"Custom discount","value_type":"percentage","value":"10.0","amount":"2.0","title":"Custom"}}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


Create custom draft order

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"title":"Custom Tee","price":"20.00","quantity":2}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


draft_order.customer:{"id":207119551}

The customer resource, which contains information about the customer. Learn more about loading and removing customers. For more information about the `customer` resource, see the [Customer](/api/admin-rest/current/resources/customer) documentation.

Create draft order with custom billing address

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"variant_id":447654529,"quantity":1}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


draft_order.billing_address:{"first_name":"Bob","last_name":"Norman","address1":"123 Main St","city":"Anytown","province":"ON","country":"Canada","zip":"A1B2C3","phone":"555-555-5555"}

->[billingAddress](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-billingAddress)

The mailing address associated with the payment method. This address is an optional field that won't be available on orders that do not require a payment method. The `billing_address` resource has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1 alpha-2 two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) for the country of the billing address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the billing address.
  * **longitude** : The longitude of the billing address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the billing address region, such as province, state, or prefecture.
  * **province_code** : The alphanumeric abbreviation of the region for the billing address.
  * **zip** : The postal code of the billing address, such as zip, postcode, or Eircode.


Create draft order with custom shipping address

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"variant_id":447654529,"quantity":1}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


draft_order.shipping_address:{"first_name":"Bob","last_name":"Norman","address1":"123 Main St","city":"Anytown","province":"ON","country":"Canada","zip":"A1B2C3","phone":"555-555-5555"}

->[shippingAddress](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-shippingAddress)

The address to ship the order to. The `shipping_address` is optional and will not be available on orders that don't require shipping. The `shipping_address` resource has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code for the country of the shipping address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the shipping address.
  * **longitude** : The longitude of the shipping address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the state or province of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the state or province of the shipping address.
  * **zip** : The zip or postal code of the shipping address.


Create a draft order with a discounted line item

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"title":"Custom Tee","price":"20.00","quantity":1,"applied_discount":{"description":"Custom discount","value_type":"fixed_amount","value":"10.0","amount":"10.0","title":"Custom"}}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


Create a simple draft order with only a product variant ID.

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.line_items:[{"variant_id":447654529,"quantity":1}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


Was this section helpful?

YesNo

post

## /admin/api/2026-01/draft_orders.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"draft_order":{"line_items":[{"title":"Custom Tee","price":"20.00","quantity":2}],"applied_discount":{"description":"Custom discount","value_type":"fixed_amount","value":"10.0","amount":"10.00","title":"Custom"},"customer":{"id":207119551},"use_customer_default_address":true}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \

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

"draft_order": {

"id": 1069920487,

"note": null,

"email": "bob.norman@mail.example.com",

"taxes_included": false,

"currency": "USD",

"invoice_sent_at": null,

"created_at": "2026-01-09T17:25:56-05:00",

"updated_at": "2026-01-09T17:25:56-05:00",

"tax_exempt": false,

"completed_at": null,

"name": "#D3",

"allow_discount_codes_in_checkout?": false,

"b2b?": false,

"status": "open",

"line_items": [

{

"id": 1066630394,

"variant_id": null,

"product_id": null,

"title": "Custom Tee",

"variant_title": null,

"sku": null,

"vendor": null,

"quantity": 2,

"requires_shipping": false,

"taxable": true,

"gift_card": false,

"fulfillment_service": "manual",

"grams": 0,

"tax_lines": [

{

"rate": 0.06,

"title": "Tax",

### examples

  * #### <span id="create-a-draft-order-with-a-discount">Create a draft order with a discount</span>

#####

        curl -d '{"draft_order":{"line_items":[{"title":"Custom Tee","price":"20.00","quantity":2}],"applied_discount":{"description":"Custom discount","value_type":"fixed_amount","value":"10.0","amount":"10.00","title":"Custom"},"customer":{"id":207119551},"use_customer_default_address":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 2
          }
        ];
        draft_order.applied_discount = {
          "description": "Custom discount",
          "value_type": "fixed_amount",
          "value": "10.0",
          "amount": "10.00",
          "title": "Custom"
        };
        draft_order.customer = {
          "id": 207119551
        };
        draft_order.use_customer_default_address = true;
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "title" => "Custom Tee",
            "price" => "20.00",
            "quantity" => 2
          }
        ]
        draft_order.applied_discount = {
          "description" => "Custom discount",
          "value_type" => "fixed_amount",
          "value" => "10.0",
          "amount" => "10.00",
          "title" => "Custom"
        }
        draft_order.customer = {
          "id" => 207119551
        }
        draft_order.use_customer_default_address = true
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 2
          }
        ];
        draft_order.applied_discount = {
          "description": "Custom discount",
          "value_type": "fixed_amount",
          "value": "10.0",
          "amount": "10.00",
          "title": "Custom"
        };
        draft_order.customer = {
          "id": 207119551
        };
        draft_order.use_customer_default_address = true;
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920487,"note":null,"email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:56-05:00","updated_at":"2026-01-09T17:25:56-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630394,"variant_id":null,"product_id":null,"title":"Custom Tee","variant_title":null,"sku":null,"vendor":null,"quantity":2,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"applied_discount":null,"name":"Custom Tee","properties":[],"custom":true,"price":"20.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630394"}],"api_client_id":755357713,"shipping_address":{"first_name":null,"address1":"Chestnut Street 92","phone":"555-625-1199","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":null,"address2":"","company":null,"latitude":null,"longitude":null,"name":"","country_code":"US","province_code":"KY"},"billing_address":{"first_name":null,"address1":"Chestnut Street 92","phone":"555-625-1199","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":null,"address2":"","company":null,"latitude":null,"longitude":null,"name":"","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/25e68884f6130247915f418312a2645c","created_on_api_version_handle":"unstable","applied_discount":{"description":"Custom discount","value":"10.0","title":"Custom","amount":"10.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"tags":"","note_attributes":[],"total_price":"31.80","subtotal_price":"30.00","total_tax":"1.80","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"40.00","currency_code":"USD"},"presentment_money":{"amount":"40.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"31.80","currency_code":"USD"},"presentment_money":{"amount":"31.80","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"30.00","currency_code":"USD"},"presentment_money":{"amount":"30.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"1.80","currency_code":"USD"},"presentment_money":{"amount":"1.80","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"31.80","currency_code":"USD"},"presentment_money":{"amount":"31.80","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920487","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}

  * #### <span id="create-a-percent-discount-on-a-line-item">Create a draft order with a percent discount on a line item</span>

#####

        curl -d '{"draft_order":{"line_items":[{"title":"Custom Tee","price":"20.00","quantity":1,"applied_discount":{"description":"Custom discount","value_type":"percentage","value":"10.0","amount":"2.0","title":"Custom"}}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 1,
            "applied_discount": {
              "description": "Custom discount",
              "value_type": "percentage",
              "value": "10.0",
              "amount": "2.0",
              "title": "Custom"
            }
          }
        ];
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "title" => "Custom Tee",
            "price" => "20.00",
            "quantity" => 1,
            "applied_discount" => {
              "description" => "Custom discount",
              "value_type" => "percentage",
              "value" => "10.0",
              "amount" => "2.0",
              "title" => "Custom"
            }
          }
        ]
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 1,
            "applied_discount": {
              "description": "Custom discount",
              "value_type": "percentage",
              "value": "10.0",
              "amount": "2.0",
              "title": "Custom"
            }
          }
        ];
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920484,"note":null,"email":null,"taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:30-05:00","updated_at":"2026-01-09T17:25:30-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630390,"variant_id":null,"product_id":null,"title":"Custom Tee","variant_title":null,"sku":null,"vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.05,"title":"GST","price":"0.90"},{"rate":0.08,"title":"Tax","price":"1.44"}],"applied_discount":{"description":"Custom discount","value":"10.0","title":"Custom","amount":"2.00","value_type":"percentage"},"name":"Custom Tee","properties":[],"custom":true,"price":"20.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630390"}],"api_client_id":755357713,"shipping_address":null,"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/a5dd3fcddd1d69d509fd5f411ffa809b","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.05,"title":"GST","price":"0.90"},{"rate":0.08,"title":"Tax","price":"1.44"}],"tags":"","note_attributes":[],"total_price":"20.34","subtotal_price":"18.00","total_tax":"2.34","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"20.00","currency_code":"USD"},"presentment_money":{"amount":"20.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"20.34","currency_code":"USD"},"presentment_money":{"amount":"20.34","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"18.00","currency_code":"USD"},"presentment_money":{"amount":"18.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"2.34","currency_code":"USD"},"presentment_money":{"amount":"2.34","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"2.00","currency_code":"USD"},"presentment_money":{"amount":"2.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"20.34","currency_code":"USD"},"presentment_money":{"amount":"20.34","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920484"}}

  * #### <span id="create-custom-draft-order">Create custom draft order</span>

#####

        curl -d '{"draft_order":{"line_items":[{"title":"Custom Tee","price":"20.00","quantity":2}],"customer":{"id":207119551},"use_customer_default_address":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 2
          }
        ];
        draft_order.customer = {
          "id": 207119551
        };
        draft_order.use_customer_default_address = true;
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "title" => "Custom Tee",
            "price" => "20.00",
            "quantity" => 2
          }
        ]
        draft_order.customer = {
          "id" => 207119551
        }
        draft_order.use_customer_default_address = true
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 2
          }
        ];
        draft_order.customer = {
          "id": 207119551
        };
        draft_order.use_customer_default_address = true;
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920485,"note":null,"email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:41-05:00","updated_at":"2026-01-09T17:25:41-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630391,"variant_id":null,"product_id":null,"title":"Custom Tee","variant_title":null,"sku":null,"vendor":null,"quantity":2,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"2.40"}],"applied_discount":null,"name":"Custom Tee","properties":[],"custom":true,"price":"20.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630391"}],"api_client_id":755357713,"shipping_address":{"first_name":null,"address1":"Chestnut Street 92","phone":"555-625-1199","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":null,"address2":"","company":null,"latitude":null,"longitude":null,"name":"","country_code":"US","province_code":"KY"},"billing_address":{"first_name":null,"address1":"Chestnut Street 92","phone":"555-625-1199","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":null,"address2":"","company":null,"latitude":null,"longitude":null,"name":"","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/86a3ccad6b92a7593d574b5695f10800","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.06,"title":"Tax","price":"2.40"}],"tags":"","note_attributes":[],"total_price":"42.40","subtotal_price":"40.00","total_tax":"2.40","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"40.00","currency_code":"USD"},"presentment_money":{"amount":"40.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"42.40","currency_code":"USD"},"presentment_money":{"amount":"42.40","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"40.00","currency_code":"USD"},"presentment_money":{"amount":"40.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"2.40","currency_code":"USD"},"presentment_money":{"amount":"2.40","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"42.40","currency_code":"USD"},"presentment_money":{"amount":"42.40","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920485","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}

  * #### <span id="create-draft-order-billing-address">Create draft order with custom billing address</span>

#####

        curl -d '{"draft_order":{"line_items":[{"variant_id":447654529,"quantity":1}],"billing_address":{"first_name":"Bob","last_name":"Norman","address1":"123 Main St","city":"Anytown","province":"ON","country":"Canada","zip":"A1B2C3","phone":"555-555-5555"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        draft_order.billing_address = {
          "first_name": "Bob",
          "last_name": "Norman",
          "address1": "123 Main St",
          "city": "Anytown",
          "province": "ON",
          "country": "Canada",
          "zip": "A1B2C3",
          "phone": "555-555-5555"
        };
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        draft_order.billing_address = {
          "first_name" => "Bob",
          "last_name" => "Norman",
          "address1" => "123 Main St",
          "city" => "Anytown",
          "province" => "ON",
          "country" => "Canada",
          "zip" => "A1B2C3",
          "phone" => "555-555-5555"
        }
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        draft_order.billing_address = {
          "first_name": "Bob",
          "last_name": "Norman",
          "address1": "123 Main St",
          "city": "Anytown",
          "province": "ON",
          "country": "Canada",
          "zip": "A1B2C3",
          "phone": "555-555-5555"
        };
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920486,"note":null,"email":null,"taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:54-05:00","updated_at":"2026-01-09T17:25:54-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630393,"variant_id":447654529,"product_id":921728736,"title":"IPod Touch 8GB","variant_title":"Black","sku":"IPOD2009BLACK","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.05,"title":"GST","price":"9.95"},{"rate":0.08,"title":"Tax","price":"15.92"}],"applied_discount":null,"name":"IPod Touch 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630393"}],"api_client_id":755357713,"shipping_address":null,"billing_address":{"first_name":"Bob","address1":"123 Main St","phone":"555-555-5555","city":"Anytown","zip":"A1B2C3","province":"Ontario","country":"Canada","last_name":"Norman","address2":null,"company":null,"latitude":null,"longitude":null,"name":"Bob Norman","country_code":"CA","province_code":"ON"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/cedd3ffe868504972cd3af3f11119161","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.05,"title":"GST","price":"9.95"},{"rate":0.08,"title":"Tax","price":"15.92"}],"tags":"","note_attributes":[],"total_price":"224.87","subtotal_price":"199.00","total_tax":"25.87","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"224.87","currency_code":"USD"},"presentment_money":{"amount":"224.87","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"25.87","currency_code":"USD"},"presentment_money":{"amount":"25.87","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"224.87","currency_code":"USD"},"presentment_money":{"amount":"224.87","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920486","customer":{"id":1073339513,"created_at":"2026-01-09T17:25:54-05:00","updated_at":"2026-01-09T17:25:54-05:00","first_name":"Bob","last_name":"Norman","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":null,"phone":null,"currency":"USD","tax_exemptions":[],"email_marketing_consent":null,"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/1073339513","default_address":{"id":1053317337,"customer_id":1073339513,"first_name":"Bob","last_name":"Norman","company":null,"address1":"123 Main St","address2":null,"city":"Anytown","province":null,"country":"Canada","zip":"A1B2C3","phone":"555-555-5555","name":"Bob Norman","province_code":null,"country_code":"CA","country_name":"Canada","default":true}}}}

  * #### <span id="create-draft-order-shipping-address">Create draft order with custom shipping address</span>

#####

        curl -d '{"draft_order":{"line_items":[{"variant_id":447654529,"quantity":1}],"shipping_address":{"first_name":"Bob","last_name":"Norman","address1":"123 Main St","city":"Anytown","province":"ON","country":"Canada","zip":"A1B2C3","phone":"555-555-5555"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        draft_order.shipping_address = {
          "first_name": "Bob",
          "last_name": "Norman",
          "address1": "123 Main St",
          "city": "Anytown",
          "province": "ON",
          "country": "Canada",
          "zip": "A1B2C3",
          "phone": "555-555-5555"
        };
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        draft_order.shipping_address = {
          "first_name" => "Bob",
          "last_name" => "Norman",
          "address1" => "123 Main St",
          "city" => "Anytown",
          "province" => "ON",
          "country" => "Canada",
          "zip" => "A1B2C3",
          "phone" => "555-555-5555"
        }
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        draft_order.shipping_address = {
          "first_name": "Bob",
          "last_name": "Norman",
          "address1": "123 Main St",
          "city": "Anytown",
          "province": "ON",
          "country": "Canada",
          "zip": "A1B2C3",
          "phone": "555-555-5555"
        };
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920482,"note":null,"email":null,"taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:26-05:00","updated_at":"2026-01-09T17:25:26-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630388,"variant_id":447654529,"product_id":921728736,"title":"IPod Touch 8GB","variant_title":"Black","sku":"IPOD2009BLACK","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.05,"title":"GST","price":"9.95"},{"rate":0.08,"title":"Tax","price":"15.92"}],"applied_discount":null,"name":"IPod Touch 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630388"}],"api_client_id":755357713,"shipping_address":{"first_name":"Bob","address1":"123 Main St","phone":"555-555-5555","city":"Anytown","zip":"A1B2C3","province":"Ontario","country":"Canada","last_name":"Norman","address2":null,"company":null,"latitude":null,"longitude":null,"name":"Bob Norman","country_code":"CA","province_code":"ON"},"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/7bd1a72f87d04049a8b8bf5d20b26edf","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.05,"title":"GST","price":"9.95"},{"rate":0.08,"title":"Tax","price":"15.92"}],"tags":"","note_attributes":[],"total_price":"224.87","subtotal_price":"199.00","total_tax":"25.87","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"224.87","currency_code":"USD"},"presentment_money":{"amount":"224.87","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"25.87","currency_code":"USD"},"presentment_money":{"amount":"25.87","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"224.87","currency_code":"USD"},"presentment_money":{"amount":"224.87","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920482","customer":{"id":1073339512,"created_at":"2026-01-09T17:25:25-05:00","updated_at":"2026-01-09T17:25:25-05:00","first_name":"Bob","last_name":"Norman","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":null,"phone":null,"currency":"USD","tax_exemptions":[],"email_marketing_consent":null,"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/1073339512","default_address":{"id":1053317335,"customer_id":1073339512,"first_name":"Bob","last_name":"Norman","company":null,"address1":"123 Main St","address2":null,"city":"Anytown","province":null,"country":"Canada","zip":"A1B2C3","phone":"555-555-5555","name":"Bob Norman","province_code":null,"country_code":"CA","country_name":"Canada","default":true}}}}

  * #### Create a draft order with a discounted line item

#####

        curl -d '{"draft_order":{"line_items":[{"title":"Custom Tee","price":"20.00","quantity":1,"applied_discount":{"description":"Custom discount","value_type":"fixed_amount","value":"10.0","amount":"10.0","title":"Custom"}}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 1,
            "applied_discount": {
              "description": "Custom discount",
              "value_type": "fixed_amount",
              "value": "10.0",
              "amount": "10.0",
              "title": "Custom"
            }
          }
        ];
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "title" => "Custom Tee",
            "price" => "20.00",
            "quantity" => 1,
            "applied_discount" => {
              "description" => "Custom discount",
              "value_type" => "fixed_amount",
              "value" => "10.0",
              "amount" => "10.0",
              "title" => "Custom"
            }
          }
        ]
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "title": "Custom Tee",
            "price": "20.00",
            "quantity": 1,
            "applied_discount": {
              "description": "Custom discount",
              "value_type": "fixed_amount",
              "value": "10.0",
              "amount": "10.0",
              "title": "Custom"
            }
          }
        ];
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920483,"note":null,"email":null,"taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:28-05:00","updated_at":"2026-01-09T17:25:28-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630389,"variant_id":null,"product_id":null,"title":"Custom Tee","variant_title":null,"sku":null,"vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.05,"title":"GST","price":"0.50"},{"rate":0.08,"title":"Tax","price":"0.80"}],"applied_discount":{"description":"Custom discount","value":"10.0","title":"Custom","amount":"10.00","value_type":"fixed_amount"},"name":"Custom Tee","properties":[],"custom":true,"price":"20.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630389"}],"api_client_id":755357713,"shipping_address":null,"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f9be74df46de2e9a729baa9c3aeebe96","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.05,"title":"GST","price":"0.50"},{"rate":0.08,"title":"Tax","price":"0.80"}],"tags":"","note_attributes":[],"total_price":"11.30","subtotal_price":"10.00","total_tax":"1.30","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"20.00","currency_code":"USD"},"presentment_money":{"amount":"20.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"11.30","currency_code":"USD"},"presentment_money":{"amount":"11.30","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"1.30","currency_code":"USD"},"presentment_money":{"amount":"1.30","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"11.30","currency_code":"USD"},"presentment_money":{"amount":"11.30","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920483"}}

  * #### Create a simple draft order with only a product variant ID.

#####

        curl -d '{"draft_order":{"line_items":[{"variant_id":447654529,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"draft_order":{"id":1069920488,"note":null,"email":null,"taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:25:59-05:00","updated_at":"2026-01-09T17:25:59-05:00","tax_exempt":false,"completed_at":null,"name":"#D3","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630395,"variant_id":447654529,"product_id":921728736,"title":"IPod Touch 8GB","variant_title":"Black","sku":"IPOD2009BLACK","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.05,"title":"GST","price":"9.95"},{"rate":0.08,"title":"Tax","price":"15.92"}],"applied_discount":null,"name":"IPod Touch 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630395"}],"api_client_id":755357713,"shipping_address":null,"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/a4e6d1e44522c65b0c260623d6ddbf11","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":null,"shipping_line":null,"tax_lines":[{"rate":0.05,"title":"GST","price":"9.95"},{"rate":0.08,"title":"Tax","price":"15.92"}],"tags":"","note_attributes":[],"total_price":"224.87","subtotal_price":"199.00","total_tax":"25.87","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"224.87","currency_code":"USD"},"presentment_money":{"amount":"224.87","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"25.87","currency_code":"USD"},"presentment_money":{"amount":"25.87","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"224.87","currency_code":"USD"},"presentment_money":{"amount":"224.87","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1069920488"}}


* * *

##

[Anchor to POST request, Send an invoice](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders-draft-order-id-send-invoice)

post

Send an invoice

[draftOrderInvoiceSend](/docs/api/admin-graphql/latest/mutations/draftOrderInvoiceSend?example=send-an-invoice)

Sends an invoice for the draft order.

You can include the following parameters in the body of the request:

  * **draft_order_invoice** : The resource to send in the body of the request.
    * **to** : The email address that will populate the **to** field of the email.
    * **from** : The email address that will populate the **from** field of the email.
    * **bcc** : The list of email addresses to include in the **bcc** field of the email. Emails must be associated with staff accounts on the shop.
    * **subject** : The email subject.
    * **custom_message** : The custom message displayed in the email.


###

[Anchor to Parameters of Send an invoice](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders-draft-order-id-send-invoice-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

draft_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-draft-orders-draft-order-id-send-invoice-examples](/docs/api/admin-rest/latest/resources/draftorder#post-draft-orders-draft-order-id-send-invoice-examples)Examples

Send a customized invoice

Path parameters

draft_order_id=994118539

string**string**

required**required**

Send the default invoice

Path parameters

draft_order_id=994118539

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/draft_orders/994118539/send_invoice.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"draft_order_invoice":{"to":"first@example.com","from":"j.smith@example.com","bcc":["j.smith@example.com"],"subject":"Apple Computer Invoice","custom_message":"Thank you for ordering!"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539/send_invoice.json" \

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

HTTP/1.1 201 Created

{

"draft_order_invoice": {

"to": "first@example.com",

"from": "j.smith@example.com",

"subject": "Apple Computer Invoice",

"custom_message": "Thank you for ordering!",

"bcc": [

"j.smith@example.com"

]

}

}

### examples

  * #### Send a customized invoice

#####

        curl -d '{"draft_order_invoice":{"to":"first@example.com","from":"j.smith@example.com","bcc":["j.smith@example.com"],"subject":"Apple Computer Invoice","custom_message":"Thank you for ordering!"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539/send_invoice.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 994118539;
        await draft_order.send_invoice({
          body: {"draft_order_invoice": {"to": "first@example.com", "from": "j.smith@example.com", "bcc": ["j.smith@example.com"], "subject": "Apple Computer Invoice", "custom_message": "Thank you for ordering!"}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 994118539
        draft_order.send_invoice(
          session: test_session,
          body: {"draft_order_invoice" => {"to" => "first@example.com", "from" => "j.smith@example.com", "bcc" => ["j.smith@example.com"], "subject" => "Apple Computer Invoice", "custom_message" => "Thank you for ordering!"}},
        )

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 994118539;
        await draft_order.send_invoice({
          body: {"draft_order_invoice": {"to": "first@example.com", "from": "j.smith@example.com", "bcc": ["j.smith@example.com"], "subject": "Apple Computer Invoice", "custom_message": "Thank you for ordering!"}},
        });

#### response

        HTTP/1.1 201 Created{"draft_order_invoice":{"to":"first@example.com","from":"j.smith@example.com","subject":"Apple Computer Invoice","custom_message":"Thank you for ordering!","bcc":["j.smith@example.com"]}}

  * #### Send the default invoice

#####

        curl -d '{"draft_order_invoice":{}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539/send_invoice.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 994118539;
        await draft_order.send_invoice({
          body: {"draft_order_invoice": {}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 994118539
        draft_order.send_invoice(
          session: test_session,
          body: {"draft_order_invoice" => {}},
        )

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 994118539;
        await draft_order.send_invoice({
          body: {"draft_order_invoice": {}},
        });

#### response

        HTTP/1.1 201 Created{"draft_order_invoice":{"to":"bob.norman@mail.example.com","from":"\"John Smith Test Store\" <j.smith@example.com>","subject":"Draft Order #D2","custom_message":"","bcc":[]}}


* * *

##

[Anchor to GET request, Retrieves a list of draft orders](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders)

get

Retrieves a list of draft orders

[draftOrders](/docs/api/admin-graphql/latest/queries/draftOrders?example=retrieves-a-list-of-draft-orders)

Retrieves a list of draft orders. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of draft orders](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response

* * *

fields

comma-separated list of fields to include in the response

* * *

ids

Filter by list of IDs

* * *

count

≤ 250**≤ 250**

default 50**default 50**

Amount of results

* * *

after_id

Restrict results to after the specified ID

* * *

status

enum**enum**

default open**default open**

Filter draft orders by their status.

Show status properties

  * **open** : All open orders (default)

  * **invoice_sent** : Draft orders for which invoice has been sent to the customer

  * **completed** : Draft orders that have been completed and turned into an order


* * *

updated_at_max

Show orders last updated before date (format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Show orders last updated after date (format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-draft-orders-examples](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-examples)Examples

List all draft orders

Retrieve all draft orders after the specified ID

Query parameters

after_id=123

Restrict results to after the specified ID

Retrieve all draft orders but show only certain properties

Query parameters

fields=created_at,id,name,total-price

comma-separated list of fields to include in the response

Retrieve draft orders last updated after 2005-07-31 15:57:11 in the EDT timezone

Query parameters

updated_at_min=2005-07-31T15:57:11-04:00

Show orders last updated after date (format: 2014-04-25T16:15:47-04:00)

Was this section helpful?

YesNo

get

## /admin/api/2026-01/draft_orders.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \

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

"draft_orders": [

{

"id": 72885271,

"note": "rush order",

"email": "bob.norman@mail.example.com",

"taxes_included": false,

"currency": "USD",

"invoice_sent_at": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"tax_exempt": false,

"completed_at": null,

"name": "#D1",

"allow_discount_codes_in_checkout?": false,

"b2b?": false,

"status": "completed",

"line_items": [

{

"id": 498266019,

"variant_id": 39072856,

"product_id": 632910392,

"title": "IPod Nano - 8GB",

"variant_title": "Green",

"sku": "IPOD2008GREEN",

"vendor": "Apple",

"quantity": 2,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"fulfillment_service": "manual",

"grams": 567,

"tax_lines": [

{

"rate": 0.06,

### examples

  * #### List all draft orders

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"draft_orders":[{"id":72885271,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":498266019,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":2,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"23.88"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/498266019"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f945c7e2b158dbb69fa642cb8d79171f","created_on_api_version_handle":null,"applied_discount":null,"order_id":450789469,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"23.88"}],"tags":"","note_attributes":[],"total_price":"431.88","subtotal_price":"398.00","total_tax":"23.88","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"398.00","currency_code":"USD"},"presentment_money":{"amount":"398.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"431.88","currency_code":"USD"},"presentment_money":{"amount":"431.88","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"398.00","currency_code":"USD"},"presentment_money":{"amount":"398.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"23.88","currency_code":"USD"},"presentment_money":{"amount":"23.88","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/72885271","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":622762746,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":466157049,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/466157049"},{"id":605833968,"variant_id":null,"product_id":null,"title":"IPod Nano Engraving","variant_title":null,"sku":"IPODENGRAVING","vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"applied_discount":null,"name":"IPod Nano Engraving","properties":[],"custom":true,"price":"30.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/605833968"},{"id":783764327,"variant_id":457924702,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Black","sku":"IPOD2008BLACK","vendor":"Apple","quantity":3,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"35.82"}],"applied_discount":null,"name":"IPod Nano - 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/783764327"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6d7704cf2f0315461api","created_on_api_version_handle":null,"applied_discount":null,"order_id":null,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"},{"rate":0.06,"title":"Tax","price":"35.82"},{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"885.56","subtotal_price":"826.00","total_tax":"49.56","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"885.56","currency_code":"USD"},"presentment_money":{"amount":"885.56","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"49.56","currency_code":"USD"},"presentment_money":{"amount":"49.56","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/622762746","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":691042898,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":"2016-12-31T19:00:00-05:00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":"2016-12-31T19:00:00-05:00","name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":158115779,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/158115779"}],"api_client_id":755357713,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/56dd92fb7adc1a2c38402b1aab15b2f4","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":450789469,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"220.94","subtotal_price":"199.00","total_tax":"11.94","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"220.94","currency_code":"USD"},"presentment_money":{"amount":"220.94","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/691042898","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":994118539,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":994118539,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/994118539"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"$5promo","value":"5.0","title":"$5promo","amount":"5.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":false,"handle":"eyJhbGciOiJIUzI1NiJ9.eyJ0aXRsZSI6IlVQUyBHcm91bmQiLCJjb2RlIjoiMyIsInNvdXJjZSI6InVwcyIsInByaWNlIjoiMTIuMjUiLCJjdXJyZW5jeSI6IlVTRCIsInByaWNlX3ByZXNlbnRtZW50IjoiMTIuMjUiLCJjdXJyZW5jeV9wcmVzZW50bWVudCI6IlVTRCIsImVzdGltYXRlZF9kZWxpdmVyeV90aW1lX3JhbmdlIjpudWxsLCJncm91cF9pZCI6bnVsbH0.5rCkHw9aNgCeQZi3Tf45S-PbW9JJd6PC5ZEapMVgIYY","price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"tags":"Wholesale","note_attributes":[],"total_price":"217.89","subtotal_price":"194.00","total_tax":"11.64","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"194.00","currency_code":"USD"},"presentment_money":{"amount":"194.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.64","currency_code":"USD"},"presentment_money":{"amount":"11.64","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"12.25","currency_code":"USD"},"presentment_money":{"amount":"12.25","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":1012750869,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":294997122,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.04,"title":"GST","price":"7.96"},{"rate":0.08,"title":"Tax","price":"15.92"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/294997122"}],"api_client_id":1354745,"shipping_address":null,"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6noaddressapi","created_on_api_version_handle":null,"applied_discount":null,"order_id":null,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.04,"title":"GST","price":"7.96"},{"rate":0.08,"title":"Tax","price":"15.92"}],"tags":"","note_attributes":[],"total_price":"232.88","subtotal_price":"199.00","total_tax":"23.88","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"232.88","currency_code":"USD"},"presentment_money":{"amount":"232.88","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"23.88","currency_code":"USD"},"presentment_money":{"amount":"23.88","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1012750869"}]}

  * #### Retrieve all draft orders after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json?after_id=123" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.all({
          session: session,
          after_id: "123",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.all(
          session: test_session,
          after_id: "123",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.all({
          session: session,
          after_id: "123",
        });

#### response

        HTTP/1.1 200 OK{"draft_orders":[{"id":72885271,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":498266019,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":2,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"23.88"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/498266019"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f945c7e2b158dbb69fa642cb8d79171f","created_on_api_version_handle":null,"applied_discount":null,"order_id":450789469,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"23.88"}],"tags":"","note_attributes":[],"total_price":"431.88","subtotal_price":"398.00","total_tax":"23.88","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"398.00","currency_code":"USD"},"presentment_money":{"amount":"398.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"431.88","currency_code":"USD"},"presentment_money":{"amount":"431.88","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"398.00","currency_code":"USD"},"presentment_money":{"amount":"398.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"23.88","currency_code":"USD"},"presentment_money":{"amount":"23.88","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/72885271","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":622762746,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":466157049,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/466157049"},{"id":605833968,"variant_id":null,"product_id":null,"title":"IPod Nano Engraving","variant_title":null,"sku":"IPODENGRAVING","vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"applied_discount":null,"name":"IPod Nano Engraving","properties":[],"custom":true,"price":"30.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/605833968"},{"id":783764327,"variant_id":457924702,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Black","sku":"IPOD2008BLACK","vendor":"Apple","quantity":3,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"35.82"}],"applied_discount":null,"name":"IPod Nano - 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/783764327"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6d7704cf2f0315461api","created_on_api_version_handle":null,"applied_discount":null,"order_id":null,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"},{"rate":0.06,"title":"Tax","price":"35.82"},{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"885.56","subtotal_price":"826.00","total_tax":"49.56","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"885.56","currency_code":"USD"},"presentment_money":{"amount":"885.56","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"49.56","currency_code":"USD"},"presentment_money":{"amount":"49.56","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/622762746","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":691042898,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":"2016-12-31T19:00:00-05:00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":"2016-12-31T19:00:00-05:00","name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":158115779,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/158115779"}],"api_client_id":755357713,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/56dd92fb7adc1a2c38402b1aab15b2f4","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":450789469,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"220.94","subtotal_price":"199.00","total_tax":"11.94","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"220.94","currency_code":"USD"},"presentment_money":{"amount":"220.94","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/691042898","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":994118539,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":994118539,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/994118539"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"$5promo","value":"5.0","title":"$5promo","amount":"5.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":false,"handle":"eyJhbGciOiJIUzI1NiJ9.eyJ0aXRsZSI6IlVQUyBHcm91bmQiLCJjb2RlIjoiMyIsInNvdXJjZSI6InVwcyIsInByaWNlIjoiMTIuMjUiLCJjdXJyZW5jeSI6IlVTRCIsInByaWNlX3ByZXNlbnRtZW50IjoiMTIuMjUiLCJjdXJyZW5jeV9wcmVzZW50bWVudCI6IlVTRCIsImVzdGltYXRlZF9kZWxpdmVyeV90aW1lX3JhbmdlIjpudWxsLCJncm91cF9pZCI6bnVsbH0.5rCkHw9aNgCeQZi3Tf45S-PbW9JJd6PC5ZEapMVgIYY","price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"tags":"Wholesale","note_attributes":[],"total_price":"217.89","subtotal_price":"194.00","total_tax":"11.64","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"194.00","currency_code":"USD"},"presentment_money":{"amount":"194.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.64","currency_code":"USD"},"presentment_money":{"amount":"11.64","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"12.25","currency_code":"USD"},"presentment_money":{"amount":"12.25","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":1012750869,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":294997122,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.04,"title":"GST","price":"7.96"},{"rate":0.08,"title":"Tax","price":"15.92"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/294997122"}],"api_client_id":1354745,"shipping_address":null,"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6noaddressapi","created_on_api_version_handle":null,"applied_discount":null,"order_id":null,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.04,"title":"GST","price":"7.96"},{"rate":0.08,"title":"Tax","price":"15.92"}],"tags":"","note_attributes":[],"total_price":"232.88","subtotal_price":"199.00","total_tax":"23.88","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"232.88","currency_code":"USD"},"presentment_money":{"amount":"232.88","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"23.88","currency_code":"USD"},"presentment_money":{"amount":"23.88","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1012750869"}]}

  * #### Retrieve all draft orders but show only certain properties

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json?fields=created_at%2Cid%2Cname%2Ctotal-price" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.all({
          session: session,
          fields: "created_at,id,name,total-price",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.all(
          session: test_session,
          fields: "created_at,id,name,total-price",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.all({
          session: session,
          fields: "created_at,id,name,total-price",
        });

#### response

        HTTP/1.1 200 OK{"draft_orders":[{"id":72885271,"created_at":"2026-01-09T17:04:11-05:00","name":"#D1","total_price":"431.88"},{"id":622762746,"created_at":"2026-01-09T17:04:11-05:00","name":"#D1","total_price":"885.56"},{"id":691042898,"created_at":"2026-01-09T17:04:11-05:00","name":"#D1","total_price":"220.94"},{"id":994118539,"created_at":"2026-01-09T17:04:11-05:00","name":"#D2","total_price":"217.89"},{"id":1012750869,"created_at":"2026-01-09T17:04:11-05:00","name":"#D2","total_price":"232.88"}]}

  * #### Retrieve draft orders last updated after 2005-07-31 15:57:11 in the EDT timezone

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders.json?updated_at_min=2005-07-31T15%3A57%3A11-04%3A00" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.all({
          session: session,
          updated_at_min: "2005-07-31T15:57:11-04:00",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.all(
          session: test_session,
          updated_at_min: "2005-07-31T15:57:11-04:00",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.all({
          session: session,
          updated_at_min: "2005-07-31T15:57:11-04:00",
        });

#### response

        HTTP/1.1 200 OK{"draft_orders":[{"id":72885271,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":498266019,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":2,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"23.88"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/498266019"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f945c7e2b158dbb69fa642cb8d79171f","created_on_api_version_handle":null,"applied_discount":null,"order_id":450789469,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"23.88"}],"tags":"","note_attributes":[],"total_price":"431.88","subtotal_price":"398.00","total_tax":"23.88","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"398.00","currency_code":"USD"},"presentment_money":{"amount":"398.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"431.88","currency_code":"USD"},"presentment_money":{"amount":"431.88","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"398.00","currency_code":"USD"},"presentment_money":{"amount":"398.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"23.88","currency_code":"USD"},"presentment_money":{"amount":"23.88","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/72885271","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":622762746,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":466157049,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/466157049"},{"id":605833968,"variant_id":null,"product_id":null,"title":"IPod Nano Engraving","variant_title":null,"sku":"IPODENGRAVING","vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"applied_discount":null,"name":"IPod Nano Engraving","properties":[],"custom":true,"price":"30.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/605833968"},{"id":783764327,"variant_id":457924702,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Black","sku":"IPOD2008BLACK","vendor":"Apple","quantity":3,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"35.82"}],"applied_discount":null,"name":"IPod Nano - 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/783764327"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6d7704cf2f0315461api","created_on_api_version_handle":null,"applied_discount":null,"order_id":null,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"},{"rate":0.06,"title":"Tax","price":"35.82"},{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"885.56","subtotal_price":"826.00","total_tax":"49.56","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"885.56","currency_code":"USD"},"presentment_money":{"amount":"885.56","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"49.56","currency_code":"USD"},"presentment_money":{"amount":"49.56","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/622762746","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":691042898,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":"2016-12-31T19:00:00-05:00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":"2016-12-31T19:00:00-05:00","name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":158115779,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/158115779"}],"api_client_id":755357713,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/56dd92fb7adc1a2c38402b1aab15b2f4","created_on_api_version_handle":"unstable","applied_discount":null,"order_id":450789469,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"220.94","subtotal_price":"199.00","total_tax":"11.94","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"220.94","currency_code":"USD"},"presentment_money":{"amount":"220.94","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/691042898","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":994118539,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":994118539,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/994118539"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"$5promo","value":"5.0","title":"$5promo","amount":"5.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":false,"handle":"eyJhbGciOiJIUzI1NiJ9.eyJ0aXRsZSI6IlVQUyBHcm91bmQiLCJjb2RlIjoiMyIsInNvdXJjZSI6InVwcyIsInByaWNlIjoiMTIuMjUiLCJjdXJyZW5jeSI6IlVTRCIsInByaWNlX3ByZXNlbnRtZW50IjoiMTIuMjUiLCJjdXJyZW5jeV9wcmVzZW50bWVudCI6IlVTRCIsImVzdGltYXRlZF9kZWxpdmVyeV90aW1lX3JhbmdlIjpudWxsLCJncm91cF9pZCI6bnVsbH0.5rCkHw9aNgCeQZi3Tf45S-PbW9JJd6PC5ZEapMVgIYY","price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"tags":"Wholesale","note_attributes":[],"total_price":"217.89","subtotal_price":"194.00","total_tax":"11.64","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"194.00","currency_code":"USD"},"presentment_money":{"amount":"194.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.64","currency_code":"USD"},"presentment_money":{"amount":"11.64","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"12.25","currency_code":"USD"},"presentment_money":{"amount":"12.25","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}},{"id":1012750869,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":294997122,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.04,"title":"GST","price":"7.96"},{"rate":0.08,"title":"Tax","price":"15.92"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/294997122"}],"api_client_id":1354745,"shipping_address":null,"billing_address":null,"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6noaddressapi","created_on_api_version_handle":null,"applied_discount":null,"order_id":null,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.04,"title":"GST","price":"7.96"},{"rate":0.08,"title":"Tax","price":"15.92"}],"tags":"","note_attributes":[],"total_price":"232.88","subtotal_price":"199.00","total_tax":"23.88","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"232.88","currency_code":"USD"},"presentment_money":{"amount":"232.88","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"23.88","currency_code":"USD"},"presentment_money":{"amount":"23.88","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/1012750869"}]}


* * *

##

[Anchor to GET request, Receive a single DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-draft-order-id)

get

Receive a single DraftOrder

[draftOrder](/docs/api/admin-graphql/latest/queries/draftOrder?example=receive-a-single-draftorder)

Retrieves a specific draft order

###

[Anchor to Parameters of Receive a single DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-draft-order-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

draft_order_id

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response

* * *

Was this section helpful?

YesNo

###

[Anchor to get-draft-orders-draft-order-id-examples](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-draft-order-id-examples)Examples

Get a representation of a single draft order

Path parameters

draft_order_id=994118539

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/draft_orders/994118539.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \

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

"draft_order": {

"id": 994118539,

"note": "rush order",

"email": "bob.norman@mail.example.com",

"taxes_included": false,

"currency": "USD",

"invoice_sent_at": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"tax_exempt": false,

"completed_at": null,

"name": "#D2",

"allow_discount_codes_in_checkout?": false,

"b2b?": false,

"status": "open",

"line_items": [

{

"id": 994118539,

"variant_id": 39072856,

"product_id": 632910392,

"title": "IPod Nano - 8GB",

"variant_title": "Green",

"sku": "IPOD2008GREEN",

"vendor": "Apple",

"quantity": 1,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"fulfillment_service": "manual",

"grams": 567,

"tax_lines": [

{

"rate": 0.06,

"title": "Tax",

### examples

  * #### Get a representation of a single draft order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.find({
          session: session,
          id: 994118539,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.find(
          session: test_session,
          id: 994118539,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.find({
          session: session,
          id: 994118539,
        });

#### response

        HTTP/1.1 200 OK{"draft_order":{"id":994118539,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":994118539,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/994118539"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"$5promo","value":"5.0","title":"$5promo","amount":"5.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":false,"handle":"eyJhbGciOiJIUzI1NiJ9.eyJ0aXRsZSI6IlVQUyBHcm91bmQiLCJjb2RlIjoiMyIsInNvdXJjZSI6InVwcyIsInByaWNlIjoiMTIuMjUiLCJjdXJyZW5jeSI6IlVTRCIsInByaWNlX3ByZXNlbnRtZW50IjoiMTIuMjUiLCJjdXJyZW5jeV9wcmVzZW50bWVudCI6IlVTRCIsImVzdGltYXRlZF9kZWxpdmVyeV90aW1lX3JhbmdlIjpudWxsLCJncm91cF9pZCI6bnVsbH0.5rCkHw9aNgCeQZi3Tf45S-PbW9JJd6PC5ZEapMVgIYY","price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"tags":"Wholesale","note_attributes":[],"total_price":"217.89","subtotal_price":"194.00","total_tax":"11.64","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}


* * *

##

[Anchor to GET request, Receive a count of all DraftOrders](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-count)

get

Receive a count of all DraftOrders

[draftOrdersCount](/docs/api/admin-graphql/latest/queries/draftOrdersCount)

Retrieves a count of draft orders

###

[Anchor to Parameters of Receive a count of all DraftOrders](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

after_id

Count draft orders after the specified ID.

* * *

status

default open**default open**

Count draft orders that have a given status.

Show status properties

  * **open** : All open orders (default)

  * **invoice_sent** : Draft orders for which invoice has been sent to the customer

  * **completed** : Draft orders that have been completed and turned into an order


* * *

updated_at_max

Count draft orders last updated before the specified date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Count draft orders last updated after the specified date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-draft-orders-count-examples](/docs/api/admin-rest/latest/resources/draftorder#get-draft-orders-count-examples)Examples

Count all draft orders

Was this section helpful?

YesNo

get

## /admin/api/2026-01/draft_orders/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/count.json" \

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

"count": 5

}

### examples

  * #### Count all draft orders

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":5}


* * *

##

[Anchor to PUT request, Modify an existing DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id)

put

Modify an existing DraftOrder

[draftOrderUpdate](/docs/api/admin-graphql/latest/mutations/draftOrderUpdate?example=modify-an-existing-draftorder)

Updates a draft order.

All non read-only properties of the  DraftOrder Resource can be edited.

Caution

If a checkout has been started for a draft order, any update to the draft will unlink the checkout. Checkouts are created but not immediately completed when opening the merchant credit card modal in the admin, and when a buyer opens the invoice URL. This is usually fine, but there is an edge case where a checkout is in progress and the draft is updated before the checkout completes. This will not interfere with the checkout and order creation, but if the link from draft to checkout is broken the draft will remain open even after the order is created.

**Caution:**

If a checkout has been started for a draft order, any update to the draft will unlink the checkout. Checkouts are created but not immediately completed when opening the merchant credit card modal in the admin, and when a buyer opens the invoice URL. This is usually fine, but there is an edge case where a checkout is in progress and the draft is updated before the checkout completes. This will not interfere with the checkout and order creation, but if the link from draft to checkout is broken the draft will remain open even after the order is created.

###

[Anchor to Parameters of Modify an existing DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

draft_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-draft-orders-draft-order-id-examples](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id-examples)Examples

Set a discount on a draft order

Path parameters

draft_order_id=994118539

string**string**

required**required**

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.id:994118539

read-only**read-only**

The ID of the draft order.

draft_order.applied_discount:{"description":"Custom discount","value_type":"percentage","value":"10.0","amount":"19.90","title":"Custom"}

->[appliedDiscount](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-appliedDiscount)

The discount applied to the line item or the draft order resource. Each draft order resource can have one `applied_discount` resource and each draft order line item can have its own `applied_discount`. The `applied_discount` resource has the following properties:

Show applied_discount properties

  * **title** : Title of the discount.
  * **description** : Reason for the discount.
  * **value** : The value of the discount. If the type of discount is `fixed_amount`, then it corresponds to a fixed dollar amount. If the type is `percentage`, then it corresponds to percentage.
  * **value_type** : The type of discount. Valid values: `percentage`, `fixed_amount`.
  * **amount** : The applied amount of the discount, based on the setting of `value_type`. For more information, see _Applying discounts_.


Add a note to a draft order

Path parameters

draft_order_id=994118539

string**string**

required**required**

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.id:994118539

read-only**read-only**

The ID of the draft order.

draft_order.note:"Customer contacted us about a custom engraving on this iPod"

->[note](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-note)

The text of an optional note that a merchant can attach to the draft order.

Change a line item on a draft order

Path parameters

draft_order_id=994118539

string**string**

required**required**

Request body

draft_order[](/apps/store/data-protection/protected-customer-data)

Draft_order resource**Draft_order resource**

Show draft_order properties

draft_order.id:994118539

read-only**read-only**

The ID of the draft order.

draft_order.line_items:[{"variant_id":447654529,"quantity":1}]

->[lineItems](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#fields-lineItems)

The product variant line item or custom line item associated to the draft order. Each draft order must include at least one `line_item`. Note that Draft orders don't currently support subscriptions. Each `line_item` resource has the following properties:

Show line_items properties

  * **custom** : _Read only field_ Whether this is a custom line item or a product variant line item. If set to `true` indicates a custom line item. If set to `false` indicates a product variant line item.
  * **id** : The ID of the line item.
  * **variant_id** : The ID of the product variant corresponding to the line item. Required for a product variant line item. Set to `null` for a custom line item.
  * **product_id** : The ID of the product corresponding to the line item’s product variant.
  * **name** : The name of the product.
  * **variant_title** : The title of the product variant. Defaults to `Custom` for custom line items created via the API.
  * **vendor** : The vendor.
  * **quantity** : The number of products that were purchased.
  * **gift_card** : Indicates if the product is a gift card. Valid values: `true` or `false`.
  * **fulfillment_service** : The service provider responsible for fulfillment. Valid values are either `manual` or the name of the provider, for example amazon, shipwire. Defaults to `manual` for custom line items.
  * **properties** : An array of custom information for an item that has been added to the draft order, often used to provide [product customization options](/api/liquid/objects/line_item#line_item-properties). Copied to created order when draft order is completed.
  * **applied_discount** : The discount applied to the line item. For more information, see the `applied_discount` property.
  * **tax_lines** : _Read only field_ The calculated rate and amount of taxes for the line item.
    * **price** : The amount of tax to be charged.
    * **rate** : The rate of tax to be applied.
    * **title** : The name of the tax.
  * **title** : The title of the product or variant. Applicable only to custom line items. _Required field_.
  * **price** : The price of the item before discounts have been applied. Applicable only to custom line items. _Required field_.
  * **grams** : The weight of the item in grams. Applicable only to custom line items. If not specified, defaults to 0.
  * **requires_shipping** : Whether the fulfillment requires shipping. Applicable only to custom line items. Valid values: `true` or `false.`
  * **sku** : A unique identifier for the item in the fulfillment. Applicable only to custom line items.
  * **taxable** : Whether the product is taxable. Applicable only to custom line items.


Was this section helpful?

YesNo

put

## /admin/api/2026-01/draft_orders/994118539.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"draft_order":{"id":994118539,"applied_discount":{"description":"Custom discount","value_type":"percentage","value":"10.0","amount":"19.90","title":"Custom"}}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \

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

HTTP/1.1 200 OK

{

"draft_order": {

"id": 994118539,

"note": "rush order",

"email": "bob.norman@mail.example.com",

"taxes_included": false,

"currency": "USD",

"invoice_sent_at": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:25:33-05:00",

"tax_exempt": false,

"completed_at": null,

"name": "#D2",

"allow_discount_codes_in_checkout?": false,

"b2b?": false,

"status": "open",

"line_items": [

{

"id": 994118539,

"variant_id": 39072856,

"product_id": 632910392,

"title": "IPod Nano - 8GB",

"variant_title": "Green",

"sku": "IPOD2008GREEN",

"vendor": "Apple",

"quantity": 1,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"fulfillment_service": "manual",

"grams": 567,

"tax_lines": [

{

"rate": 0.06,

"title": "Tax",

### examples

  * #### <span id="set-discount-on-a-draft-order">Set a discount on a draft order</span>

#####

        curl -d '{"draft_order":{"id":994118539,"applied_discount":{"description":"Custom discount","value_type":"percentage","value":"10.0","amount":"19.90","title":"Custom"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 994118539;
        draft_order.applied_discount = {
          "description": "Custom discount",
          "value_type": "percentage",
          "value": "10.0",
          "amount": "19.90",
          "title": "Custom"
        };
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 994118539
        draft_order.applied_discount = {
          "description" => "Custom discount",
          "value_type" => "percentage",
          "value" => "10.0",
          "amount" => "19.90",
          "title" => "Custom"
        }
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 994118539;
        draft_order.applied_discount = {
          "description": "Custom discount",
          "value_type": "percentage",
          "value": "10.0",
          "amount": "19.90",
          "title": "Custom"
        };
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"draft_order":{"id":994118539,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:33-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":994118539,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"10.75"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/994118539"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"Custom discount","value":"10.0","title":"Custom","amount":"19.90","value_type":"percentage"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":true,"handle":null,"price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"10.75"}],"tags":"Wholesale","note_attributes":[],"total_price":"202.10","subtotal_price":"179.10","total_tax":"10.75","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"202.10","currency_code":"USD"},"presentment_money":{"amount":"202.10","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"179.10","currency_code":"USD"},"presentment_money":{"amount":"179.10","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"10.75","currency_code":"USD"},"presentment_money":{"amount":"10.75","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"19.90","currency_code":"USD"},"presentment_money":{"amount":"19.90","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"12.25","currency_code":"USD"},"presentment_money":{"amount":"12.25","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"202.10","currency_code":"USD"},"presentment_money":{"amount":"202.10","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}

  * #### Add a note to a draft order

#####

        curl -d '{"draft_order":{"id":994118539,"note":"Customer contacted us about a custom engraving on this iPod"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 994118539;
        draft_order.note = "Customer contacted us about a custom engraving on this iPod";
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 994118539
        draft_order.note = "Customer contacted us about a custom engraving on this iPod"
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 994118539;
        draft_order.note = "Customer contacted us about a custom engraving on this iPod";
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"draft_order":{"id":994118539,"note":"Customer contacted us about a custom engraving on this iPod","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:37-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":994118539,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/994118539"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"$5promo","value":"5.0","title":"$5promo","amount":"5.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":true,"handle":null,"price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"tags":"Wholesale","note_attributes":[],"total_price":"217.89","subtotal_price":"194.00","total_tax":"11.64","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"194.00","currency_code":"USD"},"presentment_money":{"amount":"194.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.64","currency_code":"USD"},"presentment_money":{"amount":"11.64","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"12.25","currency_code":"USD"},"presentment_money":{"amount":"12.25","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}

  * #### Change a line item on a draft order

#####

        curl -d '{"draft_order":{"id":994118539,"line_items":[{"variant_id":447654529,"quantity":1}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 994118539;
        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await draft_order.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 994118539
        draft_order.line_items = [
          {
            "variant_id" => 447654529,
            "quantity" => 1
          }
        ]
        draft_order.save!

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 994118539;
        draft_order.line_items = [
          {
            "variant_id": 447654529,
            "quantity": 1
          }
        ];
        await draft_order.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"draft_order":{"id":994118539,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:43-05:00","tax_exempt":false,"completed_at":null,"name":"#D2","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"open","line_items":[{"id":1066630392,"variant_id":447654529,"product_id":921728736,"title":"IPod Touch 8GB","variant_title":"Black","sku":"IPOD2009BLACK","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"applied_discount":null,"name":"IPod Touch 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/1066630392"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/ba8dcf6c022ccad3d47e3909e378e33f","created_on_api_version_handle":null,"applied_discount":{"description":"$5promo","value":"5.0","title":"$5promo","amount":"5.00","value_type":"fixed_amount"},"order_id":null,"shipping_line":{"title":"UPS Ground","custom":true,"handle":null,"price":"12.25"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.64"}],"tags":"Wholesale","note_attributes":[],"total_price":"217.89","subtotal_price":"194.00","total_tax":"11.64","payment_terms":{"id":1054663032,"payment_terms_name":"Due on receipt","payment_terms_type":"receipt","due_in_days":null,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_schedules":[{"id":247860422,"created_at":"2020-12-31T19:00:00-05:00","updated_at":"2020-12-31T19:00:00-05:00","payment_terms_id":1054663032,"reference_id":994118539,"reference_type":"DraftOrder","issued_at":null,"due_at":"2020-12-31T19:00:00-05:00","completed_at":null,"amount":"217.89","currency":"USD","total_price":"217.89","total_price_currency":"USD","balance_due":"217.89","balance_due_currency":"USD","total_balance":"217.89","total_balance_currency":"USD","outstanding_balance":"217.89","outstanding_balance_currency":"USD"}],"can_pay_early":true},"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"194.00","currency_code":"USD"},"presentment_money":{"amount":"194.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"11.64","currency_code":"USD"},"presentment_money":{"amount":"11.64","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"12.25","currency_code":"USD"},"presentment_money":{"amount":"12.25","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"217.89","currency_code":"USD"},"presentment_money":{"amount":"217.89","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/994118539","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}


* * *

##

[Anchor to PUT request, Complete a draft order](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id-complete)

put

Complete a draft order

[draftOrderComplete](/docs/api/admin-graphql/latest/mutations/draftOrderComplete?example=complete-a-draft-order)

Completes a draft order.

Using the DraftOrder resource, you can create a draft order and transition it to an order.

The following flows are supported:

  * Create a draft order that calculates taxes and totals but accept payment from the customer outside of Shopify.
  * Create a draft order and send an invoice to the customer.


###

[Anchor to Parameters of Complete a draft order](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id-complete-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

draft_order_id

string**string**

required**required**

* * *

payment_gateway_id

Sets the payment gateway ID. For more information, see the [Payments API](/docs/api/admin-rest/reference/resources/payment#create-{{ current_version }}}).

* * *

payment_pending

Sets payment pending to true or false.

Show payment_pending properties

  * **true** : The resulting order will be unpaid and can be captured later.

  * **false** : The resulting order will be marked as paid through either the default or specified gateway.


* * *

Was this section helpful?

YesNo

###

[Anchor to put-draft-orders-draft-order-id-complete-examples](/docs/api/admin-rest/latest/resources/draftorder#put-draft-orders-draft-order-id-complete-examples)Examples

Complete a draft order, marking it as paid

Path parameters

draft_order_id=622762746

string**string**

required**required**

Complete a draft order, marking it as pending

Path parameters

draft_order_id=622762746

string**string**

required**required**

Query parameters

payment_pending=true

Sets payment pending to true or false.

Show payment_pending properties

  * **true** : The resulting order will be unpaid and can be captured later.

  * **false** : The resulting order will be marked as paid through either the default or specified gateway.


Was this section helpful?

YesNo

put

## /admin/api/2026-01/draft_orders/622762746/complete.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/complete.json" \

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

"draft_order": {

"id": 622762746,

"note": "rush order",

"email": "bob.norman@mail.example.com",

"taxes_included": false,

"currency": "USD",

"invoice_sent_at": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:25:49-05:00",

"tax_exempt": false,

"completed_at": "2026-01-09T17:25:49-05:00",

"name": "#D1",

"allow_discount_codes_in_checkout?": false,

"b2b?": false,

"status": "completed",

"line_items": [

{

"id": 466157049,

"variant_id": 39072856,

"product_id": 632910392,

"title": "IPod Nano - 8GB",

"variant_title": "Green",

"sku": "IPOD2008GREEN",

"vendor": "Apple",

"quantity": 1,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"fulfillment_service": "manual",

"grams": 567,

"tax_lines": [

{

"rate": 0.06,

"title": "Tax",

### examples

  * #### Complete a draft order, marking it as paid

#####

        curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/complete.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 622762746;
        await draft_order.complete({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 622762746
        draft_order.complete(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 622762746;
        await draft_order.complete({});

#### response

        HTTP/1.1 200 OK{"draft_order":{"id":622762746,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:49-05:00","tax_exempt":false,"completed_at":"2026-01-09T17:25:49-05:00","name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":466157049,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/466157049"},{"id":605833968,"variant_id":null,"product_id":null,"title":"IPod Nano Engraving","variant_title":null,"sku":"IPODENGRAVING","vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"applied_discount":null,"name":"IPod Nano Engraving","properties":[],"custom":true,"price":"30.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/605833968"},{"id":783764327,"variant_id":457924702,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Black","sku":"IPOD2008BLACK","vendor":"Apple","quantity":3,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"35.82"}],"applied_discount":null,"name":"IPod Nano - 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/783764327"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6d7704cf2f0315461api","created_on_api_version_handle":null,"applied_discount":null,"order_id":1073459988,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"},{"rate":0.06,"title":"Tax","price":"35.82"},{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"885.56","subtotal_price":"826.00","total_tax":"49.56","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"885.56","currency_code":"USD"},"presentment_money":{"amount":"885.56","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"49.56","currency_code":"USD"},"presentment_money":{"amount":"49.56","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/622762746","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:49-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":1053317336,"customer_id":207119551,"first_name":"Bob","last_name":"Norman","company":null,"address1":"Chestnut Street 92","address2":null,"city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(502)-459-2181","name":"Bob Norman","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}

  * #### Complete a draft order, marking it as pending

#####

        curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/complete.json?payment_pending=true" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        const { admin, session } = await authenticate.admin(request);

        const draft_order = new admin.rest.resources.DraftOrder({session: session});

        draft_order.id = 622762746;
        await draft_order.complete({
          payment_pending: "true",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        draft_order = ShopifyAPI::DraftOrder.new(session: test_session)
        draft_order.id = 622762746
        draft_order.complete(
          session: test_session,
          payment_pending: "true",
        )

#####

        // Session is built by the OAuth process

        const draft_order = new shopify.rest.DraftOrder({session: session});
        draft_order.id = 622762746;
        await draft_order.complete({
          payment_pending: "true",
        });

#### response

        HTTP/1.1 200 OK{"draft_order":{"id":622762746,"note":"rush order","email":"bob.norman@mail.example.com","taxes_included":false,"currency":"USD","invoice_sent_at":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:21-05:00","tax_exempt":false,"completed_at":"2026-01-09T17:25:21-05:00","name":"#D1","allow_discount_codes_in_checkout?":false,"b2b?":false,"status":"completed","line_items":[{"id":466157049,"variant_id":39072856,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Green","sku":"IPOD2008GREEN","vendor":"Apple","quantity":1,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"11.94"}],"applied_discount":null,"name":"IPod Nano - 8GB - Green","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/466157049"},{"id":605833968,"variant_id":null,"product_id":null,"title":"IPod Nano Engraving","variant_title":null,"sku":"IPODENGRAVING","vendor":null,"quantity":1,"requires_shipping":false,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":0,"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"}],"applied_discount":null,"name":"IPod Nano Engraving","properties":[],"custom":true,"price":"30.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/605833968"},{"id":783764327,"variant_id":457924702,"product_id":632910392,"title":"IPod Nano - 8GB","variant_title":"Black","sku":"IPOD2008BLACK","vendor":"Apple","quantity":3,"requires_shipping":true,"taxable":true,"gift_card":false,"fulfillment_service":"manual","grams":567,"tax_lines":[{"rate":0.06,"title":"Tax","price":"35.82"}],"applied_discount":null,"name":"IPod Nano - 8GB - Black","properties":[],"custom":false,"price":"199.00","admin_graphql_api_id":"gid://shopify/DraftOrderLineItem/783764327"}],"api_client_id":1354745,"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"invoice_url":"https://jsmith.myshopify.com/548380009/invoices/f1df1a91d10a6d7704cf2f0315461api","created_on_api_version_handle":null,"applied_discount":null,"order_id":1073459987,"shipping_line":{"title":"custom shipping","custom":true,"handle":null,"price":"10.00"},"tax_lines":[{"rate":0.06,"title":"Tax","price":"1.80"},{"rate":0.06,"title":"Tax","price":"35.82"},{"rate":0.06,"title":"Tax","price":"11.94"}],"tags":"","note_attributes":[],"total_price":"885.56","subtotal_price":"826.00","total_tax":"49.56","payment_terms":null,"presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"885.56","currency_code":"USD"},"presentment_money":{"amount":"885.56","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"826.00","currency_code":"USD"},"presentment_money":{"amount":"826.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"49.56","currency_code":"USD"},"presentment_money":{"amount":"49.56","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_additional_fees_set":null,"total_duties_set":null,"amount_due_now_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"amount_due_later_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"admin_graphql_api_id":"gid://shopify/DraftOrder/622762746","customer":{"id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:25:21-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":1053317334,"customer_id":207119551,"first_name":"Bob","last_name":"Norman","company":null,"address1":"Chestnut Street 92","address2":null,"city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(502)-459-2181","name":"Bob Norman","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}}


* * *

##

[Anchor to DELETE request, Remove an existing DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#delete-draft-orders-draft-order-id)

del

Remove an existing DraftOrder

[draftOrderDelete](/docs/api/admin-graphql/latest/mutations/draftOrderDelete?example=remove-an-existing-draftorder)

Deletes a draft order

###

[Anchor to Parameters of Remove an existing DraftOrder](/docs/api/admin-rest/latest/resources/draftorder#delete-draft-orders-draft-order-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

draft_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-draft-orders-draft-order-id-examples](/docs/api/admin-rest/latest/resources/draftorder#delete-draft-orders-draft-order-id-examples)Examples

Permanently delete a draft order

Path parameters

draft_order_id=994118539

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/draft_orders/994118539.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \

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

  * #### Permanently delete a draft order

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/994118539.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DraftOrder.delete({
          session: session,
          id: 994118539,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DraftOrder.delete(
          session: test_session,
          id: 994118539,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DraftOrder.delete({
          session: session,
          id: 994118539,
        });

#### response

        HTTP/1.1 200 OK{}