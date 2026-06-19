# setup_intents

*Source: https://docs.stripe.com/api/setup_intents*

---

# Setup Intents
A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments.For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment.Later, you can usePaymentIntentsto drive the payment flow.
Create a SetupIntent when you’re ready to collect your customer’s payment credentials.Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid.The SetupIntent transitions through multiplestatusesas it guidesyou through the setup process.
Successful SetupIntents result in payment credentials that are optimized for future payments.For example, cardholders incertain regionsmight need to be run throughStrong Customer Authenticationduring payment method collectionto streamline lateroff-session payments.If you use the SetupIntent with aCustomer,it automatically attaches the resulting payment method to that Customer after successful setup.We recommend using SetupIntents orsetup_future_usageonPaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.
By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.
Related guide:Setup Intents API

# The SetupIntent object

### Attributes
- idstringretrievable with publishable keyUnique identifier for the object.
- automatic_payment_methodsnullableobjectSettings for dynamic payment methods compatible with this Setup IntentShow child attributes
- client_secretnullablestringretrievable with publishable keyThe client secret of this SetupIntent. Used for client-side retrieval using a publishable key.The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.
- customernullablestringExpandableID of the Customer this SetupIntent belongs to, if one exists.If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
- customer_accountnullablestringID of the Account this SetupIntent belongs to, if one exists.If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.
- descriptionnullablestringretrievable with publishable keyAn arbitrary string attached to the object. Often useful for displaying to users.
- last_setup_errornullableobjectretrievable with publishable keyThe error encountered in the previous SetupIntent confirmation.Show child attributes
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- next_actionnullableobjectretrievable with publishable keyIf present, this property tells you what actions you need to take in order for your customer to continue payment setup.Show child attributes
- payment_methodnullablestringExpandableretrievable with publishable keyID of the payment method used with this SetupIntent. If the payment method iscard_presentand isn’t a digital wallet, then thegenerated_cardassociated with thelatest_attemptis attached to the Customer instead.
- statusenumretrievable with publishable keyStatusof this SetupIntent, one ofrequires_payment_method,requires_confirmation,requires_action,processing,canceled, orsucceeded.Possible enum valuescanceledprocessingrequires_actionrequires_confirmationrequires_payment_methodsucceeded
- usagestringretrievable with publishable keyIndicates how the payment method is intended to be used in the future.Useon_sessionif you intend to only reuse the payment method when the customer is in your checkout flow. Useoff_sessionif your customer may or may not be in your checkout flow. If not provided, this value defaults tooff_session.

#### idstringretrievable with publishable key

#### automatic_payment_methodsnullableobject

#### client_secretnullablestringretrievable with publishable key

#### customernullablestringExpandable

#### customer_accountnullablestring

#### descriptionnullablestringretrievable with publishable key

#### last_setup_errornullableobjectretrievable with publishable key

#### metadatanullableobject

#### next_actionnullableobjectretrievable with publishable key

#### payment_methodnullablestringExpandableretrievable with publishable key

#### statusenumretrievable with publishable key

[TABLE]
canceled
processing
requires_action
requires_confirmation
requires_payment_method
succeeded
[/TABLE]

```
requires_action
```

```
requires_confirmation
```

```
requires_payment_method
```

#### usagestringretrievable with publishable key

### More attributesExpand all
- objectstringretrievable with publishable key
- applicationnullablestringExpandableConnect only
- attach_to_selfnullableboolean
- cancellation_reasonnullableenumretrievable with publishable key
- createdtimestampretrievable with publishable key
- excluded_payment_method_typesnullablearray of enums
- flow_directionsnullablearray of enums
- latest_attemptnullablestringExpandable
- livemodebooleanretrievable with publishable key
- mandatenullablestringExpandable
- on_behalf_ofnullablestringExpandableConnect only
- payment_method_configuration_detailsnullableobject
- payment_method_optionsnullableobject
- payment_method_typesarray of stringsretrievable with publishable key
- single_use_mandatenullablestringExpandable

#### objectstringretrievable with publishable key

#### applicationnullablestringExpandableConnect only

#### attach_to_selfnullableboolean

#### cancellation_reasonnullableenumretrievable with publishable key

#### createdtimestampretrievable with publishable key

#### excluded_payment_method_typesnullablearray of enums

#### flow_directionsnullablearray of enums

#### latest_attemptnullablestringExpandable

#### livemodebooleanretrievable with publishable key

#### mandatenullablestringExpandable

#### on_behalf_ofnullablestringExpandableConnect only

#### payment_method_configuration_detailsnullableobject

