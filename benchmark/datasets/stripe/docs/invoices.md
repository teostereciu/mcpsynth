# invoices

*Source: https://docs.stripe.com/api/invoices*

---

# Invoices
Invoices are statements of amounts owed by a customer, and are eithergenerated one-off, or generated periodically from a subscription.
They containinvoice items, and proration adjustmentsthat may be caused by subscription upgrades/downgrades (if necessary).
If your invoice is configured to be billed through automatic charges,Stripe automatically finalizes your invoice and attempts payment.  Notethat finalizing the invoice,when automatic, doesnot happen immediately as the invoice is created. Stripe waitsuntil one hour after the last webhook was successfully sent (or the lastwebhook timed out after failing). If you (and the platforms you may haveconnected to) have no webhooks configured, Stripe waits one hour aftercreation to finalize the invoice.
If your invoice is configured to be billed by sending an email, then based on youremail settings,Stripe will email the invoice to your customer and await payment. Theseemails can contain a link to a hosted page to pay the invoice.
Stripe applies any customer credit on the account before determining theamount due for the invoice (i.e., the amount that will be actuallycharged). If the amount due for the invoice is less than Stripe’sminimum allowed chargeper currency, theinvoice is automatically marked paid, and we add the amount due to thecustomer’s credit balance which is applied to the next invoice.
More details on the customer’s credit balance arehere.
Related guide:Send invoices to customers

# The Invoice object

### Attributes
- idstringUnique identifier for the object. For preview invoices created using thecreate previewendpoint, this id will be prefixed withupcoming_in.
- auto_advancebooleanControls whether Stripe performsautomatic collectionof the invoice. Iffalse, the invoice’s state doesn’t automatically advance without an explicit action.
- automatic_taxobjectSettings and latest results for automatic tax lookup for this invoice.Show child attributes
- collection_methodenumEithercharge_automatically, orsend_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.Possible enum valuescharge_automaticallyAttempt payment using the default source attached to the customer.send_invoiceEmail payment instructions to the customer.
- confirmation_secretnullableobjectExpandableThe confirmation secret associated with this invoice. Currently, this contains the client_secret of the PaymentIntent that Stripe creates during invoice finalization.Show child attributes
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- customerstringExpandableThe ID of the customer to bill.
- customer_accountnullablestringThe ID of the account representing the customer to bill.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.
- hosted_invoice_urlnullablestringThe URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.
- linesobjectThe individual line items that make up the invoice.linesis sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.Show child attributes
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- parentnullableobjectThe parent that generated this invoiceShow child attributes
- paymentsobjectExpandablePayments for this invoice. Useinvoice paymentto get more details.Show child attributes
- period_endtimestampEnd of the usage period during which invoice items were added to this invoice. This looks back one period for a subscription invoice. Use theline item periodto get the service period for each price.
- period_starttimestampStart of the usage period during which invoice items were added to this invoice. This looks back one period for a subscription invoice. Use theline item periodto get the service period for each price.
- statusnullableenumThe status of the invoice, one ofdraft,open,paid,uncollectible, orvoid.Learn more
- totalintegerTotal after discounts and taxes.

#### idstring

#### auto_advanceboolean

#### automatic_taxobject

#### collection_methodenum

[TABLE]
charge_automaticallyAttempt payment using the default source attached to the customer.
send_invoiceEmail payment instructions to the customer.
[/TABLE]

```
charge_automatically
```

```
send_invoice
```

#### confirmation_secretnullableobjectExpandable

#### currencyenum

#### customerstringExpandable

#### customer_accountnullablestring

#### descriptionnullablestring

#### hosted_invoice_urlnullablestring

#### linesobject

#### metadatanullableobject

#### parentnullableobject

#### paymentsobjectExpandable

#### period_endtimestamp

#### period_starttimestamp

#### statusnullableenum

#### totalinteger

