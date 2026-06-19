# Payment/68/post/cancelOrRefund

*Source: https://docs.adyen.com/api-explorer/Payment/68/post/cancelOrRefund*

---

# Cancel or refund a payment
Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).
Do not use this endpoint for payments that involve:
- Multiple partial captures.
- Split dataeither at time of payment or capture for Adyen for Platforms.
Instead, check if the payment has been captured and make a corresponding/refundor/cancelcall.
For more information, refer toCancel or refund.
This endpoint is part of ourclassic API integration. If using anewer integration, use the/payments/{paymentPspReference}/reversalsendpoint under Checkout API instead.

```
/payments/{paymentPspReference}/reversals
```
This field contains additional data, which may be required for a particular modification request.
The additionalData object consists of entries, each of which includes the key and value.
The merchant account that is used to process the payment.
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
The original merchant reference to cancel.
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
The transaction reference provided by the PED. For point-of-sale integrations only.
Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only.
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