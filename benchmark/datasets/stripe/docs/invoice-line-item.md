# invoice-line-item

*Source: https://docs.stripe.com/api/invoice-line-item*

---

# Invoice Line Item
Invoice Line Items represent the individual lines within aninvoiceand only exist within the context of an invoice.
Each line item is backed by either aninvoice itemor asubscription item.

# The Invoice Line Item object

### Attributes
- idstringUnique identifier for the object.
- amountintegerThe amount, incents.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- invoicenullablestringThe ID of the invoice that contains this line item.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items withtype=subscription,metadatareflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.
- parentnullableobjectThe parent that generated this line item.Show child attributes
- periodobjectThe period thisline_itemcovers. For subscription line items, this is the subscription period. For prorations, this starts when the proration was calculated, and ends at the period end of the subscription. For invoice items, this is the time at which the invoice item was created or the period of the item. If you haveStripe Revenue Recognitionenabled, the period will be used to recognize and defer revenue. See theRevenue Recognition documentationfor details.Show child attributes
- pricingnullableobjectThe pricing information of the line item.Show child attributes
- quantitynullableintegerThe quantity of the subscription, if the line item is a subscription or a proration.

#### idstring

#### amountinteger

#### currencyenum

#### descriptionnullablestring

#### invoicenullablestring

#### metadataobject

#### parentnullableobject

#### periodobject

#### pricingnullableobject

#### quantitynullableinteger

### More attributesExpand all
- objectstring
- discount_amountsnullablearray of objects
- discountableboolean
- discountsarray of stringsExpandable
- livemodeboolean
- pretax_credit_amountsnullablearray of objects
- quantity_decimalnullabledecimal stringPreview feature
- subtotalinteger
- taxesnullablearray of objects

#### objectstring

#### discount_amountsnullablearray of objects

#### discountableboolean

#### discountsarray of stringsExpandable

#### livemodeboolean

#### pretax_credit_amountsnullablearray of objects

#### quantity_decimalnullabledecimal stringPreview feature

#### subtotalinteger

#### taxesnullablearray of objects

```
{"id":"il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R","object":"line_item","amount":1000,"currency":"usd","description":"My First Invoice Item (created for API docs)","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NpHiK2eZvKYlo2C9NdV8VrI","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1696975413,"start":1696975413},"pricing":{"price_details":{"price":"price_1NzlYfGgdF1VjufL0cVjLJVI","product":"prod_OnMHDH6VBmYlTr"},"type":"price_details","unit_amount_decimal":"1000"},"quantity":1,"taxes":[]}
```

```
{"id":"il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R","object":"line_item","amount":1000,"currency":"usd","description":"My First Invoice Item (created for API docs)","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NpHiK2eZvKYlo2C9NdV8VrI","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1696975413,"start":1696975413},"pricing":{"price_details":{"price":"price_1NzlYfGgdF1VjufL0cVjLJVI","product":"prod_OnMHDH6VBmYlTr"},"type":"price_details","unit_amount_decimal":"1000"},"quantity":1,"taxes":[]}
```

# Update an invoice's line item
Updates an invoice’s line item. Some fields, such astax_amounts, only live on the invoice line item,so they can only be updated through this endpoint. Other fields, such asamount, live on both the invoiceitem and the invoice line item, so updates on this endpoint will propagate to the invoice item as well.Updating an invoice’s line item is only possible before the invoice is finalized.

### Parameters
- invoicestringRequiredInvoice ID of line item
- line_item_idstringRequiredInvoice line item ID
- amountintegerThe integer amount incentsof the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.
- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata. Fortype=subscriptionline items, the incoming metadata specified on the request is directly used to set this value, in contrast totype=invoiceitemline items, where any existing metadata on the invoice line is merged with the incoming data.
- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you haveStripe Revenue Recognitionenabled, the period will be used to recognize and defer revenue. See theRevenue Recognition documentationfor details.Show child parameters
- pricingobjectThe pricing information for the invoice item.Show child parameters
- quantityintegerNon-negative integer. The quantity of units for the line item.

#### invoicestringRequired

#### line_item_idstringRequired

#### amountinteger

#### descriptionstring

#### metadataobject

#### periodobject

#### pricingobject

#### quantityinteger