### More attributesExpand all
- objectstring
- account_countrynullablestring
- account_namenullablestring
- account_tax_idsnullablearray of stringsExpandable
- amount_dueinteger
- amount_overpaidinteger
- amount_paidinteger
- amount_remaininginteger
- amount_shippinginteger
- applicationnullablestringExpandableConnect only
- attempt_countinteger
- attemptedboolean
- automatically_finalizes_atnullabletimestamp
- billing_reasonnullableenum
- createdtimestamp
- custom_fieldsnullablearray of objects
- customer_addressnullableobject
- customer_emailnullablestring
- customer_namenullablestring
- customer_phonenullablestring
- customer_shippingnullableobject
- customer_tax_exemptnullableenum
- customer_tax_idsnullablearray of objects
- default_payment_methodnullablestringExpandable
- default_sourcenullablestringExpandable
- default_tax_ratesarray of objects
- discountsarray of stringsExpandable
- due_datenullabletimestamp
- effective_atnullabletimestamp
- ending_balancenullableinteger
- footernullablestring
- from_invoicenullableobject
- invoice_pdfnullablestring
- issuerobjectConnect only
- last_finalization_errornullableobject
- latest_revisionnullablestringExpandable
- livemodeboolean
- next_payment_attemptnullabletimestamp
- numbernullablestring
- on_behalf_ofnullablestringExpandableConnect only
- payment_settingsobject
- post_payment_credit_notes_amountinteger
- pre_payment_credit_notes_amountinteger
- receipt_numbernullablestring
- renderingnullableobject
- shipping_costnullableobject
- shipping_detailsnullableobject
- starting_balanceinteger
- statement_descriptornullablestring
- status_transitionsobject
- subtotalinteger
- subtotal_excluding_taxnullableinteger
- test_clocknullablestringExpandable
- threshold_reasonnullableobject
- total_discount_amountsnullablearray of objects
- total_excluding_taxnullableinteger
- total_pretax_credit_amountsnullablearray of objects
- total_taxesnullablearray of objects
- webhooks_delivered_atnullabletimestamp

#### objectstring

#### account_countrynullablestring

#### account_namenullablestring

#### account_tax_idsnullablearray of stringsExpandable

#### amount_dueinteger

#### amount_overpaidinteger

#### amount_paidinteger

#### amount_remaininginteger

#### amount_shippinginteger

#### applicationnullablestringExpandableConnect only

#### attempt_countinteger

#### attemptedboolean

#### automatically_finalizes_atnullabletimestamp

#### billing_reasonnullableenum

#### createdtimestamp

#### custom_fieldsnullablearray of objects

#### customer_addressnullableobject

#### customer_emailnullablestring

#### customer_namenullablestring

#### customer_phonenullablestring

#### customer_shippingnullableobject

#### customer_tax_exemptnullableenum

#### customer_tax_idsnullablearray of objects

#### default_payment_methodnullablestringExpandable

#### default_sourcenullablestringExpandable

#### default_tax_ratesarray of objects

#### discountsarray of stringsExpandable

#### due_datenullabletimestamp

#### effective_atnullabletimestamp

#### ending_balancenullableinteger

#### footernullablestring

#### from_invoicenullableobject

#### invoice_pdfnullablestring

#### issuerobjectConnect only

#### last_finalization_errornullableobject

#### latest_revisionnullablestringExpandable

#### livemodeboolean

#### next_payment_attemptnullabletimestamp

#### numbernullablestring

#### on_behalf_ofnullablestringExpandableConnect only

#### payment_settingsobject

#### post_payment_credit_notes_amountinteger

#### pre_payment_credit_notes_amountinteger

#### receipt_numbernullablestring

#### renderingnullableobject

#### shipping_costnullableobject

#### shipping_detailsnullableobject

#### starting_balanceinteger

#### statement_descriptornullablestring

#### status_transitionsobject

#### subtotalinteger

#### subtotal_excluding_taxnullableinteger

#### test_clocknullablestringExpandable

#### threshold_reasonnullableobject

#### total_discount_amountsnullablearray of objects

#### total_excluding_taxnullableinteger

#### total_pretax_credit_amountsnullablearray of objects

#### total_taxesnullablearray of objects

#### webhooks_delivered_atnullabletimestamp

```
{"id":"in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"confirmation_secret":null,"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"payments":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoice_payments"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"transfer_data":null,"webhooks_delivered_at":1680644467}
```

```
{"id":"in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"confirmation_secret":null,"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"payments":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoice_payments"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"transfer_data":null,"webhooks_delivered_at":1680644467}
```

# Create a preview invoice
At any time, you can preview the upcoming invoice for a subscription or subscription schedule. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.
You can also preview the effects of creating or updating a subscription or subscription schedule, including a preview of any prorations that will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass thesubscription_details.proration_dateparameter when doing the actual subscription update.
The recommended way to get only the prorations being previewed on the invoice is to consider line items whereparent.subscription_item_details.prorationistrue.
Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.
Note: Currency conversion calculations use the latest exchange rates. Exchange rates may vary between the time of the preview and the time of the actual invoice creation.Learn more

