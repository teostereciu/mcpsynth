# include_dependent_response_values

*Source: https://docs.stripe.com/api/include_dependent_response_values*

---

# Include-dependent response values (API v2)
Some API v2 responses contain null values for certain properties by default, regardless of their actual values. That reduces the size of response payloads while maintaining the basic response structure. To retrieve the actual values for those properties, specify them in theincludearray request parameter.
To determine whether you need to use theincludeparameter in a given request, look at the request description. Theincludeparameter’s enum values represent the response properties that depend on theincludeparameter.
Whether a response property defaults to null depends on the request endpoint, not the object that the endpoint references. If multiple endpoints return data from the same object, a particular property can depend onincludein one endpoint and return its actual value by default for a different endpoint.
A hash property can depend on a singleincludevalue, or on multipleincludevalues associated with its child properties. For example, when updating an Account, to return actual values for the entireidentityhash, specifyidentityin theincludeparameter. Otherwise, theidentityhash is null in the response. However, to return actual values for theconfigurationhash, you must specify individual configurations in the request. If you specify at least one configuration, but not all of them, specified configurations return actual values and unspecified configurations return null. If you don’t specify any configurations, theconfigurationhash is null in the response.
- Relatedguide:Include-dependent response values

```
curl-X POST https://api.stripe.com/v2/core/accounts \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"include": ["identity","configuration.customer"]}'
```

```
curl-X POST https://api.stripe.com/v2/core/accounts \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"include": ["identity","configuration.customer"]}'
```
The response includes actual values for the properties specified in theincludeparameter, and null for all other include-dependent properties.

```
{"id":"acct_123","object":"v2.core.account","applied_configurations":["customer","merchant"],"configuration":{"customer":{"automatic_indirect_tax":{...},"billing":{...},"capabilities":{...},...},"merchant":null,"recipient":null},"contact_email":"furever@example.com","created":"2025-06-09T21:16:03.000Z","dashboard":"full","defaults":null,"display_name":"Furever","identity":{"business_details":{"doing_business_as":"FurEver","id_numbers":[{"type":"us_ein"}],"product_description":"Saas pet grooming platform at furever.dev using Connect embedded components","structure":"sole_proprietorship","url":"http://accessible.stripe.com"},"country":"US"},"livemode":true,"metadata":{},"requirements":null}
```

```
{"id":"acct_123","object":"v2.core.account","applied_configurations":["customer","merchant"],"configuration":{"customer":{"automatic_indirect_tax":{...},"billing":{...},"capabilities":{...},...},"merchant":null,"recipient":null},"contact_email":"furever@example.com","created":"2025-06-09T21:16:03.000Z","dashboard":"full","defaults":null,"display_name":"Furever","identity":{"business_details":{"doing_business_as":"FurEver","id_numbers":[{"type":"us_ein"}],"product_description":"Saas pet grooming platform at furever.dev using Connect embedded components","structure":"sole_proprietorship","url":"http://accessible.stripe.com"},"country":"US"},"livemode":true,"metadata":{},"requirements":null}
```

# Metadata
Updateable Stripe objects—includingAccount,Charge,Customer,PaymentIntent,Refund,Subscription, andTransferhave ametadataparameter. You can use this parameter to attach key-value data to these Stripe objects.
You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Keys and values are stored as strings and can contain any characters with one exception: you can’t use square brackets ([ and ]) in keys.
You can use metadata to store additional, structured information on an object. For example, you could store your user’s full name and corresponding unique identifier from your system on a StripeCustomerobject. Stripe doesn’t use metadata—for example, we don’t use it to authorize or decline a charge and it won’t be seen by your users unless you choose to show it to them.
Some of the objects listed above also support adescriptionparameter. You can use thedescriptionparameter to annotate a charge-for example, a human-readable description such as2 shirts for test@example.com. Unlikemetadata,descriptionis a single string, which your users might see (for example, in email receipts Stripe sends on your behalf).
Don’t store any sensitive information (bank account numbers, card details, and so on) as metadata or in thedescriptionparameter.
- Relatedguide:Metadata

## Sample metadata use cases
- Link IDs: Attach your system’s unique IDs to a Stripe object to simplify lookups. For example, add your order number to a charge, your user ID to a customer or recipient, or a unique receipt number to a transfer.
- Refund papertrails: Store information about the reason for a refund and the individual responsible for its creation.
- Customer details: Annotate a customer by storing an internal ID for your future use.

```
curlhttps://api.stripe.com/v1/customers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/customers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"cus_123456789","object":"customer","address":{"city":"city","country":"US","line1":"line 1","line2":"line 2","postal_code":"90210","state":"CA"},"balance":0,"created":1483565364,"currency":null,"default_source":null,"delinquent":false,"description":null,"discount":null,"email":null,"invoice_prefix":"C11F7E1","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"metadata":{"order_id":"6735"},"name":null,"next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none"}
```

```
{"id":"cus_123456789","object":"customer","address":{"city":"city","country":"US","line1":"line 1","line2":"line 2","postal_code":"90210","state":"CA"},"balance":0,"created":1483565364,"currency":null,"default_source":null,"delinquent":false,"description":null,"discount":null,"email":null,"invoice_prefix":"C11F7E1","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"metadata":{"order_id":"6735"},"name":null,"next_invoice_sequence":1,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none"}
```

# Pagination
All top-level API resources have support for bulk fetches through “list” API methods. For example, you canlist charges,list customers, andlist invoices. These list API methods share a common structure and accept, at a minimum, the following three parameters:limit,starting_after, andending_before.
Stripe’s list API methods use cursor-basedpaginationthrough thestarting_afterandending_beforeparameters. Both parameters accept an existing object ID value (see below) and return objects in reverse chronological order. Theending_beforeparameter returns objects listed before the named object. Thestarting_afterparameter returns objects listed after the named object. These parameters are mutually exclusive. You can use either thestarting_afterorending_beforeparameter, but not both simultaneously.
Our client libraries offerauto-pagination helpersto traverse all pages of a list.

