# v2/billing/meter-event-adjustments

*Source: https://docs.stripe.com/api/v2/billing/meter-event-adjustments*

---

# Meter Event Adjustmentsv2
A billing meter event adjustment is a resource that allows you to cancel a meter event. For example, you might create a billing meter event adjustment to cancel a meter event that was created in error or attached to the wrong customer_id.

# The Meter Event Adjustment objectv2

### Attributes
- idstringThe unique id of this meter event adjustment.
- objectstring, value is "v2.billing.meter_event_adjustment"String representing the object’s type. Objects of the same type share the same value of the object field.
- cancelobjectSpecifies which event to cancel.Show child attributes
- createdtimestampThe time the adjustment was created.
- event_namestringThe name of the meter event. Corresponds with theevent_namefield on a meter.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- statusenumThe meter event adjustment’s status.Possible enum valuescompleteThe event adjustment has been processed.pendingThe event adjustment is still being processed.
- typeenumSpecifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.Possible enum valuescancelCancel a single meter event by identifier.

#### idstring

#### objectstring, value is "v2.billing.meter_event_adjustment"

#### cancelobject

#### createdtimestamp

#### event_namestring

#### livemodeboolean

#### statusenum

[TABLE]
completeThe event adjustment has been processed.
pendingThe event adjustment is still being processed.
[/TABLE]

#### typeenum

[TABLE]
cancelCancel a single meter event by identifier.
[/TABLE]

```
{"object":"v2.billing.meter_event_adjustment","id":"mtr_event_adj_12345678","livemode":false,"created":"2024-06-01T12:00:00.000Z","status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"idmp_12345678"}}
```

```
{"object":"v2.billing.meter_event_adjustment","id":"mtr_event_adj_12345678","livemode":false,"created":"2024-06-01T12:00:00.000Z","status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"idmp_12345678"}}
```

# Create a Meter Event Adjustmentv2
Creates a meter event adjustment to cancel a previously sent meter event.

### Parameters
- cancelobjectRequiredSpecifies which event to cancel.Show child parameters
- event_namestringRequiredThe name of the meter event. Corresponds with theevent_namefield on a meter.
- typeenumRequiredSpecifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.Possible enum valuescancelCancel a single meter event by identifier.

#### cancelobjectRequired

#### event_namestringRequired

#### typeenumRequired

[TABLE]
cancelCancel a single meter event by identifier.
[/TABLE]

### Returns

### Response attributes
- idstringThe unique id of this meter event adjustment.
- objectstring, value is "v2.billing.meter_event_adjustment"String representing the object’s type. Objects of the same type share the same value of the object field.
- cancelobjectSpecifies which event to cancel.Show child attributes
- createdtimestampThe time the adjustment was created.
- event_namestringThe name of the meter event. Corresponds with theevent_namefield on a meter.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- statusenumThe meter event adjustment’s status.Possible enum valuescompleteThe event adjustment has been processed.pendingThe event adjustment is still being processed.
- typeenumSpecifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.Possible enum valuescancelCancel a single meter event by identifier.

#### idstring

#### objectstring, value is "v2.billing.meter_event_adjustment"

#### cancelobject

#### createdtimestamp

#### event_namestring

#### livemodeboolean

#### statusenum

[TABLE]
completeThe event adjustment has been processed.
pendingThe event adjustment is still being processed.
[/TABLE]

#### typeenum

[TABLE]
cancelCancel a single meter event by identifier.
[/TABLE]
The adjustment configuration is invalid for the adjustment type.

```
curl-X POST https://api.stripe.com/v2/billing/meter_event_adjustments \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"event_name": "ai_search_api","type": "cancel","cancel": {"identifier": "idmp_12345678"}}'
```

```
curl-X POST https://api.stripe.com/v2/billing/meter_event_adjustments \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"event_name": "ai_search_api","type": "cancel","cancel": {"identifier": "idmp_12345678"}}'
```

```
{"object":"v2.billing.meter_event_adjustment","id":"mtr_event_adj_12345678","livemode":false,"created":"2024-06-01T12:00:00.000Z","status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"idmp_12345678"}}
```

```
{"object":"v2.billing.meter_event_adjustment","id":"mtr_event_adj_12345678","livemode":false,"created":"2024-06-01T12:00:00.000Z","status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"idmp_12345678"}}
```