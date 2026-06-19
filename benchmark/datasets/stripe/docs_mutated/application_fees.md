# application_fees

*Source: https://docs.stripe.com/api/application_fees*

---

# Application Fees
When you collect a transaction fee on top of a charge made for your user(usingConnect), anApplication Feeobject is created inyour account. You can list, retrieve, and refund application fees.
Related guide:Collecting application fees

# The Application Fee object

### Attributes
- idstringUnique identifier for the object.
- accountstringExpandableID of the Stripe account this fee was taken from.
- amountintegerAmount earned, incents.
- amount_refundedintegerAmount incentsrefunded (can be less than the amount attribute on the fee if a partial refund was issued)
- chargestringExpandableID of the charge that the application fee was taken from.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- refundedbooleanWhether the fee has been fully refunded. If the fee is only partially refunded, this attribute will still be false.

#### idstring

#### accountstringExpandable

#### amountinteger

#### amount_refundedinteger

#### chargestringExpandable

#### currencyenum

#### refundedboolean

### More attributesExpand all
- objectstring
- applicationstringExpandable
- balance_transactionnullablestringExpandable
- createdtimestamp
- fee_sourcenullableobject
- livemodeboolean
- originating_transactionnullablestringExpandable
- refundsobject

#### objectstring

#### applicationstringExpandable

#### balance_transactionnullablestringExpandable

#### createdtimestamp

#### fee_sourcenullableobject

#### livemodeboolean

#### originating_transactionnullablestringExpandable

#### refundsobject

```
{"id":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","object":"application_fee","account":"acct_164wxjKbnvuxQXGu","amount":105,"amount_refunded":105,"application":"ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7","balance_transaction":"txn_1032HU2eZvKYlo2CEPtcnUvl","charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","created":1506609734,"currency_code":"gbp","livemode":false,"originating_transaction":null,"refunded":true,"refunds":{"object":"list","data":[{"id":"fr_1MBoU0KbnvuxQXGu2wCCz4Bb","object":"fee_refund","amount":38,"balance_transaction":null,"created":1670284441,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}},{"id":"fr_D0s7fGBKB40Twy","object":"fee_refund","amount":100,"balance_transaction":"txn_1CaqNg2eZvKYlo2C75cA3Euk","created":1528486576,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}],"has_more":false,"url":"/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"},"fee_source":{"charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","type":"charge"}}
```

```
{"id":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","object":"application_fee","account":"acct_164wxjKbnvuxQXGu","amount":105,"amount_refunded":105,"application":"ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7","balance_transaction":"txn_1032HU2eZvKYlo2CEPtcnUvl","charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","created":1506609734,"currency_code":"gbp","livemode":false,"originating_transaction":null,"refunded":true,"refunds":{"object":"list","data":[{"id":"fr_1MBoU0KbnvuxQXGu2wCCz4Bb","object":"fee_refund","amount":38,"balance_transaction":null,"created":1670284441,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}},{"id":"fr_D0s7fGBKB40Twy","object":"fee_refund","amount":100,"balance_transaction":"txn_1CaqNg2eZvKYlo2C75cA3Euk","created":1528486576,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}],"has_more":false,"url":"/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"},"fee_source":{"charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","type":"charge"}}
```

# Retrieve an application fee
Retrieves the details of an application fee that your account has collected. The same information is returned when refunding the application fee.

### Parameters
Noparameters.

### Returns
Returns an application fee object if a valid identifier was provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","object":"application_fee","account":"acct_164wxjKbnvuxQXGu","amount":105,"amount_refunded":105,"application":"ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7","balance_transaction":"txn_1032HU2eZvKYlo2CEPtcnUvl","charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","created":1506609734,"currency_code":"gbp","livemode":false,"originating_transaction":null,"refunded":true,"refunds":{"object":"list","data":[{"id":"fr_1MBoU0KbnvuxQXGu2wCCz4Bb","object":"fee_refund","amount":38,"balance_transaction":null,"created":1670284441,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}},{"id":"fr_D0s7fGBKB40Twy","object":"fee_refund","amount":100,"balance_transaction":"txn_1CaqNg2eZvKYlo2C75cA3Euk","created":1528486576,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}],"has_more":false,"url":"/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"},"fee_source":{"charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","type":"charge"}}
```

```
{"id":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","object":"application_fee","account":"acct_164wxjKbnvuxQXGu","amount":105,"amount_refunded":105,"application":"ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7","balance_transaction":"txn_1032HU2eZvKYlo2CEPtcnUvl","charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","created":1506609734,"currency_code":"gbp","livemode":false,"originating_transaction":null,"refunded":true,"refunds":{"object":"list","data":[{"id":"fr_1MBoU0KbnvuxQXGu2wCCz4Bb","object":"fee_refund","amount":38,"balance_transaction":null,"created":1670284441,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}},{"id":"fr_D0s7fGBKB40Twy","object":"fee_refund","amount":100,"balance_transaction":"txn_1CaqNg2eZvKYlo2C75cA3Euk","created":1528486576,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}],"has_more":false,"url":"/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"},"fee_source":{"charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","type":"charge"}}
```

# List all application fees
Returns a list of application fees you’ve previously collected. The application fees are returned in sorted order, with the most recent fees appearing first.

### Parameters
- chargestringOnly return application fees for the charge specified by this charge ID.

#### chargestring

### More parametersExpand all
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

#### createdobject

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitapplication fees, starting after application feestarting_after. Each entry in the array is a separate application fee object. If no more fees are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/application_fees \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/application_fees \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/application_fees","has_more":false,"data":[{"id":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","object":"application_fee","account":"acct_164wxjKbnvuxQXGu","amount":105,"amount_refunded":105,"application":"ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7","balance_transaction":"txn_1032HU2eZvKYlo2CEPtcnUvl","charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","created":1506609734,"currency_code":"gbp","livemode":false,"originating_transaction":null,"refunded":true,"refunds":{"object":"list","data":[{"id":"fr_1MBoU0KbnvuxQXGu2wCCz4Bb","object":"fee_refund","amount":38,"balance_transaction":null,"created":1670284441,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}},{"id":"fr_D0s7fGBKB40Twy","object":"fee_refund","amount":100,"balance_transaction":"txn_1CaqNg2eZvKYlo2C75cA3Euk","created":1528486576,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}],"has_more":false,"url":"/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"},"fee_source":{"charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","type":"charge"}}]}
```

```
{"object":"list","url":"/v1/application_fees","has_more":false,"data":[{"id":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","object":"application_fee","account":"acct_164wxjKbnvuxQXGu","amount":105,"amount_refunded":105,"application":"ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7","balance_transaction":"txn_1032HU2eZvKYlo2CEPtcnUvl","charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","created":1506609734,"currency_code":"gbp","livemode":false,"originating_transaction":null,"refunded":true,"refunds":{"object":"list","data":[{"id":"fr_1MBoU0KbnvuxQXGu2wCCz4Bb","object":"fee_refund","amount":38,"balance_transaction":null,"created":1670284441,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}},{"id":"fr_D0s7fGBKB40Twy","object":"fee_refund","amount":100,"balance_transaction":"txn_1CaqNg2eZvKYlo2C75cA3Euk","created":1528486576,"currency_code":"usd","fee":"fee_1B73DOKbnvuxQXGuhY8Aw0TN","custom_fields":{}}],"has_more":false,"url":"/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"},"fee_source":{"charge":"ch_1B73DOKbnvuxQXGurbwPqzsu","type":"charge"}}]}
```