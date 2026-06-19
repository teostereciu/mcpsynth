# Checkout/71/post/payments

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/payments*

---

# Start a transaction
Sends payment parameters (like amount, country, and currency) together with other required input details collected from the shopper. To know more about required parameters for specific payment methods, refer to ourpayment method guides.
The response depends on thepayment flow:
- For a direct flow, the response includes apspReferenceand aresultCodewith the payment result, for exampleAuthorisedorRefused.
- For a redirect or additional action, the response contains anactionobject.
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
Data for 3DS authentication.
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
The details of the bank account, from which the payment should be made.
EitherbankAccountorcardfield must be provided in a payment request.
The type of the bank account.
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
Thedelay between the authorization and automatic captureof the payment, specified in hours.
Maximum value:672(28 days).
The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from thesdkVersionortoken.
Possible values:
- iOS
- Android
- Web
Checkout attempt ID that corresponds to the Id generated by the client SDK for tracking user payment journey.
Information regarding the company.
The company website's home page.
The company name.
Registration number of the company.
Registry location of the company.
Tax ID of the company.
The company type.
UsecheckoutAttemptIdinstead
Conversion ID that corresponds to the Id generated by the client SDK for tracking user payment journey.
The shopper country code.
Format:ISO 3166-1 alpha-2Example: NL or DE
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
The date and time the purchased goods should be delivered.
FormatISO 8601: YYYY-MM-DDThh:mm:ss.sssTZD
Example: 2017-07-17T13:42:40.428+01:00
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
UsedeliverAtinstead.
The date and time the purchased goods should be delivered.
FormatISO 8601: YYYY-MM-DDThh:mm:ss.sssTZD
Example: 2017-07-17T13:42:40.428+01:00
A string containing the shopper's device fingerprint. For more information, refer toDevice fingerprinting.
When true andshopperReferenceis provided, the shopper will be asked if the payment details should be stored for futureone-click payments.
When true andshopperReferenceis provided, the payment details will be tokenized for payouts.
When true andshopperReferenceis provided, the payment details will be stored forrecurring paymentswhere the shopper is not present, such as subscription or automatic top-up payments.
Enhanced scheme datathat may be required for processing the payment and/or interchange savings can apply.
Airline enhanced scheme datathat may be required for processing the transaction and/or for interchange savings.
The reference number for the invoice, issued by the agency.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 6 characters
The two-letter agency plan identifier.
- Encoding: ASCII
- minLength: 2 characters
- maxLength: 2 characters
The amount charged for boarding the plane, inminor units.
- Encoding: Numeric
- minLength: 1 character
- maxLength: 11 characters
TheIATA3-digit accounting code (PAX) that identifies the carrier.
- Format: IATA 3-digit accounting code (PAX)
- Example: KLM = 074
- minLength: 3 characters
- maxLength: 3 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
TheCRSused to make the reservation and purchase the ticket.
- Encoding: ASCII
- minLength: 4 characters
- maxLength: 4 characters
The alphanumeric customer reference number.
- Encoding: ASCII
- maxLength: 20 characters
- If you send more than 20 characters, the customer reference number is truncated
- Must not start with a space or be all spaces.
TheIATA2-letter accounting code (PAX) that identifies the carrier.
- Encoding: ASCII
- Example: KLM = KL
- minLength: 2 characters
- maxLength: 2 characters
- Must not start with a space or be all spaces.
A code that identifies the type of item bought. The description of the code can appear on credit card statements.
- Encoding: ASCII
- Example: Passenger ticket = 01
- minLength: 2 characters
- maxLength: 2 characters
The flight departure date. Time is optional.
- Format for date only:yyyy-MM-dd
- Format for date and time:yyyy-MM-ddTHH:mm
- Use local time of departure airport.
- minLength: 10 characters
- maxLength: 16 characters
TheIATA2-letter accounting code (PAX) that identifies the carrier.
This field is required if the airline data includes leg details.
- Example: KLM = KL
- minLength: 2 characters
- maxLength: 2 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
A one-letter travel class identifier.
The following are common:
- F: first class
- J: business class
- Y: economy class
- W: premium economy
- Encoding: ASCII
- minLength: 1 character
- maxLength: 1 character
- Must not start with a space or be all spaces.
- Must not be all zeros.
Date and time of travel in formatyyyy-MM-ddTHH:mm.
- Use local time of departure airport.
- minLength: 16 characters
- maxLength: 16 characters
TheIATAthree-letter airport code of the departure airport.
This field is required if the airline data includes leg details.
- Encoding: ASCII
- Example: Amsterdam = AMS
- minLength: 3 characters
- maxLength: 3 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The amount ofdeparture taxcharged, inminor units.
- Encoding: Numeric
- minLength: 1
- maxLength: 11
- Must not be all zeros.
TheIATA3-letter airport code of the destination airport.
This field is required if the airline data includes leg details.
- Example: Amsterdam = AMS
- Encoding: ASCII
- minLength: 3 characters
- maxLength: 3 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
Thefare basis code, alphanumeric.
- minLength: 1 character
- maxLength: 15 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The flight identifier.
- minLength: 1 character
- maxLength: 5 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the passenger is entitled to make a stopover, or X if they are not.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 1 character
The passenger's name, initials, and title.
- Format: last name + first name or initials + title
- Example:FLYER / MARY MS
- minLength: 1 character
- maxLength: 20 characters
- If you send more than 20 characters, the name is truncated
- Must not start with a space or be all spaces.
- Must not be all zeros.
The passenger's date of birth.
- Formatyyyy-MM-dd
- minLength: 10
- maxLength: 10
The passenger's first name.
This field is required if the airline data includes passenger details or leg details.
- Encoding: ASCII
The passenger's last name.
This field is required if the airline data includes passenger details or leg details.
- Encoding: ASCII
The passenger's phone number, including country code. This is an alphanumeric field that can include the '+' and '-' signs.
- Encoding: ASCII
- minLength: 3 characters
- maxLength: 30 characters
The IATA passenger type code (PTC).
- Encoding: ASCII
- minLength: 3 characters
- maxLength: 6 characters
The address of the organization that issued the ticket.
- minLength: 0 characters
- maxLength: 16 characters
The date that the ticket was issued to the passenger.
- minLength: 10 characters
- maxLength: 10 characters
- FormatISO 8601: yyyy-MM-dd
The ticket's unique identifier.
- minLength: 1 character
- maxLength: 15 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The unique identifier from IATA or ARC for the travel agency that issues the ticket.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 8 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The name of the travel agency.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 25 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
Level 2 and Level 3 enhanced scheme datathat may be required for processing the transaction and/or for interchange savings.
The reference number to identify the customer and their order.
- Format: ASCII
- Max length: 25 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The destination address information.
The two-letterISO 3166-1 alpha-2or three-letterISO 3166-1 alpha-3 country codefor the destination address.
- Encoding: ASCII
- Min length: 2 characters
- Max length: 3 characters
The postal code of the destination address.
- Encoding: ASCII
- Max length: 10 characters
- Must not start with a space.
- For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
- For Canada, it must be in 6 digits format. For example, M4B 1G5.
The state or province code of the destination address.
- Encoding: ASCII
- Max length: 3 characters
- Must not start with a space.
The duty tax amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The shipping amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The list of item detail lines.
The code that identifies the item in a standardized commodity coding scheme. There are different commodity coding schemes:
- UNSPSC commodity codes
- HS commodity codes
- NAICS commodity codes
- NAPCS commodity codes
- Encoding: ASCII
- Max length: 12 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
A description of the item, that provides details about the purchase.
For Visa transactions with level 3 ESD, the description must not be the same or very similar to your merchant name, or, consist only of common words like "product", or "service".
- Encoding: ASCII
- Max length: 26 characters
- Must not be a single character.
- Must not be blank.
- Must not be all special characters.
- Must not start with a space or be all spaces.
- Must not be all zeros.
The discount amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The product code. Must be a unique product code associated with the item or service. This can be your unique code for the item, or the manufacturer's product code.
- Encoding: ASCII.
- Max length: 12 characters
The number of items. Must be an integer greater than zero.
- Encoding: Numeric
- Max value: 9999
The total amount for the line item, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
SeeAmount requirements for level 2/3 ESDto learn more about how to calculate the line item total.
The unit of measurement for an item.
- Encoding: ASCII
- Max length: 3 characters
The unit price, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The date of the order.
- Min Length: 10 characters
- Max Length: 10 characters
- FormatISO 8601: yyyy-MM-dd
The postal code of the address where the item is shipped from.
- Encoding: ASCII
- Max length: 10 characters
- For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
- For Canada, it must be in 6 digits format. For example, M4B 1G5.
The amount of state or provincialtax included in the total transaction amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
- For L2 data: must not be all zeroes.
- For L3 data: can be zero.
The type of the entity the payment is processed for.
An integer value that is added to the normal fraud score. The value can be either positive or negative.
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
The reason for the amount update. Possible values:
- delayedCharge
- noShow
- installment
Contains installment settings. For more information, refer toInstallments.
Defines the bonus percentage, refund percentage or if the transaction is Buy now Pay later.
Used forcard installments in Mexico
The installment plan, used forcard installments in Japan.
andMexico.
By default, this is set toregular.
Defines the number of installments.
Usually, the maximum allowed number of installments is capped. For example, it may not be possible to split a payment in more than 24 installments. The acquirer sets this upper limit, so its value may vary.
This value can be zero for Installments processed in Mexico.
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
Possible values:adhoc,daily,weekly,biWeekly,monthly,quarterly,halfYearly,yearly.
The message shown by UPI to the shopper on the approval screen.
Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date.
Themerchant category code(MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.
The merchant account identifier, with which you want to process the transaction.
You can use this reference to link multiple transactions to one another (for example, to track order authorization rate).For each billing cycle, this reference should be unique. After the first authorized payment attempt, do not reuse the reference. If you use this parameter, include it in all of the payment requests that you make.
We strongly recommend that you:
- Always include this parameter, so that you can benefit from linking payment requests to one another, in case of authorization retries.
- Additionally include the following parameters in theadditionalDataobject:retry.orderAttemptNumber,retry.chainAttemptNumber, andretry.skipRetry

```
retry.orderAttemptNumber
```

```
retry.chainAttemptNumber
```

```
retry.skipRetry
```
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
The order information required for partial payments.
The encrypted order data.
ThepspReferencethat belongs to the order.
When you are doing multiple partial (gift card) payments, this is thepspReferenceof the first payment. We use this to link the multiple payments to each other. As your own reference for linking multiple payments, use themerchantOrderReferenceinstead.
Required for browser-based (channelWeb) 3D Secure 2 transactions.Set this to the origin URL of the page where you are rendering the Drop-in/Component. Do not include subdirectories and a trailing slash.
The type and required details of a payment method to use.
The object that you can use to enable payment validations for a transaction.
Set torequestedto request aname validationto verify if the cardholder name provided by the shopper matches the cardholder name on file at the issuing bank.
Defines how to book chargebacks when usingAdyen for Platforms.
The method of handling the chargeback.
Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.
The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.
The unique identifier of the balance account against which the disputed amount is booked.
Required ifbehaviorisdeductFromOneBalanceAccount.
Date after which no further authorisations shall be performed. Only for 3D Secure 2.
Minimum number of days between authorisations. Only for 3D Secure 2.
Defines a recurring payment type. Required when creating a token to store payment details or using stored payment details.
Allowed values:
- Subscription– A transaction for a fixed or variable amount, which follows a fixed schedule.
- CardOnFile– With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.
- UnscheduledCardOnFile– An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount.
Specifies the redirect method (GET or POST) when redirecting back from the issuer.
Specifies the redirect method (GET or POST) when redirecting to the issuer.
The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. To provide multiple references for one transaction, separate the reference values with the hyphen (-) character.We strongly recommend that you use a unique value for each transaction.
Maximum length: 80 characters.
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
Contains risk data, such as client-side data, used to identify risk for a transaction.
Contains client-side data, like the device fingerprint, cookies, and specific browser settings.
Any custom fields used as part of the input to configured risk rules.
An integer value that is added to the normal fraud score. The value can be either positive or negative.
The risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile will be applied.
The date and time until when the session remains valid, inISO 8601format.
For example: 2020-07-18T15:42:40.428+01:00
A unique ID that can be used to associate/paymentMethodsand/paymentsrequests with the same shopper transaction, offering insights into conversion rates.
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
Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters.
Your reference must not include personally identifiable information (PII), for example name or email address.
The text to be shown on the shopper's bank statement.
We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
Allowed characters:a-z,A-Z,0-9, spaces, and special characters. , ' _ - ? + * /.
The tax info of the shopper
The two-characterISO 3166-1 alpha-2country code associated with the provided tax identification number.
Currently used only for Indian PA-CB tax verification, when applicable.
The shopper’s tax identification number.
The shopper's social security number.
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
When true andshopperReferenceis provided, the payment details will be stored for futurerecurring payments.
This field contains additional information on the submerchant, who is onboarded to an acquirer through a payment facilitator or aggregator
Required for transactions performed by registered payment facilitators. The sub-merchant's address.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
Required for transactions performed by registered payment facilitators. The amount of the payment corresponding to each sub-merchant. This value will be different than the request amount if shopper is purchasing items at different sub-merchants' shops.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Required for transactions performed by registered payment facilitators. The email associated with the sub-merchant's account.
Required for transactions performed by registered payment facilitators. A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant.
- Format: Alphanumeric
- Maximum length: 15 characters
Required for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant Category Code (MCC).
- Format: Numeric
- Fixed length: 4 digits
Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement that will appear in the card statement.
Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.
- Format: Alphanumeric
- Maximum length: 22 characters
Required for transactions performed by registered payment facilitators. The phone number associated with the sub-merchant's account.
Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.
- Format: Numeric
- Fixed length: 11 digits for the CPF or 14 digits for the CNPJ
Required for transactions performed by registered payment facilitators. The sub-merchant's URL on the platform, i.e. the sub-merchant's shop.
Thesurchargeamount to apply to the transaction, inminor units. When you apply surcharge, include the surcharge in theamount.valuefield.
Review ourSurcharge compliance guideto learn about how to comply with regulatory requirements when applying surcharge.
Thesurchargeamount to apply to the transaction, inminor units. When you apply surcharge, include the surcharge in theamount.valuefield.
Review ourSurcharge compliance guideto learn about how to comply with regulatory requirements when applying surcharge.
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
Indicates whether the cardholder shipping Address and cardholder billing address are the same. Allowed values:
- Y— Shipping Address matches Billing Address.
- N— Shipping Address does not match Billing Address.
- If your version is between 50 and 69, usethreeDSAuthenticationOnlyinstead.
- If your version is 70 or later, useauthenticationData.authenticationOnlyinstead.
If set to true, you will only perform the3D Secure 2 authentication, and not the payment authorisation.
UsethreeDSRequestorChallengeIndinstead.
Possibility to specify a preference for receiving a challenge from the issuer.
Allowed values:
- noPreference
- requestNoChallenge
- requestChallenge
- requestChallengeAsMandate
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
ThesdkEphemPubKeyvalue as received from the 3D Secure 2 SDK.
Thecrvvalue as received from the 3D Secure 2 SDK.
Thektyvalue as received from the 3D Secure 2 SDK.
Thexvalue as received from the 3D Secure 2 SDK.
Theyvalue as received from the 3D Secure 2 SDK.
The maximum amount of time in minutes for the 3D Secure 2 authentication process.
Optional and only fordeviceChannelset toapp. Defaults to60minutes.
ThesdkReferenceNumbervalue as received from the 3D Secure 2 SDK.
ThesdkTransIDvalue as received from the 3D Secure 2 SDK.
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
UseauthenticationData.authenticationOnlyinstead.
Required to trigger theauthentication-only flow. If set totrue, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorisation.Default:false.
Set to true if the payment should be routed to a trusted MID.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessactionAction to be taken for completing the payment.Select actionCheckoutAwaitActionCheckoutBankTransferActionCheckoutDelegatedAuthenticationActionCheckoutNativeRedirectActionCheckoutQrCodeActionCheckoutRedirectActionCheckoutSDKActionCheckoutThreeDS2ActionCheckoutVoucherActionadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first: Go toCustomer Area>Developers>Additional data.Select additionalDataResponseAdditionalData3DSecureResponseAdditionalDataBillingAddressResponseAdditionalDataCardResponseAdditionalDataCommonResponseAdditionalDataDomesticErrorResponseAdditionalDataInstallmentsResponseAdditionalDataNetworkTokensResponseAdditionalDataOpiResponseAdditionalDataSepaResponseAdditionalDataSwishamountobjectAuthorised amount in the transaction.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.donationTokenstringDonation Token containing payment details for Adyen Giving.fraudResultobjectThe fraud result properties of the payment.Show childrenHide childrenaccountScoreintegerThe total fraud score generated by the risk checks.resultsarray[object]The result of the individual risk checks.Show childrenHide childrenaccountScoreintegerThe fraud score generated by the risk check.checkIdintegerThe ID of the risk check.namestringThe name of the risk check.merchantReferencestringThe reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.
If you need to provide multiple references for a transaction, separate them with hyphens ("-").
Maximum length: 80 characters.orderobjectContains updated information regarding the order in case order information was provided in the request.Show childrenHide childrenamountobjectThe initial amount of the order.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.expiresAtstringThe expiry date for the order.orderDatastringThe encrypted order data.pspReferencestringThepspReferencethat belongs to the order.referencestringThe merchant reference for the order.remainingAmountobjectThe updated remaining amount.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.paymentMethodobjectDetails about the payment method used in the transaction.
Only returned ifresultCodeisAuthorised.Show childrenHide childrenbrandstringThe card brand that the shopper used to pay. Only returned ifpaymentMethod.typeisscheme.typestringThepaymentMethod.typevalue used in the request.paymentValidationsobjectThe object that contains the validation outcomes.
Only returned ifresultCodeisAuthorisedand if you have requested a payment validation in the request.Show childrenHide childrennameobjectObject that contains the status and outcomes of thename validation.Show childrenHide childrenrawResponseobjectContains the raw response(s) returned by the scheme for the name validation.Show childrenHide childrenfirstNamestringThe raw first name validation result that Adyen received from the scheme. First name validation result is only returned for Visa.fullNamestringThe raw full name validation result that Adyen received from the scheme. Full name is the only field that is validated for MastercardlastNamestringThe raw last name validation result that Adyen received from the scheme. Last name validation result is only returned for Visa.middleNamestringThe raw middle name validation result that Adyen received from the scheme. Middle name validation result is only returned for Visa.statusstringThe raw name validation status value that Adyen received from the scheme. Only returned for Visa.resultobjectContains the scheme-agnostic match values returned by Adyen.Show childrenHide childrenfirstNamestringInforms you if the first name your shopper provided matches the cardholder first name on file at the issuing bank. The first name is only validated for Visa. Possible values:match,partialMatch,noMatchfullNamestringInforms you if the full name your shopper provided matches the cardholder name on file at the issuing bank. The full name is the only field that is validated for Mastercard. Possible values:match,partialMatch,noMatchlastNamestringInforms you if the last name your shopper provided matches the cardholder last name on file at the issuing bank. The last name is only validated for Visa. Possible values:match,partialMatch,noMatchmiddleNamestringInforms you if the middle name your shopper provided matches the cardholder middle name on file at the issuing bank. The middle name is only validated for Visa. Possible values:match,partialMatch,noMatchstatusstringInforms you if the name validation was performed. Possible values:performed,notPerformed,notSupportedpspReferencestringAdyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.For payment methods that require a redirect or additional action, you will get this value in the/payments/detailsresponse.refusalReasonstringIf the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includesresultCodeandrefusalReasonvalues.For more information, seeRefusal reasons.refusalReasonCodestringCode that specifies the refusal reason. For more information, seeAuthorisation refusal reasons.resultCodestringThe result of the payment. For more information, seeResult codes.Possible values:AuthenticationFinished– The payment has been successfully authenticated with 3D Secure 2. Returned for 3D Secure 2 authentication-only transactions.AuthenticationNotRequired– The transaction does not require 3D Secure authentication. Returned forstandalone authentication-only integrations.Authorised– The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.Cancelled– Indicates the payment has been cancelled (either by the shopper or the merchant) before processing was completed. This is a final state.ChallengeShopper– The issuer requires further shopper interaction before the payment can be authenticated. Returned for 3D Secure 2 transactions.Error– There was an error when the payment was being processed. The reason is given in therefusalReasonfield. This is a final state.IdentifyShopper– The issuer requires the shopper's device fingerprint before the payment can be authenticated. Returned for 3D Secure 2 transactions.PartiallyAuthorised– The payment has been authorised for a partial amount.
This happens for card payments when the merchant supports Partial Authorisations and the cardholder has insufficient funds.Pending– Indicates that it is not possible to obtain the final status of the payment. This can happen if the systems providing final status information for the payment are unavailable, or if the shopper needs to take further action to complete the payment.PresentToShopper– Indicates that the response contains additional information that you need to present to a shopper, so that they can use it to complete a payment.Received– Indicates the payment has successfully been received by Adyen, and will be processed. This is the initial state for all payments.RedirectShopper– Indicates the shopper should be redirected to an external web page or app to complete the authorisation.Refused– Indicates the payment was refused. The reason is given in therefusalReasonfield. This is a final state.threeDS2ResponseDataobjectResponse of the 3D Secure 2 authentication.Show childrenHide childrenacsChallengeMandatedstringacsOperatorIDstringacsReferenceNumberstringacsSignedContentstringacsTransIDstringacsURLstringauthenticationTypestringcardHolderInfostringcavvAlgorithmstringchallengeIndicatorstringdsReferenceNumberstringdsTransIDstringexemptionIndicatorstringmessageVersionstringriskScorestringsdkEphemPubKeystringthreeDSServerTransIDstringtransStatusstringtransStatusReasonstringthreeDS2ResultobjectResult of the 3D Secure 2 authentication.Show childrenHide childrenauthenticationValuestringTheauthenticationValuevalue as defined in the 3D Secure 2 specification.cavvAlgorithmstringThe algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations.challengeCancelstringIndicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to3D Secure API reference.dsTransIDstringThedsTransIDvalue as defined in the 3D Secure 2 specification.ecistringTheecivalue as defined in the 3D Secure 2 specification.exemptionIndicatorstringIndicates the exemption type that was applied by the issuer to the authentication, if exemption applied.
Allowed values:lowValuesecureCorporatetrustedBeneficiarytransactionRiskAnalysismessageVersionstringThemessageVersionvalue as defined in the 3D Secure 2 specification.riskScorestringRisk score calculated by Cartes Bancaires Directory Server (DS).threeDSRequestorChallengeIndstringIndicates whether a challenge is requested for this transaction. Possible values:01— No preference02— No challenge requested03— Challenge requested (3DS Requestor preference)04— Challenge requested (Mandate)05— No challenge (transactional risk analysis is already performed)06— Data OnlythreeDSServerTransIDstringThethreeDSServerTransIDvalue as defined in the 3D Secure 2 specification.timestampstringThetimestampvalue of the 3D Secure 2 authentication.transStatusstringThetransStatusvalue as defined in the 3D Secure 2 specification.transStatusReasonstringProvides information on why thetransStatusfield has the specified value. For possible values, refer toour docs.whiteListStatusstringThewhiteListStatusvalue as defined in the 3D Secure 2 specification.threeDSPaymentDatastringWhen non-empty, contains a value that you must submit to the/payments/detailsendpoint aspaymentData.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
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
- lowValue
- secureCorporate
- trustedBeneficiary
- transactionRiskAnalysis
- 01— No preference
- 02— No challenge requested
- 03— Challenge requested (3DS Requestor preference)
- 04— Challenge requested (Mandate)
- 05— No challenge (transactional risk analysis is already performed)
- 06— Data Only

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error