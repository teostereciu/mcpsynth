# ShippingZone

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/shippingzone*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# ShippingZone

Ask assistant

You can use the ShippingZone resource to view shipping zones and their countries, provinces, and shipping rates. A shipping zone belongs to a delivery profile, which provides shops with the ability to create shipping rates per product variant and per location. For example, the merchant might want to use a shipping rate that applies only to fragile products. When querying the ShippingZone resource, each shipping zone is returned with its corresponding profile ID, location group ID, and countries. Its possible for the same country to exist in multiple shipping zones, if the shipping zones with overlapping countries have different delivery profiles.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/shipping_zones.json](/docs/api/admin-rest/latest/resources/shippingzone#get-shipping-zones)

Receive a list of all ShippingZones

[deliveryProfiles](/docs/api/admin-graphql/latest/queries/deliveryProfiles?example=receive-a-list-of-all-shippingzones)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/shippingzone#resource-object)

## The ShippingZone resource

[Anchor to ](/docs/api/admin-rest/latest/resources/shippingzone#resource-object-properties)

### Properties

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DeliveryZone#field-DeliveryZone.fields.id)

The unique numeric identifier for the shipping zone.

* * *

name

read-only**read-only**

->[name](/docs/api/admin-graphql/latest/objects/DeliveryZone#field-DeliveryZone.fields.name)

The name of the shipping zone, specified by the user.

* * *

profile_id

string**string**

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DeliveryProfile#field-DeliveryProfile.fields.id)

The ID of the shipping zone's delivery profile. Shipping profiles allow merchants to create product-based or location-based shipping rates.

* * *

location_group_id

read-only**read-only**

The ID of the shipping zone's location group. Location groups allow merchants to create shipping rates that apply only to the specific locations in the group.

* * *

countries

read-only**read-only**

->[countries](/docs/api/admin-graphql/latest/objects/DeliveryZone#field-DeliveryZone.fields.countries)

A list of countries that belong to the shipping zone.

Show countries properties

  * **id** : The unique numeric identifier for the country.
  * **code** : The ISO 3166-1 alpha-2 two-letter country code for the country. The code for a given country will be the same as the code for the same country in another shop.
  * **shipping_zone_id** : The unique numeric identifier for the shipping zone.
  * **name** : The full name of the country, in English.
  * **tax** : The tax value in decimal format.
  * **tax_name** : The name of the tax as it is referred to in the applicable province/state. For example, in Ontario, Canada the tax is referred to as HST.


* * *

provinces

read-only**read-only**

->[provinces](/docs/api/admin-graphql/latest/objects/DeliveryCountry#field-DeliveryCountry.fields.provinces)

The sub-regions of a country. The term provinces also encompasses states.

Show provinces properties

  * **code** : The two letter province or state code.
  * **country_id** : The unique numeric identifier for the country.
  * **shipping_zone_id** : The unique numeric identifier for the shipping zone.
  * **id** : The unique numeric identifier for the particular province or state.
  * **name** : The name of the province or state.
  * **tax** : The tax value in decimal format.
  * **tax_name** : The name of the tax as it is referred to in the applicable province/state. For example, in Ontario, Canada the tax is referred to as HST.
  * **tax_type** : A tax_type is applied for a compounded sales tax. For example, the Canadian HST is a compounded sales tax of both PST and GST.
  * **tax_percentage** : The tax value in percent format.


* * *

carrier_shipping_rate_providers

read-only**read-only**

->[rateProvider](/docs/api/admin-graphql/latest/objects/DeliveryMethodDefinition#field-DeliveryMethodDefinition.fields.rateProvider)

Information about carrier shipping providers and the rates used.

* * *

price_based_shipping_rates

array**array**

read-only**read-only**

->[methodConditions](/docs/api/admin-graphql/latest/objects/DeliveryMethodDefinition#field-DeliveryMethodDefinition.fields.methodConditions)

Information about a price-based shipping rate.

Show price_based_shipping_rates properties

  * **id** : The unique numeric identifier for the shipping rate.
  * **name** : The name of the shipping rate.
  * **price** : The price of the shipping rate.
  * **shipping_zone_id** : The unique numeric identifier for the associated shipping zone.
  * **min_order_subtotal** : The minimum price of an order for it to be eligible for the shipping rate.
  * **max_order_subtotal** : The maximum price of an order for it to be eligible for the shipping rate.


* * *

weight_based_shipping_rates

array**array**

read-only**read-only**

->[methodConditions](/docs/api/admin-graphql/latest/objects/DeliveryMethodDefinition#field-DeliveryMethodDefinition.fields.methodConditions)

Information about a weight-based shipping rate.

Show weight_based_shipping_rates properties

  * **id** : The unique numeric identifier for the shipping rate.
  * **name** : The name of the shipping rate.
  * **price** : The price of the shipping rate.
  * **shipping_zone_id** : The unique numeric identifier for the associated shipping zone.
  * **weight_low** : The minimum weight of an order for it to be eligible for the shipping rate.
  * **weight_high** : The maximum weight of an order for it to be eligible for the shipping rate.


* * *

Was this section helpful?

YesNo

{}

## The ShippingZone resource

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

{

"id": 132,

"name": "North America",

"profile_id": "gid://shopify/DeliveryProfile/1234",

"location_group_id": "gid://shopify/DeliveryLocationGroup/32873",

"countries": {

"id": 189,

"shipping_zone_id": 132,

"name": "Canada",

"tax": 0.5,

"code": "CA",

"tax_name": "GST",

"provinces": []

},

"provinces": {

"code": "AB",

"country_id": 879921427,

"shipping_zone_is": 132,

"id": 205434194,

"name": "Alberta",

"tax": 0.08,

"tax_name": null,

"tax_type": null,

"tax_percentage": 8

},

"carrier_shipping_rate_providers": [],

"price_based_shipping_rates": {

"price_based_shipping_rates": [

{

"id": 882078077,

"name": "$5 Shipping",

"price": "5.00",

"shipping_zone_id": 881877113,

"min_order_subtotal": "40.0",

"max_order_subtotal": null

}

]

},

"weight_based_shipping_rates": {

"weight_based_shipping_rates": [

{

"id": 882078078,

"name": "Canada Air Shipping",

"price": "25.00",

"shipping_zone_id": 881877113,

"weight_low": 0,

"weight_high": 11.02

}

]

}

}

* * *

##

[Anchor to GET request, Receive a list of all ShippingZones](/docs/api/admin-rest/latest/resources/shippingzone#get-shipping-zones)

get

Receive a list of all ShippingZones

[deliveryProfiles](/docs/api/admin-graphql/latest/queries/deliveryProfiles?example=receive-a-list-of-all-shippingzones)

Get a list of all shipping zones

###

[Anchor to Parameters of Receive a list of all ShippingZones](/docs/api/admin-rest/latest/resources/shippingzone#get-shipping-zones-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only specific fields by providing a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-shipping-zones-examples](/docs/api/admin-rest/latest/resources/shippingzone#get-shipping-zones-examples)Examples

Show list of shipping zones

Was this section helpful?

YesNo

get

## /admin/api/2026-01/shipping_zones.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shipping_zones.json" \

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

HTTP/1.1 200 OK

{

"shipping_zones": [

{

"id": 44570466,

"name": "Downtown Ottawa",

"profile_id": "gid://shopify/DeliveryProfile/690933842",

"location_group_id": "gid://shopify/DeliveryLocationGroup/694323328",

"admin_graphql_api_id": "gid://shopify/DeliveryZone/44570466",

"countries": [

{

"id": 359115488,

"name": "Colombia",

"tax": 0.15,

"code": "CO",

"tax_name": "VAT",

"shipping_zone_id": 44570466,

"provinces": []

},

{

"id": 879921427,

"name": "Canada",

"tax": 0.05,

"code": "CA",

"tax_name": "GST",

"shipping_zone_id": 44570466,

"provinces": [

{

"id": 224293623,

"country_id": 879921427,

"name": "Quebec",

"code": "QC",

"tax": 0.09,

"tax_name": "HST",

"tax_type": "compounded",

"tax_percentage": 9,

"shipping_zone_id": 44570466

},

{

"id": 702530425,

"country_id": 879921427,

"name": "Ontario",

"code": "ON",

"tax": 0.08,

"tax_name": null,

"tax_type": null,

"tax_percentage": 8,

"shipping_zone_id": 44570466

}

]

},

{

"id": 817138619,

"name": "United States",

"tax": 0,

"code": "US",

"tax_name": "Federal Tax",

"shipping_zone_id": 44570466,

"provinces": [

{

"id": 9350860,

"country_id": 817138619,

"name": "Massachusetts",

"code": "MA",

"tax": 0.065,

"tax_name": null,

"tax_type": null,

"tax_percentage": 6.5,

"shipping_zone_id": 44570466

},

{

"id": 1013111685,

"country_id": 817138619,

"name": "New York",

"code": "NY",

"tax": 0.04,

"tax_name": null,

"tax_type": null,

"tax_percentage": 4,

"shipping_zone_id": 44570466

}

]

}

],

"weight_based_shipping_rates": [

{

"id": 522512552,

"name": "Free Under 5kg",

"price": "0.00",

"shipping_zone_id": 44570466,

"weight_low": 0,

"weight_high": 5

}

],

"price_based_shipping_rates": [

{

"id": 64051,

"name": "Free Shipping",

"price": "0.00",

"shipping_zone_id": 44570466,

"min_order_subtotal": null,

"max_order_subtotal": "450"

}

],

"carrier_shipping_rate_providers": [

{

"id": 615128020,

"carrier_service_id": 260046840,

"flat_modifier": "",

"percent_modifier": null,

"service_filter": {

"*": "+"

},

"shipping_zone_id": 44570466

}

]

}

]

}

### examples

  * #### Show list of shipping zones

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shipping_zones.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ShippingZone.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ShippingZone.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ShippingZone.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"shipping_zones":[{"id":44570466,"name":"Downtown Ottawa","profile_id":"gid://shopify/DeliveryProfile/690933842","location_group_id":"gid://shopify/DeliveryLocationGroup/694323328","admin_graphql_api_id":"gid://shopify/DeliveryZone/44570466","countries":[{"id":359115488,"name":"Colombia","tax":0.15,"code":"CO","tax_name":"VAT","shipping_zone_id":44570466,"provinces":[]},{"id":879921427,"name":"Canada","tax":0.05,"code":"CA","tax_name":"GST","shipping_zone_id":44570466,"provinces":[{"id":224293623,"country_id":879921427,"name":"Quebec","code":"QC","tax":0.09,"tax_name":"HST","tax_type":"compounded","tax_percentage":9.0,"shipping_zone_id":44570466},{"id":702530425,"country_id":879921427,"name":"Ontario","code":"ON","tax":0.08,"tax_name":null,"tax_type":null,"tax_percentage":8.0,"shipping_zone_id":44570466}]},{"id":817138619,"name":"United States","tax":0.0,"code":"US","tax_name":"Federal Tax","shipping_zone_id":44570466,"provinces":[{"id":9350860,"country_id":817138619,"name":"Massachusetts","code":"MA","tax":0.065,"tax_name":null,"tax_type":null,"tax_percentage":6.5,"shipping_zone_id":44570466},{"id":1013111685,"country_id":817138619,"name":"New York","code":"NY","tax":0.04,"tax_name":null,"tax_type":null,"tax_percentage":4.0,"shipping_zone_id":44570466}]}],"weight_based_shipping_rates":[{"id":522512552,"name":"Free Under 5kg","price":"0.00","shipping_zone_id":44570466,"weight_low":0.0,"weight_high":5.0}],"price_based_shipping_rates":[{"id":64051,"name":"Free Shipping","price":"0.00","shipping_zone_id":44570466,"min_order_subtotal":null,"max_order_subtotal":"450"}],"carrier_shipping_rate_providers":[{"id":615128020,"carrier_service_id":260046840,"flat_modifier":"","percent_modifier":null,"service_filter":{"*":"+"},"shipping_zone_id":44570466}]}]}