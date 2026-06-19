# Fulfillment

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillment*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Fulfillment

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

You can use the `Fulfillment` resource to view fulfillments for an order or a [fulfillment order](/api/admin-rest/latest/resources/fulfillmentorder). A fulfillment order represents a group of one or more items in an order that will be fulfilled from the same location. A fulfillment represents work that is completed as part of a fulfillment order and can include one or more items. You can use the `Fulfillment` resource to manage fulfillments for fulfillment orders.

This resource is typically used in apps that perform shipping-related actions, such as making tracking and delivery updates, or creating additional shipments as required for an order or fulfillment order.

Each fulfillment supports a single tracking number. If you need to use multiple tracking numbers, then you should create separate fulfillments.

[Learn about using fulfillment order-based workflows](https://shopify.dev/apps/fulfillment).

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/fulfillments.json](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments)

Creates a fulfillment for one or many fulfillment orders

[fulfillmentCreateV2](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2)

  * [post/admin/api/latest/fulfillments/{fulfillment_id}/cancel.json](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-cancel)

Cancels a fulfillment

[fulfillmentCancel](/docs/api/admin-graphql/latest/mutations/fulfillmentCancel?example=cancels-a-fulfillment)

  * [post/admin/api/latest/fulfillments/{fulfillment_id}/update_tracking.json](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-update-tracking)

Updates the tracking information for a fulfillment

[fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate?example=updates-the-tracking-information-for-a-fulfillment)

  * [get/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/fulfillments.json](/docs/api/admin-rest/latest/resources/fulfillment#get-fulfillment-orders-fulfillment-order-id-fulfillments)

Retrieves fulfillments associated with a fulfillment order

[fulfillmentOrder](/docs/api/admin-graphql/latest/queries/fulfillmentOrder?example=retrieves-fulfillments-associated-with-a-fulfillment-order)

  * [get/admin/api/latest/orders/{order_id}/fulfillments.json](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments)

Retrieves fulfillments associated with an order

[order](/docs/api/admin-graphql/latest/queries/order)

  * [get/admin/api/latest/orders/{order_id}/fulfillments/{fulfillment_id}.json](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-fulfillment-id)

Receive a single Fulfillment

[fulfillment](/docs/api/admin-graphql/latest/queries/fulfillment?example=receive-a-single-fulfillment)

  * [get/admin/api/latest/orders/{order_id}/fulfillments/count.json](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-count)

Retrieves a count of fulfillments associated with a specific order

[order](/docs/api/admin-graphql/latest/queries/order)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillment#resource-object)

## The Fulfillment resource

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillment#resource-object-properties)

### Properties

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.createdAt)

The date and time when the fulfillment was created. The API returns this value in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601).

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.id)

The ID for the fulfillment.

* * *

line_items

->[fulfillmentLineItems](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems)

A list of the fulfillment's line items, which includes:

