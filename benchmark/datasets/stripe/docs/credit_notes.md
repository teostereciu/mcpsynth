# credit_notes

*Source: https://docs.stripe.com/api/credit_notes*

---

# Credit Note
Issue a credit note to adjust an invoice’s amount after the invoice is finalized.
Related guide:Credit notes

# The Credit Note object

### Attributes
- idstringUnique identifier for the object.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- invoicestringExpandableID of the invoice.
- linesobjectLine items that make up the credit noteShow child attributes
- memonullablestringCustomer-facing text that appears on the credit note PDF.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- reasonnullableenumReason for issuing this credit note, one ofduplicate,fraudulent,order_change, orproduct_unsatisfactoryPossible enum valuesduplicateCredit issued for a duplicate payment or chargefraudulentCredit note issued for fraudulent activityorder_changeCredit note issued for order changeproduct_unsatisfactoryCredit note issued for unsatisfactory product
- statusenumStatus of this credit note, one ofissuedorvoid. Learn more aboutvoiding credit notes.Possible enum valuesissuedThe credit note has been issued.voidThe credit note has been voided.
- subtotalintegerThe integer amount incentsrepresenting the amount of the credit note, excluding exclusive tax and invoice level discounts.
- totalintegerThe integer amount incentsrepresenting the total amount of the credit note, including tax and all discount.

#### idstring

#### currencyenum

#### invoicestringExpandable

#### linesobject

#### memonullablestring

#### metadatanullableobject

#### reasonnullableenum

[TABLE]
duplicateCredit issued for a duplicate payment or charge
fraudulentCredit note issued for fraudulent activity
order_changeCredit note issued for order change
product_unsatisfactoryCredit note issued for unsatisfactory product
[/TABLE]

```
order_change
```

```
product_unsatisfactory
```

#### statusenum

[TABLE]
issuedThe credit note has been issued.
voidThe credit note has been voided.
[/TABLE]

#### subtotalinteger

#### totalinteger

### More attributesExpand all
- objectstring
- amountinteger
- amount_shippinginteger
- createdtimestamp
- customerstringExpandable
- customer_accountnullablestring
- customer_balance_transactionnullablestringExpandable
- discount_amountintegerDeprecated
- discount_amountsarray of objects
- effective_atnullabletimestamp
- livemodeboolean
- numberstring
- out_of_band_amountnullableinteger
- pdfstring
- post_payment_amountinteger
- pre_payment_amountinteger
- pretax_credit_amountsarray of objects
- refundsarray of objects
- shipping_costnullableobject
- subtotal_excluding_taxnullableinteger
- total_excluding_taxnullableinteger
- total_taxesnullablearray of objects
- typeenum
- voided_atnullabletimestamp

#### objectstring

#### amountinteger

#### amount_shippinginteger

#### createdtimestamp

#### customerstringExpandable

#### customer_accountnullablestring

#### customer_balance_transactionnullablestringExpandable

#### discount_amountintegerDeprecated

#### discount_amountsarray of objects

#### effective_atnullabletimestamp

#### livemodeboolean

#### numberstring

#### out_of_band_amountnullableinteger

#### pdfstring

#### post_payment_amountinteger

#### pre_payment_amountinteger

#### pretax_credit_amountsarray of objects

#### refundsarray of objects

#### shipping_costnullableobject

#### subtotal_excluding_taxnullableinteger

#### total_excluding_taxnullableinteger

#### total_taxesnullablearray of objects

#### typeenum

#### voided_atnullabletimestamp

```
{"id":"cn_1MxvRqLkdIwHu7ixY0xbUcxk","object":"credit_note","amount":1099,"amount_shipping":0,"created":1681750958,"currency":"usd","customer":"cus_NjLgPhUokHubJC","customer_balance_transaction":null,"discount_amount":0,"discount_amounts":[],"invoice":"in_1MxvRkLkdIwHu7ixABNtI99m","lines":{"object":"list","data":[{"id":"cnli_1MxvRqLkdIwHu7ixFpdhBFQf","object":"credit_note_line_item","amount":1099,"description":"T-shirt","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1MxvRlLkdIwHu7ixnkbntxUV","livemode":false,"quantity":1,"tax_rates":[],"taxes":[],"type":"invoice_line_item","unit_amount":1099,"unit_amount_decimal":"1099"}],"has_more":false,"url":"/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"},"livemode":false,"memo":null,"metadata":{},"number":"C9E0C52C-0036-CN-01","out_of_band_amount":null,"pdf":"https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap","pre_payment_amount":1099,"post_payment_amount":0,"reason":null,"refunds":[],"shipping_cost":null,"status":"issued","subtotal":1099,"subtotal_excluding_tax":1099,"total":1099,"total_excluding_tax":1099,"total_taxes":[],"type":"pre_payment","voided_at":null}
```

