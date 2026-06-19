# payment_intents/object

*Source: https://docs.stripe.com/api/payment_intents/object*

---

# The PaymentIntent object

### Attributes
- idstringretrievable with publishable keyUnique identifier for the object.
- amountintegerretrievable with publishable keyAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in thesmallest currency unit(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US orequivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
- automatic_payment_methodsnullableobjectretrievable with publishable keySettings to configure compatible payment methods from theStripe DashboardShow child attributes
- client_secretnullablestringretrievable with publishable keyThe client secret of this PaymentIntent. Used for client-side retrieval using a publishable key.The client secret can be used to complete a payment from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.Refer to our docs toaccept a paymentand learn about howclient_secretshould be handled.
- currencyenumretrievable with publishable keyThree-letterISO currency code, in lowercase. Must be asupported currency.
- customernullablestringExpandableID of the Customer this PaymentIntent belongs to, if one exists.Payment methods attached to other Customers cannot be used with this PaymentIntent.Ifsetup_future_usageis set and this PaymentIntent’s payment method is notcard_present, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method iscard_presentand isn’t a digital wallet, then agenerated_cardpayment method representing the card is created and attached to the Customer instead.
- customer_accountnullablestringID of the Account representing the customer that this PaymentIntent belongs to, if one exists.Payment methods attached to other Accounts cannot be used with this PaymentIntent.Ifsetup_future_usageis set and this PaymentIntent’s payment method is notcard_present, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method iscard_presentand isn’t a digital wallet, then agenerated_cardpayment method representing the card is created and attached to the Account instead.
- descriptionnullablestringretrievable with publishable keyAn arbitrary string attached to the object. Often useful for displaying to users.
- last_payment_errornullableobjectretrievable with publishable keyThe payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason.Show child attributes
- latest_chargenullablestringExpandableID of the latestCharge objectcreated by this PaymentIntent. This property isnulluntil PaymentIntent confirmation is attempted.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Learn more aboutstoring information in metadata.
- next_actionnullableobjectretrievable with publishable keyIf present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source.Show child attributes
- payment_methodnullablestringExpandableretrievable with publishable keyID of the payment method used in this PaymentIntent.
- receipt_emailnullablestringretrievable with publishable keyEmail address that the receipt for the resulting payment will be sent to. Ifreceipt_emailis specified for a payment in live mode, a receipt will be sent regardless of youremail settings.
- setup_future_usagenullableenumretrievable with publishable keyIndicates that you intend to make future payments with this PaymentIntent’s payment method.If you provide a Customer with the PaymentIntent, you can use this parameter toattach the payment methodto the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can stillattachthe payment method to a Customer after the transaction completes.If the payment method iscard_presentand isn’t a digital wallet, Stripe creates and attaches agenerated_cardpayment method representing the card to the Customer instead.When processing card payments, Stripe usessetup_future_usageto help you comply with regional legislation and network rules, such asSCA.Possible enum valuesoff_sessionUseoff_sessionif your customer may or may not be present in your checkout flow.on_sessionUseon_sessionif you intend to only reuse the payment method when your customer is present in your checkout flow.
- shippingnullableobjectretrievable with publishable keyShipping information for this PaymentIntent.Show child attributes
- statement_descriptornullablestringText that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, seethe Statement Descriptor docs.Setting this value for a card charge returns an error. For card charges, set thestatement_descriptor_suffixinstead.
- statement_descriptor_suffixnullablestringProvides information about a card charge. Concatenated to the account’sstatement descriptor prefixto form the complete statement descriptor that appears on the customer’s statement.
- statusenumretrievable with publishable keyStatus of this PaymentIntent, one ofrequires_payment_method,requires_confirmation,requires_action,processing,requires_capture,canceled, orsucceeded. Read more about each PaymentIntentstatus.Possible enum valuescanceledThe PaymentIntent has been canceled.processingThe PaymentIntent is currently being processed.requires_actionThe PaymentIntent requires additional action from the customer.requires_captureThe PaymentIntent has been confirmed and requires capture.requires_confirmationThe PaymentIntent requires confirmation.requires_payment_methodThe PaymentIntent requires a payment method to be attached.succeededThe PaymentIntent has succeeded.

#### idstringretrievable with publishable key

#### amountintegerretrievable with publishable key

#### automatic_payment_methodsnullableobjectretrievable with publishable key

#### client_secretnullablestringretrievable with publishable key

#### currencyenumretrievable with publishable key

#### customernullablestringExpandable

#### customer_accountnullablestring

#### descriptionnullablestringretrievable with publishable key

#### last_payment_errornullableobjectretrievable with publishable key

#### latest_chargenullablestringExpandable

#### metadataobject

#### next_actionnullableobjectretrievable with publishable key

#### payment_methodnullablestringExpandableretrievable with publishable key

#### receipt_emailnullablestringretrievable with publishable key

#### setup_future_usagenullableenumretrievable with publishable key

[TABLE]
off_sessionUseoff_sessionif your customer may or may not be present in your checkout flow.
on_sessionUseon_sessionif you intend to only reuse the payment method when your customer is present in your checkout flow.
[/TABLE]

```
off_session
```

#### shippingnullableobjectretrievable with publishable key

#### statement_descriptornullablestring

#### statement_descriptor_suffixnullablestring

#### statusenumretrievable with publishable key

[TABLE]
canceledThe PaymentIntent has been canceled.
processingThe PaymentIntent is currently being processed.
requires_actionThe PaymentIntent requires additional action from the customer.
requires_captureThe PaymentIntent has been confirmed and requires capture.
requires_confirmationThe PaymentIntent requires confirmation.
requires_payment_methodThe PaymentIntent requires a payment method to be attached.
succeededThe PaymentIntent has succeeded.
[/TABLE]

```
requires_action
```

```
requires_capture
```

```
requires_confirmation
```

```
requires_payment_method
```

### More attributesExpand all
- objectstringretrievable with publishable key
- amount_capturableinteger
- amount_detailsnullableobject
- amount_receivedinteger
- applicationnullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- canceled_atnullabletimestampretrievable with publishable key
- cancellation_reasonnullableenumretrievable with publishable key
- capture_methodenumretrievable with publishable key
- confirmation_methodenumretrievable with publishable key
- createdtimestampretrievable with publishable key
- excluded_payment_method_typesnullablearray of enums
- hooksnullableobject
- livemodebooleanretrievable with publishable key
- on_behalf_ofnullablestringExpandableConnect only
- payment_detailsnullableobject
- payment_method_configuration_detailsnullableobject
- payment_method_optionsnullableobject
- payment_method_typesarray of stringsretrievable with publishable key
- presentment_detailsnullableobject
- processingnullableobjectretrievable with publishable key
- reviewnullablestringExpandable
- transfer_datanullableobjectConnect only
- transfer_groupnullablestringConnect only

#### objectstringretrievable with publishable key

#### amount_capturableinteger

#### amount_detailsnullableobject

#### amount_receivedinteger

#### applicationnullablestringExpandableConnect only

#### application_fee_amountnullableintegerConnect only

#### canceled_atnullabletimestampretrievable with publishable key

#### cancellation_reasonnullableenumretrievable with publishable key

#### capture_methodenumretrievable with publishable key

#### confirmation_methodenumretrievable with publishable key

#### createdtimestampretrievable with publishable key

#### excluded_payment_method_typesnullablearray of enums

#### hooksnullableobject

#### livemodebooleanretrievable with publishable key

#### on_behalf_ofnullablestringExpandableConnect only

#### payment_detailsnullableobject

#### payment_method_configuration_detailsnullableobject

#### payment_method_optionsnullableobject

#### payment_method_typesarray of stringsretrievable with publishable key

#### presentment_detailsnullableobject

#### processingnullableobjectretrievable with publishable key

#### reviewnullablestringExpandable

#### transfer_datanullableobjectConnect only

#### transfer_groupnullablestringConnect only

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

# Create a PaymentIntent
Creates a PaymentIntent object.
After the PaymentIntent is created, attach a payment method andconfirmto continue the payment. Learn more aboutthe available payment flowswith the Payment Intents API.
When you useconfirm=trueduring creation, it’s equivalent to creatingand confirming the PaymentIntent in the same call. You can use any parametersavailable in theconfirm APIwhen you supplyconfirm=true.

### Parameters
- amountintegerRequiredAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in thesmallest currency unit(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US orequivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- automatic_payment_methodsobjectWhen you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent’s other parameters.Show child parameters
- confirmbooleanSet totrueto attempt toconfirm this PaymentIntentimmediately. This parameter defaults tofalse. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in theConfirm API.
- customerstringID of the Customer this PaymentIntent belongs to, if one exists.Payment methods attached to other Customers cannot be used with this PaymentIntent.Ifsetup_future_usageis set and this PaymentIntent’s payment method is notcard_present, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method iscard_presentand isn’t a digital wallet, then agenerated_cardpayment method representing the card is created and attached to the Customer instead.
- customer_accountstringID of the Account representing the customer that this PaymentIntent belongs to, if one exists.Payment methods attached to other Accounts cannot be used with this PaymentIntent.Ifsetup_future_usageis set and this PaymentIntent’s payment method is notcard_present, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method iscard_presentand isn’t a digital wallet, then agenerated_cardpayment method representing the card is created and attached to the Account instead.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- off_sessionboolean | stringonly when confirm=trueSet totrueto indicate that the customer isn’t in your checkout flow during this payment attempt and can’t authenticate. Use this parameter in scenarios where you collect card details andcharge them later. This parameter can only be used withconfirm=true.
- payment_methodstringID of the payment method (a PaymentMethod, Card, orcompatible Sourceobject) to attach to this PaymentIntent.If you omit this parameter withconfirm=true,customer.default_sourceattaches as this PaymentIntent’s payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide thepayment_methodmoving forward.If the payment method is attached to a Customer, you must also provide the ID of that Customer as thecustomerparameter of this PaymentIntent.
- receipt_emailstringEmail address to send the receipt to. If you specifyreceipt_emailfor a payment in live mode, you send a receipt regardless of youremail settings.
- setup_future_usageenumIndicates that you intend to make future payments with this PaymentIntent’s payment method.If you provide a Customer with the PaymentIntent, you can use this parameter toattach the payment methodto the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can stillattachthe payment method to a Customer after the transaction completes.If the payment method iscard_presentand isn’t a digital wallet, Stripe creates and attaches agenerated_cardpayment method representing the card to the Customer instead.When processing card payments, Stripe usessetup_future_usageto help you comply with regional legislation and network rules, such asSCA.Possible enum valuesoff_sessionUseoff_sessionif your customer may or may not be present in your checkout flow.on_sessionUseon_sessionif you intend to only reuse the payment method when your customer is present in your checkout flow.
- shippingobjectShipping information for this PaymentIntent.Show child parameters
- statement_descriptorstringText that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, seethe Statement Descriptor docs.Setting this value for a card charge returns an error. For card charges, set thestatement_descriptor_suffixinstead.
- statement_descriptor_suffixstringProvides information about a card charge. Concatenated to the account’sstatement descriptor prefixto form the complete statement descriptor that appears on the customer’s statement.

#### amountintegerRequired

#### currencyenumRequired

#### automatic_payment_methodsobject

#### confirmboolean

#### customerstring

#### customer_accountstring

#### descriptionstring

#### metadataobject

#### off_sessionboolean | stringonly when confirm=true

```
confirm=true
```

#### payment_methodstring

#### receipt_emailstring

#### setup_future_usageenum

[TABLE]
off_sessionUseoff_sessionif your customer may or may not be present in your checkout flow.
on_sessionUseon_sessionif you intend to only reuse the payment method when your customer is present in your checkout flow.
[/TABLE]

```
off_session
```

#### shippingobject

#### statement_descriptorstring

#### statement_descriptor_suffixstring

### More parametersExpand all
- amount_detailsobject
- application_fee_amountintegerConnect only
- capture_methodenum
- confirmation_methodenum
- confirmation_tokenstringonly when confirm=true
- error_on_requires_actionbooleanonly when confirm=true
- excluded_payment_method_typesarray of enums
- hooksobject
- mandatestringonly when confirm=true
- mandate_dataobjectonly when confirm=true
- on_behalf_ofstringConnect only
- payment_detailsobject
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings
- radar_optionsobject
- return_urlstringonly when confirm=true
- transfer_dataobjectConnect only
- transfer_groupstringConnect only
- use_stripe_sdkboolean

#### amount_detailsobject

#### application_fee_amountintegerConnect only

#### capture_methodenum

#### confirmation_methodenum

#### confirmation_tokenstringonly when confirm=true

#### error_on_requires_actionbooleanonly when confirm=true

#### excluded_payment_method_typesarray of enums

#### hooksobject

#### mandatestringonly when confirm=true

#### mandate_dataobjectonly when confirm=true

#### on_behalf_ofstringConnect only

#### payment_detailsobject

#### payment_method_configurationstring

#### payment_method_dataobject

#### payment_method_optionsobject

#### payment_method_typesarray of strings

#### radar_optionsobject

#### return_urlstringonly when confirm=true

#### transfer_dataobjectConnect only

#### transfer_groupstringConnect only

#### use_stripe_sdkboolean

### Returns
Returns a PaymentIntent object.

```
curlhttps://api.stripe.com/v1/payment_intents \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=2000 \-d currency=usd \-d"automatic_payment_methods[enabled]"=true
```

```
curlhttps://api.stripe.com/v1/payment_intents \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=2000 \-d currency=usd \-d"automatic_payment_methods[enabled]"=true
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

# Update a PaymentIntent
Updates properties on a PaymentIntent object without confirming.
Depending on which properties you update, you might need to confirm thePaymentIntent again. For example, updating thepayment_methodalways requires you to confirm the PaymentIntent again. If you prefer toupdate and confirm at the same time, we recommend updating properties throughtheconfirm APIinstead.

### Parameters
- amountintegerAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in thesmallest currency unit(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US orequivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- customerstringID of the Customer this PaymentIntent belongs to, if one exists.Payment methods attached to other Customers cannot be used with this PaymentIntent.Ifsetup_future_usageis set and this PaymentIntent’s payment method is notcard_present, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method iscard_presentand isn’t a digital wallet, then agenerated_cardpayment method representing the card is created and attached to the Customer instead.
- customer_accountstringID of the Account representing the customer that this PaymentIntent belongs to, if one exists.Payment methods attached to other Accounts cannot be used with this PaymentIntent.Ifsetup_future_usageis set and this PaymentIntent’s payment method is notcard_present, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method iscard_presentand isn’t a digital wallet, then agenerated_cardpayment method representing the card is created and attached to the Account instead.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- payment_methodstringID of the payment method (a PaymentMethod, Card, orcompatible Sourceobject) to attach to this PaymentIntent. To unset this field to null, pass in an empty string.
- receipt_emailstringEmail address that the receipt for the resulting payment will be sent to. Ifreceipt_emailis specified for a payment in live mode, a receipt will be sent regardless of youremail settings.
- setup_future_usageenumIndicates that you intend to make future payments with this PaymentIntent’s payment method.If you provide a Customer with the PaymentIntent, you can use this parameter toattach the payment methodto the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can stillattachthe payment method to a Customer after the transaction completes.If the payment method iscard_presentand isn’t a digital wallet, Stripe creates and attaches agenerated_cardpayment method representing the card to the Customer instead.When processing card payments, Stripe usessetup_future_usageto help you comply with regional legislation and network rules, such asSCA.If you’ve already setsetup_future_usageand you’re performing a request using a publishable key, you can only update the value fromon_sessiontooff_session.Possible enum valuesoff_sessionUseoff_sessionif your customer may or may not be present in your checkout flow.on_sessionUseon_sessionif you intend to only reuse the payment method when your customer is present in your checkout flow.
- shippingobjectShipping information for this PaymentIntent.Show child parameters
- statement_descriptorstringText that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, seethe Statement Descriptor docs.Setting this value for a card charge returns an error. For card charges, set thestatement_descriptor_suffixinstead.
- statement_descriptor_suffixstringProvides information about a card charge. Concatenated to the account’sstatement descriptor prefixto form the complete statement descriptor that appears on the customer’s statement.

#### amountinteger

#### currencyenum

#### customerstring

#### customer_accountstring

#### descriptionstring

#### metadataobject

#### payment_methodstring

#### receipt_emailstring

#### setup_future_usageenum

[TABLE]
off_sessionUseoff_sessionif your customer may or may not be present in your checkout flow.
on_sessionUseon_sessionif you intend to only reuse the payment method when your customer is present in your checkout flow.
[/TABLE]

```
off_session
```

#### shippingobject

#### statement_descriptorstring

#### statement_descriptor_suffixstring

### More parametersExpand all
- amount_detailsobject
- application_fee_amountintegerConnect only
- capture_methodenumsecret key only
- excluded_payment_method_typesarray of enums
- hooksobject
- payment_detailsobject
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings
- transfer_dataobjectConnect only
- transfer_groupstringConnect only

#### amount_detailsobject

#### application_fee_amountintegerConnect only

#### capture_methodenumsecret key only

#### excluded_payment_method_typesarray of enums

#### hooksobject

#### payment_detailsobject

#### payment_method_configurationstring

#### payment_method_dataobject

#### payment_method_optionsobject

#### payment_method_typesarray of strings

#### transfer_dataobjectConnect only

#### transfer_groupstringConnect only

### Returns
Returns a PaymentIntent object.

```
curlhttps://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{"order_id":"6735"},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{"order_id":"6735"},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

# Retrieve a PaymentIntent
Retrieves the details of a PaymentIntent that has previously been created.
You can retrieve a PaymentIntent client-side using a publishable key when theclient_secretis in the query string.
If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to thepayment intentobject reference for more details.

### Parameters
- client_secretstringRequired if you use a publishable key.The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.

#### client_secretstringRequired if you use a publishable key.

### Returns
Returns a PaymentIntent if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

```
{"id":"pi_3MtwBwLkdIwHu7ix28a3tqPa","object":"payment_intent","amount":2000,"amount_capturable":0,"amount_details":{"tip":{}},"amount_received":0,"application":null,"application_fee_amount":null,"automatic_payment_methods":{"enabled":true},"canceled_at":null,"cancellation_reason":null,"capture_method":"automatic","client_secret":"pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH","confirmation_method":"automatic","created":1680800504,"currency":"usd","customer":null,"description":null,"last_payment_error":null,"latest_charge":null,"livemode":false,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"installments":null,"mandate_options":null,"network":null,"request_three_d_secure":"automatic"},"link":{"persistent_token":null}},"payment_method_types":["card","link"],"processing":null,"receipt_email":null,"review":null,"setup_future_usage":null,"shipping":null,"source":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"requires_payment_method","transfer_data":null,"transfer_group":null}
```

# List all PaymentIntent LineItems
Lists all LineItems of a given PaymentIntent.

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
Adictionarywith adataproperty that contains an array of up tolimitline items of the given PaymentIntent, starting after line itemstarting_after. Each entry in the array is a separate line item object. If no other line items are available, the resulting array is empty.

```
curlhttps://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/amount_details_line_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/amount_details_line_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"list","url":"/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/amount_details_line_items","has_more":false,"data":[{"id":"uli_T1KmwLEvkprqQb","object":"payment_intent_amount_details_line_item","discount_amount":50,"payment_method_options":null,"product_code":"SKU001","product_name":"Product 001","quantity":1,"tax":{"total_tax_amount":20},"unit_cost":2000,"unit_of_measure":"each"}]}
```

```
{"object":"list","url":"/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/amount_details_line_items","has_more":false,"data":[{"id":"uli_T1KmwLEvkprqQb","object":"payment_intent_amount_details_line_item","discount_amount":50,"payment_method_options":null,"product_code":"SKU001","product_name":"Product 001","quantity":1,"tax":{"total_tax_amount":20},"unit_cost":2000,"unit_of_measure":"each"}]}
```