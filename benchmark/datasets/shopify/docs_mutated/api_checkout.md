# Checkout

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/checkout*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Checkout

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

Important

The REST Checkout API is deprecated as of version 2024-07. Please see the [developer changelog](https://shopify.dev/changelog/deprecation-of-checkout-apis) for more information.

**Important:**

The REST Checkout API is deprecated as of version 2024-07. Please see the [developer changelog](https://shopify.dev/changelog/deprecation-of-checkout-apis) for more information.

If you're building an app with the [Sales Channel SDK](/docs/apps/channels), then you can use the Checkout API to let customers purchase products from Shopify stores that have installed your sales channel.

Shopify uses the Checkout resource to manage a user's cart as it transitions to a paid order. This process includes specifying which line items are included in the checkout, attaching a customer's shipping and payment details, and calculating tax and shipping rates. Credit card payments can be attached to a Checkout using the [Payment](/docs/api/admin-rest/current/resources/payment) resource.

#### Note

You can't use the Checkout API to create a new checkout user experience for an individual store. For that you need to use an SDK that's powered by the [Storefront API](/docs/api/storefront) instead, such as the [JavaScript Buy](/docs/custom-storefronts/additional-sdks/js-buy), [iOS Buy](/docs/custom-storefronts/mobile-kit/buy-sdk-ios), and [Android Buy](/docs/custom-storefronts/mobile-kit/buy-sdk-android) SDKs.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/checkouts.json](/docs/api/admin-rest/latest/resources/checkout#post-checkouts)

Creates a checkout

deprecated

**

deprecated

**

  * [ post/admin/api/latest/checkouts/{token}/complete.json](/docs/api/admin-rest/latest/resources/checkout#post-checkouts-token-complete)

Completes a checkout

deprecated

**

deprecated

**

  * [ get/admin/api/latest/checkouts/{token}.json](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token)

Retrieves a checkout

deprecated

**

deprecated

**

  * [ get/admin/api/latest/checkouts/{token}/shipping_rates.json](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token-shipping-rates)

Retrieves a list of shipping rates

deprecated

**

deprecated

**

  * [ put/admin/api/latest/checkouts/{token}.json](/docs/api/admin-rest/latest/resources/checkout#put-checkouts-token)

Modifies an existing checkout

deprecated

**

deprecated

**


* * *

[ Anchor to ](/docs/api/admin-rest/latest/resources/checkout#resource-object)

## The Checkout resource

[Anchor to ](/docs/api/admin-rest/latest/resources/checkout#resource-object-properties)

### Properties

* * *

applied_discount

deprecated**deprecated**

A cart-level discount applied to the checkout. Apply a discount by specifying values for `amount`, `title`, `description`, `value`, and `value_type`.

Show applied_discount properties

  * **amount** : The amount that is deducted from `payment_due` in presentment currency.
  * **title** : The title to categorize the applied discount.
  * **description** : The description of the applied discount.
  * **value** : The value that was used to calculate the final applied discount amount.
  * **value_type** : The type of value that was used to calculate the final applied discount amount. Valid values: `fixed_amount` and `percentage`.
  * **non_applicable_reason** : The reason why the discount is not applicable, if the discount cannot be applied to the checkout.
  * **applicable** : Whether this discount code can be applied to the checkout.
  * **application_type** : Describes how the discount was applied to the checkout. Possible values:
    * **automatic** : The discount [was applied automatically](/api/examples/discounts#creating-automatic-discounts).
    * **discount_code** : The merchant or customer entered a [discount code](/api/examples/discounts#creating-code-discounts).
    * **manual** : The discount was applied manually by the merchant or an app.
    * **script** : The discount was applied by a [Shopify Script](https://help.shopify.com/en/manual/checkout-settings/script-editor).


* * *

billing_address

deprecated**deprecated**

The mailing address associated with the payment method. It has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city, town, or village of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1 alpha-2](//en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the billing address.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the region (province, state, prefecture, …) of the billing address.
  * **province_code** : The alphanumeric abbreviation of the region of the billing address.
  * **zip** : The postal code (zip, postcode, Eircode, …) of the billing address.


* * *

buyer_accepts_marketing

deprecated**deprecated**

Whether the customer has consented to receive marketing material via email.

* * *

created_at

read-only**read-only**

deprecated**deprecated**

The date and time ([ISO 8601 format](//en.wikipedia.org/wiki/ISO_8601)) when the checkout was created.

* * *

currency

read-only**read-only**

deprecated**deprecated**

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) of the shop's default currency at the time of checkout. For the currency that the customer used at checkout, see `presentment_currency`.

* * *

customer_id

deprecated**deprecated**

The ID of the customer associated with this checkout.

* * *

discount_code

deprecated**deprecated**

The discount code that is applied to the checkout. This populates `applied_discount` with the appropriate metadata for that discount code. To remove a discount code, send an empty string or `null`.

* * *

email

deprecated**deprecated**

The customer's email address. A checkout needs to have a value for `email` or `phone` before it can be completed.

* * *

gift_cards

deprecated**deprecated**

A list of gift card objects, each containing information about a gift card applied to this checkout. Gift cards can be applied to a checkout by passing `{ "checkout": { "gift_cards": [{ "code": "a gift card code" }, { "code": "another gift card code" }] } }`. Each gift card object has the following properties:

Show gift_cards properties

  * **amount_used** : The amount of the gift card used by this checkout in presentment currency.
  * **code** : The gift card code.
  * **balance** : The amount left on the gift card after being applied to this checkout in presentment currency.
  * **id** : The ID for the applied gift card.
  * **last_characters** : The last four characters of the applied gift card for display back to the user.

Updating the gift card list overwrites any previous list already defined in the checkout. To remove a gift card from the list of applied gift cards, re-apply the `gift_cards` array without that gift card.

* * *

line_items

deprecated**deprecated**

A list of line item objects, each containing information about an item in the checkout. Each line item object has the following properties:

Show line_items properties

  * **applied_discounts** : A list of the discounts applied to the line item.
  * **compare_at_price** : The original selling price of the product, if applicable.
  * **discount_allocations** : A list all discounts on the checkout that target this line item, including both "across" and "each" applications. A superset of `applied_discounts`.
  * **fulfillment_service** : If the variant is a gift card, allows to override the fulfillment service so the gift card can be activated with a custom code. Valid values: `manual`.
  * **grams** : The weight of the item in grams.
  * **id** : The checkout-specific ID of the line item.
  * **line_price** : The line price of the item, based on `price` multiplied by `quantity`.
  * **price** : The price of the item in presentment currency.
  * **product_id** : The product of the line item.
  * **properties** : The [customization information](/api/liquid/objects/line_item#line_item-properties) for a line item (optional).
  * **quantity** : The number of products that were purchased.
  * **requires_shipping** : Whether the fulfillment requires shipping.
  * **sku** : The unique identifier of the item in the fulfillment.
  * **taxable** : Whether this product is taxable.
  * **title** : The title of the product.
  * **variant_id** : The variant ID of the line item.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.


* * *

order

read-only**read-only**

deprecated**deprecated**

An object containing the ID, name, and status page URL of the associated order when the checkout is complete. Default value: `null`.

* * *

payment_due

read-only**read-only**

deprecated**deprecated**

The amount left to be paid in presentment currency. This is equal to the sum of the checkout line prices, taxes, and shipping minus discounts and gift cards.

* * *

Show 21 hidden fields

Was this section helpful?

YesNo

{}

## The Checkout resource

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

"applied_discount": {

"amount": "30.00",

"title": "XYZ Promotion",

"description": "Promotional item for blackfriday.",

"value": "30.00",

"value_type": "fixed_amount",

"non_applicable_reason": null,

"applicable": true,

"application_type": "discount_code"

},

"billing_address": {

"address1": "Chestnut Street 92",

"address2": "Suite 300",

"city": "Louisville",

"company": null,

"country": "US",

"first_name": null,

"id": 207119551,

"last_name": null,

"phone": "555-625-1199",

"province": "KY",

"zip": "40202",

"province_code": null,

"country_code": null

},

"buyer_accepts_marketing": false,

"created_at": {

"created_at": "2008-01-10T11:00:00-05:00"

},

"currency": {

"currency": "USD"

},

"customer_id": {

"customer_id": 1234

},

* * *

##

[Anchor to POST request, Creates a checkout](/docs/api/admin-rest/latest/resources/checkout#post-checkouts)

post

Creates a checkout

deprecated**deprecated**

Requires `checkouts` access scope.

**Requires `checkouts` access scope.:**

Creates a checkout

###

[Anchor to Parameters of Creates a checkout](/docs/api/admin-rest/latest/resources/checkout#post-checkouts-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-checkouts-examples](/docs/api/admin-rest/latest/resources/checkout#post-checkouts-examples)Examples

Create a checkout with a product variant and quantity

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.line_items:[{"variant_id":39072856,"quantity":5}]

deprecated**deprecated**

A list of line item objects, each containing information about an item in the checkout. Each line item object has the following properties:

Show line_items properties

  * **applied_discounts** : A list of the discounts applied to the line item.
  * **compare_at_price** : The original selling price of the product, if applicable.
  * **discount_allocations** : A list all discounts on the checkout that target this line item, including both "across" and "each" applications. A superset of `applied_discounts`.
  * **fulfillment_service** : If the variant is a gift card, allows to override the fulfillment service so the gift card can be activated with a custom code. Valid values: `manual`.
  * **grams** : The weight of the item in grams.
  * **id** : The checkout-specific ID of the line item.
  * **line_price** : The line price of the item, based on `price` multiplied by `quantity`.
  * **price** : The price of the item in presentment currency.
  * **product_id** : The product of the line item.
  * **properties** : The [customization information](/api/liquid/objects/line_item#line_item-properties) for a line item (optional).
  * **quantity** : The number of products that were purchased.
  * **requires_shipping** : Whether the fulfillment requires shipping.
  * **sku** : The unique identifier of the item in the fulfillment.
  * **taxable** : Whether this product is taxable.
  * **title** : The title of the product.
  * **variant_id** : The variant ID of the line item.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.


Create a checkout without any line items

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.email:"me@example.com"

deprecated**deprecated**

The customer's email address. A checkout needs to have a value for `email` or `phone` before it can be completed.

Creating a checkout with errors, such as using the ID of a variant that doesn't exist or that isn't published to your sales channel, fails with a 422 response and returns errors

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.line_items:[{"variant_id":123456789,"quantity":1}]

deprecated**deprecated**

A list of line item objects, each containing information about an item in the checkout. Each line item object has the following properties:

Show line_items properties

  * **applied_discounts** : A list of the discounts applied to the line item.
  * **compare_at_price** : The original selling price of the product, if applicable.
  * **discount_allocations** : A list all discounts on the checkout that target this line item, including both "across" and "each" applications. A superset of `applied_discounts`.
  * **fulfillment_service** : If the variant is a gift card, allows to override the fulfillment service so the gift card can be activated with a custom code. Valid values: `manual`.
  * **grams** : The weight of the item in grams.
  * **id** : The checkout-specific ID of the line item.
  * **line_price** : The line price of the item, based on `price` multiplied by `quantity`.
  * **price** : The price of the item in presentment currency.
  * **product_id** : The product of the line item.
  * **properties** : The [customization information](/api/liquid/objects/line_item#line_item-properties) for a line item (optional).
  * **quantity** : The number of products that were purchased.
  * **requires_shipping** : Whether the fulfillment requires shipping.
  * **sku** : The unique identifier of the item in the fulfillment.
  * **taxable** : Whether this product is taxable.
  * **title** : The title of the product.
  * **variant_id** : The variant ID of the line item.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.


Creating a checkout with line item errors fails and returns the errors mapped by index

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.line_items:[{"variant_id":39072856,"quantity":1},{"variant_id":1,"quantity":1},{"variant_id":1,"quantity":1},{"variant_id":49148385,"quantity":1},{"variant_id":1,"quantity":1}]

deprecated**deprecated**

A list of line item objects, each containing information about an item in the checkout. Each line item object has the following properties:

Show line_items properties

  * **applied_discounts** : A list of the discounts applied to the line item.
  * **compare_at_price** : The original selling price of the product, if applicable.
  * **discount_allocations** : A list all discounts on the checkout that target this line item, including both "across" and "each" applications. A superset of `applied_discounts`.
  * **fulfillment_service** : If the variant is a gift card, allows to override the fulfillment service so the gift card can be activated with a custom code. Valid values: `manual`.
  * **grams** : The weight of the item in grams.
  * **id** : The checkout-specific ID of the line item.
  * **line_price** : The line price of the item, based on `price` multiplied by `quantity`.
  * **price** : The price of the item in presentment currency.
  * **product_id** : The product of the line item.
  * **properties** : The [customization information](/api/liquid/objects/line_item#line_item-properties) for a line item (optional).
  * **quantity** : The number of products that were purchased.
  * **requires_shipping** : Whether the fulfillment requires shipping.
  * **sku** : The unique identifier of the item in the fulfillment.
  * **taxable** : Whether this product is taxable.
  * **title** : The title of the product.
  * **variant_id** : The variant ID of the line item.
  * **variant_title** : The title of the product variant.
  * **vendor** : The name of the item's supplier.


Was this section helpful?

YesNo

post

## /admin/api/2026-01/checkouts.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"checkout":{"line_items":[{"variant_id":39072856,"quantity":5}]}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \

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

80

81

82

83

84

85

86

87

88

HTTP/1.1 202 Accepted

{

"checkout": {

"completed_at": null,

"created_at": "2026-01-09T19:34:40-05:00",

"currency": "USD",

"presentment_currency": "USD",

"customer_id": null,

"customer_locale": "en",

"device_id": null,

"discount_code": null,

"discount_codes": [],

"email": null,

"legal_notice_url": null,

"location_id": null,

"name": "#1068673455",

"note": "",

"note_attributes": {},

"order_id": null,

"order_status_url": null,

"order": null,

"payment_due": "995.00",

"payment_url": "https://app.local/cardserver/sessions",

"payments": [],

"phone": null,

"shopify_payments_account_id": null,

"privacy_policy_url": null,

"refund_policy_url": null,

"requires_shipping": true,

"reservation_time_left": 0,

"reservation_time": null,

"source_identifier": null,

"source_name": "755357713",

"source_url": null,

"subscription_policy_url": null,

"subtotal_price": "995.00",

"shipping_policy_url": null,

"tax_exempt": false,

"taxes_included": false,

"terms_of_sale_url": null,

"terms_of_service_url": null,

"token": "c6e185593768c4e69bdbe896a548031a",

"total_price": "995.00",

"total_tax": "0.00",

"total_tip_received": "0.00",

"total_line_items_price": "995.00",

"updated_at": "2026-01-09T19:34:40-05:00",

"user_id": null,

"web_url": "https://jsmith.myshopify.com/548380009/checkouts/c6e185593768c4e69bdbe896a548031a",

"line_items": [

{

"id": "1dcc8725279be502739b07335479d768",

"key": "1dcc8725279be502739b07335479d768",

"product_id": 632910392,

"variant_id": 39072856,

"sku": "IPOD2008GREEN",

"vendor": "Apple",

"title": "IPod Nano - 8GB",

"variant_title": "Green",

"image_url": "https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251",

"taxable": true,

"requires_shipping": true,

"gift_card": false,

"price": "199.00",

"compare_at_price": null,

"line_price": "995.00",

"properties": {},

"quantity": 5,

"grams": 567,

"fulfillment_service": "manual",

"applied_discounts": [],

"discount_allocations": [],

"tax_lines": []

}

],

"gift_cards": [],

"tax_lines": [],

"tax_manipulations": [],

"shipping_line": null,

"shipping_rate": null,

"shipping_address": null,

"credit_card": null,

"billing_address": null,

"applied_discount": null,

"applied_discounts": [],

"discount_violations": []

}

}

### examples

  * #### Create a checkout with a product variant and quantity

#####

        curl -d '{"checkout":{"line_items":[{"variant_id":39072856,"quantity":5}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.line_items = [
          {
            "variant_id": 39072856,
            "quantity": 5
          }
        ];
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.line_items = [
          {
            "variant_id" => 39072856,
            "quantity" => 5
          }
        ]
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.line_items = [
          {
            "variant_id": 39072856,
            "quantity": 5
          }
        ];
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2026-01-09T19:34:40-05:00","currency":"USD","presentment_currency":"USD","customer_id":null,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":null,"legal_notice_url":null,"location_id":null,"name":"#1068673455","note":"","note_attributes":{},"order_id":null,"order_status_url":null,"order":null,"payment_due":"995.00","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":true,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subscription_policy_url":null,"subtotal_price":"995.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"c6e185593768c4e69bdbe896a548031a","total_price":"995.00","total_tax":"0.00","total_tip_received":"0.00","total_line_items_price":"995.00","updated_at":"2026-01-09T19:34:40-05:00","user_id":null,"web_url":"https://jsmith.myshopify.com/548380009/checkouts/c6e185593768c4e69bdbe896a548031a","line_items":[{"id":"1dcc8725279be502739b07335479d768","key":"1dcc8725279be502739b07335479d768","product_id":632910392,"variant_id":39072856,"sku":"IPOD2008GREEN","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Green","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"995.00","properties":{},"quantity":5,"grams":567,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[]}],"gift_cards":[],"tax_lines":[],"tax_manipulations":[],"shipping_line":null,"shipping_rate":null,"shipping_address":null,"credit_card":null,"billing_address":null,"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}

  * #### Create a checkout without any line items

#####

        curl -d '{"checkout":{"email":"me@example.com"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.email = "me@example.com";
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.email = "me@example.com"
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.email = "me@example.com";
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2026-01-09T19:34:47-05:00","currency":"USD","presentment_currency":"USD","customer_id":null,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"me@example.com","legal_notice_url":null,"location_id":null,"name":"#1068673456","note":"","note_attributes":{},"order_id":null,"order_status_url":null,"order":null,"payment_due":"0.00","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":false,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"755357713","source_url":null,"subscription_policy_url":null,"subtotal_price":"0.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"cc5f6b562ebdfb890b23409667b30a6c","total_price":"0.00","total_tax":"0.00","total_tip_received":"0.00","total_line_items_price":"0.00","updated_at":"2026-01-09T19:34:47-05:00","user_id":null,"web_url":"https://jsmith.myshopify.com/548380009/checkouts/cc5f6b562ebdfb890b23409667b30a6c","line_items":[],"gift_cards":[],"tax_lines":[],"tax_manipulations":[],"shipping_line":null,"shipping_rate":null,"shipping_address":null,"credit_card":null,"billing_address":null,"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}

  * #### Creating a checkout with errors, such as using the ID of a variant that doesn't exist or that isn't published to your sales channel, fails with a 422 response and returns errors

#####

        curl -d '{"checkout":{"line_items":[{"variant_id":123456789,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.line_items = [
          {
            "variant_id": 123456789,
            "quantity": 1
          }
        ];
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.line_items = [
          {
            "variant_id" => 123456789,
            "quantity" => 1
          }
        ]
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.line_items = [
          {
            "variant_id": 123456789,
            "quantity": 1
          }
        ];
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"line_items":{"0":{"variant_id":[{"code":"product_not_available","message":"product is not published for this customer.","options":{}}]}}}}

  * #### Creating a checkout with line item errors fails and returns the errors mapped by index

#####

        curl -d '{"checkout":{"line_items":[{"variant_id":39072856,"quantity":1},{"variant_id":1,"quantity":1},{"variant_id":1,"quantity":1},{"variant_id":49148385,"quantity":1},{"variant_id":1,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.line_items = [
          {
            "variant_id": 39072856,
            "quantity": 1
          },
          {
            "variant_id": 1,
            "quantity": 1
          },
          {
            "variant_id": 1,
            "quantity": 1
          },
          {
            "variant_id": 49148385,
            "quantity": 1
          },
          {
            "variant_id": 1,
            "quantity": 1
          }
        ];
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.line_items = [
          {
            "variant_id" => 39072856,
            "quantity" => 1
          },
          {
            "variant_id" => 1,
            "quantity" => 1
          },
          {
            "variant_id" => 1,
            "quantity" => 1
          },
          {
            "variant_id" => 49148385,
            "quantity" => 1
          },
          {
            "variant_id" => 1,
            "quantity" => 1
          }
        ]
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.line_items = [
          {
            "variant_id": 39072856,
            "quantity": 1
          },
          {
            "variant_id": 1,
            "quantity": 1
          },
          {
            "variant_id": 1,
            "quantity": 1
          },
          {
            "variant_id": 49148385,
            "quantity": 1
          },
          {
            "variant_id": 1,
            "quantity": 1
          }
        ];
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"line_items":{"1":{"variant_id":[{"code":"product_not_available","message":"product is not published for this customer.","options":{}}]},"2":{"variant_id":[{"code":"product_not_available","message":"product is not published for this customer.","options":{}}]},"4":{"variant_id":[{"code":"product_not_available","message":"product is not published for this customer.","options":{}}]}}}}


* * *

##

[Anchor to POST request, Completes a checkout](/docs/api/admin-rest/latest/resources/checkout#post-checkouts-token-complete)

post

Completes a checkout

deprecated**deprecated**

Requires `checkouts` access scope.

**Requires `checkouts` access scope.:**

Completes a checkout

###

[Anchor to Parameters of Completes a checkout](/docs/api/admin-rest/latest/resources/checkout#post-checkouts-token-complete-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

token

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-checkouts-token-complete-examples](/docs/api/admin-rest/latest/resources/checkout#post-checkouts-token-complete-examples)Examples

Complete a checkout without requiring payment

Path parameters

token=b490a9220cd14d7344024f4874f640a6

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/checkouts/b490a9220cd14d7344024f4874f640a6/complete.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/b490a9220cd14d7344024f4874f640a6/complete.json" \

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

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

HTTP/1.1 202 Accepted

{

"checkout": {

"completed_at": null,

"created_at": "2012-10-12T07:05:27-04:00",

"currency": "USD",

"presentment_currency": "USD",

"customer_id": 207119551,

"customer_locale": "en",

"device_id": null,

"discount_code": null,

"discount_codes": [],

"email": "bob.norman@mail.example.com",

"legal_notice_url": null,

"location_id": null,

"name": "#86568385",

"note": "",

"note_attributes": {

"custom engraving": "Happy Birthday",

"colour": "green"

},

"order_id": null,

"order_status_url": null,

"order": null,

"payment_due": "0.00",

"payment_url": "https://app.local/cardserver/sessions",

"payments": [],

"phone": null,

"shopify_payments_account_id": null,

"privacy_policy_url": null,

"refund_policy_url": null,

"requires_shipping": false,

"reservation_time_left": 0,

"reservation_time": null,

"source_identifier": null,

"source_name": "web",

"source_url": null,

"subscription_policy_url": null,

"subtotal_price": "0.00",

"shipping_policy_url": null,

"tax_exempt": false,

"taxes_included": false,

"terms_of_sale_url": null,

"terms_of_service_url": null,

"token": "b490a9220cd14d7344024f4874f640a6",

"total_price": "0.00",

"total_tax": "0.00",

"total_tip_received": "0.00",

"total_line_items_price": "0.00",

"updated_at": "2026-01-09T19:34:57-05:00",

"user_id": null,

"web_url": "https://checkout.local/548380009/checkouts/b490a9220cd14d7344024f4874f640a6",

"line_items": [

{

"id": "49148385",

"key": "49148385",

"product_id": 632910392,

"variant_id": 49148385,

"sku": "IPOD2008RED",

"vendor": "Apple",

"title": "IPod Nano - 8GB",

"variant_title": "Red",

"image_url": "https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251",

"taxable": true,

"requires_shipping": false,

"gift_card": false,

"price": "0.00",

"compare_at_price": null,

"line_price": "0.00",

"properties": {},

"quantity": 1,

"grams": 200,

"fulfillment_service": "manual",

"applied_discounts": [],

"discount_allocations": [],

"tax_lines": [

{

"price": "0.00",

"rate": 0.06,

"title": "Tax",

"channel_liable": false

}

]

}

],

"gift_cards": [],

"tax_lines": [

{

"price": "0.00",

"rate": 0.06,

"title": "Tax",

"compare_at": 0.06

}

],

"tax_manipulations": [],

"shipping_line": null,

"shipping_rate": null,

"shipping_address": {

"id": 921093900,

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"company": null,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"province": "Kentucky",

"province_code": "KY",

"country": "United States",

"country_code": "US",

"zip": "40202"

},

"credit_card": null,

"billing_address": {

"id": 921093900,

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"company": null,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"province": "Kentucky",

"province_code": "KY",

"country": "United States",

"country_code": "US",

"zip": "40202"

},

"applied_discount": null,

"applied_discounts": [],

"discount_violations": []

}

}

### examples

  * #### Complete a checkout without requiring payment

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/b490a9220cd14d7344024f4874f640a6/complete.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.token = "b490a9220cd14d7344024f4874f640a6";
        await checkout.complete({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.token = "b490a9220cd14d7344024f4874f640a6"
        checkout.complete(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.token = "b490a9220cd14d7344024f4874f640a6";
        await checkout.complete({});

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2012-10-12T07:05:27-04:00","currency":"USD","presentment_currency":"USD","customer_id":207119551,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"bob.norman@mail.example.com","legal_notice_url":null,"location_id":null,"name":"#86568385","note":"","note_attributes":{"custom engraving":"Happy Birthday","colour":"green"},"order_id":null,"order_status_url":null,"order":null,"payment_due":"0.00","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":false,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"web","source_url":null,"subscription_policy_url":null,"subtotal_price":"0.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"b490a9220cd14d7344024f4874f640a6","total_price":"0.00","total_tax":"0.00","total_tip_received":"0.00","total_line_items_price":"0.00","updated_at":"2026-01-09T19:34:57-05:00","user_id":null,"web_url":"https://checkout.local/548380009/checkouts/b490a9220cd14d7344024f4874f640a6","line_items":[{"id":"49148385","key":"49148385","product_id":632910392,"variant_id":49148385,"sku":"IPOD2008RED","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Red","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":false,"gift_card":false,"price":"0.00","compare_at_price":null,"line_price":"0.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"0.00","rate":0.06,"title":"Tax","channel_liable":false}]}],"gift_cards":[],"tax_lines":[{"price":"0.00","rate":0.06,"title":"Tax","compare_at":0.06}],"tax_manipulations":[],"shipping_line":null,"shipping_rate":null,"shipping_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"credit_card":null,"billing_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}


* * *

##

[Anchor to GET request, Retrieves a checkout](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token)

get

Retrieves a checkout

deprecated**deprecated**

Requires `checkouts` access scope.

**Requires `checkouts` access scope.:**

Retrieves a checkout

###

[Anchor to Parameters of Retrieves a checkout](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

token

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-checkouts-token-examples](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token-examples)Examples

Retrieve a completed checkout

Path parameters

token=bd5a8aa1ecd019dd3520ff791ee3a24c

string**string**

required**required**

Retrieve a processing checkout

Path parameters

token=7yjf4v2we7gamku6a6h7tvm8h3mmvs4x

string**string**

required**required**

Retrieve an existing checkout

Path parameters

token=exuw7apwoycchjuwtiqg8nytfhphr62a

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c.json" \

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

"checkout": {

"completed_at": "2005-07-31T11:57:11-04:00",

"created_at": "2012-10-12T07:05:27-04:00",

"currency": "USD",

"presentment_currency": "USD",

"customer_id": 207119551,

"customer_locale": "en",

"device_id": null,

"discount_code": null,

"discount_codes": [],

"email": "bob.norman@mail.example.com",

"legal_notice_url": null,

"location_id": null,

"name": "#901414060",

"note": "",

"note_attributes": {

"custom engraving": "Happy Birthday",

"colour": "green"

},

"order_id": 450789469,

"order_status_url": "https://checkout.local/548380009/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c/thank_you",

"order": {

"id": 450789469,

"name": "#1001",

"status_url": "https://checkout.local/548380009/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c/thank_you"

},

"payment_due": "421.88",

"payment_url": "https://app.local/cardserver/sessions",

"payments": [],

"phone": null,

"shopify_payments_account_id": null,

"privacy_policy_url": null,

"refund_policy_url": null,

"requires_shipping": true,

### examples

  * #### Retrieve a completed checkout

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Checkout.find({
          session: session,
          token: "bd5a8aa1ecd019dd3520ff791ee3a24c",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Checkout.find(
          session: test_session,
          token: "bd5a8aa1ecd019dd3520ff791ee3a24c",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Checkout.find({
          session: session,
          token: "bd5a8aa1ecd019dd3520ff791ee3a24c",
        });

#### response

        HTTP/1.1 200 OK{"checkout":{"completed_at":"2005-07-31T11:57:11-04:00","created_at":"2012-10-12T07:05:27-04:00","currency":"USD","presentment_currency":"USD","customer_id":207119551,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"bob.norman@mail.example.com","legal_notice_url":null,"location_id":null,"name":"#901414060","note":"","note_attributes":{"custom engraving":"Happy Birthday","colour":"green"},"order_id":450789469,"order_status_url":"https://checkout.local/548380009/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c/thank_you","order":{"id":450789469,"name":"#1001","status_url":"https://checkout.local/548380009/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c/thank_you"},"payment_due":"421.88","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":true,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"web","source_url":null,"subscription_policy_url":null,"subtotal_price":"398.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"bd5a8aa1ecd019dd3520ff791ee3a24c","total_price":"421.88","total_tax":"23.88","total_tip_received":"0.00","total_line_items_price":"398.00","updated_at":"2012-10-12T07:05:27-04:00","user_id":null,"web_url":"https://checkout.local/548380009/checkouts/bd5a8aa1ecd019dd3520ff791ee3a24c","line_items":[{"id":"60715a3461f5f853","key":"60715a3461f5f853","product_id":632910392,"variant_id":49148385,"sku":"IPOD2008RED","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Red","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"11.94","rate":0.06,"title":"Tax","channel_liable":false}]},{"id":"0703986f986628ba","key":"0703986f986628ba","product_id":632910392,"variant_id":808950810,"sku":"IPOD2008PINK","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Pink","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"11.94","rate":0.06,"title":"Tax","channel_liable":false}]}],"gift_cards":[],"tax_lines":[{"price":"23.88","rate":0.06,"title":"Tax","compare_at":0.06}],"tax_manipulations":[],"shipping_line":{"handle":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping","tax_lines":[]},"shipping_rate":{"id":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping"},"shipping_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"credit_card":null,"billing_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}

  * #### Retrieve a processing checkout

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/7yjf4v2we7gamku6a6h7tvm8h3mmvs4x.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Checkout.find({
          session: session,
          token: "7yjf4v2we7gamku6a6h7tvm8h3mmvs4x",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Checkout.find(
          session: test_session,
          token: "7yjf4v2we7gamku6a6h7tvm8h3mmvs4x",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Checkout.find({
          session: session,
          token: "7yjf4v2we7gamku6a6h7tvm8h3mmvs4x",
        });

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2012-10-12T07:05:27-04:00","currency":"USD","presentment_currency":"USD","customer_id":207119551,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"bob.norman@mail.example.com","legal_notice_url":null,"location_id":null,"name":"#446514532","note":"","note_attributes":{"custom engraving":"Happy Birthday","colour":"green"},"order_id":null,"order_status_url":null,"order":null,"payment_due":"419.49","payment_url":"https://app.local/cardserver/sessions","payments":[{"id":25428999,"unique_token":"e01e661f4a99acd9dcdg6f1422d0d6f7","payment_processing_error_message":null,"fraudulent":false,"transaction":{"amount":"598.94","amount_in":null,"amount_out":null,"amount_rounding":null,"authorization":"authorization-key","created_at":"2005-08-01T11:57:11-04:00","currency":"USD","error_code":null,"parent_id":null,"gateway":"bogus","id":389404469,"kind":"authorization","message":null,"status":"success","test":false,"receipt":{"testcase":true,"authorization":"123456"},"location_id":null,"user_id":null,"transaction_group_id":null,"device_id":null,"payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"}},"credit_card":null}],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":true,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"web","source_url":null,"subscription_policy_url":null,"subtotal_price":"398.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"7yjf4v2we7gamku6a6h7tvm8h3mmvs4x","total_price":"419.49","total_tax":"21.49","total_tip_received":"0.00","total_line_items_price":"398.00","updated_at":"2012-10-12T07:05:27-04:00","user_id":null,"web_url":"https://checkout.local/548380009/checkouts/7yjf4v2we7gamku6a6h7tvm8h3mmvs4x","line_items":[{"id":"60715a3461f5f853","key":"60715a3461f5f853","product_id":632910392,"variant_id":49148385,"sku":"IPOD2008RED","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Red","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[]},{"id":"0703986f986628ba","key":"0703986f986628ba","product_id":632910392,"variant_id":808950810,"sku":"IPOD2008PINK","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Pink","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[]}],"gift_cards":[],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","compare_at":0.06}],"tax_manipulations":[],"shipping_line":{"handle":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping","tax_lines":[]},"shipping_rate":{"id":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping"},"shipping_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"credit_card":{"first_name":"Bob","last_name":"Norman","first_digits":"1","last_digits":"1","brand":"bogus","expiry_month":8,"expiry_year":2042,"customer_id":null},"billing_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}

  * #### Retrieve an existing checkout

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Checkout.find({
          session: session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Checkout.find(
          session: test_session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Checkout.find({
          session: session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        });

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2012-10-12T07:05:27-04:00","currency":"USD","presentment_currency":"USD","customer_id":207119551,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"bob.norman@mail.example.com","legal_notice_url":null,"location_id":null,"name":"#862052962","note":"","note_attributes":{"custom engraving":"Happy Birthday","colour":"green"},"order_id":null,"order_status_url":null,"order":null,"payment_due":"419.49","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":true,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"web","source_url":null,"subscription_policy_url":null,"subtotal_price":"398.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","total_price":"419.49","total_tax":"21.49","total_tip_received":"0.00","total_line_items_price":"398.00","updated_at":"2012-10-12T07:05:27-04:00","user_id":null,"web_url":"https://checkout.local/548380009/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a","line_items":[{"id":"60715a3461f5f853","key":"60715a3461f5f853","product_id":632910392,"variant_id":49148385,"sku":"IPOD2008RED","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Red","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[]},{"id":"0703986f986628ba","key":"0703986f986628ba","product_id":632910392,"variant_id":808950810,"sku":"IPOD2008PINK","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Pink","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[]}],"gift_cards":[],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","compare_at":0.06}],"tax_manipulations":[],"shipping_line":{"handle":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping","tax_lines":[]},"shipping_rate":{"id":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping"},"shipping_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"credit_card":null,"billing_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}


* * *

##

[Anchor to GET request, Retrieves a list of shipping rates](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token-shipping-rates)

get

Retrieves a list of shipping rates

deprecated**deprecated**

Retrieves a list of available shipping rates for the specified checkout. Implementers need to poll this endpoint until rates become available.

Each shipping rate contains the checkout's new subtotal price, total tax, and total price in the event that this shipping rate is selected. This can be used to update the UI without performing further API requests.

To apply a shipping rate, update the checkout's shipping line with the handle of the selected rate.

###

[Anchor to Parameters of Retrieves a list of shipping rates](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token-shipping-rates-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

token

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-checkouts-token-shipping-rates-examples](/docs/api/admin-rest/latest/resources/checkout#get-checkouts-token-shipping-rates-examples)Examples

Retrieve available shipping rates

Path parameters

token=exuw7apwoycchjuwtiqg8nytfhphr62a

string**string**

required**required**

Retrieving shipping rates before they're available returns an empty array

Path parameters

token=exuw7apwoycchjuwtiqg8nytfhphr62a

string**string**

required**required**

Retrieving shipping rates when none are available for the current shipping address or cart returns an empty array

Path parameters

token=zs9ru89kuqcdagk8bz4r9hnxt22wwd42

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a/shipping_rates.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a/shipping_rates.json" \

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

HTTP/1.1 200 OK

{

"shipping_rates": [

{

"id": "shopify-Free%20Shipping-0.00",

"price": "0.00",

"title": "Free Shipping",

"checkout": {

"total_tax": "23.88",

"total_price": "421.88",

"subtotal_price": "398.00"

},

"phone_required": false,

"delivery_range": null,

"estimated_time_in_transit": null,

"handle": "shopify-Free%20Shipping-0.00"

}

]

}

### examples

  * #### Retrieve available shipping rates

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a/shipping_rates.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Checkout.shipping_rates({
          session: session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Checkout.shipping_rates(
          session: test_session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Checkout.shipping_rates({
          session: session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        });

#### response

        HTTP/1.1 200 OK{"shipping_rates":[{"id":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping","checkout":{"total_tax":"23.88","total_price":"421.88","subtotal_price":"398.00"},"phone_required":false,"delivery_range":null,"estimated_time_in_transit":null,"handle":"shopify-Free%20Shipping-0.00"}]}

  * #### Retrieving shipping rates before they're available returns an empty array

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a/shipping_rates.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Checkout.shipping_rates({
          session: session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Checkout.shipping_rates(
          session: test_session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Checkout.shipping_rates({
          session: session,
          token: "exuw7apwoycchjuwtiqg8nytfhphr62a",
        });

#### response

        HTTP/1.1 202 Accepted{"shipping_rates":[]}

  * #### Retrieving shipping rates when none are available for the current shipping address or cart returns an empty array

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/zs9ru89kuqcdagk8bz4r9hnxt22wwd42/shipping_rates.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Checkout.shipping_rates({
          session: session,
          token: "zs9ru89kuqcdagk8bz4r9hnxt22wwd42",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Checkout.shipping_rates(
          session: test_session,
          token: "zs9ru89kuqcdagk8bz4r9hnxt22wwd42",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Checkout.shipping_rates({
          session: session,
          token: "zs9ru89kuqcdagk8bz4r9hnxt22wwd42",
        });

#### response

        HTTP/1.1 200 OK{"shipping_rates":[]}


* * *

##

[Anchor to PUT request, Modifies an existing checkout](/docs/api/admin-rest/latest/resources/checkout#put-checkouts-token)

put

Modifies an existing checkout

deprecated**deprecated**

Requires `checkouts` access scope.

**Requires `checkouts` access scope.:**

Modifies an existing checkout

###

[Anchor to Parameters of Modifies an existing checkout](/docs/api/admin-rest/latest/resources/checkout#put-checkouts-token-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

token

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-checkouts-token-examples](/docs/api/admin-rest/latest/resources/checkout#put-checkouts-token-examples)Examples

Select a shipping rate

Path parameters

token=exuw7apwoycchjuwtiqg8nytfhphr62a

string**string**

required**required**

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.token:"exuw7apwoycchjuwtiqg8nytfhphr62a"

read-only**read-only**

deprecated**deprecated**

A unique identifier for a particular checkout.

checkout.shipping_line:{"handle":"shopify-Free%20Shipping-0.00"}

deprecated**deprecated**

The selected shipping rate. A new shipping rate can be selected by updating the value for `handle`. A shipping line is required when `requires_shipping` is `true`. Learn more about selecting shipping rates.

Update the shipping address and email of a checkout

Path parameters

token=exuw7apwoycchjuwtiqg8nytfhphr62a

string**string**

required**required**

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.token:"exuw7apwoycchjuwtiqg8nytfhphr62a"

read-only**read-only**

deprecated**deprecated**

A unique identifier for a particular checkout.

checkout.email:"john.smith@example.com"

deprecated**deprecated**

The customer's email address. A checkout needs to have a value for `email` or `phone` before it can be completed.

checkout.shipping_address:{"first_name":"John","last_name":"Smith","address1":"126 York St.","city":"Los Angeles","province_code":"CA","country_code":"US","phone":"(123)456-7890","zip":"90002"}

deprecated**deprecated**

The mailing address to where the checkout will be shipped. It has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city, town, or village of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code ([ISO 3166-1 alpha-2](//en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the shipping address.
  * **first_name** : The first name of the person associated with the shipping address.
  * **last_name** : The last name of the person associated with the shipping address.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the region (province, state, prefecture, …) of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the region of the shipping address.
  * **zip** : The postal code (zip, postcode, Eircode, …) of the shipping address.


Updating a shipping address with an invalid zip code fails and returns errors

Path parameters

token=exuw7apwoycchjuwtiqg8nytfhphr62a

string**string**

required**required**

Request body

checkout[](/apps/store/data-protection/protected-customer-data)

Checkout resource**Checkout resource**

Show checkout properties

checkout.token:"exuw7apwoycchjuwtiqg8nytfhphr62a"

read-only**read-only**

deprecated**deprecated**

A unique identifier for a particular checkout.

checkout.shipping_address:{"first_name":"John","last_name":"Smith","address1":"126 York St.","city":"Beverly Hills","province_code":"CA","country_code":"US","phone":"(123)456-7890","zip":"1234"}

deprecated**deprecated**

The mailing address to where the checkout will be shipped. It has the following properties:

Show shipping_address properties

  * **address1** : The street address of the shipping address.
  * **address2** : An optional additional field for the street address of the shipping address.
  * **city** : The city, town, or village of the shipping address.
  * **company** : The company of the person associated with the shipping address.
  * **country** : The name of the country of the shipping address.
  * **country_code** : The two-letter code ([ISO 3166-1 alpha-2](//en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) for the country of the shipping address.
  * **first_name** : The first name of the person associated with the shipping address.
  * **last_name** : The last name of the person associated with the shipping address.
  * **phone** : The phone number at the shipping address.
  * **province** : The name of the region (province, state, prefecture, …) of the shipping address.
  * **province_code** : The alphanumeric abbreviation of the region of the shipping address.
  * **zip** : The postal code (zip, postcode, Eircode, …) of the shipping address.


Was this section helpful?

YesNo

put

## /admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"checkout":{"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","shipping_line":{"handle":"shopify-Free%20Shipping-0.00"}}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a.json" \

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

HTTP/1.1 202 Accepted

{

"checkout": {

"completed_at": null,

"created_at": "2012-10-12T07:05:27-04:00",

"currency": "USD",

"presentment_currency": "USD",

"customer_id": 207119551,

"customer_locale": "en",

"device_id": null,

"discount_code": null,

"discount_codes": [],

"email": "bob.norman@mail.example.com",

"legal_notice_url": null,

"location_id": null,

"name": "#862052962",

"note": "",

"note_attributes": {

"custom engraving": "Happy Birthday",

"colour": "green"

},

"order_id": null,

"order_status_url": null,

"order": null,

"payment_due": "421.88",

"payment_url": "https://app.local/cardserver/sessions",

"payments": [],

"phone": null,

"shopify_payments_account_id": null,

"privacy_policy_url": null,

"refund_policy_url": null,

"requires_shipping": true,

"reservation_time_left": 0,

"reservation_time": null,

"source_identifier": null,

"source_name": "web",

### examples

  * #### Select a shipping rate

#####

        curl -d '{"checkout":{"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","shipping_line":{"handle":"shopify-Free%20Shipping-0.00"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a";
        checkout.shipping_line = {
          "handle": "shopify-Free%20Shipping-0.00"
        };
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a"
        checkout.shipping_line = {
          "handle" => "shopify-Free%20Shipping-0.00"
        }
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a";
        checkout.shipping_line = {
          "handle": "shopify-Free%20Shipping-0.00"
        };
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2012-10-12T07:05:27-04:00","currency":"USD","presentment_currency":"USD","customer_id":207119551,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"bob.norman@mail.example.com","legal_notice_url":null,"location_id":null,"name":"#862052962","note":"","note_attributes":{"custom engraving":"Happy Birthday","colour":"green"},"order_id":null,"order_status_url":null,"order":null,"payment_due":"421.88","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":true,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"web","source_url":null,"subscription_policy_url":null,"subtotal_price":"398.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","total_price":"421.88","total_tax":"23.88","total_tip_received":"0.00","total_line_items_price":"398.00","updated_at":"2026-01-09T19:34:45-05:00","user_id":null,"web_url":"https://checkout.local/548380009/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a","line_items":[{"id":"60715a3461f5f853","key":"60715a3461f5f853","product_id":632910392,"variant_id":49148385,"sku":"IPOD2008RED","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Red","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"11.94","rate":0.06,"title":"Tax","channel_liable":false}]},{"id":"0703986f986628ba","key":"0703986f986628ba","product_id":632910392,"variant_id":808950810,"sku":"IPOD2008PINK","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Pink","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"11.94","rate":0.06,"title":"Tax","channel_liable":false}]}],"gift_cards":[],"tax_lines":[{"price":"23.88","rate":0.06,"title":"Tax","compare_at":0.06}],"tax_manipulations":[],"shipping_line":{"handle":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping","tax_lines":[]},"shipping_rate":{"id":"shopify-Free%20Shipping-0.00","price":"0.00","title":"Free Shipping"},"shipping_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"credit_card":null,"billing_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}

  * #### Update the shipping address and email of a checkout

#####

        curl -d '{"checkout":{"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","email":"john.smith@example.com","shipping_address":{"first_name":"John","last_name":"Smith","address1":"126 York St.","city":"Los Angeles","province_code":"CA","country_code":"US","phone":"(123)456-7890","zip":"90002"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a";
        checkout.email = "john.smith@example.com";
        checkout.shipping_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "126 York St.",
          "city": "Los Angeles",
          "province_code": "CA",
          "country_code": "US",
          "phone": "(123)456-7890",
          "zip": "90002"
        };
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a"
        checkout.email = "john.smith@example.com"
        checkout.shipping_address = {
          "first_name" => "John",
          "last_name" => "Smith",
          "address1" => "126 York St.",
          "city" => "Los Angeles",
          "province_code" => "CA",
          "country_code" => "US",
          "phone" => "(123)456-7890",
          "zip" => "90002"
        }
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a";
        checkout.email = "john.smith@example.com";
        checkout.shipping_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "126 York St.",
          "city": "Los Angeles",
          "province_code": "CA",
          "country_code": "US",
          "phone": "(123)456-7890",
          "zip": "90002"
        };
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 202 Accepted{"checkout":{"completed_at":null,"created_at":"2012-10-12T07:05:27-04:00","currency":"USD","presentment_currency":"USD","customer_id":207119551,"customer_locale":"en","device_id":null,"discount_code":null,"discount_codes":[],"email":"john.smith@example.com","legal_notice_url":null,"location_id":null,"name":"#862052962","note":"","note_attributes":{"custom engraving":"Happy Birthday","colour":"green"},"order_id":null,"order_status_url":null,"order":null,"payment_due":"417.90","payment_url":"https://app.local/cardserver/sessions","payments":[],"phone":null,"shopify_payments_account_id":null,"privacy_policy_url":null,"refund_policy_url":null,"requires_shipping":true,"reservation_time_left":0,"reservation_time":null,"source_identifier":null,"source_name":"web","source_url":null,"subscription_policy_url":null,"subtotal_price":"398.00","shipping_policy_url":null,"tax_exempt":false,"taxes_included":false,"terms_of_sale_url":null,"terms_of_service_url":null,"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","total_price":"417.90","total_tax":"19.90","total_tip_received":"0.00","total_line_items_price":"398.00","updated_at":"2026-01-09T19:34:37-05:00","user_id":null,"web_url":"https://checkout.local/548380009/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a?key=a9763049ee3bebeee21ad632ec902686","line_items":[{"id":"60715a3461f5f853","key":"60715a3461f5f853","product_id":632910392,"variant_id":49148385,"sku":"IPOD2008RED","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Red","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"9.95","rate":0.05,"title":"Tax","channel_liable":false}]},{"id":"0703986f986628ba","key":"0703986f986628ba","product_id":632910392,"variant_id":808950810,"sku":"IPOD2008PINK","vendor":"Apple","title":"IPod Nano - 8GB","variant_title":"Pink","image_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251","taxable":true,"requires_shipping":true,"gift_card":false,"price":"199.00","compare_at_price":null,"line_price":"199.00","properties":{},"quantity":1,"grams":200,"fulfillment_service":"manual","applied_discounts":[],"discount_allocations":[],"tax_lines":[{"price":"9.95","rate":0.05,"title":"Tax","channel_liable":false}]}],"gift_cards":[],"tax_lines":[{"price":"19.90","rate":0.05,"title":"Tax","compare_at":0.05}],"tax_manipulations":[],"shipping_line":null,"shipping_rate":null,"shipping_address":{"id":921093900,"first_name":"John","last_name":"Smith","phone":"(123)456-7890","company":null,"address1":"126 York St.","address2":"","city":"Los Angeles","province":"California","province_code":"CA","country":"United States","country_code":"US","zip":"90002"},"credit_card":null,"billing_address":{"id":921093900,"first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","province_code":"KY","country":"United States","country_code":"US","zip":"40202"},"applied_discount":null,"applied_discounts":[],"discount_violations":[]}}

  * #### Updating a shipping address with an invalid zip code fails and returns errors

#####

        curl -d '{"checkout":{"token":"exuw7apwoycchjuwtiqg8nytfhphr62a","shipping_address":{"first_name":"John","last_name":"Smith","address1":"126 York St.","city":"Beverly Hills","province_code":"CA","country_code":"US","phone":"(123)456-7890","zip":"1234"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts/exuw7apwoycchjuwtiqg8nytfhphr62a.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const checkout = new admin.rest.resources.Checkout({session: session});

        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a";
        checkout.shipping_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "126 York St.",
          "city": "Beverly Hills",
          "province_code": "CA",
          "country_code": "US",
          "phone": "(123)456-7890",
          "zip": "1234"
        };
        await checkout.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        checkout = ShopifyAPI::Checkout.new(session: test_session)
        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a"
        checkout.shipping_address = {
          "first_name" => "John",
          "last_name" => "Smith",
          "address1" => "126 York St.",
          "city" => "Beverly Hills",
          "province_code" => "CA",
          "country_code" => "US",
          "phone" => "(123)456-7890",
          "zip" => "1234"
        }
        checkout.save!

#####

        // Session is built by the OAuth process

        const checkout = new shopify.rest.Checkout({session: session});
        checkout.token = "exuw7apwoycchjuwtiqg8nytfhphr62a";
        checkout.shipping_address = {
          "first_name": "John",
          "last_name": "Smith",
          "address1": "126 York St.",
          "city": "Beverly Hills",
          "province_code": "CA",
          "country_code": "US",
          "phone": "(123)456-7890",
          "zip": "1234"
        };
        await checkout.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"shipping_address":{"zip":[{"code":"invalid_for_country","message":"Enter a valid ZIP code for the United States","options":{"country":"United States"}}]}}}