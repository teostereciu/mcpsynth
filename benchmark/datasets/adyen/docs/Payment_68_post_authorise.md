# Payment/68/post/authorise

*Source: https://docs.adyen.com/api-explorer/Payment/68/post/authorise*

---

# Create an authorisation
Creates a payment with a unique reference (pspReference) and attempts to obtain an authorisation hold. For cards, this amount can be captured or cancelled later. Non-card payment methods typically don't support this and will automatically capture as part of the authorisation.
This endpoint is part of ourclassic API integration. If using anewer integration, use the/paymentsendpoint under Checkout API instead.
Shopper account information for 3D Secure 2.
For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow.
Indicator for the length of time since this shopper account was created in the merchant's environment.
Allowed values:
- notApplicable
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
Date when the shopper's account was last changed.
Indicator for the length of time since the shopper's account was last updated.
Allowed values:
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
Date when the shopper's account was created.
Indicates the type of account. For example, for a multi-account card product.
Allowed values:
- notApplicable
- credit
- debit
Number of attempts the shopper tried to add a card to their account in the last day.
Date the selected delivery address was first used.
Indicator for the length of time since this delivery address was first used.
Allowed values:
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
UseThreeDS2RequestData.homePhoneinstead.
Shopper's home phone number (including the country code).
UseThreeDS2RequestData.mobilePhoneinstead.
Shopper's mobile phone number (including the country code).
Date when the shopper last changed their password.
Indicator when the shopper has changed their password.
Allowed values:
- notApplicable
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
Number of all transactions (successful and abandoned) from this shopper in the past 24 hours.
Number of all transactions (successful and abandoned) from this shopper in the past year.
Date this payment method was added to the shopper's account.
Indicator for the length of time since this payment method was added to this shopper's account.
Allowed values:
- notApplicable
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
Number of successful purchases in the last six months.
Whether suspicious activity was recorded on this account.
UseThreeDS2RequestData.workPhoneinstead.
Shopper's work phone number (including the country code).
If you want aBIN or card verificationrequest to use a non-zero value, assign this value toadditionalAmount(while the amount must be still set to 0 to trigger BIN or card verification).
Required to be in the same currency as theamount.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
This field contains additional data, which may be required for a particular payment request.
TheadditionalDataobject consists of entries, each of which includes the key and value.
The amount information for the transaction (inminor units). ForBIN or card verificationrequests, set amount to 0 (zero).
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Information about your application. For more details, seeBuilding Adyen solutions.
Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc.
External platform integrator.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Merchant developed software, such as cashier application, used to interact with the Adyen API.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Merchant device information.
Operating system running on the merchant device.
Version of the operating system on the merchant device.
Merchant device reference.
Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests.
Locale on the shopper interaction device.
Operating system running on the shopper interaction device.
Version of the operating system on the shopper interaction device.
The details of the bank account, from which the payment should be made.
EitherbankAccountorcardfield must be provided in a payment request.
The bank account number (without separators).
The bank city.
The location id of the bank. The field value isnilin most cases.
The name of the bank.
TheBusiness Identifier Code(BIC) is the SWIFT address assigned to a bank. The field value isnilin most cases.
Country code where the bank is located.
A valid value is an ISO two-character country code (e.g. 'NL').
TheInternational Bank Account Number(IBAN).
The name of the bank account holder.
If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For example:
- χ12 is converted to ch12.
- üA is converted to euA.
- Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.
After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one of them must be a valid Latin character (A-Z, a-z). For example:
- John17 - allowed.
- J17 - allowed.
- 171 - not allowed.
- John-7 - allowed.
If provided details don't match the required format, the response returns the error message: 203 'Invalid bank account holder name'.
The bank account holder's tax ID.
The address where to send the invoice.
ThebillingAddressobject is required in the following scenarios. Include all of the fields within this object.
- For 3D Secure 2 transactions in all browser-based and mobile implementations.
- For cross-border payouts to and from Canada.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
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
The delay between the authorisation and scheduled auto-capture, specified in hours.
A container for card data.
EitherbankAccountorcardfield must be provided in a payment request.
Thecard verification code(1-20 characters). Depending on the card brand, it is known also as:
- CVV2/CVC2 – length: 3 digits
- CID – length: 4 digits
If you are usingClient-Side Encryption, the CVC code is present in the encrypted data. You must never post the card details to the server.
This field must be always present in aone-click payment request.
When this value is returned in a response, it is always empty because it is not stored.
The card expiry month.
Format: 2 digits, zero-padded for single digits. For example:
- 03 = March
- 11 = November
The card expiry year.
Format: 4 digits. For example: 2020
The name of the cardholder, as printed on the card.
The issue number of the card (for some UK debit cards only).
The card number (4-19 characters). Do not use any separators.
When this value is returned in a response, only the last 4 digits of the card number are returned.
The month component of the start date (for some UK debit cards only).
The year component of the start date (for some UK debit cards only).
The shopper's date of birth.
FormatISO-8601: YYYY-MM-DD
The forex quote as returned in the response of the forex service.
The account name.
The account type.
The base amount.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The base points.
The buy rate.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The interbank amount.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The reference assigned to the forex quote request.
The sell rate.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The signature to validate the integrity.
The source of the forex quote.
The type of forex.
The date until which the forex quote is valid.
The address where the purchased goods should be delivered.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
The date and time the purchased goods should be delivered.
FormatISO 8601: YYYY-MM-DDThh:mm:ss.sssTZD
Example: 2017-07-17T13:42:40.428+01:00
A string containing the shopper's device fingerprint. For more information, refer toDevice fingerprinting.
The type of the entity the payment is processed for.
An integer value that is added to the normal fraud score. The value can be either positive or negative.
the person or entity receiving the money
Bank Account Number of the recipient
a map of name/value pairs for passing in additional/industry-specific data
The address where to send the invoice.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
Credit card data.
Optional ifshopperReferenceandselectedRecurringDetailReferenceare provided.
Thecard verification code(1-20 characters). Depending on the card brand, it is known also as:
- CVV2/CVC2 – length: 3 digits
- CID – length: 4 digits
If you are usingClient-Side Encryption, the CVC code is present in the encrypted data. You must never post the card details to the server.
This field must be always present in aone-click payment request.
When this value is returned in a response, it is always empty because it is not stored.
The card expiry month.
Format: 2 digits, zero-padded for single digits. For example:
- 03 = March
- 11 = November
The card expiry year.
Format: 4 digits. For example: 2020
The name of the cardholder, as printed on the card.
The issue number of the card (for some UK debit cards only).
The card number (4-19 characters). Do not use any separators.
When this value is returned in a response, only the last 4 digits of the card number are returned.
The month component of the start date (for some UK debit cards only).
The year component of the start date (for some UK debit cards only).
TherecurringDetailReferenceyou want to use for this payment. The valueLATESTcan be used to select the most recently stored recurring detail.
the email address of the person
the name of the person
The first name.
The last name.
Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
Required for Back-to-Back/ purchase driven load in Wallet transactions.
Contains the final merchant who will be receiving the money, also known as subMerchant, information.
The city of the sub-merchant's address.
- Format: Alphanumeric
- Maximum length: 13 characters
The three-letter country code of the sub-merchant's address. For example,BRAfor Brazil.
- Format:ISO 3166-1 alpha-3
- Fixed length: 3 characters
The sub-merchant's 4-digit Merchant Category Code (MCC).
- Format: Numeric
- Fixed length: 4 digits
The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement  that will appear in the card statement.
- Format: Alphanumeric
- Maximum length: 22 characters
The tax ID of the sub-merchant.
- Format: Numeric
- Fixed length: 11 digits for the CPF or 14 digits for the CNPJ
the telephone number of the person
The purpose of a digital wallet transaction.
The person or entity funding the money.
A map of name-value pairs for passing additional or industry-specific data.
The address where to send the invoice.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
Credit card data.
Optional ifshopperReferenceandselectedRecurringDetailReferenceare provided.
Thecard verification code(1-20 characters). Depending on the card brand, it is known also as:
- CVV2/CVC2 – length: 3 digits
- CID – length: 4 digits
If you are usingClient-Side Encryption, the CVC code is present in the encrypted data. You must never post the card details to the server.
This field must be always present in aone-click payment request.
When this value is returned in a response, it is always empty because it is not stored.
The card expiry month.
Format: 2 digits, zero-padded for single digits. For example:
- 03 = March
- 11 = November
The card expiry year.
Format: 4 digits. For example: 2020
The name of the cardholder, as printed on the card.
The issue number of the card (for some UK debit cards only).
The card number (4-19 characters). Do not use any separators.
When this value is returned in a response, only the last 4 digits of the card number are returned.
The month component of the start date (for some UK debit cards only).
The year component of the start date (for some UK debit cards only).
Email address of the person.
Name of the person.
The first name.
The last name.
Phone number of the person
The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value todebit.
Contains installment settings. For more information, refer toInstallments.
Defines the bonus percentage, refund percentage or if the transaction is Buy now Pay later.
Used forcard installments in Mexico
The installment plan, used forcard installments in Japan.
andMexico.
By default, this is set toregular.
Defines the number of installments.
Usually, the maximum allowed number of installments is capped. For example, it may not be possible to split a payment in more than 24 installments. The acquirer sets this upper limit, so its value may vary.
This value can be zero for Installments processed in Mexico.
ThelocalizedShopperStatementfield lets you use dynamic values for your shopper statement in a local character set. If this parameter is left empty, not provided, or not applicable (in case of cross-border transactions), thenshopperStatementis used.
Currently,localizedShopperStatementis only supported for payments with Visa, Mastercard, JCB, Diners, and Discover.
Supported characters: Hiragana, Katakana, Kanji, and alphanumeric.
The mandate details to initiate recurring transaction.
The billing amount (in minor units) of the recurring transactions.
The limitation rule of the billing amount.
Possible values:
- max: The transaction amount can not exceed theamount.
- exact: The transaction amount should be the same as theamount.
The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date.
Possible values:
- on: On a specific date.
- before:  Before and on a specific date.
- after: On and after a specific date.
The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.
Possible values: 1-31 based on thefrequency.
The number of transactions that can be performed within the given frequency.
End date of the billing plan, in YYYY-MM-DD format.
The frequency with which a shopper should be charged.
Possible values:daily,weekly,biWeekly,monthly,quarterly,halfYearly,yearly.
The message shown by UPI to the shopper on the approval screen.
Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date.
Themerchant category code(MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.
The merchant account identifier, with which you want to process the transaction.
This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle.
The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations.
We strongly recommend you send themerchantOrderReferencevalue to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provideretry.orderAttemptNumber,retry.chainAttemptNumber, andretry.skipRetryvalues inPaymentRequest.additionalData.
Additional risk fields for 3D Secure 2.
For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow.
Whether the chosen delivery address is identical to the billing address.
Indicator regarding the delivery address.
Allowed values:
- shipToBillingAddress
- shipToVerifiedAddress
- shipToNewAddress
- shipToStore
- digitalGoods
- goodsNotShipped
- other
UsedeliveryEmailAddressinstead.
The delivery email address (for digital goods).
For Electronic delivery, the email address to which the merchandise was delivered. Maximum length: 254 characters.
The estimated delivery time for the shopper to receive the goods.
Allowed values:
- electronicDelivery
- sameDayShipping
- overnightShipping
- twoOrMoreDaysShipping
For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s).
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased.
For prepaid or gift card purchase,ISO 4217three-digit currency code of the gift card, other than those listed in Table A.5 of the EMVCo 3D Secure Protocol and Core Functions Specification.
For pre-order purchases, the expected date this product will be available to the shopper.
Indicator for whether this transaction is for pre-ordering a product.
Indicates whether Cardholder is placing an order for merchandise with a future availability or release date.
Indicator for whether the shopper has already purchased the same items in the past.
Indicates whether the cardholder is reordering previously purchased merchandise.
Indicates shipping method chosen for the transaction.
Metadata consists of entries, each of which includes a key and a value.
Limits:
- Maximum 20 key-value pairs per request. When exceeding, the "177" error occurs: "Metadata size exceeds limit".
- Maximum 20 characters per key.
- Maximum 80 characters per value.
Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires).
In 3D Secure 2, this is thetransStatusfrom the challenge result. If the transaction was frictionless, omit this parameter.
The cardholder authentication value (base64 encoded, 20 bytes in a decoded form).
The CAVV algorithm used. Include this only for 3D Secure 1.
Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to3D Secure API reference.
In 3D Secure 2, this is thetransStatusfrom theARes.
Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction.
The electronic commerce indicator.
Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations.
The version of the 3D Secure protocol.
Network token authentication verification value (TAVV). The network token cryptogram.
Provides information on why thetransStatusfield has the specified value. For possible values, refer toour docs.
Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form).
The two-character country code of the shopper's nationality.
When you are doing multiple partial (gift card) payments, this is thepspReferenceof the first payment. We use this to link the multiple payments to each other. As your own reference for linking multiple payments, use themerchantOrderReferenceinstead.
Defines how to book chargebacks when usingAdyen for Platforms.
The method of handling the chargeback.
Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.
The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.
The unique identifier of the balance account against which the disputed amount is booked.
Required ifbehaviorisdeductFromOneBalanceAccount.
The recurring settings for the payment. Use this property when you want to enablerecurring payments.
The type of recurring contract to be used.
Possible values:
- ONECLICK– Payment details can be used to initiate a one-click payment, where the shopper enters thecard security code (CVC/CVV).
- RECURRING– Payment details can be used without the card security code to initiatecard-not-present transactions.
- ONECLICK,RECURRING– Payment details can be used regardless of whether the shopper is on your site or not.
- PAYOUT– Payment details can be used tomake a payout.
- EXTERNAL- Use this when you store payment details and send the raw card number or network token directly in your API request.
A descriptive name for this detail.
Date after which no further authorisations shall be performed. Only for 3D Secure 2.
Minimum number of days between authorisations. Only for 3D Secure 2.
The name of the token service.
Defines a recurring payment type. Required when creating a token to store payment details or using stored payment details.
Allowed values:
- Subscription– A transaction for a fixed or variable amount, which follows a fixed schedule.
- CardOnFile– With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.
- UnscheduledCardOnFile– An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount.
The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.
If you need to provide multiple references for a transaction, separate them with hyphens ("-").
Maximum length: 80 characters.
Checkout data for a Secure Remote Commerce payment.
The Secure Remote Commerce checkout payload to process the payment with.
This is the unique identifier generated by SRC system to track and link SRC messages. Available within the present checkout session (e.g. received in an earlier API response during the present session).
Thecard verification code.
A unique identifier that represents the token associated with a card enrolled. Required for scheme 'mc'.
The Secure Remote Commerce scheme.
A unique identifier that represents the token associated with a card enrolled. Required for scheme 'visa'.
Some payment methods require defining a value for this field to specify how to process the transaction.
For the Bancontact payment method, it can be set to:
- maestro(default), to be processed like a Maestro card, or
- bcmc, to be processed like a Bancontact card.
TherecurringDetailReferenceyou want to use for this payment. The valueLATESTcan be used to select the most recently stored recurring detail.
A session ID used to identify a payment session.
The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. > Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include thetelephoneNumber.
The shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks).
Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile integrations, if you did not include theshopperEmail. For native mobile integrations, the field is required to support cases where authentication is routed to the redirect flow. This field is also mandatory for some merchants depending on your business model. For more information,contact Support.
Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.
For the web service API, Adyen assumes Ecommerce shopper interaction by default.
This field has the following possible values:
- Ecommerce- Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.
- ContAuth- Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).
- Moto- Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.
- POS- Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal.
The combination of a language code and a country code to specify the language to be used in the payment.
The shopper's full name.
The first name.
The last name.
Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
The text to be shown on the shopper's bank statement.
We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
Allowed characters:a-z,A-Z,0-9, spaces, and special characters. , ' _ - ? + * /.
The shopper's social security number.
An array of objects specifying how the payment should be split when using either Adyen for Platforms formarketplacesorplatforms, or standaloneIssuing.
The unique identifier of the account to which the split amount is booked. Required iftypeisMarketPlaceorBalanceAccount.
- Classic Platforms integration: TheaccountCodeof the account to which the split amount is booked.
- Balance Platform: ThebalanceAccountIdof the account to which the split amount is booked.