#### payment_method_optionsnullableobject

#### payment_method_typesarray of stringsretrievable with publishable key

#### single_use_mandatenullablestringExpandable

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

# Create a SetupIntent
Creates a SetupIntent object.
After you create the SetupIntent, attach a payment method andconfirmit to collect any required permissions to charge the payment method later.

### Parameters
- automatic_payment_methodsobjectWhen you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.Show child parameters
- confirmbooleanSet totrueto attempt to confirm this SetupIntent immediately. This parameter defaults tofalse. If a card is the attached payment method, you can provide areturn_urlin case further authentication is necessary.
- customerstringID of the Customer this SetupIntent belongs to, if one exists.If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
- customer_accountstringID of the Account this SetupIntent belongs to, if one exists.If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- payment_methodstringID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
- usageenumIndicates how the payment method is intended to be used in the future. If not provided, this value defaults tooff_session.Possible enum valuesoff_sessionUseoff_sessionif your customer may or may not be in your checkout flow.on_sessionUseon_sessionif you intend to only reuse the payment method when the customer is in your checkout flow.

#### automatic_payment_methodsobject

#### confirmboolean

#### customerstring

#### customer_accountstring

#### descriptionstring

#### metadataobject

#### payment_methodstring

#### usageenum

[TABLE]
off_sessionUseoff_sessionif your customer may or may not be in your checkout flow.
on_sessionUseon_sessionif you intend to only reuse the payment method when the customer is in your checkout flow.
[/TABLE]

```
off_session
```

### More parametersExpand all
- attach_to_selfboolean
- confirmation_tokenstringonly when confirm=true
- excluded_payment_method_typesarray of enums
- flow_directionsarray of enums
- mandate_dataobjectonly when confirm=true
- on_behalf_ofstringConnect only
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings
- return_urlstringonly when confirm=true
- single_useobject
- use_stripe_sdkboolean

#### attach_to_selfboolean

#### confirmation_tokenstringonly when confirm=true

#### excluded_payment_method_typesarray of enums

#### flow_directionsarray of enums

#### mandate_dataobjectonly when confirm=true

#### on_behalf_ofstringConnect only

#### payment_method_configurationstring

#### payment_method_dataobject

#### payment_method_optionsobject

#### payment_method_typesarray of strings

#### return_urlstringonly when confirm=true

#### single_useobject

#### use_stripe_sdkboolean

### Returns
Returns a SetupIntent object.

```
curlhttps://api.stripe.com/v1/setup_intents \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"payment_method_types[]"=card
```

```
curlhttps://api.stripe.com/v1/setup_intents \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"payment_method_types[]"=card
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

# Update a SetupIntent
Updates a SetupIntent object.

### Parameters
- customerstringID of the Customer this SetupIntent belongs to, if one exists.If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
- customer_accountstringID of the Account this SetupIntent belongs to, if one exists.If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- payment_methodstringID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. To unset this field to null, pass in an empty string.

#### customerstring

#### customer_accountstring

#### descriptionstring

#### metadataobject

#### payment_methodstring

### More parametersExpand all
- attach_to_selfboolean
- excluded_payment_method_typesarray of enums
- flow_directionsarray of enums
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings

#### attach_to_selfboolean

#### excluded_payment_method_typesarray of enums

#### flow_directionsarray of enums

#### payment_method_configurationstring

#### payment_method_dataobject

#### payment_method_optionsobject

#### payment_method_typesarray of strings

### Returns
Returns a SetupIntent object.

```
curlhttps://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{"order_id":"6735"},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{"order_id":"6735"},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

# Retrieve a SetupIntent
Retrieves the details of a SetupIntent that has previously been created.
Client-side retrieval using a publishable key is allowed when theclient_secretis provided in the query string.
When retrieved with a publishable key, only a subset of properties will be returned. Please refer to theSetupIntentobject reference for more details.

### Parameters
- client_secretstringRequired if using publishable keyThe client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.

#### client_secretstringRequired if using publishable key

### Returns
Returns a SetupIntent if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```

```
{"id":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG","object":"setup_intent","application":null,"cancellation_reason":null,"client_secret":"seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe","created":1678942624,"customer":null,"description":null,"flow_directions":null,"last_setup_error":null,"latest_attempt":null,"livemode":false,"mandate":null,"metadata":{},"next_action":null,"on_behalf_of":null,"payment_method":null,"payment_method_options":{"card":{"mandate_options":null,"network":null,"request_three_d_secure":"automatic"}},"payment_method_types":["card"],"single_use_mandate":null,"status":"requires_payment_method","usage":"off_session"}
```