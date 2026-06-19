# Payout/68/post/payout

*Source: https://docs.adyen.com/api-explorer/Payout/68/post/payout*

---

# Make an instant card payout
This endpoint isdeprecatedand no longer supports new integrations. Do one of the following:
- If you are building a new integration, use the POST/transfersendpoint instead.
- If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
With the Transfers API, you can:
- Handle multiple payout use cases with a single API.
- Use new payout functionalities, such as instant payouts to bank accounts.
- Receive webhooks with more details and defined transfer states.
For more information about the payout features of the Transfers API, see ourPayoutsdocumentation.
With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the cardholder's bank account (this is dependent on whether the issuer supports this functionality). Instant card payouts are only supported for Visa and Mastercard cards.
The amount information for the transaction (inminor units). ForBIN or card verificationrequests, set amount to 0 (zero).
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
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
An integer value that is added to the normal fraud score. The value can be either positive or negative.
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
The merchant account identifier, with which you want to process the transaction.
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
The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.
If you need to provide multiple references for a transaction, separate them with hyphens ("-").
Maximum length: 80 characters.
TherecurringDetailReferenceyou want to use for this payment. The valueLATESTcan be used to select the most recently stored recurring detail.
The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. > Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include thetelephoneNumber.
Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.
For the web service API, Adyen assumes Ecommerce shopper interaction by default.
This field has the following possible values:
- Ecommerce- Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.
- ContAuth- Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).
- Moto- Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.
- POS- Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal.
The shopper's full name.
The first name.
The last name.
Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
The shopper's telephone number.
The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include theshopperEmail.
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