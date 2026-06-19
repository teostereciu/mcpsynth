# tax/registrations

*Source: https://docs.stripe.com/api/tax/registrations*

---

# Tax Registrations
A TaxRegistrationlets us know that your business is registered to collect tax on payments within a region, enabling you toautomatically collect tax.
Stripe doesn’t register on your behalf with the relevant authorities when you create a TaxRegistrationobject. For more information on how to register to collect tax, seeour guide.
Related guide:Using the Registrations API

# The Tax Registration object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- active_fromtimestampTime at which the registration becomes active. Measured in seconds since the Unix epoch.
- countrystringTwo-letter country code (ISO 3166-1 alpha-2).
- country_optionsobjectSpecific options for a registration in the specifiedcountry.Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- expires_atnullabletimestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- statusenumThe status of the registration. This field is present for convenience and can be deduced fromactive_fromandexpires_at.Possible enum valuesactiveThe Tax Registration is currently active.expiredThe Tax Registration is no longer active.scheduledThe Tax Registration will become active in the future.

#### idstring

#### objectstring

#### active_fromtimestamp

#### countrystring

#### country_optionsobject

#### createdtimestamp

#### expires_atnullabletimestamp

#### livemodeboolean

#### statusenum

[TABLE]
activeThe Tax Registration is currently active.
expiredThe Tax Registration is no longer active.
scheduledThe Tax Registration will become active in the future.
[/TABLE]

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1682036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":null,"livemode":false,"status":"active"}
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1682036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":null,"livemode":false,"status":"active"}
```

# Create a registration
Creates a new TaxRegistrationobject.

### Parameters
- active_fromstring | timestampRequiredTime at which the Tax Registration becomes active. It can be eithernowto indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
- countrystringRequiredTwo-letter country code (ISO 3166-1 alpha-2).
- country_optionsobjectRequiredSpecific options for a registration in the specifiedcountry.Show child parameters
- expires_attimestampIf set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.

#### active_fromstring | timestampRequired

#### countrystringRequired

#### country_optionsobjectRequired

#### expires_attimestamp

### Returns
A TaxRegistrationobject.

```
curlhttps://api.stripe.com/v1/tax/registrations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d country=US \-d"country_options[us][state]"=CA \-d"country_options[us][type]"=state_sales_tax \-d active_from=now
```

```
curlhttps://api.stripe.com/v1/tax/registrations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d country=US \-d"country_options[us][state]"=CA \-d"country_options[us][type]"=state_sales_tax \-d active_from=now
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1682036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":null,"livemode":false,"status":"active"}
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1682036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":null,"livemode":false,"status":"active"}
```

# Update a registration
Updates an existing TaxRegistrationobject.
A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by settingexpires_at.

### Parameters
- active_fromstring | timestampTime at which the registration becomes active. It can be eithernowto indicate the current time, or a timestamp measured in seconds since the Unix epoch.
- expires_atstring | timestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be eithernowto indicate the current time, or a timestamp measured in seconds since the Unix epoch.

#### active_fromstring | timestamp

#### expires_atstring | timestamp

### Returns
A TaxRegistrationobject.

```
curlhttps://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d expires_at=now
```

```
curlhttps://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d expires_at=now
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1683036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":1684072000,"livemode":false,"status":"active"}
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1683036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":1684072000,"livemode":false,"status":"active"}
```

# Retrieve a registration
Returns a TaxRegistrationobject.

### Parameters
Noparameters.

### Returns
A TaxRegistrationobject.

```
curlhttps://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1682036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":null,"livemode":false,"status":"active"}
```

```
{"id":"taxreg_NkyGPRPytKq66j","object":"tax.registration","active_from":1682036640,"country":"US","country_options":{"us":{"state":"CA","type":"state_sales_tax"}},"created":1682006400,"expires_at":null,"livemode":false,"status":"active"}
```