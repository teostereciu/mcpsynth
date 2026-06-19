# radar/value_list_items

*Source: https://docs.stripe.com/api/radar/value_list_items*

---

# Value List Items
Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.
Related guide:Managing list items

# The Value List Item object

### Attributes
- idstringUnique identifier for the object.
- valuestringThe value of the item.
- value_liststringThe identifier of the value list this item belongs to.

#### idstring

#### valuestring

#### value_liststring

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
{"id":"rsli_1MxxosLkdIwHu7ixxvA1yKiZ","object":"radar.value_list_item","created":1681760074,"created_by":"API","livemode":false,"value":"1.2.3.4","value_list":"rsl_1MxxosLkdIwHu7ixNiiD01Kj"}
```

```
{"id":"rsli_1MxxosLkdIwHu7ixxvA1yKiZ","object":"radar.value_list_item","created":1681760074,"created_by":"API","livemode":false,"value":"1.2.3.4","value_list":"rsl_1MxxosLkdIwHu7ixNiiD01Kj"}
```

# Create a value list item
Creates a newValueListItemobject, which is added to the specified parent value list.

### Parameters
- valuestringRequiredThe value of the item (whose type must match the type of the parent value list).The maximum length is 800 characters.
- value_liststringRequiredThe identifier of the value list which the created item will be added to.

#### valuestringRequired

#### value_liststringRequired

### Returns
Returns aValueListItemobject if creation succeeds.

```
curlhttps://api.stripe.com/v1/radar/value_list_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj \-d value="1.2.3.4"
```

```
curlhttps://api.stripe.com/v1/radar/value_list_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj \-d value="1.2.3.4"
```

```
{"id":"rsli_1MxxosLkdIwHu7ixxvA1yKiZ","object":"radar.value_list_item","created":1681760074,"created_by":"API","livemode":false,"value":"1.2.3.4","value_list":"rsl_1MxxosLkdIwHu7ixNiiD01Kj"}
```

```
{"id":"rsli_1MxxosLkdIwHu7ixxvA1yKiZ","object":"radar.value_list_item","created":1681760074,"created_by":"API","livemode":false,"value":"1.2.3.4","value_list":"rsl_1MxxosLkdIwHu7ixNiiD01Kj"}
```

# Retrieve a value list item
Retrieves aValueListItemobject.

### Parameters
Noparameters.

### Returns
Returns aValueListItemobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"rsli_1MxxosLkdIwHu7ixxvA1yKiZ","object":"radar.value_list_item","created":1681760074,"created_by":"API","livemode":false,"value":"1.2.3.4","value_list":"rsl_1MxxosLkdIwHu7ixNiiD01Kj"}
```

```
{"id":"rsli_1MxxosLkdIwHu7ixxvA1yKiZ","object":"radar.value_list_item","created":1681760074,"created_by":"API","livemode":false,"value":"1.2.3.4","value_list":"rsl_1MxxosLkdIwHu7ixNiiD01Kj"}
```

# List all value list items
Returns a list ofValueListItemobjects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters
- value_liststringRequiredIdentifier for the parent value list this item belongs to.
- valuestringReturn items belonging to the parent list whose value matches the specified value (using an “is like” match).The maximum length is 800 characters.

#### value_liststringRequired

#### valuestring

### More parametersExpand all
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

#### createdobject

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
A dictionary with adataproperty that contains an array of up tolimititems, starting after itemstarting_after. Each entry in the array is a separateValueListItemobject. If no more items are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/radar/value_list_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj
```

```
curl-G https://api.stripe.com/v1/radar/value_list_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj
```

```
{"object":"list","url":"/v1/radar/value_list_items","has_more":false,"data":[{"id":"rsl_1MxxosLkdIwHu7ixNiiD01Kj","object":"radar.value_list","alias":"custom_ip_blocklist","created":1681760074,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj"},"livemode":false,"metadata":{},"name":"Custom IP Blocklist"}]}
```

```
{"object":"list","url":"/v1/radar/value_list_items","has_more":false,"data":[{"id":"rsl_1MxxosLkdIwHu7ixNiiD01Kj","object":"radar.value_list","alias":"custom_ip_blocklist","created":1681760074,"created_by":"API","item_type":"ip_address","list_items":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/radar/value_list_items?value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj"},"livemode":false,"metadata":{},"name":"Custom IP Blocklist"}]}
```