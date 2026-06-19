# radar/early_fraud_warnings

*Source: https://docs.stripe.com/api/radar/early_fraud_warnings*

---

# Early Fraud Warning
An early fraud warning indicates that the card issuer has notified us that acharge may be fraudulent.
Related guide:Early fraud warnings

# The Early Fraud Warning object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- actionablebooleanAn EFW is actionable if it has not received a dispute and has not been fully refunded. You may wish to proactively refund a charge that receives an EFW, in order to avoid receiving a dispute later.
- chargestringExpandableID of the charge this early fraud warning is for, optionally expanded.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- fraud_typestringThe type of fraud labelled by the issuer. One ofcard_never_received,fraudulent_card_application,made_with_counterfeit_card,made_with_lost_card,made_with_stolen_card,misc,unauthorized_use_of_card.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- payment_intentnullablestringExpandableID of the Payment Intent this early fraud warning is for, optionally expanded.

#### idstring

#### objectstring

#### actionableboolean

#### chargestringExpandable

#### createdtimestamp

#### fraud_typestring

#### livemodeboolean

#### payment_intentnullablestringExpandable

```
{"id":"issfr_1NnrwHBw2dPENLoi9lnhV3RQ","object":"radar.early_fraud_warning","actionable":true,"charge":"ch_1234","created":123456789,"fraud_type":"misc","livemode":false}
```

```
{"id":"issfr_1NnrwHBw2dPENLoi9lnhV3RQ","object":"radar.early_fraud_warning","actionable":true,"charge":"ch_1234","created":123456789,"fraud_type":"misc","livemode":false}
```

# Retrieve an early fraud warning
Retrieves the details of an early fraud warning that has previously been created.
Please refer to theearly fraud warningobject reference for more details.

### Parameters
Noparameters.

### Returns
Returns an EarlyFraudWarning if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/radar/early_fraud_warnings/issfr_1NnrwHBw2dPENLoi9lnhV3RQ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/radar/early_fraud_warnings/issfr_1NnrwHBw2dPENLoi9lnhV3RQ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"issfr_1NnrwHBw2dPENLoi9lnhV3RQ","object":"radar.early_fraud_warning","actionable":true,"charge":"ch_1234","created":123456789,"fraud_type":"misc","livemode":false}
```

```
{"id":"issfr_1NnrwHBw2dPENLoi9lnhV3RQ","object":"radar.early_fraud_warning","actionable":true,"charge":"ch_1234","created":123456789,"fraud_type":"misc","livemode":false}
```

# List all early fraud warnings
Returns a list of early fraud warnings.

### Parameters
- chargestringOnly return early fraud warnings for the charge specified by this charge ID.
- createdobjectOnly return early fraud warnings that were created during the given date interval.Show child parameters
- payment_intentstringOnly return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID.

#### chargestring

#### createdobject

#### payment_intentstring

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitEarlyFraudWarnings, starting after EarlyFraudWarningsstarting_after. Each entry in the array is a separate EarlyFraudWarning object. If no more EarlyFraudWarnings are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/radar/early_fraud_warnings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/radar/early_fraud_warnings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/radar/early_fraud_warnings","has_more":false,"data":[{"id":"issfr_1NnrwHBw2dPENLoi9lnhV3RQ","object":"radar.early_fraud_warning","actionable":true,"charge":"ch_1234","created":123456789,"fraud_type":"misc","livemode":false}]}
```

```
{"object":"list","url":"/v1/radar/early_fraud_warnings","has_more":false,"data":[{"id":"issfr_1NnrwHBw2dPENLoi9lnhV3RQ","object":"radar.early_fraud_warning","actionable":true,"charge":"ch_1234","created":123456789,"fraud_type":"misc","livemode":false}]}
```