# treasury/debit_reversals

*Source: https://docs.stripe.com/api/treasury/debit_reversals*

---

# Debit Reversals
You can reverse someReceivedDebitsdepending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

# The DebitReversal object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- financial_accountnullablestringThe FinancialAccount to reverse funds from.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- linked_flowsnullableobjectOther flows linked to a DebitReversal.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- networkenumThe rails used to reverse the funds.
- received_debitstringThe ReceivedDebit being reversed.
- statusenumStatus of the DebitReversalPossible enum valuesfailedThe network has resolved the DebitReversal against the user.processingThe DebitReversal starting state.succeededThe network has resolved the DebitReversal in the users favour. A crediting Transaction is created.
- status_transitionsobjectHash containing timestamps of when the object transitioned to a particularstatus.Show child attributes
- transactionnullablestringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### createdtimestamp

#### currencyenum

#### financial_accountnullablestring

#### hosted_regulatory_receipt_urlnullablestring

#### linked_flowsnullableobject

#### livemodeboolean

#### metadataobject

#### networkenum

#### received_debitstring

#### statusenum

[TABLE]
failedThe network has resolved the DebitReversal against the user.
processingThe DebitReversal starting state.
succeededThe network has resolved the DebitReversal in the users favour. A crediting Transaction is created.
[/TABLE]

#### status_transitionsobject

#### transactionnullablestringExpandable

```
{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}
```

```
{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}
```

# Create a DebitReversal
Reverses a ReceivedDebit and creates a DebitReversal object.

### Parameters
- received_debitstringRequiredThe ReceivedDebit to reverse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### received_debitstringRequired

#### metadataobject

### Returns
Returns a DebitReversal object.

```
curlhttps://api.stripe.com/v1/treasury/debit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d received_debit=rd_1MtkMLLkdIwHu7ixoiUFN4qd
```

```
curlhttps://api.stripe.com/v1/treasury/debit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d received_debit=rd_1MtkMLLkdIwHu7ixoiUFN4qd
```

```
{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}
```

```
{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}
```

# Retrieve a DebitReversal
Retrieves a DebitReversal object.

### Parameters
Noparameters.

### Returns
Returns a DebitReversal object.

```
curlhttps://api.stripe.com/v1/treasury/debit_reversals/debrev_1MtkMLLkdIwHu7ixIcVctOKK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/debit_reversals/debrev_1MtkMLLkdIwHu7ixIcVctOKK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}
```

```
{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}
```

# List all DebitReversals
Returns a list of DebitReversals.

### Parameters
- financial_accountstringReturns objects associated with this FinancialAccount.
- received_debitstringOnly return DebitReversals for the ReceivedDebit ID.
- resolutionenumOnly return DebitReversals for a given resolution.Possible enum valueslostDebitReversal was lost, and no Transactions will be created.wonDebitReversal was won, and a crediting Transaction will be created.
- statusenumOnly return DebitReversals for a given status.Possible enum valuescanceledThe DebitReversal has been canceled before it has been sent to the network and no funds have been returned to the account. (Currently not supported).completedThe network has provided a resolution for the DebitReversal. If won, a crediting Transaction is created.processingThe DebitReversal starting state.

#### financial_accountstring

#### received_debitstring

#### resolutionenum

[TABLE]
lostDebitReversal was lost, and no Transactions will be created.
wonDebitReversal was won, and a crediting Transaction will be created.
[/TABLE]

#### statusenum

[TABLE]
canceledThe DebitReversal has been canceled before it has been sent to the network and no funds have been returned to the account. (Currently not supported).
completedThe network has provided a resolution for the DebitReversal. If won, a crediting Transaction is created.
processingThe DebitReversal starting state.
[/TABLE]

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitDebitReversals, starting after DebitReversalstarting_after. Each entry in the array is a separate DebitReversal object. If no more DebitReversals are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/treasury/debit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkMLLkdIwHu7ixrkGP4bqB \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/debit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkMLLkdIwHu7ixrkGP4bqB \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/debit_reversals","has_more":false,"data":[{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}]}
```

```
{"object":"list","url":"/v1/treasury/debit_reversals","has_more":false,"data":[{"id":"debrev_1MtkMLLkdIwHu7ixIcVctOKK","object":"treasury.debit_reversal","amount":1000,"created":1680755021,"currency_code":"usd","financial_account":"fa_1MtkMLLkdIwHu7ixrkGP4bqB","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w","linked_flows":null,"livemode":false,"custom_fields":{},"network":"ach","received_debit":"rd_1MtkMLLkdIwHu7ixoiUFN4qd","status":"processing","status_transitions":{"completed_at":null},"transaction":"trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}]}
```