### Parameters
- automatic_taxobjectSettings for automatic tax lookup for this invoice preview.Show child parameters
- customerstringThe identifier of the customer whose upcoming invoice you’re retrieving. Ifautomatic_taxis enabled then one ofcustomer,customer_details,subscription, orschedulemust be set.
- customer_accountstringThe identifier of the account representing the customer whose upcoming invoice you’re retrieving. Ifautomatic_taxis enabled then one ofcustomer,customer_account,customer_details,subscription, orschedulemust be set.
- subscriptionstringThe identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but asubscription_details.itemsis provided, you will preview creating a subscription with those items. If neithersubscriptionnorsubscription_details.itemsis provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.

#### automatic_taxobject

#### customerstring

#### customer_accountstring

#### subscriptionstring

### More parametersExpand all
- currencyenum
- customer_detailsobject
- discountsarray of objects
- invoice_itemsarray of objects
- issuerobjectConnect only
- on_behalf_ofstringConnect only
- preview_modeenum
- schedulestring
- schedule_detailsobject
- subscription_detailsobject

#### currencyenum

#### customer_detailsobject

#### discountsarray of objects

#### invoice_itemsarray of objects

#### issuerobjectConnect only

#### on_behalf_ofstringConnect only

#### preview_modeenum

#### schedulestring

#### schedule_detailsobject

#### subscription_detailsobject

