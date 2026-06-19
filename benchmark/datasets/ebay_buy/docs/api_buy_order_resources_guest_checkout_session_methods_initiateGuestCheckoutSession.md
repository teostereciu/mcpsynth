# buy/order/resources/guest_checkout_session/methods/initiateGuestCheckoutSession

*Source: https://developer.ebay.com/api-docs/buy/order/resources/guest_checkout_session/methods/initiateGuestCheckoutSession*

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

### Sample 1: Create a Guest Checkout Session

#### Thank you for helping us to improve the eBay developer program.
POST/guest_checkout_session/initiate
Note:The Order API (v2) currently only supports the guest payment/checkout flow. If you need to support member payment/checkout flow, use thev1_beta versionof the Order API.Important!(Limited Release)This method is only available to select developers approved by business units.This method creates an eBay guest checkout session, which is the first step in performing a checkout. The method returns acheckoutSessionIdthat you use as a URI parameter in subsequent guest checkout methods.Note:This method also returns theX-EBAY-SECURITY-SIGNATUREresponse header, which is a token that is used to launch the Checkout with eBay widget. The Checkout with eBay widget allows eBay guests to pay for items without leaving your site. For details about the Checkout with eBay widget, seeIntegrating the Checkout with eBay button.Also seeNegative Testing Using Stubsfor information on how to emulate error conditions for this  method using stubs.TIP:To test the entire checkout flow, you might need a "test" credit card. You can generate a credit card number fromhttp://www.getcreditcardnumbers.com.For a list of supported sites and other restrictions, seeAPI Restrictionsin the Order API overview.
Important!(Limited Release)This method is only available to select developers approved by business units.
This method is supported in Sandbox environment. To access the endpoint, just replace theapix.ebay.comroot URI withapix.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
Occurrence:Conditional
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/buy.guest.order
SeeOAuth access tokensfor more information.
The buyer's email address.Occurrence:Required
An array used to define the line item(s) and desired quantity for an eBay guest checkout session.Maximum:10 line itemsOccurrence:Required
The unique eBay-assigned identifier of an item. This ID is returned by theBrowseandFeedAPI methods. The ID must be in RESTful item ID format.For example:v1|2**********6|5**********4orv1|1**********9|0.For more information about item IDs for RESTful APIs, seeLegacy API compatibility.EachitemIdwill become a single line item.Maximum:10 per sessionOccurrence:Required
The quantity ordered in this line item.Occurrence:Required
A container that defines the shipping address for an eBay guest checkout session.Note:If the address cannot be validated, a warning message is  returned along with the response.Occurrence:Required
The first line of the street address where the item is being shipped.Maximum:40 characters for AU, CA, and US marketplaces35 characters for DE and GB marketplaces50 characters for all other marketplacesOccurrence:Required
The second line of the street address where the item is being shipped. This optional field can be used for information such as 'Suite Number' or 'Apt Number'.Maximum:40 characters for AU, CA, and US marketplaces35 characters for DE and GB marketplaces50 characters for all other marketplacesOccurrence:Optional
Occurrence:Optional
The city of the address where the item is being shipped.Occurrence:Required
The two letter code representing the country of the address.Occurrence:Required
The county of the address where the item is being shipped.Occurrence:Optional
The phone number of the person receiving the package.Note:It is highly recommended that when entering the phone number you include the country code.For example, if a US phone number is4********4, you would enter+14********4. If you do not include this code, the service will use the country specified in thecountryfield.You can find the country code athttps://countrycode.org.Occurrence:Required
The postal code of the address where the item is being shipped.Note:This is optional when shipping to EBAY_HK (Hong Kong).Occurrence:Conditional
The name of the person receiving the package.Occurrence:Required
The first name of the person receiving the purchase order.Occurrence:Required
The last name of the person receiving the purchase order.Occurrence:Required
The state or province of the address.Note:For the US marketplace, this is a two-character value. For a list of valid values, seeUS State and Canada Province Codes.Occurrence:Conditional
SeeHTTP response headersfor details.
A container that returns the information for the coupons that were applied in the guest checkout session.Occurrence:Conditional
The coupon redemption code.Occurrence:Always
Occurrence:Always
The eBay-assigned guest checkout session ID. This ID is created after a successfulinitiateGuestCheckoutSessioncall.Occurrence:Always
An array of line items associated with the guest checkout session.Occurrence:Always
A container returned for orders that are eligible for eBay's Authenticity Guarantee service. The seller ships Authenticity Guarantee service items to the authentication partner instead of the buyer. If the item is successfully authenticated, the authenticator will ship the item to the buyer.Occurrence:Conditional
An informational message that applies to the Authenticity Guarantee program.Occurrence:Conditional
An informational message regarding the authentication outcome of an Authenticity Guarantee verification inspection.Note:This field is conditionally returned when there is information that applies to the Authenticity Guarantee program.Occurrence:Conditional
An enumerated value that indicates whether the order line item has passed or failed the Authenticity Guarantee verification inspection, or whether the inspection and/or results are still pending.Note:This field is conditionally returned when the purchase is complete.Valid Values:PENDINGPASSEDFAILEDINELIGIBLEOccurrence:Conditional
The terms and conditions that apply to the Authenticity Guarantee program.Occurrence:Conditional
The cost of a single quantity of the line item. This is the starting point for computing the price during the checkout session.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
A breakdown of the fees applicable to the line item.Occurrence:Conditional
A container for the currency type and monetary amount of the fee associated with the line item.Occurrence:Conditional
The type of fee associated with the line item.Occurrence:Conditional
An eBay-assigned URL of the item image.Occurrence:Always
The URL for the image.Occurrence:Always
The eBay identifier of an item. This ID is returned by theBrowseandFeedAPI methods. The ID is in RESTful item ID format.For example:v1|2**********6|5**********4orv1|1**********9|0.For more information about item IDs for RESTful APIs, seeLegacy API compatibility.Occurrence:Always
A unique eBay-assigned ID value that identifies a line item in a checkout session.Occurrence:Always
The total cost for the line item, taking into account the quantity, any seller item discounts, and any coupon that applies.Note:This does not include any shipping discounts, shipping costs, fees, or seller adjustments.Occurrence:Always
An array of promotions applied to the line item.Occurrence:Conditional
The details regarding the monetary value of the promotional discount.Note:eBay Bucks are not supported.Occurrence:Conditional
The text for the promotion title, which describes the promotion.Occurrence:Conditional
The kind of promotion. Some examples are:SellerDiscountedPromotionalOfferandCOUPON.Occurrence:Conditional
The quantity ordered for the line item.Occurrence:Always
A container that returns the information about the seller, such as their eBay user name.Occurrence:Always
The user name created by the seller for use on eBay.Occurrence:Always
An array of shipping options that are available for the line item. By default, the first one will be selected.Note:TheupdateGuestShippingOptionmethod can be used to change the shipping option.Occurrence:Always
The delivery cost using this shipping option, for this line item, before any delivery discounts are applied.Note:The cost includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The monetary value of any delivery discounts.Occurrence:Always
TheGlobal Shipping Programimport charges for this line item.Occurrence:Conditional
The end of the date range in which the purchase order is expected to be delivered to the shipping address.Occurrence:Conditional
The beginning of the date range in which the purchase order is expected to be delivered to the shipping address.Occurrence:Conditional
A field that indicates whether the shipping method is selected.Occurrence:Always
The shipping provider for the line item, such as FedEx or USPS.Occurrence:Always
A unique ID for the selected shipping option/method.Occurrence:Always
The name of the shipping service code. For example, Priority Mail Express (provided by USPS) or FedEx International Priority (Provided by FedEx).Occurrence:Always
A container that returns the tax information for the line item.Occurrence:Conditional
A field that indicates whether tax was applied for the cost of the item and its shipping.Occurrence:Conditional
A container that returns the tax jurisdiction information.Occurrence:Conditional
The region of the tax jurisdiction.Occurrence:Conditional
A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level, or at the country level in the case of VAT tax.Occurrence:Conditional
An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCECOUNTRYOccurrence:Conditional
The identifier of the tax jurisdiction.Occurrence:Conditional
A field that indicates the type of tax that may be collected for the item.Occurrence:Conditional
The seller-created title of the item.Occurrence:Always
A container that breaks down the costs for the order, including total cost, shipping cost, tax, fees, and any discounts.Occurrence:Always
The total amount of the coupon discounts in the purchase order.Occurrence:Conditional
The total amount of any seller adjustments. An adjustment can be a credit or debit. This is used to catch any monetary changes to the order that are not already captured in one of the other fields.Occurrence:Always
The container that returns the amount and currency of an adjustment.Occurrence:Always
The text indicating what the adjustment was for.Occurrence:Always
The delivery cost for all of the line items, after any delivery discounts are applied.For example, there are four line items, and the delivery cost for each line item is $5. One of the line items qualifies for free delivery. ThedeliveryCostwould be $15, which is the total cost for delivering all of the line items after the discount is applied.Note:The cost includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The total amount of any fees for all the line items in the order, such as a recycling fee.Occurrence:Always
The sum of allGlobal Shipping Programimport charges, for all the line items in the order.Occurrence:Conditional
The amount of the import charge.Occurrence:Conditional
The type of charge to apply to the order, such as import duties.Occurrence:Conditional
The type of import tax applicable to the order, and the total amount of tax for all line items in the order.Occurrence:Conditional
The total amount of import tax for all line items of an order.Occurrence:Conditional
An enumeration value that indicates the type of import tax applicable to the order. Currently, the only applicable import tax is theGoods and Servicestax (indicated withGST). The Goods and Services tax is only applicable to orders for the eBay Australia marketplace.Occurrence:Conditional
The total discount amount for all line items in the order.For example, there are four line items in the order. Two of the line items qualify for aBuy 1, Get 1offer, which is a $6 and a $15 discount. ThepriceDiscountvalue returned would be 21, which is the total of the two discounts.Note:Delivery discount amounts, if applicable, are not reflected in the value returned in this field.Occurrence:Always
The total cost for all line items in the order, taking into account the item quantity, but before adding taxes and delivery costs, or applying discounts, fees, and adjustments.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
The total amount of taxes for all line items in the order.Occurrence:Always
The total cost of the order, which includes: (priceSubtotal-priceDiscount) +deliveryCost+tax+/-adjustment+fee+importCharges-additionalSavings.Occurrence:Always
A container that returns the address to which the purchase order will be shipped.Occurrence:Always
An array of errors or warnings that were generated during the method processing.Occurrence:Conditional
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
For more on warnings, plus the codes of other common warnings, seeHandling errors.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call starts the checkout session and returns thecheckoutSessionId, which is specific to a marketplace, and the line item IDs. Be sure to store these IDs because you need them for other Order API calls.
The inputs are the buyer's email, name, and address and the item IDs and quantity of each item. You can have a maximum of four individual items of any quantity in a checkout session. Each item is associated with a unique line item.
POSThttps://apix.ebay.com/buy/order/v2/guest_checkout_session/initiate
The output contains thecheckoutSessionId, the shipping address, total cost information, and the line items, which contain the details of the item, such as price, shipping options, and estimated delivery date.
Related topics
If you need help, contactDeveloper Technical Support.
- 40 characters for AU, CA, and US marketplaces
- 35 characters for DE and GB marketplaces
- 50 characters for all other marketplaces
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
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
X-EBAY-C-ENDUSERCTX | string | This header is used to specify thedeviceIdfor the device/user attempting to make the call.It contains an alphanumeric string that allows a payment gateway to track an API call attempt and confirm that it is a verified payment attempt by a device/user.Occurrence:Conditional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the eBay marketplace where the order will occur.SeeHTTP request headersfor the marketplace ID values.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
contactEmail | string | The buyer's email address.Occurrence:Required
lineItemInputs | array ofLineItemInput | An array used to define the line item(s) and desired quantity for an eBay guest checkout session.Maximum:10 line itemsOccurrence:Required
lineItemInputs.itemId | string | The unique eBay-assigned identifier of an item. This ID is returned by theBrowseandFeedAPI methods. The ID must be in RESTful item ID format.For example:v1|2**********6|5**********4orv1|1**********9|0.For more information about item IDs for RESTful APIs, seeLegacy API compatibility.EachitemIdwill become a single line item.Maximum:10 per sessionOccurrence:Required
lineItemInputs.quantity | integer | The quantity ordered in this line item.Occurrence:Required
shippingAddress | ShippingAddress | A container that defines the shipping address for an eBay guest checkout session.Note:If the address cannot be validated, a warning message is  returned along with the response.Occurrence:Required
shippingAddress.addressLine1 | string | The first line of the street address where the item is being shipped.Maximum:40 characters for AU, CA, and US marketplaces35 characters for DE and GB marketplaces50 characters for all other marketplacesOccurrence:Required
shippingAddress.addressLine2 | string | The second line of the street address where the item is being shipped. This optional field can be used for information such as 'Suite Number' or 'Apt Number'.Maximum:40 characters for AU, CA, and US marketplaces35 characters for DE and GB marketplaces50 characters for all other marketplacesOccurrence:Optional
shippingAddress.city | string | The city of the address where the item is being shipped.Occurrence:Required
shippingAddress.country | CountryCodeEnum | The two letter code representing the country of the address.Occurrence:Required
shippingAddress.county | string | The county of the address where the item is being shipped.Occurrence:Optional
shippingAddress.phoneNumber | string | The phone number of the person receiving the package.Note:It is highly recommended that when entering the phone number you include the country code.For example, if a US phone number is4********4, you would enter+14********4. If you do not include this code, the service will use the country specified in thecountryfield.You can find the country code athttps://countrycode.org.Occurrence:Required
shippingAddress.postalCode | string | The postal code of the address where the item is being shipped.Note:This is optional when shipping to EBAY_HK (Hong Kong).Occurrence:Conditional
shippingAddress.recipient | Recipient | The name of the person receiving the package.Occurrence:Required
shippingAddress.recipient.firstName | string | The first name of the person receiving the purchase order.Occurrence:Required
shippingAddress.recipient.lastName | string | The last name of the person receiving the purchase order.Occurrence:Required
shippingAddress.stateOrProvince | string | The state or province of the address.Note:For the US marketplace, this is a two-character value. For a list of valid values, seeUS State and Canada Province Codes.Occurrence:Conditional
[/TABLE]