### More parametersExpand all
- discountableboolean
- discountsarray of objects
- price_dataobject
- quantity_decimalstringPreview feature
- tax_amountsarray of objects
- tax_ratesarray of strings

#### discountableboolean

#### discountsarray of objects

#### price_dataobject

#### quantity_decimalstringPreview feature

#### tax_amountsarray of objects

#### tax_ratesarray of strings

### Returns
The updated invoice’s line item object is returned upon success. Otherwise, this callraisesan error.

```
curl-X POST https://api.stripe.com/v1/invoices/in_1NuhUa2eZvKYlo2CWYVhyvD9/lines/il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X POST https://api.stripe.com/v1/invoices/in_1NuhUa2eZvKYlo2CWYVhyvD9/lines/il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R","object":"line_item","amount":1000,"currency":"usd","description":"My First Invoice Item (created for API docs)","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1Nzo1ZGgdF1VjufLzD1UUn9R","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1696975413,"start":1696975413},"pricing":{"price_details":{"price":"price_1NzlYfGgdF1VjufL0cVjLJVI","product":"prod_OnMHDH6VBmYlTr"},"type":"price_details","unit_amount_decimal":"1000"},"quantity":1,"taxes":[]}
```

```
{"id":"il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R","object":"line_item","amount":1000,"currency":"usd","description":"My First Invoice Item (created for API docs)","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1Nzo1ZGgdF1VjufLzD1UUn9R","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1696975413,"start":1696975413},"pricing":{"price_details":{"price":"price_1NzlYfGgdF1VjufL0cVjLJVI","product":"prod_OnMHDH6VBmYlTr"},"type":"price_details","unit_amount_decimal":"1000"},"quantity":1,"taxes":[]}
```

# Retrieve an invoice's line items
When retrieving an invoice, you’ll get alinesproperty containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters
Noparameters.

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Returns a list ofline_item objects.

```
curlhttps://api.stripe.com/v1/invoices/in_1NpHok2eZvKYlo2CyeiBref0/lines \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/invoices/in_1NpHok2eZvKYlo2CyeiBref0/lines \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"list","url":"/v1/invoices/in_1NpHiG2eZvKYlo2CZV0ZkEBT/lines","has_more":false,"data":[{"id":"il_tmp_1NpHiK2eZvKYlo2C9NdV8VrI","object":"line_item","amount":129999,"currency":"usd","description":"My First Invoice Item (created for API docs)","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NpHiK2eZvKYlo2C9NdV8VrI","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1694467932,"start":1694467932},"pricing":{"price_details":{"price":"price_1NpEIa2eZvKYlo2CXcy5DRPA","product":"prod_OcTFTbV7qh48bd"},"type":"price_details","unit_amount_decimal":"129999"},"quantity":1,"taxes":[]}]}
```

```
{"object":"list","url":"/v1/invoices/in_1NpHiG2eZvKYlo2CZV0ZkEBT/lines","has_more":false,"data":[{"id":"il_tmp_1NpHiK2eZvKYlo2C9NdV8VrI","object":"line_item","amount":129999,"currency":"usd","description":"My First Invoice Item (created for API docs)","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NpHiK2eZvKYlo2C9NdV8VrI","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1694467932,"start":1694467932},"pricing":{"price_details":{"price":"price_1NpEIa2eZvKYlo2CXcy5DRPA","product":"prod_OcTFTbV7qh48bd"},"type":"price_details","unit_amount_decimal":"129999"},"quantity":1,"taxes":[]}]}
```

# Bulk add invoice line items
Adds multiple line items to an invoice. This is only possible when an invoice is still a draft.

### Parameters
- linesarray of objectsRequiredThe line items to add.Show child parameters
- invoice_metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### linesarray of objectsRequired

#### invoice_metadataobject

