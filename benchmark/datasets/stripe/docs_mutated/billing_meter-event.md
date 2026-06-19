# billing/meter-event

*Source: https://docs.stripe.com/api/billing/meter-event*

---

# Meter Events
Meter events represent actions that customers take in your system. You can use meter events to bill a customer_id based on their usage. Meter events are associated with billing meters, which define both the contents of the event’s payload and how to aggregate those events.

# The Meter Event object

### Attributes
- objectstringString representing the object’s type. Objects of the same type share the same value.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- event_namestringThe name of the meter event. Corresponds with theevent_namefield on a meter.The maximum length is 100 characters.
- identifierstringA unique identifier for the event.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- payloadobjectThe payload of the event. This contains the fields corresponding to a meter’scustomer_mapping.event_payload_key(default isstripe_customer_id) andvalue_settings.event_payload_key(default isvalue). Read more about thepayload.
- timestamptimestampThe timestamp passed in when creating the event. Measured in seconds since the Unix epoch.

#### objectstring

#### createdtimestamp

#### event_namestring

#### identifierstring

#### livemodeboolean

#### payloadobject

#### timestamptimestamp

```
{"object":"billing.meter_event","created":1704824589,"event_name":"ai_search_api","identifier":"identifier_123","livemode":true,"payload":{"value":"25","stripe_customer_id":"cus_NciAYcXfLnqBoz"},"timestamp":1680210639}
```

```
{"object":"billing.meter_event","created":1704824589,"event_name":"ai_search_api","identifier":"identifier_123","livemode":true,"payload":{"value":"25","stripe_customer_id":"cus_NciAYcXfLnqBoz"},"timestamp":1680210639}
```

# Create a billing meter event
Creates a billing meter event.

### Parameters
- event_namestringRequiredThe name of the meter event. Corresponds with theevent_namefield on a meter.The maximum length is 100 characters.
- payloadobjectRequiredThe payload of the event. This must contain the fields corresponding to a meter’scustomer_mapping.event_payload_key(default isstripe_customer_id) andvalue_settings.event_payload_key(default isvalue). Read more about thepayload.
- identifierstringA unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.The maximum length is 100 characters.
- timestamptimestampThe time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.

#### event_namestringRequired

#### payloadobjectRequired

#### identifierstring

#### timestamptimestamp

### Returns
Returns a billing meter event.

```
curlhttps://api.stripe.com/v1/billing/meter_events \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d event_name=ai_search_api \-d"payload[value]"=25 \-d"payload[stripe_customer_id]"=cus_NciAYcXfLnqBoz \-d identifier=identifier_123
```

```
curlhttps://api.stripe.com/v1/billing/meter_events \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d event_name=ai_search_api \-d"payload[value]"=25 \-d"payload[stripe_customer_id]"=cus_NciAYcXfLnqBoz \-d identifier=identifier_123
```

```
{"object":"billing.meter_event","created":1704824589,"event_name":"ai_search_api","identifier":"identifier_123","livemode":true,"payload":{"value":"25","stripe_customer_id":"cus_NciAYcXfLnqBoz"},"timestamp":1680210639}
```

```
{"object":"billing.meter_event","created":1704824589,"event_name":"ai_search_api","identifier":"identifier_123","livemode":true,"payload":{"value":"25","stripe_customer_id":"cus_NciAYcXfLnqBoz"},"timestamp":1680210639}
```