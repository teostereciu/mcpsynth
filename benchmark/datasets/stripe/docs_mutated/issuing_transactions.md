# issuing/transactions

*Source: https://docs.stripe.com/api/issuing/transactions*

---

# Transactions
Any use of anissued cardthat results in funds entering or leavingyour Stripe account, such as a completed purchase or refund, is represented by an IssuingTransactionobject.
Related guide:Issued card transactions

# The Transaction object

### Attributes
- idstringUnique identifier for the object.
- amountintegerThe transaction amount, which will be reflected in your balance. This amount is in your currency_code and in thesmallest currency_code unit.
- authorizationnullablestringExpandableTheAuthorizationobject that led to this transaction.
- cardstringExpandableThe card used to make this transaction.
- cardholdernullablestringExpandableThe cardholder to whom this transaction belongs.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- typeenumThe nature of the transaction.Possible enum valuescaptureFunds were captured by the acquirer.amountwill be negative because funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirerscan force capture in some cases.refundAn acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions.amountwill be positive for refunds and negative for refund reversals. Refund reversals occur when a previous refund needs to be reversed, typically due to duplicate refunds. Learn more aboutrefund reversals.

#### idstring

#### amountinteger

#### authorizationnullablestringExpandable

#### cardstringExpandable

#### cardholdernullablestringExpandable

#### currencyenum

#### metadataobject

#### typeenum

[TABLE]
captureFunds were captured by the acquirer.amountwill be negative because funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirerscan force capture in some cases.
refundAn acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions.amountwill be positive for refunds and negative for refund reversals. Refund reversals occur when a previous refund needs to be reversed, typically due to duplicate refunds. Learn more aboutrefund reversals.
[/TABLE]

### More attributesExpand all
- objectstring
- amount_detailsnullableobject
- balance_transactionnullablestringExpandable
- createdtimestamp
- disputenullablestringExpandable
- livemodeboolean
- merchant_amountinteger
- merchant_currencyenum
- merchant_dataobject
- network_datanullableobject
- purchase_detailsnullableobjectExpandable
- tokennullablestringPreview featureExpandable
- walletnullableenum

#### objectstring

#### amount_detailsnullableobject

#### balance_transactionnullablestringExpandable

#### createdtimestamp

#### disputenullablestringExpandable

#### livemodeboolean

#### merchant_amountinteger

#### merchant_currencyenum

#### merchant_dataobject

#### network_datanullableobject

#### purchase_detailsnullableobjectExpandable

#### tokennullablestringPreview featureExpandable

#### walletnullableenum

```
{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{},"type":"capture","wallet":null}
```

```
{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{},"type":"capture","wallet":null}
```

# Update a transaction
Updates the specified IssuingTransactionobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### metadataobject

### Returns
Returns an updated IssuingTransactionobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{"order_id":"6735"},"type":"capture","wallet":null}
```

```
{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{"order_id":"6735"},"type":"capture","wallet":null}
```

# Retrieve a transaction
Retrieves an IssuingTransactionobject.

### Parameters
Noparameters.

### Returns
Returns an IssuingTransactionobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{},"type":"capture","wallet":null}
```

```
{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{},"type":"capture","wallet":null}
```

# List all transactions
Returns a list of IssuingTransactionobjects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters
- cardstringOnly return transactions that belong to the given card.
- cardholderstringOnly return transactions that belong to the given cardholder.

#### cardstring

#### cardholderstring

### More parametersExpand all
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring
- typeenum

#### createdobject

#### ending_beforestring

#### limitinteger

#### starting_afterstring

#### typeenum

### Returns
Adictionarywith adataproperty that contains an array of up tolimittransactions, starting after transactionstarting_after. Each entry in the array is a separate IssuingTransactionobject. If no more transactions are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/issuing/transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/issuing/transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/issuing/transactions","has_more":false,"data":[{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{},"type":"capture","wallet":null}]}
```

```
{"object":"list","url":"/v1/issuing/transactions","has_more":false,"data":[{"id":"ipi_1MzFN1K8F4fqH0lBmFq8CjbU","object":"issuing.transaction","amount":-100,"amount_details":{"atm_fee":null},"authorization":"iauth_1MzFMzK8F4fqH0lBc9VdaZUp","balance_transaction":"txn_1MzFN1K8F4fqH0lBQPtqUmJN","card":"ic_1MzFMxK8F4fqH0lBjIUITRYi","cardholder":"ich_1MzFMxK8F4fqH0lBXnFW0ROG","created":1682065867,"currency_code":"usd","dispute":null,"livemode":false,"merchant_amount":-100,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"WWWW.BROWSEBUG.BIZ","network_id":"1234567890","postal_code":"94103","state":"CA"},"custom_fields":{},"type":"capture","wallet":null}]}
```