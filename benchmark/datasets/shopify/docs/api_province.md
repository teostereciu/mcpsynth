# Province

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/province*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Province

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Important

The REST Province API is deprecated as of version 2024-07.

Please refer to the documentation for each individual endpoint and the [developer changelog](https://shopify.dev/changelog/deprecation-notice-country-and-province-endpoints-in-admin-rest-api) for more information.

**Important:**

The REST Province API is deprecated as of version 2024-07.

Please refer to the documentation for each individual endpoint and the [developer changelog](https://shopify.dev/changelog/deprecation-notice-country-and-province-endpoints-in-admin-rest-api) for more information.

The Province resource represents the sales tax that's applied to orders based the sub-regions of a country. Sub-regions might include counties, emirates, governorates, prefectures, provinces, regions, states, and territories.

You can use the Province resource to retrieve and update available sub-regions for only the countries that a shop owner has added to a shipping zone. Merchants add countries to a shipping zone from the **Shipping** page of their Shopify admin.

For information on accessing the tax information for an entire country, including its provinces, see the [Country](/api/admin-rest/latest/resources/country) resource.

Caution

As of version 2020-10, you can no longer update custom tax values for the Province resource.

**Caution:**

As of version 2020-10, you can no longer update custom tax values for the Province resource.

## Countries that have provinces in Shopify

Shopify provides provincial tax rates for the following countries:

A-J| M-Z
---|---
Argentina (24 provinces)| Mexico (32 states)
Australia (8 states/territories)| New Zealand (16 regions)
Brazil (27 states)| Nigeria (37 states)
Canada (13 provinces/territories)| Panama (13 regions)
Chile (16 regions)| Peru (26 regions)
China (31 provinces)| Philippines (82 provinces)
Colombia (33 provinces)| Portugal (20 regions)
Egypt (29 governorates)| Romania (42 counties)
Guatemala (22 regions)| Russia (82 regions)
Hong Kong (3 regions)| South Africa (9 provinces)
India (36 states)| South Korea (17 provinces)
Indonesia (34 provinces)| Spain (52 provinces)
Ireland (26 counties)| Thailand (78 provinces)
Italy (110 provinces)| United Arab Emirates (7 emirates)
Japan (47 prefectures)| United Kingdom (5 constituent countries/provinces)
Malaysia (16 states/territories)| United States (62 states/territories)

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/countries/{country_id}/provinces.json](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces)

Retrieves a list of provinces for a country

deprecated

**

deprecated

**

  * [ get/admin/api/latest/countries/{country_id}/provinces/{province_id}.json](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-province-id)

Retrieves a single province for a country

deprecated

**

deprecated

**

  * [ get/admin/api/latest/countries/{country_id}/provinces/count.json](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-count)

Retrieves a count of provinces for a country

deprecated

**

deprecated

**

  * [ put/admin/api/latest/countries/{country_id}/provinces/{province_id}.json](/docs/api/admin-rest/latest/resources/province#put-countries-country-id-provinces-province-id)

Updates an existing province for a country

deprecated

**

deprecated

**


* * *

[ Anchor to ](/docs/api/admin-rest/latest/resources/province#resource-object)

## The Province resource

[Anchor to ](/docs/api/admin-rest/latest/resources/province#resource-object-properties)

### Properties

* * *

code

The standard abbreviation for the province.

* * *

country_id

The ID for the country that the province belongs to.

* * *

id

The ID for the province.

* * *

name

The full name of the province.

* * *

shipping_zone_id

The ID for the shipping zone that the province belongs to.

* * *

tax

The sales tax rate to be applied to orders made by customers from this province.

* * *

tax_name

The name of the tax for this province.

* * *

tax_type

The tax type. Valid values: `null`, `normal`, `harmonized`, or `compounded`.

A harmonized tax is a combination of provincial and federal sales taxes.

Normal and harmonized tax rates are applied to the pre-tax value of an order, but a compounded tax rate is applied on top of other tax rates. For example, if a $100 order receives a 5% normal tax rate and a 2% compound tax rate, then the post-tax total is $107.10 (`(100 x 1.05) x 1.02 = 107.1`).

* * *

tax_percentage

The province's tax in percent format.

* * *

Was this section helpful?

YesNo

{}

## The Province resource

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

{

"code": "AB",

"country_id": 879921427,

"id": 205434194,

"name": "Alberta",

"shipping_zone_id": 2038345,

"tax": 0.08,

"tax_name": "PST",

"tax_type": "normal",

"tax_percentage": 8

}

* * *

##

[Anchor to GET request, Retrieves a list of provinces for a country](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces)

get

Retrieves a list of provinces for a country

deprecated**deprecated**

Important

This endpoint is deprecated as of 2024-07.

**Important:**

This endpoint is deprecated as of 2024-07.

Retrieves a list of provinces.

###

[Anchor to Parameters of Retrieves a list of provinces for a country](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

country_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of fields names.

* * *

since_id

Restrict results to after the specified ID.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-countries-country-id-provinces-examples](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-examples)Examples

Retrieve all provinces for a country

Path parameters

country_id=879921427

string**string**

required**required**

Retrieve all provinces for a country after the specified ID

Path parameters

country_id=879921427

string**string**

required**required**

Query parameters

since_id=536137098

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/countries/879921427/provinces.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces.json" \

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

"provinces": [

{

"id": 205434194,

"country_id": 879921427,

"name": "Alberta",

"code": "AB",

"tax_name": null,

"tax_type": null,

"shipping_zone_id": null,

"tax": 0.08,

"tax_percentage": 8

},

{

"id": 170405627,

"country_id": 879921427,

"name": "British Columbia",

"code": "BC",

"tax_name": null,

"tax_type": null,

"shipping_zone_id": null,

"tax": 0.07,

"tax_percentage": 7

},

{

"id": 342345110,

"country_id": 879921427,

"name": "Manitoba",

"code": "MB",

"tax_name": null,

"tax_type": null,

"shipping_zone_id": null,

"tax": 0.07,

"tax_percentage": 7

},

### examples

  * #### Retrieve all provinces for a country

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Province.all({
          session: session,
          country_id: 879921427,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Province.all(
          session: test_session,
          country_id: 879921427,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Province.all({
          session: session,
          country_id: 879921427,
        });

#### response

        HTTP/1.1 200 OK{"provinces":[{"id":205434194,"country_id":879921427,"name":"Alberta","code":"AB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":170405627,"country_id":879921427,"name":"British Columbia","code":"BC","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":342345110,"country_id":879921427,"name":"Manitoba","code":"MB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":92264567,"country_id":879921427,"name":"New Brunswick","code":"NB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":243284171,"country_id":879921427,"name":"Newfoundland","code":"NL","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":439598329,"country_id":879921427,"name":"Northwest Territories","code":"NT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":448070559,"country_id":879921427,"name":"Nova Scotia","code":"NS","tax_name":null,"tax_type":"harmonized","shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":670206421,"country_id":879921427,"name":"Nunavut","code":"NU","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":702530425,"country_id":879921427,"name":"Ontario","code":"ON","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":570891722,"country_id":879921427,"name":"Prince Edward Island","code":"PE","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.1,"tax_percentage":10.0},{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax_name":"HST","tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":473391800,"country_id":879921427,"name":"Saskatchewan","code":"SK","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":1005264686,"country_id":879921427,"name":"Yukon","code":"YT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0}]}

  * #### Retrieve all provinces for a country after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces.json?since_id=536137098" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Province.all({
          session: session,
          country_id: 879921427,
          since_id: "536137098",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Province.all(
          session: test_session,
          country_id: 879921427,
          since_id: "536137098",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Province.all({
          session: session,
          country_id: 879921427,
          since_id: "536137098",
        });

#### response

        HTTP/1.1 200 OK{"provinces":[{"id":570891722,"country_id":879921427,"name":"Prince Edward Island","code":"PE","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.1,"tax_percentage":10.0},{"id":670206421,"country_id":879921427,"name":"Nunavut","code":"NU","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":702530425,"country_id":879921427,"name":"Ontario","code":"ON","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":1005264686,"country_id":879921427,"name":"Yukon","code":"YT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0}]}


* * *

##

[Anchor to GET request, Retrieves a single province for a country](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-province-id)

get

Retrieves a single province for a country

deprecated**deprecated**

Important

This endpoint is deprecated as of version 2024-07.

**Important:**

This endpoint is deprecated as of version 2024-07.

Retrieves a single province for a country

###

[Anchor to Parameters of Retrieves a single province for a country](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-province-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

country_id

string**string**

required**required**

* * *

province_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-countries-country-id-provinces-province-id-examples](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-province-id-examples)Examples

Retrieve a single province

Was this section helpful?

YesNo

get

## /admin/api/2026-01/countries/879921427/provinces/224293623.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces/224293623.json" \

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

HTTP/1.1 200 OK

{

"province": {

"id": 224293623,

"country_id": 879921427,

"name": "Quebec",

"code": "QC",

"tax_name": "HST",

"tax_type": "compounded",

"shipping_zone_id": null,

"tax": 0.09,

"tax_percentage": 9

}

}

### examples

  * #### Retrieve a single province

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces/224293623.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Province.find({
          session: session,
          country_id: 879921427,
          id: 224293623,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Province.find(
          session: test_session,
          country_id: 879921427,
          id: 224293623,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Province.find({
          session: session,
          country_id: 879921427,
          id: 224293623,
        });

#### response

        HTTP/1.1 200 OK{"province":{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax_name":"HST","tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0}}


* * *

##

[Anchor to GET request, Retrieves a count of provinces for a country](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-count)

get

Retrieves a count of provinces for a country

deprecated**deprecated**

Important

This endpoint is deprecated as of version 2024-07.

**Important:**

This endpoint is deprecated as of version 2024-07.

Retrieves a count of provinces for a country

###

[Anchor to Parameters of Retrieves a count of provinces for a country](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

country_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-countries-country-id-provinces-count-examples](/docs/api/admin-rest/latest/resources/province#get-countries-country-id-provinces-count-examples)Examples

Count all provinces

Path parameters

country_id=879921427

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/countries/879921427/provinces/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces/count.json" \

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

"count": 13

}

### examples

  * #### Count all provinces

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Province.count({
          session: session,
          country_id: 879921427,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Province.count(
          session: test_session,
          country_id: 879921427,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Province.count({
          session: session,
          country_id: 879921427,
        });

#### response

        HTTP/1.1 200 OK{"count":13}


* * *

##

[Anchor to PUT request, Updates an existing province for a country](/docs/api/admin-rest/latest/resources/province#put-countries-country-id-provinces-province-id)

put

Updates an existing province for a country

deprecated**deprecated**

Requires `shipping` access scope.

**Requires `shipping` access scope.:**

Important

This endpoint is deprecated as of version 2024-07.

**Important:**

This endpoint is deprecated as of version 2024-07.

Caution

As of version 2020-10, the tax field is deprecated.

**Caution:**

As of version 2020-10, the tax field is deprecated.

Updates an existing province for a country.

###

[Anchor to Parameters of Updates an existing province for a country](/docs/api/admin-rest/latest/resources/province#put-countries-country-id-provinces-province-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

country_id

string**string**

required**required**

* * *

province_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-countries-country-id-provinces-province-id-examples](/docs/api/admin-rest/latest/resources/province#put-countries-country-id-provinces-province-id-examples)Examples

Update a province's tax rate

Request body

province

Province resource**Province resource**

Show province properties

province.id:224293623

The ID for the province.

province.tax:0.09

The sales tax rate to be applied to orders made by customers from this province.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/countries/879921427/provinces/224293623.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"province":{"id":224293623,"tax":0.09}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces/224293623.json" \

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

HTTP/1.1 200 OK

{

"province": {

"country_id": 879921427,

"tax_name": "HST",

"name": "Quebec",

"code": "QC",

"id": 224293623,

"tax_type": "compounded",

"shipping_zone_id": null,

"tax": 0.09,

"tax_percentage": 9

}

}

### examples

  * #### Update a province's tax rate

#####

        curl -d '{"province":{"id":224293623,"tax":0.09}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427/provinces/224293623.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const province = new admin.rest.resources.Province({session: session});

        province.country_id = 879921427;
        province.id = 224293623;
        province.tax = 0.09;
        await province.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        province = ShopifyAPI::Province.new(session: test_session)
        province.country_id = 879921427
        province.id = 224293623
        province.tax = 0.09
        province.save!

#####

        // Session is built by the OAuth process

        const province = new shopify.rest.Province({session: session});
        province.country_id = 879921427;
        province.id = 224293623;
        province.tax = 0.09;
        await province.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"province":{"country_id":879921427,"tax_name":"HST","name":"Quebec","code":"QC","id":224293623,"tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0}}