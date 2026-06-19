# charges

*Source: https://docs.stripe.com/api/charges*

---

# Charges
TheChargeobject represents a single attempt to move money into your Stripe account.PaymentIntent confirmation is the most common way to create Charges, butAccount Debitsmay also create Charges.Some legacy payment flows create Charges directly, which is not recommended for new integrations.

# The Charge object

### Attributes
- idstringUnique identifier for the object.
- amountintegerAmount intended to be collected by this payment. A positive integer representing how much to charge in thesmallest currency unit(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US orequivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
- balance_transactionnullablestringExpandableID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).
- billing_detailsobjectBilling information associated with the payment method at the time of the transaction.Show child attributes
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- customernullablestringExpandableID of the customer this charge is for if one exists.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- disputedbooleanWhether the charge has been disputed.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- payment_intentnullablestringExpandableID of the PaymentIntent associated with this charge, if one exists.
- payment_method_detailsnullableobjectDetails about the payment method at the time of the transaction.Show child attributes
- receipt_emailnullablestringThis is the email address that the receipt for this charge was sent to.
- refundedbooleanWhether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.
- shippingnullableobjectShipping information for the charge.Show child attributes
- statement_descriptornullablestringFor a non-card charge, text that appears on the customer’s statement as the statement descriptor. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, seethe Statement Descriptor docs.For a card charge, this value is ignored unless you don’t specify astatement_descriptor_suffix, in which case this value is used as the suffix.
- statement_descriptor_suffixnullablestringProvides information about a card charge. Concatenated to the account’sstatement descriptor prefixto form the complete statement descriptor that appears on the customer’s statement. If the account has no prefix value, the suffix is concatenated to the account’s statement descriptor.
- statusenumThe status of the payment is eithersucceeded,pending, orfailed.

#### idstring

#### amountinteger

#### balance_transactionnullablestringExpandable

#### billing_detailsobject

#### currencyenum

#### customernullablestringExpandable

#### descriptionnullablestring

#### disputedboolean

#### metadataobject

#### payment_intentnullablestringExpandable

#### payment_method_detailsnullableobject

#### receipt_emailnullablestring

#### refundedboolean

#### shippingnullableobject

#### statement_descriptornullablestring

#### statement_descriptor_suffixnullablestring

#### statusenum

### More attributesExpand all
- objectstring
- amount_capturedinteger
- amount_refundedinteger
- applicationnullablestringExpandableConnect only
- application_feenullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- calculated_statement_descriptornullablestring
- capturedboolean
- createdtimestamp
- failure_balance_transactionnullablestringExpandable
- failure_codenullablestring
- failure_messagenullablestring
- fraud_detailsnullableobject
- livemodeboolean
- on_behalf_ofnullablestringExpandableConnect only
- outcomenullableobject
- paidboolean
- payment_methodnullablestring
- presentment_detailsnullableobject
- radar_optionsnullableobject
- receipt_numbernullablestring
- receipt_urlnullablestring
- refundsnullableobjectExpandable
- reviewnullablestringExpandable
- source_transfernullablestringExpandableConnect only
- transfernullablestringExpandableConnect only
- transfer_datanullableobjectConnect only
- transfer_groupnullablestringConnect only

#### objectstring

#### amount_capturedinteger

#### amount_refundedinteger

#### applicationnullablestringExpandableConnect only

#### application_feenullablestringExpandableConnect only

#### application_fee_amountnullableintegerConnect only

#### calculated_statement_descriptornullablestring

#### capturedboolean

#### createdtimestamp

#### failure_balance_transactionnullablestringExpandable

#### failure_codenullablestring

#### failure_messagenullablestring

#### fraud_detailsnullableobject

#### livemodeboolean

#### on_behalf_ofnullablestringExpandableConnect only

#### outcomenullableobject

#### paidboolean

#### payment_methodnullablestring

#### presentment_detailsnullableobject

#### radar_optionsnullableobject

#### receipt_numbernullablestring

#### receipt_urlnullablestring

#### refundsnullableobjectExpandable

#### reviewnullablestringExpandable

#### source_transfernullablestringExpandableConnect only

#### transfernullablestringExpandableConnect only

#### transfer_datanullableobjectConnect only

#### transfer_groupnullablestringConnect only

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY","refunded":false,"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY","refunded":false,"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

# Create a chargeDeprecated
This method is no longer recommended—use thePayment Intents APIto initiate a new payment instead. Confirmation of the PaymentIntent creates theChargeobject used to request payment.

