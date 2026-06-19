# prices

*Source: https://docs.stripe.com/api/prices*

---

# Prices
Prices define the unit cost, currency_code, and (optional) billing cycle for both recurring and one-time purchases of products.Productshelp you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.
For example, you might have a single “gold” product that has prices for $10/month, $100/year, and €9 once.
Related guides:Set up a subscription,create an invoice, and more aboutproducts and prices.

# The Price object

### Attributes
- idstringUnique identifier for the object.
- activebooleanWhether the price can be used for new purchases.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nicknamenullablestringA brief notes of the price, hidden from customers.
- productstringExpandableThe ID of the product this price is associated with.
- recurringnullableobjectThe recurring components of a price such asintervalandusage_type.Show child attributes
- tax_behaviornullableenumOnly required if adefault tax behaviorwas not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One ofinclusive,exclusive, orunspecified. Once specified as eitherinclusiveorexclusive, it cannot be changed.Possible enum valuesexclusiveinclusiveunspecified
- typeenumOne ofone_timeorrecurringdepending on whether the price is for a one-time purchase or a recurring (subscription) purchase.Possible enum valuesone_timerecurring
- unit_amountnullableintegerThe unit amount incentsto be charged, represented as a whole integer if possible. Only set ifbilling_scheme=per_unit.

#### idstring

#### activeboolean

#### currencyenum

#### metadataobject

#### nicknamenullablestring

#### productstringExpandable

#### recurringnullableobject

#### tax_behaviornullableenum

[TABLE]
exclusive
inclusive
unspecified
[/TABLE]

```
unspecified
```

#### typeenum

[TABLE]
one_time
recurring
[/TABLE]

#### unit_amountnullableinteger

### More attributesExpand all
- objectstring
- billing_schemeenum
- createdtimestamp
- currency_optionsnullableobjectExpandable
- custom_unit_amountnullableobject
- livemodeboolean
- lookup_keynullablestring
- tiersnullablearray of objectsExpandable
- tiers_modenullableenum
- transform_quantitynullableobject
- unit_amount_decimalnullabledecimal string

#### objectstring

#### billing_schemeenum

#### createdtimestamp

#### currency_optionsnullableobjectExpandable

#### custom_unit_amountnullableobject

#### livemodeboolean

#### lookup_keynullablestring

#### tiersnullablearray of objectsExpandable

#### tiers_modenullableenum

#### transform_quantitynullableobject

#### unit_amount_decimalnullabledecimal string

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

# Create a price
Creates a newPricefor an existingProduct. The Price can be recurring or one-time.

### Parameters
- currencyenumRequiredThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- activebooleanWhether the price can be used for new purchases. Defaults totrue.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- nicknamestringA brief notes of the price, hidden from customers.
- productstringRequired unless product_data is providedThe ID of theProductthat thisPricewill belong to.
- recurringobjectThe recurring components of a price such asintervalandusage_type.Show child parameters
- tax_behaviorenumRecommended if calculating taxesOnly required if adefault tax behaviorwas not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One ofinclusive,exclusive, orunspecified. Once specified as eitherinclusiveorexclusive, it cannot be changed.Possible enum valuesexclusiveinclusiveunspecified
- unit_amountintegerRequired conditionallyA positive integer incents(or 0 for a free price) representing how much to charge. One ofunit_amount,unit_amount_decimal, orcustom_unit_amountis required, unlessbilling_scheme=tiered.

#### currencyenumRequired

#### activeboolean

#### metadataobject

#### nicknamestring

#### productstringRequired unless product_data is provided

#### recurringobject

#### tax_behaviorenumRecommended if calculating taxes

[TABLE]
exclusive
inclusive
unspecified
[/TABLE]

```
unspecified
```

#### unit_amountintegerRequired conditionally

### More parametersExpand all
- billing_schemeenum
- currency_optionsobject
- custom_unit_amountobjectRequired unless unit_amount is provided
- lookup_keystring
- product_dataobjectRequired unless product is provided
- tiersarray of objectsRequired if billing_scheme=tiered
- tiers_modeenumRequired if billing_scheme=tiered
- transfer_lookup_keyboolean
- transform_quantityobject
- unit_amount_decimalstring

#### billing_schemeenum

#### currency_optionsobject

#### custom_unit_amountobjectRequired unless unit_amount is provided

#### lookup_keystring

#### product_dataobjectRequired unless product is provided

#### tiersarray of objectsRequired if billing_scheme=tiered

#### tiers_modeenumRequired if billing_scheme=tiered

#### transfer_lookup_keyboolean

#### transform_quantityobject

#### unit_amount_decimalstring

### Returns
The newly createdPriceobject is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/prices \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d currency_code=usd \-d unit_amount=1000 \-d"recurring[interval]"=month \-d"product_data[name]"="Gold Plan"
```

```
curlhttps://api.stripe.com/v1/prices \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d currency_code=usd \-d unit_amount=1000 \-d"recurring[interval]"=month \-d"product_data[name]"="Gold Plan"
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

# Update a price
Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.

### Parameters
- activebooleanWhether the price can be used for new purchases. Defaults totrue.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- nicknamestringA brief notes of the price, hidden from customers.
- tax_behaviorenumRecommended if calculating taxesOnly required if adefault tax behaviorwas not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One ofinclusive,exclusive, orunspecified. Once specified as eitherinclusiveorexclusive, it cannot be changed.Possible enum valuesexclusiveinclusiveunspecified

#### activeboolean

#### metadataobject

#### nicknamestring

#### tax_behaviorenumRecommended if calculating taxes

[TABLE]
exclusive
inclusive
unspecified
[/TABLE]

```
unspecified
```

### More parametersExpand all
- currency_optionsobject
- lookup_keystring
- transfer_lookup_keyboolean

#### currency_optionsobject

#### lookup_keystring

#### transfer_lookup_keyboolean

### Returns
The updated price object is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{"order_id":"6735"},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{"order_id":"6735"},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

# Retrieve a price
Retrieves the price with the given ID.

### Parameters
Noparameters.

### Returns
Returns a price if a valid price or plan ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```

```
{"id":"price_1MoBy5LkdIwHu7ixZhnattbh","object":"price","active":true,"billing_scheme":"per_unit","created":1679431181,"currency_code":"usd","custom_unit_amount":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NZKdYqrwEYx6iK","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"}
```