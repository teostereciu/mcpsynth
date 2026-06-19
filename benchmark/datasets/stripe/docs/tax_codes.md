# tax_codes

*Source: https://docs.stripe.com/api/tax_codes*

---

# Tax Code
Tax codesclassify goods and services for tax purposes.

# The Tax Code object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- descriptionstringA detailed description of which types of products the tax code represents.
- namestringA short name for the tax code.

#### idstring

#### objectstring

#### descriptionstring

#### namestring

```
{"id":"txcd_99999999","object":"tax_code","description":"Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.","name":"General - Tangible Goods"}
```

```
{"id":"txcd_99999999","object":"tax_code","description":"Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.","name":"General - Tangible Goods"}
```

# Retrieve a tax code
Retrieves the details of an existing tax code. Supply the unique tax code ID and Stripe will return the corresponding tax code information.

### Parameters
Noparameters.

### Returns
Returns a tax code object if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/tax_codes/txcd_99999999 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/tax_codes/txcd_99999999 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"txcd_99999999","object":"tax_code","description":"Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.","name":"General - Tangible Goods"}
```

```
{"id":"txcd_99999999","object":"tax_code","description":"Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.","name":"General - Tangible Goods"}
```

# List all tax codes
A list ofall tax codes availableto add to Products in order to allow specific tax calculations.

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
A dictionary with a data property that contains an array of up to limit tax codes, starting after tax code starting_after. Each entry in the array is a separate tax code object. If no more tax codes are available, the resulting array will be empty. This request should never return an error.

```
curl-G https://api.stripe.com/v1/tax_codes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/tax_codes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/tax_codes","has_more":false,"data":[{"id":"txcd_99999999","object":"tax_code","description":"Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.","name":"General - Tangible Goods"}]}
```

```
{"object":"list","url":"/v1/tax_codes","has_more":false,"data":[{"id":"txcd_99999999","object":"tax_code","description":"Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.","name":"General - Tangible Goods"}]}
```