### Parameters
- limitoptional, default is 10This specifies a limit on the number of objects to return, ranging between 1 and 100.
- starting_afteroptional object IDA cursor to use in pagination.starting_afteris an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, ending withobj_foo, your subsequent call can includestarting_after=obj_footo fetch the next page of the list.
- ending_beforeoptional object IDA cursor to use in pagination.ending_beforeis an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, starting withobj_bar, your subsequent call can includeending_before=obj_barto fetch the previous page of the list.

#### limitoptional, default is 10

#### starting_afteroptional object ID

#### ending_beforeoptional object ID

### List Response Format
- objectstring, value is "list"A string that provides a description of the object type that returns.
- dataarrayAn array containing the actual response elements, paginated by any request parameters.
- has_morebooleanWhether or not there are more elements available after this set. Iffalse, this set comprises the end of the list.
- urlurlThe URL for accessing this list.

#### objectstring, value is "list"

#### dataarray

#### has_moreboolean

#### urlurl
APIs within the/v2namespace contain a differentpaginationinterface than thev1namespace.

```
{"object":"list","url":"/v1/customers","has_more":false,"data":[{"id":"cus_4QFJOjw2pOmAGJ","object":"customer","address":null,"balance":0,"created":1405641735,"currency":"usd","default_source":"card_14HOpG2eZvKYlo2Cz4u5AJG5","delinquent":false,"description":"New customer","discount":null,"email":null,"invoice_prefix":"7D11B54","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"metadata":{"order_id":"6735"},"name":"cus_4QFJOjw2pOmAGJ","next_invoice_sequence":25,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null},]}
```

```
{"object":"list","url":"/v1/customers","has_more":false,"data":[{"id":"cus_4QFJOjw2pOmAGJ","object":"customer","address":null,"balance":0,"created":1405641735,"currency":"usd","default_source":"card_14HOpG2eZvKYlo2Cz4u5AJG5","delinquent":false,"description":"New customer","discount":null,"email":null,"invoice_prefix":"7D11B54","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"metadata":{"order_id":"6735"},"name":"cus_4QFJOjw2pOmAGJ","next_invoice_sequence":25,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null},]}
```

# Search
Some top-level API resource have support for retrieval via “search” API methods. For example, you cansearch charges,search customers, andsearch subscriptions.
Stripe’s search API methods utilize cursor-based pagination via thepagerequest parameter andnext_pageresponse parameter. For example, if you make a search request and receive"next_page": "pagination_key"in the response, your subsequent call can includepage=pagination_keyto fetch the next page of results.
Our client libraries offerauto-paginationhelpers to easily traverse all pages of a search result.

### Search request format
- queryrequiredThe search query string. Seesearch query language.
- limitoptionalA limit on the number of objects returned. Limit can range between 1 and 100, and the default is 10.
- pageoptionalA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use thenext_pagevalue returned in a previous response to request subsequent results.

#### queryrequired

#### limitoptional

#### pageoptional

### Search response format
- objectstring, value is "search_result"A string describing the object type returned.
- urlstringThe URL for accessing this list.
- has_morebooleanWhether or not there are more elements available after this set. Iffalse, this set comprises the end of the list.
- dataarrayAn array containing the actual response elements, paginated by any request parameters.
- next_pagestringA cursor for use in pagination. Ifhas_moreis true, you can pass the value ofnext_pageto a subsequent call to fetch the next page of results.
- total_countoptional positive integer or zeroThe total number of objects that match the query, only accurate up to 10,000. This field isn’t included by default. To include it in the response,expandthetotal_countfield.

#### objectstring, value is "search_result"

#### urlstring

#### has_moreboolean

#### dataarray

#### next_pagestring

#### total_countoptional positive integer or zero

```
{"object":"search_result","url":"/v1/customers/search","has_more":false,"data":[{"id":"cus_4QFJOjw2pOmAGJ","object":"customer","address":null,"balance":0,"created":1405641735,"currency":"usd","default_source":"card_14HOpG2eZvKYlo2Cz4u5AJG5","delinquent":false,"description":"someone@example.com for Coderwall","discount":null,"email":null,"invoice_prefix":"7D11B54","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"metadata":{"foo":"bar"},"name":"fakename","next_invoice_sequence":25,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}]}
```

```
{"object":"search_result","url":"/v1/customers/search","has_more":false,"data":[{"id":"cus_4QFJOjw2pOmAGJ","object":"customer","address":null,"balance":0,"created":1405641735,"currency":"usd","default_source":"card_14HOpG2eZvKYlo2Cz4u5AJG5","delinquent":false,"description":"someone@example.com for Coderwall","discount":null,"email":null,"invoice_prefix":"7D11B54","invoice_settings":{"custom_fields":null,"default_payment_method":null,"footer":null,"rendering_options":null},"livemode":false,"metadata":{"foo":"bar"},"name":"fakename","next_invoice_sequence":25,"phone":null,"preferred_locales":[],"shipping":null,"tax_exempt":"none","test_clock":null}]}
```

# Auto-pagination
Our libraries support auto-pagination. This feature allows you to easily iterate through large lists of resources without having to manually perform the requests to fetch subsequent pages.

```
# The auto-pagination feature is specific to Stripe's# libraries and cannot be used directly with curl.
```

```
# The auto-pagination feature is specific to Stripe's# libraries and cannot be used directly with curl.
```