Show line_items properties

  * **id** : The ID of the line item within the fulfillment.
  * **variant_id** : The ID of the product variant being fulfilled.
  * **title** : The title of the product.
  * **quantity** : The number of items in the fulfillment.
  * **price** : The price of the item before discounts have been applied in the shop currency.
  * **price_set** : The price of the line item in shop and presentment currencies.
  * **grams** : The weight of the item in grams.
  * **sku** : The unique identifier of the item in the fulfillment.
  * **variant_title** : The title of the product variant being fulfilled.
  * **vendor** : The name of the supplier of the item.
  * **fulfillment_service** : The service provider who is doing the fulfillment. This field will be deprecated. Use the `assigned_location` property on the `FulfillmentOrder` resource instead.
  * **product_id** : The unique numeric identifier for the product in the fulfillment.
  * **requires_shipping** : Whether a customer needs to provide a shipping address when placing an order for this product variant.
  * **taxable** : Whether the line item is taxable.
  * **gift_card** : Whether the line item is a [gift card](https://help.shopify.com/manual/products/gift-card-products).
  * **name** : The name of the product variant.
  * **variant_inventory_management** : The name of the inventory management system.
  * **properties** : Any additional properties associated with the line item.
  * **product_exists** : Whether the product exists.
  * **fulfillable_quantity** : The amount available to fulfill. This is the quantity - max (refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity. This field will be deprecated. Use the `fulfillable_quantity` property of the `line_item` property on the `FulfillmentOrder` resource instead.
  * **total_discount** : The total of any discounts applied to the line item with respect to its total quantity on the order. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **fulfillment_status** : The status of an order in terms of the line items being fulfilled. Valid values: `fulfilled`, `null`, or `partial`. This field will be deprecated. Use the `status` property on the `FulfillmentOrder` resource instead.
  * **total_discount_set** : The total amount allocated to the line item in the presentment currency. Instead of using this field, Shopify recommends using `discount_allocations`, which provides the same information.
  * **discount_allocations** : An ordered list of amounts allocated by discount applications. The amount is representative of the discount applied to the total quantity of the line item on the order, not just this fulfillment. Each discount allocation is associated with a particular discount application.
    * `amount`: The discount amount allocated to the line in the shop currency.
    * `discount_application_index`: The index of the associated discount application in the order's `discount_applications` list.
    * `amount_set`: The discount amount allocated to the line item in shop and presentment currencies.
  * **fulfillment_line_item_id** : A unique identifier for a quantity of items within a single fulfillment. An order can have multiple fulfillment line items.
  * **tax_lines** : The `title`, `price`, and `rate` of any taxes applied to the line item for its total quantity on the order.
  * **duties** : A list of duty objects, each containing information about a duty on the line item for its total quantity on the order.


* * *

location_id

->[id](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id)

The unique identifier of the location that the fulfillment was processed at. To find the ID of the location, use the [Location resource](/docs/admin-api/rest/reference/inventory/location).

* * *

name

->[name](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.name)

The uniquely identifying fulfillment name, consisting of two parts separated by a `.`. The first part represents the order name and the second part represents the fulfillment number. The fulfillment number automatically increments depending on how many fulfillments are in an order (e.g. `#1001.1`, `#1001.2`).

* * *

order_id

->[id](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.id)

The unique numeric identifier for the order.

* * *

origin_address

->[originAddress](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.originAddress)

The address of the fulfillment location. This property is intended for tax purposes, as a full address is required for tax providers to accurately calculate taxes. To retrieve a fulfillment location's address, use the `assigned_location`` property on the [FulfillmentOrder](/docs/api/admin-rest/latest/resources/fulfillmentorder) resource instead.

Show origin_address properties

  * **address1** : (string) The street address of the fulfillment location.
  * **address2** : (string) The second line of the address. Typically the number of the apartment, suite, or unit.
  * **city** : (string) The city of the fulfillment location.
  * **country_code** : (string) (required) The two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) of the fulfillment location.
  * **province_code** : (string) The province of the fulfillment location.
  * **zip** : (string) The zip code of the fulfillment location.


* * *

receipt

deprecated**deprecated**

A text field that provides information about the receipt:

Show receipt properties

  * **testcase** : Whether the fulfillment was a testcase.
  * **authorization** : The authorization code.


* * *

service

->[handle](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.handle)

The fulfillment service associated with the fulfillment.

* * *

shipment_status

->[status](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.status)

The current shipment status of the fulfillment. Valid values:

Show shipment_status properties

  * **label_printed** : A label for the shipment was purchased and printed.
  * **label_purchased** : A label for the shipment was purchased, but not printed.
  * **attempted_delivery** : Delivery of the shipment was attempted, but unable to be completed.
  * **ready_for_pickup** : The shipment is ready for pickup at a shipping depot.
  * **confirmed** : The carrier is aware of the shipment, but hasn't received it yet.
  * **in_transit** : The shipment is being transported between shipping facilities on the way to its destination.
  * **out_for_delivery** : The shipment is being delivered to its final destination.
  * **delivered** : The shipment was succesfully delivered.
  * **failure** : Something went wrong when pulling tracking information for the shipment, such as the tracking number was invalid or the shipment was canceled.


* * *

status

->[status](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.status)

The status of the fulfillment. Valid values:

Show status properties

  * **pending** : Shopify has created the fulfillment and is waiting for the third-party fulfillment service to transition it to 'open' or 'success'.
  * **open** : The fulfillment has been acknowledged by the service and is in processing.
  * **success** : The fulfillment was successful.
  * **cancelled** : The fulfillment was cancelled.
  * **error** : There was an error with the fulfillment request.
  * **failure** : The fulfillment request failed.


* * *

tracking_company

The name of the tracking company.

For the tracking company names from the list below Shopify automatically builds tracking URLs for all of the provided tracking numbers, which makes the tracking numbers clickable in the interface.

Additionally, for the tracking companies listed on the [Shipping Carriers help page](https://help.shopify.com/en/manual/shipping/understanding-shipping/shipping-carriers#integrated-shipping-carriers) Shopify will automatically update the fulfillment's `shipment_status` field during the fulfillment process.

Note

Send the tracking company name exactly as written in the list below (capitalization matters).

**Note:**

Send the tracking company name exactly as written in the list below (capitalization matters).

#### Supported tracking companies

The following tracking companies display for shops located in any country:

Show tracking_company properties

  * **4PX**
  * **AGS**
  * **Amazon Logistics UK**
  * **Amazon Logistics US**
  * **An Post**
  * **Anjun Logistics**
  * **APC**
  * **Asendia USA**
  * **Australia Post**
  * **Bonshaw**
  * **BPost**
  * **BPost International**
  * **Canada Post**
  * **Canpar**
  * **CDL Last Mile**
  * **China Post**
  * **Chronopost**
  * **Chukou1**
  * **Colissimo**
  * **Comingle**
  * **Coordinadora**
  * **Correios**
  * **Correos**
  * **CTT**
  * **CTT Express**
  * **Cyprus Post**
  * **Delnext**
  * **Deutsche Post**
  * **DHL eCommerce**
  * **DHL eCommerce Asia**
  * **DHL Express**
  * **DPD**
  * **DPD Local**
  * **DPD UK**
  * **DTD Express**
  * **DX**
  * **Eagle**
  * **Estes**
  * **Evri**
  * **FedEx**
  * **First Global Logistics**
  * **First Line**
  * **FSC**
  * **Fulfilla**
  * **GLS**
  * **Guangdong Weisuyi Information Technology (WSE)**
  * **Heppner Internationale Spedition GmbH & Co.**
  * **Iceland Post**
  * **IDEX**
  * **Israel Post**
  * **Japan Post (EN)**
  * **Japan Post (JA)**
  * **La Poste**
  * **Lasership**
  * **Latvia Post**
  * **Lietuvos Paštas**
  * **Logisters**
  * **Lone Star Overnight**
  * **M3 Logistics**
  * **Meteor Space**
  * **Mondial Relay**
  * **New Zealand Post**
  * **NinjaVan**
  * **North Russia Supply Chain (Shenzhen) Co.**
  * **OnTrac**
  * **Packeta**
  * **Pago Logistics**
  * **Ping An Da Tengfei Express**
  * **Pitney Bowes**
  * **Portal PostNord**
  * **Poste Italiane**
  * **PostNL**
  * **PostNord DK**
  * **PostNord NO**
  * **PostNord SE**
  * **Purolator**
  * **Qxpress**
  * **Qyun Express**
  * **Royal Mail**
  * **Royal Shipments**
  * **Sagawa (EN)**
  * **Sagawa (JA)**
  * **Sendle**
  * **SF Express**
  * **SFC Fulfillment**
  * **SHREE NANDAN COURIER**
  * **Singapore Post**
  * **Southwest Air Cargo**
  * **StarTrack**
  * **Step Forward Freight**
  * **Swiss Post**
  * **TForce Final Mile**
  * **Tinghao**
  * **TNT**
  * **Toll IPEC**
  * **United Delivery Service**
  * **UPS**
  * **USPS**
  * **Venipak**
  * **We Post**
  * **Whistl**
  * **Wizmo**
  * **WMYC**
  * **Xpedigo**
  * **XPO Logistics**
  * **Yamato (EN)**
  * **Yamato (JA)**
  * **YiFan Express**
  * **YunExpress**


The following tracking companies are displayed for shops located in specific countries:

  * **Australia** : Australia Post, Sendle, Aramex Australia, TNT Australia, Hunter Express, Couriers Please, Bonds, Allied Express, Direct Couriers, Northline, GO Logistics
  * **Austria** : Österreichische Post
  * **Bulgaria** : Speedy
  * **Canada** : Intelcom, BoxKnight, Loomis, GLS
  * **China** : China Post, DHL eCommerce Asia, WanbExpress, YunExpress, Anjun Logistics, SFC Fulfillment, FSC
  * **Czechia** : Zásilkovna
  * **Germany** : Deutsche Post (DE), Deutsche Post (EN), DHL, DHL Express, Swiship, Hermes, GLS
  * **Spain** : SEUR
  * **France** : Colissimo, Mondial Relay, Colis Privé, GLS
  * **United Kingdom** : Evri, DPD UK, Parcelforce, Yodel, DHL Parcel, Tuffnells
  * **Greece** : ACS Courier
  * **Hong Kong SAR** : SF Express
  * **Ireland** : Fastway, DPD Ireland
  * **India** : DTDC, India Post, Delhivery, Gati KWE, Professional Couriers, XpressBees, Ecom Express, Ekart, Shadowfax, Bluedart
  * **Italy** : BRT, GLS Italy
  * **Japan** : エコ配, 西濃運輸, 西濃スーパーエキスプレス, 福山通運, 日本通運, 名鉄運輸, 第一貨物
  * **Netherlands** : DHL Parcel, DPD
  * **Norway** : Bring
  * **Poland** : Inpost
  * **Turkey** : PTT, Yurtiçi Kargo, Aras Kargo, Sürat Kargo
  * **United States** : GLS, Alliance Air Freight, Pilot Freight, LSO, Old Dominion, R+L Carriers, Southwest Air Cargo
  * **South Africa** : Fastway, Skynet


* * *

Show 6 hidden fields

Was this section helpful?

YesNo

{}

## The Fulfillment resource

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

89

90

91

92

93

94

95

96

97

{

"created_at": "2012-03-13T16:09:54-04:00",

"id": 255858046,

"line_items": [

{

"id": 466157049,

"variant_id": 39072856,

"title": "IPod Nano - 8gb",

"quantity": 1,

"price": "199.00",

"grams": 200,

"sku": "IPOD2008GREEN",

"variant_title": "green",

"vendor": null,

"fulfillment_service": "manual",

"product_id": 632910392,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "IPod Nano - 8gb - green",

"variant_inventory_management": "shopify",

"properties": [],

"product_exists": true,

"fulfillable_quantity": 1,

"total_discount": "0.00",

"fulfillment_status": null,

"fulfillment_line_item_id": 274098237,

"tax_lines": [],

"duties": [

{

"id": "2",

"harmonized_system_code": "520300",

"country_code_of_origin": "CA",

"shop_money": {

"amount": "164.86",

"currency_code": "CAD"

},

"presentment_money": {

"amount": "105.31",

"currency_code": "EUR"

},

"tax_lines": [

{

"title": "VAT",

"price": "16.486",

"rate": 0.1,

"price_set": {

"shop_money": {

"amount": "16.486",

"currency_code": "CAD"

},

"presentment_money": {

"amount": "10.531",

"currency_code": "EUR"

}

}

}

],

"admin_graphql_api_id": "gid://shopify/Duty/2"

}

]

}

],

"location_id": 40642626,

"name": "#1001.1",

"order_id": 450789469,

"origin_address": [

{

"address1": "1 Rue des Carrieres",

"address2": "Suite 1234",

"city": "Montreal",

"country_code": "CA",

"province_code": "QC",

"zip": "G1R 4P5"

}

],

"receipt": {

"testcase": true,

"authorization": "123456"

},

"service": "manual",

"shipment_status": "confirmed",

"status": "failure",

"tracking_company": "China Post",

"tracking_numbers": [

"112345Z2345",

"1Z001985YW99744790"

],

"tracking_number": "112345Z2345",

"tracking_urls": [

"http://track-chinapost.com/startairmail.php?code=112345Z2345",

"http://wwwapps.ups.com/etracking/tracking.cgi?InquiryNumber1=1Z001985YW99744790&TypeOfInquiryNumber=T&AcceptUPSLicenseAgreement=yes&submit=Track"

],

"tracking_url": "http://track-chinapost.com/startairmail.php?code=112345Z2345",

"updated_at": "2012-05-01T14:22:25-04:00",

"variant_inventory_management": "shopify"

}

* * *

##

[Anchor to POST request, Creates a fulfillment for one or many fulfillment orders](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments)

post

Creates a fulfillment for one or many fulfillment orders

[fulfillmentCreateV2](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2)

Creates a fulfillment for one or many fulfillment orders. The fulfillment orders are associated with the same order and are assigned to the same location.

###

[Anchor to Parameters of Creates a fulfillment for one or many fulfillment orders](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

line_items_by_fulfillment_order

array**array**

required**required**

The fulfillment order line items that have to be fulfilled.

Show line_items_by_fulfillment_order properties

  * **fulfillment_order_id** : (integer) (required) The ID of the fulfillment order.
  * **fulfillment_order_line_items** : (array) The fulfillment order line items and the quantity of each which should be fulfilled. If this property is `undefined`, then all of the fulfillment order line items of the associated fulfillment order are fulfilled.
    * **id** : (integer) (required) The ID of the fulfillment order line item.
    * **quantity** : (integer) (required) (minimum: 1) The quantity of the fulfillment order line item.


* * *

message

string**string**

A message that's associated with the fulfillment request. This message is only available if the associated fulfillment order is assigned to a third-party fulfillment service that has opted in to managing fulfillment orders.

* * *

notify_customer

boolean**boolean**

Whether the customer should be notified. If set to `true`, then an email will be sent when the fulfillment is created or updated. The default value is `false`.

* * *

origin_address

object**object**

The address of the fulfillment location. This property is intended for tax purposes, as a full address is required for tax providers to accurately calculate taxes. To retrieve a fulfillment location's address, use the `assigned_location`` property on the [FulfillmentOrder](/docs/api/admin-rest/latest/resources/fulfillmentorder) resource instead.

Show origin_address properties

  * **address1** : (string) The street address of the fulfillment location.
  * **address2** : (string) The second line of the address. Typically the number of the apartment, suite, or unit.
  * **city** : (string) The city of the fulfillment location.
  * **country_code** : (string) (required) The two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) of the fulfillment location.
  * **province_code** : (string) The province of the fulfillment location.
  * **zip** : (string) The zip code of the fulfillment location.


* * *

tracking_info

object**object**

The tracking information for the fulfillment.

Show tracking_info properties

  * **company** : (string) The name of the tracking company.

For the tracking company names from the list below Shopify automatically builds tracking URLs for all of the provided tracking numbers, which makes the tracking numbers clickable in the interface.

Additionally, for the tracking companies listed on the [Shipping Carriers help page](https://help.shopify.com/en/manual/shipping/understanding-shipping/shipping-carriers#integrated-shipping-carriers) Shopify will automatically update the fulfillment's `shipment_status` field during the fulfillment process.

Note

Send the tracking company name exactly as written in the list below (capitalization matters).

**Note:**

Send the tracking company name exactly as written in the list below (capitalization matters).

#### Supported tracking companies

The following tracking companies display for shops located in any country:

    * **4PX**
    * **AGS**
    * **Amazon Logistics UK**
    * **Amazon Logistics US**
    * **An Post**
    * **Anjun Logistics**
    * **APC**
    * **Asendia USA**
    * **Australia Post**
    * **Bonshaw**
    * **BPost**
    * **BPost International**
    * **Canada Post**
    * **Canpar**
    * **CDL Last Mile**
    * **China Post**
    * **Chronopost**
    * **Chukou1**
    * **Colissimo**
    * **Comingle**
    * **Coordinadora**
    * **Correios**
    * **Correos**
    * **CTT**
    * **CTT Express**
    * **Cyprus Post**
    * **Delnext**
    * **Deutsche Post**
    * **DHL eCommerce**
    * **DHL eCommerce Asia**
    * **DHL Express**
    * **DPD**
    * **DPD Local**
    * **DPD UK**
    * **DTD Express**
    * **DX**
    * **Eagle**
    * **Estes**
    * **Evri**
    * **FedEx**
    * **First Global Logistics**
    * **First Line**
    * **FSC**
    * **Fulfilla**
    * **GLS**
    * **Guangdong Weisuyi Information Technology (WSE)**
    * **Heppner Internationale Spedition GmbH & Co.**
    * **Iceland Post**
    * **IDEX**
    * **Israel Post**
    * **Japan Post (EN)**
    * **Japan Post (JA)**
    * **La Poste**
    * **Lasership**
    * **Latvia Post**
    * **Lietuvos Paštas**
    * **Logisters**
    * **Lone Star Overnight**
    * **M3 Logistics**
    * **Meteor Space**
    * **Mondial Relay**
    * **New Zealand Post**
    * **NinjaVan**
    * **North Russia Supply Chain (Shenzhen) Co.**
    * **OnTrac**
    * **Packeta**
    * **Pago Logistics**
    * **Ping An Da Tengfei Express**
    * **Pitney Bowes**
    * **Portal PostNord**
    * **Poste Italiane**
    * **PostNL**
    * **PostNord DK**
    * **PostNord NO**
    * **PostNord SE**
    * **Purolator**
    * **Qxpress**
    * **Qyun Express**
    * **Royal Mail**
    * **Royal Shipments**
    * **Sagawa (EN)**
    * **Sagawa (JA)**
    * **Sendle**
    * **SF Express**
    * **SFC Fulfillment**
    * **SHREE NANDAN COURIER**
    * **Singapore Post**
    * **Southwest Air Cargo**
    * **StarTrack**
    * **Step Forward Freight**
    * **Swiss Post**
    * **TForce Final Mile**
    * **Tinghao**
    * **TNT**
    * **Toll IPEC**
    * **United Delivery Service**
    * **UPS**
    * **USPS**
    * **Venipak**
    * **We Post**
    * **Whistl**
    * **Wizmo**
    * **WMYC**
    * **Xpedigo**
    * **XPO Logistics**
    * **Yamato (EN)**
    * **Yamato (JA)**
    * **YiFan Express**
    * **YunExpress**

The following tracking companies are displayed for shops located in specific countries:

    * **Australia** : Australia Post, Sendle, Aramex Australia, TNT Australia, Hunter Express, Couriers Please, Bonds, Allied Express, Direct Couriers, Northline, GO Logistics
    * **Austria** : Österreichische Post
    * **Bulgaria** : Speedy
    * **Canada** : Intelcom, BoxKnight, Loomis, GLS
    * **China** : China Post, DHL eCommerce Asia, WanbExpress, YunExpress, Anjun Logistics, SFC Fulfillment, FSC
    * **Czechia** : Zásilkovna
    * **Germany** : Deutsche Post (DE), Deutsche Post (EN), DHL, DHL Express, Swiship, Hermes, GLS
    * **Spain** : SEUR
    * **France** : Colissimo, Mondial Relay, Colis Privé, GLS
    * **United Kingdom** : Evri, DPD UK, Parcelforce, Yodel, DHL Parcel, Tuffnells
    * **Greece** : ACS Courier
    * **Hong Kong SAR** : SF Express
    * **Ireland** : Fastway, DPD Ireland
    * **India** : DTDC, India Post, Delhivery, Gati KWE, Professional Couriers, XpressBees, Ecom Express, Ekart, Shadowfax, Bluedart
    * **Italy** : BRT, GLS Italy
    * **Japan** : エコ配, 西濃運輸, 西濃スーパーエキスプレス, 福山通運, 日本通運, 名鉄運輸, 第一貨物
    * **Netherlands** : DHL Parcel, DPD
    * **Norway** : Bring
    * **Poland** : Inpost
    * **Turkey** : PTT, Yurtiçi Kargo, Aras Kargo, Sürat Kargo
    * **United States** : GLS, Alliance Air Freight, Pilot Freight, LSO, Old Dominion, R+L Carriers, Southwest Air Cargo
    * **South Africa** : Fastway, Skynet
  * **number** : (string) The tracking number for the fulfillment.

The tracking number will be clickable in the interface if one of the following applies (the highest in the list has the highest priority):

    * Tracking URL provided in the `url` field.
    * Shopify-known tracking company name specified in the `company` field. Shopify will build the tracking url automatically based on the tracking number specified.
    * The tracking number has a Shopify-known format. Shopify will guess the tracking provider and build the tracking url based on the tracking number format. Not all tracking carriers are supported, and multiple tracking carriers may use similarly formatted tracking numbers. This can result in an invalid tracking URL. It is highly recommended that you send the tracking company and the tracking URL.

Note

With the REST API, you can set only one tracking number and one tracking URL per fulfillment. If you send multiple shipments with one fulfillment, you may want to specify tracking numbers and tracking URLs for all of them. You can do it with the equivalent GraphQL [fulfillmentCreate](/docs/api/admin-graphql/unstable/mutations/fulfillmentCreate) and [fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/unstable/mutations/fulfillmentTrackingInfoUpdate) mutations.

**Note:**

With the REST API, you can set only one tracking number and one tracking URL per fulfillment. If you send multiple shipments with one fulfillment, you may want to specify tracking numbers and tracking URLs for all of them. You can do it with the equivalent GraphQL [fulfillmentCreate](/docs/api/admin-graphql/unstable/mutations/fulfillmentCreate) and [fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/unstable/mutations/fulfillmentTrackingInfoUpdate) mutations.

  * **url** : (string) The URL to track the fulfillment.

The tracking URL is displayed in the merchant's admin in the order page. The tracking URL is displayed in the shipping confirmation email, which can optionally be sent to the customer. When accounts are enabled, it is also displayed in the customer's order history.

The URL must be an [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) and [RFC 3987](https://datatracker.ietf.org/doc/html/rfc3987)-compliant URI string. For example, `https://www.myshipping.com/track/?tracknumbers=TRACKING_NUMBER` is a valid URL. It includes a scheme (`https`) and a host (`myshipping.com`). If you do not provide a scheme (`http` or `https`), then `http` will be substituted.


* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillments-examples](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-examples)Examples

Create a fulfillment with a tracking number of a Shopify unsupported tracking carrier, and therefore with a tracking url provided.

Create a fulfillment with a tracking number provided. Tracking url and tracking company name will be determined automatically as the tracking number format unambiguously maps to a supported company (UPS).

Create a fulfillment for all fulfillment order line items if `fulfillment_order_line_items` is left blank

Create a fulfillment for the fulfillment order line items specified

Create a fulfillment without tracking info. Tracking numbers can be set later with the `/admin/api/API_VERSION/fulfillments/FULFILLMENT_ID/update_tracking.json` endpoint.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillments.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment":{"line_items_by_fulfillment_order":[{"fulfillment_order_id":1046000857}],"tracking_info":{"number":"MS1562678","url":"https://www.my-shipping-company.com?tracking_number=MS1562678"}}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments.json" \

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

HTTP/1.1 201 Created

{

"fulfillment": {

"id": 1069019898,

"order_id": 450789469,

"status": "success",

"created_at": "2026-01-09T22:36:42-05:00",

"service": "manual",

"updated_at": "2026-01-09T22:36:42-05:00",

"tracking_company": null,

"shipment_status": null,

"location_id": 24826418,

"origin_address": null,

"line_items": [

{

"id": 1071823265,

"variant_id": 389013007,

"title": "Crafty Shoes - Red",

"quantity": 1,

"sku": "crafty_shoes_red",

"variant_title": "Small",

"vendor": "Birthday Present Factory",

"fulfillment_service": "manual",

"product_id": 910489600,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "Crafty Shoes - Red - Small",

"variant_inventory_management": null,

"properties": [],

"product_exists": true,

"fulfillable_quantity": 0,

"grams": 0,

"price": "10.00",

"total_discount": "0.00",

"fulfillment_status": "fulfilled",

"price_set": {

"shop_money": {

"amount": "10.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "10.00",

"currency_code": "USD"

}

},

"total_discount_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "USD"

}

},

"discount_allocations": [],

"duties": [],

"admin_graphql_api_id": "gid://shopify/LineItem/1071823265",

"tax_lines": []

}

],

"tracking_number": "MS1562678",

"tracking_numbers": [

"MS1562678"

],

"tracking_url": "https://www.my-shipping-company.com?tracking_number=MS1562678",

"tracking_urls": [

"https://www.my-shipping-company.com?tracking_number=MS1562678"

],

"receipt": {},

"name": "#1001.2",

"admin_graphql_api_id": "gid://shopify/Fulfillment/1069019898"

}

}

### examples

  * ####  Create a fulfillment with a tracking number of a Shopify unsupported tracking carrier, and therefore with a tracking url provided.

#####

        curl -d '{"fulfillment":{"line_items_by_fulfillment_order":[{"fulfillment_order_id":1046000857}],"tracking_info":{"number":"MS1562678","url":"https://www.my-shipping-company.com?tracking_number=MS1562678"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000857
          }
        ];
        fulfillment.tracking_info = {
          "number": "MS1562678",
          "url": "https://www.my-shipping-company.com?tracking_number=MS1562678"
        };
        await fulfillment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id" => 1046000857
          }
        ]
        fulfillment.tracking_info = {
          "number" => "MS1562678",
          "url" => "https://www.my-shipping-company.com?tracking_number=MS1562678"
        }
        fulfillment.save!

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000857
          }
        ];
        fulfillment.tracking_info = {
          "number": "MS1562678",
          "url": "https://www.my-shipping-company.com?tracking_number=MS1562678"
        };
        await fulfillment.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment":{"id":1069019898,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:36:42-05:00","service":"manual","updated_at":"2026-01-09T22:36:42-05:00","tracking_company":null,"shipment_status":null,"location_id":24826418,"origin_address":null,"line_items":[{"id":1071823265,"variant_id":389013007,"title":"Crafty Shoes - Red","quantity":1,"sku":"crafty_shoes_red","variant_title":"Small","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":910489600,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Crafty Shoes - Red - Small","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":0,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823265","tax_lines":[]}],"tracking_number":"MS1562678","tracking_numbers":["MS1562678"],"tracking_url":"https://www.my-shipping-company.com?tracking_number=MS1562678","tracking_urls":["https://www.my-shipping-company.com?tracking_number=MS1562678"],"receipt":{},"name":"#1001.2","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019898"}}

  * ####  Create a fulfillment with a tracking number provided. Tracking url and tracking company name will be determined automatically as the tracking number format unambiguously maps to a supported company (UPS).

