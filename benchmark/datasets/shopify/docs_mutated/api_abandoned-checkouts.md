# Abandoned checkouts

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/abandoned-checkouts*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Abandoned checkouts

Ask assistant

Requires `orders` access scope.

**Requires `orders` access scope.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

You can use the [Abandoned checkouts](/api/admin-rest/latest/resources/abandoned-checkouts#resource_object) resource to retrieve a list and a count of abandoned checkouts. A checkout is considered abandoned after the customer has added contact information, but before the customer has completed their purchase.

This resource may be helpful to complete the following actions:

  * Gather marketing information on customers who have abandoned their cart.
  * Use information to remarket to abandoned checkout customers.
  * Understand customers’ behavior.
  * Track abandoned checkouts over time.
  * View abandoned checkout items.


Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/checkouts.json?created_at_max=2013-10-12T07:05:27-02:00](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?created-at-max=2013-10-12T07:05:27-02:00)

Retrieves a count of checkouts

[abandonedCheckoutsCount](/docs/api/admin-graphql/latest/queries/abandonedCheckoutsCount?example=retrieves-a-count-of-checkouts)

  * [get/admin/api/latest/checkouts.json?count=1](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?count=1)

Retrieves a list of abandoned checkouts

[abandonedCheckouts](/docs/api/admin-graphql/latest/queries/abandonedCheckouts?example=retrieves-a-list-of-abandoned-checkouts)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/abandoned-checkouts#resource-object)

## The Abandoned checkouts resource

