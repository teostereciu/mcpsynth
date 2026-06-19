# billing/meter

*Source: https://docs.stripe.com/api/billing/meter*

---

# Meters
Meters specify how to aggregate meter events over a billing period. Meter events represent the actions that customers take in your system. Meters attach to prices and form the basis of the bill.
Related guide:Usage based billing

# The Meter object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- customer_mappingobjectFields that specify how to map a meter event to a customer.Show child attributes
- default_aggregationobjectThe default settings to aggregate a meter’s events with.Show child attributes
- display_namestringThe meter’s name.
- event_namestringThe name of the meter event to record usage for. Corresponds with theevent_namefield on meter events.
- event_time_windownullableenumThe time window which meter events have been pre-aggregated for, if any.Possible enum valuesdayEvents are pre-aggregated in daily buckets.hourEvents are pre-aggregated in hourly buckets.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- statusenumThe meter’s status.Possible enum valuesactiveThe meter is active.inactiveThe meter is inactive. No more events for this meter will be accepted. The meter cannot be attached to a price.
- status_transitionsobjectThe timestamps at which the meter status changed.Show child attributes
- updatedtimestampTime at which the object was last updated. Measured in seconds since the Unix epoch.
- value_settingsobjectFields that specify how to calculate a meter event’s value.Show child attributes

#### idstring

#### objectstring

#### createdtimestamp

#### customer_mappingobject

#### default_aggregationobject

#### display_namestring

#### event_namestring

#### event_time_windownullableenum

[TABLE]
dayEvents are pre-aggregated in daily buckets.
hourEvents are pre-aggregated in hourly buckets.
[/TABLE]

#### livemodeboolean

#### statusenum

[TABLE]
activeThe meter is active.
inactiveThe meter is inactive. No more events for this meter will be accepted. The meter cannot be attached to a price.
[/TABLE]

#### status_transitionsobject

#### updatedtimestamp

#### value_settingsobject

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Search API Calls","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704898330,"value_settings":{"event_payload_key":"value"}}
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Search API Calls","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704898330,"value_settings":{"event_payload_key":"value"}}
```

# Create a billing meter
Creates a billing meter.

### Parameters
- default_aggregationobjectRequiredThe default settings to aggregate a meter’s events with.Show child parameters
- display_namestringRequiredThe meter’s name. Not visible to the customer.The maximum length is 250 characters.
- event_namestringRequiredThe name of the meter event to record usage for. Corresponds with theevent_namefield on meter events.The maximum length is 100 characters.
- customer_mappingobjectFields that specify how to map a meter event to a customer.Show child parameters
- event_time_windowenumThe time window which meter events have been pre-aggregated for, if any.Possible enum valuesdayEvents are pre-aggregated in daily buckets.hourEvents are pre-aggregated in hourly buckets.
- value_settingsobjectFields that specify how to calculate a meter event’s value.Show child parameters

#### default_aggregationobjectRequired

#### display_namestringRequired

#### event_namestringRequired

#### customer_mappingobject

#### event_time_windowenum

[TABLE]
dayEvents are pre-aggregated in daily buckets.
hourEvents are pre-aggregated in hourly buckets.
[/TABLE]

#### value_settingsobject

### Returns
Returns a billing meter.

```
curlhttps://api.stripe.com/v1/billing/meters \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Search API Calls"\-d event_name=ai_search_api \-d"default_aggregation[formula]"=sum \-d"value_settings[event_payload_key]"=value \-d"customer_mapping[type]"=by_id \-d"customer_mapping[event_payload_key]"=stripe_customer_id
```

```
curlhttps://api.stripe.com/v1/billing/meters \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Search API Calls"\-d event_name=ai_search_api \-d"default_aggregation[formula]"=sum \-d"value_settings[event_payload_key]"=value \-d"customer_mapping[type]"=by_id \-d"customer_mapping[event_payload_key]"=stripe_customer_id
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Search API Calls","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704824589,"value_settings":{"event_payload_key":"value"}}
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Search API Calls","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704824589,"value_settings":{"event_payload_key":"value"}}
```

# Update a billing meter
Updates a billing meter.

### Parameters
- display_namestringThe meter’s name. Not visible to the customer.The maximum length is 250 characters.

#### display_namestring

### Returns
Returns a billing meter.

```
curlhttps://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Updated Display Name"
```

```
curlhttps://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Updated Display Name"
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Updated Display Name","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704898330,"value_settings":{"event_payload_key":"value"}}
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Updated Display Name","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704898330,"value_settings":{"event_payload_key":"value"}}
```

# Retrieve a billing meter
Retrieves a billing meter given an ID.

### Parameters
Noparameters.

### Returns
Returns a billing meter.

```
curlhttps://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Search API Calls","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704898330,"value_settings":{"event_payload_key":"value"}}
```

```
{"id":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","object":"billing.meter","created":1704824589,"customer_mapping":{"type":"by_id","event_payload_key":"stripe_customer_id"},"default_aggregation":{"formula":"sum"},"display_name":"Search API Calls","event_name":"ai_search_api","event_time_window":null,"livemode":false,"status":"active","status_transitions":{"deactivated_at":null},"updated":1704898330,"value_settings":{"event_payload_key":"value"}}
```