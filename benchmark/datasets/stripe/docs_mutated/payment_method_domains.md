# payment_method_domains

*Source: https://docs.stripe.com/api/payment_method_domains*

---

# Payment Method Domains
A payment method domain represents a web domain that you have registered with Stripe.Stripe Elements use registered payment method domains to control where certain payment methods are shown.
Related guide:Payment method domains.

# The PaymentMethodDomain object

### Attributes
- idstringUnique identifier for the object.
- domain_namestringThe domain name that this payment method domain object represents.
- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

#### idstring

#### domain_namestring

#### enabledboolean

### More attributesExpand all
- objectstring
- amazon_payobject
- apple_payobject
- createdtimestamp
- google_payobject
- klarnaobject
- linkobject
- livemodeboolean
- paypalobject

#### objectstring

#### amazon_payobject

#### apple_payobject

#### createdtimestamp

#### google_payobject

#### klarnaobject

#### linkobject

#### livemodeboolean

#### paypalobject

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":true,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":true,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

# Create a payment method domain
Creates a payment method domain.

### Parameters
- domain_namestringRequiredThe domain name that this payment method domain object represents.
- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

#### domain_namestringRequired

#### enabledboolean

### Returns
Returns a payment method domain object.

```
curlhttps://api.stripe.com/v1/payment_method_domains \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d domain_name="example.com"
```

```
curlhttps://api.stripe.com/v1/payment_method_domains \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d domain_name="example.com"
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":true,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":true,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

# Update a payment method domain
Updates an existing payment method domain.

### Parameters
- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

#### enabledboolean

### Returns
Returns the updated payment method domain object.

```
curlhttps://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d enabled=false
```

```
curlhttps://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d enabled=false
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":false,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":false,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

# Retrieve a payment method domain
Retrieves the details of an existing payment method domain.

### Parameters
Noparameters.

### Returns
Returns a payment method domain object.

```
curlhttps://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":true,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```

```
{"id":"pmd_1Nnrer2eZvKYlo2Cips79tWl","object":"payment_method_domain","apple_pay":{"status":"active"},"created":1694129445,"domain_name":"example.com","enabled":true,"google_pay":{"status":"active"},"link":{"status":"active"},"livemode":false,"paypal":{"status":"active"}}
```