# tax/settings

*Source: https://docs.stripe.com/api/tax/settings*

---

# Tax Settings
You can use TaxSettingsto manage configurations used by Stripe Tax calculations.
Related guide:Using the Settings API

# The Tax Setting object

### Attributes
- objectstringString representing the object’s type. Objects of the same type share the same value.
- defaultsobjectDefault configuration to be used on Stripe Tax calculations.Show child attributes
- head_officenullableobjectThe place where your business is located.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- statusenumThe status of the TaxSettings.Possible enum valuesactiveTaxSettingshave the required information and ready for tax calculations.pendingTaxSettingsmissing some required information and not ready for tax calculations. Checkstatus_detailsfield for more.
- status_detailsobjectInformation about the status.Show child attributes

#### objectstring

#### defaultsobject

#### head_officenullableobject

#### livemodeboolean

#### statusenum

[TABLE]
activeTaxSettingshave the required information and ready for tax calculations.
pendingTaxSettingsmissing some required information and not ready for tax calculations. Checkstatus_detailsfield for more.
[/TABLE]

#### status_detailsobject

```
{"object":"tax.settings","defaults":{"tax_behavior":null,"tax_code":"txcd_10000000"},"head_office":{"address":{"city":null,"country":"US","line1":null,"line2":null,"postal_code":null,"state":"CA"}},"livemode":false,"status":"active","status_details":{"active":{}}}
```

```
{"object":"tax.settings","defaults":{"tax_behavior":null,"tax_code":"txcd_10000000"},"head_office":{"address":{"city":null,"country":"US","line1":null,"line2":null,"postal_code":null,"state":"CA"}},"livemode":false,"status":"active","status_details":{"active":{}}}
```

# Update settings
Updates TaxSettingsparameters used in tax calculations. All parameters are editable but none can be removed once set.

### Parameters
- defaultsobjectDefault configuration to be used on Stripe Tax calculations.Show child parameters
- head_officeobjectThe place where your business is located.Show child parameters

#### defaultsobject

#### head_officeobject

### Returns
A TaxSettingsobject.

```
curlhttps://api.stripe.com/v1/tax/settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"defaults[tax_behavior]"=inclusive \-d"defaults[tax_code]"=txcd_10000000 \-d"head_office[address][country]"=DE
```

```
curlhttps://api.stripe.com/v1/tax/settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"defaults[tax_behavior]"=inclusive \-d"defaults[tax_code]"=txcd_10000000 \-d"head_office[address][country]"=DE
```

```
{"object":"tax.settings","defaults":{"tax_behavior":"inclusive","tax_code":"txcd_10000000"},"head_office":{"address":{"city":null,"country":"DE","line1":null,"line2":null,"postal_code":null,"state":null}},"livemode":false,"status":"active","status_details":{"active":{}}}
```

```
{"object":"tax.settings","defaults":{"tax_behavior":"inclusive","tax_code":"txcd_10000000"},"head_office":{"address":{"city":null,"country":"DE","line1":null,"line2":null,"postal_code":null,"state":null}},"livemode":false,"status":"active","status_details":{"active":{}}}
```

# Retrieve settings
Retrieves TaxSettingsfor a merchant.

### Parameters
Noparameters.

### Returns
A TaxSettingsobject.

```
curlhttps://api.stripe.com/v1/tax/settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/tax/settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"tax.settings","defaults":{"tax_behavior":null,"tax_code":"txcd_10000000"},"head_office":{"address":{"city":null,"country":"US","line1":null,"line2":null,"postal_code":null,"state":"CA"}},"livemode":false,"status":"active","status_details":{"active":{}}}
```

```
{"object":"tax.settings","defaults":{"tax_behavior":null,"tax_code":"txcd_10000000"},"head_office":{"address":{"city":null,"country":"US","line1":null,"line2":null,"postal_code":null,"state":"CA"}},"livemode":false,"status":"active","status_details":{"active":{}}}
```