[Anchor to ](/docs/api/admin-rest/latest/resources/abandoned-checkouts#resource-object-properties)

### Properties

* * *

abandoned_checkout_url

->[abandonedCheckoutUrl](/docs/api/admin-graphql/latest/objects/AbandonedCheckout#field-AbandonedCheckout.fields.abandonedCheckoutUrl)

The recovery URL that's sent to a customer so they can recover their checkout.

* * *

billing_address

[](/apps/store/data-protection/protected-customer-data)

->[billingAddress](/docs/api/admin-graphql/latest/objects/AbandonedCheckout#field-AbandonedCheckout.fields.billingAddress)

The mailing address associated with the payment method. It has the following properties:

Show billing_address properties

  * **address1** : The street address of the billing address.
  * **address2** : An optional additional field for the street address of the billing address.
  * **city** : The city of the billing address.
  * **company** : The company of the person associated with the billing address.
  * **country** : The name of the country of the billing address.
  * **country_code** : The two-letter code ([ISO 3166-1 alpha-2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) for the country of the billing address.
  * **default** : Whether this is the default address for the customer.
  * **first_name** : The first name of the person associated with the payment method.
  * **last_name** : The last name of the person associated with the payment method.
  * **latitude** : The latitude of the billing address.
  * **longitude** : The longitude of the billing address.
  * **name** : The full name of the person associated with the payment method.
  * **phone** : The phone number at the billing address.
  * **province** : The name of the state or province of the billing address.
  * **province_code** : The alphanumeric abbreviation of the state or province of the billing address.
  * **zip** : The zip or postal code of the billing address.


* * *

buyer_accepts_marketing

->[emailMarketingConsent](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.emailMarketingConsent)

Whether the customer would like to receive email updates from the shop. This is set by the **I want to receive occasional emails about new products, promotions and other news** checkbox during checkout.

* * *

buyer_accepts_sms_marketing

->[smsMarketingConsent](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.smsMarketingConsent)

Whether the customer would like to receive SMS updates from the shop. This is set by the **Text me with news and offers** checkbox during checkout.

* * *

cart_token

deprecated**deprecated**

The ID for the cart that's attached to the checkout.

* * *

closed_at

deprecated**deprecated**

The date and time ([ISO 8601 format](//en.wikipedia.org/wiki/ISO_8601)) when the checkout was closed. If the checkout was not closed, then this value is `null`.

* * *

completed_at

->[completedAt](/docs/api/admin-graphql/latest/objects/AbandonedCheckout#field-AbandonedCheckout.fields.completedAt)

The date and time ([ISO 8601 format](//en.wikipedia.org/wiki/ISO_8601)) when the checkout was completed. For abandoned checkouts, this value is `null` until a customer completes the checkout using the recovery URL.

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/AbandonedCheckout#field-AbandonedCheckout.fields.createdAt)

The date and time ([ISO 8601 format](//en.wikipedia.org/wiki/ISO_8601)) when the checkout was created.

* * *

currency

deprecated**deprecated**

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) of the shop's default currency at the time of checkout. For the currency that the customer used at checkout, see `presentment_currency`.

* * *

customer

[](/apps/store/data-protection/protected-customer-data)

->[customer](/docs/api/admin-graphql/latest/objects/AbandonedCheckout#field-AbandonedCheckout.fields.customer)

The customer details associated with the abandoned checkout. For more information, refer to the [Customer](/api/admin-rest/latest/resources/customer) resource.

* * *

customer_locale

->[locale](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.locale)

The two or three-letter language code, optionally followed by a region modifier. Example values: `en`, `en-CA`.

* * *

device_id

deprecated**deprecated**

The ID of the Shopify POS device that created the checkout. This field is **deprecated**.

* * *

Show 27 hidden fields

Was this section helpful?

YesNo

{}

## The Abandoned checkouts resource

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

{

"abandoned_checkout_url": "https://www.snowdevil.ca/14168/checkouts/0123456789abcdef0456456789abcdef/recover?key=6dacd6065bb80268bda857ee",

"billing_address": {

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"country_code": "US",

"default": true,

"first_name": "Greg",

"id": 207119551,

"last_name": "Piotrowski",

"name": "Greg Piotrowski",

"phone": "555-625-1199",

"province": "Kentucky",

"province_code": "KY",

"zip": "40202"

},

"buyer_accepts_marketing": false,

"buyer_accepts_sms_marketing": false,

"cart_token": "0123456789abcdef0456456789abcdef",

"closed_at": null,

"completed_at": null,

"created_at": "2008-01-10T11:00:00-05:00",

"currency": {

"currency": "USD"

},

"customer": {

"accepts_marketing": false,

"created_at": "2012-03-13T16:09:55-04:00",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"id": 207119551,

"last_name": "Norman",

"note": null,

"orders_count": "0",

"state": null,

"total_spent": "0.00",

"updated_at": "2012-03-13T16:09:55-04:00",

"tags": "tagcity"

},

"customer_locale": "fr",

"device_id": 1,

"discount_codes": [

{

"discount_code": {

"id": 507328175,

"code": "WINTERSALE20OFF",

"usage_count": 0,

"created_at": "2017-09-25T19:32:28-04:00",

"updated_at": "2017-09-25T19:32:28-04:00"

}

}

],

"email": "bob.norman@mail.example.com",

"gateway": "authorize_net",

"id": 450789469,

"landing_site": "http://www.example.com?source=abc",

"line_items": {

"price": 214,

"product_id": 431300801,

"quantity": 4,

"sku": "SKU123",

"title": "Jib",

"variant_id": 233402193,

"variant_title": "Green",

"vendor": "Ottawa Sail Shop"

},

"location_id": 1,

"note": null,

"phone": {

"phone": "+13125551212"

},

"presentment_currency": {

"presentment_currency": "USD"

},

"referring_site": "http://www.anexample.com",

"shipping_address": {

"address1": "Chestnut Street 92",

"address2": "Apt 2",

"city": "Louisville",

"company": null,

"country": "United States",

"first_name": "Bob",

"last_name": "Norman",

"latitude": "45.41634",

"longitude": "-75.6868",

"phone": "555-625-1199",

"province": "Kentucky",

"zip": "40202",

"name": "Bob Norman",

"country_code": "US",

"province_code": "KY"

},

"sms_marketing_phone": "+16135555555",

"shipping_lines": {

"code": "Free Shipping",

"price": "0.00",

"source": "shopify",

"title": "Free Shipping"

},

"source_name": "web",

"subtotal_price": "398.00",

"tax_lines": {

"price": "11.94",

"rate": 0.06,

"title": "State Tax",

"channel_liable": true

},

"taxes_included": false,

"token": "b1946ac92492d2347c6235b4d2611184",

"total_discounts": "0.00",

"total_duties": "105.31",

"total_line_items_price": "398.00",

"total_price": "409.94",

"total_tax": "11.94",

"total_weight": 400,

"updated_at": "2012-08-24T14:02:15-04:00",

"user_id": 1

}

* * *

##

[Anchor to GET request, Retrieves a count of checkouts](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?created-at-max=2013-10-12T07:05:27-02:00)

get

Retrieves a count of checkouts

[abandonedCheckoutsCount](/docs/api/admin-graphql/latest/queries/abandonedCheckoutsCount?example=retrieves-a-count-of-checkouts)

Retrieves a count of checkouts from the past 90 days

###

[Anchor to Parameters of Retrieves a count of checkouts](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?created-at-max=2013-10-12T07:05:27-02:00-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Count checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

created_after

Count checkouts created after the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

after_id

Restrict results to after the specified ID.

* * *

status

default open**default open**

Count checkouts with a given status.

Show status properties

  * **open** : Count only open abandoned checkouts.

  * **closed** : Count only closed abandoned checkouts that have been archived.


* * *

updated_at_max

Count checkouts last updated before the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Count checkouts last updated after the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-checkouts?created-at-max=2013-10-12T07:05:27-02:00-examples](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?created-at-max=2013-10-12T07:05:27-02:00-examples)Examples

Count abandoned checkouts created before date specified

Query parameters

created_at_max=2013-10-12T07:05:27-02:00

Count checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00)

Count all abandoned checkouts

Count closed abandoned checkouts

Query parameters

status=closed

default open**default open**

Count checkouts with a given status.

Show status properties

  * **open** : Count only open abandoned checkouts.

  * **closed** : Count only closed abandoned checkouts that have been archived.


Was this section helpful?

YesNo

get

## /admin/api/2026-01/checkouts.json?created_at_max=2013-10-12T07:05:27-02:00

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?created_at_max=2013-10-12T07%3A05%3A27-02%3A00" \

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

"checkouts": [

{

"id": 450789469,

"token": "2a1ace52255252df566af0faaedfbfa7",

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"email": "bob.norman@mail.example.com",

"gateway": null,

"buyer_accepts_marketing": false,

"created_at": "2012-10-12T07:05:27-04:00",

"updated_at": "2012-10-12T07:05:27-04:00",

"landing_site": null,

"note": null,

"note_attributes": [

{

"name": "custom engraving",

"value": "Happy Birthday"

},

{

"name": "colour",

"value": "green"

}

],

"referring_site": null,

"shipping_lines": [

{

"code": "Free Shipping",

"price": "0.00",

"original_shop_price": null,

"original_rate_price": null,

"original_shop_markup": null,

"source": "shopify",

"title": "Free Shipping",

"presentment_title": null,

"phone": null,

### examples

  * #### Count abandoned checkouts created before date specified

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?created_at_max=2013-10-12T07%3A05%3A27-02%3A00" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
          created_at_max: "2013-10-12T07:05:27-02:00",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
          created_at_max: "2013-10-12T07:05:27-02:00",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
          created_at_max: "2013-10-12T07:05:27-02:00",
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}

  * #### Count all abandoned checkouts

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}

  * #### Count closed abandoned checkouts

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?status=closed" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
          status: "closed",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
          status: "closed",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
          status: "closed",
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}


* * *

##

[Anchor to GET request, Retrieves a list of abandoned checkouts](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?count=1)

get

Retrieves a list of abandoned checkouts

[abandonedCheckouts](/docs/api/admin-graphql/latest/queries/abandonedCheckouts?example=retrieves-a-list-of-abandoned-checkouts)

Retrieves a list of abandoned checkouts.

###

[Anchor to Parameters of Retrieves a list of abandoned checkouts](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?count=1-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Show checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

created_after

Show checkouts created after the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

after_id

Restrict results to after the specified ID.

* * *

status

default open**default open**

Show only checkouts with a given status.

Show status properties

  * **open** : Show only open abandoned checkouts.

  * **closed** : Count only closed abandoned checkouts that have been archived.


* * *

updated_at_max

Show checkouts last updated before the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Show checkouts last updated after the specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-checkouts?count=1-examples](/docs/api/admin-rest/latest/resources/abandoned-checkouts#get-checkouts?count=1-examples)Examples

Retrieve a limited number of abandoned checkouts

Query parameters

count=1

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

Retrieve all abandoned checkouts

Retrieve checkouts created before date specified

Query parameters

created_at_max=2013-10-12T07:05:27-02:00

Show checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00)

Retrieve closed abandoned checkouts

Query parameters

status=closed

default open**default open**

Show only checkouts with a given status.

Show status properties

  * **open** : Show only open abandoned checkouts.

  * **closed** : Count only closed abandoned checkouts that have been archived.


Was this section helpful?

YesNo

get

## /admin/api/2026-01/checkouts.json?count=1

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?count=1" \

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

"checkouts": [

{

"id": 450789469,

"token": "2a1ace52255252df566af0faaedfbfa7",

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"email": "bob.norman@mail.example.com",

"gateway": null,

"buyer_accepts_marketing": false,

"created_at": "2012-10-12T07:05:27-04:00",

"updated_at": "2012-10-12T07:05:27-04:00",

"landing_site": null,

"note": null,

"note_attributes": [

{

"name": "custom engraving",

"value": "Happy Birthday"

},

{

"name": "colour",

"value": "green"

}

],

"referring_site": null,

"shipping_lines": [

{

"code": "Free Shipping",

"price": "0.00",

"original_shop_price": null,

"original_rate_price": null,

"original_shop_markup": null,

"source": "shopify",

"title": "Free Shipping",

"presentment_title": null,

"phone": null,

### examples

  * #### Retrieve a limited number of abandoned checkouts

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?count=1" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
          count: "1",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
          count: "1",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
          count: "1",
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}

  * #### Retrieve all abandoned checkouts

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}

  * #### Retrieve checkouts created before date specified

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?created_at_max=2013-10-12T07%3A05%3A27-02%3A00" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
          created_at_max: "2013-10-12T07:05:27-02:00",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
          created_at_max: "2013-10-12T07:05:27-02:00",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
          created_at_max: "2013-10-12T07:05:27-02:00",
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}

  * #### Retrieve closed abandoned checkouts

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/checkouts.json?status=closed" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AbandonedCheckout.checkouts({
          session: session,
          status: "closed",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AbandonedCheckout.checkouts(
          session: test_session,
          status: "closed",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AbandonedCheckout.checkouts({
          session: session,
          status: "closed",
        });

#### response

        HTTP/1.1 200 OK{"checkouts":[{"id":450789469,"token":"2a1ace52255252df566af0faaedfbfa7","cart_token":"68778783ad298f1c80c3bafcddeea02f","email":"bob.norman@mail.example.com","gateway":null,"buyer_accepts_marketing":false,"created_at":"2012-10-12T07:05:27-04:00","updated_at":"2012-10-12T07:05:27-04:00","landing_site":null,"note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"referring_site":null,"shipping_lines":[{"code":"Free Shipping","price":"0.00","original_shop_price":null,"original_rate_price":null,"original_shop_markup":null,"source":"shopify","title":"Free Shipping","presentment_title":null,"phone":null,"tax_lines":null,"custom_tax_lines":null,"markup":null,"delivery_category":null,"carrier_identifier":null,"carrier_service_id":null,"api_client_id":null,"requested_fulfillment_service_id":null,"applied_discounts":[],"delivery_option_group_type":null,"delivery_expectation_range":null,"delivery_expectation_type":null,"estimated_delivery_time_range":null,"id":"5da41c1738454765","validation_context":null}],"taxes_included":false,"total_weight":400,"currency":"USD","completed_at":null,"closed_at":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"device_id":null,"phone":null,"customer_locale":"en","line_items":[{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"f32827a8d00b0a8d","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Red","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":49148385,"variant_title":"Red","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"},{"applied_discounts":[],"discount_allocations":[{"id":null,"amount":"19.90","description":"TENOFF","created_at":null,"application_type":"discount_code","discount_class":"ORDER"}],"key":"7e8c529027b9a00e","destination_location_id":null,"fulfillment_service":"manual","gift_card":false,"grams":200,"origin_location_id":null,"presentment_title":"IPod Nano - 8GB","presentment_variant_title":"Pink","product_id":632910392,"properties":null,"quantity":1,"requires_shipping":true,"sku":"IPOD2008PINK","tax_lines":[],"taxable":true,"title":"IPod Nano - 8GB","variant_id":808950810,"variant_title":"Pink","variant_price":null,"vendor":"Apple","user_id":null,"unit_price_measurement":null,"rank":null,"compare_at_price":null,"line_price":"199.00","price":"199.00"}],"name":"#450789469","source":null,"abandoned_checkout_url":"https://checkout.local/548380009/checkouts/2a1ace52255252df566af0faaedfbfa7/recover","discount_codes":[{"code":"TENOFF","amount":"39.80","type":"percentage"}],"tax_lines":[{"price":"21.49","rate":0.06,"title":"State Tax","channel_liable":null}],"source_name":"web","presentment_currency":"USD","buyer_accepts_sms_marketing":false,"sms_marketing_phone":null,"total_discounts":"39.80","total_line_items_price":"398.00","total_price":"379.69","total_tax":"21.49","subtotal_price":"358.20","total_duties":null,"reservation_token":"0123456789abcdef0123456789zjkw","billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}]}