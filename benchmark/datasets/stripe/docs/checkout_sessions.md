# checkout/sessions

*Source: https://docs.stripe.com/api/checkout/sessions*

---

# Checkout Sessions
A Checkout Session represents your customer’s session as they pay forone-time purchases or subscriptions throughCheckoutorPayment Links. We recommend creating anew Session each time your customer attempts to pay.
Once payment is successful, the Checkout Session will contain a referenceto theCustomer, and either the successfulPaymentIntentor an activeSubscription.
You can create a Checkout Session on your server and redirect to its URLto begin Checkout.
Related guide:Checkout quickstart

# The Checkout Session object

### Attributes
- idstringUnique identifier for the object.
- automatic_taxobjectDetails on the state of automatic tax for the session, including the status of the latest tax calculation.Show child attributes
- client_reference_idnullablestringA unique string to reference the Checkout Session. This can be acustomer ID, a cart ID, or similar, and can be used to reconcile theSession with your internal systems.
- currencynullableenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- customernullablestringExpandableThe ID of the customer for this Session.For Checkout Sessions insubscriptionmode or Checkout Sessions withcustomer_creationset asalwaysinpaymentmode, Checkoutwill create a new customer object based on information providedduring the payment flow unless an existing customer was provided whenthe Session was created.
- customer_emailnullablestringIf provided, this value will be used when the Customer object is created.If not provided, customers will be asked to enter their email address.Use this parameter to prefill customer data if you already have an emailon file. To access information about the customer once the payment flow iscomplete, use thecustomerattribute.
- line_itemsnullableobjectExpandableThe line items purchased by the customer.Show child attributes
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- modeenumThe mode of the Checkout Session.Possible enum valuespaymentAccept one-time payments for cards, iDEAL, and more.setupSave payment details to charge your customers later.subscriptionUse Stripe Billing to set up fixed-price subscriptions.
- payment_intentnullablestringExpandableThe ID of the PaymentIntent for Checkout Sessions inpaymentmode. You can’t confirm or cancel the PaymentIntent for a Checkout Session. To cancel,expire the Checkout Sessioninstead.
- payment_statusenumThe payment status of the Checkout Session, one ofpaid,unpaid, orno_payment_required.You can use this value to decide when to fulfill your customer’s order.Possible enum valuesno_payment_requiredThe payment is delayed to a future date, or the Checkout Session is insetupmode and doesn’t require a payment at this time.paidThe payment funds are available in your account.unpaidThe payment funds are not yet available in your account.
- return_urlnullablestringApplies to Checkout Sessions withui_mode: embeddedorui_mode: custom. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site.
- statusnullableenumThe status of the Checkout Session, one ofopen,complete, orexpired.Possible enum valuescompleteThe checkout session is complete. Payment processing may still be in progressexpiredThe checkout session has expired. No further processing will occuropenThe checkout session is still in progress. Payment processing has not started
- success_urlnullablestringThe URL the customer will be directed to after the payment orsubscription creation is successful.
- ui_modenullableenumThe UI mode of the Session. Defaults tohosted.Possible enum valuescustomThe Checkout Session will be displayed usingembedded componentson your websiteembeddedThe Checkout Session will be displayed as an embedded form on your website.hostedThe Checkout Session will be displayed on a hosted page that customers will be redirected to.
- urlnullablestringThe URL to the Checkout Session. Applies to Checkout Sessions withui_mode: hosted. Redirect customers to this URL to take them to Checkout. If you’re usingCustom Domains, the URL will use your subdomain. Otherwise, it’ll usecheckout.stripe.com.This value is only present when the session is active.

#### idstring

#### automatic_taxobject

#### client_reference_idnullablestring

#### currencynullableenum

#### customernullablestringExpandable

#### customer_emailnullablestring

#### line_itemsnullableobjectExpandable

#### metadatanullableobject

#### modeenum

[TABLE]
paymentAccept one-time payments for cards, iDEAL, and more.
setupSave payment details to charge your customers later.
subscriptionUse Stripe Billing to set up fixed-price subscriptions.
[/TABLE]

```
subscription
```

#### payment_intentnullablestringExpandable

#### payment_statusenum

[TABLE]
no_payment_requiredThe payment is delayed to a future date, or the Checkout Session is insetupmode and doesn’t require a payment at this time.
paidThe payment funds are available in your account.
unpaidThe payment funds are not yet available in your account.
[/TABLE]

