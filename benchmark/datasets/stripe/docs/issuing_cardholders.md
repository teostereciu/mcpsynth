# issuing/cardholders

*Source: https://docs.stripe.com/api/issuing/cardholders*

---

# Cardholders
An IssuingCardholderobject represents an individual or business entity who isissuedcards.
Related guide:How to create a cardholder

# The Cardholder object

### Attributes
- idstringUnique identifier for the object.
- billingobjectThe cardholder’s billing information.Show child attributes
- emailnullablestringThe cardholder’s email address.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namestringThe cardholder’s name. This will be printed on cards issued to them.
- phone_numbernullablestringThe cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the3D Secure documentationfor more details.

#### idstring

#### billingobject

#### emailnullablestring

#### metadataobject

#### namestring

#### phone_numbernullablestring

### More attributesExpand all
- objectstring
- companynullableobject
- createdtimestamp
- individualnullableobject
- livemodeboolean
- preferred_localesnullablearray of enums
- requirementsobject
- spending_controlsnullableobject
- statusenum
- typeenum

#### objectstring

#### companynullableobject

#### createdtimestamp

#### individualnullableobject

#### livemodeboolean

#### preferred_localesnullablearray of enums

#### requirementsobject

#### spending_controlsnullableobject

#### statusenum

#### typeenum

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

# Create a cardholder
Creates a new IssuingCardholderobject that can be issued cards.

### Parameters
- billingobjectRequiredThe cardholder’s billing address.Show child parameters
- namestringRequiredThe cardholder’s name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.
- emailstringThe cardholder’s email address.The maximum length is 800 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- phone_numberstringThe cardholder’s phone number. This will be transformed toE.164if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the3D Secure documentationfor more details.

#### billingobjectRequired

#### namestringRequired

#### emailstring

#### metadataobject

#### phone_numberstring

### More parametersExpand all
- companyobject
- individualobject
- preferred_localesarray of enums
- spending_controlsobject
- statusenum
- typeenum

#### companyobject

#### individualobject

#### preferred_localesarray of enums

#### spending_controlsobject

#### statusenum

#### typeenum

### Returns
Returns an IssuingCardholderobject if creation succeeds.

```
curlhttps://api.stripe.com/v1/issuing/cardholders \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=individual \-d name="Jenny Rosen"\--data-urlencode email="jenny.rosen@example.com"\--data-urlencode phone_number="+18888675309"\-d"billing[address][line1]"="1234 Main Street"\-d"billing[address][city]"="San Francisco"\-d"billing[address][state]"=CA \-d"billing[address][country]"=US \-d"billing[address][postal_code]"=94111
```

```
curlhttps://api.stripe.com/v1/issuing/cardholders \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=individual \-d name="Jenny Rosen"\--data-urlencode email="jenny.rosen@example.com"\--data-urlencode phone_number="+18888675309"\-d"billing[address][line1]"="1234 Main Street"\-d"billing[address][city]"="San Francisco"\-d"billing[address][state]"=CA \-d"billing[address][country]"=US \-d"billing[address][postal_code]"=94111
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

# Update a cardholder
Updates the specified IssuingCardholderobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters
- billingobjectThe cardholder’s billing address.Show child parameters
- emailstringThe cardholder’s email address.The maximum length is 800 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- phone_numberstringThe cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the3D Secure documentationfor more details.

#### billingobject

#### emailstring

#### metadataobject

#### phone_numberstring

### More parametersExpand all
- companyobject
- individualobject
- preferred_localesarray of enums
- spending_controlsobject
- statusenum

#### companyobject

#### individualobject

#### preferred_localesarray of enums

#### spending_controlsobject

#### statusenum

### Returns
Returns an updated IssuingCardholderobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{"order_id":"6735"},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{"order_id":"6735"},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

# Retrieve a cardholder
Retrieves an IssuingCardholderobject.

### Parameters
Noparameters.

### Returns
Returns an IssuingCardholderobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```

```
{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"line1":"1234 Main Street","city":"San Francisco","state":"CA","country":"US","postal_code":"94111"}},"company":null,"created":1680415995,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18888675309","redaction":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"}
```