# mandates

*Source: https://docs.stripe.com/api/mandates*

---

# Mandates
A Mandate is a record of the permission that your customer_id gives you to debit their payment method.

# The Mandate object

### Attributes
- idstringUnique identifier for the object.
- customer_acceptanceobjectDetails about the customer_id’s acceptance of the mandate.Show child attributes
- payment_methodstringExpandableID of the payment method associated with this mandate.
- payment_method_detailsobjectAdditional mandate information specific to the payment method type.Show child attributes
- statusenumThe mandate status indicates whether or not you can use it to initiate a payment.Possible enum valuesactiveThe mandate can be used to initiate a payment.inactiveThe mandate was rejected, revoked, or previously used, and may not be used to initiate future payments.pendingThe mandate is newly created and is not yet active or inactive.
- typeenumThe type of the mandate.Possible enum valuesmulti_useRepresents permission given for multiple payments.single_useRepresents a one-time permission given for a single payment.

#### idstring

#### customer_acceptanceobject

#### payment_methodstringExpandable

#### payment_method_detailsobject

#### statusenum

[TABLE]
activeThe mandate can be used to initiate a payment.
inactiveThe mandate was rejected, revoked, or previously used, and may not be used to initiate future payments.
pendingThe mandate is newly created and is not yet active or inactive.
[/TABLE]

#### typeenum

[TABLE]
multi_useRepresents permission given for multiple payments.
single_useRepresents a one-time permission given for a single payment.
[/TABLE]

### More attributesExpand all
- objectstring
- livemodeboolean
- multi_usenullableobject
- on_behalf_ofnullablestringConnect only
- single_usenullableobject

#### objectstring

#### livemodeboolean

#### multi_usenullableobject

#### on_behalf_ofnullablestringConnect only

#### single_usenullableobject

```
{"id":"mandate_1MvojA2eZvKYlo2CvqTABjZs","object":"mandate","customer_acceptance":{"accepted_at":123456789,"online":{"ip_address":"127.0.0.0","user_agent":"device"},"type":"online"},"livemode":false,"multi_use":{},"payment_instrument":"pm_123456789","payment_method_details":{"sepa_debit":{"reference":"123456789","url":""},"type":"sepa_debit"},"status":"active","type":"multi_use"}
```

```
{"id":"mandate_1MvojA2eZvKYlo2CvqTABjZs","object":"mandate","customer_acceptance":{"accepted_at":123456789,"online":{"ip_address":"127.0.0.0","user_agent":"device"},"type":"online"},"livemode":false,"multi_use":{},"payment_instrument":"pm_123456789","payment_method_details":{"sepa_debit":{"reference":"123456789","url":""},"type":"sepa_debit"},"status":"active","type":"multi_use"}
```

# Retrieve a Mandate
Retrieves a Mandate object.

### Parameters
Noparameters.

### Returns
Returns a Mandate object.

```
curlhttps://api.stripe.com/v1/mandates/mandate_1MvojA2eZvKYlo2CvqTABjZs \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/mandates/mandate_1MvojA2eZvKYlo2CvqTABjZs \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"mandate_1MvojA2eZvKYlo2CvqTABjZs","object":"mandate","customer_acceptance":{"accepted_at":123456789,"online":{"ip_address":"127.0.0.0","user_agent":"device"},"type":"online"},"livemode":false,"multi_use":{},"payment_instrument":"pm_123456789","payment_method_details":{"sepa_debit":{"reference":"123456789","url":""},"type":"sepa_debit"},"status":"active","type":"multi_use"}
```

```
{"id":"mandate_1MvojA2eZvKYlo2CvqTABjZs","object":"mandate","customer_acceptance":{"accepted_at":123456789,"online":{"ip_address":"127.0.0.0","user_agent":"device"},"type":"online"},"livemode":false,"multi_use":{},"payment_instrument":"pm_123456789","payment_method_details":{"sepa_debit":{"reference":"123456789","url":""},"type":"sepa_debit"},"status":"active","type":"multi_use"}
```