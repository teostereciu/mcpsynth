# billing/meter-event-adjustment

*Source: https://docs.stripe.com/api/billing/meter-event-adjustment*

---

# Meter Event Adjustment
A billing meter event adjustment is a resource that allows you to cancel a meter event. For example, you might create a billing meter event adjustment to cancel a meter event that was created in error or attached to the wrong customer.

# The Meter Event Adjustment object

### Attributes
- objectstringString representing the object’s type. Objects of the same type share the same value.
- cancelnullableobjectSpecifies which event to cancel.Show child attributes
- event_namestringThe name of the meter event. Corresponds with theevent_namefield on a meter.The maximum length is 100 characters.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- statusenumThe meter event adjustment’s status.Possible enum valuescompleteThe event adjustment has been processed.pendingThe event adjustment is still being processed.
- typeenumSpecifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.Possible enum valuescancelCancel a single meter event by identifier.

#### objectstring

#### cancelnullableobject

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
{"object":"billing.meter_event_adjustment","livemode":false,"status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"identifier_123"}}
```

```
{"object":"billing.meter_event_adjustment","livemode":false,"status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"identifier_123"}}
```

# Create a billing meter event adjustment
Creates a billing meter event adjustment.

### Parameters
- event_namestringRequiredThe name of the meter event. Corresponds with theevent_namefield on a meter.The maximum length is 100 characters.
- typeenumRequiredSpecifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.Possible enum valuescancelCancel a single meter event by identifier.
- cancelobjectSpecifies which event to cancel.Show child parameters

#### event_namestringRequired

#### typeenumRequired

[TABLE]
cancelCancel a single meter event by identifier.
[/TABLE]

#### cancelobject

### Returns
Returns a billing meter event adjustment.

```
curlhttps://api.stripe.com/v1/billing/meter_event_adjustments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=cancel \-d event_name=ai_search_api \-d"cancel[identifier]"=identifier_123
```

```
curlhttps://api.stripe.com/v1/billing/meter_event_adjustments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=cancel \-d event_name=ai_search_api \-d"cancel[identifier]"=identifier_123
```

```
{"object":"billing.meter_event_adjustment","livemode":false,"status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"identifier_123"}}
```

```
{"object":"billing.meter_event_adjustment","livemode":false,"status":"pending","event_name":"ai_search_api","type":"cancel","cancel":{"identifier":"identifier_123"}}
```