[TABLE]
X-EBAY-SECURITY-SIGNATURE | A token that is used to launch the Checkout with eBay widget. For details about the Checkout with eBay widget, seeIntegrating the Checkout with eBay button
[/TABLE]

[TABLE]
Output container/field | Type | Description
appliedCoupons | array ofCoupon | A container that returns the information for the coupons that were applied in the guest checkout session.Occurrence:Conditional
appliedCoupons.redemptionCode | string | The coupon redemption code.Occurrence:Always
checkoutSessionId | string | The eBay-assigned guest checkout session ID. This ID is created after a successfulinitiateGuestCheckoutSessioncall.Occurrence:Always
lineItems | array ofLineItem | An array of line items associated with the guest checkout session.Occurrence:Always
lineItems.authenticityVerification | AuthenticityVerificationProgram | A container returned for orders that are eligible for eBay's Authenticity Guarantee service. The seller ships Authenticity Guarantee service items to the authentication partner instead of the buyer. If the item is successfully authenticated, the authenticator will ship the item to the buyer.Occurrence:Conditional
lineItems.authenticityVerification.description | string | An informational message that applies to the Authenticity Guarantee program.Occurrence:Conditional
lineItems.authenticityVerification.outcomeReason | string | An informational message regarding the authentication outcome of an Authenticity Guarantee verification inspection.Note:This field is conditionally returned when there is information that applies to the Authenticity Guarantee program.Occurrence:Conditional
lineItems.authenticityVerification.status | AuthenticityVerificationStatusEnum | An enumerated value that indicates whether the order line item has passed or failed the Authenticity Guarantee verification inspection, or whether the inspection and/or results are still pending.Note:This field is conditionally returned when the purchase is complete.Valid Values:PENDINGPASSEDFAILEDINELIGIBLEOccurrence:Conditional
lineItems.authenticityVerification.termsWebUrl | string | The terms and conditions that apply to the Authenticity Guarantee program.Occurrence:Conditional
lineItems.baseUnitPrice | Amount | The cost of a single quantity of the line item. This is the starting point for computing the price during the checkout session.Note:The price includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
lineItems.baseUnitPrice.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.baseUnitPrice.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.fees | array ofFee | A breakdown of the fees applicable to the line item.Occurrence:Conditional
lineItems.fees.amount | Amount | A container for the currency type and monetary amount of the fee associated with the line item.Occurrence:Conditional
lineItems.fees.amount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.fees.amount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.fees.feeType | FeeEnum | The type of fee associated with the line item.Occurrence:Conditional
lineItems.image | Image | An eBay-assigned URL of the item image.Occurrence:Always
lineItems.image.imageUrl | string | The URL for the image.Occurrence:Always
lineItems.itemId | string | The eBay identifier of an item. This ID is returned by theBrowseandFeedAPI methods. The ID is in RESTful item ID format.For example:v1|2**********6|5**********4orv1|1**********9|0.For more information about item IDs for RESTful APIs, seeLegacy API compatibility.Occurrence:Always
lineItems.lineItemId | string | A unique eBay-assigned ID value that identifies a line item in a checkout session.Occurrence:Always
lineItems.netPrice | Amount | The total cost for the line item, taking into account the quantity, any seller item discounts, and any coupon that applies.Note:This does not include any shipping discounts, shipping costs, fees, or seller adjustments.Occurrence:Always
lineItems.netPrice.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.netPrice.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.promotions | array ofPromotion | An array of promotions applied to the line item.Occurrence:Conditional
lineItems.promotions.discount | Amount | The details regarding the monetary value of the promotional discount.Note:eBay Bucks are not supported.Occurrence:Conditional
lineItems.promotions.discount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.promotions.discount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.promotions.message | string | The text for the promotion title, which describes the promotion.Occurrence:Conditional
lineItems.promotions.promotionType | string | The kind of promotion. Some examples are:SellerDiscountedPromotionalOfferandCOUPON.Occurrence:Conditional
lineItems.quantity | integer | The quantity ordered for the line item.Occurrence:Always
lineItems.seller | Seller | A container that returns the information about the seller, such as their eBay user name.Occurrence:Always
lineItems.seller.username | string | The user name created by the seller for use on eBay.Occurrence:Always
lineItems.shippingOptions | array ofShippingOption | An array of shipping options that are available for the line item. By default, the first one will be selected.Note:TheupdateGuestShippingOptionmethod can be used to change the shipping option.Occurrence:Always
lineItems.shippingOptions.baseDeliveryCost | Amount | The delivery cost using this shipping option, for this line item, before any delivery discounts are applied.Note:The cost includes the value-added tax (VAT) for applicable jurisdictions when requested from supported marketplaces. In this case, users must pass theX-EBAY-C-MARKETPLACE-IDrequest header specifying the supported marketplace (such asEBAY_GB) to see VAT-inclusive pricing. For more information on VAT, refer toVAT Obligations in the EU.Occurrence:Always
lineItems.shippingOptions.baseDeliveryCost.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.shippingOptions.baseDeliveryCost.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.shippingOptions.deliveryDiscount | Amount | The monetary value of any delivery discounts.Occurrence:Always
lineItems.shippingOptions.deliveryDiscount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.shippingOptions.deliveryDiscount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.shippingOptions.importCharges | Amount | TheGlobal Shipping Programimport charges for this line item.Occurrence:Conditional
lineItems.shippingOptions.importCharges.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.shippingOptions.importCharges.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
lineItems.shippingOptions.maxEstimatedDeliveryDate | string | The end of the date range in which the purchase order is expected to be delivered to the shipping address.Occurrence:Conditional
lineItems.shippingOptions.minEstimatedDeliveryDate | string | The beginning of the date range in which the purchase order is expected to be delivered to the shipping address.Occurrence:Conditional
lineItems.shippingOptions.selected | boolean | A field that indicates whether the shipping method is selected.Occurrence:Always
lineItems.shippingOptions.shippingCarrierCode | string | The shipping provider for the line item, such as FedEx or USPS.Occurrence:Always
lineItems.shippingOptions.shippingOptionId | string | A unique ID for the selected shipping option/method.Occurrence:Always
lineItems.shippingOptions.shippingServiceCode | string | The name of the shipping service code. For example, Priority Mail Express (provided by USPS) or FedEx International Priority (Provided by FedEx).Occurrence:Always
lineItems.taxDetails | array ofTaxDetail | A container that returns the tax information for the line item.Occurrence:Conditional
lineItems.taxDetails.includedInPrice | boolean | A field that indicates whether tax was applied for the cost of the item and its shipping.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction | TaxJurisdiction | A container that returns the tax jurisdiction information.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction.region | Region | The region of the tax jurisdiction.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction.region.regionName | string | A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level, or at the country level in the case of VAT tax.Occurrence:Conditional
lineItems.taxDetails.taxJurisdiction.region.regionType | RegionTypeEnum | An enumeration value that indicates the type of region for the tax jurisdiction.Valid Values:STATE_OR_PROVINCECOUNTRYOccurrence:Conditional
lineItems.taxDetails.taxJurisdiction.taxJurisdictionId | string | The identifier of the tax jurisdiction.Occurrence:Conditional
lineItems.taxDetails.taxType | TaxType | A field that indicates the type of tax that may be collected for the item.Occurrence:Conditional
lineItems.title | string | The seller-created title of the item.Occurrence:Always
pricingSummary | PricingSummaryV2 | A container that breaks down the costs for the order, including total cost, shipping cost, tax, fees, and any discounts.Occurrence:Always
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
pricingSummary.fee | Amount | The total amount of any fees for all the line items in the order, such as a recycling fee.Occurrence:Always
pricingSummary.fee.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.fee.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importCharges | ImportChargesV2 | The sum of allGlobal Shipping Programimport charges, for all the line items in the order.Occurrence:Conditional
pricingSummary.importCharges.amount | Amount | The amount of the import charge.Occurrence:Conditional
pricingSummary.importCharges.amount.currency | CurrencyCodeEnum | The currency used in the monetary transaction. Generally, this is the currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importCharges.amount.value | string | The amount of the currency specified in thecurrencyfield. The value of thecurrencydefaults to the standard currency used by the country of the eBay site offering the item.Occurrence:Conditional
pricingSummary.importCharges.applicableChargeType | ApplicableChargeTypeEnum | The type of charge to apply to the order, such as import duties.Occurrence:Conditional
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
shippingAddress | ShippingAddress | A container that returns the address to which the purchase order will be shipped.Occurrence:Always
shippingAddress.addressLine1 | string | The first line of the street address where the item is being shipped.Maximum:40 characters for AU, CA, and US marketplaces35 characters for DE and GB marketplaces50 characters for all other marketplacesOccurrence:Always
shippingAddress.addressLine2 | string | The second line of the street address where the item is being shipped. This optional field can be used for information such as 'Suite Number' or 'Apt Number'.Maximum:40 characters for AU, CA, and US marketplaces35 characters for DE and GB marketplaces50 characters for all other marketplacesOccurrence:Conditional
shippingAddress.city | string | The city of the address where the item is being shipped.Occurrence:Always
shippingAddress.country | CountryCodeEnum | The two letter code representing the country of the address.Occurrence:Always
shippingAddress.county | string | The county of the address where the item is being shipped.Occurrence:Conditional
shippingAddress.phoneNumber | string | The phone number of the person receiving the package.Note:It is highly recommended that when entering the phone number you include the country code.For example, if a US phone number is4********4, you would enter+14********4. If you do not include this code, the service will use the country specified in thecountryfield.You can find the country code athttps://countrycode.org.Occurrence:Always
shippingAddress.postalCode | string | The postal code of the address where the item is being shipped.Note:This is optional when shipping to EBAY_HK (Hong Kong).Occurrence:Conditional
shippingAddress.recipient | Recipient | The name of the person receiving the package.Occurrence:Always
shippingAddress.recipient.firstName | string | The first name of the person receiving the purchase order.Occurrence:Conditional
shippingAddress.recipient.lastName | string | The last name of the person receiving the purchase order.Occurrence:Conditional
shippingAddress.stateOrProvince | string | The state or province of the address.Note:For the US marketplace, this is a two-character value. For a list of valid values, seeUS State and Canada Province Codes.Occurrence:Conditional
warnings | array ofErrorDetailV3 | An array of errors or warnings that were generated during the method processing.Occurrence:Conditional
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
400 | Bad Request
409 | Conflict
500 | Internal Error
[/TABLE]