#####

        curl -d '{"fulfillment":{"line_items_by_fulfillment_order":[{"fulfillment_order_id":1046000852}],"tracking_info":{"number":"1Z001985YW99744790"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000852
          }
        ];
        fulfillment.tracking_info = {
          "number": "1Z001985YW99744790"
        };
        await fulfillment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id" => 1046000852
          }
        ]
        fulfillment.tracking_info = {
          "number" => "1Z001985YW99744790"
        }
        fulfillment.save!

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000852
          }
        ];
        fulfillment.tracking_info = {
          "number": "1Z001985YW99744790"
        };
        await fulfillment.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment":{"id":1069019892,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:36:28-05:00","service":"manual","updated_at":"2026-01-09T22:36:28-05:00","tracking_company":"UPS","shipment_status":null,"location_id":24826418,"origin_address":null,"line_items":[{"id":1071823255,"variant_id":389013007,"title":"Crafty Shoes - Red","quantity":1,"sku":"crafty_shoes_red","variant_title":"Small","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":910489600,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Crafty Shoes - Red - Small","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":0,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823255","tax_lines":[]}],"tracking_number":"1Z001985YW99744790","tracking_numbers":["1Z001985YW99744790"],"tracking_url":"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790","tracking_urls":["https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790"],"receipt":{},"name":"#1001.2","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019892"}}

  * #### Create a fulfillment for all fulfillment order line items if `fulfillment_order_line_items` is left blank

