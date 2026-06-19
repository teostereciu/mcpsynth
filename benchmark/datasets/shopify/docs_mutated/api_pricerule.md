# PriceRule

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/pricerule*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# PriceRule

Ask assistant

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Note

We recommend using the GraphQL Admin API to manage discounts. The [Discount types](/api/examples/discounts) available in the GraphQL Admin API are intended to replace the GraphQL Admin `PriceRule` object and REST Admin `PriceRule` and `DiscountCode` resources.

**Note:**

We recommend using the GraphQL Admin API to manage discounts. The [Discount types](/api/examples/discounts) available in the GraphQL Admin API are intended to replace the GraphQL Admin `PriceRule` object and REST Admin `PriceRule` and `DiscountCode` resources.

You can use the PriceRule resource to create discounts using conditions. You can then associate the conditions with a discount code by using the [DiscountCode](/docs/admin-api/rest/reference/discounts/discountcode) resource. Merchants can distribute the discount codes to their customers.

Using the PriceRule resource, you can create discounts that specify a discount as a percentage, a fixed amount, or free shipping. You use entitlements and prerequisites to dynamically build these discounts.

To learn about how to associate a price rule with a discount code, see the [DiscountCode](/docs/admin-api/rest/reference/discounts/discountcode) resource.

## Create a price rule

You can create price rules with entitlements and prerequisites. Entitlements describe the designated resources that a discount applies to, such as specific products, variants, or collections. Prerequisites describe the requirements that must be met in order for the discount to apply to the entitled resources. For example, you might want a discount to apply only to a certain shipping price range, or a certain subtotal range.

You can use entitlements, prereqisites, and other conditions to create discounts, such as the following examples:

  * $10 off the buyer's order if the total exceeds $40
  * 15% off certain collections
  * free shipping on orders over $100.00 for Canadian buyers, redeemable up to 20 times


