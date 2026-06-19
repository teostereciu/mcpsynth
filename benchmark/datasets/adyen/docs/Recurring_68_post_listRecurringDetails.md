# Recurring/68/post/listRecurringDetails

*Source: https://docs.adyen.com/api-explorer/Recurring/68/post/listRecurringDetails*

---

# Get stored payment details
Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for presentation to the shopper.
For more information, refer toRetrieve stored details.
The merchant account identifier you want to process the (transaction) request with.
A container for the type of a recurring contract to be retrieved.
The contract value needs to match the contract value submitted in the payment transaction used to create a recurring contract.
However, ifONECLICK,RECURRINGis the original contract definition in the initial payment, thencontractshould take eitherONECLICKorRECURRING, depending on whether or not you want the shopper to enter their card's security code when they finalize their purchase.
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
The reference you use to uniquely identify the shopper (e.g. user ID or account ID).
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscreationDatestringThe date when the recurring details were created.detailsarray[RecurringDetailWrapper]Payment details stored for recurring payments.Show childrenHide childrenRecurringDetailobjectShow childrenHide childrenadditionalDataobjectThis field contains additional data, which may be returned in a particular response.The additionalData object consists of entries, each of which includes the key and value.aliasstringThe alias of the credit card number.Applies only to recurring contracts storing credit card detailsaliasTypestringThe alias type of the credit card number.Applies only to recurring contracts storing credit card details.bankobjectA container for bank account data.Show childrenHide childrenbankAccountNumberstringThe bank account number (without separators).bankCitystringThe bank city.bankLocationIdstringThe location id of the bank. The field value isnilin most cases.bankNamestringThe name of the bank.bicstringTheBusiness Identifier Code(BIC) is the SWIFT address assigned to a bank. The field value isnilin most cases.countryCodestringCountry code where the bank is located.A valid value is an ISO two-character country code (e.g. 'NL').ibanstringTheInternational Bank Account Number(IBAN).ownerNamestringThe name of the bank account holder.
If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For example:χ12 is converted to ch12.üA is converted to euA.Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.
After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one of them must be a valid Latin character (A-Z, a-z). For example:John17 - allowed.J17 - allowed.171 - not allowed.John-7 - allowed.If provided details don't match the required format, the response returns the error message: 203 'Invalid bank account holder name'.taxIdstringThe bank account holder's tax ID.billingAddressobjectThe billing address.Show childrenHide childrencitystringMax length:3000The name of the city. Maximum length: 3000 characters.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.houseNumberOrNamestringMax length:3000The number or name of the house. Maximum length: 3000 characters.postalCodestringA maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.stateOrProvincestringThe two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.streetstringMax length:3000The name of the street. Maximum length: 3000 characters.The house number should not be included in this field; it should be separately provided viahouseNumberOrName.cardobjectA container for card data.Show childrenHide childrencvcstringMin length:1Max length:20Thecard verification code(1-20 characters). Depending on the card brand, it is known also as:CVV2/CVC2 – length: 3 digitsCID – length: 4 digitsIf you are usingClient-Side Encryption, the CVC code is present in the encrypted data. You must never post the card details to the server.
This field must be always present in aone-click payment request.
When this value is returned in a response, it is always empty because it is not stored.expiryMonthstringMin length:1Max length:2The card expiry month.
Format: 2 digits, zero-padded for single digits. For example:03 = March11 = NovemberexpiryYearstringMin length:4Max length:4The card expiry year.
Format: 4 digits. For example: 2020holderNamestringMin length:1Max length:50The name of the cardholder, as printed on the card.issueNumberstringMin length:1Max length:2The issue number of the card (for some UK debit cards only).numberstringMin length:4Max length:19The card number (4-19 characters). Do not use any separators.
When this value is returned in a response, only the last 4 digits of the card number are returned.startMonthstringMin length:1Max length:2The month component of the start date (for some UK debit cards only).startYearstringMin length:4Max length:4The year component of the start date (for some UK debit cards only).contractTypesarray[string]Types of recurring contracts.creationDatestringThe date when the recurring details were created.firstPspReferencestringThepspReferenceof the first recurring payment that created the recurring detail.namestringAn optional descriptive name for this recurring detail.networkTxReferencestringReturned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.This contains either the Mastercard Trace ID or the Visa Transaction ID.paymentMethodVariantstringThe  type or sub-brand of a payment method used, e.g. Visa Debit, Visa Corporate, etc. For more information, refer toPaymentMethodVariant.recurringDetailReferencestringThe reference that uniquely identifies the recurring detail.shopperNameobjectThe name of the shopper.Show childrenHide childrenfirstNamestringMax length:80The first name.lastNamestringMax length:80The last name.socialSecurityNumberstringA shopper's social security number (only in countries where it is legal to collect).tokenDetailsobjectShow childrenHide childrentokenDataobjecttokenDataTypestringvariantstringThe payment method, such as “mc", "visa", "ideal", "paypal".lastKnownShopperEmailstringThe most recent email for this shopper (if available).shopperReferencestringThe reference you use to uniquely identify the shopper (e.g. user ID or account ID).
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- χ12 is converted to ch12.
- üA is converted to euA.
- Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.
After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one of them must be a valid Latin character (A-Z, a-z). For example:
- John17 - allowed.
- J17 - allowed.
- 171 - not allowed.
- John-7 - allowed.
- CVV2/CVC2 – length: 3 digits
- CID – length: 4 digits
- 03 = March
- 11 = November

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error