# coupons

*Source: https://docs.stripe.com/api/coupons*

---

# Coupons
A coupon contains information about a percent-off or amount-off discount youmight want to apply to a customer. Coupons may be applied tosubscriptions,invoices,checkout sessions,quotes, and more. Coupons do not work with conventional one-offchargesorpayment intents.

# The Coupon object

### Attributes
- idstringUnique identifier for the object.
- amount_offnullableintegerAmount (in thecurrencyspecified) that will be taken off the subtotal of any invoices for this customer.
- currencynullableenumIfamount_offhas been set, the three-letterISO code for the currencyof the amount to take off.
- durationenumOne offorever,once, orrepeating. Describes how long a customer who applies this coupon will get the discount.Possible enum valuesforeverApplies to all charges from a subscription with this coupon applied.onceApplies to the first charge from a subscription with this coupon applied.repeatingApplies to charges in the firstduration_in_monthsmonths from a subscription with this coupon applied.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namenullablestringName of the coupon displayed to customers on for instance invoices or receipts.
- percent_offnullablefloatPercent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a$100 invoice$50 instead.

#### idstring

#### amount_offnullableinteger

#### currencynullableenum

#### durationenum

[TABLE]
foreverApplies to all charges from a subscription with this coupon applied.
onceApplies to the first charge from a subscription with this coupon applied.
repeatingApplies to charges in the firstduration_in_monthsmonths from a subscription with this coupon applied.
[/TABLE]

#### metadatanullableobject

#### namenullablestring

#### percent_offnullablefloat

### More attributesExpand all
- objectstring
- applies_tonullableobjectExpandable
- createdtimestamp
- currency_optionsnullableobjectExpandable
- duration_in_monthsnullableinteger
- livemodeboolean
- max_redemptionsnullableinteger
- redeem_bynullabletimestamp
- times_redeemedinteger
- validboolean

#### objectstring

#### applies_tonullableobjectExpandable

#### createdtimestamp

#### currency_optionsnullableobjectExpandable

#### duration_in_monthsnullableinteger

#### livemodeboolean

#### max_redemptionsnullableinteger

#### redeem_bynullabletimestamp

#### times_redeemedinteger

#### validboolean

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"repeating","duration_in_months":3,"livemode":false,"max_redemptions":null,"metadata":{},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"repeating","duration_in_months":3,"livemode":false,"max_redemptions":null,"metadata":{},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

# Create a coupon
You can create coupons easily via thecoupon managementpage of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.
A coupon has either apercent_offor anamount_offandcurrency. If you set anamount_off, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of100EURwill have a final total of0EURif a coupon with anamount_offof20000is applied to it and an invoice with a subtotal of300EURwill have a final total of100EURif a coupon with anamount_offof20000is applied to it.

### Parameters
- amount_offintegerA positive integer representing the amount to subtract from an invoice total (required ifpercent_offis not passed).
- currencyenumThree-letterISO code for the currencyof theamount_offparameter (required ifamount_offis passed).
- durationenumSpecifies how long the discount will be in effect if used on a subscription. Defaults toonce.Possible enum valuesforeverApplies to all charges from a subscription with this coupon applied.onceApplies to the first charge from a subscription with this coupon applied.repeatingApplies to charges in the firstduration_in_monthsmonths from a subscription with this coupon applied.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringName of the coupon displayed to customers on, for instance invoices, or receipts. By default theidis shown ifnameis not set.The maximum length is 40 characters.
- percent_offfloatA positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required ifamount_offis not passed).

#### amount_offinteger

#### currencyenum

#### durationenum

[TABLE]
foreverApplies to all charges from a subscription with this coupon applied.
onceApplies to the first charge from a subscription with this coupon applied.
repeatingApplies to charges in the firstduration_in_monthsmonths from a subscription with this coupon applied.
[/TABLE]

#### metadataobject

#### namestring

#### percent_offfloat

### More parametersExpand all
- applies_toobject
- currency_optionsobject
- duration_in_monthsinteger
- idstring
- max_redemptionsinteger
- redeem_bytimestamp

#### applies_toobject

#### currency_optionsobject

#### duration_in_monthsinteger

#### idstring

#### max_redemptionsinteger

#### redeem_bytimestamp

### Returns
Returns the coupon object.

```
curlhttps://api.stripe.com/v1/coupons \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d duration=forever \-d percent_off="25.5"
```

```
curlhttps://api.stripe.com/v1/coupons \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d duration=forever \-d percent_off="25.5"
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"forever","livemode":false,"max_redemptions":null,"metadata":{},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"forever","livemode":false,"max_redemptions":null,"metadata":{},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

# Update a coupon
Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringName of the coupon displayed to customers on, for instance invoices, or receipts. By default theidis shown ifnameis not set.The maximum length is 40 characters.

#### metadataobject

#### namestring

### More parametersExpand all
- currency_optionsobject

#### currency_optionsobject

### Returns
The newly updated coupon object if the call succeeded. Otherwise, this callraisesan error, such as if the coupon has been deleted.

```
curlhttps://api.stripe.com/v1/coupons/jMT0WJUD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/coupons/jMT0WJUD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"repeating","duration_in_months":3,"livemode":false,"max_redemptions":null,"metadata":{"order_id":"6735"},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"repeating","duration_in_months":3,"livemode":false,"max_redemptions":null,"metadata":{"order_id":"6735"},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

# Retrieve a coupon
Retrieves the coupon with the given ID.

### Parameters
Noparameters.

### Returns
Returns a coupon if a valid coupon ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/coupons/jMT0WJUD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/coupons/jMT0WJUD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"repeating","duration_in_months":3,"livemode":false,"max_redemptions":null,"metadata":{},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```

```
{"id":"jMT0WJUD","object":"coupon","amount_off":null,"created":1678037688,"currency":null,"duration":"repeating","duration_in_months":3,"livemode":false,"max_redemptions":null,"metadata":{},"name":null,"percent_off":25.5,"redeem_by":null,"times_redeemed":0,"valid":true}
```