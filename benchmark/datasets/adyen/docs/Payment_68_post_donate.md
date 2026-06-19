# Payment/68/post/donate

*Source: https://docs.adyen.com/api-explorer/Payment/68/post/donate*

---

# Create a donation
Schedules a new payment to be created (including a new authorisation request) for the specified donation using the payment details of the original payment.
This endpoint is part of ourclassic API integration. If using anewer integration, use the/donationsendpoint under Checkout API instead.
The Adyen account name of the charity.
The merchant account that is used to process the payment.
The amount to be donated.Thecurrencymust match the currency used in authorisation, thevaluemust be smaller than or equal to the authorised amount.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The original pspReference of the payment to modify.
This reference is returned in:
- authorisation response
- authorisation notification
Defines how to book chargebacks when usingAdyen for Platforms.
The method of handling the chargeback.
Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.
The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.
The unique identifier of the balance account against which the disputed amount is booked.
Required ifbehaviorisdeductFromOneBalanceAccount.
Your reference for the payment modification. This reference is visible in Customer Area and in reports.
Maximum length: 80 characters.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalDataobjectThis field contains additional data, which may be returned in a particular modification response.pspReferencestringAdyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.responsestringIndicates if the modification request has been received for processing.
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