# Checkout/71/post/sessions

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/sessions*

---

# Create a payment session
Creates a payment session forDrop-in,Components, andHosted Checkoutintegrations.
The response contains encrypted payment session data. The front end then uses the session data to make any required server-side calls for the payment flow.
You get the payment outcome asynchronously, in anAUTHORISATIONwebhook.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
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
List of payment methods to be presented to the shopper. To refer to payment methods, use theirpayment method type.
Example:"allowedPaymentMethods":["ideal","applepay"]
The amount of the payment.
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
Configuration data for 3DS payments.
Indicates when 3D Secure authentication should be attempted. This overrides all other rules, includingDynamic 3D Secure settings.
Possible values:
- always: Perform 3D Secure authentication.
- never: Don't perform 3D Secure authentication. If PSD2 SCA or other national regulations require authentication, the transaction gets declined.
Required to trigger theauthentication-only flow. If set totrue, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.
Default:false.
Object with additional parameters for the 3D Secure authentication flow.
Dimensions of the 3DS2 challenge window to be displayed to the cardholder.
Possible values:
- 01- size of 250x400
- 02- size of 390x400
- 03- size of 500x600
- 04- size of 600x400
- 05- Fullscreen
Required to trigger thedata-only flow. When set totrue, forces the 3D Secure 2 data-only flow for all transactions where it is possible.
Indicates ifnative 3D Secure authenticationshould be triggered when available. Adyen can still select to fallback to the redirect flow to optimize authorization rates and improve the shopper's experience.
Possible values:
- preferred: Use native 3D Secure authentication when available.
- disabled: Use the redirect 3D Secure authentication flow.
The version of 3D Secure to use.
Possible values:
- 2.1.0
- 2.2.0
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
List of payment methods to be hidden from the shopper. To refer to payment methods, use theirpayment method type.
Example:"blockedPaymentMethods":["ideal","applepay"]
The delay between the authorisation and scheduled auto-capture, specified in hours.
The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from thesdkVersionortoken.
Possible values:
- iOS
- Android
- Web
Information regarding the company.
The company website's home page.
The company name.
Registration number of the company.
Registry location of the company.
Tax ID of the company.
The company type.
The shopper's two-letter country code.
The shopper's date of birth.
FormatISO-8601: YYYY-MM-DD
The date and time when the purchased goods should be delivered.
ISO 8601format: YYYY-MM-DDThh:mm:ss+TZD, for example,2020-12-18T10:15:30+01:00.
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
When true andshopperReferenceis provided, the shopper will be asked if the payment details should be stored for futureone-click payments.
When true andshopperReferenceis provided, the payment details will be tokenized for payouts.
When true andshopperReferenceis provided, the payment details will be stored forrecurring paymentswhere the shopper is not present, such as subscription or automatic top-up payments.
The date the session expires inISO8601format. When not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more than 24 hours after session creation.
The person or entity funding the money.
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
The email address of the person funding the money.
The name of the person funding the money.
The first name.
The last name.
The phone number of the person funding the money.
The unique identifier of the wallet where the funds are coming from.
the person or entity receiving the money
The IBAN of the bank account where the funds are being transferred to.
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
The payment method used by the shopper.
The sequence number for the debit. For example, send2if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper.
Secondary brand of the card. For example:plastix,hmclub.
The checkout attempt identifier.
The card verification code. Only collect raw card data if you arefully PCI compliant.
Only include this for JSON Web Encryption (JWE) implementations. The JWE-encrypted card details.
The encrypted card number.
The encrypted card expiry month.
The encrypted card expiry year.
This field contains an encrypted, one-time password or an authentication code provided by the cardholder.
The encrypted card verification code.
The card expiry month. Only collect raw card data if you arefully PCI compliant.
The card expiry year. Only collect raw card data if you arefully PCI compliant.
The encoded fastlane data blob
The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value todebit.
The name of the card holder.
The transaction identifier from card schemes. This is thenetworkTxReferencefrom the response to the first payment.

