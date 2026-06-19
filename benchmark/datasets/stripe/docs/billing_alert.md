# billing/alert

*Source: https://docs.stripe.com/api/billing/alert*

---

# Alerts
A billing alert is a resource that notifies you when a certain usage threshold on a meter is crossed. For example, you might create a billing alert to notify you when a certain user made 100 API requests.

# The Alert object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- alert_typeenumDefines the type of the alert.Possible enum valuesusage_thresholdUseusage_thresholdif you intend for an alert to fire when a usage threshold on a meter is crossed.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- statusnullableenumStatus of the alert. This can be active, inactive or archived.
- titlestringTitle of the alert.
- usage_thresholdnullableobjectEncapsulates configuration of the alert to monitor usage on a specificBilling Meter.Show child attributes

#### idstring

#### objectstring

#### alert_typeenum

[TABLE]
usage_thresholdUseusage_thresholdif you intend for an alert to fire when a usage threshold on a meter is crossed.
[/TABLE]

```
usage_threshold
```

#### livemodeboolean

#### statusnullableenum

#### titlestring

#### usage_thresholdnullableobject

```
{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"}
```

```
{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"}
```

# Create a billing alert
Creates a billing alert

### Parameters
- alert_typeenumRequiredThe type of alert to create.Possible enum valuesusage_thresholdUseusage_thresholdif you intend for an alert to fire when a usage threshold on a meter is crossed.
- titlestringRequiredThe title of the alert.The maximum length is 256 characters.
- usage_thresholdobjectThe configuration of the usage threshold.Show child parameters

#### alert_typeenumRequired

[TABLE]
usage_thresholdUseusage_thresholdif you intend for an alert to fire when a usage threshold on a meter is crossed.
[/TABLE]

```
usage_threshold
```

#### titlestringRequired

#### usage_thresholdobject

### Returns
Returns a billing alert

```
curlhttps://api.stripe.com/v1/billing/alerts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d title="API Request usage alert"\-d alert_type=usage_threshold \-d"usage_threshold[gte]"=10000 \-d"usage_threshold[meter]"=mtr_12345 \-d"usage_threshold[recurrence]"=one_time
```

```
curlhttps://api.stripe.com/v1/billing/alerts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d title="API Request usage alert"\-d alert_type=usage_threshold \-d"usage_threshold[gte]"=10000 \-d"usage_threshold[meter]"=mtr_12345 \-d"usage_threshold[recurrence]"=one_time
```

```
{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"}
```

```
{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"}
```

# Retrieve a billing alert
Retrieves a billing alert given an ID

### Parameters
Noparameters.

### Returns
Returns the alert

```
curlhttps://api.stripe.com/v1/billing/alerts/alrt_12345 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/billing/alerts/alrt_12345 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"}
```

```
{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"}
```

# List billing alerts
Lists billing active and inactive alerts

### Parameters
- alert_typeenumFilter results to only include this type of alert.Possible enum valuesusage_thresholdUseusage_thresholdif you intend for an alert to fire when a usage threshold on a meter is crossed.
- meterstringFilter results to only include alerts with the given meter.

#### alert_typeenum

[TABLE]
usage_thresholdUseusage_thresholdif you intend for an alert to fire when a usage threshold on a meter is crossed.
[/TABLE]

```
usage_threshold
```

#### meterstring

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Returns a list of billing alerts

```
curlhttps://api.stripe.com/v1/billing/alerts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/billing/alerts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"data":[{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"},{"id":"alrt_67890","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":120,"meter":"mtr_67890","recurrence":"one_time"},"status":"active"}]}
```

```
{"data":[{"id":"alrt_12345","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":10000,"meter":"mtr_12345","recurrence":"one_time"},"status":"active"},{"id":"alrt_67890","object":"billing.alert","title":"API Request usage alert","livemode":true,"alert_type":"usage_threshold","usage_threshold":{"gte":120,"meter":"mtr_67890","recurrence":"one_time"},"status":"active"}]}
```