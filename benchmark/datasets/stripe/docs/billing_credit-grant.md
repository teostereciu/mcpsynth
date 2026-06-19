# billing/credit-grant

*Source: https://docs.stripe.com/api/billing/credit-grant*

---

# Credit Grant
A credit grant is an API resource that documents the allocation of some billing credits to a customer.
Related guide:Billing credits

# The Credit Grant object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountobjectAmount of this credit grant.Show child attributes
- applicability_configobjectConfiguration specifying what this credit grant applies to. We currently only supportmeteredprices that have aBilling Meterattached to them.Show child attributes
- categoryenumThe category of this credit grant. This is for tracking purposes and isn’t displayed to the customer.Possible enum valuespaidThe credit grant was purchased by the customer for some amount.promotionalThe credit grant was given to the customer for free.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- customerstringExpandableID of the customer receiving the billing credits.
- customer_accountnullablestringID of the account representing the customer receiving the billing credits
- effective_atnullabletimestampThe time when the billing credits become effective-when they’re eligible for use.
- expires_atnullabletimestampThe time when the billing credits expire. If not present, the billing credits don’t expire.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namenullablestringA descriptive name shown in dashboard.
- prioritynullableintegerPreview featureThe priority for applying this credit grant. The highest priority is 0 and the lowest is 100.
- test_clocknullablestringExpandableID of the test clock this credit grant belongs to.
- updatedtimestampTime at which the object was last updated. Measured in seconds since the Unix epoch.
- voided_atnullabletimestampThe time when this credit grant was voided. If not present, the credit grant hasn’t been voided.

#### idstring

#### objectstring

#### amountobject

#### applicability_configobject

#### categoryenum

[TABLE]
paidThe credit grant was purchased by the customer for some amount.
promotionalThe credit grant was given to the customer for free.
[/TABLE]

```
promotional
```

#### createdtimestamp

#### customerstringExpandable

#### customer_accountnullablestring

#### effective_atnullabletimestamp

#### expires_atnullabletimestamp

#### livemodeboolean

#### metadataobject

#### namenullablestring

#### prioritynullableintegerPreview feature

#### test_clocknullablestringExpandable

#### updatedtimestamp

#### voided_atnullabletimestamp

```
{"id":"credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726620803,"customer":"cus_QrvQguzkIK8zTj","effective_at":1729297860,"expires_at":null,"livemode":false,"metadata":{},"name":"Purchased Credits","priority":50,"test_clock":null,"updated":1726620803,"voided_at":null}
```

```
{"id":"credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726620803,"customer":"cus_QrvQguzkIK8zTj","effective_at":1729297860,"expires_at":null,"livemode":false,"metadata":{},"name":"Purchased Credits","priority":50,"test_clock":null,"updated":1726620803,"voided_at":null}
```

# Create a credit grant
Creates a credit grant.

### Parameters
- amountobjectRequiredAmount of this credit grant.Show child parameters
- applicability_configobjectRequiredConfiguration specifying what this credit grant applies to. We currently only supportmeteredprices that have aBilling Meterattached to them.Show child parameters
- categoryenumThe category of this credit grant. It defaults topaidif not specified.Possible enum valuespaidThe credit grant was purchased by the customer for some amount.promotionalThe credit grant was given to the customer for free.
- customerstringID of the customer receiving the billing credits.
- customer_accountstringID of the account representing the customer receiving the billing credits.
- effective_attimestampThe time when the billing credits become effective-when they’re eligible for use. It defaults to the current timestamp if not specified.
- expires_attimestampThe time when the billing credits expire. If not specified, the billing credits don’t expire.
- metadataobjectSet of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
- namestringA descriptive name shown in the Dashboard.The maximum length is 100 characters.
- priorityintegerPreview featureThe desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.

#### amountobjectRequired

#### applicability_configobjectRequired

#### categoryenum

[TABLE]
paidThe credit grant was purchased by the customer for some amount.
promotionalThe credit grant was given to the customer for free.
[/TABLE]

```
promotional
```

#### customerstring

#### customer_accountstring

#### effective_attimestamp

#### expires_attimestamp

#### metadataobject

#### namestring

#### priorityintegerPreview feature

### Returns
Returns a credit grant.

```
curlhttps://api.stripe.com/v1/billing/credit_grants \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Purchased Credits"\-d customer=cus_QrvQguzkIK8zTj \-d"amount[monetary][currency]"=usd \-d"amount[monetary][value]"=1000 \-d"amount[type]"=monetary \-d"applicability_config[scope][price_type]"=metered \-d category=paid
```

```
curlhttps://api.stripe.com/v1/billing/credit_grants \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Purchased Credits"\-d customer=cus_QrvQguzkIK8zTj \-d"amount[monetary][currency]"=usd \-d"amount[monetary][value]"=1000 \-d"amount[type]"=monetary \-d"applicability_config[scope][price_type]"=metered \-d category=paid
```

```
{"id":"credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726620803,"customer":"cus_QrvQguzkIK8zTj","effective_at":1729297860,"expires_at":null,"livemode":false,"metadata":{},"name":"Purchased Credits","priority":null,"test_clock":null,"updated":1726620803}
```

```
{"id":"credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726620803,"customer":"cus_QrvQguzkIK8zTj","effective_at":1729297860,"expires_at":null,"livemode":false,"metadata":{},"name":"Purchased Credits","priority":null,"test_clock":null,"updated":1726620803}
```

# Update a credit grant
Updates a credit grant.

### Parameters
- idstringRequiredUnique identifier for the object.
- expires_attimestampThe time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.
- metadataobjectSet of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.

#### idstringRequired

#### expires_attimestamp

#### metadataobject

### Returns
Returns the updated credit grant.

```
curlhttps://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[cost_basis]"="0.9"\-d expires_at=1759302000
```

```
curlhttps://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[cost_basis]"="0.9"\-d expires_at=1759302000
```

```
{"id":"credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726688933,"customer":"cus_QsEHa3GKweMwih","effective_at":1726688933,"expires_at":1759302000,"livemode":false,"metadata":{"cost_basis":"0.9"},"name":"Purchased Credits","priority":50,"test_clock":null,"updated":1726688977,"voided_at":null}
```

```
{"id":"credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726688933,"customer":"cus_QsEHa3GKweMwih","effective_at":1726688933,"expires_at":1759302000,"livemode":false,"metadata":{"cost_basis":"0.9"},"name":"Purchased Credits","priority":50,"test_clock":null,"updated":1726688977,"voided_at":null}
```

# Retrieve a credit grant
Retrieves a credit grant.

### Parameters
- idstringRequiredUnique identifier for the object.

#### idstringRequired

### Returns
Returns a credit grant.

```
curlhttps://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726620803,"customer":"cus_QrvQguzkIK8zTj","effective_at":1729297860,"expires_at":null,"livemode":false,"metadata":{},"name":"Purchased Credits","priority":50,"test_clock":null,"updated":1726620803}
```

```
{"id":"credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo","object":"billing.credit_grant","amount":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"applicability_config":{"scope":{"price_type":"metered"}},"category":"paid","created":1726620803,"customer":"cus_QrvQguzkIK8zTj","effective_at":1729297860,"expires_at":null,"livemode":false,"metadata":{},"name":"Purchased Credits","priority":50,"test_clock":null,"updated":1726620803}
```