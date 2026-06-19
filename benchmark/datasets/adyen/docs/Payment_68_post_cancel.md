# Payment/68/post/cancel

*Source: https://docs.adyen.com/api-explorer/Payment/68/post/cancel*

---

# Cancel an authorisation
Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel payments after authorisation only for payment methods that support distinct authorisations and captures.
For more information, refer toCancel.
This endpoint is part of ourclassic API integration. If using anewer integration, use the/payments/{paymentPspReference}/cancelsendpoint under Checkout API instead.

```
/payments/{paymentPspReference}/cancels
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
An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to split payments forplatforms.
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