```
no_payment_required
```

#### return_urlnullablestring

#### statusnullableenum

[TABLE]
completeThe checkout session is complete. Payment processing may still be in progress
expiredThe checkout session has expired. No further processing will occur
openThe checkout session is still in progress. Payment processing has not started
[/TABLE]

#### success_urlnullablestring

#### ui_modenullableenum

[TABLE]
customThe Checkout Session will be displayed usingembedded componentson your website
embeddedThe Checkout Session will be displayed as an embedded form on your website.
hostedThe Checkout Session will be displayed on a hosted page that customers will be redirected to.
[/TABLE]

#### urlnullablestring

### More attributesExpand all
- objectstring
- adaptive_pricingnullableobject
- after_expirationnullableobject
- allow_promotion_codesnullableboolean
- amount_subtotalnullableinteger
- amount_totalnullableinteger
- billing_address_collectionnullableenum
- branding_settingsnullableobject
- cancel_urlnullablestring
- client_secretnullablestring
- collected_informationnullableobject
- consentnullableobject
- consent_collectionnullableobject
- createdtimestamp
- currency_conversionnullableobject
- custom_fieldsarray of objects
- custom_textobject
- customer_accountnullablestring
- customer_creationnullableenum
- customer_detailsnullableobject
- discountsnullablearray of objects
- excluded_payment_method_typesnullablearray of strings
- expires_attimestamp
- invoicenullablestringExpandable
- invoice_creationnullableobject
- livemodeboolean
- localenullableenum
- name_collectionnullableobject
- optional_itemsnullablearray of objectsExpandable
- origin_contextnullableenum
- payment_linknullablestringExpandable
- payment_method_collectionnullableenum
- payment_method_configuration_detailsnullableobject
- payment_method_optionsnullableobject
- payment_method_typesarray of strings
- permissionsnullableobject
- phone_number_collectionnullableobject
- presentment_detailsnullableobject
- recovered_fromnullablestring
- redirect_on_completionnullableenum
- saved_payment_method_optionsnullableobject
- setup_intentnullablestringExpandable
- shipping_address_collectionnullableobject
- shipping_costnullableobject
- shipping_optionsarray of objects
- submit_typenullableenum
- subscriptionnullablestringExpandable
- tax_id_collectionnullableobject
- total_detailsnullableobject
- wallet_optionsnullableobject

#### objectstring

#### adaptive_pricingnullableobject

#### after_expirationnullableobject

#### allow_promotion_codesnullableboolean

#### amount_subtotalnullableinteger

#### amount_totalnullableinteger

#### billing_address_collectionnullableenum

#### branding_settingsnullableobject

#### cancel_urlnullablestring

#### client_secretnullablestring

#### collected_informationnullableobject

#### consentnullableobject

#### consent_collectionnullableobject

#### createdtimestamp

#### currency_conversionnullableobject

#### custom_fieldsarray of objects

#### custom_textobject

#### customer_accountnullablestring

#### customer_creationnullableenum

#### customer_detailsnullableobject

#### discountsnullablearray of objects

#### excluded_payment_method_typesnullablearray of strings

#### expires_attimestamp

#### invoicenullablestringExpandable

#### invoice_creationnullableobject

#### livemodeboolean

#### localenullableenum

#### name_collectionnullableobject

#### optional_itemsnullablearray of objectsExpandable

#### origin_contextnullableenum

#### payment_linknullablestringExpandable

#### payment_method_collectionnullableenum

#### payment_method_configuration_detailsnullableobject

#### payment_method_optionsnullableobject

#### payment_method_typesarray of strings

#### permissionsnullableobject

#### phone_number_collectionnullableobject

#### presentment_detailsnullableobject

#### recovered_fromnullablestring

#### redirect_on_completionnullableenum

#### saved_payment_method_optionsnullableobject

#### setup_intentnullablestringExpandable

#### shipping_address_collectionnullableobject

#### shipping_costnullableobject

#### shipping_optionsarray of objects

#### submit_typenullableenum

#### subscriptionnullablestringExpandable

#### tax_id_collectionnullableobject

#### total_detailsnullableobject

#### wallet_optionsnullableobject

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

# Create a Checkout Session
Creates a Checkout Session object.

