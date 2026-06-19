# v2/meter-events

*Source: https://docs.stripe.com/api/v2/meter-events*

---

# Meter Eventsv2
Meter events are used to report customer usage of your product or service. Meter events are associated with billing meters, which define the shape of the event’s payload and how those events are aggregated. Meter events are processed asynchronously, so they may not be immediately reflected in aggregates or on upcoming invoices.

# The Meter Event objectv2

### Attributes
- objectstring, value is "v2.billing.meter_event"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampThe creation time of this meter event.
- event_namestringThe name of the meter event. Corresponds with theevent_namefield on a meter.
- identifierstringA unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- payloadmapThe payload of the event. This must contain the fields corresponding to a meter’scustomer_mapping.event_payload_key(default isstripe_customer_id) andvalue_settings.event_payload_key(default isvalue). Read more aboutthepayload…
- timestamptimestampThe time of the event. Must be within the past 35 calendar days or up to5 minutes in the future. Defaults to current timestamp if not specified.

#### objectstring, value is "v2.billing.meter_event"

#### createdtimestamp

#### event_namestring

#### identifierstring

#### livemodeboolean

#### payloadmap

#### timestamptimestamp

```
{"object":"v2.billing.meter_event","created":"2024-06-01T12:10:00.000Z","livemode":false,"identifier":"idmp_12345678","event_name":"ai_search_api","timestamp":"2024-06-01T12:00:00.000Z","payload":{"stripe_customer_id":"cus_12345678","value":"25"}}
```

```
{"object":"v2.billing.meter_event","created":"2024-06-01T12:10:00.000Z","livemode":false,"identifier":"idmp_12345678","event_name":"ai_search_api","timestamp":"2024-06-01T12:00:00.000Z","payload":{"stripe_customer_id":"cus_12345678","value":"25"}}
```

# Create a Meter Event with synchronous validationv2
Creates a meter event. Events are validated synchronously, but are processed asynchronously. Supports up to 1,000 events per second in livemode. For higher rate-limits, please use meter event streams instead.

### Parameters
- event_namestringRequiredThe name of the meter event. Corresponds with theevent_namefield on a meter.
- payloadmapRequiredThe payload of the event. This must contain the fields corresponding to a meter’scustomer_mapping.event_payload_key(default isstripe_customer_id) andvalue_settings.event_payload_key(default isvalue). Read more aboutthepayload.
- identifierstringA unique identifier for the event. If not provided, one will be generated.We recommend using a globally unique identifier for this. We’ll enforceuniqueness within a rolling 24 hour period.
- timestamptimestampThe time of the event. Must be within the past 35 calendar days or up to5 minutes in the future. Defaults to current timestamp if not specified.

#### event_namestringRequired

#### payloadmapRequired

#### identifierstring

#### timestamptimestamp

### Returns

### Response attributes
- objectstring, value is "v2.billing.meter_event"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampThe creation time of this meter event.
- event_namestringThe name of the meter event. Corresponds with theevent_namefield on a meter.
- identifierstringA unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We’ll enforce uniqueness within a rolling 24 hour period.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- payloadmapThe payload of the event. This must contain the fields corresponding to a meter’scustomer_mapping.event_payload_key(default isstripe_customer_id) andvalue_settings.event_payload_key(default isvalue). Read more aboutthepayload…
- timestamptimestampThe time of the event. Must be within the past 35 calendar days or up to5 minutes in the future. Defaults to current timestamp if not specified.

#### objectstring, value is "v2.billing.meter_event"

#### createdtimestamp

#### event_namestring

#### identifierstring

#### livemodeboolean

#### payloadmap

#### timestamptimestamp
The meter must be Active to submit events.
A meter event with a duplicate identifier has already been submitted.
A meter must exist to submit events.
The value must be a positive integer.
The payload must have a reference to the customer.
The payload must have a value.
Cannot create multiple usage events for the same customer, meter concurrently.

```
curl-X POST https://api.stripe.com/v2/billing/meter_events \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"identifier": "idmp_12345678","event_name": "ai_search_api","timestamp": "2024-06-01T12:00:00.000Z","payload": {"stripe_customer_id": "cus_12345678","value": "25"}}'
```

```
curl-X POST https://api.stripe.com/v2/billing/meter_events \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"identifier": "idmp_12345678","event_name": "ai_search_api","timestamp": "2024-06-01T12:00:00.000Z","payload": {"stripe_customer_id": "cus_12345678","value": "25"}}'
```

```
{"object":"v2.billing.meter_event","created":"2024-06-01T12:10:00.000Z","livemode":false,"identifier":"idmp_12345678","event_name":"ai_search_api","timestamp":"2024-06-01T12:00:00.000Z","payload":{"stripe_customer_id":"cus_12345678","value":"25"}}
```

```
{"object":"v2.billing.meter_event","created":"2024-06-01T12:10:00.000Z","livemode":false,"identifier":"idmp_12345678","event_name":"ai_search_api","timestamp":"2024-06-01T12:00:00.000Z","payload":{"stripe_customer_id":"cus_12345678","value":"25"}}
```