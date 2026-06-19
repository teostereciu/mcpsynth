# fee_refunds

*Source: https://docs.stripe.com/api/fee_refunds*

---

# Application Fee Refunds
Application Fee Refundobjects allow you to refund an application fee thathas previously been created but not yet refunded. Funds will be refunded tothe Stripe account from which the fee was originally collected.
Related guide:Refunding application fees

# The Application Fee Refund object

### Attributes
- idstringUnique identifier for the object.
- amountintegerAmount, incents.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- feestringExpandableID of the application fee that was refunded.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### idstring

#### amountinteger

#### currencyenum

#### feestringExpandable

#### metadatanullableobject

### More attributesExpand all
- objectstring
- balance_transactionnullablestringExpandable
- createdtimestamp

#### objectstring

#### balance_transactionnullablestringExpandable

#### createdtimestamp

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}
```

# Create an application fee refund
Refunds an application fee that has previously been collected but not yet refunded.Funds will be refunded to the Stripe account from which the fee was originally collected.
You can optionally refund only part of an application fee.You can do so multiple times, until the entire fee has been refunded.
Once entirely refunded, an application fee can’t be refunded again.This method willraisean error when called on an already-refunded application fee,or when trying to refund more money than is left on an application fee.

### Parameters
- amountintegerA positive integer, incents, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### amountinteger

#### metadataobject

### Returns
Returns theApplication Fee Refundobject if the refundsucceeded.Raisesan errorif the fee has already been refunded,or if an invalid fee identifier was provided.

```
curl-X POST https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X POST https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}
```

# Update an application fee refund
Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request only accepts custom_fields as an argument.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### metadataobject

### Returns
Returns the application fee refund object if the update succeeded. This call willraisean errorif update parameters are invalid.

```
curlhttps://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{"order_id":"6735"}}
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{"order_id":"6735"}}
```

# Retrieve an application fee refund
By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

### Parameters
Noparameters.

### Returns
Returns the application fee refund object.

```
curlhttps://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}
```

```
{"id":"fr_1MtJRpKbnvuxQXGuM6Ww0D24","object":"fee_refund","amount":100,"balance_transaction":null,"created":1680651573,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}
```