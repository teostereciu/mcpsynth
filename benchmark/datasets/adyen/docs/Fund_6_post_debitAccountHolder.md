# Fund/6/post/debitAccountHolder

*Source: https://docs.adyen.com/api-explorer/Fund/6/post/debitAccountHolder*

---

# Send a direct debit request
Sends a direct debit request to an account holder's bank account. If the direct debit is successful, the funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct debit in aDIRECT_DEBIT_INITIATEDnotification webhook.

```
DIRECT_DEBIT_INITIATED
```
To learn more about direct debits, seeTop up accounts.
The code of the account holder.
The amount to be debited from the account holder's bank account.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.
A description of the direct debit. Maximum length: 35 characters.
Allowed characters:a-z,A-Z,0-9, and special characters/?:().,'+ ";.
Your merchant account.
Contains instructions on how to split the funds between the accounts in your platform. The request must have at least one split item.
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
- Required iftypeisBalanceAccount,Commission,Default, orVATin yourBalance Platformintegration.
The three-characterISO currency code. By default, this is the original payment currency.
The value of the split amount, inminor units.
Your description for the split item.
Your unique reference for the part of the payment booked to the specifiedaccount.
This is required iftypeisMarketPlace(Classic Platforms integration) orBalanceAccount(Balance Platform).
For the other types, we also recommend providing auniquereference so you can reconcile the split and the associated payment in the transaction overview and in the reports.
The part of the payment you want to book to the specifiedaccount.
Possible values for theBalance Platform:
- BalanceAccount: books part of the payment (specified inamount) to the specifiedaccount.
- Transaction fees types that you can book to the specifiedaccount:AcquiringFees: the aggregated amount of the interchange and scheme fees.PaymentFee: the aggregated amount of all transaction fees.AdyenFees: the aggregated amount of Adyen's commission and markup fees.AdyenCommission: the transaction fees due to Adyen underblended rates.AdyenMarkup: the transaction fees due to Adyen underInterchange ++ pricing.Interchange: the fees paid to the issuer for each payment made with the card network.SchemeFee: the fees paid to the card scheme for using their network.
- Commission: your platform's commission on the payment (specified inamount), booked to your liable balance account.
- Remainder: the amount left over after a currency conversion, booked to the specifiedaccount.
- TopUp: allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.
- VAT: the value-added tax charged on the payment, booked to your platforms liable balance account.
- Commission: your platform's commission (specified inamount) on the payment, booked to your liable balance account.
- Default: in very specific use cases, allows you to book the specifiedamountto the specifiedaccount. For more information, contact Adyen support.
- AcquiringFees: the aggregated amount of the interchange and scheme fees.
- PaymentFee: the aggregated amount of all transaction fees.
- AdyenFees: the aggregated amount of Adyen's commission and markup fees.
- AdyenCommission: the transaction fees due to Adyen underblended rates.
- AdyenMarkup: the transaction fees due to Adyen underInterchange ++ pricing.
- Interchange: the fees paid to the issuer for each payment made with the card network.
- SchemeFee: the fees paid to the card scheme for using their network.
Possible values for theClassic Platforms integration:Commission,Default,Marketplace,PaymentFee,VAT.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaccountHolderCodestringThe code of the account holder.bankAccountUUIDstringThe Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.invalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.merchantReferencesarray[string]List of thereferencevalues from thesplitarray in the request.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 202 - AcceptedThe request has been accepted for processing, but the processing has not been completed.Show moreShow lessaccountHolderCodestringThe code of the account holder.bankAccountUUIDstringThe Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.invalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.merchantReferencesarray[string]List of thereferencevalues from thesplitarray in the request.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error