### Parameters
- amountintegerRequiredAmount intended to be collected by this payment. A positive integer representing how much to charge in thesmallest currency unit(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US orequivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- customerstringThe ID of an existing customer that will be charged in this request.The maximum length is 500 characters.
- descriptionstringAn arbitrary string which you can attach to aChargeobject. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include thedescriptionof the charge(s) that they are describing.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- receipt_emailstringThe email address to which this charge’sreceiptwill be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for aCustomer, the email address specified here will override the customer’s email address. Ifreceipt_emailis specified for a charge in live mode, a receipt will be sent regardless of youremail settings.The maximum length is 800 characters.
- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.Show child parameters
- sourcestringA payment source to be charged. This can be the ID of acard(i.e., credit or debit card), abank account, asource, atoken, or aconnected account. For certain sources—namely,cards,bank accounts, and attachedsources—you must also pass the ID of the associated customer.
- statement_descriptorstringFor a non-card charge, text that appears on the customer’s statement as the statement descriptor. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, seethe Statement Descriptor docs.For a card charge, this value is ignored unless you don’t specify astatement_descriptor_suffix, in which case this value is used as the suffix.
- statement_descriptor_suffixstringProvides information about a card charge. Concatenated to the account’sstatement descriptor prefixto form the complete statement descriptor that appears on the customer’s statement. If the account has no prefix value, the suffix is concatenated to the account’s statement descriptor.

#### amountintegerRequired

#### currencyenumRequired

#### customerstring

#### descriptionstring

#### metadataobject

#### receipt_emailstring

#### shippingobject

#### sourcestring

#### statement_descriptorstring

#### statement_descriptor_suffixstring

### More parametersExpand all
- application_fee_amountintegerConnect only
- captureboolean
- on_behalf_ofstringConnect only
- radar_optionsobject
- transfer_dataobjectConnect only
- transfer_groupstringConnect only

#### application_fee_amountintegerConnect only

#### captureboolean

#### on_behalf_ofstringConnect only

#### radar_optionsobject

#### transfer_dataobjectConnect only

#### transfer_groupstringConnect only

### Returns
Returns the charge object if the charge succeeded.This callraisesan errorif something goes wrong.A common source of error is an invalid or expired card,or a valid card with insufficient available balance.

```
curlhttps://api.stripe.com/v1/charges \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1099 \-d currency=usd \-d source=tok_visa
```

```
curlhttps://api.stripe.com/v1/charges \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1099 \-d currency=usd \-d source=tok_visa
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY","refunded":false,"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY","refunded":false,"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

# Update a charge
Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters
- customerstringThe ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.
- descriptionstringAn arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include thedescriptionof the charge(s) that they are describing.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- receipt_emailstringThis is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.
- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.Show child parameters

#### customerstring

#### descriptionstring

#### metadataobject

#### receipt_emailstring

#### shippingobject

### More parametersExpand all
- fraud_detailsobject
- transfer_groupstringConnect only

#### fraud_detailsobject

#### transfer_groupstringConnect only

### Returns
Returns the charge object if the update succeeded. This call willraisean errorif update parameters are invalid.

```
curlhttps://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[shipping]"=express
```

```
curlhttps://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[shipping]"=express
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{"shipping":"express"},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","network_token":{"used":false},"three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KPDLl6UGMgawkab5iK86LBYtkq0XrhiQf1RsA2ubesH4GHiixEU8_1-Wp7h4oQEdfSUGiZpJwtQHBErT","refunded":false,"refunds":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15/refunds"},"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{"shipping":"express"},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","network_token":{"used":false},"three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KPDLl6UGMgawkab5iK86LBYtkq0XrhiQf1RsA2ubesH4GHiixEU8_1-Wp7h4oQEdfSUGiZpJwtQHBErT","refunded":false,"refunds":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15/refunds"},"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

# Retrieve a charge
Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

### Parameters
Noparameters.

### Returns
Returns a charge if a valid identifier was provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY","refunded":false,"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```

```
{"id":"ch_3MmlLrLkdIwHu7ix0snN0B15","object":"charge","amount":1099,"amount_captured":1099,"amount_refunded":0,"application":null,"application_fee":null,"application_fee_amount":null,"balance_transaction":"txn_3MmlLrLkdIwHu7ix0uke3Ezy","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"calculated_statement_descriptor":"Stripe","captured":true,"created":1679090539,"currency":"usd","customer":null,"description":null,"disputed":false,"failure_balance_transaction":null,"failure_code":null,"failure_message":null,"fraud_details":{},"livemode":false,"metadata":{},"on_behalf_of":null,"outcome":{"network_status":"approved_by_network","reason":null,"risk_level":"normal","risk_score":32,"seller_message":"Payment complete.","type":"authorized"},"paid":true,"payment_intent":null,"payment_method":"card_1MmlLrLkdIwHu7ixIJwEWSNR","payment_method_details":{"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","exp_month":3,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","installments":null,"last4":"4242","mandate":null,"network":"visa","three_d_secure":null,"wallet":null},"type":"card"},"receipt_email":null,"receipt_number":null,"receipt_url":"https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY","refunded":false,"review":null,"shipping":null,"source_transfer":null,"statement_descriptor":null,"statement_descriptor_suffix":null,"status":"succeeded","transfer_data":null,"transfer_group":null}
```