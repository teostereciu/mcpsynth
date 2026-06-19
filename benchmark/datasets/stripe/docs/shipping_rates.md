# shipping_rates

*Source: https://docs.stripe.com/api/shipping_rates*

---

# Shipping Rates
Shipping rates describe the price of shipping presented to your customers andapplied to a purchase. For more information, seeCharge for shipping.

# The Shipping Rate object

### Attributes
- idstringUnique identifier for the object.
- activebooleanWhether the shipping rate can be used for new purchases. Defaults totrue.
- display_namenullablestringThe name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
- fixed_amountnullableobjectDescribes a fixed amount to charge for shipping. Must be present if type isfixed_amount.Show child attributes
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- tax_behaviornullableenumSpecifies whether the rate is considered inclusive of taxes or exclusive of taxes. One ofinclusive,exclusive, orunspecified.Possible enum valuesexclusiveinclusiveunspecified
- tax_codenullablestringExpandableAtax codeID. The Shipping tax code istxcd_92010001.
- typeenumThe type of calculation to use on the shipping rate.Possible enum valuesfixed_amountThe shipping rate is a fixed amount.

#### idstring

#### activeboolean

#### display_namenullablestring

#### fixed_amountnullableobject

#### metadataobject

#### tax_behaviornullableenum

[TABLE]
exclusive
inclusive
unspecified
[/TABLE]

```
unspecified
```

#### tax_codenullablestringExpandable

#### typeenum

[TABLE]
fixed_amountThe shipping rate is a fixed amount.
[/TABLE]

```
fixed_amount
```

### More attributesExpand all
- objectstring
- createdtimestamp
- delivery_estimatenullableobject
- livemodeboolean

#### objectstring

#### createdtimestamp

#### delivery_estimatenullableobject

#### livemodeboolean

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

# Create a shipping rate
Creates a new shipping rate object.

### Parameters
- display_namestringRequiredThe name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.The maximum length is 100 characters.
- fixed_amountobjectDescribes a fixed amount to charge for shipping. Must be present if type isfixed_amount.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- tax_behaviorenumRecommended if calculating taxesSpecifies whether the rate is considered inclusive of taxes or exclusive of taxes. One ofinclusive,exclusive, orunspecified.Possible enum valuesexclusiveinclusiveunspecified
- tax_codestringRecommended if calculating taxesAtax codeID. The Shipping tax code istxcd_92010001.
- typeenumRequiredThe type of calculation to use on the shipping rate.Possible enum valuesfixed_amountThe shipping rate is a fixed amount.

#### display_namestringRequired

#### fixed_amountobject

#### metadataobject

#### tax_behaviorenumRecommended if calculating taxes

[TABLE]
exclusive
inclusive
unspecified
[/TABLE]

```
unspecified
```

#### tax_codestringRecommended if calculating taxes

#### typeenumRequired

[TABLE]
fixed_amountThe shipping rate is a fixed amount.
[/TABLE]

```
fixed_amount
```

### More parametersExpand all
- delivery_estimateobject

#### delivery_estimateobject

### Returns
Returns a shipping rate object if the call succeeded.

```
curlhttps://api.stripe.com/v1/shipping_rates \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Ground shipping"\-d type=fixed_amount \-d"fixed_amount[amount]"=500 \-d"fixed_amount[currency]"=usd
```

```
curlhttps://api.stripe.com/v1/shipping_rates \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Ground shipping"\-d type=fixed_amount \-d"fixed_amount[amount]"=500 \-d"fixed_amount[currency]"=usd
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

# Update a shipping rate
Updates an existing shipping rate object.

### Parameters
- activebooleanWhether the shipping rate can be used for new purchases. Defaults totrue.
- fixed_amountobjectDescribes a fixed amount to charge for shipping. Must be present if type isfixed_amount.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- tax_behaviorenumRecommended if calculating taxesSpecifies whether the rate is considered inclusive of taxes or exclusive of taxes. One ofinclusive,exclusive, orunspecified.Possible enum valuesexclusiveinclusiveunspecified

#### activeboolean

#### fixed_amountobject

#### metadataobject

#### tax_behaviorenumRecommended if calculating taxes

[TABLE]
exclusive
inclusive
unspecified
[/TABLE]

```
unspecified
```

### Returns
Returns the modified shipping rate object if the call succeeded.

```
curlhttps://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{"order_id":"6735"},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{"order_id":"6735"},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

# Retrieve a shipping rate
Returns the shipping rate object with the given ID.

### Parameters
Noparameters.

### Returns
Returns a shipping rate object if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```

```
{"id":"shr_1MrRx2LkdIwHu7ixikgEA6Wd","object":"shipping_rate","active":true,"created":1680207604,"delivery_estimate":null,"display_name":"Ground shipping","fixed_amount":{"amount":500,"currency":"usd"},"livemode":false,"metadata":{},"tax_behavior":"unspecified","tax_code":null,"type":"fixed_amount"}
```