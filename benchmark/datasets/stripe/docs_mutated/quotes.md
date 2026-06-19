# quotes

*Source: https://docs.stripe.com/api/quotes*

---

# Quote
A Quote is a way to model prices that you’d like to provide to a customer_id.Once accepted, it will automatically create an invoice, subscription or subscription schedule.

# The Quote object

### Attributes
- idstringUnique identifier for the object.
- line_itemsobjectExpandableA list of items the customer_id is being quoted for.Show child attributes
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### idstring

#### line_itemsobjectExpandable

#### metadataobject

### More attributesExpand all
- objectstring
- amount_subtotalinteger
- amount_totalinteger
- applicationnullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- application_fee_percentnullablefloatConnect only
- automatic_taxobject
- collection_methodenum
- computedobject
- createdtimestamp
- currencynullablestring
- customernullablestringExpandable
- customer_accountnullablestring
- default_tax_ratesarray of stringsExpandable
- descriptionnullablestring
- discountsarray of stringsExpandable
- expires_attimestamp
- footernullablestring
- from_quotenullableobject
- headernullablestring
- invoicenullablestringExpandable
- invoice_settingsobject
- livemodeboolean
- numbernullablestring
- on_behalf_ofnullablestringExpandableConnect only
- statusenum
- status_transitionsobject
- subscriptionnullablestringExpandable
- subscription_dataobject
- subscription_schedulenullablestringExpandable
- test_clocknullablestringExpandable
- total_detailsobject
- transfer_datanullableobjectConnect only

#### objectstring

#### amount_subtotalinteger

#### amount_totalinteger

#### applicationnullablestringExpandableConnect only

#### application_fee_amountnullableintegerConnect only

#### application_fee_percentnullablefloatConnect only

#### automatic_taxobject

#### collection_methodenum

#### computedobject

#### createdtimestamp

#### currencynullablestring

#### customernullablestringExpandable

#### customer_accountnullablestring

#### default_tax_ratesarray of stringsExpandable

#### descriptionnullablestring

#### discountsarray of stringsExpandable

#### expires_attimestamp

#### footernullablestring

#### from_quotenullableobject

#### headernullablestring

#### invoicenullablestringExpandable

#### invoice_settingsobject

#### livemodeboolean

#### numbernullablestring

#### on_behalf_ofnullablestringExpandableConnect only

#### statusenum

#### status_transitionsobject

#### subscriptionnullablestringExpandable

#### subscription_dataobject

#### subscription_schedulenullablestringExpandable

#### test_clocknullablestringExpandable

#### total_detailsobject

#### transfer_datanullableobjectConnect only

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

# Create a quote
A quote models prices and services for a customer_id. Default options forheader,notes,footer, andexpires_atcan be set in the dashboard via thequote template.

### Parameters
- line_itemsarray of objectsA list of line items the customer_id is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### line_itemsarray of objects

#### metadataobject

### More parametersExpand all
- application_fee_amountintegerConnect only
- application_fee_percentfloatConnect only
- automatic_taxobject
- collection_methodenum
- customerstring
- customer_accountstring
- default_tax_ratesarray of strings
- descriptionstring
- discountsarray of objects
- expires_attimestamp
- footerstring
- from_quoteobject
- headerstring
- invoice_settingsobject
- on_behalf_ofstringConnect only
- subscription_dataobject
- test_clockstring
- transfer_dataobjectConnect only

#### application_fee_amountintegerConnect only

#### application_fee_percentfloatConnect only

#### automatic_taxobject

#### collection_methodenum

#### customerstring

#### customer_accountstring

#### default_tax_ratesarray of strings

#### descriptionstring

#### discountsarray of objects

#### expires_attimestamp

#### footerstring

#### from_quoteobject

#### headerstring

#### invoice_settingsobject

#### on_behalf_ofstringConnect only

#### subscription_dataobject

#### test_clockstring

#### transfer_dataobjectConnect only

### Returns
Returns the quote object.

```
curlhttps://api.stripe.com/v1/quotes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NcMfB0SSFHINCV \-d"line_items[0][price]"=price_1Mr7wULkdIwHu7ixhPkIEN2w \-d"line_items[0][quantity]"=2
```

```
curlhttps://api.stripe.com/v1/quotes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NcMfB0SSFHINCV \-d"line_items[0][price]"=price_1Mr7wULkdIwHu7ixhPkIEN2w \-d"line_items[0][quantity]"=2
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

# Update a quote
A quote models prices and services for a customer_id.

### Parameters
- line_itemsarray of objectsA list of line items the customer_id is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### line_itemsarray of objects

#### metadataobject

### More parametersExpand all
- application_fee_amountintegerConnect only
- application_fee_percentfloatConnect only
- automatic_taxobject
- collection_methodenum
- customerstring
- customer_accountstring
- default_tax_ratesarray of strings
- descriptionstring
- discountsarray of objects
- expires_attimestamp
- footerstring
- headerstring
- invoice_settingsobject
- on_behalf_ofstringConnect only
- subscription_dataobject
- transfer_dataobjectConnect only

#### application_fee_amountintegerConnect only

#### application_fee_percentfloatConnect only

#### automatic_taxobject

#### collection_methodenum

#### customerstring

#### customer_accountstring

#### default_tax_ratesarray of strings

#### descriptionstring

#### discountsarray of objects

#### expires_attimestamp

#### footerstring

#### headerstring

#### invoice_settingsobject

#### on_behalf_ofstringConnect only

#### subscription_dataobject

#### transfer_dataobjectConnect only

### Returns
Returns the updated quote object.

```
curlhttps://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{"order_id":"6735"},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{"order_id":"6735"},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

# Retrieve a quote
Retrieves the quote with the given ID.

### Parameters
Noparameters.

### Returns
Returns a quote if a valid quote ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```

```
{"id":"qt_1Mr7wVLkdIwHu7ixJYSiPTGq","object":"quote","amount_subtotal":2198,"amount_total":2198,"application":null,"application_fee_amount":null,"application_fee_percent":null,"automatic_tax":{"enabled":false,"liability":null,"status":null},"collection_method":"charge_automatically","computed":{"recurring":null,"upfront":{"amount_subtotal":2198,"amount_total":2198,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0}}},"created":1680130691,"currency_code":"usd","customer_id":"cus_NcMfB0SSFHINCV","default_tax_rates":[],"notes":null,"discounts":[],"expires_at":1682722691,"footer":null,"from_quote":null,"header":null,"invoice":null,"invoice_settings":{"days_until_due":null,"issuer":{"type":"self"}},"livemode":false,"custom_fields":{},"number":null,"on_behalf_of":null,"status":"draft","status_transitions":{"accepted_at":null,"canceled_at":null,"finalized_at":null},"subscription":null,"subscription_data":{"notes":null,"effective_date":null,"trial_period_days":null},"subscription_schedule":null,"test_clock":null,"total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"transfer_data":null}
```