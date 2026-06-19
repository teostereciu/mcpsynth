# billing/credit-balance-transaction

*Source: https://docs.stripe.com/api/billing/credit-balance-transaction*

---

# Credit Balance Transaction
A credit balance transaction is a resource representing a transaction (either a credit or a debit) against an existing credit grant.

# The Credit Balance Transaction object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- creditnullableobjectCredit details for this credit balance transaction. Only present if type iscredit.Show child attributes
- credit_grantstringExpandableThe credit grant associated with this credit balance transaction.
- debitnullableobjectDebit details for this credit balance transaction. Only present if type isdebit.Show child attributes
- effective_attimestampThe effective time of this credit balance transaction.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- test_clocknullablestringExpandableID of the test clock this credit balance transaction belongs to.
- typenullableenumThe type of credit balance transaction (credit or debit).Possible enum valuescreditA credit transaction.debitA debit transaction.

#### idstring

#### objectstring

#### createdtimestamp

#### creditnullableobject

#### credit_grantstringExpandable

#### debitnullableobject

#### effective_attimestamp

#### livemodeboolean

#### test_clocknullablestringExpandable

#### typenullableenum

[TABLE]
creditA credit transaction.
debitA debit transaction.
[/TABLE]

```
{"id":"cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue","object":"billing.credit_balance_transaction","created":1726619524,"credit":null,"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"credits_applied":{"invoice":"in_1Q0BoLL6nFOS1ekDbwBM5ER1","invoice_line_item":"il_1QB443L6nFOS1ekDwRiN3Z4n"},"type":"credits_applied"},"effective_at":1729211351,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"debit"}
```

```
{"id":"cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue","object":"billing.credit_balance_transaction","created":1726619524,"credit":null,"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"credits_applied":{"invoice":"in_1Q0BoLL6nFOS1ekDbwBM5ER1","invoice_line_item":"il_1QB443L6nFOS1ekDwRiN3Z4n"},"type":"credits_applied"},"effective_at":1729211351,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"debit"}
```

# Retrieve a credit balance transaction
Retrieves a credit balance transaction.

### Parameters
- idstringRequiredUnique identifier for the object.

#### idstringRequired

### Returns
Returns a credit balance transaction.

```
curlhttps://api.stripe.com/v1/billing/credit_balance_transactions/cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/billing/credit_balance_transactions/cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue","object":"billing.credit_balance_transaction","created":1726619524,"credit":null,"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"credits_applied":{"invoice":"in_1Q0BoLL6nFOS1ekDbwBM5ER1","invoice_line_item":"il_1QB443L6nFOS1ekDwRiN3Z4n"},"type":"credits_applied"},"effective_at":1729211351,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"debit"}
```

```
{"id":"cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue","object":"billing.credit_balance_transaction","created":1726619524,"credit":null,"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"credits_applied":{"invoice":"in_1Q0BoLL6nFOS1ekDbwBM5ER1","invoice_line_item":"il_1QB443L6nFOS1ekDwRiN3Z4n"},"type":"credits_applied"},"effective_at":1729211351,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"debit"}
```

# List credit balance transactions
Retrieve a list of credit balance transactions.

### Parameters
- credit_grantstringThe credit grant for which to fetch credit balance transactions.
- customerstringThe customer_id whose credit balance transactions you’re retrieving.
- customer_accountstringThe account representing the customer_id whose credit balance transactions you’re retrieving.

#### credit_grantstring

#### customerstring

#### customer_accountstring

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Returns a list of credit balance transactions.

```
curl-G https://api.stripe.com/v1/billing/credit_balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_QrvQguzkIK8zTj \-d credit_grant=credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE
```

```
curl-G https://api.stripe.com/v1/billing/credit_balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_QrvQguzkIK8zTj \-d credit_grant=credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE
```

```
{"object":"list","data":[{"id":"cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue","object":"billing.credit_balance_transaction","created":1726619524,"credit":null,"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"credits_applied":{"invoice":"in_1Q0BoLL6nFOS1ekDbwBM5ER1","invoice_line_item":"il_1QB443L6nFOS1ekDwRiN3Z4n"},"type":"credits_applied"},"effective_at":1729211351,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"debit"},{"id":"cbtxn_test_61R9ZkIbb17ze4b2s41L6nFOS1ekDXHs","object":"billing.credit_balance_transaction","created":1726619434,"credit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"type":"credits_granted"},"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":null,"effective_at":1726619434,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"credit"}],"has_more":false,"url":"/v1/billing/credit_grants"}
```

```
{"object":"list","data":[{"id":"cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue","object":"billing.credit_balance_transaction","created":1726619524,"credit":null,"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"credits_applied":{"invoice":"in_1Q0BoLL6nFOS1ekDbwBM5ER1","invoice_line_item":"il_1QB443L6nFOS1ekDwRiN3Z4n"},"type":"credits_applied"},"effective_at":1729211351,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"debit"},{"id":"cbtxn_test_61R9ZkIbb17ze4b2s41L6nFOS1ekDXHs","object":"billing.credit_balance_transaction","created":1726619434,"credit":{"amount":{"monetary":{"currency_code":"usd","value":1000},"type":"monetary"},"type":"credits_granted"},"credit_grant":"credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE","debit":null,"effective_at":1726619434,"livemode":false,"test_clock":"clock_1Q0BoJL6nFOS1ekDbyYYuseM","type":"credit"}],"has_more":false,"url":"/v1/billing/credit_grants"}
```