#####

        curl -d '{"fulfillment":{"message":"The package was shipped this morning.","notify_customer":false,"tracking_info":{"number":"MS1562678","url":"https://www.my-shipping-company.com?tracking=MS1562678"},"line_items_by_fulfillment_order":[{"fulfillment_order_id":1046000858}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.message = "The package was shipped this morning.";
        fulfillment.notify_customer = false;
        fulfillment.tracking_info = {
          "number": "MS1562678",
          "url": "https://www.my-shipping-company.com?tracking=MS1562678"
        };
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000858
          }
        ];
        await fulfillment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.message = "The package was shipped this morning."
        fulfillment.notify_customer = false
        fulfillment.tracking_info = {
          "number" => "MS1562678",
          "url" => "https://www.my-shipping-company.com?tracking=MS1562678"
        }
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id" => 1046000858
          }
        ]
        fulfillment.save!

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.message = "The package was shipped this morning.";
        fulfillment.notify_customer = false;
        fulfillment.tracking_info = {
          "number": "MS1562678",
          "url": "https://www.my-shipping-company.com?tracking=MS1562678"
        };
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000858
          }
        ];
        await fulfillment.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment":{"id":1069019900,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:36:45-05:00","service":"manual","updated_at":"2026-01-09T22:36:45-05:00","tracking_company":null,"shipment_status":null,"location_id":24826418,"origin_address":null,"line_items":[{"id":1071823267,"variant_id":389013007,"title":"Crafty Shoes - Red","quantity":1,"sku":"crafty_shoes_red","variant_title":"Small","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":910489600,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Crafty Shoes - Red - Small","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":0,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823267","tax_lines":[]}],"tracking_number":"MS1562678","tracking_numbers":["MS1562678"],"tracking_url":"https://www.my-shipping-company.com?tracking=MS1562678","tracking_urls":["https://www.my-shipping-company.com?tracking=MS1562678"],"receipt":{},"name":"#1001.2","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019900"}}

  * #### Create a fulfillment for the fulfillment order line items specified

