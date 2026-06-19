# buy/order/resources/guest_purchase_order/methods/getGuestPurchaseOrder

*Source: https://developer.ebay.com/api-docs/buy/order/resources/guest_purchase_order/methods/getGuestPurchaseOrder*

---

## Input

### Resource URI

### URI parameters

### HTTP request headers

### OAuth scope

### Request payload

### Request fields

## Output

### HTTP response headers

### Response payload

### Response fields

### HTTP status codes

## Error codes

## Warnings

## Samples

### Sample 1: Get the Details of a Guest Purchase Order

#### Thank you for helping us to improve the eBay developer program.
GET/guest_purchase_order/{purchaseOrderId}
Note:The Order API (v2) currently only supports the guest payment/checkout flow. If you need to support member payment/checkout flow, use thev1_beta versionof the Order API.Important!(Limited Release)This method is only available to select developers approved by business units.This method retrieves the details about a specific guest purchase order. It returns the line items, including purchase  order status, dates created and modified, item quantity and listing data, payment and shipping information, and prices, taxes, discounts and credits.ThepurchaseOrderIdis passed in as a URI parameter and is required.Note:ThepurchaseOrderIdvalue is returned in the call-back URL that is sent through the new eBay pay widget. For more information about eBay managed payments and the new Order API payment flow, seeOrder APIin the Buying Integration Guide.You can use this method to not only get the details of a purchase order, but to check the value of thepurchaseOrderPaymentStatusfield to determine if the order has been paid for. If the order has been paid for, this field will returnPAID.For a list of supported sites and other restrictions, seeAPI Restrictionsin the Order API overview.
Important!(Limited Release)This method is only available to select developers approved by business units.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Conditional
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.guest.order
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
An array of line items in the order.Occurrence:Always
Occurrence:Always
A container that is returned for orders that are eligible for eBay's Authenticity Guarantee program. The seller ships Authenticity Guarantee program items to the authentication partner instead of the buyer. If the item is successfully authenticated, the authenticator will ship the item to the buyer.Occurrence:Conditional
An informational message that applies to the Authenticity Guarantee program.Occurrence:Conditional
An informational message regarding the authentication outcome of an Authenticity Guarantee verification inspection.Note:This field is conditionally returned when there is information that applies to the Authenticity Guarantee program.Occurrence:Conditional
An enumerated value that indicates whether the order line item has passed or failed the Authenticity Guarantee verification inspection, or whether the inspection and/or results are still pending.Note:This field is conditionally returned when the purchase is complete.Valid Values:PENDINGPASSEDFAILEDINELIGIBLEOccurrence:Conditional
The terms and conditions that apply to the Authenticity Guarantee program.Occurrence:Conditional
The cost of a single quantity of the line item.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
A breakdown of the fees applicable to the line item.Occurrence:Conditional
A container for the currency type and monetary amount of the fee associated with the line item.Occurrence:Conditional
The type of fee associated with the line item.Occurrence:Conditional
An eBay-assigned URL of the item image.Occurrence:Always
The URL for the image.Occurrence:Always
The eBay identifier of an item. This ID is returned by theBrowseandFeedAPI methods.Occurrence:Always
When this value istrueit indicates that the item has been put on hold due to a violation of eBay Policy.Occurrence:Conditional
A container that returns fields to support using thePost Order APIfor returns and cancellations. For information about what is returned in these fields and how to use the Post Order API, seeUsing the Post Order API.Note:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
The legacy ID used to identify an item.This is used by the Post Order APICreate Return Requestmethod. This call initiates the item return process. For more information on how to use this field in the Post Order API, seeCreate a return requestin the Buy Integration Guide.Restriction:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
The legacy ID of the order.This is used by the Post Order APISubmit Cancellation Requestmethod. This method initiates the item cancellation process. For more information on how to use this field in the Post Order API, seeUsing the Post Order API.Restriction:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
The legacy ID of the transaction.This is used by the Post Order APICreate Return Requestcall. This call initiates the item return process. For more information on how to use this field in the Post Order API, seeUsing the Post Order APIin the Buy Integration Guide.Restriction:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
A unique eBay-assigned ID value that identifies a line item in a checkout session. This is created by theinitiateGuestCheckoutSession.Occurrence:Always
An enumeration value that indicates the payment status of the line item.Occurrence:Always
An enumeration value that indicates the fulfillment state of this line item.Note:When there is no tracking information, the status will never change fromFULFILLMENT_IN_PROGRESS; without tracking information, eBay has no way of knowing whether the order was delivered.Occurrence:Always
The total cost for the line item, taking into account the quantity, any seller item discounts, and any coupon that applies.Note:This does not include any shipping discounts, shipping costs, fees, or seller adjustments.Occurrence:Always
The unique order ID for the line item.Maximum Length:40 charactersOccurrence:Conditional
An array of promotions applied to the line item.Occurrence:Conditional
The details regarding the monetary value of the promotional discount.Note:eBay Bucks are not supported.Occurrence:Conditional
The text for the promotion title, which describes the promotion.Occurrence:Conditional
The kind of promotion. Some examples are:SellerDiscountedPromotionalOfferandCOUPON.Occurrence:Conditional
The quantity ordered for the line item.Occurrence:Always
A container for information about the seller offering this item, such as the seller's user name.Occurrence:Always
The user name created by the seller for use on eBay.Occurrence:Always
A container for information about the shipping details of the order.Occurrence:Conditional
The end of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).Occurrence:Conditional
The beginning of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).Occurrence:Conditional
The shipping provider for the line item, such as FedEx or USPS.Occurrence:Conditional
The name of the shipping service option. For example, Priority Mail Express (provided by USPS) or FedEx International Priority (Provided by FedEx).Occurrence:Conditional
A container for the tax information for the line item.Occurrence:Conditional
A field that indicates whether tax was applied for the cost of the item and its shipping.Occurrence:Conditional
A container that returns the tax jurisdiction information.Occurrence:Conditional
The region of the tax jurisdiction.Occurrence:Conditional
A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level, or at the country level in the case of VAT tax.Occurrence:Conditional
An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCECOUNTRYOccurrence:Conditional
The identifier of the tax jurisdiction.Occurrence:Conditional
A field that indicates the type of tax that may be collected for the item.Occurrence:Conditional
The seller-created title of the item.Occurrence:Conditional
A container that breaks down the costs for the order, including total cost, shipping cost, tax, fees, and any discounts.Occurrence:Always
The total amount of the coupon discounts in the purchase order.Occurrence:Conditional
The total amount of any seller adjustments. An adjustment can be a credit or debit. This is used to catch any monetary changes to the order that are not already captured in one of the other fields.Occurrence:Always
The container that returns the amount and currency of an adjustment.Occurrence:Always
The text indicating what the adjustment was for.Occurrence:Always
The delivery cost for all of the line items, after any delivery discounts are applied.For example, there are four line items, and the delivery cost for each line item is $5. One of the line items qualifies for free delivery. ThedeliveryCostwould be $15, which is the total cost for delivering all of the line items after the discount is applied.Note:The cost includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The total amount of the order delivery discounts for all of the line items, such as free shipping.Occurrence:Conditional
The total amount of any fees for all the line items in the order, such as a recycling fee.Occurrence:Always
The sum of allGlobal Shipping Programimport charges, for all the line items in the order.Occurrence:Conditional
The type of import tax applicable to the order, and the total amount of tax for all line items in the order.Occurrence:Conditional
The total amount of import tax for all line items of an order.Occurrence:Conditional
An enumeration value that indicates the type of import tax applicable to the order. Currently, the only applicable import tax is theGoods and Servicestax (indicated withGST). The Goods and Services tax is only applicable to orders for the eBay Australia marketplace.Occurrence:Conditional
The total discount amount for all line items in the order.For example, there are four line items in the order. Two of the line items qualify for aBuy 1, Get 1offer, which is a $6 and a $15 discount. ThepriceDiscountvalue returned would be 21, which is the total of the two discounts.Note:Delivery discount amounts, if applicable, are not reflected in the value returned in this field.Occurrence:Always
The total cost for all line items in the order, taking into account the item quantity, but before adding taxes and delivery costs, or applying discounts, fees, and adjustments.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The total amount of taxes for all line items in the order.Occurrence:Always
The total cost of the order, which includes: (priceSubtotal-priceDiscount) +deliveryCost+tax+/-adjustment+fee+importCharges-additionalSavings.Occurrence:Always
The creation date of the purchase order.Occurrence:Always
The unique identifier of the purchase order.Occurrence:Always
A container that returns the payment status for the purchase order.Occurrence:Always
An enumeration value that indicates the current status of the buyer's payment and any refund that applies to the purchase order.Occurrence:Always
The total amount of any refunds for the purchase order.Occurrence:Conditional
A container for any warning messages.Occurrence:Conditional
This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.Occurrence:Conditional
The name of the primary system where the error occurred. This is relevant for application errors.Occurrence:Conditional
A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.Occurrence:Conditional
An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.Occurrence:Conditional
A detailed description of the condition that caused the error or warning, and information on what what must be done to correct the problem.Occurrence:Conditional
A description of the condition that caused the error or warning.Occurrence:Conditional
An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.Occurrence:Conditional
The name of the input field that caused an issue with the method request.Occurrence:Conditional
The actual value that was passed in for the element specified in thenamefield.Occurrence:Conditional
The name of the subdomain in which the error or warning occurred.Occurrence:NA
Occurrence:NA
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample returns the details for the specified guest purchase order.
The input is thepurchaseOrderIdURI parameter. There is no payload with this request.
GEThttps://api.ebay.com/buy/order/v2/guest_purchase_order/2*************2
The output shows that the specified purchase order contained one line item. The total cost of the item was 102.00 (pricingSummary.total) and the purchase order was paid for but as not been shipped (purchaseOrderPaymentStatus=PAIDandpurchaseOrderStatus=PENDING).
Related topics
If you need help, contactDeveloper Technical Support.
- PENDING
- PASSED
- FAILED
- INELIGIBLE
- STATE_OR_PROVINCE
- COUNTRY
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
purchaseOrderId | string | This path parameter specifies the unique identifier of a purchase order made by a guest buyer, for which details are to be retrieved.Note:This value is returned in the response URL that is sent through the new eBay pay widget. For more information about eBay managed payments and the new Order API payment flow, seeOrder APIin the Buying Integration Guide.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
X-EBAY-C-ENDUSERCTX | string | This header is used to specify thedeviceIdfor the device/user attempting to make the call.It contains an alphanumeric string that allows a payment gateway to track an API call attempt and confirm that it is a verified payment attempt by a device/user.Occurrence:Conditional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the eBay marketplace where the order will occur.Note:For this method, this value must match theX-EBAY-C-MARKETPLACE-IDused when the associated checkout session was created.SeeHTTP request headersfor the marketplace ID values.Occurrence:Conditional
[/TABLE]

