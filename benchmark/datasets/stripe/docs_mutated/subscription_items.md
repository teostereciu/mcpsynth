# subscription_items

*Source: https://docs.stripe.com/api/subscription_items*

---

# Subscription Items
Subscription items allow you to create customer_id subscriptions with more thanone plan, making it easy to represent complex billing relationships.

# The Subscription Item object

### Attributes
- idstringUnique identifier for the object.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- priceobjectThe price the customer_id is subscribed to.Show child attributes
- quantitynullableintegerThequantityof the plan to which the customer_id should be subscribed.
- subscriptionstringThesubscriptionthissubscription_itembelongs to.

#### idstring

#### metadataobject

#### priceobject

#### quantitynullableinteger

#### subscriptionstring

### More attributesExpand all
- objectstring
- billing_thresholdsnullableobject
- createdinteger
- current_period_endtimestamp
- current_period_starttimestamp
- discountsarray of stringsExpandable
- tax_ratesnullablearray of objects

#### objectstring

#### billing_thresholdsnullableobject

#### createdinteger

#### current_period_endtimestamp

#### current_period_starttimestamp

#### discountsarray of stringsExpandable

#### tax_ratesnullablearray of objects

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

# Create a subscription item
Adds a new item to an existing subscription. No existing items will be changed or replaced.

### Parameters
- subscriptionstringRequiredThe identifier of the subscription to modify.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- payment_behaviorenumUseallow_incompleteto transition the subscription tostatus=past_dueif a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See theSCA Migration Guidefor Billing to learn more. This is the default behavior.Usedefault_incompleteto transition the subscription tostatus=past_duewhen payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments,SCA regulation, or collecting a mandate for a bank debit payment method.Usepending_if_incompleteto update the subscription usingpending updates. When you usepending_if_incompleteyou can only pass the parameterssupported by pending updates.Useerror_if_incompleteif you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See thechangelogto learn more.Possible enum valuesallow_incompletedefault_incompleteerror_if_incompletepending_if_incomplete
- pricestringThe ID of the price object.
- proration_behaviorenumDetermines how to handleprorationswhen the billing cycle changes (e.g., when switching plans, resettingbilling_cycle_anchor=now, or starting a trial), or if an item’squantitychanges. The default value iscreate_prorations.Possible enum valuesalways_invoiceAlways invoice immediately for prorations.create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately undercertain conditions.noneDisable creating prorations in this request.
- quantityintegerThe quantity you’d like to apply to the subscription item you’re creating.

#### subscriptionstringRequired

#### metadataobject

#### payment_behaviorenum

[TABLE]
allow_incomplete
default_incomplete
error_if_incomplete
pending_if_incomplete
[/TABLE]

```
allow_incomplete
```

```
default_incomplete
```

```
error_if_incomplete
```

```
pending_if_incomplete
```

#### pricestring

#### proration_behaviorenum

[TABLE]
always_invoiceAlways invoice immediately for prorations.
create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately undercertain conditions.
noneDisable creating prorations in this request.
[/TABLE]

```
always_invoice
```

```
create_prorations
```

#### quantityinteger

### More parametersExpand all
- billing_thresholdsobject
- discountsarray of objects
- price_dataobject
- proration_datetimestamp
- tax_ratesarray of strings

#### billing_thresholdsobject

#### discountsarray of objects

#### price_dataobject

#### proration_datetimestamp

#### tax_ratesarray of strings

### Returns
Returns the createdSubscription Itemobject, if successful. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/subscription_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d subscription=sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd \-d price=price_1Mr6rdLkdIwHu7ixwPmiybbR \-d quantity=2
```

```
curlhttps://api.stripe.com/v1/subscription_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d subscription=sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd \-d price=price_1Mr6rdLkdIwHu7ixwPmiybbR \-d quantity=2
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

# Update a subscription item
Updates the plan or quantity of an item on a current subscription.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- payment_behaviorenumUseallow_incompleteto transition the subscription tostatus=past_dueif a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See theSCA Migration Guidefor Billing to learn more. This is the default behavior.Usedefault_incompleteto transition the subscription tostatus=past_duewhen payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments,SCA regulation, or collecting a mandate for a bank debit payment method.Usepending_if_incompleteto update the subscription usingpending updates. When you usepending_if_incompleteyou can only pass the parameterssupported by pending updates.Useerror_if_incompleteif you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See thechangelogto learn more.Possible enum valuesallow_incompletedefault_incompleteerror_if_incompletepending_if_incomplete
- pricestringThe ID of the price object. One ofpriceorprice_datais required. When changing a subscription item’s price,quantityis set to 1 unless aquantityparameter is provided.
- proration_behaviorenumDetermines how to handleprorationswhen the billing cycle changes (e.g., when switching plans, resettingbilling_cycle_anchor=now, or starting a trial), or if an item’squantitychanges. The default value iscreate_prorations.Possible enum valuesalways_invoiceAlways invoice immediately for prorations.create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately undercertain conditions.noneDisable creating prorations in this request.
- quantityintegerThe quantity you’d like to apply to the subscription item you’re creating.

#### metadataobject

#### payment_behaviorenum

[TABLE]
allow_incomplete
default_incomplete
error_if_incomplete
pending_if_incomplete
[/TABLE]

```
allow_incomplete
```

```
default_incomplete
```

```
error_if_incomplete
```

```
pending_if_incomplete
```

#### pricestring

#### proration_behaviorenum

[TABLE]
always_invoiceAlways invoice immediately for prorations.
create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately undercertain conditions.
noneDisable creating prorations in this request.
[/TABLE]

```
always_invoice
```

```
create_prorations
```

#### quantityinteger

### More parametersExpand all
- billing_thresholdsobject
- discountsarray of objects
- off_sessionboolean
- price_dataobject
- proration_datetimestamp
- tax_ratesarray of strings

#### billing_thresholdsobject

#### discountsarray of objects

#### off_sessionboolean

#### price_dataobject

#### proration_datetimestamp

#### tax_ratesarray of strings

### Returns

```
curlhttps://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{"order_id":"6735"},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{"order_id":"6735"},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

# Retrieve a subscription item
Retrieves the subscription item with the given ID.

### Parameters
Noparameters.

### Returns
Returns a subscription item if a valid subscription item ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```

```
{"id":"si_NcLYdDxLHxlFo7","object":"subscription_item","created":1680126546,"custom_fields":{},"price":{"id":"price_1Mr6rdLkdIwHu7ixwPmiybbR","object":"price","active":true,"billing_scheme":"per_unit","created":1680126545,"currency_code":"usd","custom_unit_amount":null,"discounts":null,"livemode":false,"lookup_key":null,"custom_fields":{},"nickname":null,"product":"prod_NcLYGKH0eY5b8s","recurring":{"interval":"month","interval_count":1,"trial_period_days":null,"usage_type":"licensed"},"tax_behavior":"unspecified","tiers_mode":null,"transform_quantity":null,"type":"recurring","unit_amount":1000,"unit_amount_decimal":"1000"},"quantity":2,"subscription":"sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd","tax_rates":[]}
```