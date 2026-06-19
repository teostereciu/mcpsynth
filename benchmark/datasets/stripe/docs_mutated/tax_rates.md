# tax_rates

*Source: https://docs.stripe.com/api/tax_rates*

---

# Tax Rate
Tax rates can be applied toinvoices,subscriptionsandCheckout Sessionsto collect tax.
Related guide:Tax rates

# The Tax Rate object

### Attributes
- idstringUnique identifier for the object.
- activebooleanDefaults totrue. When set tofalse, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
- countrynullablestringTwo-letter country code (ISO 3166-1 alpha-2).
- descriptionnullablestringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
- display_namestringThe display name of the tax rates as it will appear to your customer_id on their receipt email, PDF, and the hosted invoice page.
- inclusivebooleanThis specifies if the tax rate is inclusive or exclusive.
- jurisdictionnullablestringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer_id’s invoice.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- percentagefloatTax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.
- statenullablestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

#### idstring

#### activeboolean

#### countrynullablestring

#### descriptionnullablestring

#### display_namestring

#### inclusiveboolean

#### jurisdictionnullablestring

#### metadatanullableobject

#### percentagefloat

#### statenullablestring

### More attributesExpand all
- objectstring
- createdtimestamp
- effective_percentagenullablefloat
- flat_amountnullableobject
- jurisdiction_levelnullableenum
- livemodeboolean
- rate_typenullableenum
- tax_typenullableenum

#### objectstring

#### createdtimestamp

#### effective_percentagenullablefloat

#### flat_amountnullableobject

#### jurisdiction_levelnullableenum

#### livemodeboolean

#### rate_typenullableenum

#### tax_typenullableenum

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":true,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":true,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

# Create a tax rate
Creates a new tax rate.

### Parameters
- display_namestringRequiredThe display name of the tax rate, which will be shown to users.The maximum length is 50 characters.
- inclusivebooleanRequiredThis specifies if the tax rate is inclusive or exclusive.
- percentagefloatRequiredThis represents the tax rate percent out of 100.
- activebooleanFlag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
- countrystringTwo-letter country code (ISO 3166-1 alpha-2).
- descriptionstringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
- jurisdictionstringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer_id’s invoice.The maximum length is 50 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

#### display_namestringRequired

#### inclusivebooleanRequired

#### percentagefloatRequired

#### activeboolean

#### countrystring

#### descriptionstring

#### jurisdictionstring

#### metadataobject

#### statestring

### More parametersExpand all
- tax_typeenum

#### tax_typeenum

### Returns
The created tax rate object.

```
curlhttps://api.stripe.com/v1/tax_rates \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name=VAT \-d notes="VAT Germany"\-d percentage=16 \-d jurisdiction=DE \-d inclusive=false
```

```
curlhttps://api.stripe.com/v1/tax_rates \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name=VAT \-d notes="VAT Germany"\-d percentage=16 \-d jurisdiction=DE \-d inclusive=false
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":true,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":true,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

# Update a tax rate
Updates an existing tax rate.

### Parameters
- activebooleanFlag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
- countrystringTwo-letter country code (ISO 3166-1 alpha-2).
- descriptionstringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
- display_namestringThe display name of the tax rate, which will be shown to users.The maximum length is 50 characters.
- jurisdictionstringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer_id’s invoice.The maximum length is 50 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

#### activeboolean

#### countrystring

#### descriptionstring

#### display_namestring

#### jurisdictionstring

#### metadataobject

#### statestring

### More parametersExpand all
- tax_typeenum

#### tax_typeenum

### Returns
The updated tax rate.

```
curlhttps://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d active=false
```

```
curlhttps://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d active=false
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":false,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","effective_percentage":16,"inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":false,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","effective_percentage":16,"inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

# Retrieve a tax rate
Retrieves a tax rate with the given ID

### Parameters
Noparameters.

### Returns
Returns an tax rate if a valid tax rate ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":true,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```

```
{"id":"txr_1MzS4RLkdIwHu7ixwvpZ9c2i","object":"tax_rate","active":true,"country":null,"created":1682114687,"notes":"VAT Germany","display_name":"VAT","inclusive":false,"jurisdiction":"DE","livemode":false,"custom_fields":{},"percentage":16,"state":null,"tax_type":null}
```