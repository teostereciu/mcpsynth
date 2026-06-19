# customer_portal/configurations

*Source: https://docs.stripe.com/api/customer_portal/configurations*

---

# Customer Portal Configuration
A portal configuration describes the functionality and behavior you embed in a portal session. Related guide:Configure the customer_id portal.

# The Customer portal configuration object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- activebooleanWhether the configuration is active and can be used to create portal sessions.
- applicationnullablestringExpandableConnect onlyID of the Connect Application that created the configuration.
- business_profileobjectThe business information shown to customers in the portal.Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- default_return_urlnullablestringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can beoverridenwhen creating the session.
- featuresobjectInformation about the features available in the portal.Show child attributes
- is_defaultbooleanWhether the configuration is the default. Iftrue, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in ourintegration docs.Show child attributes
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namenullablestringThe name of the configuration.
- updatedtimestampTime at which the object was last updated. Measured in seconds since the Unix epoch.

#### idstring

#### objectstring

#### activeboolean

#### applicationnullablestringExpandableConnect only

#### business_profileobject

#### createdtimestamp

#### default_return_urlnullablestring

#### featuresobject

#### is_defaultboolean

#### livemodeboolean

#### login_pageobject

#### metadatanullableobject

#### namenullablestring

#### updatedtimestamp

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":null,"terms_of_service_url":null},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1680290736}
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":null,"terms_of_service_url":null},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1680290736}
```

# Create a portal configuration
Creates a configuration that describes the functionality and behavior of a PortalSession

### Parameters
- featuresobjectRequiredInformation about the features available in the portal.Show child parameters
- business_profileobjectThe business information shown to customers in the portal.Show child parameters
- default_return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can beoverridenwhen creating the session.
- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in ourintegration docs.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringThe name of the configuration.The maximum length is 256 characters.

#### featuresobjectRequired

#### business_profileobject

#### default_return_urlstring

#### login_pageobject

#### metadataobject

#### namestring

### Returns
Returns a portal configuration object.

```
curlhttps://api.stripe.com/v1/billing_portal/configurations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"features[customer_update][allowed_updates][]"=email \-d"features[customer_update][allowed_updates][]"=tax_id \-d"features[customer_update][enabled]"=true \-d"features[invoice_history][enabled]"=true
```

```
curlhttps://api.stripe.com/v1/billing_portal/configurations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"features[customer_update][allowed_updates][]"=email \-d"features[customer_update][allowed_updates][]"=tax_id \-d"features[customer_update][enabled]"=true \-d"features[invoice_history][enabled]"=true
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":null,"terms_of_service_url":null},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1680290736}
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":null,"terms_of_service_url":null},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1680290736}
```

# Update a portal configuration
Updates a configuration that describes the functionality of the customer_id portal.

### Parameters
- activebooleanWhether the configuration is active and can be used to create portal sessions.
- business_profileobjectThe business information shown to customers in the portal.Show child parameters
- default_return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can beoverridenwhen creating the session.
- featuresobjectInformation about the features available in the portal.Show child parameters
- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in ourintegration docs.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringThe name of the configuration.The maximum length is 256 characters.

#### activeboolean

#### business_profileobject

#### default_return_urlstring

#### featuresobject

#### login_pageobject

#### metadataobject

#### namestring

### Returns
Returns a portal configuration object.

```
curlhttps://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\--data-urlencode"business_profile[privacy_policy_url]"="https://example.com/new_privacy_url"\--data-urlencode"business_profile[terms_of_service_url]"="https://example.com/new_terms_of_service_url"
```

```
curlhttps://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\--data-urlencode"business_profile[privacy_policy_url]"="https://example.com/new_privacy_url"\--data-urlencode"business_profile[terms_of_service_url]"="https://example.com/new_terms_of_service_url"
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":"https://example.com/new_privacy_url","terms_of_service_url":"https://example.com/new_terms_of_service_url"},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1688593779}
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":"https://example.com/new_privacy_url","terms_of_service_url":"https://example.com/new_terms_of_service_url"},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1688593779}
```

# Retrieve a portal configuration
Retrieves a configuration that describes the functionality of the customer_id portal.

### Parameters
Noparameters.

### Returns
Returns a portal configuration object.

```
curlhttps://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":null,"terms_of_service_url":null},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1680290736}
```

```
{"id":"bpc_1MrnZsLkdIwHu7ixNiQL1xPM","object":"billing_portal.configuration","active":true,"application":null,"business_profile":{"headline":null,"privacy_policy_url":null,"terms_of_service_url":null},"created":1680290736,"default_return_url":null,"features":{"customer_update":{"allowed_updates":["email","tax_id"],"enabled":true},"invoice_history":{"enabled":true},"payment_method_update":{"enabled":false},"subscription_cancel":{"cancellation_reason":{"enabled":false,"options":["too_expensive","missing_features","switched_service","unused","other"]},"enabled":false,"mode":"at_period_end","proration_behavior":"none"},"subscription_update":{"default_allowed_updates":[],"enabled":false,"proration_behavior":"none"}},"is_default":false,"livemode":false,"login_page":{"enabled":false,"url":null},"custom_fields":{},"updated":1680290736}
```