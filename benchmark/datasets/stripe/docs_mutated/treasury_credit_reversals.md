# treasury/credit_reversals

*Source: https://docs.stripe.com/api/treasury/credit_reversals*

---

# Credit Reversals
You can reverse someReceivedCreditsdepending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

# The CreditReversal object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- financial_accountstringThe FinancialAccount to reverse funds from.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- networkenumThe rails used to reverse the funds.
- received_creditstringThe ReceivedCredit being reversed.
- statusenumStatus of the CreditReversalPossible enum valuescanceledThe CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).postedThe CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)processingThe CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).
- status_transitionsobjectHash containing timestamps of when the object transitioned to a particularstatus.Show child attributes
- transactionnullablestringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### createdtimestamp

#### currencyenum

#### financial_accountstring

#### hosted_regulatory_receipt_urlnullablestring

#### livemodeboolean

#### metadataobject

#### networkenum

#### received_creditstring

#### statusenum

[TABLE]
canceledThe CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).
postedThe CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)
processingThe CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).
[/TABLE]

#### status_transitionsobject

#### transactionnullablestringExpandable

```
{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}
```

```
{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}
```

# Create a CreditReversal
Reverses a ReceivedCredit and creates a CreditReversal object.

### Parameters
- received_creditstringRequiredThe ReceivedCredit to reverse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### received_creditstringRequired

#### metadataobject

### Returns
Returns a CreditReversal object.

```
curlhttps://api.stripe.com/v1/treasury/credit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d received_credit=rc_1MtkGJLkdIwHu7ixWPuY9DGn
```

```
curlhttps://api.stripe.com/v1/treasury/credit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d received_credit=rc_1MtkGJLkdIwHu7ixWPuY9DGn
```

```
{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}
```

```
{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}
```

# Retrieve a CreditReversal
Retrieves the details of an existing CreditReversal by passing the unique CreditReversal ID from either the CreditReversal creation request or CreditReversal list

### Parameters
Noparameters.

### Returns
Returns a CreditReversal object.

```
curlhttps://api.stripe.com/v1/treasury/credit_reversals/credrev_1Mtklw2eZvKYlo2CJG2MWJM7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/credit_reversals/credrev_1Mtklw2eZvKYlo2CJG2MWJM7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}
```

```
{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}
```

# List all CreditReversals
Returns a list of CreditReversals.

### Parameters
- financial_accountstringReturns objects associated with this FinancialAccount.
- received_creditstringOnly return CreditReversals for the ReceivedCredit ID.
- statusenumOnly return CreditReversals for a given status.Possible enum valuescanceledThe CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).postedThe CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)processingThe CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).

#### financial_accountstring

#### received_creditstring

#### statusenum

[TABLE]
canceledThe CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).
postedThe CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)
processingThe CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).
[/TABLE]

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitCreditReversals, starting after CreditReversalstarting_after. Each entry in the array is a separate CreditReversal object. If no more CreditReversal are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/treasury/credit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkGJLkdIwHu7ix6FAcfxof \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/credit_reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkGJLkdIwHu7ix6FAcfxof \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/credit_reversals","has_more":false,"data":[{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}]}
```

```
{"object":"list","url":"/v1/treasury/credit_reversals","has_more":false,"data":[{"id":"credrev_1Mtklw2eZvKYlo2CJG2MWJM7","object":"treasury.credit_reversal","amount":1000,"created":1680756608,"currency_code":"usd","financial_account":"fa_1Mtklw2eZvKYlo2CNHscZzs2","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ","livemode":false,"custom_fields":{},"network":"ach","received_credit":"rc_1Mtklw2eZvKYlo2CxuluQFPR","status":"processing","status_transitions":{"posted_at":null},"transaction":"trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}]}
```