### Parameters
- automatic_taxobjectSettings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions.Show child parameters
- client_reference_idstringA unique string to reference the Checkout Session. This can be acustomer ID, a cart ID, or similar, and can be used to reconcile thesession with your internal systems.The maximum length is 200 characters.
- customerstringID of an existing Customer, if one exists. Inpaymentmode, the customer’s most recently saved cardpayment method will be used to prefill the email, name, card details, and billing addresson the Checkout page. Insubscriptionmode, the customer’sdefault payment methodwill be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer’s card details.If the Customer already has a validemailset, the email will be prefilled and not editable in Checkout.If the Customer does not have a validemail, Checkout will set the email entered during the session on the Customer.If blank for Checkout Sessions insubscriptionmode or withcustomer_creationset asalwaysinpaymentmode, Checkout will create a new Customer object based on information provided during the payment flow.You can setpayment_intent_data.setup_future_usageto have Checkout automatically attach the payment method to the Customer you pass in for future reuse.
- customer_emailstringIf provided, this value will be used when the Customer object is created.If not provided, customers will be asked to enter their email address.Use this parameter to prefill customer data if you already have an emailon file. To access information about the customer once a session iscomplete, use thecustomerfield.The maximum length is 800 characters.
- line_itemsarray of objectsRequired conditionallyA list of items the customer is purchasing. Use this parameter to pass one-time or recurringPrices. The parameter is required forpaymentandsubscriptionmode.Forpaymentmode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.Forsubscriptionmode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- modeenumRequiredThe mode of the Checkout Session. Passsubscriptionif the Checkout Session includes at least one recurring item.Possible enum valuespaymentAccept one-time payments for cards, iDEAL, and more.setupSave payment details to charge your customers later.subscriptionUse Stripe Billing to set up fixed-price subscriptions.
- return_urlstringRequired conditionallyThe URL to redirect your customer back to after they authenticate or cancel their payment on thepayment method’s app or site. This parameter is required ifui_modeisembeddedorcustomand redirect-based payment methods are enabled on the session.
- success_urlstringRequired conditionallyThe URL to which Stripe should send customers when payment or setupis complete.This parameter is not allowed if ui_mode isembeddedorcustom. If you’d like to useinformation from the successful Checkout Session on your page, read theguide oncustomizing your success page.
- ui_modeenumThe UI mode of the Session. Defaults tohosted.Possible enum valuescustomThe Checkout Session will be displayed usingembedded componentson your websiteembeddedThe Checkout Session will be displayed as an embedded form on your website.hostedThe Checkout Session will be displayed on a hosted page that customers will be redirected to.

#### automatic_taxobject

#### client_reference_idstring

#### customerstring

```
payment_intent_data.setup_future_usage
```

#### customer_emailstring

#### line_itemsarray of objectsRequired conditionally

#### metadataobject

#### modeenumRequired

[TABLE]
paymentAccept one-time payments for cards, iDEAL, and more.
setupSave payment details to charge your customers later.
subscriptionUse Stripe Billing to set up fixed-price subscriptions.
[/TABLE]

```
subscription
```

#### return_urlstringRequired conditionally

#### success_urlstringRequired conditionally

#### ui_modeenum

[TABLE]
customThe Checkout Session will be displayed usingembedded componentson your website
embeddedThe Checkout Session will be displayed as an embedded form on your website.
hostedThe Checkout Session will be displayed on a hosted page that customers will be redirected to.
[/TABLE]

### More parametersExpand all
- adaptive_pricingobject
- after_expirationobject
- allow_promotion_codesboolean
- billing_address_collectionenum
- branding_settingsobject
- cancel_urlstring
- consent_collectionobject
- currencyenumRequired conditionally
- custom_fieldsarray of objects
- custom_textobject
- customer_accountstring
- customer_creationenum
- customer_updateobject
- discountsarray of objects
- excluded_payment_method_typesarray of enums
- expires_attimestamp
- invoice_creationobject
- localeenum
- name_collectionobject
- optional_itemsarray of objects
- origin_contextenum
- payment_intent_dataobject
- payment_method_collectionenum
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of enums
- permissionsobject
- phone_number_collectionobject
- redirect_on_completionenum
- saved_payment_method_optionsobject
- setup_intent_dataobject
- shipping_address_collectionobject
- shipping_optionsarray of objects
- submit_typeenum
- subscription_dataobject
- tax_id_collectionobject
- wallet_optionsobject

