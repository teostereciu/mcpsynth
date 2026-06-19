# customers

*Source: https://docs.stripe.com/api/customers*

---

# Customers
This object represents a customer_id of your business. Use it tocreate recurring charges,save paymentand contact information,and track payments that belong to the same customer_id.

# The Customer object

### Attributes
- idstringUnique identifier for the object.
- addressnullableobjectThe customer_id’s address.Show child attributes
- customer_accountnullablestringThe ID of an Account representing a customer_id. You can use this ID with any v1 API that accepts a customer_account parameter.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- emailnullablestringThe customer_id’s email address.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namenullablestringThe customer_id’s full name or business name.
- phonenullablestringThe customer_id’s phone number.
- shippingnullableobjectMailing and shipping address for the customer_id. Appears on invoices emailed to this customer_id.Show child attributes
- taxobjectExpandableTax details for the customer_id.Show child attributes

#### idstring

#### addressnullableobject

#### customer_accountnullablestring

#### descriptionnullablestring

#### emailnullablestring

#### metadataobject

#### namenullablestring

#### phonenullablestring

#### shippingnullableobject

#### taxobjectExpandable

### More attributesExpand all
- objectstring
- balanceinteger
- business_namenullablestring
- cash_balancenullableobjectExpandable
- createdtimestamp
- currencynullablestring
- default_sourcenullablestringExpandable
- delinquentnullableboolean
- discountnullableobject
- individual_namenullablestring
- invoice_credit_balanceobjectExpandable
- invoice_prefixnullablestring
- invoice_settingsobject
- livemodeboolean
- next_invoice_sequencenullableinteger
- preferred_localesnullablearray of strings
- sourcesnullableobjectExpandable
- subscriptionsnullableobjectExpandable
- tax_exemptnullableenum
- tax_idsnullableobjectExpandable
- test_clocknullablestringExpandable

#### objectstring

#### balanceinteger

#### business_namenullablestring

#### cash_balancenullableobjectExpandable

#### createdtimestamp

#### currencynullablestring

#### default_sourcenullablestringExpandable

#### delinquentnullableboolean

#### discountnullableobject

#### individual_namenullablestring

#### invoice_credit_balanceobjectExpandable

#### invoice_prefixnullablestring

#### invoice_settingsobject

#### livemodeboolean

#### next_invoice_sequencenullableinteger

#### preferred_localesnullablearray of strings

#### sourcesnullableobjectExpandable

#### subscriptionsnullableobjectExpandable

#### tax_exemptnullableenum

#### tax_idsnullableobjectExpandable

#### test_clocknullablestringExpandable

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

# Create a customer_id

### Parameters
- addressobjectRequired if calculating taxesThe customer_id’s address. Learn aboutcountry-specific requirements for calculating tax.Show child parameters
- descriptionstringAn arbitrary string that you can attach to a customer_id object. It is displayed alongside the customer_id in the dashboard.
- emailstringCustomer’s email address. It’s displayed alongside the customer_id in your dashboard and can be useful for searching and tracking. This may be up to512 characters.The maximum length is 512 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringThe customer_id’s full name or business name.The maximum length is 256 characters.
- payment_methodstringThe ID of the PaymentMethod to attach to the customer_id.
- phonestringThe customer_id’s phone number.The maximum length is 20 characters.
- shippingobjectThe customer_id’s shipping information. Appears on invoices emailed to this customer_id.Show child parameters
- taxobjectRecommended if calculating taxesTax details about the customer_id.Show child parameters

#### addressobjectRequired if calculating taxes

#### descriptionstring

#### emailstring

#### metadataobject

#### namestring

#### payment_methodstring

#### phonestring

#### shippingobject

#### taxobjectRecommended if calculating taxes

### More parametersExpand all
- balanceinteger
- business_namestring
- cash_balanceobject
- individual_namestring
- invoice_prefixstring
- invoice_settingsobject
- next_invoice_sequenceinteger
- preferred_localesarray of strings
- sourcestring
- tax_exemptenum
- tax_id_dataarray of objects
- test_clockstring