### Returns
Returns an invoice if valid customer information is provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/invoices/create_preview \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_NeZwdNtLEOXuvB
```

```
curlhttps://api.stripe.com/v1/invoices/create_preview \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_NeZwdNtLEOXuvB
```

```
{"id":"upcoming_in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"application_fee_amount":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"webhooks_delivered_at":1680644467}
```

```
{"id":"upcoming_in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"application_fee_amount":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"webhooks_delivered_at":1680644467}
```

# Create an invoice
This endpoint creates a draft invoice for a given customer. The invoice remains a draft until youfinalizethe invoice, which allows you topayorsendthe invoice to your customers.

### Parameters
- auto_advancebooleanControls whether Stripe performsautomatic collectionof the invoice. Iffalse, the invoice’s state doesn’t automatically advance without an explicit action. Defaults to false.
- automatic_taxobjectSettings for automatic tax lookup for this invoice.Show child parameters
- collection_methodenumEithercharge_automatically, orsend_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults tocharge_automatically.Possible enum valuescharge_automaticallysend_invoice
- customerstringRequired unless from_invoice is providedThe ID of the customer to bill.
- customer_accountstringThe ID of the account to bill.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- subscriptionstringThe ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription’s billing cycle and regular subscription events won’t be affected.

#### auto_advanceboolean

#### automatic_taxobject

#### collection_methodenum

[TABLE]
charge_automatically
send_invoice
[/TABLE]

```
charge_automatically
```

```
send_invoice
```

#### customerstringRequired unless from_invoice is provided

#### customer_accountstring

#### descriptionstring

#### metadataobject

#### subscriptionstring

### More parametersExpand all
- account_tax_idsarray of strings
- application_fee_amountintegerConnect only
- automatically_finalizes_attimestamp
- currencyenum
- custom_fieldsarray of objects
- days_until_dueinteger
- default_payment_methodstring
- default_sourcestring
- default_tax_ratesarray of strings
- discountsarray of objects
- due_datetimestamp
- effective_attimestamp
- footerstring
- from_invoiceobjectRequired unless customer is provided
- issuerobjectConnect only
- numberstring
- on_behalf_ofstringConnect only
- payment_settingsobject
- pending_invoice_items_behaviorenum
- renderingobject
- shipping_costobject
- shipping_detailsobject
- statement_descriptorstring
- transfer_dataobjectConnect only

#### account_tax_idsarray of strings

#### application_fee_amountintegerConnect only

#### automatically_finalizes_attimestamp

#### currencyenum

#### custom_fieldsarray of objects

#### days_until_dueinteger

#### default_payment_methodstring

#### default_sourcestring

#### default_tax_ratesarray of strings

#### discountsarray of objects

#### due_datetimestamp

#### effective_attimestamp

#### footerstring

#### from_invoiceobjectRequired unless customer is provided

#### issuerobjectConnect only

#### numberstring

#### on_behalf_ofstringConnect only

#### payment_settingsobject

#### pending_invoice_items_behaviorenum

#### renderingobject

#### shipping_costobject

#### shipping_detailsobject

#### statement_descriptorstring

#### transfer_dataobjectConnect only

### Returns
Returns the invoice object.Raisesan errorif the customer ID provided is invalid.

```
curlhttps://api.stripe.com/v1/invoices \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_NeZwdNtLEOXuvB
```

```
curlhttps://api.stripe.com/v1/invoices \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_NeZwdNtLEOXuvB
```

```
{"id":"in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"webhooks_delivered_at":1680644467}
```

```
{"id":"in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"livemode":false,"metadata":{},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"webhooks_delivered_at":1680644467}
```

# Update an invoice
Draft invoices are fully editable. Once an invoice isfinalized,monetary values, as well ascollection_method, become uneditable.
If you would like to stop the Stripe Billing engine from automatically finalizing, reattempting payments on,sending reminders for, orautomatically reconcilinginvoices, passauto_advance=false.

### Parameters
- auto_advancebooleanControls whether Stripe performsautomatic collectionof the invoice.
- automatic_taxobjectSettings for automatic tax lookup for this invoice.Show child parameters
- collection_methodenumEithercharge_automaticallyorsend_invoice. This field can be updated only ondraftinvoices.Possible enum valuescharge_automaticallysend_invoice
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### auto_advanceboolean

#### automatic_taxobject

#### collection_methodenum

[TABLE]
charge_automatically
send_invoice
[/TABLE]

```
charge_automatically
```

```
send_invoice
```

#### descriptionstring

#### metadataobject

### More parametersExpand all
- account_tax_idsarray of strings
- application_fee_amountintegerConnect only
- automatically_finalizes_attimestamp
- custom_fieldsarray of objects
- days_until_dueinteger
- default_payment_methodstring
- default_sourcestring
- default_tax_ratesarray of strings
- discountsarray of objects
- due_datetimestamp
- effective_attimestamp
- footerstring
- issuerobjectConnect only
- numberstring
- on_behalf_ofstringConnect only
- payment_settingsobject
- renderingobject
- shipping_costobject
- shipping_detailsobject
- statement_descriptorstring
- transfer_dataobjectConnect only

#### account_tax_idsarray of strings

#### application_fee_amountintegerConnect only

#### automatically_finalizes_attimestamp

#### custom_fieldsarray of objects

#### days_until_dueinteger

#### default_payment_methodstring

#### default_sourcestring

#### default_tax_ratesarray of strings

#### discountsarray of objects

#### due_datetimestamp

#### effective_attimestamp

#### footerstring

#### issuerobjectConnect only

#### numberstring

#### on_behalf_ofstringConnect only

#### payment_settingsobject

#### renderingobject

#### shipping_costobject

#### shipping_detailsobject

#### statement_descriptorstring

#### transfer_dataobjectConnect only

### Returns
Returns the invoice object.

```
curlhttps://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"livemode":false,"metadata":{"order_id":"6735"},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"webhooks_delivered_at":1680644467}
```

```
{"id":"in_1MtHbELkdIwHu7ixl4OzzPMv","object":"invoice","account_country":"US","account_name":"Stripe Docs","account_tax_ids":null,"amount_due":0,"amount_paid":0,"amount_overpaid":0,"amount_remaining":0,"amount_shipping":0,"application":null,"attempt_count":0,"attempted":false,"auto_advance":false,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_reason":"manual","collection_method":"charge_automatically","created":1680644467,"currency":"usd","custom_fields":null,"customer":"cus_NeZwdNtLEOXuvB","customer_address":null,"customer_email":"jennyrosen@example.com","customer_name":"Jenny Rosen","customer_phone":null,"customer_shipping":null,"customer_tax_exempt":"none","customer_tax_ids":[],"default_payment_method":null,"default_source":null,"default_tax_rates":[],"description":null,"discounts":[],"due_date":null,"ending_balance":null,"footer":null,"from_invoice":null,"hosted_invoice_url":null,"invoice_pdf":null,"issuer":{"type":"self"},"last_finalization_error":null,"latest_revision":null,"lines":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"},"livemode":false,"metadata":{"order_id":"6735"},"next_payment_attempt":null,"number":null,"on_behalf_of":null,"parent":null,"payment_settings":{"default_mandate":null,"payment_method_options":null,"payment_method_types":null},"period_end":1680644467,"period_start":1680644467,"post_payment_credit_notes_amount":0,"pre_payment_credit_notes_amount":0,"receipt_number":null,"shipping_cost":null,"shipping_details":null,"starting_balance":0,"statement_descriptor":null,"status":"draft","status_transitions":{"finalized_at":null,"marked_uncollectible_at":null,"paid_at":null,"voided_at":null},"subtotal":0,"subtotal_excluding_tax":0,"test_clock":null,"total":0,"total_discount_amounts":[],"total_excluding_tax":0,"total_taxes":[],"webhooks_delivered_at":1680644467}
```