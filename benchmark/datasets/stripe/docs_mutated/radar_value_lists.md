# radar/value_lists

*Source: https://docs.stripe.com/api/radar/value_lists*

---

# Value Lists
Value lists allow you to group values together which can then be referenced in rules.
Related guide:Default Stripe lists

# The Value List object

### Attributes
- idstringUnique identifier for the object.
- aliasstringThe name of the value list for use in rules.
- item_typeenumThe type of items in the value list. One ofcard_fingerprint,card_bin,email,ip_address,country,string,case_sensitive_string,customer_id,sepa_debit_fingerprint, orus_bank_account_fingerprint.Possible enum valuescard_bincard_fingerprintcase_sensitive_stringcountrycustomer_idemailip_addresssepa_debit_fingerprintstringus_bank_account_fingerprint
- list_itemsobjectList of items contained within this value list.Show child attributes
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namestringThe name of the value list.

#### idstring

#### aliasstring

#### item_typeenum

[TABLE]
card_bin
card_fingerprint
case_sensitive_string
country
customer_id
email
ip_address
sepa_debit_fingerprint
string
us_bank_account_fingerprint
[/TABLE]

```
card_fingerprint
```

```
case_sensitive_string
```

```
customer_id
```

```
sepa_debit_fingerprint
```

```
us_bank_account_fingerprint
```

#### list_itemsobject

#### metadataobject

#### namestring

### More attributesExpand all
- objectstring
- createdtimestamp
- created_bystring
- livemodeboolean

#### objectstring

#### createdtimestamp

#### created_bystring

#### livemodeboolean

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Custom IP Blocklist"}
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Custom IP Blocklist"}
```

# Create a value list
Creates a newValueListobject, which can then be referenced in rules.

### Parameters
- aliasstringRequiredThe name of the value list for use in rules.The maximum length is 100 characters.
- namestringRequiredThe human-readable name of the value list.The maximum length is 100 characters.
- item_typestringType of the items in the value list. One ofcard_fingerprint,card_bin,email,ip_address,country,string,case_sensitive_string,customer_id,sepa_debit_fingerprint, orus_bank_account_fingerprint. Usestringif the item type is unknown or mixed.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### aliasstringRequired

#### namestringRequired

#### item_typestring

#### metadataobject

### Returns
Returns aValueListobject if creation succeeds.

```
curlhttps://api.stripe.com/v1/radar/value_lists \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Custom IP Blocklist"\-d alias=custom_ip_blocklist \-d item_type=ip_address
```

```
curlhttps://api.stripe.com/v1/radar/value_lists \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Custom IP Blocklist"\-d alias=custom_ip_blocklist \-d item_type=ip_address
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Custom IP Blocklist"}
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Custom IP Blocklist"}
```

# Update a value list
Updates aValueListobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note thatitem_typeis immutable.

### Parameters
- aliasstringThe name of the value list for use in rules.The maximum length is 100 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- namestringThe human-readable name of the value list.The maximum length is 100 characters.

#### aliasstring

#### metadataobject

#### namestring

### Returns
Returns an updatedValueListobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Updated IP Blocklist"
```

```
curlhttps://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Updated IP Blocklist"
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Updated IP Blocklist"}
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Updated IP Blocklist"}
```

# Retrieve a value list
Retrieves aValueListobject.

### Parameters
Noparameters.

### Returns
Returns aValueListobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Custom IP Blocklist"}
```

```
{"id":"rsl_1MrQSwLkdIwHu7ixWOGS5c8M","object":"radar.value_list","alias":"custom_ip_blocklist","created":1680201894,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"},"livemode":false,"custom_fields":{},"name":"Custom IP Blocklist"}
```