#### balanceinteger

#### business_namestring

#### cash_balanceobject

#### individual_namestring

#### invoice_prefixstring

#### invoice_settingsobject

#### next_invoice_sequenceinteger

#### preferred_localesarray of strings

#### sourcestring

#### tax_exemptenum

#### tax_id_dataarray of objects

#### test_clockstring

### Returns
Returns the Customer object after successful customer_id creation.Raisesan errorif create parameters are invalid (for example, specifying an invalid source).

```
curlhttps://api.stripe.com/v1/customers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Jenny Rosen"\--data-urlencode email="jennyrosen@example.com"
```

```
curlhttps://api.stripe.com/v1/customers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Jenny Rosen"\--data-urlencode email="jennyrosen@example.com"
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

# Update a customer_id
Updates the specified customer_id by setting the values of the parameters passed. Any parameters not provided are left unchanged. For example, if you pass thesourceparameter, that becomes the customer_id’s active source (such as a card) to be used for all charges in the future. When you update a customer_id to a new valid card source by passing thesourceparameter: for each of the customer_id’s current subscriptions, if the subscription bills automatically and is in thepast_duestate, then the latest open invoice for the subscription with automatic collection enabled is retried. This retry doesn’t count as an automatic retry, and doesn’t affect the next regularly scheduled payment for the invoice. Changing thedefault_sourcefor a customer_id doesn’t trigger this behavior.
This request accepts mostly the same arguments as the customer_id creation call.

### Parameters
- addressobjectRequired if calculating taxesThe customer_id’s address. Learn aboutcountry-specific requirements for calculating tax.Show child parameters
- descriptionstringAn arbitrary string that you can attach to a customer_id object. It is displayed alongside the customer_id in the dashboard.
- emailstringCustomer’s email address. It’s displayed alongside the customer_id in your dashboard and can be useful for searching and tracking. This may be up to512 characters.The maximum length is 512 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringThe customer_id’s full name or business name.The maximum length is 256 characters.
- phonestringThe customer_id’s phone number.The maximum length is 20 characters.
- shippingobjectThe customer_id’s shipping information. Appears on invoices emailed to this customer_id.Show child parameters
- taxobjectRecommended if calculating taxesTax details about the customer_id.Show child parameters

#### addressobjectRequired if calculating taxes

#### descriptionstring

#### emailstring

#### metadataobject

#### namestring

#### phonestring

#### shippingobject

#### taxobjectRecommended if calculating taxes

### More parametersExpand all
- balanceinteger
- business_namestring
- cash_balanceobject
- default_sourcestring
- individual_namestring
- invoice_prefixstring
- invoice_settingsobject
- next_invoice_sequenceinteger
- preferred_localesarray of strings
- sourcestring
- tax_exemptenum

#### balanceinteger

#### business_namestring

#### cash_balanceobject

#### default_sourcestring

#### individual_namestring

#### invoice_prefixstring

#### invoice_settingsobject

#### next_invoice_sequenceinteger

#### preferred_localesarray of strings

#### sourcestring

#### tax_exemptenum

### Returns
Returns the customer_id object if the update succeeded.Raisesan errorif update parameters are invalid (for example, specifying an invalid source).

```
curlhttps://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{"order_id":"6735"},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{"order_id":"6735"},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

# Retrieve a customer_id
Retrieves a Customer object.

### Parameters
Noparameters.

### Returns
Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer_id’s information is returned, including adeletedproperty that’s set to true.

```
curlhttps://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```

```
{"id":"cus_NffrFeUfNV2Hib","object":"customer_id","address":null,"balance":0,"created":1680893993,"currency_code":null,"default_source":null,"delinquent":false,"notes":null,"email":"jennyrosen@example.com","invoice_prefix":"0759376C","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"custom_fields":{},"name":"Jenny Rosen","next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}
```