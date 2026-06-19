# payment-webhooks/1/post/balancePlatform.payment.updated

*Source: https://docs.adyen.com/api-explorer/payment-webhooks/1/post/balancePlatform.payment.updated*

---

# Payment authorisation expired or cancelled
UsebalancePlatform.transfer.updatedinstead.
Adyen sends this webhook when a payment authorisation has expired or has been cancelled. Use thedata.idto track the original payment authorisation from thebalancePlatform.payment.createdwebhook.
Contains event details.
Contains information about the account holder.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The amount converted to the balance account's currency, in case the original transaction currency is different.
- Apositivevalue means the amount is added to the balance account.
- Anegativevalue means the amount is deducted from the balance account.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The authorisation code for the payment.
Contains information about the balance account.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The unique identifier of the balance platform.
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
Array of checks that Adyen performed to validate the payment and the result of each.
The result of the check.
Possible values:
- valid: The validation was successful.
- invalid: The validation failed.
- notValidated: The validation was not performed because some services were unreachable or Adyen does not have the information needed to perform the check.
- notApplicable: The validation is not applicable.
Type of check.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK