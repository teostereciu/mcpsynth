# Payout/68/post/storeDetail

*Source: https://docs.adyen.com/api-explorer/Payout/68/post/storeDetail*

---

# Store payout details
This endpoint isdeprecatedand no longer supports new integrations. Do one of the following:
- If you are building a new integration, use theTransfers APIinstead.
- If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
With the Transfers API, you can:
- Handle multiple payout use cases with a single API.
- Use new payout functionalities, such as instant payouts to bank accounts.
- Receive webhooks with more details and defined transfer states.
For more information about the payout features of the Transfers API, see ourPayoutsdocumentation.
Stores payment details under thePAYOUTrecurring contract. These payment details can be used later to submit a payout via the/submitThirdPartycall.
This field contains additional data, which may be required for a particular request.
A container for bank account data.
This field is mandatory ifcardis not provided.
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
The billing address.
ThebillingAddressobject is required for cross-border payouts to and from Canada. Include all of the fields within this object.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
A container for card data.
This field is mandatory ifbankis not provided.
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
The date of birth.
Format:ISO-8601; example: YYYY-MM-DD
For Paysafecard it must be the same as used when registering the Paysafecard account.
This field is mandatory for natural persons.
The type of the entity the payout is processed for.
An integer value that is added to the normal fraud score. The value can be either positive or negative.
The merchant account identifier, with which you want to process the transaction.
The shopper's nationality.
A valid value is an ISO 2-character country code (e.g. 'NL').
A container for the type of recurring contract to be retrieved.
The recurring.contract must be set toPAYOUT
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
The name of the brand to make a payout to.
For Paysafecard it must be set topaysafecard.
The shopper's email address.
The shopper's name.
When theentityTypeisCompany, theshopperName.lastNamemust contain the company name.
The first name.
The last name.
The shopper's reference for the payment transaction.
The shopper's social security number.
The shopper's phone number.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalDataobjectThis field contains additional data, which may be returned in a particular response.pspReferencestringA new reference to uniquely identify this request.recurringDetailReferencestringThe token which you can use later on for submitting the payout.resultCodestringThe result code of the transaction.Successindicates that the details were stored successfully.
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