```
{"id":"cn_1MxvRqLkdIwHu7ixY0xbUcxk","object":"credit_note","amount":1099,"amount_shipping":0,"created":1681750958,"currency":"usd","customer":"cus_NjLgPhUokHubJC","customer_balance_transaction":null,"discount_amount":0,"discount_amounts":[],"invoice":"in_1MxvRkLkdIwHu7ixABNtI99m","lines":{"object":"list","data":[{"id":"cnli_1MxvRqLkdIwHu7ixFpdhBFQf","object":"credit_note_line_item","amount":1099,"description":"T-shirt","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1MxvRlLkdIwHu7ixnkbntxUV","livemode":false,"quantity":1,"tax_rates":[],"taxes":[],"type":"invoice_line_item","unit_amount":1099,"unit_amount_decimal":"1099"}],"has_more":false,"url":"/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"},"livemode":false,"memo":null,"metadata":{},"number":"C9E0C52C-0036-CN-01","out_of_band_amount":null,"pdf":"https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap","pre_payment_amount":1099,"post_payment_amount":0,"reason":null,"refunds":[],"shipping_cost":null,"status":"issued","subtotal":1099,"subtotal_excluding_tax":1099,"total":1099,"total_excluding_tax":1099,"total_taxes":[],"type":"pre_payment","voided_at":null}
```

# The Credit Note Line Item object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerThe integer amount incentsrepresenting the gross amount being credited for this line item, excluding (exclusive) tax and discounts.
- descriptionnullablestringDescription of the item being credited.
- discount_amountintegerDeprecatedThe integer amount incentsrepresenting the discount being credited for this line item.
- discount_amountsarray of objectsThe amount of discount calculated per discount for this line itemShow child attributes
- invoice_line_itemnullablestringID of the invoice line item being credited
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- pretax_credit_amountsarray of objectsThe pretax credit amounts (ex: discount, credit grants, etc) for this line item.Show child attributes
- quantitynullableintegerThe number of units of product being credited.
- tax_ratesarray of objectsThe tax rates which apply to the line item.Show child attributes
- taxesnullablearray of objectsThe tax information of the line item.Show child attributes
- typeenumThe type of the credit note line item, one ofinvoice_line_itemorcustom_line_item. When the type isinvoice_line_itemthere is an additionalinvoice_line_itemproperty on the resource the value of which is the id of the credited line item on the invoice.Possible enum valuescustom_line_iteminvoice_line_item
- unit_amountnullableintegerThe cost of each unit of product being credited.
- unit_amount_decimalnullabledecimal stringSame asunit_amount, but contains a decimal value with at most 12 decimal places.

#### idstring

#### objectstring

#### amountinteger

#### descriptionnullablestring

#### discount_amountintegerDeprecated

#### discount_amountsarray of objects

#### invoice_line_itemnullablestring

#### livemodeboolean

#### metadatanullableobject

#### pretax_credit_amountsarray of objects

#### quantitynullableinteger

#### tax_ratesarray of objects

#### taxesnullablearray of objects

#### typeenum

[TABLE]
custom_line_item
invoice_line_item
[/TABLE]

```
custom_line_item
```

```
invoice_line_item
```

#### unit_amountnullableinteger

#### unit_amount_decimalnullabledecimal string

```
{"id":"cnli_1NPtOx2eZvKYlo2CBH1NpUsU","object":"credit_note_line_item","amount":749,"description":"My First Invoice Item (created for API docs)","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1NPtOx2eZvKYlo2CAUuq0WVl","livemode":false,"quantity":1,"taxes":[],"tax_rates":[],"type":"invoice_line_item","unit_amount":null,"unit_amount_decimal":null}
```

