# treasury/transactions

*Source: https://docs.stripe.com/api/treasury/transactions*

---

# Transactions
Transactions represent changes to aFinancialAccount’sbalance.

# The Transaction object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- balance_impactobjectThe change made to each of the FinancialAccount’s sub-balances by the Transaction.Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- entriesnullableobjectExpandableA list of TransactionEntries that are part of this Transaction. This cannot be expanded in any list endpoints.Show child attributes
- financial_accountstringThe FinancialAccount associated with this object.
- flownullablestringID of the flow that created the Transaction.
- flow_detailsnullableobjectExpandableDetails of the flow that created the Transaction.Show child attributes
- flow_typeenumType of the flow that created the Transaction.Possible enum valuescredit_reversalThe Transaction is associated with a CreditReversal.debit_reversalThe Transaction is associated with a DebitReversal.inbound_transferThe Transaction is associated with an InboundTransfer.issuing_authorizationThe Transaction is associated with an Issuing authorization.otherThe Transaction is associated with some other money movement not listed above.outbound_paymentThe Transaction is associated with an OutboundPayment.outbound_transferThe Transaction is associated with an OutboundTransfer.received_creditThe Transaction is associated with a ReceivedCredit.received_debitThe Transaction is associated with a ReceivedDebit.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- statusenumStatus of the Transaction.Possible enum valuesopenThe initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.postedFunds have successfully entered or left the account. The current balance was affected.voidThe Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.
- status_transitionsobjectHash containing timestamps of when the object transitioned to a particularstatus.Show child attributes

#### idstring

#### objectstring

#### amountinteger

#### balance_impactobject

#### createdtimestamp

#### currencyenum

#### descriptionstring

#### entriesnullableobjectExpandable

#### financial_accountstring

#### flownullablestring

#### flow_detailsnullableobjectExpandable

#### flow_typeenum

[TABLE]
credit_reversalThe Transaction is associated with a CreditReversal.
debit_reversalThe Transaction is associated with a DebitReversal.
inbound_transferThe Transaction is associated with an InboundTransfer.
issuing_authorizationThe Transaction is associated with an Issuing authorization.
otherThe Transaction is associated with some other money movement not listed above.
outbound_paymentThe Transaction is associated with an OutboundPayment.
outbound_transferThe Transaction is associated with an OutboundTransfer.
received_creditThe Transaction is associated with a ReceivedCredit.
received_debitThe Transaction is associated with a ReceivedDebit.
[/TABLE]

```
credit_reversal
```

```
debit_reversal
```

```
inbound_transfer
```

```
issuing_authorization
```

```
outbound_payment
```

```
outbound_transfer
```

```
received_credit
```

```
received_debit
```

#### livemodeboolean

#### statusenum

[TABLE]
openThe initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.
postedFunds have successfully entered or left the account. The current balance was affected.
voidThe Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.
[/TABLE]

#### status_transitionsobject

```
{"id":"trxn_1MtkYw2eZvKYlo2ClMGIO54z","object":"treasury.transaction","amount":-100,"balance_impact":{"cash":-100,"inbound_pending":0,"outbound_pending":100},"created":1680755802,"currency":"usd","description":"Jane Austen (6789) | Outbound transfer | transfer","financial_account":"fa_1MtkYw2eZvKYlo2CrqmzUo3O","flow":"obt_1MtkYw2eZvKYlo2CqsyBpQts","flow_type":"outbound_transfer","livemode":false,"status":"open","status_transitions":{"posted_at":null,"void_at":null}}
```

```
{"id":"trxn_1MtkYw2eZvKYlo2ClMGIO54z","object":"treasury.transaction","amount":-100,"balance_impact":{"cash":-100,"inbound_pending":0,"outbound_pending":100},"created":1680755802,"currency":"usd","description":"Jane Austen (6789) | Outbound transfer | transfer","financial_account":"fa_1MtkYw2eZvKYlo2CrqmzUo3O","flow":"obt_1MtkYw2eZvKYlo2CqsyBpQts","flow_type":"outbound_transfer","livemode":false,"status":"open","status_transitions":{"posted_at":null,"void_at":null}}
```

# Retrieve a Transaction
Retrieves the details of an existing Transaction.

### Parameters
Noparameters.

### Returns
Returns a Transaction object if a valid identifier was provided. Otherwise, returns an error.

