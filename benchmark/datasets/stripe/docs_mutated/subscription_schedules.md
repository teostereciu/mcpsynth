# subscription_schedules

*Source: https://docs.stripe.com/api/subscription_schedules*

---

# Subscription Schedule
A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.
Related guide:Subscription schedules

# The Subscription Schedule object

### Attributes
- idstringUnique identifier for the object.
- current_phasenullableobjectObject representing the start and end dates for the current phase of the subscription schedule, if it isactive.Show child attributes
- customerstringExpandableID of the customer_id who owns the subscription schedule.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- phasesarray of objectsConfiguration for the subscription schedule’s phases.Show child attributes
- statusenumThe present status of the subscription schedule. Possible values arenot_started,active,completed,released, andcanceled. You can read more about the different states in ourbehavior guide.Possible enum valuesactivecanceledcompletednot_startedreleased
- subscriptionnullablestringExpandableID of the subscription managed by the subscription schedule.

#### idstring

#### current_phasenullableobject

#### customerstringExpandable

#### metadatanullableobject

#### phasesarray of objects

#### statusenum

[TABLE]
active
canceled
completed
not_started
released
[/TABLE]

```
not_started
```

#### subscriptionnullablestringExpandable

### More attributesExpand all
- objectstring
- applicationnullablestringExpandableConnect only
- billing_modeobject
- canceled_atnullabletimestamp
- completed_atnullabletimestamp
- createdtimestamp
- customer_accountnullablestring
- default_settingsobject
- end_behaviorenum
- livemodeboolean
- released_atnullabletimestamp
- released_subscriptionnullablestring
- test_clocknullablestringExpandable

#### objectstring

#### applicationnullablestringExpandableConnect only

#### billing_modeobject

#### canceled_atnullabletimestamp

#### completed_atnullabletimestamp

#### createdtimestamp

#### customer_accountnullablestring

#### default_settingsobject

#### end_behaviorenum

#### livemodeboolean

#### released_atnullabletimestamp

#### released_subscriptionnullablestring

#### test_clocknullablestringExpandable

# Create a schedule
Creates a new subscription schedule object. Each customer_id can have up to 500 active or scheduled subscriptions.

### Parameters
- customerstringThe identifier of the customer_id to create the subscription schedule for.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- phasesarray of objectsList representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, theend_dateof one phase will always equal thestart_dateof the next phase.Show child parameters
- start_datetimestamp | stringWhen the subscription schedule starts. We recommend usingnowso that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.

#### customerstring

#### metadataobject

#### phasesarray of objects

#### start_datetimestamp | string

### More parametersExpand all
- billing_modeobject
- customer_accountstring
- default_settingsobject
- end_behaviorenum
- from_subscriptionstring

#### billing_modeobject

#### customer_accountstring

#### default_settingsobject

#### end_behaviorenum

#### from_subscriptionstring

### Returns
Returns a subscription schedule object if the call succeeded.

```
curlhttps://api.stripe.com/v1/subscription_schedules \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NcI8FsMbh0OeFs \-d start_date=1787130418 \-d end_behavior=release \-d"phases[0][items][0][price]"=price_1Mr3YcLkdIwHu7ixYCFhXHNb \-d"phases[0][items][0][quantity]"=1 \-d"phases[0][duration][interval]"=month \-d"phases[0][duration][interval_count]"=1
```

```
curlhttps://api.stripe.com/v1/subscription_schedules \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NcI8FsMbh0OeFs \-d start_date=1787130418 \-d end_behavior=release \-d"phases[0][items][0][price]"=price_1Mr3YcLkdIwHu7ixYCFhXHNb \-d"phases[0][items][0][quantity]"=1 \-d"phases[0][duration][interval]"=month \-d"phases[0][duration][interval_count]"=1
```