For examples of how to create price rules, see the [POST method](/docs/admin-api/rest/reference/discounts/pricerule/#create-{{ current_version }}).

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/price_rules.json](/docs/api/admin-rest/latest/resources/pricerule#post-price-rules)

Creates a price rule

[discountCodeBasicCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate)

[discountAutomaticBasicCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate)

[discountCodeBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate)

[discountAutomaticBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate)

[discountCodeFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingCreate)

[discountAutomaticFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate)

  * [get/admin/api/latest/price_rules.json](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules)

Retrieves a list of price rules

[discountNodes](/docs/api/admin-graphql/latest/queries/discountNodes)

  * [get/admin/api/latest/price_rules/{price_rule_id}.json](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-price-rule-id)

Retrieves a single price rule

[discountNode](/docs/api/admin-graphql/latest/queries/discountNode)

  * [get/admin/api/latest/price_rules/count.json](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-count)

Retrieves a count of all price rules

[discountNodesCount](/docs/api/admin-graphql/latest/queries/discountNodesCount?example=retrieves-a-count-of-all-price-rules)

  * [put/admin/api/latest/price_rules/{price_rule_id}.json](/docs/api/admin-rest/latest/resources/pricerule#put-price-rules-price-rule-id)

Updates an existing a price rule

[discountCodeBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate)

[discountAutomaticBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate)

[discountCodeBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate)

[discountAutomaticBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate)

[discountCodeFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingUpdate)

[discountAutomaticFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate)

  * [del/admin/api/latest/price_rules/{price_rule_id}.json](/docs/api/admin-rest/latest/resources/pricerule#delete-price-rules-price-rule-id)

Remove an existing PriceRule

[discountCodeDelete](/docs/api/admin-graphql/latest/mutations/discountCodeDelete)

[discountAutomaticDelete](/docs/api/admin-graphql/latest/mutations/discountAutomaticDelete?example=remove-an-existing-pricerule)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/pricerule#resource-object)

## The PriceRule resource

[Anchor to ](/docs/api/admin-rest/latest/resources/pricerule#resource-object-properties)

### Properties

* * *

allocation_method

deprecated**deprecated**

The allocation method of the price rule. Valid values:

Show allocation_method properties

  * **each** : The discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15.
  * **across** : The calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items.


When the value of `target_type` is `shipping_line`, then this value must be `each`.

* * *

created_at

read-only**read-only**

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule was created.

* * *

updated_at

read-only**read-only**

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule was updated.

* * *

customer_selection

deprecated**deprecated**

The customer selection for the price rule. Valid values:

Show customer_selection properties

  * **all** : The price rule is valid for all customers.
  * **prerequisite** : The customer must either belong to one of the customer segments specified by `customer_segment_prerequisite_ids`, or be one of the customers specified by `prerequisite_customer_ids`.


* * *

ends_at

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule ends. Must be after `starts_at`.

* * *

entitled_collection_ids

deprecated**deprecated**

A list of IDs of collections whose products will be eligible to the discount. It can be used only with `target_type` set to `line_item` and `target_selection` set to `entitled`. It can't be used in combination with `entitled_product_ids` or `entitled_variant_ids`.

* * *

entitled_country_ids

deprecated**deprecated**

A list of IDs of shipping countries that will be entitled to the discount. It can be used only with `target_type` set to `shipping_line` and `target_selection` set to `entitled`.

* * *

entitled_product_ids

deprecated**deprecated**

A list of IDs of products that will be entitled to the discount. It can be used only with `target_type` set to `line_item` and `target_selection` set to `entitled`.

Caution

If a product variant is included in `entitled_variant_ids`, then `entitled_product_ids` can't include the ID of the product associated with that variant.

**Caution:**

If a product variant is included in `entitled_variant_ids`, then `entitled_product_ids` can't include the ID of the product associated with that variant.

* * *

entitled_variant_ids

deprecated**deprecated**

A list of IDs of product variants that will be entitled to the discount. It can be used only with `target_type` set to `line_item` and `target_selection` set to `entitled`.

Caution

If a product is included in `entitled_product_ids`, then `entitled_variant_ids` can't include the ID of any variants associated with that product.

**Caution:**

If a product is included in `entitled_product_ids`, then `entitled_variant_ids` can't include the ID of any variants associated with that product.

* * *

id

read-only**read-only**

deprecated**deprecated**

The ID for the price rule.

* * *

once_per_customer

deprecated**deprecated**

Whether the generated discount code will be valid only for a single use per customer. This is tracked using customer ID.

* * *

prerequisite_customer_ids

deprecated**deprecated**

A list of customer IDs. For the price rule to be applicable, the customer must match one of the specified [customers](/docs/admin-api/rest/reference/customers/customer).

If `prerequisite_customer_ids` is populated, then `customer_segment_prerequisite_ids` must be empty.

* * *

Show 17 hidden fields

Was this section helpful?

YesNo

{}

## The PriceRule resource

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

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

{

"allocation_method": "each",

"created_at": "2017-03-13T16:09:54-04:00",

"updated_at": "2017-03-14T16:09:54-04:00",

"customer_selection": "prerequisite",

"ends_at": "2017-04-19T17:59:10Z",

"entitled_collection_ids": [

4564654869,

8979761006

],

"entitled_country_ids": {

" entitled_country_ids": [

7897987023,

3569053679

]

},

"entitled_product_ids": [

7897397755,

42382368242

],

"entitled_variant_ids": [

6798798798,

5675765905

],

"id": 9808080986,

"once_per_customer": true,

"prerequisite_customer_ids": [

384028349005,

3492039843

],

"prerequisite_quantity_range": {

"greater_than_or_equal_to": 2

},

"customer_segment_prerequisite_ids": [

1122345432,

43535360314

],

"prerequisite_shipping_price_range": {

"less_than_or_equal_to": "10.0"

},

"prerequisite_subtotal_range": {

"greater_than_or_equal_to": "40.0"

},

"prerequisite_to_entitlement_purchase": {

"prerequisite_amount": "80.00"

},

"starts_at": "2017-01-19T17:59:10Z",

"target_selection": "entitled",

"target_type": "line_item",

"title": "SUMMERSALE10OFF",

"usage_limit": 10,

"prerequisite_product_ids": [

7897397755,

42382368242

],

"prerequisite_variant_ids": [

6798798798,

5675765905

],

"prerequisite_collection_ids": [

4564654869,

8979761006

],

"value": -35,

"value_type": "fixed_amount",

"prerequisite_to_entitlement_quantity_ratio": {

"prerequisite_quantity": 2,

"entitled_quantity": 1

},

"allocation_limit": 3

}

* * *

##

[Anchor to POST request, Creates a price rule](/docs/api/admin-rest/latest/resources/pricerule#post-price-rules)

post

Creates a price rule

[discountCodeBasicCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate)

[discountAutomaticBasicCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate)

[discountCodeBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate)

[discountAutomaticBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate)

[discountCodeFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingCreate)

[discountAutomaticFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate)

Creates a price rule

###

[Anchor to Parameters of Creates a price rule](/docs/api/admin-rest/latest/resources/pricerule#post-price-rules-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-price-rules-examples](/docs/api/admin-rest/latest/resources/pricerule#post-price-rules-examples)Examples

Create a Buy X Get Y price rule that gives one free ipod touch if customer buys 2 ipods

Request body

price_rule

Price_rule resource**Price_rule resource**

Show price_rule properties

price_rule.title:"Buy2iPodsGetiPodTouchForFree"

deprecated**deprecated**

The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the **Discounts** page of the Shopify admin for bulk discounts.

For non-bulk discounts, the discount code is displayed on the admin.

Caution

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

**Caution:**

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

price_rule.value_type:"percentage"

deprecated**deprecated**

The value type of the price rule. Valid values:

Show value_type properties

  * **fixed_amount** : Applies a discount of `value` as a unit of the store's currency. For example, if `value` is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied.
  * **percentage** : Applies a percentage discount of `value`. For example, if `value` is -30, then 30% will be deducted when the discount is applied.


If `target_type` is `shipping_line`, then only `percentage` is accepted.

price_rule.value:"-100.0"

deprecated**deprecated**

The value of the price rule. If if the value of `target_type` is `shipping_line`, then only `-100` is accepted. The value must be negative.

price_rule.customer_selection:"all"

deprecated**deprecated**

The customer selection for the price rule. Valid values:

Show customer_selection properties

  * **all** : The price rule is valid for all customers.
  * **prerequisite** : The customer must either belong to one of the customer segments specified by `customer_segment_prerequisite_ids`, or be one of the customers specified by `prerequisite_customer_ids`.


price_rule.target_type:"line_item"

deprecated**deprecated**

The target type that the price rule applies to. Valid values:

Show target_type properties

  * **line_item** : The price rule applies to the cart's line items.
  * **shipping_line** : The price rule applies to the cart's shipping lines.


price_rule.target_selection:"entitled"

deprecated**deprecated**

The target selection method of the price rule. Valid values:

Show target_selection properties

  * **all** : The price rule applies the discount to all line items in the checkout.
  * **entitled** : The price rule applies the discount to selected entitlements only.


price_rule.allocation_method:"each"

deprecated**deprecated**

The allocation method of the price rule. Valid values:

Show allocation_method properties

  * **each** : The discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15.
  * **across** : The calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items.


When the value of `target_type` is `shipping_line`, then this value must be `each`.

price_rule.starts_at:"2018-03-22T00:00:00-00:00"

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule starts.

price_rule.prerequisite_collection_ids:[841564295]

deprecated**deprecated**

List of collection ids that will be a prerequisites for a Buy X Get Y discount. The `entitled_collection_ids` can be used only with:

Show prerequisite_collection_ids properties

  * `target_type` set to `line_item`,
  * `target_selection` set to `entitled`,
  * `allocation_method` set to `each` and
  * `prerequisite_to_entitlement_quantity_ratio` defined.

Cannot be used in combination with `prerequisite_product_ids` or `prerequisite_variant_ids`.

price_rule.entitled_product_ids:[921728736]

deprecated**deprecated**

A list of IDs of products that will be entitled to the discount. It can be used only with `target_type` set to `line_item` and `target_selection` set to `entitled`.

Caution

If a product variant is included in `entitled_variant_ids`, then `entitled_product_ids` can't include the ID of the product associated with that variant.

**Caution:**

If a product variant is included in `entitled_variant_ids`, then `entitled_product_ids` can't include the ID of the product associated with that variant.

price_rule.prerequisite_to_entitlement_quantity_ratio:{"prerequisite_quantity":2,"entitled_quantity":1}

deprecated**deprecated**

Buy/Get ratio for a Buy X Get Y discount. `prerequisite_quantity` defines the necessary 'buy' quantity and `entitled_quantity` the offered 'get' quantity.

The `prerequisite_to_entitlement_quantity_ratio` can be used only with:

Show prerequisite_to_entitlement_quantity_ratio properties

  * `value_type` set to `percentage`,
  * `target_type` set to `line_item`,
  * `target_selection` set to `entitled`,
  * `allocation_method` set to `each`,
  * `prerequisite_product_ids` or `prerequisite_variant_ids` or `prerequisite_collection_ids` defined and
  * `entitled_product_ids` or `entitled_variant_ids` or `entitled_collection_ids` defined.


Caution

Cannot be used in combination with `prerequisite_subtotal_range`, `prerequisite_quantity_range` or `prerequisite_shipping_price_range`.

**Caution:**

Cannot be used in combination with `prerequisite_subtotal_range`, `prerequisite_quantity_range` or `prerequisite_shipping_price_range`.

price_rule.allocation_limit:3

deprecated**deprecated**

The number of times the discount can be allocated on the cart - if eligible. For example a Buy 1 hat Get 1 hat for free discount can be applied 3 times on a cart having more than 6 hats, where maximum of 3 hats get discounted - if the `allocation_limit` is 3. Empty (`null`) `allocation_limit` means unlimited number of allocations.

Caution

`allocation_limit` is only working with Buy X Get Y discount. The default value on creation will be `null` (unlimited).

**Caution:**

`allocation_limit` is only working with Buy X Get Y discount. The default value on creation will be `null` (unlimited).

Create a price rule that gives a select group of customers $5 off their order

Request body

price_rule

Price_rule resource**Price_rule resource**

Show price_rule properties

price_rule.title:"5OFFCUSTOMERGROUP"

deprecated**deprecated**

The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the **Discounts** page of the Shopify admin for bulk discounts.

For non-bulk discounts, the discount code is displayed on the admin.

Caution

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

**Caution:**

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

price_rule.target_type:"line_item"

deprecated**deprecated**

The target type that the price rule applies to. Valid values:

Show target_type properties

  * **line_item** : The price rule applies to the cart's line items.
  * **shipping_line** : The price rule applies to the cart's shipping lines.


price_rule.target_selection:"all"

deprecated**deprecated**

The target selection method of the price rule. Valid values:

Show target_selection properties

  * **all** : The price rule applies the discount to all line items in the checkout.
  * **entitled** : The price rule applies the discount to selected entitlements only.


price_rule.allocation_method:"across"

deprecated**deprecated**

The allocation method of the price rule. Valid values:

Show allocation_method properties

  * **each** : The discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15.
  * **across** : The calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items.


When the value of `target_type` is `shipping_line`, then this value must be `each`.

price_rule.value_type:"fixed_amount"

deprecated**deprecated**

The value type of the price rule. Valid values:

Show value_type properties

  * **fixed_amount** : Applies a discount of `value` as a unit of the store's currency. For example, if `value` is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied.
  * **percentage** : Applies a percentage discount of `value`. For example, if `value` is -30, then 30% will be deducted when the discount is applied.


If `target_type` is `shipping_line`, then only `percentage` is accepted.

price_rule.value:"-5.0"

deprecated**deprecated**

The value of the price rule. If if the value of `target_type` is `shipping_line`, then only `-100` is accepted. The value must be negative.

price_rule.customer_selection:"prerequisite"

deprecated**deprecated**

The customer selection for the price rule. Valid values:

Show customer_selection properties

  * **all** : The price rule is valid for all customers.
  * **prerequisite** : The customer must either belong to one of the customer segments specified by `customer_segment_prerequisite_ids`, or be one of the customers specified by `prerequisite_customer_ids`.


price_rule.customer_segment_prerequisite_ids:[210588551]

deprecated**deprecated**

A list of customer segment IDs. For the price rule to be applicable, the customer must be in the group of customers matching a customer segment.

If `customer_segment_prerequisite_ids` is populated, then `prerequisite_customer_ids` must be empty.

price_rule.starts_at:"2017-01-19T17:59:10Z"

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule starts.

Create a price rule that gives the buyer $10.00 off an order

Request body

price_rule

Price_rule resource**Price_rule resource**

Show price_rule properties

price_rule.title:"SUMMERSALE10OFF"

deprecated**deprecated**

The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the **Discounts** page of the Shopify admin for bulk discounts.

For non-bulk discounts, the discount code is displayed on the admin.

Caution

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

**Caution:**

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

price_rule.target_type:"line_item"

deprecated**deprecated**

The target type that the price rule applies to. Valid values:

Show target_type properties

  * **line_item** : The price rule applies to the cart's line items.
  * **shipping_line** : The price rule applies to the cart's shipping lines.


price_rule.target_selection:"all"

deprecated**deprecated**

The target selection method of the price rule. Valid values:

Show target_selection properties

  * **all** : The price rule applies the discount to all line items in the checkout.
  * **entitled** : The price rule applies the discount to selected entitlements only.


price_rule.allocation_method:"across"

deprecated**deprecated**

The allocation method of the price rule. Valid values:

Show allocation_method properties

  * **each** : The discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15.
  * **across** : The calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items.


When the value of `target_type` is `shipping_line`, then this value must be `each`.

price_rule.value_type:"fixed_amount"

deprecated**deprecated**

The value type of the price rule. Valid values:

Show value_type properties

  * **fixed_amount** : Applies a discount of `value` as a unit of the store's currency. For example, if `value` is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied.
  * **percentage** : Applies a percentage discount of `value`. For example, if `value` is -30, then 30% will be deducted when the discount is applied.


If `target_type` is `shipping_line`, then only `percentage` is accepted.

price_rule.value:"-10.0"

deprecated**deprecated**

The value of the price rule. If if the value of `target_type` is `shipping_line`, then only `-100` is accepted. The value must be negative.

price_rule.customer_selection:"all"

deprecated**deprecated**

The customer selection for the price rule. Valid values:

Show customer_selection properties

  * **all** : The price rule is valid for all customers.
  * **prerequisite** : The customer must either belong to one of the customer segments specified by `customer_segment_prerequisite_ids`, or be one of the customers specified by `prerequisite_customer_ids`.


price_rule.starts_at:"2017-01-19T17:59:10Z"

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule starts.

Create a price rule that gives the buyer 15% off a specific collection

Request body

price_rule

Price_rule resource**Price_rule resource**

Show price_rule properties

price_rule.title:"15OFFCOLLECTION"

deprecated**deprecated**

The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the **Discounts** page of the Shopify admin for bulk discounts.

For non-bulk discounts, the discount code is displayed on the admin.

Caution

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

**Caution:**

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

price_rule.target_type:"line_item"

deprecated**deprecated**

The target type that the price rule applies to. Valid values:

Show target_type properties

  * **line_item** : The price rule applies to the cart's line items.
  * **shipping_line** : The price rule applies to the cart's shipping lines.


price_rule.target_selection:"entitled"

deprecated**deprecated**

The target selection method of the price rule. Valid values:

Show target_selection properties

  * **all** : The price rule applies the discount to all line items in the checkout.
  * **entitled** : The price rule applies the discount to selected entitlements only.


price_rule.allocation_method:"across"

deprecated**deprecated**

The allocation method of the price rule. Valid values:

Show allocation_method properties

  * **each** : The discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15.
  * **across** : The calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items.


When the value of `target_type` is `shipping_line`, then this value must be `each`.

price_rule.value_type:"percentage"

deprecated**deprecated**

The value type of the price rule. Valid values:

Show value_type properties

  * **fixed_amount** : Applies a discount of `value` as a unit of the store's currency. For example, if `value` is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied.
  * **percentage** : Applies a percentage discount of `value`. For example, if `value` is -30, then 30% will be deducted when the discount is applied.


If `target_type` is `shipping_line`, then only `percentage` is accepted.

price_rule.value:"-15.0"

deprecated**deprecated**

The value of the price rule. If if the value of `target_type` is `shipping_line`, then only `-100` is accepted. The value must be negative.

price_rule.customer_selection:"all"

deprecated**deprecated**

The customer selection for the price rule. Valid values:

Show customer_selection properties

  * **all** : The price rule is valid for all customers.
  * **prerequisite** : The customer must either belong to one of the customer segments specified by `customer_segment_prerequisite_ids`, or be one of the customers specified by `prerequisite_customer_ids`.


price_rule.entitled_collection_ids:[841564295]

deprecated**deprecated**

A list of IDs of collections whose products will be eligible to the discount. It can be used only with `target_type` set to `line_item` and `target_selection` set to `entitled`. It can't be used in combination with `entitled_product_ids` or `entitled_variant_ids`.

price_rule.starts_at:"2017-01-19T17:59:10Z"

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule starts.

Create a price rule that gives the buyer free shipping on orders over $50.00 that can be used up to 20 times

Request body

price_rule

Price_rule resource**Price_rule resource**

Show price_rule properties

price_rule.title:"FREESHIPPING"

deprecated**deprecated**

The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the **Discounts** page of the Shopify admin for bulk discounts.

For non-bulk discounts, the discount code is displayed on the admin.

Caution

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

**Caution:**

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

price_rule.target_type:"shipping_line"

deprecated**deprecated**

The target type that the price rule applies to. Valid values:

Show target_type properties

  * **line_item** : The price rule applies to the cart's line items.
  * **shipping_line** : The price rule applies to the cart's shipping lines.


price_rule.target_selection:"all"

deprecated**deprecated**

The target selection method of the price rule. Valid values:

Show target_selection properties

  * **all** : The price rule applies the discount to all line items in the checkout.
  * **entitled** : The price rule applies the discount to selected entitlements only.


price_rule.allocation_method:"each"

deprecated**deprecated**

The allocation method of the price rule. Valid values:

Show allocation_method properties

  * **each** : The discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15.
  * **across** : The calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items.


When the value of `target_type` is `shipping_line`, then this value must be `each`.

price_rule.value_type:"percentage"

deprecated**deprecated**

The value type of the price rule. Valid values:

Show value_type properties

  * **fixed_amount** : Applies a discount of `value` as a unit of the store's currency. For example, if `value` is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied.
  * **percentage** : Applies a percentage discount of `value`. For example, if `value` is -30, then 30% will be deducted when the discount is applied.


If `target_type` is `shipping_line`, then only `percentage` is accepted.

price_rule.value:"-100.0"

deprecated**deprecated**

The value of the price rule. If if the value of `target_type` is `shipping_line`, then only `-100` is accepted. The value must be negative.

price_rule.usage_limit:20

deprecated**deprecated**

The maximum number of times the price rule can be used, per discount code.

price_rule.customer_selection:"all"

deprecated**deprecated**

The customer selection for the price rule. Valid values:

Show customer_selection properties

  * **all** : The price rule is valid for all customers.
  * **prerequisite** : The customer must either belong to one of the customer segments specified by `customer_segment_prerequisite_ids`, or be one of the customers specified by `prerequisite_customer_ids`.


price_rule.prerequisite_subtotal_range:{"greater_than_or_equal_to":"50.0"}

deprecated**deprecated**

The minimum subtotal for the price rule to be applicable. It has the following property:

Show prerequisite_subtotal_range properties

  * **greater_than_or_equal_to** : The subtotal of the entitled cart items must be greater than or equal to this value for the discount to apply.


price_rule.starts_at:"2017-01-19T17:59:10Z"

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the price rule starts.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/price_rules.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"price_rule":{"title":"Buy2iPodsGetiPodTouchForFree","value_type":"percentage","value":"-100.0","customer_selection":"all","target_type":"line_item","target_selection":"entitled","allocation_method":"each","starts_at":"2018-03-22T00:00:00-00:00","prerequisite_collection_ids":[841564295],"entitled_product_ids":[921728736],"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":2,"entitled_quantity":1},"allocation_limit":3}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \

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

HTTP/1.1 201 Created

{

"price_rule": {

"id": 1057856659,

"value_type": "percentage",

"value": "-100.0",

"customer_selection": "all",

"target_type": "line_item",

"target_selection": "entitled",

"allocation_method": "each",

"allocation_limit": 3,

"once_per_customer": false,

"usage_limit": null,

"starts_at": "2018-03-21T20:00:00-04:00",

"ends_at": null,

"created_at": "2026-01-09T19:37:12-05:00",

"updated_at": "2026-01-09T19:37:12-05:00",

"entitled_product_ids": [

921728736

],

"entitled_variant_ids": [],

"entitled_collection_ids": [],

"entitled_country_ids": [],

"prerequisite_product_ids": [],

"prerequisite_variant_ids": [],

"prerequisite_collection_ids": [

841564295

],

"customer_segment_prerequisite_ids": [],

"prerequisite_customer_ids": [],

"prerequisite_subtotal_range": null,

"prerequisite_quantity_range": null,

"prerequisite_shipping_price_range": null,

"prerequisite_to_entitlement_quantity_ratio": {

"prerequisite_quantity": 2,

"entitled_quantity": 1

},

"prerequisite_to_entitlement_purchase": {

"prerequisite_amount": null

},

"title": "Buy2iPodsGetiPodTouchForFree",

"admin_graphql_api_id": "gid://shopify/PriceRule/1057856659"

}

}

### examples

  * #### Create a Buy X Get Y price rule that gives one free ipod touch if customer buys 2 ipods

#####

        curl -d '{"price_rule":{"title":"Buy2iPodsGetiPodTouchForFree","value_type":"percentage","value":"-100.0","customer_selection":"all","target_type":"line_item","target_selection":"entitled","allocation_method":"each","starts_at":"2018-03-22T00:00:00-00:00","prerequisite_collection_ids":[841564295],"entitled_product_ids":[921728736],"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":2,"entitled_quantity":1},"allocation_limit":3}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const price_rule = new admin.rest.resources.PriceRule({session: session});

        price_rule.title = "Buy2iPodsGetiPodTouchForFree";
        price_rule.value_type = "percentage";
        price_rule.value = "-100.0";
        price_rule.customer_selection = "all";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "entitled";
        price_rule.allocation_method = "each";
        price_rule.starts_at = "2018-03-22T00:00:00-00:00";
        price_rule.prerequisite_collection_ids = [
          841564295
        ];
        price_rule.entitled_product_ids = [
          921728736
        ];
        price_rule.prerequisite_to_entitlement_quantity_ratio = {
          "prerequisite_quantity": 2,
          "entitled_quantity": 1
        };
        price_rule.allocation_limit = 3;
        await price_rule.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        price_rule = ShopifyAPI::PriceRule.new(session: test_session)
        price_rule.title = "Buy2iPodsGetiPodTouchForFree"
        price_rule.value_type = "percentage"
        price_rule.value = "-100.0"
        price_rule.customer_selection = "all"
        price_rule.target_type = "line_item"
        price_rule.target_selection = "entitled"
        price_rule.allocation_method = "each"
        price_rule.starts_at = "2018-03-22T00:00:00-00:00"
        price_rule.prerequisite_collection_ids = [
          841564295
        ]
        price_rule.entitled_product_ids = [
          921728736
        ]
        price_rule.prerequisite_to_entitlement_quantity_ratio = {
          "prerequisite_quantity" => 2,
          "entitled_quantity" => 1
        }
        price_rule.allocation_limit = 3
        price_rule.save!

#####

        // Session is built by the OAuth process

        const price_rule = new shopify.rest.PriceRule({session: session});
        price_rule.title = "Buy2iPodsGetiPodTouchForFree";
        price_rule.value_type = "percentage";
        price_rule.value = "-100.0";
        price_rule.customer_selection = "all";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "entitled";
        price_rule.allocation_method = "each";
        price_rule.starts_at = "2018-03-22T00:00:00-00:00";
        price_rule.prerequisite_collection_ids = [
          841564295
        ];
        price_rule.entitled_product_ids = [
          921728736
        ];
        price_rule.prerequisite_to_entitlement_quantity_ratio = {
          "prerequisite_quantity": 2,
          "entitled_quantity": 1
        };
        price_rule.allocation_limit = 3;
        await price_rule.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"price_rule":{"id":1057856659,"value_type":"percentage","value":"-100.0","customer_selection":"all","target_type":"line_item","target_selection":"entitled","allocation_method":"each","allocation_limit":3,"once_per_customer":false,"usage_limit":null,"starts_at":"2018-03-21T20:00:00-04:00","ends_at":null,"created_at":"2026-01-09T19:37:12-05:00","updated_at":"2026-01-09T19:37:12-05:00","entitled_product_ids":[921728736],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[841564295],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":2,"entitled_quantity":1},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"Buy2iPodsGetiPodTouchForFree","admin_graphql_api_id":"gid://shopify/PriceRule/1057856659"}}

  * #### Create a price rule that gives a select group of customers $5 off their order

#####

        curl -d '{"price_rule":{"title":"5OFFCUSTOMERGROUP","target_type":"line_item","target_selection":"all","allocation_method":"across","value_type":"fixed_amount","value":"-5.0","customer_selection":"prerequisite","customer_segment_prerequisite_ids":[210588551],"starts_at":"2017-01-19T17:59:10Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const price_rule = new admin.rest.resources.PriceRule({session: session});

        price_rule.title = "5OFFCUSTOMERGROUP";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "all";
        price_rule.allocation_method = "across";
        price_rule.value_type = "fixed_amount";
        price_rule.value = "-5.0";
        price_rule.customer_selection = "prerequisite";
        price_rule.customer_segment_prerequisite_ids = [
          210588551
        ];
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        price_rule = ShopifyAPI::PriceRule.new(session: test_session)
        price_rule.title = "5OFFCUSTOMERGROUP"
        price_rule.target_type = "line_item"
        price_rule.target_selection = "all"
        price_rule.allocation_method = "across"
        price_rule.value_type = "fixed_amount"
        price_rule.value = "-5.0"
        price_rule.customer_selection = "prerequisite"
        price_rule.customer_segment_prerequisite_ids = [
          210588551
        ]
        price_rule.starts_at = "2017-01-19T17:59:10Z"
        price_rule.save!

#####

        // Session is built by the OAuth process

        const price_rule = new shopify.rest.PriceRule({session: session});
        price_rule.title = "5OFFCUSTOMERGROUP";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "all";
        price_rule.allocation_method = "across";
        price_rule.value_type = "fixed_amount";
        price_rule.value = "-5.0";
        price_rule.customer_selection = "prerequisite";
        price_rule.customer_segment_prerequisite_ids = [
          210588551
        ];
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"customer_segment_prerequisite_ids":["segment with id: 210588551 is invalid"]}}

  * #### Create a price rule that gives the buyer $10.00 off an order

#####

        curl -d '{"price_rule":{"title":"SUMMERSALE10OFF","target_type":"line_item","target_selection":"all","allocation_method":"across","value_type":"fixed_amount","value":"-10.0","customer_selection":"all","starts_at":"2017-01-19T17:59:10Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const price_rule = new admin.rest.resources.PriceRule({session: session});

        price_rule.title = "SUMMERSALE10OFF";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "all";
        price_rule.allocation_method = "across";
        price_rule.value_type = "fixed_amount";
        price_rule.value = "-10.0";
        price_rule.customer_selection = "all";
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        price_rule = ShopifyAPI::PriceRule.new(session: test_session)
        price_rule.title = "SUMMERSALE10OFF"
        price_rule.target_type = "line_item"
        price_rule.target_selection = "all"
        price_rule.allocation_method = "across"
        price_rule.value_type = "fixed_amount"
        price_rule.value = "-10.0"
        price_rule.customer_selection = "all"
        price_rule.starts_at = "2017-01-19T17:59:10Z"
        price_rule.save!

#####

        // Session is built by the OAuth process

        const price_rule = new shopify.rest.PriceRule({session: session});
        price_rule.title = "SUMMERSALE10OFF";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "all";
        price_rule.allocation_method = "across";
        price_rule.value_type = "fixed_amount";
        price_rule.value = "-10.0";
        price_rule.customer_selection = "all";
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"price_rule":{"id":1057856660,"value_type":"fixed_amount","value":"-10.0","customer_selection":"all","target_type":"line_item","target_selection":"all","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2017-01-19T12:59:10-05:00","ends_at":null,"created_at":"2026-01-09T19:37:13-05:00","updated_at":"2026-01-09T19:37:13-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"SUMMERSALE10OFF","admin_graphql_api_id":"gid://shopify/PriceRule/1057856660"}}

  * #### Create a price rule that gives the buyer 15% off a specific collection

#####

        curl -d '{"price_rule":{"title":"15OFFCOLLECTION","target_type":"line_item","target_selection":"entitled","allocation_method":"across","value_type":"percentage","value":"-15.0","customer_selection":"all","entitled_collection_ids":[841564295],"starts_at":"2017-01-19T17:59:10Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const price_rule = new admin.rest.resources.PriceRule({session: session});

        price_rule.title = "15OFFCOLLECTION";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "entitled";
        price_rule.allocation_method = "across";
        price_rule.value_type = "percentage";
        price_rule.value = "-15.0";
        price_rule.customer_selection = "all";
        price_rule.entitled_collection_ids = [
          841564295
        ];
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        price_rule = ShopifyAPI::PriceRule.new(session: test_session)
        price_rule.title = "15OFFCOLLECTION"
        price_rule.target_type = "line_item"
        price_rule.target_selection = "entitled"
        price_rule.allocation_method = "across"
        price_rule.value_type = "percentage"
        price_rule.value = "-15.0"
        price_rule.customer_selection = "all"
        price_rule.entitled_collection_ids = [
          841564295
        ]
        price_rule.starts_at = "2017-01-19T17:59:10Z"
        price_rule.save!

#####

        // Session is built by the OAuth process

        const price_rule = new shopify.rest.PriceRule({session: session});
        price_rule.title = "15OFFCOLLECTION";
        price_rule.target_type = "line_item";
        price_rule.target_selection = "entitled";
        price_rule.allocation_method = "across";
        price_rule.value_type = "percentage";
        price_rule.value = "-15.0";
        price_rule.customer_selection = "all";
        price_rule.entitled_collection_ids = [
          841564295
        ];
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"price_rule":{"id":1057856661,"value_type":"percentage","value":"-15.0","customer_selection":"all","target_type":"line_item","target_selection":"entitled","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2017-01-19T12:59:10-05:00","ends_at":null,"created_at":"2026-01-09T19:37:15-05:00","updated_at":"2026-01-09T19:37:15-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[841564295],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"15OFFCOLLECTION","admin_graphql_api_id":"gid://shopify/PriceRule/1057856661"}}

  * #### Create a price rule that gives the buyer free shipping on orders over $50.00 that can be used up to 20 times

#####

        curl -d '{"price_rule":{"title":"FREESHIPPING","target_type":"shipping_line","target_selection":"all","allocation_method":"each","value_type":"percentage","value":"-100.0","usage_limit":20,"customer_selection":"all","prerequisite_subtotal_range":{"greater_than_or_equal_to":"50.0"},"starts_at":"2017-01-19T17:59:10Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const price_rule = new admin.rest.resources.PriceRule({session: session});

        price_rule.title = "FREESHIPPING";
        price_rule.target_type = "shipping_line";
        price_rule.target_selection = "all";
        price_rule.allocation_method = "each";
        price_rule.value_type = "percentage";
        price_rule.value = "-100.0";
        price_rule.usage_limit = 20;
        price_rule.customer_selection = "all";
        price_rule.prerequisite_subtotal_range = {
          "greater_than_or_equal_to": "50.0"
        };
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        price_rule = ShopifyAPI::PriceRule.new(session: test_session)
        price_rule.title = "FREESHIPPING"
        price_rule.target_type = "shipping_line"
        price_rule.target_selection = "all"
        price_rule.allocation_method = "each"
        price_rule.value_type = "percentage"
        price_rule.value = "-100.0"
        price_rule.usage_limit = 20
        price_rule.customer_selection = "all"
        price_rule.prerequisite_subtotal_range = {
          "greater_than_or_equal_to" => "50.0"
        }
        price_rule.starts_at = "2017-01-19T17:59:10Z"
        price_rule.save!

#####

        // Session is built by the OAuth process

        const price_rule = new shopify.rest.PriceRule({session: session});
        price_rule.title = "FREESHIPPING";
        price_rule.target_type = "shipping_line";
        price_rule.target_selection = "all";
        price_rule.allocation_method = "each";
        price_rule.value_type = "percentage";
        price_rule.value = "-100.0";
        price_rule.usage_limit = 20;
        price_rule.customer_selection = "all";
        price_rule.prerequisite_subtotal_range = {
          "greater_than_or_equal_to": "50.0"
        };
        price_rule.starts_at = "2017-01-19T17:59:10Z";
        await price_rule.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"price_rule":{"id":1057856662,"value_type":"percentage","value":"-100.0","customer_selection":"all","target_type":"shipping_line","target_selection":"all","allocation_method":"each","allocation_limit":null,"once_per_customer":false,"usage_limit":20,"starts_at":"2017-01-19T12:59:10-05:00","ends_at":null,"created_at":"2026-01-09T19:37:16-05:00","updated_at":"2026-01-09T19:37:16-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":{"greater_than_or_equal_to":"50.0"},"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"FREESHIPPING","admin_graphql_api_id":"gid://shopify/PriceRule/1057856662"}}


* * *

##

[Anchor to GET request, Retrieves a list of price rules](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules)

get

Retrieves a list of price rules

[discountNodes](/docs/api/admin-graphql/latest/queries/discountNodes)

Retrieves a list of price rules. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of price rules](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Show price rules created before date (format 2017-03-25T16:15:47-04:00).

* * *

created_after

Show price rules created after date (format 2017-03-25T16:15:47-04:00).

* * *

ends_at_max

Show price rules ending before date (format 2017-03-25T16:15:47-04:00).

* * *

ends_at_min

Show price rules ending after date (format 2017-03-25T16:15:47-04:00).

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to retrieve.

* * *

after_id

Restrict results to after the specified ID.

* * *

starts_at_max

Show price rules starting before date (format 2017-03-25T16:15:47-04:00).

* * *

starts_at_min

Show price rules starting after date (format 2017-03-25T16:15:47-04:00).

* * *

times_used

Show price rules with times used.

* * *

updated_at_max

Show price rules last updated before date (format 2017-03-25T16:15:47-04:00).

* * *

updated_at_min

Show price rules last updated after date (format 2017-03-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-examples](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-examples)Examples

Retrieve all price rules

Retrieve all price rules after a specified ID

Query parameters

after_id=1057856657

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \

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

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

HTTP/1.1 200 OK

{

"price_rules": [

{

"id": 1057856657,

"value_type": "percentage",

"value": "20.0",

"customer_selection": "all",

"target_type": "line_item",

"target_selection": "all",

"allocation_method": "across",

"allocation_limit": null,

"once_per_customer": false,

"usage_limit": null,

"starts_at": "2026-01-08T19:37:04-05:00",

"ends_at": null,

"created_at": "2026-01-09T19:37:04-05:00",

"updated_at": "2026-01-09T19:37:04-05:00",

"entitled_product_ids": [],

"entitled_variant_ids": [],

"entitled_collection_ids": [],

"entitled_country_ids": [],

"prerequisite_product_ids": [],

"prerequisite_variant_ids": [],

"prerequisite_collection_ids": [],

"customer_segment_prerequisite_ids": [],

"prerequisite_customer_ids": [],

"prerequisite_subtotal_range": null,

"prerequisite_quantity_range": null,

"prerequisite_shipping_price_range": null,

"prerequisite_to_entitlement_quantity_ratio": {

"prerequisite_quantity": null,

"entitled_quantity": null

},

"prerequisite_to_entitlement_purchase": {

"prerequisite_amount": null

},

"title": "Test Rule 2",

"admin_graphql_api_id": "gid://shopify/PriceRule/1057856657"

},

{

"id": 1057856656,

"value_type": "percentage",

"value": "10.0",

"customer_selection": "all",

"target_type": "line_item",

"target_selection": "all",

"allocation_method": "across",

"allocation_limit": null,

"once_per_customer": false,

"usage_limit": null,

"starts_at": "2026-01-08T19:37:03-05:00",

"ends_at": null,

"created_at": "2026-01-09T19:37:04-05:00",

"updated_at": "2026-01-09T19:37:04-05:00",

"entitled_product_ids": [],

"entitled_variant_ids": [],

"entitled_collection_ids": [],

"entitled_country_ids": [],

"prerequisite_product_ids": [],

"prerequisite_variant_ids": [],

"prerequisite_collection_ids": [],

"customer_segment_prerequisite_ids": [],

"prerequisite_customer_ids": [],

"prerequisite_subtotal_range": null,

"prerequisite_quantity_range": null,

"prerequisite_shipping_price_range": null,

"prerequisite_to_entitlement_quantity_ratio": {

"prerequisite_quantity": null,

"entitled_quantity": null

},

"prerequisite_to_entitlement_purchase": {

"prerequisite_amount": null

},

"title": "Test Rule 1",

"admin_graphql_api_id": "gid://shopify/PriceRule/1057856656"

}

]

}

### examples

  * #### Retrieve all price rules

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.PriceRule.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::PriceRule.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.PriceRule.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"price_rules":[{"id":1057856657,"value_type":"percentage","value":"20.0","customer_selection":"all","target_type":"line_item","target_selection":"all","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2026-01-08T19:37:04-05:00","ends_at":null,"created_at":"2026-01-09T19:37:04-05:00","updated_at":"2026-01-09T19:37:04-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"Test Rule 2","admin_graphql_api_id":"gid://shopify/PriceRule/1057856657"},{"id":1057856656,"value_type":"percentage","value":"10.0","customer_selection":"all","target_type":"line_item","target_selection":"all","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2026-01-08T19:37:03-05:00","ends_at":null,"created_at":"2026-01-09T19:37:04-05:00","updated_at":"2026-01-09T19:37:04-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"Test Rule 1","admin_graphql_api_id":"gid://shopify/PriceRule/1057856656"}]}

  * #### Retrieve all price rules after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules.json?after_id=1057856657" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.PriceRule.all({
          session: session,
          after_id: "1057856657",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::PriceRule.all(
          session: test_session,
          after_id: "1057856657",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.PriceRule.all({
          session: session,
          after_id: "1057856657",
        });

#### response

        HTTP/1.1 200 OK{"price_rules":[{"id":1057856658,"value_type":"percentage","value":"15.0","customer_selection":"all","target_type":"line_item","target_selection":"all","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2026-01-08T19:37:09-05:00","ends_at":null,"created_at":"2026-01-09T19:37:09-05:00","updated_at":"2026-01-09T19:37:09-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"Test Rule for after_id","admin_graphql_api_id":"gid://shopify/PriceRule/1057856658"}]}


* * *

##

[Anchor to GET request, Retrieves a single price rule](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-price-rule-id)

get

Retrieves a single price rule

[discountNode](/docs/api/admin-graphql/latest/queries/discountNode)

Retrieves a single price rule

###

[Anchor to Parameters of Retrieves a single price rule](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-price-rule-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-price-rule-id-examples](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-price-rule-id-examples)Examples

Retrieve a single price rule by its ID

Path parameters

price_rule_id=507328175

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules/507328175.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175.json" \

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

HTTP/1.1 200 OK

{

"price_rule": {

"id": 507328175,

"value_type": "fixed_amount",

"value": "-10.0",

"customer_selection": "all",

"target_type": "line_item",

"target_selection": "all",

"allocation_method": "across",

"allocation_limit": null,

"once_per_customer": false,

"usage_limit": null,

"starts_at": "2026-01-03T17:04:11-05:00",

"ends_at": "2026-01-15T17:04:11-05:00",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"entitled_product_ids": [],

"entitled_variant_ids": [],

"entitled_collection_ids": [],

"entitled_country_ids": [],

"prerequisite_product_ids": [],

"prerequisite_variant_ids": [],

"prerequisite_collection_ids": [],

"customer_segment_prerequisite_ids": [],

"prerequisite_customer_ids": [],

"prerequisite_subtotal_range": null,

"prerequisite_quantity_range": null,

"prerequisite_shipping_price_range": null,

"prerequisite_to_entitlement_quantity_ratio": {

"prerequisite_quantity": null,

"entitled_quantity": null

},

"prerequisite_to_entitlement_purchase": {

"prerequisite_amount": null

},

"title": "SUMMERSALE10OFF",

"admin_graphql_api_id": "gid://shopify/PriceRule/507328175"

}

}

### examples

  * #### Retrieve a single price rule by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.PriceRule.find({
          session: session,
          id: 507328175,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::PriceRule.find(
          session: test_session,
          id: 507328175,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.PriceRule.find({
          session: session,
          id: 507328175,
        });

#### response

        HTTP/1.1 200 OK{"price_rule":{"id":507328175,"value_type":"fixed_amount","value":"-10.0","customer_selection":"all","target_type":"line_item","target_selection":"all","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2026-01-03T17:04:11-05:00","ends_at":"2026-01-15T17:04:11-05:00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"SUMMERSALE10OFF","admin_graphql_api_id":"gid://shopify/PriceRule/507328175"}}


* * *

##

[Anchor to GET request, Retrieves a count of all price rules](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-count)

get

Retrieves a count of all price rules

[discountNodesCount](/docs/api/admin-graphql/latest/queries/discountNodesCount?example=retrieves-a-count-of-all-price-rules)

Retrieves a count of all price rules.

###

[Anchor to Parameters of Retrieves a count of all price rules](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-count-examples](/docs/api/admin-rest/latest/resources/pricerule#get-price-rules-count-examples)Examples

Retrieve a count of all price rules

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/count.json" \

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

"count": 2

}

### examples

  * #### Retrieve a count of all price rules

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.PriceRule.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::PriceRule.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.PriceRule.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}


* * *

##

[Anchor to PUT request, Updates an existing a price rule](/docs/api/admin-rest/latest/resources/pricerule#put-price-rules-price-rule-id)

put

Updates an existing a price rule

[discountCodeBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate)

[discountAutomaticBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate)

[discountCodeBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate)

[discountAutomaticBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate)

[discountCodeFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingUpdate)

[discountAutomaticFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate)

Updates an existing a price rule

###

[Anchor to Parameters of Updates an existing a price rule](/docs/api/admin-rest/latest/resources/pricerule#put-price-rules-price-rule-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-price-rules-price-rule-id-examples](/docs/api/admin-rest/latest/resources/pricerule#put-price-rules-price-rule-id-examples)Examples

Update the title of a price rule

Path parameters

price_rule_id=507328175

string**string**

required**required**

Request body

price_rule

Price_rule resource**Price_rule resource**

Show price_rule properties

price_rule.id:507328175

read-only**read-only**

deprecated**deprecated**

The ID for the price rule.

price_rule.title:"WINTER SALE"

deprecated**deprecated**

The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the **Discounts** page of the Shopify admin for bulk discounts.

For non-bulk discounts, the discount code is displayed on the admin.

Caution

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

**Caution:**

For a consistent search experience, use the same value for `title` as the `code` property of the associated discount code.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/price_rules/507328175.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"price_rule":{"id":507328175,"title":"WINTER SALE"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175.json" \

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

HTTP/1.1 200 OK

{

"price_rule": {

"id": 507328175,

"value_type": "fixed_amount",

"value": "-10.0",

"customer_selection": "all",

"target_type": "line_item",

"target_selection": "all",

"allocation_method": "across",

"allocation_limit": null,

"once_per_customer": false,

"usage_limit": null,

"starts_at": "2026-01-03T17:04:11-05:00",

"ends_at": "2026-01-15T17:04:11-05:00",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T19:37:11-05:00",

"entitled_product_ids": [],

"entitled_variant_ids": [],

"entitled_collection_ids": [],

"entitled_country_ids": [],

"prerequisite_product_ids": [],

"prerequisite_variant_ids": [],

"prerequisite_collection_ids": [],

"customer_segment_prerequisite_ids": [],

"prerequisite_customer_ids": [],

"prerequisite_subtotal_range": null,

"prerequisite_quantity_range": null,

"prerequisite_shipping_price_range": null,

"prerequisite_to_entitlement_quantity_ratio": {

"prerequisite_quantity": null,

"entitled_quantity": null

},

"prerequisite_to_entitlement_purchase": {

"prerequisite_amount": null

},

"title": "WINTER SALE",

"admin_graphql_api_id": "gid://shopify/PriceRule/507328175"

}

}

### examples

  * #### Update the title of a price rule

#####

        curl -d '{"price_rule":{"id":507328175,"title":"WINTER SALE"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const price_rule = new admin.rest.resources.PriceRule({session: session});

        price_rule.id = 507328175;
        price_rule.title = "WINTER SALE";
        await price_rule.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        price_rule = ShopifyAPI::PriceRule.new(session: test_session)
        price_rule.id = 507328175
        price_rule.title = "WINTER SALE"
        price_rule.save!

#####

        // Session is built by the OAuth process

        const price_rule = new shopify.rest.PriceRule({session: session});
        price_rule.id = 507328175;
        price_rule.title = "WINTER SALE";
        await price_rule.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"price_rule":{"id":507328175,"value_type":"fixed_amount","value":"-10.0","customer_selection":"all","target_type":"line_item","target_selection":"all","allocation_method":"across","allocation_limit":null,"once_per_customer":false,"usage_limit":null,"starts_at":"2026-01-03T17:04:11-05:00","ends_at":"2026-01-15T17:04:11-05:00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:37:11-05:00","entitled_product_ids":[],"entitled_variant_ids":[],"entitled_collection_ids":[],"entitled_country_ids":[],"prerequisite_product_ids":[],"prerequisite_variant_ids":[],"prerequisite_collection_ids":[],"customer_segment_prerequisite_ids":[],"prerequisite_customer_ids":[],"prerequisite_subtotal_range":null,"prerequisite_quantity_range":null,"prerequisite_shipping_price_range":null,"prerequisite_to_entitlement_quantity_ratio":{"prerequisite_quantity":null,"entitled_quantity":null},"prerequisite_to_entitlement_purchase":{"prerequisite_amount":null},"title":"WINTER SALE","admin_graphql_api_id":"gid://shopify/PriceRule/507328175"}}


* * *

##

[Anchor to DELETE request, Remove an existing PriceRule](/docs/api/admin-rest/latest/resources/pricerule#delete-price-rules-price-rule-id)

del

Remove an existing PriceRule

[discountCodeDelete](/docs/api/admin-graphql/latest/mutations/discountCodeDelete)

[discountAutomaticDelete](/docs/api/admin-graphql/latest/mutations/discountAutomaticDelete?example=remove-an-existing-pricerule)

Deletes a price rule

###

[Anchor to Parameters of Remove an existing PriceRule](/docs/api/admin-rest/latest/resources/pricerule#delete-price-rules-price-rule-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-price-rules-price-rule-id-examples](/docs/api/admin-rest/latest/resources/pricerule#delete-price-rules-price-rule-id-examples)Examples

Delete a price rule

Path parameters

price_rule_id=507328175

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/price_rules/507328175.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

HTTP/1.1 204 No Content

### examples

  * #### Delete a price rule

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.PriceRule.delete({
          session: session,
          id: 507328175,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::PriceRule.delete(
          session: test_session,
          id: 507328175,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.PriceRule.delete({
          session: session,
          id: 507328175,
        });

#### response

        HTTP/1.1 204 No Content