# Shop

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/shop*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Shop

Ask assistant

The Shop resource is a collection of general business and store management settings and information about the store. The resource lets you retrieve information about the store, but it doesn't let you update any information. Only the merchant can update this information from inside the Shopify admin.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/shop.json](/docs/api/admin-rest/latest/resources/shop#get-shop)

Retrieves the shop's configuration

[shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-the-shops-configuration)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/shop#resource-object)

## The Shop resource

[Anchor to ](/docs/api/admin-rest/latest/resources/shop#resource-object-properties)

### Properties

* * *

address1

->[address1](/docs/api/admin-graphql/latest/objects/ShopAddress#field-ShopAddress.fields.address1)

The shop's street address.

* * *

address2

->[address2](/docs/api/admin-graphql/latest/objects/ShopAddress#field-ShopAddress.fields.address2)

The optional second line of the shop's street address.

* * *

auto_configure_tax_inclusivity

deprecated**deprecated**

The setting for whether applicable taxes are included automatically, based on buyer's location.

* * *

checkout_api_supported

->[checkoutApiSupported](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.checkoutApiSupported)

Whether the shop is capable of accepting payments directly through the [Checkout API](/docs/api/admin-rest/current/resources/checkout).

* * *

city

->[city](/docs/api/admin-graphql/latest/objects/ShopAddress#field-ShopAddress.fields.city)

The shop's city.

* * *

country

->[country](/docs/api/admin-graphql/latest/objects/ShopAddress#field-ShopAddress.fields.country)

The shop's country. In most cases, this value matches the `country_code`.

* * *

country_code

->[countryCodeV2](/docs/api/admin-graphql/latest/objects/ShopAddress#field-ShopAddress.fields.countryCodeV2)

The two-letter country code corresponding to the shop's country.

* * *

country_name

->[country](/docs/api/admin-graphql/latest/objects/ShopAddress#field-ShopAddress.fields.country)

The shop's normalized country name.

* * *

county_taxes

boolean**boolean**

deprecated**deprecated**

Whether the shop is applying taxes on a per-county basis. Only applicable to shops based in the US. Valid values: `true` or `null`."

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) when the shop was created.

* * *

customer_email

->[contactEmail](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.contactEmail)

The contact email used for communication between the shop owner and the customer.

* * *

currency

->[currencyCode](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencyCode)

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the shop's default currency.

* * *

Show 43 hidden fields

Was this section helpful?

YesNo

{}

## The Shop resource

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

{

"address1": "1 Infinite Loop",

"address2": "Suite 100",

"auto_configure_tax_inclusivity": true,

"checkout_api_supported": true,

"city": "Cupertino",

"country": "US",

"country_code": "US",

"country_name": "United States",

"county_taxes": null,

"created_at": "2007-12-31T19:00:00-05:00",

"customer_email": "customers@apple.com",

"currency": "USD",

"domain": "shop.apple.com",

"enabled_presentment_currencies": [

"CAD",

"GBP",

"USD",

"JPY"

],

"eligible_for_payments": true,

"email": "j.smith@example.com",

"finances": true,

"force_ssl": true,

"google_apps_domain": null,

"google_apps_login_enabled": null,

"has_discounts": false,

"has_gift_cards": true,

"has_storefront": true,

"iana_timezone": "America/New_York",

"id": 548380009,

"latitude": 45.427408,

"longitude": -75.68903,

"money_format": "${{amount}}",

"money_in_emails_format": "${{amount}}",

"money_with_currency_format": "${{amount}} USD",

"money_with_currency_in_emails_format": "${{amount}} USD",

"multi_location_enabled": true,

"myshopify_domain": "jsmith.myshopify.com",

"name": "John Smith Test Store",

"password_enabled": false,

"phone": null,

"plan_display_name": "enterprise",

"pre_launch_enabled": false,

"plan_name": "enterprise",

"primary_locale": "fr",

"primary_location_id": 905684977,

"province": "California",

"province_code": "CA",

"requires_extra_payments_agreement": false,

"setup_required": false,

"shop_owner": "John Smith",

"source": null,

"taxes_included": null,

"tax_shipping": null,

"timezone": "(GMT-05:00) Eastern Time",

"transactional_sms_disabled": false,

"updated_at": "2007-12-31T19:00:00-05:00",

"weight_unit": "lb",

"zip": "95014",

"marketing_sms_consent_enabled_at_checkout": true

}

* * *

##

[Anchor to GET request, Retrieves the shop's configuration](/docs/api/admin-rest/latest/resources/shop#get-shop)

get

Retrieves the shop's configuration

[shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-the-shops-configuration)

Retrieves the shop's configuration

###

[Anchor to Parameters of Retrieves the shop's configuration](/docs/api/admin-rest/latest/resources/shop#get-shop-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-shop-examples](/docs/api/admin-rest/latest/resources/shop#get-shop-examples)Examples

Retrieve the shop's configuration

Retrieve the shop's mailing address

Query parameters

fields=address1,address2,city,province,country

A comma-separated list of fields to include in the response.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/shop.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shop.json" \

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

HTTP/1.1 200 OK

{

"shop": {

"id": 548380009,

"name": "John Smith Test Store",

"email": "j.smith@example.com",

"domain": "shop.apple.com",

"province": "California",

"country": "US",

"address1": "1 Infinite Loop",

"zip": "95014",

"city": "Cupertino",

"source": null,

"phone": "1231231234",

"latitude": 45.45,

"longitude": -75.43,

"primary_locale": "en",

"address2": "Suite 100",

"created_at": "2007-12-31T19:00:00-05:00",

"updated_at": "2026-01-09T19:37:58-05:00",

"country_code": "US",

"country_name": "United States",

"currency": "USD",

"customer_email": "customers@apple.com",

"timezone": "(GMT-05:00) Eastern Time (US & Canada)",

"iana_timezone": "America/New_York",

"shop_owner": "John Smith",

"money_format": "${{amount}}",

"money_with_currency_format": "${{amount}} USD",

"weight_unit": "lb",

"province_code": "CA",

"taxes_included": null,

"auto_configure_tax_inclusivity": null,

"tax_shipping": null,

"county_taxes": true,

"plan_display_name": "Shopify Plus",

"plan_name": "enterprise",

"has_discounts": true,

"has_gift_cards": true,

"myshopify_domain": "jsmith.myshopify.com",

"google_apps_domain": null,

"google_apps_login_enabled": null,

"money_in_emails_format": "${{amount}}",

"money_with_currency_in_emails_format": "${{amount}} USD",

"eligible_for_payments": true,

"requires_extra_payments_agreement": false,

"password_enabled": false,

"has_storefront": true,

"finances": true,

"primary_location_id": 655441491,

"checkout_api_supported": true,

"multi_location_enabled": true,

"setup_required": false,

"pre_launch_enabled": false,

"enabled_presentment_currencies": [

"USD"

],

"marketing_sms_consent_enabled_at_checkout": false,

"transactional_sms_disabled": false

}

}

### examples

  * #### Retrieve the shop's configuration

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shop.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Shop.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Shop.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Shop.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"shop":{"id":548380009,"name":"John Smith Test Store","email":"j.smith@example.com","domain":"shop.apple.com","province":"California","country":"US","address1":"1 Infinite Loop","zip":"95014","city":"Cupertino","source":null,"phone":"1231231234","latitude":45.45,"longitude":-75.43,"primary_locale":"en","address2":"Suite 100","created_at":"2007-12-31T19:00:00-05:00","updated_at":"2026-01-09T19:37:58-05:00","country_code":"US","country_name":"United States","currency":"USD","customer_email":"customers@apple.com","timezone":"(GMT-05:00) Eastern Time (US & Canada)","iana_timezone":"America/New_York","shop_owner":"John Smith","money_format":"${{amount}}","money_with_currency_format":"${{amount}} USD","weight_unit":"lb","province_code":"CA","taxes_included":null,"auto_configure_tax_inclusivity":null,"tax_shipping":null,"county_taxes":true,"plan_display_name":"Shopify Plus","plan_name":"enterprise","has_discounts":true,"has_gift_cards":true,"myshopify_domain":"jsmith.myshopify.com","google_apps_domain":null,"google_apps_login_enabled":null,"money_in_emails_format":"${{amount}}","money_with_currency_in_emails_format":"${{amount}} USD","eligible_for_payments":true,"requires_extra_payments_agreement":false,"password_enabled":false,"has_storefront":true,"finances":true,"primary_location_id":655441491,"checkout_api_supported":true,"multi_location_enabled":true,"setup_required":false,"pre_launch_enabled":false,"enabled_presentment_currencies":["USD"],"marketing_sms_consent_enabled_at_checkout":false,"transactional_sms_disabled":false}}

  * #### Retrieve the shop's mailing address

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shop.json?fields=address1%2Caddress2%2Ccity%2Cprovince%2Ccountry" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Shop.all({
          session: session,
          fields: "address1,address2,city,province,country",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Shop.all(
          session: test_session,
          fields: "address1,address2,city,province,country",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Shop.all({
          session: session,
          fields: "address1,address2,city,province,country",
        });

#### response

        HTTP/1.1 200 OK{"shop":{"province":"California","country":"US","address1":"1 Infinite Loop","city":"Cupertino","address2":"Suite 100"}}