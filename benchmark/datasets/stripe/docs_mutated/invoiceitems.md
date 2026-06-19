# invoiceitems

*Source: https://docs.stripe.com/api/invoiceitems*

---

# Invoice Items
Invoice Items represent the component lines of aninvoice. When you create an invoice item with aninvoicefield, it is attached to the specified invoice and included asan invoice line itemwithininvoice.lines.
Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combinedwith asubscription. Sometimes you want to add a charge or credit to a customer_id, but actually chargeor credit the customer_id’s card only at the end of a regular billing cycle. This is useful for combining several charges(to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.
Related guides:Integrate with the Invoicing API,Subscription Invoices.

# The Invoice Item object

### Attributes
- idstringUnique identifier for the object.
- amountintegerAmount (in thecurrencyspecified) of the invoice item. This should always be equal tounit_amount * quantity.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- customerstringExpandableThe ID of the customer_id to bill for this invoice item.
- customer_accountnullablestringThe ID of the account to bill for this invoice item.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- parentnullableobjectThe parent that generated this invoice item.Show child attributes
- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you haveStripe Revenue Recognitionenabled, the period will be used to recognize and defer revenue. See theRevenue Recognition documentationfor details.Show child attributes
- pricingnullableobjectThe pricing information of the invoice item.Show child attributes
- prorationbooleanWhether the invoice item was created automatically as a proration adjustment when the customer_id switched plans.

#### idstring

#### amountinteger

#### currencyenum

#### customerstringExpandable

#### customer_accountnullablestring

#### descriptionnullablestring

#### metadatanullableobject

#### parentnullableobject

#### periodobject

#### pricingnullableobject

#### prorationboolean

### More attributesExpand all
- objectstring
- datetimestamp
- discountableboolean
- discountsnullablearray of stringsExpandable
- invoicenullablestringExpandable
- livemodeboolean
- net_amountnullableinteger
- proration_detailsnullableobject
- quantityinteger
- quantity_decimaldecimal stringPreview feature
- tax_ratesnullablearray of objects
- test_clocknullablestringExpandable

#### objectstring

#### datetimestamp

#### discountableboolean

#### discountsnullablearray of stringsExpandable

#### invoicenullablestringExpandable

#### livemodeboolean

#### net_amountnullableinteger

#### proration_detailsnullableobject

#### quantityinteger

#### quantity_decimaldecimal stringPreview feature

#### tax_ratesnullablearray of objects

#### test_clocknullablestringExpandable

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

# Create an invoice item
Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer_id specified.

### Parameters
- amountintegerThe integer amount incentsof the charge to be applied to the upcoming invoice. Passing in a negativeamountwill reduce theamount_dueon the invoice.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- customerstringThe ID of the customer_id to bill for this invoice item.
- customer_accountstringThe ID of the account representing the customer_id to bill for this invoice item.
- descriptionstringAn arbitrary string which you can attach to the invoice item. The notes is displayed in the invoice for easy tracking.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you haveStripe Revenue Recognitionenabled, the period will be used to recognize and defer revenue. See theRevenue Recognition documentationfor details.Show child parameters
- pricingobjectThe pricing information for the invoice item.Show child parameters

#### amountinteger

#### currencyenum

#### customerstring

#### customer_accountstring

#### descriptionstring

#### metadataobject

#### periodobject

#### pricingobject

### More parametersExpand all
- discountableboolean
- discountsarray of objects
- invoicestring
- price_dataobject
- quantityinteger
- quantity_decimalstringPreview feature
- subscriptionstring
- tax_behaviorenumRecommended if calculating taxes
- tax_codestringRecommended if calculating taxes
- tax_ratesarray of strings
- unit_amount_decimalstring

#### discountableboolean

#### discountsarray of objects

#### invoicestring

#### price_dataobject

#### quantityinteger

#### quantity_decimalstringPreview feature

#### subscriptionstring

#### tax_behaviorenumRecommended if calculating taxes

#### tax_codestringRecommended if calculating taxes

#### tax_ratesarray of strings

#### unit_amount_decimalstring

### Returns
The created invoice item object is returned if successful. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/invoiceitems \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NeZei8imSbMVvi \-d"pricing[price]"=price_1MtGUsLkdIwHu7ix1be5Ljaj
```

```
curlhttps://api.stripe.com/v1/invoiceitems \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NeZei8imSbMVvi \-d"pricing[price]"=price_1MtGUsLkdIwHu7ix1be5Ljaj
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

# Update an invoice item
Updates the amount or notes of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.

### Parameters
- amountintegerThe integer amount incentsof the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer_id’s account, pass a negative amount.
- descriptionstringAn arbitrary string which you can attach to the invoice item. The notes is displayed in the invoice for easy tracking.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you haveStripe Revenue Recognitionenabled, the period will be used to recognize and defer revenue. See theRevenue Recognition documentationfor details.Show child parameters
- pricingobjectThe pricing information for the invoice item.Show child parameters

#### amountinteger

#### descriptionstring

#### metadataobject

#### periodobject

#### pricingobject

### More parametersExpand all
- discountableboolean
- discountsarray of objects
- price_dataobject
- quantityinteger
- quantity_decimalstringPreview feature
- tax_behaviorenumRecommended if calculating taxes
- tax_codestringRecommended if calculating taxes
- tax_ratesarray of strings
- unit_amount_decimalstring

#### discountableboolean

#### discountsarray of objects

#### price_dataobject

#### quantityinteger

#### quantity_decimalstringPreview feature

#### tax_behaviorenumRecommended if calculating taxes

#### tax_codestringRecommended if calculating taxes

#### tax_ratesarray of strings

#### unit_amount_decimalstring

### Returns
The updated invoice item object is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{"order_id":"6735"},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{"order_id":"6735"},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

# Retrieve an invoice item
Retrieves the invoice item with the given ID.

### Parameters
Noparameters.

### Returns
Returns an invoice item if a valid invoice item ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```

```
{"id":"ii_1MtGUtLkdIwHu7ixBYwjAM00","object":"invoiceitem","amount":1099,"currency_code":"usd","customer_id":"cus_NeZei8imSbMVvi","date":1680640231,"notes":"T-shirt","discountable":true,"discounts":[],"invoice":null,"livemode":false,"custom_fields":{},"parent":null,"period":{"end":1680640231,"start":1680640231},"pricing":{"price_details":{"price":"price_1MtGUsLkdIwHu7ix1be5Ljaj","product":"prod_NeZe7xbBdJT8EN"},"type":"price_details","unit_amount_decimal":"1099"},"proration":false,"quantity":1,"tax_rates":[],"test_clock":null}
```