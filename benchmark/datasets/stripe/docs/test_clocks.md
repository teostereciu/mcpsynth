# test_clocks

*Source: https://docs.stripe.com/api/test_clocks*

---

# Test ClocksTest helper
A test clock enables deterministic control over objects in testmode. With a test clock, you can createobjects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances,you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

# The Test Clock objectTest helper

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- deletes_aftertimestampTime at which this clock is scheduled to auto delete.
- frozen_timetimestampTime at which all objects belonging to this clock are frozen.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- namenullablestringThe custom name supplied at creation.
- statusenumThe status of the Test Clock.Possible enum valuesadvancingIn the process of advancing time for the test clock objects.internal_failureFailed to advance time. Future requests to advance time will fail.readyAll test clock objects have advanced to thefrozen_time.
- status_detailsobjectDetails on the current state of the Test Clock.Show child attributes

#### idstring

#### objectstring

#### createdtimestamp

#### deletes_aftertimestamp

#### frozen_timetimestamp

#### livemodeboolean

#### namenullablestring

#### statusenum

[TABLE]
advancingIn the process of advancing time for the test clock objects.
internal_failureFailed to advance time. Future requests to advance time will fail.
readyAll test clock objects have advanced to thefrozen_time.
[/TABLE]

```
internal_failure
```

#### status_detailsobject

```
{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}
```

```
{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}
```

# Create a test clockTest helper
Creates a new test clock that can be attached to new customers and quotes.

### Parameters
- frozen_timetimestampRequiredThe initial frozen time for this test clock.
- namestringThe name for this test clock.The maximum length is 300 characters.

#### frozen_timetimestampRequired

#### namestring

### Returns
The newly createdTestClockobject is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/test_helpers/test_clocks \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d frozen_time=1577836800
```

```
curlhttps://api.stripe.com/v1/test_helpers/test_clocks \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d frozen_time=1577836800
```

```
{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}
```

```
{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}
```

# Retrieve a test clockTest helper
Retrieves a test clock.

### Parameters
Noparameters.

### Returns
Returns theTestClockobject. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}
```

```
{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}
```

# List all test clocksTest helper
Returns a list of your test clocks.

### Parameters
Noparameters.

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimittest clocks, starting afterstarting_after. Each entry in the array is a separate test clock object. If no more test clocks are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/test_helpers/test_clocks \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/test_helpers/test_clocks \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/test_helpers/test_clocks","has_more":false,"data":[{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}]}
```

```
{"object":"list","url":"/v1/test_helpers/test_clocks","has_more":false,"data":[{"id":"clock_1Mr3I22eZvKYlo2Ck0rgMqd7","object":"test_helpers.test_clock","created":1680112806,"deletes_after":1680717606,"frozen_time":1577836800,"livemode":false,"name":null,"status":"ready"}]}
```