#####

        curl -d '{"fulfillment":{"message":"The package was shipped this morning.","notify_customer":false,"tracking_info":{"number":"1Z001985YW99744790","company":"UPS"},"line_items_by_fulfillment_order":[{"fulfillment_order_id":1046000860,"fulfillment_order_line_items":[{"id":1072503386,"quantity":1}]}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.message = "The package was shipped this morning.";
        fulfillment.notify_customer = false;
        fulfillment.tracking_info = {
          "number": "1Z001985YW99744790",
          "company": "UPS"
        };
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000860,
            "fulfillment_order_line_items": [
              {
                "id": 1072503386,
                "quantity": 1
              }
            ]
          }
        ];
        await fulfillment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.message = "The package was shipped this morning."
        fulfillment.notify_customer = false
        fulfillment.tracking_info = {
          "number" => "1Z001985YW99744790",
          "company" => "UPS"
        }
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id" => 1046000860,
            "fulfillment_order_line_items" => [
              {
                "id" => 1072503386,
                "quantity" => 1
              }
            ]
          }
        ]
        fulfillment.save!

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.message = "The package was shipped this morning.";
        fulfillment.notify_customer = false;
        fulfillment.tracking_info = {
          "number": "1Z001985YW99744790",
          "company": "UPS"
        };
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000860,
            "fulfillment_order_line_items": [
              {
                "id": 1072503386,
                "quantity": 1
              }
            ]
          }
        ];
        await fulfillment.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment":{"id":1069019903,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:36:50-05:00","service":"manual","updated_at":"2026-01-09T22:36:50-05:00","tracking_company":"UPS","shipment_status":null,"location_id":24826418,"origin_address":null,"line_items":[{"id":1071823269,"variant_id":389013007,"title":"Crafty Shoes - Red","quantity":1,"sku":"crafty_shoes_red","variant_title":"Small","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":910489600,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Crafty Shoes - Red - Small","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":0,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823269","tax_lines":[]}],"tracking_number":"1Z001985YW99744790","tracking_numbers":["1Z001985YW99744790"],"tracking_url":"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790","tracking_urls":["https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790"],"receipt":{},"name":"#1001.2","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019903"}}

  * #### Create a fulfillment without tracking info. Tracking numbers can be set later with the <code>/admin/api/API_VERSION/fulfillments/FULFILLMENT_ID/update_tracking.json</code> endpoint.

#####

        curl -d '{"fulfillment":{"line_items_by_fulfillment_order":[{"fulfillment_order_id":1046000851}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000851
          }
        ];
        await fulfillment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id" => 1046000851
          }
        ]
        fulfillment.save!

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.line_items_by_fulfillment_order = [
          {
            "fulfillment_order_id": 1046000851
          }
        ];
        await fulfillment.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment":{"id":1069019890,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:36:26-05:00","service":"manual","updated_at":"2026-01-09T22:36:26-05:00","tracking_company":null,"shipment_status":null,"location_id":24826418,"origin_address":null,"line_items":[{"id":1071823253,"variant_id":389013007,"title":"Crafty Shoes - Red","quantity":1,"sku":"crafty_shoes_red","variant_title":"Small","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":910489600,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Crafty Shoes - Red - Small","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":0,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823253","tax_lines":[]}],"tracking_number":null,"tracking_numbers":[],"tracking_url":null,"tracking_urls":[],"receipt":{},"name":"#1001.2","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019890"}}


* * *

##

[Anchor to POST request, Cancels a fulfillment](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-cancel)

post

Cancels a fulfillment

[fulfillmentCancel](/docs/api/admin-graphql/latest/mutations/fulfillmentCancel?example=cancels-a-fulfillment)

Cancels a fulfillment.

###

[Anchor to Parameters of Cancels a fulfillment](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-cancel-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillments-fulfillment-id-cancel-examples](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-cancel-examples)Examples

Cancel a fulfillment

Path parameters

fulfillment_id=1069019896

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillments/1069019896/cancel.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments/1069019896/cancel.json" \

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

HTTP/1.1 200 OK

{

"fulfillment": {

"order_id": 450789469,

"status": "cancelled",

"shipment_status": null,

"location_id": 24826418,

"id": 1069019896,

"created_at": "2026-01-09T22:32:40-05:00",

"service": "manual",

"updated_at": "2026-01-09T22:36:40-05:00",

"tracking_company": "UPS",

"origin_address": {

"address1": "150 Elgin St",

"city": "Ottawa",

"zip": "K2P 1L4",

"province_code": "ON",

"country_code": "CA"

},

"line_items": [

{

"id": 1071823262,

"variant_id": 43729076,

"title": "Draft",

"quantity": 1,

"sku": "draft-151",

"variant_title": "151cm",

"vendor": "Birthday Present Factory",

"fulfillment_service": "manual",

"product_id": 108828309,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "Draft - 151cm",

"variant_inventory_management": null,

"properties": [],

"product_exists": true,

"fulfillable_quantity": 1,

"grams": 0,

"price": "10.00",

"total_discount": "0.00",

"fulfillment_status": "fulfilled",

"price_set": {

"shop_money": {

"amount": "10.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "10.00",

"currency_code": "USD"

}

},

"total_discount_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "USD"

}

},

"discount_allocations": [],

"duties": [],

"admin_graphql_api_id": "gid://shopify/LineItem/1071823262",

"tax_lines": []

}

],

"tracking_number": "#☠1☢\n---\n4321\n",

"tracking_numbers": [

"#☠1☢\n---\n4321\n"

],

"tracking_url": "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321",

"tracking_urls": [

"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321"

],

"receipt": {},

"name": "#1001.1",

"admin_graphql_api_id": "gid://shopify/Fulfillment/1069019896"

}

}