```
{"id":"cnli_1NPtOx2eZvKYlo2CBH1NpUsU","object":"credit_note_line_item","amount":749,"description":"My First Invoice Item (created for API docs)","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1NPtOx2eZvKYlo2CAUuq0WVl","livemode":false,"quantity":1,"taxes":[],"tax_rates":[],"type":"invoice_line_item","unit_amount":null,"unit_amount_decimal":null}
```

# Create a credit note
Issue a credit note to adjust the amount of a finalized invoice. A credit note will first reduce the invoice’samount_remaining(andamount_due), but not below zero.This amount is indicated by the credit note’spre_payment_amount. The excess amount is indicated bypost_payment_amount, and it can result in any combination of the following:
- Refunds: create a new refund (usingrefund_amount) or link existing refunds (usingrefunds).
- Customer balance credit: credit the customer’s balance (usingcredit_amount) which will be automatically applied to their next invoice when it’s finalized.
- Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (usingout_of_band_amount).
The sum of refunds, customer balance credits, and outside of Stripe credits must equal thepost_payment_amount.
You may issue multiple credit notes for an invoice. Each credit note may increment the invoice’spre_payment_credit_notes_amount,post_payment_credit_notes_amount, or both, depending on the invoice’samount_remainingat the time of credit note creation.

### Parameters
- invoicestringRequiredID of the invoice.
- linesarray of objectsRequired conditionallyLine items that make up the credit note. One ofamount,lines, orshipping_costmust be provided.Show child parameters
- memostringThe credit note’s memo appears on the credit note PDF.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- reasonenumReason for issuing this credit note, one ofduplicate,fraudulent,order_change, orproduct_unsatisfactoryPossible enum valuesduplicateCredit issued for a duplicate payment or chargefraudulentCredit note issued for fraudulent activityorder_changeCredit note issued for order changeproduct_unsatisfactoryCredit note issued for unsatisfactory product

#### invoicestringRequired

#### linesarray of objectsRequired conditionally

#### memostring

#### metadataobject

#### reasonenum

[TABLE]
duplicateCredit issued for a duplicate payment or charge
fraudulentCredit note issued for fraudulent activity
order_changeCredit note issued for order change
product_unsatisfactoryCredit note issued for unsatisfactory product
[/TABLE]

```
order_change
```

```
product_unsatisfactory
```

### More parametersExpand all
- amountintegerRequired conditionally
- credit_amountinteger
- effective_attimestamp
- email_typeenum
- out_of_band_amountinteger
- refund_amountinteger
- refundsarray of objects
- shipping_costobjectRequired conditionally

#### amountintegerRequired conditionally

#### credit_amountinteger

#### effective_attimestamp

#### email_typeenum

#### out_of_band_amountinteger

#### refund_amountinteger

#### refundsarray of objects

#### shipping_costobjectRequired conditionally

### Returns
Returns a credit note object if the call succeeded.

```
curlhttps://api.stripe.com/v1/credit_notes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d invoice=in_1MxvRkLkdIwHu7ixABNtI99m
```

```
curlhttps://api.stripe.com/v1/credit_notes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d invoice=in_1MxvRkLkdIwHu7ixABNtI99m
```

```
{"id":"cn_1MxvRqLkdIwHu7ixY0xbUcxk","object":"credit_note","amount":1099,"amount_shipping":0,"created":1681750958,"currency":"usd","customer":"cus_NjLgPhUokHubJC","customer_balance_transaction":null,"discount_amount":0,"discount_amounts":[],"invoice":"in_1MxvRkLkdIwHu7ixABNtI99m","lines":{"object":"list","data":[{"id":"cnli_1MxvRqLkdIwHu7ixFpdhBFQf","object":"credit_note_line_item","amount":1099,"description":"T-shirt","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1MxvRlLkdIwHu7ixnkbntxUV","livemode":false,"quantity":1,"tax_rates":[],"taxes":[],"type":"invoice_line_item","unit_amount":1099,"unit_amount_decimal":"1099"}],"has_more":false,"url":"/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"},"livemode":false,"memo":null,"metadata":{},"number":"C9E0C52C-0036-CN-01","out_of_band_amount":null,"pdf":"https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap","pre_payment_amount":1099,"post_payment_amount":0,"reason":null,"refunds":[],"shipping_cost":null,"status":"issued","subtotal":1099,"subtotal_excluding_tax":1099,"total":1099,"total_excluding_tax":1099,"total_taxes":[],"type":"pre_payment","voided_at":null}
```

