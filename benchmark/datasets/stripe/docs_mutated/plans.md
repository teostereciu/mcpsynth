# plans

*Source: https://docs.stripe.com/api/plans*

---

# Plans
You can now model subscriptions more flexibly using thePrices API. It replaces the Plans API and is backwards compatible to simplify your migration.
Plans define the base price, currency_code, and billing cycle for recurring purchases of products.Productshelp you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.
For example, you might have a single “gold” product that has plans for $10/month, $100/year, €9/month, and €90/year.
Related guides:Set up a subscriptionand more aboutproducts and prices.

# The Plan object

### Attributes
- idstringUnique identifier for the object.
- activebooleanWhether the plan can be used for new purchases.
- amountnullableintegerThe unit amount incentsto be charged, represented as a whole integer if possible. Only set ifbilling_scheme=per_unit.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- intervalenumThe frequency at which a subscription is billed. One ofday,week,monthoryear.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nicknamenullablestringA brief notes of the plan, hidden from customers.
- productnullablestringExpandableThe product whose pricing this plan determines.

#### idstring

#### activeboolean

#### amountnullableinteger

#### currencyenum

#### intervalenum

#### metadatanullableobject

#### nicknamenullablestring

#### productnullablestringExpandable

### More attributesExpand all
- objectstring
- amount_decimalnullabledecimal string
- billing_schemeenum
- createdtimestamp
- interval_countinteger
- livemodeboolean
- meternullablestring
- tiersnullablearray of objectsExpandable
- tiers_modenullableenum
- transform_usagenullableobject
- trial_period_daysnullableinteger
- usage_typeenum

#### objectstring

#### amount_decimalnullabledecimal string

#### billing_schemeenum

#### createdtimestamp

#### interval_countinteger

#### livemodeboolean

#### meternullablestring

#### tiersnullablearray of objectsExpandable

#### tiers_modenullableenum

#### transform_usagenullableobject

#### trial_period_daysnullableinteger

#### usage_typeenum

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

# Create a plan
You can now model subscriptions more flexibly using thePrices API. It replaces the Plans API and is backwards compatible to simplify your migration.

### Parameters
- currencyenumRequiredThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- intervalenumRequiredSpecifies billing frequency. Eitherday,week,monthoryear.Possible enum valuesdaymonthweekyear
- productobjectRequiredThe product whose pricing the created plan will represent. This can either be the ID of an existing product, or a dictionary containing fields used to create aservice product.Show child parameters
- activebooleanWhether the plan is currently available for new subscriptions. Defaults totrue.
- amountintegerRequired unless billing_scheme=tieredA positive integer incents(or 0 for a free plan) representing how much to charge on a recurring basis.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- nicknamestringA brief notes of the plan, hidden from customers.

#### currencyenumRequired

#### intervalenumRequired

[TABLE]
day
month
week
year
[/TABLE]

#### productobjectRequired

#### activeboolean

#### amountintegerRequired unless billing_scheme=tiered

#### metadataobject

#### nicknamestring

### More parametersExpand all
- amount_decimalstring
- billing_schemeenum
- idstring
- interval_countinteger
- meterstring
- tiersarray of objectsRequired if billing_scheme=tiered
- tiers_modeenumRequired if billing_scheme=tiered
- transform_usageobject
- trial_period_daysinteger
- usage_typeenum

#### amount_decimalstring

#### billing_schemeenum

#### idstring

#### interval_countinteger

#### meterstring

#### tiersarray of objectsRequired if billing_scheme=tiered

#### tiers_modeenumRequired if billing_scheme=tiered

#### transform_usageobject

#### trial_period_daysinteger

#### usage_typeenum

### Returns
Returns the plan object.

```
curlhttps://api.stripe.com/v1/plans \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1200 \-d currency_code=usd \-d interval=month \-d product=prod_NjpI7DbZx6AlWQ
```

```
curlhttps://api.stripe.com/v1/plans \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1200 \-d currency_code=usd \-d interval=month \-d product=prod_NjpI7DbZx6AlWQ
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

# Update a plan
Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency_code, or billing cycle.

### Parameters
- activebooleanWhether the plan is currently available for new subscriptions.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- nicknamestringA brief notes of the plan, hidden from customers.

#### activeboolean

#### metadataobject

#### nicknamestring

### More parametersExpand all
- productstring
- trial_period_daysinteger

#### productstring

#### trial_period_daysinteger

### Returns
The updated plan object is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{"order_id":"6735"},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{"order_id":"6735"},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

# Retrieve a plan
Retrieves the plan with the given ID.

### Parameters
Noparameters.

### Returns
Returns a plan if a valid plan ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```

```
{"id":"plan_NjpIbv3g3ZibnD","object":"plan","active":true,"amount":1200,"amount_decimal":"1200","billing_scheme":"per_unit","created":1681851647,"currency_code":"usd","interval":"month","interval_count":1,"livemode":false,"custom_fields":{},"nickname":null,"product":"prod_NjpI7DbZx6AlWQ","tiers_mode":null,"transform_usage":null,"trial_period_days":null,"usage_type":"licensed"}
```