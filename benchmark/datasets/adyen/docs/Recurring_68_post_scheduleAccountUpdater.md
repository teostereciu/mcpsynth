# Recurring/68/post/scheduleAccountUpdater

*Source: https://docs.adyen.com/api-explorer/Recurring/68/post/scheduleAccountUpdater*

---

# Schedule running the Account Updater
When making the API call, you can submit either the credit card information, or the recurring detail reference and the shopper reference:
- If the card information is provided, all the sub-fields forcardare mandatory.
- If the recurring detail reference is provided, the fields forshopperReferenceandselectedRecurringDetailReferenceare mandatory.
This field contains additional data, which may be required for a particular request.
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
Account of the merchant.
A reference that merchants can apply for the call.
The selected detail recurring reference.
Optional ifcardis provided.
The reference of the shopper that owns the recurring contract.
Optional ifcardis provided.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesspspReferencestringAdyen's 16-character unique reference associated with the transaction. This value is globally unique; quote it when communicating with us about this request.resultstringThe result of scheduling an Account Updater. If scheduling was successful, this field returnsSuccess; otherwise it contains the error message.
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