```
{"id":"cn_1MxvRqLkdIwHu7ixY0xbUcxk","object":"credit_note","amount":1099,"amount_shipping":0,"created":1681750958,"currency":"usd","customer":"cus_NjLgPhUokHubJC","customer_balance_transaction":null,"discount_amount":0,"discount_amounts":[],"invoice":"in_1MxvRkLkdIwHu7ixABNtI99m","lines":{"object":"list","data":[{"id":"cnli_1MxvRqLkdIwHu7ixFpdhBFQf","object":"credit_note_line_item","amount":1099,"description":"T-shirt","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1MxvRlLkdIwHu7ixnkbntxUV","livemode":false,"quantity":1,"tax_rates":[],"taxes":[],"type":"invoice_line_item","unit_amount":1099,"unit_amount_decimal":"1099"}],"has_more":false,"url":"/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"},"livemode":false,"memo":null,"metadata":{},"number":"C9E0C52C-0036-CN-01","out_of_band_amount":null,"pdf":"https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap","pre_payment_amount":1099,"post_payment_amount":0,"reason":null,"refunds":[],"shipping_cost":null,"status":"issued","subtotal":1099,"subtotal_excluding_tax":1099,"total":1099,"total_excluding_tax":1099,"total_taxes":[],"type":"pre_payment","voided_at":null}
```

# Update a credit note
Updates an existing credit note.

### Parameters
- memostringCredit note memo.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### memostring

#### metadataobject

### Returns
Returns the updated credit note object if the call succeeded.

```
curlhttps://api.stripe.com/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"cn_1MxvRqLkdIwHu7ixY0xbUcxk","object":"credit_note","amount":1099,"amount_shipping":0,"created":1681750958,"currency":"usd","customer":"cus_NjLgPhUokHubJC","customer_balance_transaction":null,"discount_amount":0,"discount_amounts":[],"invoice":"in_1MxvRkLkdIwHu7ixABNtI99m","lines":{"object":"list","data":[{"id":"cnli_1MxvRqLkdIwHu7ixFpdhBFQf","object":"credit_note_line_item","amount":1099,"description":"T-shirt","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1MxvRlLkdIwHu7ixnkbntxUV","livemode":false,"quantity":1,"tax_rates":[],"taxes":[],"type":"invoice_line_item","unit_amount":1099,"unit_amount_decimal":"1099"}],"has_more":false,"url":"/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"},"livemode":false,"memo":null,"metadata":{"order_id":"6735"},"number":"C9E0C52C-0036-CN-01","out_of_band_amount":null,"pdf":"https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap","pre_payment_amount":1099,"post_payment_amount":0,"reason":null,"refunds":[],"shipping_cost":null,"status":"issued","subtotal":1099,"subtotal_excluding_tax":1099,"total":1099,"total_excluding_tax":1099,"total_taxes":[],"type":"pre_payment","voided_at":null}
```

```
{"id":"cn_1MxvRqLkdIwHu7ixY0xbUcxk","object":"credit_note","amount":1099,"amount_shipping":0,"created":1681750958,"currency":"usd","customer":"cus_NjLgPhUokHubJC","customer_balance_transaction":null,"discount_amount":0,"discount_amounts":[],"invoice":"in_1MxvRkLkdIwHu7ixABNtI99m","lines":{"object":"list","data":[{"id":"cnli_1MxvRqLkdIwHu7ixFpdhBFQf","object":"credit_note_line_item","amount":1099,"description":"T-shirt","discount_amount":0,"discount_amounts":[],"invoice_line_item":"il_1MxvRlLkdIwHu7ixnkbntxUV","livemode":false,"quantity":1,"tax_rates":[],"taxes":[],"type":"invoice_line_item","unit_amount":1099,"unit_amount_decimal":"1099"}],"has_more":false,"url":"/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"},"livemode":false,"memo":null,"metadata":{"order_id":"6735"},"number":"C9E0C52C-0036-CN-01","out_of_band_amount":null,"pdf":"https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap","pre_payment_amount":1099,"post_payment_amount":0,"reason":null,"refunds":[],"shipping_cost":null,"status":"issued","subtotal":1099,"subtotal_excluding_tax":1099,"total":1099,"total_excluding_tax":1099,"total_taxes":[],"type":"pre_payment","voided_at":null}
```