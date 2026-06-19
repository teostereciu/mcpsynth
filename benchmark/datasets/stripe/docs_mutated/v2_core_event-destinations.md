# v2/core/event-destinations

*Source: https://docs.stripe.com/api/v2/core/event-destinations*

---

# Event Destinationsv2
Set up an event destination to receive events from Stripe across multiple destination types, includingwebhook endpointsandAmazon EventBridge. Event destinations support receivingthin eventsandsnapshot events.

# The Event Destination objectv2

### Attributes
- idstringUnique identifier for the object.
- objectstring, value is "v2.core.event_destination"String representing the object’s type. Objects of the same type share the same value of the object field.
- amazon_eventbridgenullableobjectAmazon EventBridge configuration.Show child attributes
- createdtimestampTime at which the object was created.
- descriptionstringAn optional notes of what the event destination is used for.
- enabled_eventsarray of stringsThe list of events to enable for this endpoint.
- event_payloadenumPayload type of events being subscribed to.Possible enum valuessnapshotEvents from v1 APIs.thinEvents from v2 APIs.
- events_fromnullablearray of enumsWhere events should be routed from.Possible enum valuesother_accountsReceive events from accounts connected to the account that owns the event destination.selfReceive events from the account that owns the event destination.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapMetadata.
- namestringEvent destination name.
- snapshot_api_versionnullablestringIf using the snapshot event payload, the API version events are rendered as.
- statusenumStatus. It can be set to either enabled or disabled.Possible enum valuesdisabledEvent destination is disabled.enabledEvent destination is enabled.
- status_detailsnullableobjectAdditional information about event destination status.Show child attributes
- typeenumEvent destination type.Possible enum valuesamazon_eventbridgeAmazon EventBridge.webhook_endpointWebhook endpoint.
- updatedtimestampTime at which the object was last updated.
- webhook_endpointnullableobjectWebhook endpoint configuration.Show child attributes

#### idstring

#### objectstring, value is "v2.core.event_destination"

#### amazon_eventbridgenullableobject

#### createdtimestamp

#### descriptionstring

#### enabled_eventsarray of strings

#### event_payloadenum

[TABLE]
snapshotEvents from v1 APIs.
thinEvents from v2 APIs.
[/TABLE]

#### events_fromnullablearray of enums

[TABLE]
other_accountsReceive events from accounts connected to the account that owns the event destination.
selfReceive events from the account that owns the event destination.
[/TABLE]

```
other_accounts
```

#### livemodeboolean

#### metadatanullablemap

#### namestring

#### snapshot_api_versionnullablestring

#### statusenum

[TABLE]
disabledEvent destination is disabled.
enabledEvent destination is enabled.
[/TABLE]

#### status_detailsnullableobject

#### typeenum

[TABLE]
amazon_eventbridgeAmazon EventBridge.
webhook_endpointWebhook endpoint.
[/TABLE]

```
amazon_eventbridge
```

```
webhook_endpoint
```

#### updatedtimestamp

#### webhook_endpointnullableobject

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"This is my event destination, I like it a lot","enabled_events":["v1.billing.meter.error_report_triggered"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"enabled","status_details":null,"type":"webhook_endpoint","updated":"2024-10-22T16:20:09.937Z","webhook_endpoint":{"signing_secret":null,"url":"https://example.com/my/webhook/endpoint"}}
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"This is my event destination, I like it a lot","enabled_events":["v1.billing.meter.error_report_triggered"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"enabled","status_details":null,"type":"webhook_endpoint","updated":"2024-10-22T16:20:09.937Z","webhook_endpoint":{"signing_secret":null,"url":"https://example.com/my/webhook/endpoint"}}
```

# Create an Event Destinationv2
Create a new event destination.

### Parameters
- enabled_eventsarray of stringsRequiredThe list of events to enable for this endpoint.
- event_payloadenumRequiredPayload type of events being subscribed to.Possible enum valuessnapshotEvents from v1 APIs.thinEvents from v2 APIs.
- namestringRequiredEvent destination name.
- typeenumRequiredEvent destination type.Possible enum valuesamazon_eventbridgeAmazon EventBridge.webhook_endpointWebhook endpoint.
- amazon_eventbridgeobjectAmazon EventBridge configuration.Show child parameters
- descriptionstringAn optional notes of what the event destination is used for.
- events_fromarray of enumsWhere events should be routed from.Possible enum valuesother_accountsReceive events from accounts connected to the account that owns the event destination.selfReceive events from the account that owns the event destination.
- includearray of enumsAdditional fields to include in the response.Possible enum valueswebhook_endpoint.signing_secretInclude parameter to exposewebhook_endpoint.signing_secret.webhook_endpoint.urlInclude parameter to exposewebhook_endpoint.url.
- metadatamapMetadata.
- snapshot_api_versionstringIf using the snapshot event payload, the API version events are rendered as.
- webhook_endpointobjectWebhook endpoint configuration.Show child parameters

#### enabled_eventsarray of stringsRequired

#### event_payloadenumRequired

[TABLE]
snapshotEvents from v1 APIs.
thinEvents from v2 APIs.
[/TABLE]

#### namestringRequired

#### typeenumRequired

[TABLE]
amazon_eventbridgeAmazon EventBridge.
webhook_endpointWebhook endpoint.
[/TABLE]

```
amazon_eventbridge
```

```
webhook_endpoint
```

#### amazon_eventbridgeobject

#### descriptionstring

#### events_fromarray of enums

[TABLE]
other_accountsReceive events from accounts connected to the account that owns the event destination.
selfReceive events from the account that owns the event destination.
[/TABLE]

```
other_accounts
```

#### includearray of enums

[TABLE]
webhook_endpoint.signing_secretInclude parameter to exposewebhook_endpoint.signing_secret.
webhook_endpoint.urlInclude parameter to exposewebhook_endpoint.url.
[/TABLE]

```
webhook_endpoint.signing_secret
```

```
webhook_endpoint.url
```

#### metadatamap

#### snapshot_api_versionstring

#### webhook_endpointobject

### Returns

### Response attributes
- idstringUnique identifier for the object.
- objectstring, value is "v2.core.event_destination"String representing the object’s type. Objects of the same type share the same value of the object field.
- amazon_eventbridgenullableobjectAmazon EventBridge configuration.Show child attributes
- createdtimestampTime at which the object was created.
- descriptionstringAn optional notes of what the event destination is used for.
- enabled_eventsarray of stringsThe list of events to enable for this endpoint.
- event_payloadenumPayload type of events being subscribed to.Possible enum valuessnapshotEvents from v1 APIs.thinEvents from v2 APIs.
- events_fromnullablearray of enumsWhere events should be routed from.Possible enum valuesother_accountsReceive events from accounts connected to the account that owns the event destination.selfReceive events from the account that owns the event destination.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapMetadata.
- namestringEvent destination name.
- snapshot_api_versionnullablestringIf using the snapshot event payload, the API version events are rendered as.
- statusenumStatus. It can be set to either enabled or disabled.Possible enum valuesdisabledEvent destination is disabled.enabledEvent destination is enabled.
- status_detailsnullableobjectAdditional information about event destination status.Show child attributes
- typeenumEvent destination type.Possible enum valuesamazon_eventbridgeAmazon EventBridge.webhook_endpointWebhook endpoint.
- updatedtimestampTime at which the object was last updated.
- webhook_endpointnullableobjectWebhook endpoint configuration.Show child attributes

#### idstring

#### objectstring, value is "v2.core.event_destination"

#### amazon_eventbridgenullableobject

#### createdtimestamp

#### descriptionstring

#### enabled_eventsarray of strings

#### event_payloadenum

[TABLE]
snapshotEvents from v1 APIs.
thinEvents from v2 APIs.
[/TABLE]

#### events_fromnullablearray of enums

[TABLE]
other_accountsReceive events from accounts connected to the account that owns the event destination.
selfReceive events from the account that owns the event destination.
[/TABLE]

```
other_accounts
```

#### livemodeboolean

#### metadatanullablemap

#### namestring

#### snapshot_api_versionnullablestring

#### statusenum

[TABLE]
disabledEvent destination is disabled.
enabledEvent destination is enabled.
[/TABLE]

#### status_detailsnullableobject

#### typeenum

[TABLE]
amazon_eventbridgeAmazon EventBridge.
webhook_endpointWebhook endpoint.
[/TABLE]

```
amazon_eventbridge
```

```
webhook_endpoint
```

#### updatedtimestamp

#### webhook_endpointnullableobject
An idempotent retry occurred with different request parameters.

```
curl-X POST https://api.stripe.com/v2/core/event_destinations \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"name": "My Event Destination","notes": "This is my event destination, I like it a lot","enabled_events": ["v1.billing.meter.error_report_triggered"],"type": "webhook_endpoint","webhook_endpoint": {"url": "https://example.com/my/webhook/endpoint"},"event_payload": "thin","include": ["webhook_endpoint.url"]}'
```

```
curl-X POST https://api.stripe.com/v2/core/event_destinations \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"name": "My Event Destination","notes": "This is my event destination, I like it a lot","enabled_events": ["v1.billing.meter.error_report_triggered"],"type": "webhook_endpoint","webhook_endpoint": {"url": "https://example.com/my/webhook/endpoint"},"event_payload": "thin","include": ["webhook_endpoint.url"]}'
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"This is my event destination, I like it a lot","enabled_events":["v1.billing.meter.error_report_triggered"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"enabled","status_details":null,"type":"webhook_endpoint","updated":"2024-10-22T16:20:09.937Z","webhook_endpoint":{"signing_secret":null,"url":"https://example.com/my/webhook/endpoint"}}
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"This is my event destination, I like it a lot","enabled_events":["v1.billing.meter.error_report_triggered"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"enabled","status_details":null,"type":"webhook_endpoint","updated":"2024-10-22T16:20:09.937Z","webhook_endpoint":{"signing_secret":null,"url":"https://example.com/my/webhook/endpoint"}}
```

# Update an Event Destinationv2
Update the details of an event destination.

### Parameters
- idstringRequiredIdentifier for the event destination to update.
- descriptionstringAn optional notes of what the event destination is used for.
- enabled_eventsarray of stringsThe list of events to enable for this endpoint.
- includearray of enumsAdditional fields to include in the response. Currently supportswebhook_endpoint.url.Possible enum valueswebhook_endpoint.urlInclude parameter to exposewebhook_endpoint.url.
- metadatamapMetadata.
- namestringEvent destination name.
- webhook_endpointobjectWebhook endpoint configuration.Show child parameters

#### idstringRequired

#### descriptionstring

#### enabled_eventsarray of strings

#### includearray of enums

[TABLE]
webhook_endpoint.urlInclude parameter to exposewebhook_endpoint.url.
[/TABLE]

```
webhook_endpoint.url
```

#### metadatamap

#### namestring

#### webhook_endpointobject

### Returns

### Response attributes
- idstringUnique identifier for the object.
- objectstring, value is "v2.core.event_destination"String representing the object’s type. Objects of the same type share the same value of the object field.
- amazon_eventbridgenullableobjectAmazon EventBridge configuration.Show child attributes
- createdtimestampTime at which the object was created.
- descriptionstringAn optional notes of what the event destination is used for.
- enabled_eventsarray of stringsThe list of events to enable for this endpoint.
- event_payloadenumPayload type of events being subscribed to.Possible enum valuessnapshotEvents from v1 APIs.thinEvents from v2 APIs.
- events_fromnullablearray of enumsWhere events should be routed from.Possible enum valuesother_accountsReceive events from accounts connected to the account that owns the event destination.selfReceive events from the account that owns the event destination.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapMetadata.
- namestringEvent destination name.
- snapshot_api_versionnullablestringIf using the snapshot event payload, the API version events are rendered as.
- statusenumStatus. It can be set to either enabled or disabled.Possible enum valuesdisabledEvent destination is disabled.enabledEvent destination is enabled.
- status_detailsnullableobjectAdditional information about event destination status.Show child attributes
- typeenumEvent destination type.Possible enum valuesamazon_eventbridgeAmazon EventBridge.webhook_endpointWebhook endpoint.
- updatedtimestampTime at which the object was last updated.
- webhook_endpointnullableobjectWebhook endpoint configuration.Show child attributes

#### idstring

#### objectstring, value is "v2.core.event_destination"

#### amazon_eventbridgenullableobject

#### createdtimestamp

#### descriptionstring

#### enabled_eventsarray of strings

#### event_payloadenum

[TABLE]
snapshotEvents from v1 APIs.
thinEvents from v2 APIs.
[/TABLE]

#### events_fromnullablearray of enums

[TABLE]
other_accountsReceive events from accounts connected to the account that owns the event destination.
selfReceive events from the account that owns the event destination.
[/TABLE]

```
other_accounts
```

#### livemodeboolean

#### metadatanullablemap

#### namestring

#### snapshot_api_versionnullablestring

#### statusenum

[TABLE]
disabledEvent destination is disabled.
enabledEvent destination is enabled.
[/TABLE]

#### status_detailsnullableobject

#### typeenum

[TABLE]
amazon_eventbridgeAmazon EventBridge.
webhook_endpointWebhook endpoint.
[/TABLE]

```
amazon_eventbridge
```

```
webhook_endpoint
```

#### updatedtimestamp

#### webhook_endpointnullableobject
The resource wasn’t found.
An idempotent retry occurred with different request parameters.

```
curl-X POST https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"notes": "A better notes","enabled_events": ["v1.billing.meter.error_report_triggered","v1.billing.meter.no_meter_found"],"include": ["webhook_endpoint.url"]}'
```

```
curl-X POST https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"notes": "A better notes","enabled_events": ["v1.billing.meter.error_report_triggered","v1.billing.meter.no_meter_found"],"include": ["webhook_endpoint.url"]}'
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"A better notes","enabled_events":["v1.billing.meter.error_report_triggered","v1.billing.meter.no_meter_found"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"disabled","status_details":{"disabled":{"reason":"user"}},"type":"webhook_endpoint","updated":"2024-10-22T16:25:48.976Z","webhook_endpoint":{"signing_secret":null,"url":"https://example.com/my/webhook/endpoint"}}
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"A better notes","enabled_events":["v1.billing.meter.error_report_triggered","v1.billing.meter.no_meter_found"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"disabled","status_details":{"disabled":{"reason":"user"}},"type":"webhook_endpoint","updated":"2024-10-22T16:25:48.976Z","webhook_endpoint":{"signing_secret":null,"url":"https://example.com/my/webhook/endpoint"}}
```

# Retrieve an Event Destinationv2
Retrieves the details of an event destination.

### Parameters
- idstringRequiredIdentifier for the event destination to retrieve.
- includearray of enumsAdditional fields to include in the response.Possible enum valueswebhook_endpoint.urlInclude parameter to exposewebhook_endpoint.url.

#### idstringRequired

#### includearray of enums

[TABLE]
webhook_endpoint.urlInclude parameter to exposewebhook_endpoint.url.
[/TABLE]

```
webhook_endpoint.url
```

### Returns

### Response attributes
- idstringUnique identifier for the object.
- objectstring, value is "v2.core.event_destination"String representing the object’s type. Objects of the same type share the same value of the object field.
- amazon_eventbridgenullableobjectAmazon EventBridge configuration.Show child attributes
- createdtimestampTime at which the object was created.
- descriptionstringAn optional notes of what the event destination is used for.
- enabled_eventsarray of stringsThe list of events to enable for this endpoint.
- event_payloadenumPayload type of events being subscribed to.Possible enum valuessnapshotEvents from v1 APIs.thinEvents from v2 APIs.
- events_fromnullablearray of enumsWhere events should be routed from.Possible enum valuesother_accountsReceive events from accounts connected to the account that owns the event destination.selfReceive events from the account that owns the event destination.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapMetadata.
- namestringEvent destination name.
- snapshot_api_versionnullablestringIf using the snapshot event payload, the API version events are rendered as.
- statusenumStatus. It can be set to either enabled or disabled.Possible enum valuesdisabledEvent destination is disabled.enabledEvent destination is enabled.
- status_detailsnullableobjectAdditional information about event destination status.Show child attributes
- typeenumEvent destination type.Possible enum valuesamazon_eventbridgeAmazon EventBridge.webhook_endpointWebhook endpoint.
- updatedtimestampTime at which the object was last updated.
- webhook_endpointnullableobjectWebhook endpoint configuration.Show child attributes

#### idstring

#### objectstring, value is "v2.core.event_destination"

#### amazon_eventbridgenullableobject

#### createdtimestamp

#### descriptionstring

#### enabled_eventsarray of strings

#### event_payloadenum

[TABLE]
snapshotEvents from v1 APIs.
thinEvents from v2 APIs.
[/TABLE]

#### events_fromnullablearray of enums

[TABLE]
other_accountsReceive events from accounts connected to the account that owns the event destination.
selfReceive events from the account that owns the event destination.
[/TABLE]

```
other_accounts
```

#### livemodeboolean

#### metadatanullablemap

#### namestring

#### snapshot_api_versionnullablestring

#### statusenum

[TABLE]
disabledEvent destination is disabled.
enabledEvent destination is enabled.
[/TABLE]

#### status_detailsnullableobject

#### typeenum

[TABLE]
amazon_eventbridgeAmazon EventBridge.
webhook_endpointWebhook endpoint.
[/TABLE]

```
amazon_eventbridge
```

```
webhook_endpoint
```

#### updatedtimestamp

#### webhook_endpointnullableobject
The resource wasn’t found.

```
curl-G https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\-d"include[0]"="webhook_endpoint.url"
```

```
curl-G https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\-d"include[0]"="webhook_endpoint.url"
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"This is my event destination, I like it a lot","enabled_events":["v1.billing.meter.error_report_triggered"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"disabled","status_details":{"disabled":{"reason":"user"}},"type":"webhook_endpoint","updated":"2024-10-22T16:22:02.524Z","webhook_endpoint":{"signing_secret":null,"url":null}}
```

```
{"id":"ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6","object":"v2.core.event_destination","created":"2024-10-22T16:20:09.931Z","notes":"This is my event destination, I like it a lot","enabled_events":["v1.billing.meter.error_report_triggered"],"event_payload":"thin","events_from":["self"],"livemode":false,"custom_fields":{},"name":"My Event Destination","snapshot_api_version":null,"status":"disabled","status_details":{"disabled":{"reason":"user"}},"type":"webhook_endpoint","updated":"2024-10-22T16:22:02.524Z","webhook_endpoint":{"signing_secret":null,"url":null}}
```