```
curlhttps://api.stripe.com/v1/treasury/transactions/trxn_1MtkYw2eZvKYlo2ClMGIO54z \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/transactions/trxn_1MtkYw2eZvKYlo2ClMGIO54z \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"trxn_1MtkYw2eZvKYlo2ClMGIO54z","object":"treasury.transaction","amount":-100,"balance_impact":{"cash":-100,"inbound_pending":0,"outbound_pending":100},"created":1680755802,"currency":"usd","description":"Jane Austen (6789) | Outbound transfer | transfer","financial_account":"fa_1MtkYw2eZvKYlo2CrqmzUo3O","flow":"obt_1MtkYw2eZvKYlo2CqsyBpQts","flow_type":"outbound_transfer","livemode":false,"status":"open","status_transitions":{"posted_at":null,"void_at":null}}
```

```
{"id":"trxn_1MtkYw2eZvKYlo2ClMGIO54z","object":"treasury.transaction","amount":-100,"balance_impact":{"cash":-100,"inbound_pending":0,"outbound_pending":100},"created":1680755802,"currency":"usd","description":"Jane Austen (6789) | Outbound transfer | transfer","financial_account":"fa_1MtkYw2eZvKYlo2CrqmzUo3O","flow":"obt_1MtkYw2eZvKYlo2CqsyBpQts","flow_type":"outbound_transfer","livemode":false,"status":"open","status_transitions":{"posted_at":null,"void_at":null}}
```

# List all Transactions
Retrieves a list of Transaction objects.

### Parameters
- financial_accountstringReturns objects associated with this FinancialAccount.
- createdobjectOnly return Transactions that were created during the given date interval.Show child parameters
- order_byenumThe results are in reverse chronological order bycreatedorposted_at. The default iscreated.Possible enum valuescreatedTimestamp describing when the Transaction was created.posted_atTimestamp describing when the Transaction was posted.
- statusenumOnly return Transactions that have the given status:open,posted, orvoid.Possible enum valuesopenThe initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.postedFunds have successfully entered or left the account. The current balance was affected.voidThe Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.
- status_transitionsobjectA filter for thestatus_transitions.posted_attimestamp. When using this filter,status=postedandorder_by=posted_atmust also be specified.Show child parameters

#### financial_accountstring

#### createdobject

#### order_byenum

[TABLE]
createdTimestamp describing when the Transaction was created.
posted_atTimestamp describing when the Transaction was posted.
[/TABLE]

#### statusenum

[TABLE]
openThe initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.
postedFunds have successfully entered or left the account. The current balance was affected.
voidThe Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.
[/TABLE]

#### status_transitionsobject

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitTransactions, starting after Transactionstarting_after. Each entry in the array is a separate Transaction object. If no more Transactions are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/treasury/transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkYw2eZvKYlo2CrqmzUo3O \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkYw2eZvKYlo2CrqmzUo3O \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/transactions","has_more":false,"data":[{"id":"trxn_1MtkYw2eZvKYlo2ClMGIO54z","object":"treasury.transaction","amount":-100,"balance_impact":{"cash":-100,"inbound_pending":0,"outbound_pending":100},"created":1680755802,"currency":"usd","description":"Jane Austen (6789) | Outbound transfer | transfer","financial_account":"fa_1MtkYw2eZvKYlo2CrqmzUo3O","flow":"obt_1MtkYw2eZvKYlo2CqsyBpQts","flow_type":"outbound_transfer","livemode":false,"status":"open","status_transitions":{"posted_at":null,"void_at":null}}]}
```

```
{"object":"list","url":"/v1/treasury/transactions","has_more":false,"data":[{"id":"trxn_1MtkYw2eZvKYlo2ClMGIO54z","object":"treasury.transaction","amount":-100,"balance_impact":{"cash":-100,"inbound_pending":0,"outbound_pending":100},"created":1680755802,"currency":"usd","description":"Jane Austen (6789) | Outbound transfer | transfer","financial_account":"fa_1MtkYw2eZvKYlo2CrqmzUo3O","flow":"obt_1MtkYw2eZvKYlo2CqsyBpQts","flow_type":"outbound_transfer","livemode":false,"status":"open","status_transitions":{"posted_at":null,"void_at":null}}]}
```