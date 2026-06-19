# Notification/6/post/DIRECT_DEBIT_INITIATED

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/DIRECT_DEBIT_INITIATED*

---

# Automated direct debit initiated
Adyen sends this notification when adirect debit is initiated.
Details of the direct debit.
The code of the account.
The amount to be debited from the funding account.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The date of the debit initiation.
Invalid fields list.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The code of the merchant account.
The split data for the debit request.
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
Direct debit status.
The message regarding the operation status.
The message code.
The message text.
The status code.
Error information of failed request. No value provided here if no error occurred on processing.
The Adyen code that is mapped to the error message.
A short explanation of the issue.
The date and time when an event has been completed.
The event type of the notification.
The user or process that has triggered the notification.
Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated from the test environment.
The PSP reference of the request from which the notification originates.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringSet this parameter to[accepted]to acknowledge that you received a notification from Adyen.

#### 200 - OK