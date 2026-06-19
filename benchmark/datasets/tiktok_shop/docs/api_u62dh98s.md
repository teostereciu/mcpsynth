# For Indonesian market: Changes in Order and Finance APIs for Horizon+ Orders

*Source: https://partner.tiktokshop.com/docv2/page/u62dh98s*

---

The orders with tag "Horizon+" will hide shipping fees at sku prices, so the sku prices will be increased and the shipping fee will be reduced. There are changes in order and finance APIs for this type of order which are estimated to be effective on January 22, 2026. By using these API, the sellers can get the original sku prices and shipping fees. These original sku prices and shipping fees can also be checked at the seller center.
Here is the list of changes:

1. [Get Order Detail](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507) (https://partner.tiktokshop.com/docv2/page/get-order-detail-202507) and [Get Order List](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) (https://partner.tiktokshop.com/docv2/page/get-order-list-202309) API

Response Parameters (Newly added fields in bond lines, existing fields with new logic in italic lines):
| Properties |  | Type | Properties description | New logic  |
| --- | --- | --- | --- | --- |
| code |  | int | The success or failure status code returned in API response. |  |
| message |  | string | The success or failure messages returned in API response. Reasons of failure will be described in the message. |  |
| request_id |  | string | Request log |  |
| data |  | object | Specific return information |  |
| > | orders | []object | Order information. |  |
| **>>**  | **order_rights** | **int** | **Order tag identifier if has certain rights within the order based on the program subscribed by sellers.** <br> **1 = Shipping Fee Reimbursement Program** <br> **2 = Horizon+ Program**  <br> **Applicable for SEA market only**  |  |
| >> | Payment | []object | Payment info about a TikTok Shop order. |  |
| >>> | *sub_total* | *string* | *Buyer paid subtotal of all the SKUs in the order. For the US market, this is pre-tax total amount.sub_total = original_total_product_price - seller_discount - platform_discount.* | *SKUPriceRemainingAmount + SKUPriceOverchargeAmount* |
| >>> | shipping_fee | string | Buyer paid shipping fee. shipping_fee = original_shipping_fee - shipping_fee_seller_discount - shipping_fee_platform_discountFor the US market, this is pre-tax total amount. | ShippingSalePrice (No change) |
| >>> | original_shipping_fee | string | Shipping fee before discount | ShippingListPrice (No Change) |
| >>> | *original_total_product_price* | *string* | *Total original price of products (VAT included for crossborder shop).For the US market, this is pre-tax total amount.* | *Total of SKUlistPrice, if the order is distance fee, then total of SKUOriginListPrice* |
| **>>>** | **distance_shipping_fee** | **string** | **Distance shipping fee is fee that is charged by our logistics partner and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program.** <br> **Only applicable in ID Market.** | **SKUPriceLogisticsAmount** |
| **>>>** | **distance_fee_amount** | **string**  | **Total distance fee for Horizon+ Program. Only applicable for ID market** | **SKUFreightEmbedAmount** |
| >> | line_items | []object | Line item info list. |  |
| **>>>** | *original_price* | *string* | *Item original price, please refer to the currency of payment_info.* | *if hidden fee, then it shows SKUOriginListPrice, but if normal order then it shows SKUlistprice value* |
| **>>>** | *salePrice* | *string* | *Item sale price, please refer to the currency of payment_info.*  <br> *For ID market, if order included in the horizon+ program, the saleprice is equal to final sale product without the distance fee*  | *Item subtotal after discount* |
| **>>>** | **distance_shipping_fee** | **string** | **Distance shipping fee is fee that is charged by our logistics partner and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program.** <br> **Only applicable in ID Market.** | **SKUPriceLogisticsAmount** |
| **>>>** | **distance_fee_amount** | **string**  | **Total distance fee for Horizon+ Program. Only applicable for ID market** | **SKUFreightEmbedAmount** |


2. [Get Price Detail](https://partner.tiktokshop.com/docv2/page/get-price-detail-202407) API (https://partner.tiktokshop.com/docv2/page/get-price-detail-202407)

Response Parameters (Newly added fields in bond lines, existing fields with new logic in italic lines):
| Properties |  | Type | Properties description | New Calculation |
| --- | --- | --- | --- | --- |
| code |  | int | The success or failure status code returned in API response. |  |
| message |  | string | The success or failure messages returned in API response. Reasons of failure will be described in the message. |  |
| request_id |  | string | Request log |  |
| data |  | object | Specific return information |  |
| > | *sku_list_price* | *string* | *Total MSRP price of the products.* | *if hidden fee, then it shows SKUOriginListPrice, but if normal order then it shows SKUlistprice value* |
| > | *subtotal* | *string* | *Total promotional sale price of the products including tax. Calculation: sku_sale_price + subtotal_tax_amount* | *SKUPriceRemainingAmount + SKUPriceOverchargeAmount* |
| > | *sku_sale_price* | *string* | *Total promotional sale price of the products. Calculation: sku_list_price - subtotal_deduction_seller - subtotal_deduction_platform* <br>  <br> *For ID market, if order included in the horizon+ program, the saleprice is equal to final sale product without the distance fee*  |  *New field from pricedetail = SkuListPrice -  Platform discount on items - Seller discount on items -  Distant Shipping fee from Horizon Program - SkuPriceOverChargePlatformAmount = SkuPriceRemainingAmount + SkuPriceOverChargeAmount* |
| > | shipping_list_price | string | Original shipping price  | ShippingListPrice (No change) |
| > | shipping_sale_price | string | Promotional shipping price Calculation: shipping_list_price - shipping_fee_deduction -shipping_fee_deduction_platform | ShippingSalePrice (No Change) |
| > | distance_shipping_fee | string | Distance shipping fee is fee that is charged by our logistics partner and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program. <br> Only applicable in ID Market. | take from SkuPriceLogisticsAmount |
| **>** | **distance_fee** | **string** | **Total distance fee for Horizon+ Program. Only applicable for ID market** | **SKUFreightEmbedAmount** |
| line_items |  | []object | Each object is the same as the "data" field (line 5) without "line_items". |  |
| > | *subtotal* | *string* | *Total promotional sale price of the products including tax. Calculation: sku_sale_price + subtotal_tax_amount* | *Confirm to RD*  |
| > | sku_list_price | string | Total MSRP price of the products. | if hidden fee, then it shows SKUOriginListPrice, but if normal order then it shows SKUlistprice value |
| > | *sku_sale_price* | *string* | *Total promotional sale price of the products. Calculation: sku_list_price - subtotal_deduction_seller - subtotal_deduction_platform* <br>  <br> *For ID market, if order included in the horizon+ program, the saleprice is equal to final sale product without the distance fee*  | *Item subtotal after discount* |
| > | shipping_list_price | string | Original shipping price  | ShippingListPrice (No change) |
| > | shipping_sale_price | string | Promotional shipping price Calculation: shipping_list_price - shipping_fee_deduction -shipping_fee_deduction_platform | ShippingSalePrice (No Change) |
| > | **distance_shipping_fee** | **string** | **Distance shipping fee is fee that is charged by our logistics partner and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program.** <br> **Only applicable in ID Market.** | **take from SkuPriceLogisticsAmount** |
| > | **distance_fee** | **string** | **Total distance fee for Horizon+ Program. Only applicable for ID market** | **SKUFreightEmbedAmount** |


3. Statement APIs changes

| **API name** | **changes** | **Screenshot** |
| --- | --- | --- |
| [Get Statements](https://partner.tiktokshop.com/docv2/page/get-statements-202309) *(https://patner.tiktokshop.com/docv2/page/get-statements-202309)* | * fee_amount will add distant_shipping_fee value <br> * revenue_amount will add distant_item_fee value <br>  <br>  | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/ee95b9dac697473cb27ff43e6bdb97d7~tplv-k9wyc2ijk0-image.image) <br>  |
| [Get Transactions by Order ](https://partner.tiktokshop.com/docv2/page/get-transactions-by-order-202501)*(https://partner.tiktokshop.com/docv2/page/get-transactions-by-order-202501)* | * shipping_cost_amount will add distant_shipping_fee value <br> * revenue_amount will add distant_item_fee value <br> * A new field “distant_shipping_fee” will be shown under shipping_cost_breakdown object <br> * A new field “distant_item_fee” will be shown under revenue_breakdown object <br>  <br>  | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a807a66cbdd7488b9e2d5d808121278d~tplv-k9wyc2ijk0-image.image) <br>  |
| [Get Transactions by Statement](https://partner.tiktokshop.com/docv2/page/get-transactions-by-statement-202501) *(https://patner.tiktokshop.com/docv2/page/get-transactions-by-statement-202501)* | * total_settlement_amount will add distant_shipping_fee value <br> * total_shipping_cost_amount will add distant_shipping_fee value <br> * shipping_cost_amount will add distant_shipping_fee value <br> * revenue_amount will add distant_item_fee value <br> * A new field “distant_shipping_fee” will be shown under shipping_cost_breakdown object <br> * A new field “distant_item_fee” will be shown under revenue_breakdown object <br>  <br>  | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/638190c200b4468c8351504a099b1625~tplv-k9wyc2ijk0-image.image) <br> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e8479a5e9c4e4705aa62a5de59a70730~tplv-k9wyc2ijk0-image.image) <br>  <br>  <br>  |
| [Get Unsettled Transactions](https://partner.tiktokshop.com/docv2/page/get-unsettled-transactions-202507) *(https://partner.tiktokshop.com/docv2/page/get-unsettled-transactions-202507)* | * sum_est_fee_amount will add distant_shipping_fee value <br> * sum_est_revenue_amount will add distant_item_fee value <br> * est_revenue_amount will add distant_item_fee value <br> * est_shipping_cost_amount will add distant_shipping_fee value <br> * A new field “distant_shipping_fee” will be shown under shipping_cost_breakdown object <br> * A new field “distant_item_fee” will be shown under revenue_breakdown object | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1c8497e8257f40458ad4262aabe7f773~tplv-k9wyc2ijk0-image.image) <br> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/69d7780075664941b4ef87a0d85e9df0~tplv-k9wyc2ijk0-image.image) <br>  <br>  <br>  |
# Which markets are affected?
The updates of the requirements apply to the Local to Local sellers for the Indonesian market.
# Who is affected?
Developers with applications that use APIs shown above
# Which version is applicable?
The updates of the requirements apply to the versions shown above.
# What action is required?
Developers need to check whether to use APIs shown above and handle the related error messages.