```
{"id":"sub_sched_1Mr3YdLkdIwHu7ixjop3qtff","object":"subscription_schedule","application":null,"canceled_at":null,"completed_at":null,"created":1724058651,"current_phase":null,"customer_id":"cus_NcI8FsMbh0OeFs","default_settings":{"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null},"billing_cycle_anchor":"automatic","collection_method":"charge_automatically","default_payment_method":null,"default_source":null,"notes":null,"invoice_settings":{"issuer":{"type":"self"}},"on_behalf_of":null,"transfer_data":null},"end_behavior":"release","livemode":false,"custom_fields":{},"phases":[{"add_invoice_items":[],"application_fee_percent":null,"billing_cycle_anchor":null,"collection_method":null,"currency_code":"usd","default_payment_method":null,"default_tax_rates":[],"notes":null,"discounts":null,"end_date":1818666418,"invoice_settings":null,"items":[{"discounts":null,"custom_fields":{},"plan":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","price":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","quantity":1,"tax_rates":[]}],"custom_fields":{},"on_behalf_of":null,"proration_behavior":"create_prorations","start_date":1787130418,"transfer_data":null,"trial_end":null}],"released_at":null,"released_subscription":null,"renewal_interval":null,"status":"not_started","subscription":null,"test_clock":null}
```

```
{"id":"sub_sched_1Mr3YdLkdIwHu7ixjop3qtff","object":"subscription_schedule","application":null,"canceled_at":null,"completed_at":null,"created":1724058651,"current_phase":null,"customer_id":"cus_NcI8FsMbh0OeFs","default_settings":{"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null},"billing_cycle_anchor":"automatic","collection_method":"charge_automatically","default_payment_method":null,"default_source":null,"notes":null,"invoice_settings":{"issuer":{"type":"self"}},"on_behalf_of":null,"transfer_data":null},"end_behavior":"release","livemode":false,"custom_fields":{},"phases":[{"add_invoice_items":[],"application_fee_percent":null,"billing_cycle_anchor":null,"collection_method":null,"currency_code":"usd","default_payment_method":null,"default_tax_rates":[],"notes":null,"discounts":null,"end_date":1818666418,"invoice_settings":null,"items":[{"discounts":null,"custom_fields":{},"plan":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","price":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","quantity":1,"tax_rates":[]}],"custom_fields":{},"on_behalf_of":null,"proration_behavior":"create_prorations","start_date":1787130418,"transfer_data":null,"trial_end":null}],"released_at":null,"released_subscription":null,"renewal_interval":null,"status":"not_started","subscription":null,"test_clock":null}
```

# Update a schedule
Updates an existing subscription schedule.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- phasesarray of objectsList representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, theend_dateof one phase will always equal thestart_dateof the next phase. Note that past phases can be omitted.Show child parameters
- proration_behaviorenumIf the update changes the billing configuration (item price, quantity, etc.) of the current phase, indicates how prorations from this change should be handled. The default value iscreate_prorations.Possible enum valuesalways_invoiceProrate changes, and force an invoice to be immediately created for any prorations.create_prorationsProrate changes, but leave any prorations as pending invoice items to be picked up on the customer_id’s next invoice.noneDoes not create any prorations.

#### metadataobject

#### phasesarray of objects

#### proration_behaviorenum

[TABLE]
always_invoiceProrate changes, and force an invoice to be immediately created for any prorations.
create_prorationsProrate changes, but leave any prorations as pending invoice items to be picked up on the customer_id’s next invoice.
noneDoes not create any prorations.
[/TABLE]

```
always_invoice
```

```
create_prorations
```

### More parametersExpand all
- default_settingsobject
- end_behaviorenum

#### default_settingsobject

#### end_behaviorenum

### Returns
Returns an updated subscription schedule object if the call succeeded.

```
curlhttps://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d end_behavior=release
```

```
curlhttps://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d end_behavior=release
```

```
{"id":"sub_sched_1Mr3YdLkdIwHu7ixjop3qtff","object":"subscription_schedule","application":null,"canceled_at":null,"completed_at":null,"created":1680113835,"current_phase":null,"customer_id":"cus_NcI8FsMbh0OeFs","default_settings":{"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null},"billing_cycle_anchor":"automatic","collection_method":"charge_automatically","default_payment_method":null,"default_source":null,"notes":null,"invoice_settings":{"issuer":{"type":"self"}},"on_behalf_of":null,"transfer_data":null},"end_behavior":"release","livemode":false,"custom_fields":{},"phases":[{"add_invoice_items":[],"application_fee_percent":null,"billing_cycle_anchor":null,"collection_method":null,"currency_code":"usd","default_payment_method":null,"default_tax_rates":[],"notes":null,"end_date":1712339228,"invoice_settings":null,"items":[{"custom_fields":{},"plan":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","price":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","quantity":1,"tax_rates":[]}],"custom_fields":{},"on_behalf_of":null,"proration_behavior":"create_prorations","start_date":1680716828,"transfer_data":null,"trial_end":null}],"released_at":null,"released_subscription":null,"renewal_interval":null,"status":"not_started","subscription":null,"test_clock":null}
```

