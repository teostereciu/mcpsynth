# Currency

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/currency*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Currency

Ask assistant

Merchants who use Shopify Payments can allow customers to pay in their local currency on the online store. When a customer selects a currency, all prices on the online store and checkout are automatically converted to that currency. Merchants enable the currencies that they want to offer to customers from their Shopify Payments settings.

The Currency resource represents a currency that the merchant has enabled. For each enabled currency, the Currency resource returns the currency code and the time when its conversion rate was last updated.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/currencies.json](/docs/api/admin-rest/latest/resources/currency#get-currencies)

Retrieves a list of currencies enabled on a shop

[shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-currencies-enabled-on-a-shop)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/currency#resource-object)

## The Currency resource

[Anchor to ](/docs/api/admin-rest/latest/resources/currency#resource-object-properties)

### Properties

* * *

currency

->[currencyCode](/docs/api/admin-graphql/latest/objects/CurrencySetting#field-CurrencySetting.fields.currencyCode)

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency associated with this setting.

* * *

rate_updated_at

->[rateUpdatedAt](/docs/api/admin-graphql/latest/objects/CurrencySetting#field-CurrencySetting.fields.rateUpdatedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the conversion rate associated with this currency was last updated. If manual FX rates are active on a shop, then the updated date of these rates will replace the automatic conversion rates. Conversion rates are checked every 15 minutes, but typically updated only a few times a day. Manual FX rates are updated at the merchant's request.

* * *

Was this section helpful?

YesNo

{}

## The Currency resource

9

1

2

3

4

{

"currency": "JPY",

"rate_updated_at": "2018-10-03T14:44:08-04:00"

}

* * *

##

[Anchor to GET request, Retrieves a list of currencies enabled on a shop](/docs/api/admin-rest/latest/resources/currency#get-currencies)

get

Retrieves a list of currencies enabled on a shop

[shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-currencies-enabled-on-a-shop)

Retrieves a list of currencies enabled on a shop

###

[Anchor to Parameters of Retrieves a list of currencies enabled on a shop](/docs/api/admin-rest/latest/resources/currency#get-currencies-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-currencies-examples](/docs/api/admin-rest/latest/resources/currency#get-currencies-examples)Examples

Retrieve a list of currencies enabled on a shop

Was this section helpful?

YesNo

get

## /admin/api/2026-01/currencies.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/currencies.json" \

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

HTTP/1.1 200 OK

{

"currencies": [

{

"currency": "CAD",

"rate_updated_at": "2018-01-23T19:01:01-05:00",

"enabled": true

},

{

"currency": "EUR",

"rate_updated_at": "2018-01-23T19:01:01-05:00",

"enabled": true

},

{

"currency": "JPY",

"rate_updated_at": "2018-01-23T19:01:01-05:00",

"enabled": true

}

]

}

### examples

  * #### Retrieve a list of currencies enabled on a shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/currencies.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Currency.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Currency.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Currency.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"currencies":[{"currency":"CAD","rate_updated_at":"2018-01-23T19:01:01-05:00","enabled":true},{"currency":"EUR","rate_updated_at":"2018-01-23T19:01:01-05:00","enabled":true},{"currency":"JPY","rate_updated_at":"2018-01-23T19:01:01-05:00","enabled":true}]}