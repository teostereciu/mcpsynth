# webhook_endpoints

*Source: https://docs.stripe.com/api/webhook_endpoints*

---

# Webhook Endpoints
You can configurewebhook endpointsvia the API to benotified about events that happen in your Stripe account or connectedaccounts.
Most users configure webhooks fromthe dashboard, which provides a user interface for registering and testing your webhook endpoints.
Related guide:Setting up webhooks

# The Webhook Endpoint object

### Attributes
- idstringUnique identifier for the object.
- api_versionnullablestringThe API version events are rendered as for this webhook endpoint.
- descriptionnullablestringAn optional description of what the webhook is used for.
- enabled_eventsarray of stringsThe list of events to enable for this endpoint.['*']indicates that all events are enabled, except those that require explicit selection.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- secretstringThe endpoint’s secret, used to generatewebhook signatures. Only returned at creation.
- statusstringThe status of the webhook. It can beenabledordisabled.
- urlstringThe URL of the webhook endpoint.

#### idstring

#### api_versionnullablestring

#### descriptionnullablestring

#### enabled_eventsarray of strings

#### metadataobject

#### secretstring

#### statusstring

#### urlstring

### More attributesExpand all
- objectstring
- applicationnullablestring
- createdtimestamp
- livemodeboolean

#### objectstring

#### applicationnullablestring

#### createdtimestamp

