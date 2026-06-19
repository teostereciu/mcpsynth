# confirmation_tokens

*Source: https://docs.stripe.com/api/confirmation_tokens*

---

# Confirmation Token
ConfirmationTokens help transport client side data collected by Stripe JS overto your server for confirming a PaymentIntent or SetupIntent. If the confirmationis successful, values present on the ConfirmationToken are written onto the Intent.
To learn more about how to use ConfirmationToken, visit the related guides:
- Finalize payments on the server
- Build two-step confirmation.

# The Confirmation Token object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- expires_atnullabletimestampTime at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- mandate_datanullableobjectData used for generating a Mandate.Show child attributes
- payment_intentnullablestringID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.
- payment_method_optionsnullableobjectPayment-method-specific configuration for this ConfirmationToken.Show child attributes
- payment_method_previewnullableobjectPayment details collected by the Payment Element, used to create a PaymentMethod when a PaymentIntent or SetupIntent is confirmed with this ConfirmationToken.Show child attributes
- return_urlnullablestringReturn URL used to confirm the Intent.
- setup_future_usagenullableenumIndicates that you intend to make future payments with this ConfirmationToken’s payment method.The presence of this property willattach the payment methodto the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.Possible enum valuesoff_sessionUseoff_sessionif your customer_id may or may not be present in your checkout flow.on_sessionUseon_sessionif you intend to only reuse the payment method when your customer_id is present in your checkout flow.
- setup_intentnullablestringID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.
- shippingnullableobjectShipping information collected on this ConfirmationToken.Show child attributes
- use_stripe_sdkbooleanIndicates whether the Stripe SDK is used to handle confirmation flow. Defaults totrueon ConfirmationToken.

#### idstring

#### objectstring

#### createdtimestamp

#### expires_atnullabletimestamp

#### livemodeboolean

#### mandate_datanullableobject

#### payment_intentnullablestring

#### payment_method_optionsnullableobject

#### payment_method_previewnullableobject

#### return_urlnullablestring

#### setup_future_usagenullableenum

[TABLE]
off_sessionUseoff_sessionif your customer_id may or may not be present in your checkout flow.
on_sessionUseon_sessionif you intend to only reuse the payment method when your customer_id is present in your checkout flow.
[/TABLE]

```
off_session
```

#### setup_intentnullablestring

#### shippingnullableobject

#### use_stripe_sdkboolean

```
{"id":"ctoken_1NnQUf2eZvKYlo2CIObdtbnb","object":"confirmation_token","created":1694025025,"expires_at":1694068225,"livemode":true,"mandate_data":null,"payment_intent":null,"payment_instrument":null,"payment_method_preview":{"billing_details":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"email":"jennyrosen@stripe.com","name":"Jenny Rosen","phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","display_brand":"visa","exp_month":8,"exp_year":2026,"funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"type":"card"},"return_url":"https://example.com/return","setup_future_usage":"off_session","setup_intent":null,"shipping":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"name":"Jenny Rosen","phone":null}}
```

```
{"id":"ctoken_1NnQUf2eZvKYlo2CIObdtbnb","object":"confirmation_token","created":1694025025,"expires_at":1694068225,"livemode":true,"mandate_data":null,"payment_intent":null,"payment_instrument":null,"payment_method_preview":{"billing_details":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"email":"jennyrosen@stripe.com","name":"Jenny Rosen","phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","display_brand":"visa","exp_month":8,"exp_year":2026,"funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"type":"card"},"return_url":"https://example.com/return","setup_future_usage":"off_session","setup_intent":null,"shipping":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"name":"Jenny Rosen","phone":null}}
```

# Retrieve a ConfirmationToken
Retrieves an existing ConfirmationToken object

### Parameters
Noparameters.

### Returns
Returns the specified ConfirmationToken

