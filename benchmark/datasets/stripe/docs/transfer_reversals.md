# transfer_reversals

*Source: https://docs.stripe.com/api/transfer_reversals*

---

# Transfer Reversals
Stripe Connectplatforms can reverse transfers made to aconnected account, either entirely or partially, and can also specify whetherto refund any related application fees. Transfer reversals add to theplatform’s balance and subtract from the destination account’s balance.
Reversing a transfer that was made for adestinationchargeis allowed only up to the amount ofthe charge. It is possible to reverse atransfer_grouptransfer only if the destination account has enough balance to cover thereversal.
Related guide:Reverse transfers

# The Transfer Reversal object

### Attributes
- idstringUnique identifier for the object.
- amountintegerAmount, incents.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- transferstringExpandableID of the transfer that was reversed.

#### idstring

#### amountinteger

#### currencyenum

#### metadatanullableobject

#### transferstringExpandable

### More attributesExpand all
- objectstring
- balance_transactionnullablestringExpandable
- createdtimestamp
- destination_payment_refundnullablestringExpandable
- source_refundnullablestringExpandable

#### objectstring

#### balance_transactionnullablestringExpandable

#### createdtimestamp

#### destination_payment_refundnullablestringExpandable

#### source_refundnullablestringExpandable

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

# Create a transfer reversal
When you create a new reversal, you must specify a transfer to create it on.
When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.
Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.

### Parameters
- amountintegerA positive integer incentsrepresenting how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.
- descriptionstringAn arbitrary string which you can attach to a reversal object. This will be unset if you POST an empty value.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### amountinteger

#### descriptionstring

#### metadataobject

### More parametersExpand all
- refund_application_feeboolean

#### refund_application_feeboolean

### Returns
Returns a transfer reversal object if the reversal succeeded.Raisesan errorif the transfer has already been reversed or an invalid transfer identifier was provided.

```
curlhttps://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=400
```

```
curlhttps://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=400
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

# Update a reversal
Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request only accepts metadata and description as arguments.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### metadataobject

### Returns
Returns the reversal object if the update succeeded. This call willraisean errorif update parameters are invalid.

```
curlhttps://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{"order_id":"6735"},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{"order_id":"6735"},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

# Retrieve a reversal
By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

### Parameters
Noparameters.

### Returns
Returns the reversal object.

```
curlhttps://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```

```
{"id":"trr_1Mio2eLkdIwHu7ixN5LPJS4a","object":"transfer_reversal","amount":400,"balance_transaction":"txn_1Mio2eLkdIwHu7ixosfrbjhW","created":1678147568,"currency":"usd","destination_payment_refund":"pyr_1Mio2eQ9PRzxEwkZYewpaIFB","metadata":{},"source_refund":null,"transfer":"tr_1Mio2dLkdIwHu7ixsUuCxJpu"}
```