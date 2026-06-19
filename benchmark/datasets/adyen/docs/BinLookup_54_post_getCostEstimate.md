# BinLookup/54/post/getCostEstimate

*Source: https://docs.adyen.com/api-explorer/BinLookup/54/post/getCostEstimate*

---

# Get a fees cost estimate
This API is available only for merchants operating in Australia, the EU, and the UK.
Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.
To retrieve this information, make the call to the/getCostEstimateendpoint. The response to this call contains the amount of the interchange and scheme fees charged by the network for this transaction, and also which surcharging policy is possible (based on current regulations).
Since not all information is known in advance (for example, if the cardholder will successfully authenticate via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a set of assumption criteria you define in theassumptionsparameter.
The transaction amount used as a base for the cost estimation.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Assumptions made for the expected characteristics of the transaction, for which the charges are being estimated.
If true, the cardholder is expected to successfully authorise via 3D Secure.
If true, the transaction is expected to have valid Level 3 data.
If not zero, the number of installments.
The card number (4-19 characters) for PCI compliant use cases. Do not use any separators.
Either thecardNumberorencryptedCardNumberfield must be provided in a payment request.
Encrypted data that stores card information for non PCI-compliant use cases. The encrypted data must be created with the Checkout Card Component or Secured Fields Component, and must contain theencryptedCardNumberfield.
Either thecardNumberorencryptedCardNumberfield must be provided in a payment request.
The merchant account identifier you want to process the (transaction) request with.
Additional data for merchants who don't use Adyen as the payment authorisation gateway.
2-letter ISO 3166 country code of the card acceptor location.
This parameter is required for the merchants who don't use Adyen as the payment authorisation gateway.
If true, indicates that the merchant is enrolled in 3D Secure for the card network.
The merchant category code (MCC) is a four-digit number which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.
The list of MCCs can be foundhere.
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
TherecurringDetailReferenceyou want to use for this cost estimate. The valueLATESTcan be used to select the most recently stored recurring detail.
Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.
For the web service API, Adyen assumes Ecommerce shopper interaction by default.
This field has the following possible values:
- Ecommerce- Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.
- ContAuth- Card on file and/or subscription transactions, where the card holder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).
- Moto- Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.
- POS- Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal.
Required for recurring payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscardBinobjectCard BIN details.Show childrenHide childrenbinstringThe first 6 digit of the card number. Enable this field via merchant account settings.commercialbooleanIf true, it indicates a commercial card. Enable this field via merchant account settings.fundingSourcestringThe card funding source. Valid values are:CHARGECREDITDEBITDEFERRED_DEBITPREPAIDPREPAID_RELOADABLEPREPAID_NONRELOADABLEEnable this field via merchant account settings.fundsAvailabilitystringIndicates availability of funds.Visa:"I" (fast funds are supported)"N" (otherwise)Mastercard:"I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list)"N" (otherwise)Returned when you verify a card BIN or estimate costs, and only ifpayoutEligibleis different from "N" or "U".issuerBinstringThe first 8 digit of the card number. Enable this field via merchant account settings.issuingBankstringThe issuing bank of the card.issuingCountrystringThe country where the card was issued from.issuingCurrencystringThe currency of the card.paymentMethodstringThe payment method associated with the card (e.g. visa, mc, or amex).payoutEligiblestringIndicates whether a payout is eligible or not for this card.Visa:"Y""N"Mastercard:"Y" (domestic and cross-border)"D" (only domestic)"N" (no MoneySend)"U" (unknown)Returned when you verify a card BIN or estimate costs, and only ifpayoutEligibleis different from "N" or "U".summarystringThe last four digits of the card number.costEstimateAmountobjectThe estimated cost (scheme fee + interchange) in the settlement currency. If the settlement currency cannot be determined, the fee in EUR is returned.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.costEstimateReferencestringAdyen's 16-character reference associated with the request.resultCodestringThe result of the cost estimation.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- CHARGE
- CREDIT
- DEBIT
- DEFERRED_DEBIT
- PREPAID
- PREPAID_RELOADABLE
- PREPAID_NONRELOADABLE
- "I" (fast funds are supported)
- "N" (otherwise)
- "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list)
- "N" (otherwise)
- "Y"
- "N"
- "Y" (domestic and cross-border)
- "D" (only domestic)
- "N" (no MoneySend)
- "U" (unknown)

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error