### Returns
The updated invoice with newly added line items is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/invoices/in_1NuhUa2eZvKYlo2CWYVhyvD9/add_lines \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"lines[0][description]"="test description"\-d"lines[0][amount]"=799 \-d"lines[1][invoice_item]"=ii_1NuLVd2eZvKYlo2CRWY0Hqgi
```

```
curlhttps://api.stripe.com/v1/invoices/in_1NuhUa2eZvKYlo2CWYVhyvD9/add_lines \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"lines[0][description]"="test description"\-d"lines[0][amount]"=799 \-d"lines[1][invoice_item]"=ii_1NuLVd2eZvKYlo2CRWY0Hqgi
```

```
{"id":"in_1NuhUa2eZvKYlo2CWYVhyvD9","object":"invoice","account_country":"US","account_name":"Stripe.com","account_tax_ids":null,"amount_due":998,"amount_paid":0,"amount_overpaid":0,"amount_remaining":998,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1695758664,"currency":"usd","custom_fields":null,"customer":"cus_9s6XKzkNRiz8i3","customer_address":null,"customer_email":"test@test.com","customer_name":null,"customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"effective_at":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[{"id":"il_1NuhUa2eZvKYlo2CC98Fg3Bo","object":"line_item","amount":799,"currency":"usd","description":"test description","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NuhUa2eZvKYlo2CGeF7Qgx0","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1695758664,"start":1695758664},"pricing":{"price_details":{"price":"price_1NuhLA2eZvKYlo2Cq1tIGEBp","product":"prod_Oi7aO1GPi1dWX7"},"type":"price_details","unit_amount_decimal":"799"},"quantity":1,"taxes":[]},{"id":"il_1NuLVe2eZvKYlo2Canh35EfU","object":"line_item","amount":199,"currency":"usd","description":"Canned Coffee","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NuLVd2eZvKYlo2CRWY0Hqgi","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1695674161,"start":1695674161},"pricing":{"price_details":{"price":"price_1NuI212eZvKYlo2CWgdD8kET","product":"prod_OhhQNWDYdIbXYv"},"type":"price_details","unit_amount_decimal":"199"},"quantity":1,"taxes":[]}],"has_more":false,"url":"/v1/invoices/upcoming/lines?customer=cus_9s6XKzkNRiz8i3"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1688482163,"period_start":1688395763,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"redaction":null,"rendering":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":998,"subtotal_excluding_tax":998,"test_clock":null,"total":998,"total_discount_amounts":[],"total_excluding_tax":998,"total_taxes":[],"webhooks_delivered_at":null}
```

```
{"id":"in_1NuhUa2eZvKYlo2CWYVhyvD9","object":"invoice","account_country":"US","account_name":"Stripe.com","account_tax_ids":null,"amount_due":998,"amount_paid":0,"amount_overpaid":0,"amount_remaining":998,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1695758664,"currency":"usd","custom_fields":null,"customer":"cus_9s6XKzkNRiz8i3","customer_address":null,"customer_email":"test@test.com","customer_name":null,"customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"effective_at":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[{"id":"il_1NuhUa2eZvKYlo2CC98Fg3Bo","object":"line_item","amount":799,"currency":"usd","description":"test description","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NuhUa2eZvKYlo2CGeF7Qgx0","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1695758664,"start":1695758664},"pricing":{"price_details":{"price":"price_1NuhLA2eZvKYlo2Cq1tIGEBp","product":"prod_Oi7aO1GPi1dWX7"},"type":"price_details","unit_amount_decimal":"799"},"quantity":1,"taxes":[]},{"id":"il_1NuLVe2eZvKYlo2Canh35EfU","object":"line_item","amount":199,"currency":"usd","description":"Canned Coffee","discount_amounts":[],"discountable":true,"discounts":[],"livemode":false,"metadata":{},"parent":{"type":"invoice_item_details","invoice_item_details":{"invoice_item":"ii_1NuLVd2eZvKYlo2CRWY0Hqgi","proration":false,"proration_details":{"credited_items":null},"subscription":null}},"period":{"end":1695674161,"start":1695674161},"pricing":{"price_details":{"price":"price_1NuI212eZvKYlo2CWgdD8kET","product":"prod_OhhQNWDYdIbXYv"},"type":"price_details","unit_amount_decimal":"199"},"quantity":1,"taxes":[]}],"has_more":false,"url":"/v1/invoices/upcoming/lines?customer=cus_9s6XKzkNRiz8i3"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1688482163,"period_start":1688395763,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"redaction":null,"rendering":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":998,"subtotal_excluding_tax":998,"test_clock":null,"total":998,"total_discount_amounts":[],"total_excluding_tax":998,"total_taxes":[],"webhooks_delivered_at":null}
```