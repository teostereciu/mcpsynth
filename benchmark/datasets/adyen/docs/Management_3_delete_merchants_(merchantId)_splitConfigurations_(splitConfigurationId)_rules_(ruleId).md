# Management/3/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)

*Source: https://docs.adyen.com/api-explorer/Management/3/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)*

---

# Delete a rule
Deletes the rule specified in the path.
To make this request, your API credential must have the followingrole:
- Management API - SplitConfiguration read and write
The unique identifier of the split configuration.
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdescriptionstringMax length:300Your description for the split configuration.rulesarray[object]Array of rules that define the split configuration behavior.Show childrenHide childrencardRegionstringThe card region condition that determines whether thesplit logicapplies to the transaction.This condition is in pilot phase, and not yet available for all platforms.Possible values:domestic: The card issuer and the store where the transaction is processed are registered in the same country.international: The card issuer and the store where the transaction is processed are registered in different countries or regions. Includes allinterRegionalandintraRegionaltransactions.interRegional: The card issuer and the store where the transaction is processed are registered in different regions.intraRegional: The card issuer and the store where the transaction is processed are registered in different countries, but in the same region.ANY: Applies to all transactions, regardless of the processing and issuing country/region.currencystringThe currency condition that defines whether the split logic applies.
Its value must be a three-characterISO currency code.fundingSourcestringThe funding source of the payment method.Possible values:creditdebitprepaiddeferred_debitchargedANYpaymentMethodstringThe payment method condition that defines whether the split logic applies.Possible values:Payment method variant: Apply the split logic for a specific payment method.ANY: Apply the split logic for all available payment methods.ruleIdstringThe unique identifier of the split configuration rule.shopperInteractionstringThe sales channel condition that defines whether the split logic applies.Possible values:Ecommerce: Online transactions where the cardholder is present.ContAuth: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).Moto: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.POS: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.ANY: All sales channels.splitLogicobjectContains the split logic that is applied if the rule conditions are met.Show childrenHide childrenacquiringFeesstringDeducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.additionalCommissionobjectDefines whether to book an additional commission for payments to your user's balance account. The commission amount can be defined as a fixed amount (specified in minor units), a percentage (specified in basis points), or both.Show childrenHide childrenbalanceAccountIdstringUnique identifier of the balance account to which the additional commission is booked.fixedAmountintegerA fixed commission fee, in minor units.variablePercentageintegerA variable commission fee, in basis points.adyenCommissionstringDeducts the transaction fee due to Adyen underblended ratesfrom the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.adyenFeesstringDeducts the fees due to Adyen (markup or commission) from the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.adyenMarkupstringDeducts the transaction fee due to Adyen underInterchange ++ pricingfrom the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.chargebackstringSpecifies how and from which balance account(s) to deduct the chargeback amount.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatio.chargebackCostAllocationstringDeducts the chargeback costs from the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccountcommissionobjectDefines your platform's commission for the processed payments as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. The commission is booked to your platform's liable balance account.Show childrenHide childrenfixedAmountintegerA fixed commission fee, in minor units.variablePercentageintegerA variable commission fee, in basis points.interchangestringDeducts the interchange fee from specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.paymentFeestringDeducts all transaction fees incurred by the payment from the specified balance account. The transaction fees include the acquiring fees (interchange and scheme fee), and the fees due to Adyen (markup or commission). You can book any and all these fees to different balance account by specifying other transaction fee parameters in your split configuration profile:adyenCommission: The transaction fee due to Adyen underblended rates.adyenMarkup: The transaction fee due to Adyen underInterchange ++ pricing.schemeFee: The fee paid to the card scheme for using their network.interchange: The fee paid to the issuer for each payment transaction made with the card network.adyenFees: The aggregated amount of Adyen's commission and markup.acquiringFees: The aggregated amount of the interchange and scheme fees.If you don't include at least one transaction fee type in thesplitLogicobject, Adyen updates the payment request with thepaymentFeeparameter, booking all transaction fees to your platform's liable balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.refundstringSpecifies how and from which balance account(s) to deduct the refund amount.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount,deductAccordingToSplitRatiorefundCostAllocationstringDeducts the refund costs from the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccountremainderstringBooks the amount left over after currency conversion to the specified balance account.Possible values:addToLiableAccount,addToOneBalanceAccount.schemeFeestringDeducts the scheme fee from the specified balance account.Possible values:deductFromLiableAccount,deductFromOneBalanceAccount.splitLogicIdstringUnique identifier of the collection of split instructions that are applied when the rule conditions are met.surchargestringBooks the surcharge amount to the specified balance account.Possible values:addToLiableAccount,addToOneBalanceAccounttipstringBooks the tips (gratuity) to the specified balance account.Possible values:addToLiableAccount,addToOneBalanceAccount.splitConfigurationIdstringUnique identifier of the split configuration.
- 204 - No ContentThe request has been successfully processed, but there is no additional content.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- domestic: The card issuer and the store where the transaction is processed are registered in the same country.
- international: The card issuer and the store where the transaction is processed are registered in different countries or regions. Includes allinterRegionalandintraRegionaltransactions.
- interRegional: The card issuer and the store where the transaction is processed are registered in different regions.
- intraRegional: The card issuer and the store where the transaction is processed are registered in different countries, but in the same region.
- ANY: Applies to all transactions, regardless of the processing and issuing country/region.
- credit
- debit
- prepaid
- deferred_debit
- charged
- ANY
- Payment method variant: Apply the split logic for a specific payment method.
- ANY: Apply the split logic for all available payment methods.
- Ecommerce: Online transactions where the cardholder is present.
- ContAuth: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).
- Moto: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.
- POS: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.
- ANY: All sales channels.
- adyenCommission: The transaction fee due to Adyen underblended rates.
- adyenMarkup: The transaction fee due to Adyen underInterchange ++ pricing.
- schemeFee: The fee paid to the card scheme for using their network.
- interchange: The fee paid to the issuer for each payment transaction made with the card network.
- adyenFees: The aggregated amount of Adyen's commission and markup.
- acquiringFees: The aggregated amount of the interchange and scheme fees.

```
adyenCommission
```

```
adyenMarkup
```

```
interchange
```

```
acquiringFees
```

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error