[TABLE]
15000 | API_ORDER | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
15001 | API_ORDER | REQUEST | Missing field: {fieldName}. The indicated field is required for this request. Add the field and resubmit the call.
15002 | API_ORDER | REQUEST | Invalid field: {fieldName}.  The indicated field contains an invalid value. Correct the value and resubmit the call.
15011 | API_ORDER | BUSINESS | You have exceeded the maximum number of {maxLineItems} line items. Correct the request and resubmit the call.
15012 | API_ORDER | BUSINESS | There is a limit on the quantity of this item that can be purchased. Reduce the quantity and resubmit the call.
15013 | API_ORDER | BUSINESS | The item is either out of stock, or the desired quantity exceeds the quantity available. If out of stock, please wait for seller to restock. If desired quantity exceeds available quantity, please reduce the quantity value and try again.
15014 | API_ORDER | BUSINESS | The quantity submitted for this item is invalid. Correct the quantity value and resubmit the call.
15015 | API_ORDER | BUSINESS | There is a problem with the credit card and it cannot be used to purchase items. Use the updatePaymentInfo call to change the payment information.
15017 | API_ORDER | BUSINESS | The payment for the order line items in your cart could not be processed due to issues with one or more sellers.
15018 | API_ORDER | BUSINESS | The item is not available for purchase. This can be for several reasons including the listing has ended. Remove the item and resubmit the call.
15019 | API_ORDER | BUSINESS | To place an order, you must have at least one line item. Use the initiateCheckoutSession call to add line items (maximum of {maxLineItems}) and create a new checkout session.
15026 | API_ORDER | BUSINESS | The item is not shippable to the specified shipping address.
15027 | API_ORDER | BUSINESS | The value {fieldValue} is not supported for the {fieldName}. The supported values are: {supportedValues}.
15028 | API_ORDER | BUSINESS | The item {itemId} is not available for purchase because it cannot be shipped to {country}.
15029 | API_ORDER | REQUEST | The X-EBAY-C-MARKETPLACE-ID value {fieldValue} is invalid for this checkout session because it is different from the X-EBAY-C-MARKETPLACE-ID header value used to create the session. For all calls in this checkout session, you must use X-EBAY-C-MARKETPLACE-ID {supportedValues}.
15031 | API_ORDER | BUSINESS | The item is not purchasable because the buyer has been blocked by the seller.
15044 | API_ORDER | BUSINESS | At least one of the items in the cart cannot be purchased using this API. The purchase can be done on eBay, through the eBay app or eBay website.
15045 | API_ORDER | BUSINESS | The item cannot be purchased because the seller is away and is not processing orders. If you are trying to purchase more than one item, you need to create a new checkout session to purchase the other items.
15047 | API_ORDER | BUSINESS | In compliance with applicable economic sanctions and trade restrictions, eBay is unavailable in your location. If you believe you are receiving this notice in error, please contact eBay's Customer Service.
15048 | API_ORDER | REQUEST | The value of {fieldName} is too long. For more information, see the documentation for this call.
15053 | API_ORDER | BUSINESS | Your desired item(s) are not available for purchase at this time. The unavailability of an item could be for any of several reasons, including the item being out of stock. Add available item(s) and resubmit the call.
17002 | API_ORDER | REQUEST | Invalid character(s) found in the shipping address. Please check name and shipping address fields, remove invalid character(s) and resubmit the call.
20002 | API_ORDER | BUSINESS | This item {itemId} is currently unavailable to buy from the seller.
[/TABLE]

[TABLE]
15007 | API_ORDER | REQUEST | The address provided may be incorrect. You may proceed with this address or provide a correct address.
15043 | API_ORDER | BUSINESS | The item {itemId} cannot be purchased using this API and has been removed from the cart. The purchase can be done on ebay.com.
15055 | API_ORDER | BUSINESS | The item is removed due to one or more reasons (out of stock, the desired quantity exceeds the quantity available, etc).
20000 | API_ORDER | BUSINESS | This order contains the item {itemId} that may be subject to certain importation permitting/licensing requirements. Please check applicable regulations for specific import restrictions in your country.
20001 | API_ORDER | BUSINESS | This item {itemId} ships via a freight carrier. For information regarding shipping, tracking, delivery, etc. check with the seller.
[/TABLE]