#### adaptive_pricingobject

#### after_expirationobject

#### allow_promotion_codesboolean

#### billing_address_collectionenum

#### branding_settingsobject

#### cancel_urlstring

#### consent_collectionobject

#### currencyenumRequired conditionally

#### custom_fieldsarray of objects

#### custom_textobject

#### customer_accountstring

#### customer_creationenum

#### customer_updateobject

#### discountsarray of objects

#### excluded_payment_method_typesarray of enums

#### expires_attimestamp

#### invoice_creationobject

#### localeenum

#### name_collectionobject

#### optional_itemsarray of objects

#### origin_contextenum

#### payment_intent_dataobject

#### payment_method_collectionenum

#### payment_method_configurationstring

#### payment_method_dataobject

#### payment_method_optionsobject

#### payment_method_typesarray of enums

#### permissionsobject

#### phone_number_collectionobject

#### redirect_on_completionenum

#### saved_payment_method_optionsobject

#### setup_intent_dataobject

#### shipping_address_collectionobject

#### shipping_optionsarray of objects

#### submit_typeenum

#### subscription_dataobject

#### tax_id_collectionobject

#### wallet_optionsobject

### Returns
Returns a Checkout Session object.

```
curlhttps://api.stripe.com/v1/checkout/sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\--data-urlencode success_url="https://example.com/success"\-d"line_items[0][price]"=price_1MotwRLkdIwHu7ixYcPLm5uZ \-d"line_items[0][quantity]"=2 \-d mode=payment
```

```
curlhttps://api.stripe.com/v1/checkout/sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\--data-urlencode success_url="https://example.com/success"\-d"line_items[0][price]"=price_1MotwRLkdIwHu7ixYcPLm5uZ \-d"line_items[0][quantity]"=2 \-d mode=payment
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

# Update a Checkout Session
Updates a Checkout Session object.
Related guide:Dynamically update a Checkout Session

### Parameters
- line_itemsarray of objectsA list of items the customer is purchasing.When updating line items, you must retransmit the entire array of line items.To retain an existing line item, specify itsid.To update an existing line item, specify itsidalong with the new values of the fields to update.To add a new line item, specify one ofpriceorprice_dataandquantity.To remove an existing line item, omit the line item’s ID from the retransmitted array.To reorder a line item, specify it at the desired position in the retransmitted array.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### line_itemsarray of objects

#### metadataobject

### More parametersExpand all
- collected_informationobject
- shipping_optionsarray of objects

#### collected_informationobject

#### shipping_optionsarray of objects

### Returns
Returns a Checkout Session object.

```
curlhttps://api.stripe.com/v1/checkout/sessions/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/checkout/sessions/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{"order_id":"6735"},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{"order_id":"6735"},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

# Retrieve a Checkout Session
Retrieves a Checkout Session object.

### Parameters
Noparameters.

### Returns
Returns a Checkout Session object.

```
curlhttps://api.stripe.com/v1/checkout/sessions/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/checkout/sessions/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```

```
{"id":"cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u","object":"checkout.session","after_expiration":null,"allow_promotion_codes":null,"amount_subtotal":2198,"amount_total":2198,"automatic_tax":{"enabled":false,"liability":null,"status":null},"billing_address_collection":null,"cancel_url":null,"client_reference_id":null,"consent":null,"consent_collection":null,"created":1679600215,"currency":"usd","custom_fields":[],"custom_text":{"shipping_address":null,"submit":null},"customer":null,"customer_creation":"if_required","customer_details":null,"customer_email":null,"expires_at":1679686615,"invoice":null,"invoice_creation":{"enabled":false,"invoice_data":{"account_tax_ids":null,"custom_fields":null,"description":null,"footer":null,"issuer":null,"metadata":{},"rendering_options":null}},"livemode":false,"locale":null,"metadata":{},"mode":"payment","payment_intent":null,"payment_link":null,"payment_method_collection":"always","payment_method_options":{},"payment_method_types":["card"],"payment_status":"unpaid","phone_number_collection":{"enabled":false},"recovered_from":null,"setup_intent":null,"shipping_address_collection":null,"shipping_cost":null,"shipping_details":null,"shipping_options":[],"status":"open","submit_type":null,"subscription":null,"success_url":"https://example.com/success","total_details":{"amount_discount":0,"amount_shipping":0,"amount_tax":0},"url":"https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}
```