```
networkTxReference
```
The card number. Only collect raw card data if you arefully PCI compliant.
UsestoredPaymentMethodIdinstead.
This is therecurringDetailReferencereturned in the response when you created the token.
Base64-encoded JSON object containing SDK related parameters required by the SDK
TheshopperNotificationReferencereturned in the response when you requested to notify the shopper. Used only for recurring payments in India.
An identifier used for the Click to Pay transaction.
The SRC reference for the Click to Pay token.
The scheme that is being used for Click to Pay.
The reference for the Click to Pay token.
This is therecurringDetailReferencereturned in the response when you created the token.
Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.
Default payment method details. Common for scheme payment methods, and for simple payment method details.
The email address of the shopper.
The name of the shopper.
The first name.
The last name.
Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
This is therecurringDetailReferencereturned in the response when you created the token.
Required for back-to-back/purchase-driven-load transactions, where the funds are taken from the shopper's stored card when the wallet balance is insufficient.
The final merchant who will receive the money, also known as asub-merchant.
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
The telephone number of the shopper.
The unique identifier for the wallet the funds are being transferred to. You can use the shopper reference or any other identifier.
The tax identifier of the person receiving the funds.
The purpose of a digital wallet transaction.
A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example,cardto specify installment options for all cards, orvisaormc. The value must be an object containing the installment options.
Defines the type of installment plan. If not set, defaults toregular.
Possible values:
- regular
- revolving
- bonus
- with_interest
- buynow_paylater
- nointerest_bonus
- interest_bonus
- refund_prctg
- nointeres_refund_prctg
- interes_refund_prctg
Preselected number of installments offered for this payment method.
An array of the number of installments that the shopper can choose from. For example,[2,3,5]. This cannot be specified simultaneously withmaxValue.
Price and product information about the purchased items, to be included on the invoice sent to the shopper.
This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty.
Item amount excluding the tax, inminor units.
Item amount including the tax, inminor units.
Brand of the item.
Color of the item.
Description of the line item.
ID of the line item.
Link to the picture of the purchased item.
Item category, used by the payment methods PayPal and Ratepay.
Manufacturer of the item.
Marketplace seller id.
Link to the purchased item.
Number of items.
Email associated with the given product in the basket (usually in electronic gift cards).
Size of the item.
Stock keeping unit.
Tax amount, inminor units.
Tax percentage, represented as abasis pointinteger. For example:
- 530for 5.3% (five point three percent)
- 2100for 21% (twenty-one percent)
Universal Product Code.
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
Possible values:adhoc,daily,weekly,biWeekly,monthly,quarterly,halfYearly,yearly.
The message shown by UPI to the shopper on the approval screen.
Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date.
Themerchant category code(MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.
The merchant account identifier, with which you want to process the transaction.
This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle.
The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations.
We strongly recommend you send themerchantOrderReferencevalue to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provideretry.orderAttemptNumber,retry.chainAttemptNumber, andretry.skipRetryvalues inPaymentRequest.additionalData.
Metadata consists of entries, each of which includes a key and a value.
Limits:
- Maximum 20 key-value pairs per request.
- Maximum 20 characters per key.
- Maximum 80 characters per value.
Indicates the type of front end integration. Possible values:
- embedded(default): Drop-in or Components integration
- hosted: Hosted Checkout integration
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
Defines how to book chargebacks when usingAdyen for Platforms.
The method of handling the chargeback.
Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.
The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.
The unique identifier of the balance account against which the disputed amount is booked.
Required ifbehaviorisdeductFromOneBalanceAccount.
Date after which no further authorisations shall be performed. Only for 3D Secure 2.
Minimum number of days between authorisations. Only for 3D Secure 2.
Defines a recurring payment type. Required when creating a token to store payment details.
Allowed values:
- Subscription– A transaction for a fixed or variable amount, which follows a fixed schedule.
- CardOnFile– With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.
- UnscheduledCardOnFile– An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount.
Specifies the redirect method (GET or POST) when redirecting back from the issuer.
Specifies the redirect method (GET or POST) when redirecting to the issuer.
The reference to uniquely identify a payment.
The URL to return to in case of a redirection.
The format depends on the channel.
- For web, include the protocolhttp://orhttps://. You can also include your own additional query parameters, for example, shopper ID or order reference number.
Example:https://your-company.example.com/checkout?shopperOrder=12xy
- For iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to theApple Developer documentation.
Example:my-app://
- For Android, use a custom URL handled by an Activity on your app. You can configure it with anintent filter.
Example:my-app://your.package.name
If the URL to return to includes non-ASCII characters, like spaces or special letters, URL encode the value.
We strongly recommend that you use a maximum of 1024 characters.
The URL must not include personally identifiable information (PII), for example name or email address.
Any risk-related settings to apply to the payment.
Contains client-side data, like the device fingerprint, cookies, and specific browser settings.
Any custom fields used as part of the input to configured risk rules.
An integer value that is added to the normal fraud score. The value can be either positive or negative.
The risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile will be applied.
The shopper's email address.
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
The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program.
The first name.
The last name.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
The text to be shown on the shopper's bank statement.
We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
Allowed characters:a-z,A-Z,0-9, spaces, and special characters. , ' _ - ? + * /.
Set to true to show the payment amount per installment.
Set totrueto show a button that lets the shopper remove a stored payment method.
The shopper's social security number.
Boolean value indicating whether the card payment method should be split into separate debit and credit options.
An array of objects specifying how to split a payment when usingAdyen for Platforms,Classic Platforms integration, orIssuing.
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
Specifies how payment methods should be filtered based on the 'store' parameter:
- 'exclusive': Only payment methods belonging to the specified 'store' are returned.
- 'inclusive': Payment methods from the 'store' and those not associated with any other store are returned.
When true andshopperReferenceis provided, the payment details will be stored for futurerecurring payments.
Indicates if the details of the payment method will be stored for the shopper. Possible values:
- disabled– No details will be stored (default).
- askForConsent– If theshopperReferenceis provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.
- enabled– If theshopperReferenceis provided, the details will be stored without asking the shopper for consent.
The shopper's telephone number.
The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail.
Sets a custom theme forHosted Checkout. The value can be any of theTheme IDvalues from your Customer Area.
Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer toOnline payments.
The home phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.
Country code. Length: 1–3 digits.
Subscriber number. Length: 4-15  digits.
The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.
Country code. Length: 1–3 digits.
Subscriber number. Length: 4-15  digits.
Indicates whether a challenge is requested for this transaction. Possible values:
- 01— No preference
- 02— No challenge requested
- 03— Challenge requested (3DS Requestor preference)
- 04— Challenge requested (Mandate)
- 05— No challenge (transactional risk analysis is already performed)
- 06— Data Only
The work phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.
Country code. Length: 1–3 digits.
Subscriber number. Length: 4-15  digits.
UseauthenticationData.authenticationOnlyinstead.
Required to trigger theauthentication-only flow. If set totrue, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default:false.
Set to true if the payment should be routed to a trusted MID.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 201 - CreatedThe request has been fulfilled and has resulted in one or more new resources being created.Show moreShow lessaccountInfoobjectShopper account information for 3D Secure 2.For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow.Show childrenHide childrenaccountAgeIndicatorstringIndicator for the length of time since this shopper account was created in the merchant's environment.
Allowed values:notApplicablethisTransactionlessThan30Daysfrom30To60DaysmoreThan60DaysaccountChangeDatestringDate when the shopper's account was last changed.accountChangeIndicatorstringIndicator for the length of time since the shopper's account was last updated.
Allowed values:thisTransactionlessThan30Daysfrom30To60DaysmoreThan60DaysaccountCreationDatestringDate when the shopper's account was created.accountTypestringIndicates the type of account. For example, for a multi-account card product.
Allowed values:notApplicablecreditdebitaddCardAttemptsDayintegerNumber of attempts the shopper tried to add a card to their account in the last day.deliveryAddressUsageDatestringDate the selected delivery address was first used.deliveryAddressUsageIndicatorstringIndicator for the length of time since this delivery address was first used.
Allowed values:thisTransactionlessThan30Daysfrom30To60DaysmoreThan60DayshomePhonestringDeprecated in version 68UseThreeDS2RequestData.homePhoneinstead.Shopper's home phone number (including the country code).mobilePhonestringDeprecated in version 68UseThreeDS2RequestData.mobilePhoneinstead.Shopper's mobile phone number (including the country code).passwordChangeDatestringDate when the shopper last changed their password.passwordChangeIndicatorstringIndicator when the shopper has changed their password.
Allowed values:notApplicablethisTransactionlessThan30Daysfrom30To60DaysmoreThan60DayspastTransactionsDayintegerNumber of all transactions (successful and abandoned) from this shopper in the past 24 hours.pastTransactionsYearintegerNumber of all transactions (successful and abandoned) from this shopper in the past year.paymentAccountAgestringDate this payment method was added to the shopper's account.paymentAccountIndicatorstringIndicator for the length of time since this payment method was added to this shopper's account.
Allowed values:notApplicablethisTransactionlessThan30Daysfrom30To60DaysmoreThan60DayspurchasesLast6MonthsintegerNumber of successful purchases in the last six months.suspiciousActivitybooleanWhether suspicious activity was recorded on this account.workPhonestringDeprecated in version 68UseThreeDS2RequestData.workPhoneinstead.Shopper's work phone number (including the country code).additionalAmountobjectIf you want aBIN or card verificationrequest to use a non-zero value, assign this value toadditionalAmount(while the amount must be still set to 0 to trigger BIN or card verification).
Required to be in the same currency as theamount.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.additionalDataobjectThis field contains additional data, which may be required for a particular payment request.TheadditionalDataobject consists of entries, each of which includes the key and value.Select additionalDataAdditionalData3DSecureAdditionalDataAirlineAdditionalDataCarRentalAdditionalDataCommonAdditionalDataLevel23AdditionalDataLodgingAdditionalDataOpenInvoiceAdditionalDataOpiAdditionalDataRatepayAdditionalDataRetryAdditionalDataRiskAdditionalDataRiskStandaloneAdditionalDataSubMerchantAdditionalDataTemporaryServicesAdditionalDataWalletsallowedPaymentMethodsarray[string]List of payment methods to be presented to the shopper. To refer to payment methods, use theirpayment method type.Example:"allowedPaymentMethods":["ideal","applepay"]amountobjectThe amount of the payment.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.applicationInfoobjectInformation about your application. For more details, seeBuilding Adyen solutions.Show childrenHide childrenadyenLibraryobjectAdyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc.Show childrenHide childrennamestringName of the field. For example, Name of External Platform.versionstringVersion of the field. For example, Version of External Platform.adyenPaymentSourceobjectAdyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc.Show childrenHide childrennamestringName of the field. For example, Name of External Platform.versionstringVersion of the field. For example, Version of External Platform.externalPlatformobjectThird-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc.Show childrenHide childrenintegratorstringExternal platform integrator.namestringName of the field. For example, Name of External Platform.versionstringVersion of the field. For example, Version of External Platform.merchantApplicationobjectMerchant developed software, such as cashier application, used to interact with the Adyen API.Show childrenHide childrennamestringName of the field. For example, Name of External Platform.versionstringVersion of the field. For example, Version of External Platform.merchantDeviceobjectMerchant device information.Show childrenHide childrenosstringOperating system running on the merchant device.osVersionstringVersion of the operating system on the merchant device.referencestringMerchant device reference.shopperInteractionDeviceobjectShopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests.Show childrenHide childrenlocalestringLocale on the shopper interaction device.osstringOperating system running on the shopper interaction device.osVersionstringVersion of the operating system on the shopper interaction device.authenticationDataobjectConfiguration data for 3DS payments.Show childrenHide childrenattemptAuthenticationstringIndicates when 3D Secure authentication should be attempted. This overrides all other rules, includingDynamic 3D Secure settings.Possible values:always: Perform 3D Secure authentication.never: Don't perform 3D Secure authentication. If PSD2 SCA or other national regulations require authentication, the transaction gets declined.authenticationOnlybooleanRequired to trigger theauthentication-only flow. If set totrue, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.
Default:false.threeDSRequestDataobjectObject with additional parameters for the 3D Secure authentication flow.Show childrenHide childrenchallengeWindowSizestringDimensions of the 3DS2 challenge window to be displayed to the cardholder.Possible values:01- size of 250x40002- size of 390x40003- size of 500x60004- size of 600x40005- FullscreendataOnlystringRequired to trigger thedata-only flow. When set totrue, forces the 3D Secure 2 data-only flow for all transactions where it is possible.nativeThreeDSstringIndicates ifnative 3D Secure authenticationshould be triggered when available. Adyen can still select to fallback to the redirect flow to optimize authorization rates and improve the shopper's experience.Possible values:preferred: Use native 3D Secure authentication when available.disabled: Use the redirect 3D Secure authentication flow.threeDSVersionstringThe version of 3D Secure to use.Possible values:2.1.02.2.0billingAddressobjectThe address where to send the invoice.Show childrenHide childrencitystringMax length:3000The name of the city. Maximum length: 3000 characters.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.houseNumberOrNamestringMax length:3000The number or name of the house. Maximum length: 3000 characters.postalCodestringA maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.stateOrProvincestringMax length:1000The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.streetstringMax length:3000The name of the street. Maximum length: 3000 characters.The house number should not be included in this field; it should be separately provided viahouseNumberOrName.blockedPaymentMethodsarray[string]List of payment methods to be hidden from the shopper. To refer to payment methods, use theirpayment method type.Example:"blockedPaymentMethods":["ideal","applepay"]captureDelayHoursintegerThe delay between the authorisation and scheduled auto-capture, specified in hours.channelstringThe platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from thesdkVersionortoken.Possible values:iOSAndroidWebcompanyobjectInformation regarding the company.Show childrenHide childrenhomepagestringThe company website's home page.namestringThe company name.registrationNumberstringRegistration number of the company.registryLocationstringRegistry location of the company.taxIdstringTax ID of the company.typestringThe company type.countryCodestringThe shopper's two-letter country code.dateOfBirthstringThe shopper's date of birth inISO8601format.deliverAtstringThe date and time when the purchased goods should be delivered.ISO 8601format: YYYY-MM-DDThh:mm:ss+TZD, for example,2020-12-18T10:15:30+01:00.deliveryAddressobjectThe address where the purchased goods should be delivered.Show childrenHide childrencitystringMax length:3000The name of the city. Maximum length: 3000 characters.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.firstNamestringhouseNumberOrNamestringMax length:3000The number or name of the house. Maximum length: 3000 characters.lastNamestringpostalCodestringA maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.stateOrProvincestringMax length:1000The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.streetstringMax length:3000The name of the street. Maximum length: 3000 characters.The house number should not be included in this field; it should be separately provided viahouseNumberOrName.enableOneClickbooleanWhen true andshopperReferenceis provided, the shopper will be asked if the payment details should be stored for futureone-click payments.enablePayOutbooleanWhen true andshopperReferenceis provided, the payment details will be tokenized for payouts.enableRecurringbooleanWhen true andshopperReferenceis provided, the payment details will be stored forrecurring paymentswhere the shopper is not present, such as subscription or automatic top-up payments.expiresAtstringThe date the session expires inISO8601format. When not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more than 24 hours after session creation.fundOriginobjectThe person or entity funding the money.Show childrenHide childrenbillingAddressobjectThe address where to send the invoice.Show childrenHide childrencitystringMax length:3000The name of the city. Maximum length: 3000 characters.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.houseNumberOrNamestringMax length:3000The number or name of the house. Maximum length: 3000 characters.postalCodestringA maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.stateOrProvincestringThe two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.streetstringMax length:3000The name of the street. Maximum length: 3000 characters.The house number should not be included in this field; it should be separately provided viahouseNumberOrName.shopperEmailstringThe email address of the person funding the money.shopperNameobjectThe name of the person funding the money.Show childrenHide childrenfirstNamestringMax length:80The first name.lastNamestringMax length:80The last name.telephoneNumberstringThe phone number of the person funding the money.walletIdentifierstringThe unique identifier of the wallet where the funds are coming from.fundRecipientobjectthe person or entity receiving the moneyShow childrenHide childrenIBANstringThe IBAN of the bank account where the funds are being transferred to.billingAddressobjectThe address where to send the invoice.Show childrenHide childrencitystringMax length:3000The name of the city. Maximum length: 3000 characters.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.houseNumberOrNamestringMax length:3000The number or name of the house. Maximum length: 3000 characters.postalCodestringA maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.stateOrProvincestringThe two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.streetstringMax length:3000The name of the street. Maximum length: 3000 characters.The house number should not be included in this field; it should be separately provided viahouseNumberOrName.paymentMethodobjectThe payment method used by the shopper.Show childrenHide childrenbillingSequenceNumberstringThe sequence number for the debit. For example, send2if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper.brandstringSecondary brand of the card. For example:plastix,hmclub.checkoutAttemptIdstringThe checkout attempt identifier.cupsecureplus.smscodestringDeprecatedcvcstringThe card verification code. Only collect raw card data if you arefully PCI compliant.encryptedCardstringMax length:40000Only include this for JSON Web Encryption (JWE) implementations. The JWE-encrypted card details.encryptedCardNumberstringMax length:15000The encrypted card number.encryptedExpiryMonthstringMax length:15000The encrypted card expiry month.encryptedExpiryYearstringMax length:15000The encrypted card expiry year.encryptedPasswordstringMax length:15000This field contains an encrypted, one-time password or an authentication code provided by the cardholder.encryptedSecurityCodestringMax length:15000The encrypted card verification code.expiryMonthstringThe card expiry month. Only collect raw card data if you arefully PCI compliant.expiryYearstringThe card expiry year. Only collect raw card data if you arefully PCI compliant.fastlaneDatastringThe encoded fastlane data blobfundingSourcestringThe funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value todebit.holderNamestringMax length:15000The name of the card holder.networkPaymentReferencestringThe transaction identifier from card schemes. This is thenetworkTxReferencefrom the response to the first payment.numberstringThe card number. Only collect raw card data if you arefully PCI compliant.recurringDetailReferencestringDeprecated in version 49UsestoredPaymentMethodIdinstead.This is therecurringDetailReferencereturned in the response when you created the token.sdkDatastringMax length:50000Base64-encoded JSON object containing SDK related parameters required by the SDKshopperNotificationReferencestringTheshopperNotificationReferencereturned in the response when you requested to notify the shopper. Used only for recurring payments in India.srcCorrelationIdstringAn identifier used for the Click to Pay transaction.srcDigitalCardIdstringThe SRC reference for the Click to Pay token.srcSchemestringThe scheme that is being used for Click to Pay.srcTokenReferencestringThe reference for the Click to Pay token.storedPaymentMethodIdstringMax length:64This is therecurringDetailReferencereturned in the response when you created the token.threeDS2SdkVersionstringMax length:12Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.typestringDefault payment method details. Common for scheme payment methods, and for simple payment method details.shopperEmailstringThe email address of the shopper.shopperNameobjectThe name of the shopper.Show childrenHide childrenfirstNamestringMax length:80The first name.lastNamestringMax length:80The last name.shopperReferencestringMin length:3Max length:256Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.Your reference must not include personally identifiable information (PII) such as name or email address.storedPaymentMethodIdstringMax length:64This is therecurringDetailReferencereturned in the response when you created the token.subMerchantobjectRequired for back-to-back/purchase-driven-load transactions, where the funds are taken from the shopper's stored card when the wallet balance is insufficient.
The final merchant who will receive the money, also known as asub-merchant.Show childrenHide childrencitystringThe city of the sub-merchant's address.Format: AlphanumericMaximum length: 13 characterscountrystringThe three-letter country code of the sub-merchant's address. For example,BRAfor Brazil.Format:ISO 3166-1 alpha-3Fixed length: 3 charactersmccstringThe sub-merchant's 4-digit Merchant Category Code (MCC).Format: NumericFixed length: 4 digitsnamestringThe name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement  that will appear in the card statement.Format: AlphanumericMaximum length: 22 characterstaxIdstringThe tax ID of the sub-merchant.Format: NumericFixed length: 11 digits for the CPF or 14 digits for the CNPJtelephoneNumberstringThe telephone number of the shopper.walletIdentifierstringThe unique identifier for the wallet the funds are being transferred to. You can use the shopper reference or any other identifier.walletOwnerTaxIdstringThe tax identifier of the person receiving the funds.walletPurposestringThe purpose of a digital wallet transaction.idstringA unique identifier of the session.installmentOptionsobjectA set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example,cardto specify installment options for all cards, orvisaormc. The value must be an object containing the installment options.Show childrenHide childrenplansarray[string]Defines the type of installment plan. If not set, defaults toregular.Possible values:regularrevolvingbonuswith_interestbuynow_paylaternointerest_bonusinterest_bonusrefund_prctgnointeres_refund_prctginteres_refund_prctgpreselectedValueintegerPreselected number of installments offered for this payment method.valuesarray[integer]An array of the number of installments that the shopper can choose from. For example,[2,3,5]. This cannot be specified simultaneously withmaxValue.lineItemsarray[object]Price and product information about the purchased items, to be included on the invoice sent to the shopper.This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty.Show childrenHide childrenamountExcludingTaxintegerItem amount excluding the tax, inminor units.amountIncludingTaxintegerItem amount including the tax, inminor units.brandstringBrand of the item.colorstringColor of the item.descriptionstringMax length:10000Description of the line item.idstringID of the line item.imageUrlstringLink to the picture of the purchased item.itemCategorystringItem category, used by the payment methods PayPal and Ratepay.manufacturerstringManufacturer of the item.marketplaceSellerIdstringMarketplace seller id.productUrlstringLink to the purchased item.quantityintegerNumber of items.receiverEmailstringEmail associated with the given product in the basket (usually in electronic gift cards).sizestringSize of the item.skustringStock keeping unit.taxAmountintegerTax amount, inminor units.taxPercentageintegerTax percentage, represented as abasis pointinteger. For example:530for 5.3% (five point three percent)2100for 21% (twenty-one percent)upcstringUniversal Product Code.mandateobjectThe mandate details to initiate recurring transaction.Show childrenHide childrenamountstringThe billing amount (in minor units) of the recurring transactions.amountRulestringThe limitation rule of the billing amount.Possible values:max: The transaction amount can not exceed theamount.exact: The transaction amount should be the same as theamount.billingAttemptsRulestringThe rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date.Possible values:on: On a specific date.before:  Before and on a specific date.after: On and after a specific date.billingDaystringThe number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.Possible values: 1-31 based on thefrequency.countstringThe number of transactions that can be performed within the given frequency.endsAtstringEnd date of the billing plan, in YYYY-MM-DD format.frequencystringThe frequency with which a shopper should be charged.Possible values:adhoc,daily,weekly,biWeekly,monthly,quarterly,halfYearly,yearly.remarksstringThe message shown by UPI to the shopper on the approval screen.startsAtstringStart date of the billing plan, in YYYY-MM-DD format. By default, the transaction date.mccstringThemerchant category code(MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.merchantAccountstringThe merchant account identifier, with which you want to process the transaction.merchantOrderReferencestringThis reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle.
The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations.We strongly recommend you send themerchantOrderReferencevalue to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provideretry.orderAttemptNumber,retry.chainAttemptNumber, andretry.skipRetryvalues inPaymentRequest.additionalData.metadataobjectMetadata consists of entries, each of which includes a key and a value.
Limits:Maximum 20 key-value pairs per request.Maximum 20 characters per key.Maximum 80 characters per value.modestringIndicates the type of front end integration. Possible values:embedded(default): Drop-in or Components integrationhosted: Hosted Checkout integrationmpiDataobjectAuthentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires).Show childrenHide childrenauthenticationResponsestringIn 3D Secure 2, this is thetransStatusfrom the challenge result. If the transaction was frictionless, omit this parameter.cavvstringThe cardholder authentication value (base64 encoded, 20 bytes in a decoded form).cavvAlgorithmstringThe CAVV algorithm used. Include this only for 3D Secure 1.challengeCancelstringIndicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to3D Secure API reference.directoryResponsestringIn 3D Secure 2, this is thetransStatusfrom theARes.dsTransIDstringSupported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction.ecistringThe electronic commerce indicator.riskScorestringRisk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations.threeDSVersionstringThe version of the 3D Secure protocol.tokenAuthenticationVerificationValuestringNetwork token authentication verification value (TAVV). The network token cryptogram.transStatusReasonstringProvides information on why thetransStatusfield has the specified value. For possible values, refer toour docs.xidstringSupported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form).platformChargebackLogicobjectDefines how to book chargebacks when usingAdyen for Platforms.Show childrenHide childrenbehaviorstringThe method of handling the chargeback.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.costAllocationAccountstringThe unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.targetAccountstringThe unique identifier of the balance account against which the disputed amount is booked.Required ifbehaviorisdeductFromOneBalanceAccount.recurringExpirystringDate after which no further authorisations shall be performed. Only for 3D Secure 2.recurringFrequencystringMinimum number of days between authorisations. Only for 3D Secure 2.recurringProcessingModelstringDefines a recurring payment type. Required when creating a token to store payment details.
Allowed values:Subscription– A transaction for a fixed or variable amount, which follows a fixed schedule.CardOnFile– With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.UnscheduledCardOnFile– An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount.redirectFromIssuerMethodstringSpecifies the redirect method (GET or POST) when redirecting back from the issuer.redirectToIssuerMethodstringSpecifies the redirect method (GET or POST) when redirecting to the issuer.referencestringThe reference to uniquely identify a payment.returnUrlstringMax length:8000The URL to return to in case of a redirection.
The format depends on the channel.For web, include the protocolhttp://orhttps://. You can also include your own additional query parameters, for example, shopper ID or order reference number.
Example:https://your-company.example.com/checkout?shopperOrder=12xyFor iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to theApple Developer documentation.
Example:my-app://For Android, use a custom URL handled by an Activity on your app. You can configure it with anintent filter.
Example:my-app://your.package.nameIf the URL to return to includes non-ASCII characters, like spaces or special letters, URL encode the value.We strongly recommend that you use a maximum of 1024 characters.The URL must not include personally identifiable information (PII), for example name or email address.riskDataobjectAny risk-related settings to apply to the payment.Show childrenHide childrenclientDatastringMax length:5000Contains client-side data, like the device fingerprint, cookies, and specific browser settings.customFieldsobjectAny custom fields used as part of the input to configured risk rules.fraudOffsetintegerAn integer value that is added to the normal fraud score. The value can be either positive or negative.profileReferencestringThe risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile will be applied.sessionDatastringThe payment session data you need to pass to your front end.shopperEmailstringThe shopper's email address.shopperIPstringThe shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks).Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile integrations, if you did not include theshopperEmail. For native mobile integrations, the field is required to support cases where authentication is routed to the redirect flow. This field is also mandatory for some merchants depending on your business model. For more information,contact Support.shopperInteractionstringSpecifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.
For the web service API, Adyen assumes Ecommerce shopper interaction by default.This field has the following possible values:Ecommerce- Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.ContAuth- Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).Moto- Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.POS- Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal.shopperLocalestringThe combination of a language code and a country code to specify the language to be used in the payment.shopperNameobjectThe shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program.Show childrenHide childrenfirstNamestringMax length:80The first name.lastNamestringMax length:80The last name.shopperReferencestringMin length:3Max length:256Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.Your reference must not include personally identifiable information (PII) such as name or email address.shopperStatementstringThe text to be shown on the shopper's bank statement.
We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
Allowed characters:a-z,A-Z,0-9, spaces, and special characters. , ' _ - ? + * /.showInstallmentAmountbooleanSet to true to show the payment amount per installment.showRemovePaymentMethodButtonbooleanSet totrueto show a button that lets the shopper remove a stored payment method.socialSecurityNumberstringThe shopper's social security number.splitCardFundingSourcesbooleanBoolean value indicating whether the card payment method should be split into separate debit and credit options.splitsarray[object]An array of objects specifying how to split a payment when usingAdyen for Platforms,Classic Platforms integration, orIssuing.Show childrenHide childrenaccountstringThe unique identifier of the account to which the split amount is booked. Required iftypeisMarketPlaceorBalanceAccount.Classic Platforms integration: TheaccountCodeof the account to which the split amount is booked.Balance Platform: ThebalanceAccountIdof the account to which the split amount is booked.amountobjectThe amount of the split item.Required for all split types in theClassic Platforms integration.Required iftypeisBalanceAccount,Commission,Surcharge,Default, orVATin yourBalance Platformintegration.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency code. By default, this is the original payment currency.valueintegerThe value of the split amount, inminor units.descriptionstringYour description for the split item.referencestringYour unique reference for the part of the payment booked to the specifiedaccount.This is required iftypeisMarketPlace(Classic Platforms integration) orBalanceAccount(Balance Platform).For the other types, we also recommend providing auniquereference so you can reconcile the split and the associated payment in the transaction overview and in the reports.typestringThe part of the payment you want to book to the specifiedaccount.Possible values for theBalance Platform:BalanceAccount: Books part of the payment (specified inamount) to the specifiedaccount.Transaction fees types that you can book to the specifiedaccount:AcquiringFees: The aggregated amount of the interchange and scheme fees.PaymentFee: The aggregated amount of all transaction fees.AdyenFees: The aggregated amount of Adyen's commission and markup fees.AdyenCommission: The transaction fees due to Adyen underblended rates.AdyenMarkup: The transaction fees due to Adyen underInterchange ++ pricing.Interchange: The fees paid to the issuer for each payment made with the card network.SchemeFee: The fees paid to the card scheme for using their network.Commission: Your platform's commission on the payment (specified inamount), booked to your liable balance account.Remainder: The amount left over after a currency conversion, booked to the specifiedaccount.Surcharge: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.TopUp: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.VAT: The value-added tax charged on the payment, booked to your platforms liable balance account.Default: In very specific use cases, allows you to book the specifiedamountto the specifiedaccount. For more information, contact Adyen support.Possible values for theClassic Platforms integration:Commission,Default,MarketPlace,PaymentFee,VAT.storestringRequired for Adyen for Platforms integrations if you are a platform model. This is yourreference(onbalance platform) or thestoreReference(in theclassic integration) for the ecommerce or point-of-sale store that is processing the payment.storeFiltrationModestringSpecifies how payment methods should be filtered based on the 'store' parameter:'exclusive': Only payment methods belonging to the specified 'store' are returned.'inclusive': Payment methods from the 'store' and those not associated with any other store are returned.storePaymentMethodbooleanWhen true andshopperReferenceis provided, the payment details will be stored for futurerecurring payments.storePaymentMethodModestringIndicates if the details of the payment method will be stored for the shopper. Possible values:disabled– No details will be stored (default).askForConsent– If theshopperReferenceis provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.enabled– If theshopperReferenceis provided, the details will be stored without asking the shopper for consent.telephoneNumberstringThe shopper's telephone number.
The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail.themeIdstringSets a custom theme forHosted Checkout. The value can be any of theTheme IDvalues from your Customer Area.threeDS2RequestDataobjectRequest fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer toOnline payments.Show childrenHide childrenhomePhoneobjectThe home phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.Show childrenHide childrenccstringMin length:1Max length:3Country code. Length: 1–3 digits.subscriberstringMax length:15Subscriber number. Length: 4-15  digits.mobilePhoneobjectThe mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.Show childrenHide childrenccstringMin length:1Max length:3Country code. Length: 1–3 digits.subscriberstringMax length:15Subscriber number. Length: 4-15  digits.threeDSRequestorChallengeIndstringIndicates whether a challenge is requested for this transaction. Possible values:01— No preference02— No challenge requested03— Challenge requested (3DS Requestor preference)04— Challenge requested (Mandate)05— No challenge (transactional risk analysis is already performed)06— Data OnlyworkPhoneobjectThe work phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail, and did not send the shopper's phone number intelephoneNumber.Show childrenHide childrenccstringMin length:1Max length:3Country code. Length: 1–3 digits.subscriberstringMax length:15Subscriber number. Length: 4-15  digits.threeDSAuthenticationOnlybooleanDeprecated in version 69UseauthenticationData.authenticationOnlyinstead.Required to trigger theauthentication-only flow. If set totrue, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default:false.trustedShopperbooleanSet to true if the payment should be routed to a trusted MID.urlstringThe URL for the Hosted Checkout page. Redirect the shopper to this URL so they can make the payment.