#### livemodeboolean

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"secret":"whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z","status":"enabled","url":"https://example.com/my/webhook/endpoint"}
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"secret":"whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z","status":"enabled","url":"https://example.com/my/webhook/endpoint"}
```

# Create a webhook endpoint
A webhook endpoint must have aurland a list ofenabled_events. You may optionally specify the Booleanconnectparameter. If set to true, then a Connect webhook endpoint that notifies the specifiedurlabout events from all connected accounts is created; otherwise an account webhook endpoint that notifies the specifiedurlonly about events from your account is created. You can also create webhook endpoints in thewebhooks settingssection of the Dashboard.

### Parameters
- enabled_eventsarray of enumsRequiredThe list of events to enable for this endpoint. You may specify['*']to enable all events, except those that require explicit selection.Possible enum valuesaccount.application.authorizedOccurs whenever a user authorizes an application. Sent to the related application only.account.application.deauthorizedOccurs whenever a user deauthorizes an application. Sent to the related application only.account.external_account.createdOccurs whenever an external account is created.account.external_account.deletedOccurs whenever an external account is deleted.account.external_account.updatedOccurs whenever an external account is updated.account.updatedOccurs whenever an account status or property has changed.application_fee.createdOccurs whenever an application fee is created on a charge.application_fee.refund.updatedOccurs whenever an application fee refund is updated.application_fee.refundedOccurs whenever an application fee is refunded, whether from refunding a charge or fromrefunding the application fee directly. This includes partial refunds.balance.availableOccurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.Show 214 more
- urlstringRequiredThe URL of the webhook endpoint.
- api_versionstringEvents sent to this endpoint will be generated with this Stripe Version instead of your account’s default Stripe Version.
- descriptionstringAn optional description of what the webhook is used for.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### enabled_eventsarray of enumsRequired

[TABLE]
account.application.authorizedOccurs whenever a user authorizes an application. Sent to the related application only.
account.application.deauthorizedOccurs whenever a user deauthorizes an application. Sent to the related application only.
account.external_account.createdOccurs whenever an external account is created.
account.external_account.deletedOccurs whenever an external account is deleted.
account.external_account.updatedOccurs whenever an external account is updated.
account.updatedOccurs whenever an account status or property has changed.
application_fee.createdOccurs whenever an application fee is created on a charge.
application_fee.refund.updatedOccurs whenever an application fee refund is updated.
application_fee.refundedOccurs whenever an application fee is refunded, whether from refunding a charge or fromrefunding the application fee directly. This includes partial refunds.
balance.availableOccurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.
Show 214 more
[/TABLE]

```
account.application.authorized
```

```
account.application.deauthorized
```

```
account.external_account.created
```

```
account.external_account.deleted
```

```
account.external_account.updated
```

```
account.updated
```

```
application_fee.created
```

```
application_fee.refund.updated
```

```
application_fee.refunded
```

```
balance.available
```

#### urlstringRequired

#### api_versionstring

#### descriptionstring

#### metadataobject

### More parametersExpand all
- connectboolean

#### connectboolean

### Returns
Returns the webhook endpoint object with thesecretfield populated.

```
curlhttps://api.stripe.com/v1/webhook_endpoints \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"enabled_events[]"="charge.succeeded"\-d"enabled_events[]"="charge.failed"\--data-urlencode url="https://example.com/my/webhook/endpoint"
```

```
curlhttps://api.stripe.com/v1/webhook_endpoints \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"enabled_events[]"="charge.succeeded"\-d"enabled_events[]"="charge.failed"\--data-urlencode url="https://example.com/my/webhook/endpoint"
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"secret":"whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z","status":"enabled","url":"https://example.com/my/webhook/endpoint"}
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"secret":"whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z","status":"enabled","url":"https://example.com/my/webhook/endpoint"}
```

# Update a webhook endpoint
Updates the webhook endpoint. You may edit theurl, the list ofenabled_events, and the status of your endpoint.

### Parameters
- descriptionstringAn optional description of what the webhook is used for.
- enabled_eventsarray of enumsThe list of events to enable for this endpoint. You may specify['*']to enable all events, except those that require explicit selection.Possible enum valuesaccount.application.authorizedOccurs whenever a user authorizes an application. Sent to the related application only.account.application.deauthorizedOccurs whenever a user deauthorizes an application. Sent to the related application only.account.external_account.createdOccurs whenever an external account is created.account.external_account.deletedOccurs whenever an external account is deleted.account.external_account.updatedOccurs whenever an external account is updated.account.updatedOccurs whenever an account status or property has changed.application_fee.createdOccurs whenever an application fee is created on a charge.application_fee.refund.updatedOccurs whenever an application fee refund is updated.application_fee.refundedOccurs whenever an application fee is refunded, whether from refunding a charge or fromrefunding the application fee directly. This includes partial refunds.balance.availableOccurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.Show 214 more
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- urlstringThe URL of the webhook endpoint.

#### descriptionstring

#### enabled_eventsarray of enums

[TABLE]
account.application.authorizedOccurs whenever a user authorizes an application. Sent to the related application only.
account.application.deauthorizedOccurs whenever a user deauthorizes an application. Sent to the related application only.
account.external_account.createdOccurs whenever an external account is created.
account.external_account.deletedOccurs whenever an external account is deleted.
account.external_account.updatedOccurs whenever an external account is updated.
account.updatedOccurs whenever an account status or property has changed.
application_fee.createdOccurs whenever an application fee is created on a charge.
application_fee.refund.updatedOccurs whenever an application fee refund is updated.
application_fee.refundedOccurs whenever an application fee is refunded, whether from refunding a charge or fromrefunding the application fee directly. This includes partial refunds.
balance.availableOccurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.
Show 214 more
[/TABLE]

```
account.application.authorized
```

```
account.application.deauthorized
```

```
account.external_account.created
```

```
account.external_account.deleted
```

```
account.external_account.updated
```

```
account.updated
```

```
application_fee.created
```

```
application_fee.refund.updated
```

```
application_fee.refunded
```

```
balance.available
```

#### metadataobject

#### urlstring

### More parametersExpand all
- disabledboolean

#### disabledboolean

### Returns
The updated webhook endpoint object if successful. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"enabled_events[]"="charge.succeeded"\-d"enabled_events[]"="charge.failed"\--data-urlencode url="https://example.com/new_endpoint"
```

```
curlhttps://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"enabled_events[]"="charge.succeeded"\-d"enabled_events[]"="charge.failed"\--data-urlencode url="https://example.com/new_endpoint"
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"status":"disabled","url":"https://example.com/new_endpoint"}
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"status":"disabled","url":"https://example.com/new_endpoint"}
```

# Retrieve a webhook endpoint
Retrieves the webhook endpoint with the given ID.

### Parameters
Noparameters.

### Returns
Returns a webhook endpoint if a valid webhook endpoint ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"status":"enabled","url":"https://example.com/my/webhook/endpoint"}
```

```
{"id":"we_1Mr5jULkdIwHu7ix1ibLTM0x","object":"webhook_endpoint","api_version":null,"application":null,"created":1680122196,"description":null,"enabled_events":["charge.succeeded","charge.failed"],"livemode":false,"metadata":{},"status":"enabled","url":"https://example.com/my/webhook/endpoint"}
```