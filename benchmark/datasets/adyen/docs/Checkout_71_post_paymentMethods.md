# Checkout/71/post/paymentMethods

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/paymentMethods*

---

# Get a list of available payment methods
Retrieves the list of available payment methods for the transaction, based on the transaction information like amount, country, and currency.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
This field contains additional data, which may be required for a particular payment request.
TheadditionalDataobject consists of entries, each of which includes the key and value.
List of payment methods to be presented to the shopper. To refer to payment methods, use theirpayment method type.
Example:"allowedPaymentMethods":["ideal","applepay"]
The amount information for the transaction (inminor units). ForBIN or card verificationrequests, set amount to 0 (zero).
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
List of payment methods to be hidden from the shopper. To refer to payment methods, use theirpayment method type.
Example:"blockedPaymentMethods":["ideal","applepay"]
The shopper's browser information.
For 3D Secure, the full object is required for web integrations. For mobile app integrations, include theuserAgentandacceptHeaderfields to indicate  that your integration can support a redirect in case a payment is routed to 3D Secure 2 redirect.
The accept header value of the shopper's browser.
The color depth of the shopper's browser in bits per pixel. This should be obtained by using the browser'sscreen.colorDepthproperty. Accepted values: 1, 4, 8, 15, 16, 24, 30, 32 or 48 bit color depth.
Boolean value indicating if the shopper's browser is able to execute Java.
Boolean value indicating if the shopper's browser is able to execute JavaScript. A default 'true' value is assumed if the field is not present.
Thenavigator.languagevalue of the shopper's browser (as defined in IETF BCP 47).
The total height of the shopper's device screen in pixels.
The total width of the shopper's device screen in pixels.
Time difference between UTC time and the shopper's browser local time, in minutes.
The user agent value of the shopper's browser.
The platform where a payment transaction takes place. This field can be used for filtering out payment methods that are only available on specific platforms. Possible values:
- iOS
- Android
- Web
The shopper's country code.
The merchant account identifier, with which you want to process the transaction.
The order information required for partial payments.
The encrypted order data.
ThepspReferencethat belongs to the order.
A unique ID that can be used to associate/paymentMethodsand/paymentsrequests with the same shopper transaction, offering insights into conversion rates.
The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. > Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include thetelephoneNumber.
The shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks).
Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile integrations, if you did not include theshopperEmail. For native mobile integrations, the field is required to support cases where authentication is routed to the redirect flow. This field is also mandatory for some merchants depending on your business model. For more information,contact Support.
The combination of a language code and a country code to specify the language to be used in the payment.
Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
Boolean value indicating whether the card payment method should be split into separate debit and credit options.
Required for Adyen for Platforms integrations if you are a platform model. This is yourreference(onbalance platform) or thestoreReference(in theclassic integration) for the ecommerce or point-of-sale store that is processing the payment.
Specifies how payment methods should be filtered based on thestoreparameter:
- exclusive: Only payment methods belonging to the specifiedstoreare returned.
- inclusive: Payment methods from thestoreand those not associated with any other store are returned.
The shopper's telephone number.
The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesspaymentMethodsarray[object]Detailed list of payment methods required to generate payment forms.Show childrenHide childrenappsarray[object]A list of apps for this payment method.Show childrenHide childrenidstringThe unique identifier of this app, to submit in requests to /payments.namestringA localized name of the app.brandstringBrand for the selected gift card. For example: plastix, hmclub.brandsarray[string]List of possible brands. For example: visa, mc.configurationobjectThe configuration of the payment method.fundingSourcestringThe funding source of the payment method.groupobjectThe group where this payment method belongs to.Show childrenHide childrennamestringThe name of the group.paymentMethodDatastringEcho data to be used if the payment method is displayed as part of this group.typestringThe unique code of the group.inputDetailsarray[object]DeprecatedAll input details to be provided to complete the payment with this payment method.Show childrenHide childrenconfigurationobjectConfiguration parameters for the required input.detailsarray[object]Input details can also be provided recursively.Show childrenHide childrenconfigurationobjectConfiguration parameters for the required input.itemsarray[object]In case of a select, the items to choose from.Show childrenHide childrenidstringThe value to provide in the result.namestringThe display name.keystringThe value to provide in the result.optionalbooleanTrue if this input is optional to provide.typestringThe type of the required input.valuestringThe value can be pre-filled, if available.inputDetailsarray[object]DeprecatedInput details can also be provided recursively (deprecated).Show childrenHide childrenconfigurationobjectConfiguration parameters for the required input.itemsarray[object]In case of a select, the items to choose from.Show childrenHide childrenidstringThe value to provide in the result.namestringThe display name.keystringThe value to provide in the result.optionalbooleanTrue if this input is optional to provide.typestringThe type of the required input.valuestringThe value can be pre-filled, if available.itemSearchUrlstringIn case of a select, the URL from which to query the items.itemsarray[object]In case of a select, the items to choose from.Show childrenHide childrenidstringThe value to provide in the result.namestringThe display name.keystringThe value to provide in the result.optionalbooleanTrue if this input value is optional.typestringThe type of the required input.valuestringThe value can be pre-filled, if available.issuersarray[object]A list of issuers for this payment method.Show childrenHide childrendisabledbooleanA boolean value indicating whether this issuer is unavailable. Can betruewhenever the issuer is offline.idstringThe unique identifier of this issuer, to submit in requests to /payments.namestringA localized name of the issuer.namestringThe displayable name of this payment method.promotedbooleanIndicates whether this payment method should be promoted or not.typestringThe unique payment method code.storedPaymentMethodsarray[object]List of all stored payment methods.Show childrenHide childrenbankAccountNumberstringThe bank account number (without separators).bankLocationIdstringThe location id of the bank. The field value isnilin most cases.brandstringThe brand of the card.expiryMonthstringThe two-digit month when the card expiresexpiryYearstringThe last two digits of the year the card expires. For example,22for the year 2022.holderNamestringThe unique payment method code.ibanstringThe IBAN of the bank account.idstringA unique identifier of this stored payment method.labelstringThe shopper’s issuer account labellastFourstringThe last four digits of the PAN.namestringThe display name of the stored payment method.networkTxReferencestringReturned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.This contains either the Mastercard Trace ID or the Visa Transaction ID.ownerNamestringThe name of the bank account holder.shopperEmailstringThe shopper’s email address.supportedRecurringProcessingModelsarray[string]The supported recurring processing models for this stored payment method.supportedShopperInteractionsarray[string]The supported shopper interactions for this stored payment method.typestringThe type of payment method.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error