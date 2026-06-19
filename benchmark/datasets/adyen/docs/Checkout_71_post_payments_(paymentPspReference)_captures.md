# Checkout/71/post/payments/(paymentPspReference)/captures

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/payments/(paymentPspReference)/captures*

---

# Capture an authorised payment
Captures an authorised payment and returns a unique reference for this request. You get the outcome of the request asynchronously, in aCAPTUREwebhook.
You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on your account and the payment method supports multiple partial captures.
Automatic captureis the default setting for most payment methods. In these cases, you don't need to make capture requests. However, making capture requests for payments that are captured automatically does not result in double charges.
For more information, refer toCapture.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
ThepspReferenceof the payment that you want to capture.

```
pspReference
```
The amount that you want to capture. Thecurrencymust match the currency used in authorisation, thevaluemust be smaller than or equal to the authorised amount.
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
Enhanced scheme data that may be required for processing the payment. For example, airline information.
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
Price and product information of the refunded items, required forpartial refunds.
This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip.
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
The merchant account that is used to process the payment.
Defines how to book chargebacks when usingAdyen for Platforms.
The method of handling the chargeback.
Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.
The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.
The unique identifier of the balance account against which the disputed amount is booked.
Required ifbehaviorisdeductFromOneBalanceAccount.
Your reference for the capture request. Maximum length: 80 characters.
An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments formarketplacesorplatforms.
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
A List of sub-merchants.
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
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 201 - CreatedThe request has been fulfilled and has resulted in one or more new resources being created.Show moreShow lessamountobjectThe captured amount.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.lineItemsarray[object]Price and product information of the refunded items, required forpartial refunds.This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip.Show childrenHide childrenamountExcludingTaxintegerItem amount excluding the tax, inminor units.amountIncludingTaxintegerItem amount including the tax, inminor units.brandstringBrand of the item.colorstringColor of the item.descriptionstringMax length:10000Description of the line item.idstringID of the line item.imageUrlstringLink to the picture of the purchased item.itemCategorystringItem category, used by the payment methods PayPal and Ratepay.manufacturerstringManufacturer of the item.marketplaceSellerIdstringMarketplace seller id.productUrlstringLink to the purchased item.quantityintegerNumber of items.receiverEmailstringEmail associated with the given product in the basket (usually in electronic gift cards).sizestringSize of the item.skustringStock keeping unit.taxAmountintegerTax amount, inminor units.taxPercentageintegerTax percentage, represented as abasis pointinteger. For example:530for 5.3% (five point three percent)2100for 21% (twenty-one percent)upcstringUniversal Product Code.merchantAccountstringThe merchant account that is used to process the payment.paymentPspReferencestringThepspReferenceof the payment to capture.platformChargebackLogicobjectDefines how to book chargebacks when usingAdyen for Platforms.Show childrenHide childrenbehaviorstringThe method of handling the chargeback.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.costAllocationAccountstringThe unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.targetAccountstringThe unique identifier of the balance account against which the disputed amount is booked.Required ifbehaviorisdeductFromOneBalanceAccount.pspReferencestringAdyen's 16-character reference associated with the capture request.referencestringYour reference for the capture request.splitsarray[object]An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments formarketplacesorplatforms.Show childrenHide childrenaccountstringThe unique identifier of the account to which the split amount is booked. Required iftypeisMarketPlaceorBalanceAccount.Classic Platforms integration: TheaccountCodeof the account to which the split amount is booked.Balance Platform: ThebalanceAccountIdof the account to which the split amount is booked.amountobjectThe amount of the split item.Required for all split types in theClassic Platforms integration.Required iftypeisBalanceAccount,Commission,Surcharge,Default, orVATin yourBalance Platformintegration.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency code. By default, this is the original payment currency.valueintegerThe value of the split amount, inminor units.descriptionstringYour description for the split item.referencestringYour unique reference for the part of the payment booked to the specifiedaccount.This is required iftypeisMarketPlace(Classic Platforms integration) orBalanceAccount(Balance Platform).For the other types, we also recommend providing auniquereference so you can reconcile the split and the associated payment in the transaction overview and in the reports.typestringThe part of the payment you want to book to the specifiedaccount.Possible values for theBalance Platform:BalanceAccount: Books part of the payment (specified inamount) to the specifiedaccount.Transaction fees types that you can book to the specifiedaccount:AcquiringFees: The aggregated amount of the interchange and scheme fees.PaymentFee: The aggregated amount of all transaction fees.AdyenFees: The aggregated amount of Adyen's commission and markup fees.AdyenCommission: The transaction fees due to Adyen underblended rates.AdyenMarkup: The transaction fees due to Adyen underInterchange ++ pricing.Interchange: The fees paid to the issuer for each payment made with the card network.SchemeFee: The fees paid to the card scheme for using their network.Commission: Your platform's commission on the payment (specified inamount), booked to your liable balance account.Remainder: The amount left over after a currency conversion, booked to the specifiedaccount.Surcharge: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.TopUp: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.VAT: The value-added tax charged on the payment, booked to your platforms liable balance account.Default: In very specific use cases, allows you to book the specifiedamountto the specifiedaccount. For more information, contact Adyen support.Possible values for theClassic Platforms integration:Commission,Default,MarketPlace,PaymentFee,VAT.statusstringThe status of your request. This will always have the valuereceived.subMerchantsarray[object]List of sub-merchants.Show childrenHide childrenaddressobjectRequired for transactions performed by registered payment facilitators. The sub-merchant's address.Show childrenHide childrencitystringMax length:3000The name of the city. Maximum length: 3000 characters.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.houseNumberOrNamestringMax length:3000The number or name of the house. Maximum length: 3000 characters.postalCodestringA maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.stateOrProvincestringMax length:1000The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.streetstringMax length:3000The name of the street. Maximum length: 3000 characters.The house number should not be included in this field; it should be separately provided viahouseNumberOrName.amountobjectRequired for transactions performed by registered payment facilitators. The amount of the payment corresponding to each sub-merchant. This value will be different than the request amount if shopper is purchasing items at different sub-merchants' shops.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.emailstringMax length:320Required for transactions performed by registered payment facilitators. The email associated with the sub-merchant's account.idstringRequired for transactions performed by registered payment facilitators. A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant.Format: AlphanumericMaximum length: 15 charactersmccstringRequired for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant Category Code (MCC).Format: NumericFixed length: 4 digitsnamestringRequired for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement that will appear in the card statement.
Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.Format: AlphanumericMaximum length: 22 charactersphoneNumberstringMax length:20Required for transactions performed by registered payment facilitators. The phone number associated with the sub-merchant's account.registeredSincestringtaxIdstringRequired for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.Format: NumericFixed length: 11 digits for the CPF or 14 digits for the CNPJurlstringMax length:320Required for transactions performed by registered payment facilitators. The sub-merchant's URL on the platform, i.e. the sub-merchant's shop.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 201 - Created
- 530for 5.3% (five point three percent)
- 2100for 21% (twenty-one percent)

```
pspReference
```
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
- Format: Alphanumeric
- Maximum length: 15 characters
- Format: Numeric
- Fixed length: 4 digits
- Format: Alphanumeric
- Maximum length: 22 characters
- Format: Numeric
- Fixed length: 11 digits for the CPF or 14 digits for the CNPJ

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error