#### 201 - Created
- notApplicable
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
- notApplicable
- credit
- debit
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
- notApplicable
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
- notApplicable
- thisTransaction
- lessThan30Days
- from30To60Days
- moreThan60Days
- always: Perform 3D Secure authentication.
- never: Don't perform 3D Secure authentication. If PSD2 SCA or other national regulations require authentication, the transaction gets declined.
- 01- size of 250x400
- 02- size of 390x400
- 03- size of 500x600
- 04- size of 600x400
- 05- Fullscreen
- preferred: Use native 3D Secure authentication when available.
- disabled: Use the redirect 3D Secure authentication flow.
- 2.1.0
- 2.2.0
- iOS
- Android
- Web

```
networkTxReference
```
- Format: Alphanumeric
- Maximum length: 13 characters
- Format:ISO 3166-1 alpha-3
- Fixed length: 3 characters
- Format: Numeric
- Fixed length: 4 digits
- Format: Alphanumeric
- Maximum length: 22 characters
- Format: Numeric
- Fixed length: 11 digits for the CPF or 14 digits for the CNPJ
- regular
- revolving
- bonus
- with_interest
- buynow_paylater
- nointerest_bonus
- interest_bonus
- refund_prctg
- nointeres_refund_prctg
- interes_refund_prctg
- 530for 5.3% (five point three percent)
- 2100for 21% (twenty-one percent)
- max: The transaction amount can not exceed theamount.
- exact: The transaction amount should be the same as theamount.
- on: On a specific date.
- before:  Before and on a specific date.
- after: On and after a specific date.
- Maximum 20 key-value pairs per request.
- Maximum 20 characters per key.
- Maximum 80 characters per value.
- embedded(default): Drop-in or Components integration
- hosted: Hosted Checkout integration
- Subscription– A transaction for a fixed or variable amount, which follows a fixed schedule.
- CardOnFile– With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.
- UnscheduledCardOnFile– An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount.
- For web, include the protocolhttp://orhttps://. You can also include your own additional query parameters, for example, shopper ID or order reference number.
Example:https://your-company.example.com/checkout?shopperOrder=12xy
- For iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to theApple Developer documentation.
Example:my-app://
- For Android, use a custom URL handled by an Activity on your app. You can configure it with anintent filter.
Example:my-app://your.package.name
- Ecommerce- Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.
- ContAuth- Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).
- Moto- Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.
- POS- Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal.
- Classic Platforms integration: TheaccountCodeof the account to which the split amount is booked.
- Balance Platform: ThebalanceAccountIdof the account to which the split amount is booked.

```
accountCode
```

```
balanceAccountId
```
- Required for all split types in theClassic Platforms integration.
- Required iftypeisBalanceAccount,Commission,Surcharge,Default, orVATin yourBalance Platformintegration.
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
- 'exclusive': Only payment methods belonging to the specified 'store' are returned.
- 'inclusive': Payment methods from the 'store' and those not associated with any other store are returned.
- disabled– No details will be stored (default).
- askForConsent– If theshopperReferenceis provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.
- enabled– If theshopperReferenceis provided, the details will be stored without asking the shopper for consent.
- 01— No preference
- 02— No challenge requested
- 03— Challenge requested (3DS Requestor preference)
- 04— Challenge requested (Mandate)
- 05— No challenge (transactional risk analysis is already performed)
- 06— Data Only