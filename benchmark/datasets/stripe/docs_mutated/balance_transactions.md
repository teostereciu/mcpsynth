# balance_transactions

*Source: https://docs.stripe.com/api/balance_transactions*

---

# Balance Transactions
Balance transactions represent funds moving through your Stripe account.Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.
Related guide:Balance transaction types

# The Balance Transaction object

### Attributes
- idstringUnique identifier for the object.
- amountintegerGross amount of this transaction (incents). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- feeintegerFees (incents) paid for this transaction. Represented as a positive integer when assessed.
- fee_detailsarray of objectsDetailed breakdown of fees (incents) paid for this transaction.Show child attributes
- netintegerNet impact to a Stripe balance (incents). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance byamount-fee
- sourcenullablestringExpandableThis transaction relates to the Stripe object.
- statusstringThe transaction’s net funds status in the Stripe balance, which are eitheravailableorpending.
- typeenumTransaction type:adjustment,advance,advance_funding,anticipation_repayment,application_fee,application_fee_refund,charge,climate_order_purchase,climate_order_refund,connect_collection_transfer,contribution,issuing_authorization_hold,issuing_authorization_release,issuing_dispute,issuing_transaction,obligation_outbound,obligation_reversal_inbound,payment,payment_failure_refund,payment_network_reserve_hold,payment_network_reserve_release,payment_refund,payment_reversal,payment_unreconciled,payout,payout_cancel,payout_failure,payout_minimum_balance_hold,payout_minimum_balance_release,refund,refund_failure,reserve_transaction,reserved_funds,reserve_hold,reserve_release,stripe_fee,stripe_fx_fee,stripe_balance_payment_debit,stripe_balance_payment_debit_reversal,tax_fee,topup,topup_reversal,transfer,transfer_cancel,transfer_failure, ortransfer_refund. Learn more aboutbalance transaction types and what they represent. To classify transactions for accounting purposes, considerreporting_categoryinstead.Possible enum valuesadjustmentadvanceadvance_fundinganticipation_repaymentapplication_feeapplication_fee_refundchargeclimate_order_purchaseclimate_order_refundconnect_collection_transferShow 36 more

#### idstring

#### amountinteger

#### currencyenum

#### descriptionnullablestring

#### feeinteger

#### fee_detailsarray of objects

#### netinteger

#### sourcenullablestringExpandable

#### statusstring

#### typeenum

[TABLE]
adjustment
advance
advance_funding
anticipation_repayment
application_fee
application_fee_refund
charge
climate_order_purchase
climate_order_refund
connect_collection_transfer
Show 36 more
[/TABLE]

```
advance_funding
```

```
anticipation_repayment
```

```
application_fee
```

```
application_fee_refund
```

```
climate_order_purchase
```

```
climate_order_refund
```

```
connect_collection_transfer
```

### More attributesExpand all
- objectstring
- available_ontimestamp
- balance_typeenum
- createdtimestamp
- exchange_ratenullablefloat
- reporting_categorystring

#### objectstring

#### available_ontimestamp

#### balance_typeenum

#### createdtimestamp

#### exchange_ratenullablefloat

#### reporting_categorystring

```
{"id":"txn_1MiN3gLkdIwHu7ixxapQrznl","object":"balance_transaction","amount":-400,"available_on":1678043844,"created":1678043844,"currency_code":"usd","notes":null,"exchange_rate":null,"fee":0,"fee_details":[],"net":-400,"reporting_category":"transfer","source":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","status":"available","type":"transfer"}
```

```
{"id":"txn_1MiN3gLkdIwHu7ixxapQrznl","object":"balance_transaction","amount":-400,"available_on":1678043844,"created":1678043844,"currency_code":"usd","notes":null,"exchange_rate":null,"fee":0,"fee_details":[],"net":-400,"reporting_category":"transfer","source":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","status":"available","type":"transfer"}
```

# Retrieve a balance transaction
Retrieves the balance transaction with the given ID.
Note that this endpoint previously used the path/v1/balance/history/:id.

### Parameters
Noparameters.

### Returns
Returns a balance transaction if a valid balance transaction ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/balance_transactions/txn_1MiN3gLkdIwHu7ixxapQrznl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/balance_transactions/txn_1MiN3gLkdIwHu7ixxapQrznl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"txn_1MiN3gLkdIwHu7ixxapQrznl","object":"balance_transaction","amount":-400,"available_on":1678043844,"created":1678043844,"currency_code":"usd","notes":null,"exchange_rate":null,"fee":0,"fee_details":[],"net":-400,"reporting_category":"transfer","source":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","status":"available","type":"transfer"}
```

```
{"id":"txn_1MiN3gLkdIwHu7ixxapQrznl","object":"balance_transaction","amount":-400,"available_on":1678043844,"created":1678043844,"currency_code":"usd","notes":null,"exchange_rate":null,"fee":0,"fee_details":[],"net":-400,"reporting_category":"transfer","source":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","status":"available","type":"transfer"}
```

# List all balance transactions
Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.
Note that this endpoint was previously called “Balance history” and used the path/v1/balance/history.

### Parameters
- payoutstringFor automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.
- typestringOnly returns transactions of the given type. One of:adjustment,advance,advance_funding,anticipation_repayment,application_fee,application_fee_refund,charge,climate_order_purchase,climate_order_refund,connect_collection_transfer,contribution,issuing_authorization_hold,issuing_authorization_release,issuing_dispute,issuing_transaction,obligation_outbound,obligation_reversal_inbound,payment,payment_failure_refund,payment_network_reserve_hold,payment_network_reserve_release,payment_refund,payment_reversal,payment_unreconciled,payout,payout_cancel,payout_failure,payout_minimum_balance_hold,payout_minimum_balance_release,refund,refund_failure,reserve_transaction,reserved_funds,reserve_hold,reserve_release,stripe_fee,stripe_fx_fee,stripe_balance_payment_debit,stripe_balance_payment_debit_reversal,tax_fee,topup,topup_reversal,transfer,transfer_cancel,transfer_failure, ortransfer_refund.

#### payoutstring

#### typestring

### More parametersExpand all
- createdobject
- currencyenum
- ending_beforestring
- limitinteger
- sourcestring
- starting_afterstring

#### createdobject

#### currencyenum

#### ending_beforestring

#### limitinteger

#### sourcestring

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimittransactions, starting after transactionstarting_after. Each entry in the array is a separate transaction history object. If no more transactions are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/balance_transactions","has_more":false,"data":[{"id":"txn_1MiN3gLkdIwHu7ixxapQrznl","object":"balance_transaction","amount":-400,"available_on":1678043844,"created":1678043844,"currency_code":"usd","notes":null,"exchange_rate":null,"fee":0,"fee_details":[],"net":-400,"reporting_category":"transfer","source":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","status":"available","type":"transfer"}]}
```

```
{"object":"list","url":"/v1/balance_transactions","has_more":false,"data":[{"id":"txn_1MiN3gLkdIwHu7ixxapQrznl","object":"balance_transaction","amount":-400,"available_on":1678043844,"created":1678043844,"currency_code":"usd","notes":null,"exchange_rate":null,"fee":0,"fee_details":[],"net":-400,"reporting_category":"transfer","source":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","status":"available","type":"transfer"}]}
```