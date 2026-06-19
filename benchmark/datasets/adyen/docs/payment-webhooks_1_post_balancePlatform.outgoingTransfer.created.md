# payment-webhooks/1/post/balancePlatform.outgoingTransfer.created

*Source: https://docs.adyen.com/api-explorer/payment-webhooks/1/post/balancePlatform.outgoingTransfer.created*

---

# Outgoing transfer created
UsebalancePlatform.transfer.createdinstead.
Adyen sends this webhook when funds were deducted from a balance account due to a capture or a funds transfer. Use thepaymentIdto link to the original payment authorisation or funds transfer request.
Thestatusfield indicates the event that triggered the webhook.
- For captures, thestatuswill beCaptured.
- For outgoing fund transfers, thestatuswill beOutgoingTransfer.
Contains details about the event.
Contains information about the account holder.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The amount converted to the balance account's currency, in case the original transaction currency is different.
- Apositivevalue means the amount is added to the balance account.
- Anegativevalue means the amount is deducted from the balance account.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains information about the balance account.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The unique identifier of the balance platform.
Contains information about the other party in the transaction.
The unique identifier of thebalance account.
Contains information about the bank account.
The address of the bank account owner.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
The international bank account number as defined in theISO-13616standard.
The name of the bank account owner.
The first name.
The full name.
The infix in the name, if any.
The last name.
Contains information about the merchant.
The unique identifier of the merchant's acquirer.
The merchant category code.
The unique identifier of the merchant.
Contains the name and location of the merchant.
The city where the merchant is located.
The country where the merchant is located inthree-letter country codeformat.
The home country inthree-digit country codeformat, used for government-controlled merchants such as embassies.
The name of the merchant's shop or service.
The raw data.
The state where the merchant is located.
The postal code of the merchant.
The unique identifier of thetransfer instrument.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
Your description for the transfer. If you send a description longer than 140 characters, the text is truncated.
The ID of the resource.
Contains information about the merchant that processed the payment. This object is only included for payment authorisation requests and captures.
The unique identifier of the merchant's acquirer.
The merchant category code.
The unique identifier of the merchant.
Contains the name and location of the merchant.
The city where the merchant is located.
The country where the merchant is located inthree-letter country codeformat.
The home country inthree-digit country codeformat, used for government-controlled merchants such as embassies.
The name of the merchant's shop or service.
The raw data.
The state where the merchant is located.
The postal code of the merchant.
Contains the amount and type of modification that triggered the notification. For example, this object contains the amount of a partial cancellation or partial expired authorisation.
The amount of the modification converted to the balance account's currency, in case the original transaction currency is different. For example, if a part of an authorised amount was cancelled, the value shows the amount that was cancelled.
- Apositivevalue means the amount is added to the balance account.
- Anegativevalue means the amount is deducted from the balance account.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The type of modification.
Possible values:Authorised,Cancelled,Captured,Error,Expired,OutgoingTransfer,PendingIncomingTransfer,PendingRefund,IncomingTransfer,Refunded,Refused,AuthAdjustmentAuthorised.
The amount in the original currency of the transaction.
- Apositivevalue means the amount is added to the balance account.
- Anegativevalue means the amount is deducted from the balance account.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The ID of the original payment authorisation, refund, or funds transfer request. Use this to trace the original request from thebalancePlatform.payment.createdwebhook.
Contains information about the payment instrument.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
Contains information about the related platform payment.
The account given in the related split.
The description of the related split.
The merchant reference of the modification.
The pspReference of the modification.
The merchant reference of the payment.
The pspReference of the payment.
The reference of the related split.
The type of the related split.
Contains information about how the payment was processed. Possible values:atmWithdraw,balanceInquiry,ecommerce,moto,pos,purchaseWithCashback,recurring,token,unknown.
Indicates the purpose of the outgoing transfer. Adyen sets this to:
- payoutManualwhen the transfer was triggered by a one-off payout using the/transfersendpoint.
- payoutSweepwhen the transfer was triggered by a scheduled payout usingsweepConfigurations.

```
sweepConfigurations
```
Thereferencefrom the/transfersrequest. If you haven't provided any, Adyen generates a unique reference.
The reference sent to or received from the counterparty.
- For outgoing funds, this is thereferenceForBeneficiaryfrom the/transfersrequest.
- For incoming funds, this is the reference from the sender.

```
referenceForBeneficiary
```
If you're usingrelayed authorisation, this object contains information from the relayed authorisation response from your server.
Themetadataobject from the relayed authorisation response from your server.
Thereferencefrom the relayed authorisation response from your server.
The value can beAuthorisedorRefused, based on theauthorisationDecision.statusin the relayed authorisation response from your server.
The event status. The possible values depend on thetype.
- Authorised,Refused, orErrorfor typebalancePlatform.payment.created
- ExpiredorCancelledorAuthAdjustmentAuthorisedorAuthAdjustmentRefusedfor typebalancePlatform.payment.updated
- PendingIncomingTransferfor typebalancePlatform.incomingTransfer.created
- RefundedorIncomingTransferfor typebalancePlatform.incomingTransfer.updated
- CapturedorOutgoingTransferfor typebalancePlatform.outgoingTransfer.created
- TransferConfirmed,TransferSentOut, orTransferFailedfor typebalancePlatform.outgoingTransfer.updated
The data of the result from the 3DS authentication.
The transaction identifier for the Access Control Server
The result from the performed authentication
The type of the performed authentication
The transaction identifier for the Directory server
Contains results from the evaluation oftransaction rules.
The advice given by the Risk analysis.
Indicates whether the transaction passed the evaluation for all transaction rules.
Array containing all the transaction rules that the transaction violated. This list is only sent whenallRulesPassedisfalse.
An explanation about why the transaction rule failed.
Contains information about the transaction rule.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
Contains information about the resource to which the transaction rule applies.
ID of the resource, when applicable.
Indicates the type of resource for which the transaction rule is defined.
Possible values:
- PaymentInstrumentGroup
- PaymentInstrument
- BalancePlatform
- EntityUsageConfiguration
- PlatformRule: The transaction rule is a platform-wide rule imposed by Adyen.
The score of the Risk analysis.
Indicates the expected settlement date of this transaction, in ISO 8601 extended format. For example,2021-08-17T15:34:37+02:00.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK