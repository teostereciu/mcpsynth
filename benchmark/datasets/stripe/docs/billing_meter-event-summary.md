# billing/meter-event-summary

*Source: https://docs.stripe.com/api/billing/meter-event-summary*

---

# Meter Event Summary
A billing meter event summary represents an aggregated view of a customer’s billing meter events within a specified timeframe. It indicates how muchusage was accrued by a customer for that period.
Note: Meters events are aggregated asynchronously so the meter event summaries provide an eventually consistent view of the reported usage.

# The Meter Event Summary object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- aggregated_valuefloatAggregated value of all the events withinstart_time(inclusive) andend_time(inclusive). The aggregation strategy is defined on meter viadefault_aggregation.
- end_timetimestampEnd timestamp for this event summary (exclusive). Must be aligned with minute boundaries.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- meterstringThe meter associated with this event summary.
- start_timetimestampStart timestamp for this event summary (inclusive). Must be aligned with minute boundaries.

#### idstring

#### objectstring

#### aggregated_valuefloat

#### end_timetimestamp

#### livemodeboolean

#### meterstring

#### start_timetimestamp

```
{"id":"mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy","object":"billing.meter_event_summary","aggregated_value":10,"end_time":1711659600,"livemode":false,"meter":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","start_time":1711656000}
```

```
{"id":"mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy","object":"billing.meter_event_summary","aggregated_value":10,"end_time":1711659600,"livemode":false,"meter":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","start_time":1711656000}
```

# List billing meter event summaries
Retrieve a list of billing meter event summaries.

### Parameters
- customerstringRequiredThe customer for which to fetch event summaries.
- end_timetimestampRequiredThe timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.
- idstringRequiredUnique identifier for the object.
- start_timetimestampRequiredThe timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.
- value_grouping_windowenumSpecifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, …, 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC).Possible enum valuesdayGenerate event summaries per day.hourGenerate event summaries per hour.

#### customerstringRequired

#### end_timetimestampRequired

#### idstringRequired

#### start_timetimestampRequired

#### value_grouping_windowenum

[TABLE]
dayGenerate event summaries per day.
hourGenerate event summaries per hour.
[/TABLE]

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Returns a list of billing meter event summaries.

```
curl-G https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA/event_summaries \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_Pp40waj64hdRxb \-d start_time=1711584000 \-d end_time=1711666800 \-d value_grouping_window=hour
```

```
curl-G https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA/event_summaries \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_Pp40waj64hdRxb \-d start_time=1711584000 \-d end_time=1711666800 \-d value_grouping_window=hour
```

```
{"object":"list","data":[{"id":"mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xl3bk3Cy3Cy","object":"billing.meter_event_summary","aggregated_value":15,"end_time":1711663200,"livemode":false,"meter":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","start_time":1711659600},{"id":"mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy","object":"billing.meter_event_summary","aggregated_value":10,"end_time":1711659600,"livemode":false,"meter":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","start_time":1711656000}],"has_more":false,"url":"/v1/billing/meters/:id/event_summaries"}
```

```
{"object":"list","data":[{"id":"mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xl3bk3Cy3Cy","object":"billing.meter_event_summary","aggregated_value":15,"end_time":1711663200,"livemode":false,"meter":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","start_time":1711659600},{"id":"mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy","object":"billing.meter_event_summary","aggregated_value":10,"end_time":1711659600,"livemode":false,"meter":"mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA","start_time":1711656000}],"has_more":false,"url":"/v1/billing/meters/:id/event_summaries"}
```