```
accountCode
```

```
balanceAccountId
```
The amount of the split item.
- Required for all split types in theClassic Platforms integration.
- Required iftypeisBalanceAccount,Commission,Surcharge,Default, orVATin yourBalance Platformintegration.
The three-characterISO currency code. By default, this is the original payment currency.
The value of the split amount, inminor units.
Your description for the split item.
Your unique reference for the part of the payment booked to the specifiedaccount.
This is required iftypeisMarketPlace(Classic Platforms integration) orBalanceAccount(Balance Platform).
For the other types, we also recommend providing auniquereference so you can reconcile the split and the associated payment in the transaction overview and in the reports.
The part of the payment you want to book to the specifiedaccount.
Possible values for theBalance Platform:
- BalanceAccount: Books part of the payment (specified inamount) to the specifiedaccount.
- Transaction fees types that you can book to the specifiedaccount:AcquiringFees: The aggregated amount of the interchange and scheme fees.PaymentFee: The aggregated amount of all transaction fees.AdyenFees: The aggregated amount of Adyen's commission and markup fees.AdyenCommission: The transaction fees due to Adyen underblended rates.AdyenMarkup: The transaction fees due to Adyen underInterchange ++ pricing.Interchange: The fees paid to the issuer for each payment made with the card network.SchemeFee: The fees paid to the card scheme for using their network.
- Commission: Your platform's commission on the payment (specified inamount), booked to your liable balance account.
- Remainder: The amount left over after a currency conversion, booked to the specifiedaccount.
- Surcharge: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.
- TopUp: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.
- VAT: The value-added tax charged on the payment, booked to your platforms liable balance account.
- Default: In very specific use cases, allows you to book the specifiedamountto the specifiedaccount. For more information, contact Adyen support.
- AcquiringFees: The aggregated amount of the interchange and scheme fees.
- PaymentFee: The aggregated amount of all transaction fees.
- AdyenFees: The aggregated amount of Adyen's commission and markup fees.
- AdyenCommission: The transaction fees due to Adyen underblended rates.
- AdyenMarkup: The transaction fees due to Adyen underInterchange ++ pricing.
- Interchange: The fees paid to the issuer for each payment made with the card network.
- SchemeFee: The fees paid to the card scheme for using their network.
Possible values for theClassic Platforms integration:Commission,Default,MarketPlace,PaymentFee,VAT.
Required for Adyen for Platforms integrations if you are a platform model. This is yourreference(onbalance platform) or thestoreReference(in theclassic integration) for the ecommerce or point-of-sale store that is processing the payment.
The shopper's telephone number.
The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail.
Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer toOnline paymentsorClassic integrationdocumentation.
Additional information about the cardholder’s account provided by the 3DS Requestor.
Length of time that the cardholder has had the account with the 3DS Requestor.
Allowed values:
- 01— No account
- 02— Created during this transaction
- 03— Less than 30 days
- 04— 30–60 days
- 05— More than 60 days
Date that the cardholder’s account with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added.
Format:YYYYMMDD
Length of time since the cardholder’s account information with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added.
Allowed values:
- 01— Changed during this transaction
- 02— Less than 30 days
- 03— 30–60 days
- 04— More than 60 days
Date that cardholder’s account with the 3DS Requestor had a password change or account reset.
Format:YYYYMMDD
Indicates the length of time since the cardholder’s account with the 3DS Requestor had a password change or account reset.
Allowed values:
- 01— No change
- 02— Changed during this transaction
- 03— Less than 30 days
- 04— 30–60 days
- 05— More than 60 days
Date that the cardholder opened the account with the 3DS Requestor.
Format:YYYYMMDD
Number of purchases with this cardholder account during the previous six months. Max length: 4 characters.
String that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.
Format:YYYYMMDD
Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.
Allowed values:
- 01— No account (guest checkout)
- 02— During this transaction
- 03— Less than 30 days
- 04— 30–60 days
- 05— More than 60 days
Number of Add Card attempts in the last 24 hours. Max length: 3 characters.
String when the shipping address used for this transaction was first used with the 3DS Requestor.
Format:YYYYMMDD
Indicates when the shipping address used for this transaction was first used with the 3DS Requestor.
Allowed values:
- 01— This transaction
- 02— Less than 30 days
- 03— 30–60 days
- 04— More than 60 days
Indicates if the Cardholder Name on the account is identical to the shipping Name used for this transaction.
Allowed values:
- 01— Account Name identical to shipping Name
- 02— Account Name different to shipping Name
Indicates whether the 3DS Requestor has experienced suspicious activity (including previous fraud) on the cardholder account.
Allowed values:
- 01— No suspicious activity has been observed
- 02— Suspicious activity has been observed
Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous 24 hours. Max length: 3 characters.
Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous year. Max length: 3 characters.
Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed values:
- 01— Not applicable
- 02— Credit
- 03— Debit
Required forauthentication-only integration. The acquiring BIN enrolled for 3D Secure 2. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform.
Required forauthentication-only integration. The merchantId that is enrolled for 3D Secure 2 by the merchant's acquirer. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform.
Indicates whether the cardholder shipping address and cardholder billing address are the same. Allowed values:
- Y— Shipping address matches billing address.
- N— Shipping address does not match billing address.
UsethreeDSAuthenticationOnlyinstead.
If set to true, you will only perform the3D Secure 2 authentication, and not the payment authorisation.
UsethreeDSRequestorChallengeIndinstead.
Possibility to specify a preference for receiving a challenge from the issuer.
Allowed values:
- noPreference
- requestNoChallenge
- requestChallenge
- requestChallengeAsMandate
The environment of the shopper.
Allowed values:
- app
- browser
Display options for the 3D Secure 2 SDK.
Optional and only fordeviceChannelapp.
Supported SDK interface types.
Allowed values:
- native
- html
- both
UI types supported for displaying specific challenges.
Allowed values:
- text
- singleSelect
- outOfBand
- otherHtml
- multiSelect
The home phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.
Country code. Length: 1–3 digits.
Subscriber number. Length: 4-15  digits.
Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostlyauthentication-only integrations. Themccis a four-digit code with which the previously givenacquirerMerchantIDis registered at the scheme.
Required forauthentication-only integration. The merchant name that the issuer presents to the shopper if they get a challenge. We recommend to use the same value that you will use in the authorization. Maximum length is 40 characters.
Optional for afull 3D Secure 2 integration. Use this field if you are enrolled for 3D Secure 2 with us and want to override the merchant name already configured on your account.
ThemessageVersionvalue indicating the 3D Secure 2 protocol version.
The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.
Country code. Length: 1–3 digits.
Subscriber number. Length: 4-15  digits.
URL to where the issuer should send theCRes. Required if you are not using components forchannelWebor if you are using classic integrationdeviceChannelbrowser.
Valuetrueindicates that the transaction was de-tokenised prior to being received by the ACS.
Indicates the type of payment for which an authentication is requested (message extension)
Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters.
Date after which no further authorisations shall be performed. Format: YYYYMMDD
Indicates the minimum number of days between authorisations. Maximum length: 4 characters.
ThesdkAppIDvalue as received from the 3D Secure 2 SDK.
Required fordeviceChannelset toapp.
ThesdkEncDatavalue as received from the 3D Secure 2 SDK.
Required fordeviceChannelset toapp.
ThesdkEphemPubKeyvalue as received from the 3D Secure 2 SDK.
Required fordeviceChannelset toapp.
Thecrvvalue as received from the 3D Secure 2 SDK.
Thektyvalue as received from the 3D Secure 2 SDK.
Thexvalue as received from the 3D Secure 2 SDK.
Theyvalue as received from the 3D Secure 2 SDK.
The maximum amount of time in minutes for the 3D Secure 2 authentication process.
Optional and only fordeviceChannelset toapp. Defaults to60minutes.
ThesdkReferenceNumbervalue as received from the 3D Secure 2 SDK.
Only fordeviceChannelset toapp.
ThesdkTransIDvalue as received from the 3D Secure 2 SDK.
Only fordeviceChannelset toapp.
Version of the 3D Secure 2 mobile SDK.
Only fordeviceChannelset toapp.
Completion indicator for the device fingerprinting.
Indicates the type of Authentication request.
Information about how the 3DS Requestor authenticated the cardholder before or during the transaction
Data that documents and supports a specific authentication process. Maximum length: 2048 bytes.
Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values:
- 01— No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest).
- 02— Login to the cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials.
- 03— Login to the cardholder account at the 3DS Requestor system using federated ID.
- 04— Login to the cardholder account at the 3DS Requestor system using issuer credentials.
- 05— Login to the cardholder account at the 3DS Requestor system using third-party authentication.
- 06— Login to the cardholder account at the 3DS Requestor system using FIDO Authenticator.
Date and time in UTC of the cardholder authentication. Format: YYYYMMDDHHMM
Indicates whether a challenge is requested for this transaction. Possible values:
- 01— No preference
- 02— No challenge requested
- 03— Challenge requested (3DS Requestor preference)
- 04— Challenge requested (Mandate)
- 05— No challenge (transactional risk analysis is already performed)
- 06— Data Only
Required forauthentication-only integrationfor Visa. Unique 3D Secure requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2.
Required forauthentication-only integrationfor Visa. Unique 3D Secure requestor name assigned by the Directory Server when you enrol for 3D Secure 2.
Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction.
Data that documents and supports a specific authentication process. Maximum length: 2048 bytes.
Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor. Allowed values:
- 01— Frictionless authentication occurred by ACS.
- 02— Cardholder challenge occurred by ACS.
- 03— AVS verified.
- 04— Other issuer methods.
Date and time in UTC of the prior cardholder authentication. Format: YYYYMMDDHHMM
This data element provides additional information to the ACS to determine the best approach for handing a request. This data element contains an ACS Transaction ID for a prior authenticated transaction. For example, the first recurring transaction that was authenticated with the cardholder. Length: 30 characters.
URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process.
Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values:
- 01— Goods/Service Purchase
- 03— Check Acceptance
- 10— Account Funding
- 11— Quasi-Cash Transaction
- 28— Prepaid Activation and Load
Identify the type of the transaction being authenticated.
ThewhiteListStatusvalue returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2 protocol version 2.2.0.
The work phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.
Country code. Length: 1–3 digits.
Subscriber number. Length: 4-15  digits.
Required to trigger theauthentication-only flow. If set totrue, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default:false.
The reference value to aggregate sales totals in reporting. When not specified, the store field is used (if available).
Set to true if the payment should be routed to a trusted MID.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first: Go toCustomer Area>Developers>Additional data.Select additionalDataResponseAdditionalData3DSecureResponseAdditionalDataBillingAddressResponseAdditionalDataCardResponseAdditionalDataCommonResponseAdditionalDataDomesticErrorResponseAdditionalDataInstallmentsResponseAdditionalDataNetworkTokensResponseAdditionalDataOpiResponseAdditionalDataSepaResponseAdditionalDataSwishauthCodestringAuthorisation code:When the payment is authorised successfully, this field holds the authorisation code for the payment.When the payment is not authorised, this field is empty.dccAmountobjectIncludes the currency of the conversion and the value of the transaction.This value only applies if you have implemented Dynamic Currency Conversion. For more information,contact Support.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.dccSignaturestringCryptographic signature used to verifydccQuote.This value only applies if you have implemented Dynamic Currency Conversion. For more information,contact Support.fraudResultobjectThe fraud result properties of the payment.Show childrenHide childrenaccountScoreintegerThe total fraud score generated by the risk checks.resultsarray[FraudCheckResultWrapper]The result of the individual risk checks.Show childrenHide childrenFraudCheckResultobjectShow childrenHide childrenaccountScoreintegerThe fraud score generated by the risk check.checkIdintegerThe ID of the risk check.namestringThe name of the risk check.issuerUrlstringThe URL to direct the shopper to.In case of SecurePlus, do not redirect a shopper to this URL.mdstringMax length:20000The payment session.paRequeststringThe 3D request data for the issuer.If the value isCUPSecurePlus-CollectSMSVerificationCode, collect an SMS code from the shopper and pass it in the/authorise3Drequest. For more information, see3D Secure.pspReferencestringAdyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.refusalReasonstringIf the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includesresultCodeandrefusalReasonvalues.For more information, seeRefusal reasons.resultCodestringThe result of the payment. For more information, seeResult codes.Possible values:AuthenticationFinished– The payment has been successfully authenticated with 3D Secure 2. Returned for 3D Secure 2 authentication-only transactions.AuthenticationNotRequired– The transaction does not require 3D Secure authentication. Returned forstandalone authentication-only integrations.Authorised– The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.Cancelled– Indicates the payment has been cancelled (either by the shopper or the merchant) before processing was completed. This is a final state.ChallengeShopper– The issuer requires further shopper interaction before the payment can be authenticated. Returned for 3D Secure 2 transactions.Error– There was an error when the payment was being processed. The reason is given in therefusalReasonfield. This is a final state.IdentifyShopper– The issuer requires the shopper's device fingerprint before the payment can be authenticated. Returned for 3D Secure 2 transactions.PartiallyAuthorised– The payment has been authorised for a partial amount.
This happens for card payments when the merchant supports Partial Authorisations and the cardholder has insufficient funds.Pending– Indicates that it is not possible to obtain the final status of the payment. This can happen if the systems providing final status information for the payment are unavailable, or if the shopper needs to take further action to complete the payment.PresentToShopper– Indicates that the response contains additional information that you need to present to a shopper, so that they can use it to complete a payment.Received– Indicates the payment has successfully been received by Adyen, and will be processed. This is the initial state for all payments.RedirectShopper– Indicates the shopper should be redirected to an external web page or app to complete the authorisation.Refused– Indicates the payment was refused. The reason is given in therefusalReasonfield. This is a final state.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- When the payment is authorised successfully, this field holds the authorisation code for the payment.
- When the payment is not authorised, this field is empty.
- AuthenticationFinished– The payment has been successfully authenticated with 3D Secure 2. Returned for 3D Secure 2 authentication-only transactions.
- AuthenticationNotRequired– The transaction does not require 3D Secure authentication. Returned forstandalone authentication-only integrations.
- Authorised– The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.
- Cancelled– Indicates the payment has been cancelled (either by the shopper or the merchant) before processing was completed. This is a final state.
- ChallengeShopper– The issuer requires further shopper interaction before the payment can be authenticated. Returned for 3D Secure 2 transactions.
- Error– There was an error when the payment was being processed. The reason is given in therefusalReasonfield. This is a final state.
- IdentifyShopper– The issuer requires the shopper's device fingerprint before the payment can be authenticated. Returned for 3D Secure 2 transactions.
- PartiallyAuthorised– The payment has been authorised for a partial amount.
This happens for card payments when the merchant supports Partial Authorisations and the cardholder has insufficient funds.
- Pending– Indicates that it is not possible to obtain the final status of the payment. This can happen if the systems providing final status information for the payment are unavailable, or if the shopper needs to take further action to complete the payment.
- PresentToShopper– Indicates that the response contains additional information that you need to present to a shopper, so that they can use it to complete a payment.
- Received– Indicates the payment has successfully been received by Adyen, and will be processed. This is the initial state for all payments.
- RedirectShopper– Indicates the shopper should be redirected to an external web page or app to complete the authorisation.
- Refused– Indicates the payment was refused. The reason is given in therefusalReasonfield. This is a final state.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error