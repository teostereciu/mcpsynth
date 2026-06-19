# v2/meter-event-streams

*Source: https://docs.stripe.com/api/v2/meter-event-streams*

---

# Meter Event Streamsv2
You can send a higher-throughput of meter events using meter event streams. For this flow, you must first create a meter event session, which will provide you with a session token. You can then create meter events through the meter event stream endpoint, using the session token for authentication. The session tokens are short-lived and you will need to create a new meter event session when the token expires.

# The Meter Event Session objectv2

### Attributes
- idstringThe unique id of this auth session.
- objectstring, value is "v2.billing.meter_event_session"String representing the object’s type. Objects of the same type share the same value of the object field.
- authentication_tokenstringThe authentication token for this session.  Use this token when calling thehigh-throughput meter event API.
- createdtimestampThe creation time of this session.
- expires_attimestampThe time at which this session will expire.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.

#### idstring

#### objectstring, value is "v2.billing.meter_event_session"

#### authentication_tokenstring

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

```
{"id":"<AUTH_SESSION_ID>","livemode":"false","object":"v2.billing.meter_event_session","authentication_token":"token_12345678","created":"2024-06-01T12:00:00.000Z","expires_at":"2024-06-01T12:15:00.000Z"}
```

```
{"id":"<AUTH_SESSION_ID>","livemode":"false","object":"v2.billing.meter_event_session","authentication_token":"token_12345678","created":"2024-06-01T12:00:00.000Z","expires_at":"2024-06-01T12:15:00.000Z"}
```

# Create a Meter Event Stream Authentication Sessionv2
Creates a meter event session to send usage on the high-throughput meter event stream. Authentication tokens are only valid for 15 minutes, so you will need to create a new meter event session when your token expires.

### Parameters
Noparameters.

### Returns

### Response attributes
- idstringThe unique id of this auth session.
- objectstring, value is "v2.billing.meter_event_session"String representing the object’s type. Objects of the same type share the same value of the object field.
- authentication_tokenstringThe authentication token for this session.  Use this token when calling thehigh-throughput meter event API.
- createdtimestampThe creation time of this session.
- expires_attimestampThe time at which this session will expire.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.

#### idstring

#### objectstring, value is "v2.billing.meter_event_session"

#### authentication_tokenstring

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

```
curl-X POST https://api.stripe.com/v2/billing/meter_event_session \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
curl-X POST https://api.stripe.com/v2/billing/meter_event_session \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
{"id":"<AUTH_SESSION_ID>","livemode":"false","object":"v2.billing.meter_event_session","authentication_token":"token_12345678","created":"2024-06-01T12:00:00.000Z","expires_at":"2024-06-01T12:15:00.000Z"}
```

```
{"id":"<AUTH_SESSION_ID>","livemode":"false","object":"v2.billing.meter_event_session","authentication_token":"token_12345678","created":"2024-06-01T12:00:00.000Z","expires_at":"2024-06-01T12:15:00.000Z"}
```

# Create a Meter Event with asynchronous validationv2
Creates meter events. Events are processed asynchronously, including validation. Requires a meter event session for authentication. Supports up to 10,000 requests per second in livemode. For even higher rate-limits, contact sales.

### Parameters
- eventsarray of objectsRequiredList of meter events to include in the request. Supports up to 100 events per request.Show child parameters

#### eventsarray of objectsRequired

### Returns

### Response attributes
Noresponse attributes.
The temporary session token has expired.

```
curl-X POST https://meter-events.stripe.com/v2/billing/meter_event_stream \-H"Authorization: Bearer {{SESSION AUTH TOKEN}}"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"events": [{"identifier": "idmp_12345678","event_name": "ai_search_api","timestamp": "2024-06-01T12:00:00.000Z","payload": {"stripe_customer_id": "cus_12345678","value": "25"}}]}'
```

```
curl-X POST https://meter-events.stripe.com/v2/billing/meter_event_stream \-H"Authorization: Bearer {{SESSION AUTH TOKEN}}"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"events": [{"identifier": "idmp_12345678","event_name": "ai_search_api","timestamp": "2024-06-01T12:00:00.000Z","payload": {"stripe_customer_id": "cus_12345678","value": "25"}}]}'
```