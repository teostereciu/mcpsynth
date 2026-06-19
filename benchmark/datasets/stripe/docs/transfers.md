# transfers

*Source: https://docs.stripe.com/api/transfers*

---

# Transfers
ATransferobject is created when you move funds between Stripe accounts aspart of Connect.
Before April 6, 2017, transfers also represented movement of funds from aStripe account to a card or bank account. This behavior has since been splitout into aPayoutobject, with corresponding payout endpoints. For moreinformation, read about thetransfer/payout split.
Related guide:Creating separate charges and transfers

# The Transfer object

### Attributes
- idstringUnique identifier for the object.
- amountintegerAmount incentsto be transferred.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- destinationnullablestringExpandableID of the Stripe account the transfer was sent to.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### idstring

#### amountinteger

#### currencyenum

#### descriptionnullablestring

#### destinationnullablestringExpandable

#### metadataobject

### More attributesExpand all
- objectstring
- amount_reversedinteger
- balance_transactionnullablestringExpandable
- createdtimestamp
- destination_paymentnullablestringExpandable
- livemodeboolean
- reversalsobject
- reversedboolean
- source_transactionnullablestringExpandable
- source_typenullablestring
- transfer_groupnullablestring

#### objectstring

#### amount_reversedinteger

#### balance_transactionnullablestringExpandable

#### createdtimestamp

#### destination_paymentnullablestringExpandable

#### livemodeboolean

#### reversalsobject

#### reversedboolean

#### source_transactionnullablestringExpandable

#### source_typenullablestring

#### transfer_groupnullablestring

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

# Create a transfer
To send funds from your Stripe account to a connected account, you create a new transfer object. YourStripe balancemust be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.

### Parameters
- currencyenumRequiredThree-letterISO code for currencyin lowercase. Must be asupported currency.
- destinationstringRequiredThe ID of a connected Stripe account.See the Connect documentationfor details.
- amountintegerRequiredA positive integer incentsrepresenting how much to transfer.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### currencyenumRequired

#### destinationstringRequired

#### amountintegerRequired

#### descriptionstring

#### metadataobject

### More parametersExpand all
- source_transactionstring
- source_typestring
- transfer_groupstring

#### source_transactionstring

#### source_typestring

#### transfer_groupstring

### Returns
Returns a transfer object if there were no initial errors with the transfer creation (e.g., insufficient funds).

```
curlhttps://api.stripe.com/v1/transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=400 \-d currency=usd \-d destination=acct_1MTfjCQ9PRzxEwkZ \-d transfer_group=ORDER_95
```

```
curlhttps://api.stripe.com/v1/transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=400 \-d currency=usd \-d destination=acct_1MTfjCQ9PRzxEwkZ \-d transfer_group=ORDER_95
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

# Update a transfer
Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request accepts only metadata as an argument.

### Parameters
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### descriptionstring

#### metadataobject

### Returns
Returns the transfer object if the update succeeded. This call willraisean errorif update parameters are invalid.

```
curlhttps://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{"order_id":"6735"},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{"order_id":"6735"},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

# Retrieve a transfer
Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.

### Parameters
Noparameters.

### Returns
Returns a transfer object if a valid identifier was provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```

```
{"id":"tr_1MiN3gLkdIwHu7ixNCZvFdgA","object":"transfer","amount":400,"amount_reversed":0,"balance_transaction":"txn_1MiN3gLkdIwHu7ixxapQrznl","created":1678043844,"currency":"usd","description":null,"destination":"acct_1MTfjCQ9PRzxEwkZ","destination_payment":"py_1MiN3gQ9PRzxEwkZWTPGNq9o","livemode":false,"metadata":{},"reversals":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"},"reversed":false,"source_transaction":null,"source_type":"card","transfer_group":"ORDER_95"}
```