### examples

  * #### Cancel a fulfillment

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments/1069019896/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.id = 1069019896;
        await fulfillment.cancel({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.id = 1069019896
        fulfillment.cancel(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.id = 1069019896;
        await fulfillment.cancel({});

#### response

        HTTP/1.1 200 OK{"fulfillment":{"order_id":450789469,"status":"cancelled","shipment_status":null,"location_id":24826418,"id":1069019896,"created_at":"2026-01-09T22:32:40-05:00","service":"manual","updated_at":"2026-01-09T22:36:40-05:00","tracking_company":"UPS","origin_address":{"address1":"150 Elgin St","city":"Ottawa","zip":"K2P 1L4","province_code":"ON","country_code":"CA"},"line_items":[{"id":1071823262,"variant_id":43729076,"title":"Draft","quantity":1,"sku":"draft-151","variant_title":"151cm","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":108828309,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Draft - 151cm","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823262","tax_lines":[]}],"tracking_number":"#☠1☢\n---\n4321\n","tracking_numbers":["#☠1☢\n---\n4321\n"],"tracking_url":"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321","tracking_urls":["https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321"],"receipt":{},"name":"#1001.1","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019896"}}


* * *

##

[Anchor to POST request, Updates the tracking information for a fulfillment](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-update-tracking)

post

Updates the tracking information for a fulfillment

[fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate?example=updates-the-tracking-information-for-a-fulfillment)

Updates the tracking information for a fulfillment.

###

[Anchor to Parameters of Updates the tracking information for a fulfillment](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-update-tracking-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

tracking_info

object**object**

required**required**

The tracking information for the fulfillment.

Show tracking_info properties

  * **company** : (string) The name of the tracking company.

For the tracking company names from the list below Shopify automatically builds tracking URLs for all of the provided tracking numbers, which makes the tracking numbers clickable in the interface.

Additionally, for the tracking companies listed on the [Shipping Carriers help page](https://help.shopify.com/en/manual/shipping/understanding-shipping/shipping-carriers#integrated-shipping-carriers) Shopify will automatically update the fulfillment's `shipment_status` field during the fulfillment process.

Note

Send the tracking company name exactly as written in the list below (capitalization matters).

**Note:**

Send the tracking company name exactly as written in the list below (capitalization matters).

#### Supported tracking companies

The following tracking companies display for shops located in any country:

    * **4PX**
    * **AGS**
    * **Amazon Logistics UK**
    * **Amazon Logistics US**
    * **An Post**
    * **Anjun Logistics**
    * **APC**
    * **Asendia USA**
    * **Australia Post**
    * **Bonshaw**
    * **BPost**
    * **BPost International**
    * **Canada Post**
    * **Canpar**
    * **CDL Last Mile**
    * **China Post**
    * **Chronopost**
    * **Chukou1**
    * **Colissimo**
    * **Comingle**
    * **Coordinadora**
    * **Correios**
    * **Correos**
    * **CTT**
    * **CTT Express**
    * **Cyprus Post**
    * **Delnext**
    * **Deutsche Post**
    * **DHL eCommerce**
    * **DHL eCommerce Asia**
    * **DHL Express**
    * **DPD**
    * **DPD Local**
    * **DPD UK**
    * **DTD Express**
    * **DX**
    * **Eagle**
    * **Estes**
    * **Evri**
    * **FedEx**
    * **First Global Logistics**
    * **First Line**
    * **FSC**
    * **Fulfilla**
    * **GLS**
    * **Guangdong Weisuyi Information Technology (WSE)**
    * **Heppner Internationale Spedition GmbH & Co.**
    * **Iceland Post**
    * **IDEX**
    * **Israel Post**
    * **Japan Post (EN)**
    * **Japan Post (JA)**
    * **La Poste**
    * **Lasership**
    * **Latvia Post**
    * **Lietuvos Paštas**
    * **Logisters**
    * **Lone Star Overnight**
    * **M3 Logistics**
    * **Meteor Space**
    * **Mondial Relay**
    * **New Zealand Post**
    * **NinjaVan**
    * **North Russia Supply Chain (Shenzhen) Co.**
    * **OnTrac**
    * **Packeta**
    * **Pago Logistics**
    * **Ping An Da Tengfei Express**
    * **Pitney Bowes**
    * **Portal PostNord**
    * **Poste Italiane**
    * **PostNL**
    * **PostNord DK**
    * **PostNord NO**
    * **PostNord SE**
    * **Purolator**
    * **Qxpress**
    * **Qyun Express**
    * **Royal Mail**
    * **Royal Shipments**
    * **Sagawa (EN)**
    * **Sagawa (JA)**
    * **Sendle**
    * **SF Express**
    * **SFC Fulfillment**
    * **SHREE NANDAN COURIER**
    * **Singapore Post**
    * **Southwest Air Cargo**
    * **StarTrack**
    * **Step Forward Freight**
    * **Swiss Post**
    * **TForce Final Mile**
    * **Tinghao**
    * **TNT**
    * **Toll IPEC**
    * **United Delivery Service**
    * **UPS**
    * **USPS**
    * **Venipak**
    * **We Post**
    * **Whistl**
    * **Wizmo**
    * **WMYC**
    * **Xpedigo**
    * **XPO Logistics**
    * **Yamato (EN)**
    * **Yamato (JA)**
    * **YiFan Express**
    * **YunExpress**

The following tracking companies are displayed for shops located in specific countries:

    * **Australia** : Australia Post, Sendle, Aramex Australia, TNT Australia, Hunter Express, Couriers Please, Bonds, Allied Express, Direct Couriers, Northline, GO Logistics
    * **Austria** : Österreichische Post
    * **Bulgaria** : Speedy
    * **Canada** : Intelcom, BoxKnight, Loomis, GLS
    * **China** : China Post, DHL eCommerce Asia, WanbExpress, YunExpress, Anjun Logistics, SFC Fulfillment, FSC
    * **Czechia** : Zásilkovna
    * **Germany** : Deutsche Post (DE), Deutsche Post (EN), DHL, DHL Express, Swiship, Hermes, GLS
    * **Spain** : SEUR
    * **France** : Colissimo, Mondial Relay, Colis Privé, GLS
    * **United Kingdom** : Evri, DPD UK, Parcelforce, Yodel, DHL Parcel, Tuffnells
    * **Greece** : ACS Courier
    * **Hong Kong SAR** : SF Express
    * **Ireland** : Fastway, DPD Ireland
    * **India** : DTDC, India Post, Delhivery, Gati KWE, Professional Couriers, XpressBees, Ecom Express, Ekart, Shadowfax, Bluedart
    * **Italy** : BRT, GLS Italy
    * **Japan** : エコ配, 西濃運輸, 西濃スーパーエキスプレス, 福山通運, 日本通運, 名鉄運輸, 第一貨物
    * **Netherlands** : DHL Parcel, DPD
    * **Norway** : Bring
    * **Poland** : Inpost
    * **Turkey** : PTT, Yurtiçi Kargo, Aras Kargo, Sürat Kargo
    * **United States** : GLS, Alliance Air Freight, Pilot Freight, LSO, Old Dominion, R+L Carriers, Southwest Air Cargo
    * **South Africa** : Fastway, Skynet
  * **number** : (string) The tracking number for the fulfillment.

The tracking number will be clickable in the interface if one of the following applies (the highest in the list has the highest priority):

    * Tracking URL provided in the `url` field.
    * Shopify-known tracking company name specified in the `company` field. Shopify will build the tracking url automatically based on the tracking number specified.
    * The tracking number has a Shopify-known format. Shopify will guess the tracking provider and build the tracking url based on the tracking number format. Not all tracking carriers are supported, and multiple tracking carriers may use similarly formatted tracking numbers. This can result in an invalid tracking URL. It is highly recommended that you send the tracking company and the tracking URL.

Note

With the REST API, you can set only one tracking number and one tracking URL per fulfillment. If you send multiple shipments with one fulfillment, you may want to specify tracking numbers and tracking URLs for all of them. You can do it with the equivalent GraphQL [fulfillmentCreate](/docs/api/admin-graphql/unstable/mutations/fulfillmentCreate) and [fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/unstable/mutations/fulfillmentTrackingInfoUpdate) mutations.

**Note:**

With the REST API, you can set only one tracking number and one tracking URL per fulfillment. If you send multiple shipments with one fulfillment, you may want to specify tracking numbers and tracking URLs for all of them. You can do it with the equivalent GraphQL [fulfillmentCreate](/docs/api/admin-graphql/unstable/mutations/fulfillmentCreate) and [fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/unstable/mutations/fulfillmentTrackingInfoUpdate) mutations.

  * **url** : (string) The URL to track the fulfillment.

The tracking URL is displayed in the merchant's admin in the order page. The tracking URL is displayed in the shipping confirmation email, which can optionally be sent to the customer. When accounts are enabled, it is also displayed in the customer's order history.

The URL must be an [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) and [RFC 3987](https://datatracker.ietf.org/doc/html/rfc3987)-compliant URI string. For example, `https://www.myshipping.com/track/?tracknumbers=TRACKING_NUMBER` is a valid URL. It includes a scheme (`https`) and a host (`myshipping.com`). If you do not provide a scheme (`http` or `https`), then `http` will be substituted.


* * *

notify_customer

boolean**boolean**

Whether the customer will be notified of this update and future updates for the fulfillment.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillments-fulfillment-id-update-tracking-examples](/docs/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-update-tracking-examples)Examples

Update the tracking information for a fulfillment with a supported tracking company name and a tracking number. Notify the customer about the tracking details provided.

Path parameters

fulfillment_id=1069019893

string**string**

required**required**

Update the tracking information for a fulfillment with a tracking number and a tracking url

Path parameters

fulfillment_id=1069019895

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillments/1069019893/update_tracking.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment":{"notify_customer":true,"tracking_info":{"company":"UPS","number":"1Z001985YW99744790"}}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments/1069019893/update_tracking.json" \

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

HTTP/1.1 200 OK

{

"fulfillment": {

"tracking_company": "UPS",

"shipment_status": null,

"location_id": 24826418,

"status": "success",

"id": 1069019893,

"order_id": 450789469,

"created_at": "2026-01-09T22:32:40-05:00",

"service": "manual",

"updated_at": "2026-01-09T22:36:30-05:00",

"origin_address": {

"address1": "150 Elgin St",

"city": "Ottawa",

"zip": "K2P 1L4",

"province_code": "ON",

"country_code": "CA"

},

"line_items": [

{

"id": 1071823256,

"variant_id": 43729076,

"title": "Draft",

"quantity": 1,

"sku": "draft-151",

"variant_title": "151cm",

"vendor": "Birthday Present Factory",

"fulfillment_service": "manual",

"product_id": 108828309,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "Draft - 151cm",

"variant_inventory_management": null,

"properties": [],

"product_exists": true,

"fulfillable_quantity": 1,

"grams": 0,

"price": "10.00",

"total_discount": "0.00",

"fulfillment_status": null,

"price_set": {

"shop_money": {

"amount": "10.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "10.00",

"currency_code": "USD"

}

},

"total_discount_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "USD"

}

},

"discount_allocations": [],

"duties": [],

"admin_graphql_api_id": "gid://shopify/LineItem/1071823256",

"tax_lines": []

}

],

"tracking_number": "1Z001985YW99744790",

"tracking_numbers": [

"1Z001985YW99744790"

],

"tracking_url": "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790",

"tracking_urls": [

"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790"

],

"receipt": {},

"name": "#1001.1",

"admin_graphql_api_id": "gid://shopify/Fulfillment/1069019893"

}

}

### examples

  * #### Update the tracking information for a fulfillment with a supported tracking company name and a tracking number. Notify the customer about the tracking details provided.

#####

        curl -d '{"fulfillment":{"notify_customer":true,"tracking_info":{"company":"UPS","number":"1Z001985YW99744790"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments/1069019893/update_tracking.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.id = 1069019893;
        await fulfillment.update_tracking({
          body: {"fulfillment": {"notify_customer": true, "tracking_info": {"company": "UPS", "number": "1Z001985YW99744790"}}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.id = 1069019893
        fulfillment.update_tracking(
          session: test_session,
          body: {"fulfillment" => {"notify_customer" => true, "tracking_info" => {"company" => "UPS", "number" => "1Z001985YW99744790"}}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.id = 1069019893;
        await fulfillment.update_tracking({
          body: {"fulfillment": {"notify_customer": true, "tracking_info": {"company": "UPS", "number": "1Z001985YW99744790"}}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment":{"tracking_company":"UPS","shipment_status":null,"location_id":24826418,"status":"success","id":1069019893,"order_id":450789469,"created_at":"2026-01-09T22:32:40-05:00","service":"manual","updated_at":"2026-01-09T22:36:30-05:00","origin_address":{"address1":"150 Elgin St","city":"Ottawa","zip":"K2P 1L4","province_code":"ON","country_code":"CA"},"line_items":[{"id":1071823256,"variant_id":43729076,"title":"Draft","quantity":1,"sku":"draft-151","variant_title":"151cm","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":108828309,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Draft - 151cm","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823256","tax_lines":[]}],"tracking_number":"1Z001985YW99744790","tracking_numbers":["1Z001985YW99744790"],"tracking_url":"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790","tracking_urls":["https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1Z001985YW99744790"],"receipt":{},"name":"#1001.1","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019893"}}

  * #### Update the tracking information for a fulfillment with a tracking number and a tracking url

#####

        curl -d '{"fulfillment":{"notify_customer":true,"tracking_info":{"number":"1111","url":"http://www.my-url.com"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillments/1069019895/update_tracking.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment = new admin.rest.resources.Fulfillment({session: session});

        fulfillment.id = 1069019895;
        await fulfillment.update_tracking({
          body: {"fulfillment": {"notify_customer": true, "tracking_info": {"number": "1111", "url": "http://www.my-url.com"}}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment = ShopifyAPI::Fulfillment.new(session: test_session)
        fulfillment.id = 1069019895
        fulfillment.update_tracking(
          session: test_session,
          body: {"fulfillment" => {"notify_customer" => true, "tracking_info" => {"number" => "1111", "url" => "http://www.my-url.com"}}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment = new shopify.rest.Fulfillment({session: session});
        fulfillment.id = 1069019895;
        await fulfillment.update_tracking({
          body: {"fulfillment": {"notify_customer": true, "tracking_info": {"number": "1111", "url": "http://www.my-url.com"}}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment":{"tracking_company":null,"shipment_status":null,"location_id":24826418,"status":"success","id":1069019895,"order_id":450789469,"created_at":"2026-01-09T22:32:40-05:00","service":"manual","updated_at":"2026-01-09T22:36:37-05:00","origin_address":{"address1":"150 Elgin St","city":"Ottawa","zip":"K2P 1L4","province_code":"ON","country_code":"CA"},"line_items":[{"id":1071823260,"variant_id":43729076,"title":"Draft","quantity":1,"sku":"draft-151","variant_title":"151cm","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":108828309,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Draft - 151cm","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823260","tax_lines":[]}],"tracking_number":"1111","tracking_numbers":["1111"],"tracking_url":"http://www.my-url.com","tracking_urls":["http://www.my-url.com"],"receipt":{},"name":"#1001.1","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019895"}}


* * *

##

[Anchor to GET request, Retrieves fulfillments associated with a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillment#get-fulfillment-orders-fulfillment-order-id-fulfillments)

get

Retrieves fulfillments associated with a fulfillment order

[fulfillmentOrder](/docs/api/admin-graphql/latest/queries/fulfillmentOrder?example=retrieves-fulfillments-associated-with-a-fulfillment-order)

Retrieves fulfillments associated with a fulfillment order.

###

[Anchor to Parameters of Retrieves fulfillments associated with a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillment#get-fulfillment-orders-fulfillment-order-id-fulfillments-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

fulfillment_order_id

The ID of the fulfillment order that is associated with the fulfillments.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-fulfillment-orders-fulfillment-order-id-fulfillments-examples](/docs/api/admin-rest/latest/resources/fulfillment#get-fulfillment-orders-fulfillment-order-id-fulfillments-examples)Examples

Retrieve a list of all fulfillments for a fulfillment order

Was this section helpful?

YesNo

get

## /admin/api/2026-01/fulfillment_orders/1046000854/fulfillments.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000854/fulfillments.json" \

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

80

81

82

83

HTTP/1.1 200 OK

{

"fulfillments": [

{

"id": 1069019894,

"order_id": 450789469,

"status": "success",

"created_at": "2026-01-09T22:32:40-05:00",

"service": "manual",

"updated_at": "2026-01-09T22:32:40-05:00",

"tracking_company": "UPS",

"shipment_status": null,

"location_id": 24826418,

"origin_address": {

"address1": "150 Elgin St",

"city": "Ottawa",

"zip": "K2P 1L4",

"province_code": "ON",

"country_code": "CA"

},

"line_items": [

{

"id": 1071823258,

"variant_id": 43729076,

"title": "Draft",

"quantity": 1,

"sku": "draft-151",

"variant_title": "151cm",

"vendor": "Birthday Present Factory",

"fulfillment_service": "manual",

"product_id": 108828309,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "Draft - 151cm",

"variant_inventory_management": null,

"properties": [],

"product_exists": true,

"fulfillable_quantity": 1,

"grams": 0,

"price": "10.00",

"total_discount": "0.00",

"fulfillment_status": null,

"price_set": {

"shop_money": {

"amount": "10.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "10.00",

"currency_code": "USD"

}

},

"total_discount_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "USD"

}

},

"discount_allocations": [],

"duties": [],

"admin_graphql_api_id": "gid://shopify/LineItem/1071823258",

"tax_lines": []

}

],

"tracking_number": "#☠1☢\n---\n4321\n",

"tracking_numbers": [

"#☠1☢\n---\n4321\n"

],

"tracking_url": "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321",

"tracking_urls": [

"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321"

],

"receipt": {},

"name": "#1001.1",

"admin_graphql_api_id": "gid://shopify/Fulfillment/1069019894"

}

]

}

### examples

  * #### Retrieve a list of all fulfillments for a fulfillment order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000854/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Fulfillment.all({
          session: session,
          fulfillment_order_id: 1046000854,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Fulfillment.all(
          session: test_session,
          fulfillment_order_id: 1046000854,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Fulfillment.all({
          session: session,
          fulfillment_order_id: 1046000854,
        });

#### response

        HTTP/1.1 200 OK{"fulfillments":[{"id":1069019894,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:32:40-05:00","service":"manual","updated_at":"2026-01-09T22:32:40-05:00","tracking_company":"UPS","shipment_status":null,"location_id":24826418,"origin_address":{"address1":"150 Elgin St","city":"Ottawa","zip":"K2P 1L4","province_code":"ON","country_code":"CA"},"line_items":[{"id":1071823258,"variant_id":43729076,"title":"Draft","quantity":1,"sku":"draft-151","variant_title":"151cm","vendor":"Birthday Present Factory","fulfillment_service":"manual","product_id":108828309,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"Draft - 151cm","variant_inventory_management":null,"properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":0,"price":"10.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/1071823258","tax_lines":[]}],"tracking_number":"#☠1☢\n---\n4321\n","tracking_numbers":["#☠1☢\n---\n4321\n"],"tracking_url":"https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321","tracking_urls":["https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=#☠1☢---4321"],"receipt":{},"name":"#1001.1","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019894"}]}


* * *

##

[Anchor to GET request, Retrieves fulfillments associated with an order](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments)

get

Retrieves fulfillments associated with an order

[order](/docs/api/admin-graphql/latest/queries/order)

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace_orders`.:**

Retrieves fulfillments associated with an order. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves fulfillments associated with an order](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

created_at_max

Show fulfillments created before date (format: 2014-04-25T16:15:47-04:00).

* * *

created_at_min

Show fulfillments created after date (format: 2014-04-25T16:15:47-04:00).

* * *

fields

A comma-separated list of fields to include in the response.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

Limit the amount of results.

* * *

since_id

Restrict results to after the specified ID.

* * *

updated_at_max

Show fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Show fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-fulfillments-examples](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-examples)Examples

Retrieve a list of all fulfillments for an order

Path parameters

order_id=450789469

string**string**

required**required**

Retrieve all fulfillments after the specified ID

Path parameters

order_id=450789469

string**string**

required**required**

Query parameters

since_id=255858046

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/fulfillments.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments.json" \

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

120

121

122

HTTP/1.1 200 OK

{

"fulfillments": [

{

"id": 255858046,

"order_id": 450789469,

"status": "failure",

"created_at": "2026-01-09T22:32:40-05:00",

"service": "manual",

"updated_at": "2026-01-09T22:32:40-05:00",

"tracking_company": "USPS",

"shipment_status": null,

"location_id": 655441491,

"origin_address": null,

"line_items": [

{

"id": 466157049,

"variant_id": 39072856,

"title": "IPod Nano - 8gb",

"quantity": 1,

"sku": "IPOD2008GREEN",

"variant_title": "green",

"vendor": null,

"fulfillment_service": "manual",

"product_id": 632910392,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "IPod Nano - 8gb - green",

"variant_inventory_management": "shopify",

"properties": [

{

"name": "Custom Engraving Front",

"value": "Happy Birthday"

},

{

"name": "Custom Engraving Back",

"value": "Merry Christmas"

}

],

"product_exists": true,

"fulfillable_quantity": 0,

"grams": 200,

"price": "199.00",

"total_discount": "0.00",

"fulfillment_status": null,

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

"total_discount_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "USD"

}

},

"discount_allocations": [

{

"amount": "3.34",

"discount_application_index": 0,

"amount_set": {

"shop_money": {

"amount": "3.34",

"currency_code": "USD"

},

"presentment_money": {

"amount": "3.34",

"currency_code": "USD"

}

}

}

],

"admin_graphql_api_id": "gid://shopify/LineItem/466157049",

"duties": [],

"tax_lines": [

{

"price": "3.98",

"rate": 0.06,

"title": "State Tax",

"price_set": {

"shop_money": {

"amount": "3.98",

"currency_code": "USD"

},

"presentment_money": {

"amount": "3.98",

"currency_code": "USD"

}

},

"channel_liable": null

}

],

"fulfillment_line_item_id": 225088298

}

],

"tracking_number": "1Z1234512345123456",

"tracking_numbers": [

"1Z1234512345123456"

],

"tracking_url": "https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456",

"tracking_urls": [

"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"

],

"receipt": {

"testcase": true,

"authorization": "123456"

},

"name": "#1001.0",

"admin_graphql_api_id": "gid://shopify/Fulfillment/255858046"

}

]

}

### examples

  * #### Retrieve a list of all fulfillments for an order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Fulfillment.all({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Fulfillment.all(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Fulfillment.all({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"fulfillments":[{"id":255858046,"order_id":450789469,"status":"failure","created_at":"2026-01-09T22:32:40-05:00","service":"manual","updated_at":"2026-01-09T22:32:40-05:00","tracking_company":"USPS","shipment_status":null,"location_id":655441491,"origin_address":null,"line_items":[{"id":466157049,"variant_id":39072856,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008GREEN","variant_title":"green","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - green","variant_inventory_management":"shopify","properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"product_exists":true,"fulfillable_quantity":0,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.34","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}}}],"admin_graphql_api_id":"gid://shopify/LineItem/466157049","duties":[],"tax_lines":[{"price":"3.98","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"channel_liable":null}],"fulfillment_line_item_id":225088298}],"tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"receipt":{"testcase":true,"authorization":"123456"},"name":"#1001.0","admin_graphql_api_id":"gid://shopify/Fulfillment/255858046"}]}

  * #### Retrieve all fulfillments after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments.json?since_id=255858046" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Fulfillment.all({
          session: session,
          order_id: 450789469,
          since_id: "255858046",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Fulfillment.all(
          session: test_session,
          order_id: 450789469,
          since_id: "255858046",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Fulfillment.all({
          session: session,
          order_id: 450789469,
          since_id: "255858046",
        });

#### response

        HTTP/1.1 200 OK{"fulfillments":[{"id":1069019901,"order_id":450789469,"status":"success","created_at":"2026-01-09T22:36:47-05:00","service":"shipwire-app","updated_at":"2026-01-09T22:36:47-05:00","tracking_company":"my-custom-shipping-company","shipment_status":null,"location_id":24826418,"origin_address":null,"line_items":[{"id":518995019,"variant_id":49148385,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008RED","variant_title":"red","vendor":null,"fulfillment_service":"shipwire-app","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - red","variant_inventory_management":"shopify","properties":[],"product_exists":true,"fulfillable_quantity":0,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":"fulfilled","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.33","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}}}],"admin_graphql_api_id":"gid://shopify/LineItem/518995019","duties":[],"tax_lines":[{"price":"3.98","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"channel_liable":null}],"fulfillment_line_item_id":1036448668}],"tracking_number":"123456789","tracking_numbers":["123456789"],"tracking_url":"http://my-custom-shipping-company.shopifyapps.com/track/123456","tracking_urls":["http://my-custom-shipping-company.shopifyapps.com/track/123456","http://my-custom-shipping-company.shopifyapps.com/track/789012"],"receipt":{},"name":"#1001.1","admin_graphql_api_id":"gid://shopify/Fulfillment/1069019901"}]}


* * *

##

[Anchor to GET request, Receive a single Fulfillment](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-fulfillment-id)

get

Receive a single Fulfillment

[fulfillment](/docs/api/admin-graphql/latest/queries/fulfillment?example=receive-a-single-fulfillment)

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace_orders`.:**

Retrieve a specific fulfillment

###

[Anchor to Parameters of Receive a single Fulfillment](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-fulfillment-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

fields

Comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-fulfillments-fulfillment-id-examples](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-fulfillment-id-examples)Examples

Retrieve a specific fulfillment

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/fulfillments/255858046.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046.json" \

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

"fulfillment": {

"id": 255858046,

"order_id": 450789469,

"status": "failure",

"created_at": "2026-01-09T22:32:40-05:00",

"service": "manual",

"updated_at": "2026-01-09T22:32:40-05:00",

"tracking_company": "USPS",

"shipment_status": null,

"location_id": 655441491,

"origin_address": null,

"line_items": [

{

"id": 466157049,

"variant_id": 39072856,

"title": "IPod Nano - 8gb",

"quantity": 1,

"sku": "IPOD2008GREEN",

"variant_title": "green",

"vendor": null,

"fulfillment_service": "manual",

"product_id": 632910392,

"requires_shipping": true,

"taxable": true,

"gift_card": false,

"name": "IPod Nano - 8gb - green",

"variant_inventory_management": "shopify",

"properties": [

{

"name": "Custom Engraving Front",

"value": "Happy Birthday"

},

{

"name": "Custom Engraving Back",

"value": "Merry Christmas"

}

],

"product_exists": true,

"fulfillable_quantity": 1,

"grams": 200,

"price": "199.00",

"total_discount": "0.00",

"fulfillment_status": null,

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

"total_discount_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "USD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "USD"

}

},

"discount_allocations": [

{

"amount": "3.34",

"discount_application_index": 0,

"amount_set": {

"shop_money": {

"amount": "3.34",

"currency_code": "USD"

},

"presentment_money": {

"amount": "3.34",

"currency_code": "USD"

}

}

}

],

"duties": [],

"admin_graphql_api_id": "gid://shopify/LineItem/466157049",

"tax_lines": [

{

"title": "State Tax",

"price": "3.98",

"rate": 0.06,

"channel_liable": null,

"price_set": {

"shop_money": {

"amount": "3.98",

"currency_code": "USD"

},

"presentment_money": {

"amount": "3.98",

"currency_code": "USD"

}

}

}

]

}

],

"tracking_number": "1Z1234512345123456",

"tracking_numbers": [

"1Z1234512345123456"

],

"tracking_url": "https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456",

"tracking_urls": [

"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"

],

"receipt": {

"testcase": true,

"authorization": "123456"

},

"name": "#1001.0",

"admin_graphql_api_id": "gid://shopify/Fulfillment/255858046"

}

}

### examples

  * #### Retrieve a specific fulfillment

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Fulfillment.find({
          session: session,
          order_id: 450789469,
          id: 255858046,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Fulfillment.find(
          session: test_session,
          order_id: 450789469,
          id: 255858046,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Fulfillment.find({
          session: session,
          order_id: 450789469,
          id: 255858046,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment":{"id":255858046,"order_id":450789469,"status":"failure","created_at":"2026-01-09T22:32:40-05:00","service":"manual","updated_at":"2026-01-09T22:32:40-05:00","tracking_company":"USPS","shipment_status":null,"location_id":655441491,"origin_address":null,"line_items":[{"id":466157049,"variant_id":39072856,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008GREEN","variant_title":"green","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - green","variant_inventory_management":"shopify","properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"product_exists":true,"fulfillable_quantity":1,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.34","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}}}],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/466157049","tax_lines":[{"title":"State Tax","price":"3.98","rate":0.06,"channel_liable":null,"price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}}}]}],"tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"receipt":{"testcase":true,"authorization":"123456"},"name":"#1001.0","admin_graphql_api_id":"gid://shopify/Fulfillment/255858046"}}


* * *

##

[Anchor to GET request, Retrieves a count of fulfillments associated with a specific order](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-count)

get

Retrieves a count of fulfillments associated with a specific order

[order](/docs/api/admin-graphql/latest/queries/order)

Requires `orders` access scope.

**Requires `orders` access scope.:**

Retrieves a count of fulfillments associated with a specific order

###

[Anchor to Parameters of Retrieves a count of fulfillments associated with a specific order](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

created_at_max

Count fulfillments created before date (format: 2014-04-25T16:15:47-04:00).

* * *

created_at_min

Count fulfillments created after date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_max

Count fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Count fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-fulfillments-count-examples](/docs/api/admin-rest/latest/resources/fulfillment#get-orders-order-id-fulfillments-count-examples)Examples

Count the total number of fulfillments for an order

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/fulfillments/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/count.json" \

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

  * #### Count the total number of fulfillments for an order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Fulfillment.count({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Fulfillment.count(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Fulfillment.count({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"count":1}