```
curlhttps://api.stripe.com/v1/confirmation_tokens/ctoken_1NnQUf2eZvKYlo2CIObdtbnb \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/confirmation_tokens/ctoken_1NnQUf2eZvKYlo2CIObdtbnb \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ctoken_1NnQUf2eZvKYlo2CIObdtbnb","object":"confirmation_token","created":1694025025,"expires_at":1694068225,"livemode":true,"mandate_data":null,"payment_intent":null,"payment_instrument":null,"payment_method_preview":{"billing_details":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"email":"jennyrosen@stripe.com","name":"Jenny Rosen","phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","display_brand":"visa","exp_month":8,"exp_year":2026,"funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"type":"card"},"return_url":"https://example.com/return","setup_future_usage":"off_session","setup_intent":null,"shipping":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"name":"Jenny Rosen","phone":null}}
```

```
{"id":"ctoken_1NnQUf2eZvKYlo2CIObdtbnb","object":"confirmation_token","created":1694025025,"expires_at":1694068225,"livemode":true,"mandate_data":null,"payment_intent":null,"payment_instrument":null,"payment_method_preview":{"billing_details":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"email":"jennyrosen@stripe.com","name":"Jenny Rosen","phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":null},"country":"US","display_brand":"visa","exp_month":8,"exp_year":2026,"funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"type":"card"},"return_url":"https://example.com/return","setup_future_usage":"off_session","setup_intent":null,"shipping":{"address":{"city":"Hyde Park","country":"US","line1":"50 Sprague St","line2":"","postal_code":"02136","state":"MA"},"name":"Jenny Rosen","phone":null}}
```

# Create a test Confirmation TokenTest helper
Creates a test mode Confirmation Token server side for your integration tests.

### Parameters
- payment_methodstringID of an existing PaymentMethod.
- payment_method_dataobjectIf provided, this hash will be used to create a PaymentMethod.Show child parameters
- payment_method_optionsobjectPayment-method-specific configuration for this ConfirmationToken.Show child parameters
- return_urlstringReturn URL used to confirm the Intent.
- setup_future_usageenumIndicates that you intend to make future payments with this ConfirmationToken’s payment method.The presence of this property willattach the payment methodto the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.Possible enum valuesoff_sessionUseoff_sessionif your customer_id may or may not be present in your checkout flow.on_sessionUseon_sessionif you intend to only reuse the payment method when your customer_id is present in your checkout flow.
- shippingobjectShipping information for this ConfirmationToken.Show child parameters

#### payment_methodstring

#### payment_method_dataobject

#### payment_method_optionsobject

#### return_urlstring

#### setup_future_usageenum

[TABLE]
off_sessionUseoff_sessionif your customer_id may or may not be present in your checkout flow.
on_sessionUseon_sessionif you intend to only reuse the payment method when your customer_id is present in your checkout flow.
[/TABLE]

```
off_session
```

#### shippingobject

### Returns
Returns a testmode Confirmation Token

```
curlhttps://api.stripe.com/v1/test_helpers/confirmation_tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d payment_instrument=pm_card_visa
```

```
curlhttps://api.stripe.com/v1/test_helpers/confirmation_tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d payment_instrument=pm_card_visa
```

```
{"id":"ctoken_1Ow71CL4FhS6zgoxWjxc7sfr","object":"confirmation_token","created":1710871450,"expires_at":1710914650,"livemode":false,"payment_intent":null,"payment_method_preview":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":"unchecked"},"country":"US","display_brand":"visa","exp_month":3,"exp_year":2025,"fingerprint":"jbGyCKrSRsFpOBWP","funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"type":"card"},"return_url":null,"setup_future_usage":null,"setup_intent":null,"shipping":null,"use_stripe_sdk":true}
```

```
{"id":"ctoken_1Ow71CL4FhS6zgoxWjxc7sfr","object":"confirmation_token","created":1710871450,"expires_at":1710914650,"livemode":false,"payment_intent":null,"payment_method_preview":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":"unchecked"},"country":"US","display_brand":"visa","exp_month":3,"exp_year":2025,"fingerprint":"jbGyCKrSRsFpOBWP","funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"type":"card"},"return_url":null,"setup_future_usage":null,"setup_intent":null,"shipping":null,"use_stripe_sdk":true}
```