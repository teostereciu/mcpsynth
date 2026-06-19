# sources

*Source: https://docs.stripe.com/api/sources*

---

# SourcesDeprecated
Sourceobjects allow you to accept a variety of payment methods. Theyrepresent a customer’s payment instrument, and can be used with the Stripe APIjust like aCardobject: once chargeable, they can be charged, or can beattached to customers.
Stripe doesn’t recommend using the deprecatedSources API.We recommend that you adopt thePaymentMethods API.This newer API provides access to our latest features and payment method types.
Related guides:Sources APIandSources & Customers.

# The Source objectDeprecated

### Attributes
- idstringUnique identifier for the object.
- amountnullableintegerA positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required forsingle_usesources.
- currencynullableenumThree-letterISO code for the currencyassociated with the source. This is the currency for which the source will be chargeable once ready. Required forsingle_usesources.
- customernullablestringThe ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- ownernullableobjectInformation about the owner of the payment instrument that may be used or required by particular source types.Show child attributes
- redirectnullableobjectInformation related to the redirect flow. Present if the source is authenticated by a redirect (flowisredirect).Show child attributes
- statement_descriptornullablestringExtra information about a source. This will appear on your customer’s statement every time you charge the source.
- statusstringThe status of the source, one ofcanceled,chargeable,consumed,failed, orpending. Onlychargeablesources can be used to create a charge.
- typeenumThetypeof the source. Thetypeis a payment method, one ofach_credit_transfer,ach_debit,alipay,bancontact,card,card_present,eps,giropay,ideal,multibanco,klarna,p24,sepa_debit,sofort,three_d_secure, orwechat. An additional hash is included on the source with a name matching this value. It contains additional information specific to thepayment methodused.Possible enum valuesach_credit_transferach_debitalipaybancontactcardcard_presentepsgiropayidealklarnaShow 6 more

#### idstring

#### amountnullableinteger

#### currencynullableenum

#### customernullablestring

#### metadatanullableobject

#### ownernullableobject

#### redirectnullableobject

#### statement_descriptornullablestring

#### statusstring

#### typeenum

[TABLE]
ach_credit_transfer
ach_debit
alipay
bancontact
card
card_present
eps
giropay
ideal
klarna
Show 6 more
[/TABLE]

```
ach_credit_transfer
```

```
card_present
```

### More attributesExpand all
- objectstring
- allow_redisplaynullableenum
- client_secretstring
- code_verificationnullableobject
- createdtimestamp
- flowstring
- livemodeboolean
- receivernullableobject
- source_ordernullableobject
- usagenullablestring

#### objectstring

#### allow_redisplaynullableenum

#### client_secretstring

#### code_verificationnullableobject

#### createdtimestamp

#### flowstring

#### livemodeboolean

#### receivernullableobject

#### source_ordernullableobject

#### usagenullablestring

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

# Create a source
Creates a new source object.

### Parameters
- typestringRequiredThetypeof the source to create. Required unlesscustomerandoriginal_sourceare specified (see theCloning card Sourcesguide)
- amountintegerAmount associated with the source. This is the amount for which the source will be chargeable once ready. Required forsingle_usesources. Not supported forreceivertype sources, where charge amount may not be specified until funds land.
- currencyenumThree-letterISO code for the currencyassociated with the source. This is the currency for which the source will be chargeable once ready.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- ownerobjectInformation about the owner of the payment instrument that may be used or required by particular source types.Show child parameters
- redirectobjectParameters required for the redirect flow. Required if the source is authenticated by a redirect (flowisredirect).Show child parameters
- statement_descriptorstringAn arbitrary string to be displayed on your customer’s statement. As an example, if your website isRunCluband the item you’re charging for is a race ticket, you may want to specify astatement_descriptorofRunClub 5K race ticket.While many payment types will display this information, some may not display it at all.

#### typestringRequired

#### amountinteger

#### currencyenum

#### metadataobject

#### ownerobject

#### redirectobject

#### statement_descriptorstring

### More parametersExpand all
- flowstring
- mandateobject
- receiverobject
- source_orderobject
- tokenstring
- usagestring

#### flowstring

#### mandateobject

#### receiverobject

#### source_orderobject

#### tokenstring

#### usagestring

### Returns
Returns a newly created source.

```
curlhttps://api.stripe.com/v1/sources \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=ach_credit_transfer \-d currency=usd \--data-urlencode"owner[email]"="jenny.rosen@example.com"
```

```
curlhttps://api.stripe.com/v1/sources \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=ach_credit_transfer \-d currency=usd \--data-urlencode"owner[email]"="jenny.rosen@example.com"
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

# Update a source
Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request accepts themetadataandowneras arguments. It is also possible to update type specific information for selected payment methods. Please refer to ourpayment method guidesfor more detail.

### Parameters
- amountintegerAmount associated with the source.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- ownerobjectInformation about the owner of the payment instrument that may be used or required by particular source types.Show child parameters

#### amountinteger

#### metadataobject

#### ownerobject

### More parametersExpand all
- mandateobject
- source_orderobject

#### mandateobject

#### source_orderobject

### Returns
Returns the source object if the update succeeded. This call willraisean errorif update parameters are invalid.

```
curlhttps://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{"order_id":"6735"},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{"order_id":"6735"},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

# Retrieve a source
Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

### Parameters
Noparameters.

### More parametersExpand all
- client_secretstring

#### client_secretstring

### Returns
Returns a source if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```

```
{"id":"src_1N3lxdLkdIwHu7ixPHXy8UcI","object":"source","ach_credit_transfer":{"account_number":"test_eb829353ed79","bank_name":"TEST BANK","fingerprint":"kBQsBk9KtfCgjEYK","refund_account_holder_name":null,"refund_account_holder_type":null,"refund_routing_number":null,"routing_number":"110000000","swift_code":"TSTEZ122"},"amount":null,"client_secret":"src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr","created":1683144457,"currency":"usd","flow":"receiver","livemode":false,"metadata":{},"owner":{"address":null,"email":"jenny.rosen@example.com","name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"receiver":{"address":"110000000-test_eb829353ed79","amount_charged":0,"amount_received":0,"amount_returned":0,"refund_attributes_method":"email","refund_attributes_status":"missing"},"statement_descriptor":null,"status":"pending","type":"ach_credit_transfer","usage":"reusable"}
```