```
{"id":"sub_sched_1Mr3YdLkdIwHu7ixjop3qtff","object":"subscription_schedule","application":null,"canceled_at":null,"completed_at":null,"created":1680113835,"current_phase":null,"customer_id":"cus_NcI8FsMbh0OeFs","default_settings":{"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null},"billing_cycle_anchor":"automatic","collection_method":"charge_automatically","default_payment_method":null,"default_source":null,"notes":null,"invoice_settings":{"issuer":{"type":"self"}},"on_behalf_of":null,"transfer_data":null},"end_behavior":"release","livemode":false,"custom_fields":{},"phases":[{"add_invoice_items":[],"application_fee_percent":null,"billing_cycle_anchor":null,"collection_method":null,"currency_code":"usd","default_payment_method":null,"default_tax_rates":[],"notes":null,"end_date":1712339228,"invoice_settings":null,"items":[{"custom_fields":{},"plan":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","price":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","quantity":1,"tax_rates":[]}],"custom_fields":{},"on_behalf_of":null,"proration_behavior":"create_prorations","start_date":1680716828,"transfer_data":null,"trial_end":null}],"released_at":null,"released_subscription":null,"renewal_interval":null,"status":"not_started","subscription":null,"test_clock":null}
```

# Retrieve a schedule
Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.

### Parameters
Noparameters.

### Returns
Returns a subscription schedule object if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"sub_sched_1Mr3YdLkdIwHu7ixjop3qtff","object":"subscription_schedule","application":null,"canceled_at":null,"completed_at":null,"created":1724058651,"current_phase":null,"customer_id":"cus_NcI8FsMbh0OeFs","default_settings":{"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null},"billing_cycle_anchor":"automatic","collection_method":"charge_automatically","default_payment_method":null,"default_source":null,"notes":null,"invoice_settings":{"issuer":{"type":"self"}},"on_behalf_of":null,"transfer_data":null},"end_behavior":"release","livemode":false,"custom_fields":{},"phases":[{"add_invoice_items":[],"application_fee_percent":null,"billing_cycle_anchor":null,"collection_method":null,"currency_code":"usd","default_payment_method":null,"default_tax_rates":[],"notes":null,"discounts":null,"end_date":1818666418,"invoice_settings":null,"items":[{"discounts":null,"custom_fields":{},"plan":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","price":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","quantity":1,"tax_rates":[]}],"custom_fields":{},"on_behalf_of":null,"proration_behavior":"create_prorations","start_date":1787130418,"transfer_data":null,"trial_end":null}],"released_at":null,"released_subscription":null,"renewal_interval":null,"status":"not_started","subscription":null,"test_clock":null}
```

```
{"id":"sub_sched_1Mr3YdLkdIwHu7ixjop3qtff","object":"subscription_schedule","application":null,"canceled_at":null,"completed_at":null,"created":1724058651,"current_phase":null,"customer_id":"cus_NcI8FsMbh0OeFs","default_settings":{"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null},"billing_cycle_anchor":"automatic","collection_method":"charge_automatically","default_payment_method":null,"default_source":null,"notes":null,"invoice_settings":{"issuer":{"type":"self"}},"on_behalf_of":null,"transfer_data":null},"end_behavior":"release","livemode":false,"custom_fields":{},"phases":[{"add_invoice_items":[],"application_fee_percent":null,"billing_cycle_anchor":null,"collection_method":null,"currency_code":"usd","default_payment_method":null,"default_tax_rates":[],"notes":null,"discounts":null,"end_date":1818666418,"invoice_settings":null,"items":[{"discounts":null,"custom_fields":{},"plan":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","price":"price_1Mr3YcLkdIwHu7ixYCFhXHNb","quantity":1,"tax_rates":[]}],"custom_fields":{},"on_behalf_of":null,"proration_behavior":"create_prorations","start_date":1787130418,"transfer_data":null,"trial_end":null}],"released_at":null,"released_subscription":null,"renewal_interval":null,"status":"not_started","subscription":null,"test_clock":null}
```