[TABLE]
Output container/field | Type | Description
lineItems | array ofOrderLineItemV2 | An array of line items in the order.Occurrence:Always
lineItems.authenticityVerification | AuthenticityVerificationProgram | A container that is returned for orders that are eligible for eBay's Authenticity Guarantee program. The seller ships Authenticity Guarantee program items to the authentication partner instead of the buyer. If the item is successfully authenticated, the authenticator will ship the item to the buyer.Occurrence:Conditional
lineItems.authenticityVerification.description | string | An informational message that applies to the Authenticity Guarantee program.Occurrence:Conditional
lineItems.authenticityVerification.outcomeReason | string | An informational message regarding the authentication outcome of an Authenticity Guarantee verification inspection.Note:This field is conditionally returned when there is information that applies to the Authenticity Guarantee program.Occurrence:Conditional
lineItems.authenticityVerification.status | AuthenticityVerificationStatusEnum | An enumerated value that indicates whether the order line item has passed or failed the Authenticity Guarantee verification inspection, or whether the inspection and/or results are still pending.Note:This field is conditionally returned when the purchase is complete.Valid Values:PENDINGPASSEDFAILEDINELIGIBLEOccurrence:Conditional
lineItems.authenticityVerification.termsWebUrl | string | The terms and conditions that apply to the Authenticity Guarantee program.Occurrence:Conditional
lineItems.baseUnitPrice | Amount | The cost of a single quantity of the line item.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
lineItems.baseUnitPrice.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.baseUnitPrice.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.fees | array ofFee | A breakdown of the fees applicable to the line item.Occurrence:Conditional
lineItems.fees.amount | Amount | A container for the currency type and monetary amount of the fee associated with the line item.Occurrence:Conditional
lineItems.fees.amount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.fees.amount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.fees.feeType | FeeEnum | The type of fee associated with the line item.Occurrence:Conditional
lineItems.image | Image | An eBay-assigned URL of the item image.Occurrence:Always
lineItems.image.imageUrl | string | The URL for the image.Occurrence:Always
lineItems.itemId | string | The eBay identifier of an item. This ID is returned by theBrowseandFeedAPI methods.Occurrence:Always
lineItems.itemOnHold | boolean | When this value istrueit indicates that the item has been put on hold due to a violation of eBay Policy.Occurrence:Conditional
lineItems.legacyReference | LegacyReference | A container that returns fields to support using thePost Order APIfor returns and cancellations. For information about what is returned in these fields and how to use the Post Order API, seeUsing the Post Order API.Note:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
lineItems.legacyReference.legacyItemId | string | The legacy ID used to identify an item.This is used by the Post Order APICreate Return Requestmethod. This call initiates the item return process. For more information on how to use this field in the Post Order API, seeCreate a return requestin the Buy Integration Guide.Restriction:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
lineItems.legacyReference.legacyOrderId | string | The legacy ID of the order.This is used by the Post Order APISubmit Cancellation Requestmethod. This method initiates the item cancellation process. For more information on how to use this field in the Post Order API, seeUsing the Post Order API.Restriction:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
lineItems.legacyReference.legacyTransactionId | string | The legacy ID of the transaction.This is used by the Post Order APICreate Return Requestcall. This call initiates the item return process. For more information on how to use this field in the Post Order API, seeUsing the Post Order APIin the Buy Integration Guide.Restriction:The Post Order API can be used only with eBay member checkouts.Occurrence:Conditional
lineItems.lineItemId | string | A unique eBay-assigned ID value that identifies a line item in a checkout session. This is created by theinitiateGuestCheckoutSession.Occurrence:Always
lineItems.lineItemPaymentStatus | LineItemPaymentStatusEnum | An enumeration value that indicates the payment status of the line item.Occurrence:Always
lineItems.lineItemStatus | LineItemStatusEnum | An enumeration value that indicates the fulfillment state of this line item.Note:When there is no tracking information, the status will never change fromFULFILLMENT_IN_PROGRESS; without tracking information, eBay has no way of knowing whether the order was delivered.Occurrence:Always
lineItems.netPrice | Amount | The total cost for the line item, taking into account the quantity, any seller item discounts, and any coupon that applies.Note:This does not include any shipping discounts, shipping costs, fees, or seller adjustments.Occurrence:Always
lineItems.netPrice.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.netPrice.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.orderId | string | The unique order ID for the line item.Maximum Length:40 charactersOccurrence:Conditional
lineItems.promotions | array ofPromotion | An array of promotions applied to the line item.Occurrence:Conditional
lineItems.promotions.discount | Amount | The details regarding the monetary value of the promotional discount.Note:eBay Bucks are not supported.Occurrence:Conditional
lineItems.promotions.discount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.promotions.discount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.promotions.message | string | The text for the promotion title, which describes the promotion.Occurrence:Conditional
lineItems.promotions.promotionType | string | The kind of promotion. Some examples are:SellerDiscountedPromotionalOfferandCOUPON.Occurrence:Conditional
lineItems.quantity | integer | The quantity ordered for the line item.Occurrence:Always
lineItems.seller | Seller | A container for information about the seller offering this item, such as the seller's user name.Occurrence:Always
lineItems.seller.username | string | The user name created by the seller for use on eBay.Occurrence:Always
lineItems.shippingDetail | ShippingDetail | A container for information about the shipping details of the order.Occurrence:Conditional
lineItems.shippingDetail.maxEstimatedDeliveryDate | string | The end of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).Occurrence:Conditional
lineItems.shippingDetail.minEstimatedDeliveryDate | string | The beginning of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).Occurrence:Conditional
lineItems.shippingDetail.shippingCarrierCode | string | The shipping provider for the line item, such as FedEx or USPS.Occurrence:Conditional
lineItems.shippingDetail.shippingServiceCode | string | The name of the shipping service option. For example, Priority Mail Express (provided by USPS) or FedEx International Priority (Provided by FedEx).Occurrence:Conditional
lineItems.taxDetails | array ofTaxDetail | A container for the tax information for the line item.Occurrence:Conditional
lineItems.taxDetails.includedInPrice | boolean | A field that indicates whether tax was applied for the cost of the item and its shipping.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction | TaxJurisdiction | A container that returns the tax jurisdiction information.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction.region | Region | The region of the tax jurisdiction.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction.region.regionName | string | A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level, or at the country level in the case of VAT tax.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction.region.regionType | RegionTypeEnum | An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCECOUNTRYOccurrence:Conditional
lineItems.taxDetails.taxJurisdiction.taxJurisdictionId | string | The identifier of the tax jurisdiction.Occurrence:Conditional
lineItems.taxDetails.taxType | TaxType | A field that indicates the type of tax that may be collected for the item.Occurrence:Conditional
lineItems.title | string | The seller-created title of the item.Occurrence:Conditional
pricingSummary | PricingSummary | A container that breaks down the costs for the order, including total cost, shipping cost, tax, fees, and any discounts.Occurrence:Always
pricingSummary.additionalSavings | Amount | The total amount of the coupon discounts in the purchase order.Occurrence:Conditional
pricingSummary.additionalSavings.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.additionalSavings.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.adjustment | Adjustment | The total amount of any seller adjustments. An adjustment can be a credit or debit. This is used to catch any monetary changes to the order that are not already captured in one of the other fields.Occurrence:Always
pricingSummary.adjustment.amount | Amount | The container that returns the amount and currency of an adjustment.Occurrence:Always
pricingSummary.adjustment.amount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.adjustment.amount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.adjustment.label | string | The text indicating what the adjustment was for.Occurrence:Always
pricingSummary.deliveryCost | Amount | The delivery cost for all of the line items, after any delivery discounts are applied.For example, there are four line items, and the delivery cost for each line item is $5. One of the line items qualifies for free delivery. ThedeliveryCostwould be $15, which is the total cost for delivering all of the line items after the discount is applied.Note:The cost includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
pricingSummary.deliveryCost.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.deliveryCost.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.deliveryDiscount | Amount | The total amount of the order delivery discounts for all of the line items, such as free shipping.Occurrence:Conditional
pricingSummary.deliveryDiscount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.deliveryDiscount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.fee | Amount | The total amount of any fees for all the line items in the order, such as a recycling fee.Occurrence:Always
pricingSummary.fee.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.fee.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importCharges | Amount | The sum of allGlobal Shipping Programimport charges, for all the line items in the order.Occurrence:Conditional
pricingSummary.importCharges.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importCharges.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importTax | ImportTax | The type of import tax applicable to the order, and the total amount of tax for all line items in the order.Occurrence:Conditional
pricingSummary.importTax.amount | Amount | The total amount of import tax for all line items of an order.Occurrence:Conditional
pricingSummary.importTax.amount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importTax.amount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importTax.importTaxType | ImportTaxTypeEnum | An enumeration value that indicates the type of import tax applicable to the order. Currently, the only applicable import tax is theGoods and Servicestax (indicated withGST). The Goods and Services tax is only applicable to orders for the eBay Australia marketplace.Occurrence:Conditional
pricingSummary.priceDiscount | Amount | The total discount amount for all line items in the order.For example, there are four line items in the order. Two of the line items qualify for aBuy 1, Get 1offer, which is a $6 and a $15 discount. ThepriceDiscountvalue returned would be 21, which is the total of the two discounts.Note:Delivery discount amounts, if applicable, are not reflected in the value returned in this field.Occurrence:Always
pricingSummary.priceDiscount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.priceDiscount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.priceSubtotal | Amount | The total cost for all line items in the order, taking into account the item quantity, but before adding taxes and delivery costs, or applying discounts, fees, and adjustments.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
pricingSummary.priceSubtotal.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.priceSubtotal.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.tax | Amount | The total amount of taxes for all line items in the order.Occurrence:Always
pricingSummary.tax.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.tax.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.total | Amount | The total cost of the order, which includes: (priceSubtotal-priceDiscount) +deliveryCost+tax+/-adjustment+fee+importCharges-additionalSavings.Occurrence:Always
pricingSummary.total.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.total.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
purchaseOrderCreationDate | string | The creation date of the purchase order.Occurrence:Always
purchaseOrderId | string | The unique identifier of the purchase order.Occurrence:Always
purchaseOrderPaymentStatus | PurchaseOrderPaymentStatusEnum | A container that returns the payment status for the purchase order.Occurrence:Always
purchaseOrderStatus | PurchaseOrderStatusEnum | An enumeration value that indicates the current status of the buyer's payment and any refund that applies to the purchase order.Occurrence:Always
refundedAmount | Amount | The total amount of any refunds for the purchase order.Occurrence:Conditional
refundedAmount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
refundedAmount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
warnings | array ofErrorDetailV3 | A container for any warning messages.Occurrence:Conditional
warnings.category | string | This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.Occurrence:Conditional
warnings.domain | string | The name of the primary system where the error occurred. This is relevant for application errors.Occurrence:Conditional
warnings.errorId | integer | A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.Occurrence:Conditional
warnings.inputRefIds | array ofstring | An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.Occurrence:Conditional
warnings.longMessage | string | A detailed description of the condition that caused the error or warning, and information on what what must be done to correct the problem.Occurrence:Conditional
warnings.message | string | A description of the condition that caused the error or warning.Occurrence:Conditional
warnings.outputRefIds | array ofstring | An array of reference IDs that identify the specific response elements most closely associated to the error or warning, if any.Occurrence:Conditional
warnings.parameters | array ofErrorParameterV3 | An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.Occurrence:Conditional
warnings.parameters.name | string | The name of the input field that caused an issue with the method request.Occurrence:Conditional
warnings.parameters.value | string | The actual value that was passed in for the element specified in thenamefield.Occurrence:Conditional
warnings.subdomain | string | The name of the subdomain in which the error or warning occurred.Occurrence:NA
[/TABLE]

[TABLE]
200 | OK
403 | Access Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
16001 | API_ORDER | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
16002 | API_ORDER | REQUEST | The purchase order ID was not found.
16003 | API_ORDER | REQUEST | Access to the purchase order is not authorized.
[/TABLE]