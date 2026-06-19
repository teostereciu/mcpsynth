# Country

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/country*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Country

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Important

The REST Country API is deprecated as of version 2024-07.

Please refer to the documentation for each individual endpoint and the [developer changelog](https://shopify.dev/changelog/deprecation-notice-country-and-province-endpoints-in-admin-rest-api) for more information.

**Important:**

The REST Country API is deprecated as of version 2024-07.

Please refer to the documentation for each individual endpoint and the [developer changelog](https://shopify.dev/changelog/deprecation-notice-country-and-province-endpoints-in-admin-rest-api) for more information.

The Country resource represents the tax rates applied to orders from the different countries where a shop sells its products.

Merchants select the countries where they sell their products when they set up their shipping zones and rates on the **Shipping** page of the Shopify admin. After adding a country to a shipping zone, store owners can then verify and adjust tax rates for each country on the **Taxes** page.

The Country resource lets you access the countries and tax rates set up by the merchant. The countries list includes a default entry called **Rest of World** , which represents all non-specified countries.

You can use the Country resource to modify the sales tax rate for a country or sub-region to account for surtaxes or exemptions that apply to the store.

For more information on managing tax rates for sub-regions of a country, such as states or provinces, see the [Province](/docs/admin-api/rest/reference/store-properties/province) resource.

Caution

As of version 2020-10, you can no longer create or update custom tax values for the Country resource.

**Caution:**

As of version 2020-10, you can no longer create or update custom tax values for the Country resource.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/countries.json](/docs/api/admin-rest/latest/resources/country#post-countries)

Creates a country

deprecated

**

deprecated

**

  * [ get/admin/api/latest/countries.json](/docs/api/admin-rest/latest/resources/country#get-countries)

Retrieves a list of countries

deprecated

**

deprecated

**

  * [ get/admin/api/latest/countries/{country_id}.json](/docs/api/admin-rest/latest/resources/country#get-countries-country-id)

Retrieves a specific country

deprecated

**

deprecated

**

  * [ get/admin/api/latest/countries/count.json](/docs/api/admin-rest/latest/resources/country#get-countries-count)

Retrieves a count of countries

deprecated

**

deprecated

**

  * [ put/admin/api/latest/countries/{country_id}.json](/docs/api/admin-rest/latest/resources/country#put-countries-country-id)

Updates an existing country

deprecated

**

deprecated

**

  * [ del/admin/api/latest/countries/{country_id}.json](/docs/api/admin-rest/latest/resources/country#delete-countries-country-id)

Deletes a country

deprecated

**

deprecated

**


* * *

[ Anchor to ](/docs/api/admin-rest/latest/resources/country#resource-object)

## The Country resource

[Anchor to ](/docs/api/admin-rest/latest/resources/country#resource-object-properties)

### Properties

* * *

code

deprecated**deprecated**

The two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format).

* * *

id

deprecated**deprecated**

The ID for the country. The ID for a country is unique across all Shopify stores. The ID for a country in one shop will be different from the same country in another shop.

* * *

name

deprecated**deprecated**

The full name of the country in English.

* * *

provinces

deprecated**deprecated**

The sub-regions of a country, such as its provinces or states. Each sub-region has the following properties:

Show provinces properties

  * **code** : The two letter province or state code.
  * **country_id** : The ID for the country to which this sub-region belongs.
  * **id** : The ID for the particular sub-region.
  * **name** : The name of the sub-region.
  * **tax** : The tax value in decimal format.
  * **tax_name** : The name of the tax as it is referred to in the applicable sub-region. For example, in Canada, the sales tax in the province Ontario is referred to as HST.
  * **tax_type** : The tax type. Valid values: `null`, `normal`, or `harmonized`. If the value is `harmonized`, then the tax is compounded of the provincial and federal sales taxes.
  * **tax_percentage** : The tax value in percent format.


* * *

tax

deprecated**deprecated**

The national sales tax rate applied to orders made by customers from that country.

* * *

Was this section helpful?

YesNo

{}

## The Country resource

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

{

"code": "CA",

"id": 879921427,

"name": "Canada",

"provinces": [

{

"code": "ON",

"country_id": 879921427,

"id": 205434194,

"name": "Ontario",

"tax": 0.13,

"tax_name": "HST",

"tax_type": "harmonized",

"tax_percentage": 13

}

],

"tax": 0.05

}

* * *

##

[Anchor to POST request, Creates a country](/docs/api/admin-rest/latest/resources/country#post-countries)

post

Creates a country

deprecated**deprecated**

Requires `shipping` access scope.

**Requires `shipping` access scope.:**

Important

This endpoint is deprecated as of 2024-07.

**Important:**

This endpoint is deprecated as of 2024-07.

Caution

As of version 2020-10, the tax field is deprecated.

**Caution:**

As of version 2020-10, the tax field is deprecated.

Creates a country.

###

[Anchor to Parameters of Creates a country](/docs/api/admin-rest/latest/resources/country#post-countries-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-countries-examples](/docs/api/admin-rest/latest/resources/country#post-countries-examples)Examples

Create a country using Shopify's tax rate for it

Request body

country

Country resource**Country resource**

Show country properties

country.code:"FR"

deprecated**deprecated**

The two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format).

Create a country using a custom tax rate

Request body

country

Country resource**Country resource**

Show country properties

country.code:"FR"

deprecated**deprecated**

The two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format).

country.tax:0.2

deprecated**deprecated**

The national sales tax rate applied to orders made by customers from that country.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/countries.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"country":{"code":"FR"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/countries.json" \

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

HTTP/1.1 201 Created

{

"country": {

"id": 980881736,

"name": "France",

"code": "FR",

"tax_name": "TVA",

"tax": 0.2,

"provinces": []

}

}

### examples

  * #### Create a country using Shopify's tax rate for it

#####

        curl -d '{"country":{"code":"FR"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/countries.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const country = new admin.rest.resources.Country({session: session});

        country.code = "FR";
        await country.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        country = ShopifyAPI::Country.new(session: test_session)
        country.code = "FR"
        country.save!

#####

        // Session is built by the OAuth process

        const country = new shopify.rest.Country({session: session});
        country.code = "FR";
        await country.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"country":{"id":980881736,"name":"France","code":"FR","tax_name":"TVA","tax":0.2,"provinces":[]}}

  * #### Create a country using a custom tax rate

#####

        curl -d '{"country":{"code":"FR","tax":0.2}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/countries.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const country = new admin.rest.resources.Country({session: session});

        country.code = "FR";
        country.tax = 0.2;
        await country.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        country = ShopifyAPI::Country.new(session: test_session)
        country.code = "FR"
        country.tax = 0.2
        country.save!

#####

        // Session is built by the OAuth process

        const country = new shopify.rest.Country({session: session});
        country.code = "FR";
        country.tax = 0.2;
        await country.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"country":{"id":980881737,"name":"France","code":"FR","tax_name":"TVA","tax":0.2,"provinces":[]}}


* * *

##

[Anchor to GET request, Retrieves a list of countries](/docs/api/admin-rest/latest/resources/country#get-countries)

get

Retrieves a list of countries

deprecated**deprecated**

Important

This endpoint is deprecated as of version 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

**Important:**

This endpoint is deprecated as of version 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

Retrieves a list of countries.

###

[Anchor to Parameters of Retrieves a list of countries](/docs/api/admin-rest/latest/resources/country#get-countries-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

after_id

Restrict results to after the specified ID.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-countries-examples](/docs/api/admin-rest/latest/resources/country#get-countries-examples)Examples

Retrieve all countries

Retrieve all countries after the specified ID

Query parameters

after_id=359115488

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/countries.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries.json" \

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

"countries": [

{

"id": 879921427,

"name": "Canada",

"code": "CA",

"tax_name": "GST",

"tax": 0.05,

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

### examples

  * #### Retrieve all countries

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Country.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Country.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Country.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"countries":[{"id":879921427,"name":"Canada","code":"CA","tax_name":"GST","tax":0.05,"provinces":[{"id":205434194,"country_id":879921427,"name":"Alberta","code":"AB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":170405627,"country_id":879921427,"name":"British Columbia","code":"BC","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":342345110,"country_id":879921427,"name":"Manitoba","code":"MB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":92264567,"country_id":879921427,"name":"New Brunswick","code":"NB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":243284171,"country_id":879921427,"name":"Newfoundland","code":"NL","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":439598329,"country_id":879921427,"name":"Northwest Territories","code":"NT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":448070559,"country_id":879921427,"name":"Nova Scotia","code":"NS","tax_name":null,"tax_type":"harmonized","shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":670206421,"country_id":879921427,"name":"Nunavut","code":"NU","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":702530425,"country_id":879921427,"name":"Ontario","code":"ON","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":570891722,"country_id":879921427,"name":"Prince Edward Island","code":"PE","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.1,"tax_percentage":10.0},{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax_name":"HST","tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":473391800,"country_id":879921427,"name":"Saskatchewan","code":"SK","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":1005264686,"country_id":879921427,"name":"Yukon","code":"YT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0}]},{"id":359115488,"name":"Colombia","code":"CO","tax_name":"VAT","tax":0.15,"provinces":[]},{"id":817138619,"name":"United States","code":"US","tax_name":"Federal Tax","tax":0.0,"provinces":[{"id":952629862,"country_id":817138619,"name":"California","code":"CA","tax_name":null,"tax_type":null,"shipping_zone_id":1039932365,"tax":0.05,"tax_percentage":5.0},{"id":222234158,"country_id":817138619,"name":"Kentucky","code":"KY","tax_name":null,"tax_type":null,"shipping_zone_id":1039932365,"tax":0.06,"tax_percentage":6.0},{"id":9350860,"country_id":817138619,"name":"Massachusetts","code":"MA","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.065,"tax_percentage":6.5},{"id":696485510,"country_id":817138619,"name":"Minnesota","code":"MN","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.065,"tax_percentage":6.5},{"id":753050225,"country_id":817138619,"name":"New Jersey","code":"NJ","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.06,"tax_percentage":6.0},{"id":1013111685,"country_id":817138619,"name":"New York","code":"NY","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.04,"tax_percentage":4.0},{"id":915134533,"country_id":817138619,"name":"Pennsylvania","code":"PA","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.05,"tax_percentage":5.0},{"id":591478044,"country_id":817138619,"name":"Rhode Island","code":"RI","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0}]}]}

  * #### Retrieve all countries after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries.json?after_id=359115488" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Country.all({
          session: session,
          after_id: "359115488",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Country.all(
          session: test_session,
          after_id: "359115488",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Country.all({
          session: session,
          after_id: "359115488",
        });

#### response

        HTTP/1.1 200 OK{"countries":[{"id":817138619,"name":"United States","code":"US","tax_name":"Federal Tax","tax":0.0,"provinces":[{"id":952629862,"country_id":817138619,"name":"California","code":"CA","tax_name":null,"tax_type":null,"shipping_zone_id":1039932365,"tax":0.05,"tax_percentage":5.0},{"id":222234158,"country_id":817138619,"name":"Kentucky","code":"KY","tax_name":null,"tax_type":null,"shipping_zone_id":1039932365,"tax":0.06,"tax_percentage":6.0},{"id":9350860,"country_id":817138619,"name":"Massachusetts","code":"MA","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.065,"tax_percentage":6.5},{"id":696485510,"country_id":817138619,"name":"Minnesota","code":"MN","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.065,"tax_percentage":6.5},{"id":753050225,"country_id":817138619,"name":"New Jersey","code":"NJ","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.06,"tax_percentage":6.0},{"id":1013111685,"country_id":817138619,"name":"New York","code":"NY","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.04,"tax_percentage":4.0},{"id":915134533,"country_id":817138619,"name":"Pennsylvania","code":"PA","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.05,"tax_percentage":5.0},{"id":591478044,"country_id":817138619,"name":"Rhode Island","code":"RI","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0}]},{"id":879921427,"name":"Canada","code":"CA","tax_name":"GST","tax":0.05,"provinces":[{"id":205434194,"country_id":879921427,"name":"Alberta","code":"AB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":170405627,"country_id":879921427,"name":"British Columbia","code":"BC","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":342345110,"country_id":879921427,"name":"Manitoba","code":"MB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":92264567,"country_id":879921427,"name":"New Brunswick","code":"NB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":243284171,"country_id":879921427,"name":"Newfoundland","code":"NL","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":439598329,"country_id":879921427,"name":"Northwest Territories","code":"NT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":448070559,"country_id":879921427,"name":"Nova Scotia","code":"NS","tax_name":null,"tax_type":"harmonized","shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":670206421,"country_id":879921427,"name":"Nunavut","code":"NU","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":702530425,"country_id":879921427,"name":"Ontario","code":"ON","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":570891722,"country_id":879921427,"name":"Prince Edward Island","code":"PE","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.1,"tax_percentage":10.0},{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax_name":"HST","tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":473391800,"country_id":879921427,"name":"Saskatchewan","code":"SK","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":1005264686,"country_id":879921427,"name":"Yukon","code":"YT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0}]}]}


* * *

##

[Anchor to GET request, Retrieves a specific country](/docs/api/admin-rest/latest/resources/country#get-countries-country-id)

get

Retrieves a specific country

deprecated**deprecated**

Important

This endpoint is deprecated as of version 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

**Important:**

This endpoint is deprecated as of version 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

Retrieves a specific country

###

[Anchor to Parameters of Retrieves a specific country](/docs/api/admin-rest/latest/resources/country#get-countries-country-id-parameters)Parameters

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

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-countries-country-id-examples](/docs/api/admin-rest/latest/resources/country#get-countries-country-id-examples)Examples

Retrieve a specific country by its ID

Path parameters

country_id=879921427

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/countries/879921427.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427.json" \

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

"country": {

"id": 879921427,

"name": "Canada",

"code": "CA",

"tax_name": "GST",

"tax": 0.05,

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

### examples

  * #### Retrieve a specific country by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Country.find({
          session: session,
          id: 879921427,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Country.find(
          session: test_session,
          id: 879921427,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Country.find({
          session: session,
          id: 879921427,
        });

#### response

        HTTP/1.1 200 OK{"country":{"id":879921427,"name":"Canada","code":"CA","tax_name":"GST","tax":0.05,"provinces":[{"id":205434194,"country_id":879921427,"name":"Alberta","code":"AB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":170405627,"country_id":879921427,"name":"British Columbia","code":"BC","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":342345110,"country_id":879921427,"name":"Manitoba","code":"MB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"id":92264567,"country_id":879921427,"name":"New Brunswick","code":"NB","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":243284171,"country_id":879921427,"name":"Newfoundland","code":"NL","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":439598329,"country_id":879921427,"name":"Northwest Territories","code":"NT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":448070559,"country_id":879921427,"name":"Nova Scotia","code":"NS","tax_name":null,"tax_type":"harmonized","shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"id":670206421,"country_id":879921427,"name":"Nunavut","code":"NU","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"id":702530425,"country_id":879921427,"name":"Ontario","code":"ON","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"id":570891722,"country_id":879921427,"name":"Prince Edward Island","code":"PE","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.1,"tax_percentage":10.0},{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax_name":"HST","tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":473391800,"country_id":879921427,"name":"Saskatchewan","code":"SK","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"id":1005264686,"country_id":879921427,"name":"Yukon","code":"YT","tax_name":null,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0}]}}


* * *

##

[Anchor to GET request, Retrieves a count of countries](/docs/api/admin-rest/latest/resources/country#get-countries-count)

get

Retrieves a count of countries

deprecated**deprecated**

Important

This endpoint is deprecated as of 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

**Important:**

This endpoint is deprecated as of 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

Retrieves a count of countries.

###

[Anchor to Parameters of Retrieves a count of countries](/docs/api/admin-rest/latest/resources/country#get-countries-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-countries-count-examples](/docs/api/admin-rest/latest/resources/country#get-countries-count-examples)Examples

Count all countries

Was this section helpful?

YesNo

get

## /admin/api/2026-01/countries/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/count.json" \

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

"count": 3

}

### examples

  * #### Count all countries

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/countries/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Country.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Country.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Country.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":3}


* * *

##

[Anchor to PUT request, Updates an existing country](/docs/api/admin-rest/latest/resources/country#put-countries-country-id)

put

Updates an existing country

deprecated**deprecated**

Requires `shipping` access scope.

**Requires `shipping` access scope.:**

Important

This endpoint is deprecated as of 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

**Important:**

This endpoint is deprecated as of 2024-07.

Please see the [Countries in shipping zone API](https://shopify.dev/docs/api/admin-graphql/2024-01/objects/CountriesInShippingZones) for a GraphQL alternative.

Caution

As of version 2020-10, the tax field is deprecated.

**Caution:**

As of version 2020-10, the tax field is deprecated.

Updates an existing country.

###

[Anchor to Parameters of Updates an existing country](/docs/api/admin-rest/latest/resources/country#put-countries-country-id-parameters)Parameters

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

[Anchor to put-countries-country-id-examples](/docs/api/admin-rest/latest/resources/country#put-countries-country-id-examples)Examples

Update a country's tax rate

Path parameters

country_id=879921427

string**string**

required**required**

Request body

country

Country resource**Country resource**

Show country properties

country.id:879921427

deprecated**deprecated**

The ID for the country. The ID for a country is unique across all Shopify stores. The ID for a country in one shop will be different from the same country in another shop.

country.tax:0.05

deprecated**deprecated**

The national sales tax rate applied to orders made by customers from that country.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/countries/879921427.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"country":{"id":879921427,"tax":0.05}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427.json" \

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

"country": {

"name": "Canada",

"code": "CA",

"id": 879921427,

"tax_name": "GST",

"tax": 0.05,

"provinces": [

{

"country_id": 879921427,

"tax_name": "Tax",

"name": "Alberta",

"code": "AB",

"id": 205434194,

"tax_type": null,

"shipping_zone_id": null,

"tax": 0.08,

"tax_percentage": 8

},

{

"country_id": 879921427,

"tax_name": "Tax",

"name": "British Columbia",

"code": "BC",

"id": 170405627,

"tax_type": null,

"shipping_zone_id": null,

"tax": 0.07,

"tax_percentage": 7

},

{

"country_id": 879921427,

"tax_name": "Tax",

"name": "Manitoba",

"code": "MB",

### examples

  * #### Update a country's tax rate

#####

        curl -d '{"country":{"id":879921427,"tax":0.05}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const country = new admin.rest.resources.Country({session: session});

        country.id = 879921427;
        country.tax = 0.05;
        await country.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        country = ShopifyAPI::Country.new(session: test_session)
        country.id = 879921427
        country.tax = 0.05
        country.save!

#####

        // Session is built by the OAuth process

        const country = new shopify.rest.Country({session: session});
        country.id = 879921427;
        country.tax = 0.05;
        await country.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"country":{"name":"Canada","code":"CA","id":879921427,"tax_name":"GST","tax":0.05,"provinces":[{"country_id":879921427,"tax_name":"Tax","name":"Alberta","code":"AB","id":205434194,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"country_id":879921427,"tax_name":"Tax","name":"British Columbia","code":"BC","id":170405627,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"country_id":879921427,"tax_name":"Tax","name":"Manitoba","code":"MB","id":342345110,"tax_type":null,"shipping_zone_id":null,"tax":0.07,"tax_percentage":7.0},{"country_id":879921427,"tax_name":"Tax","name":"New Brunswick","code":"NB","id":92264567,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"country_id":879921427,"tax_name":"Tax","name":"Newfoundland","code":"NL","id":243284171,"tax_type":null,"shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"country_id":879921427,"tax_name":"Tax","name":"Northwest Territories","code":"NT","id":439598329,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"country_id":879921427,"tax_name":"Tax","name":"Nova Scotia","code":"NS","id":448070559,"tax_type":"harmonized","shipping_zone_id":null,"tax":0.15,"tax_percentage":15.0},{"country_id":879921427,"tax_name":"Tax","name":"Nunavut","code":"NU","id":670206421,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0},{"country_id":879921427,"tax_name":"Tax","name":"Ontario","code":"ON","id":702530425,"tax_type":null,"shipping_zone_id":null,"tax":0.08,"tax_percentage":8.0},{"country_id":879921427,"tax_name":"Tax","name":"Prince Edward Island","code":"PE","id":570891722,"tax_type":null,"shipping_zone_id":null,"tax":0.1,"tax_percentage":10.0},{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax_name":"HST","tax_type":"compounded","shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"country_id":879921427,"tax_name":"Tax","name":"Saskatchewan","code":"SK","id":473391800,"tax_type":null,"shipping_zone_id":null,"tax":0.09,"tax_percentage":9.0},{"country_id":879921427,"tax_name":"Tax","name":"Yukon","code":"YT","id":1005264686,"tax_type":null,"shipping_zone_id":null,"tax":0.0,"tax_percentage":0.0}]}}


* * *

##

[Anchor to DELETE request, Deletes a country](/docs/api/admin-rest/latest/resources/country#delete-countries-country-id)

del

Deletes a country

deprecated**deprecated**

Requires `shipping` access scope.

**Requires `shipping` access scope.:**

Important

This endpoint is deprecated as of version 2024-07.

**Important:**

This endpoint is deprecated as of version 2024-07.

###

[Anchor to Parameters of Deletes a country](/docs/api/admin-rest/latest/resources/country#delete-countries-country-id-parameters)Parameters

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

[Anchor to delete-countries-country-id-examples](/docs/api/admin-rest/latest/resources/country#delete-countries-country-id-examples)Examples

Delete a country

Path parameters

country_id=879921427

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/countries/879921427.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427.json" \

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

  * #### Delete a country

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/countries/879921427.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Country.delete({
          session: session,
          id: 879921427,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Country.delete(
          session: test_session,
          id: 879921427,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Country.delete({
          session: session,
          id: 879921427,
        });

#### response

        HTTP/1.1 200 OK{}