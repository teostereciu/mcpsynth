# topups

*Source: https://docs.stripe.com/api/topups*

---

# Top-ups
To top up your Stripe balance, you create a top-up object. You can retrieveindividual top-ups, as well as list all top-ups. Top-ups are identified by aunique, random ID.
Related guide:Topping up your platform account

# The Top-up object

### Attributes
- idstringUnique identifier for the object.
- amountintegerAmount transferred.
- currencystringThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- statusenumThe status of the top-up is eithercanceled,failed,pending,reversed, orsucceeded.Possible enum valuescanceledfailedpendingreversedsucceeded

#### idstring

#### amountinteger

#### currencystring

#### descriptionnullablestring

#### metadataobject

#### statusenum

[TABLE]
canceled
failed
pending
reversed
succeeded
[/TABLE]

### More attributesExpand all
- objectstring
- balance_transactionnullablestringExpandable
- createdtimestamp
- expected_availability_datenullableinteger
- failure_codenullablestring
- failure_messagenullablestring
- livemodeboolean
- sourcenullableobjectDeprecated
- statement_descriptornullablestring
- transfer_groupnullablestring

#### objectstring

#### balance_transactionnullablestringExpandable

#### createdtimestamp

#### expected_availability_datenullableinteger

#### failure_codenullablestring

#### failure_messagenullablestring

#### livemodeboolean

#### sourcenullableobjectDeprecated

#### statement_descriptornullablestring

#### transfer_groupnullablestring

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null}
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null}
```

# Create a top-up
Top up the balance of an account

### Parameters
- amountintegerRequiredA positive integer representing how much to transfer.
- currencystringRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### amountintegerRequired

#### currencystringRequired

#### descriptionstring

#### metadataobject

### More parametersExpand all
- sourcestring
- statement_descriptorstring
- transfer_groupstring

#### sourcestring

#### statement_descriptorstring

#### transfer_groupstring

### Returns
Returns the top-up object.

```
curlhttps://api.stripe.com/v1/topups \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=2000 \-d currency=usd \-d description="Top-up for Jenny Rosen"\-d statement_descriptor=Top-up
```

```
curlhttps://api.stripe.com/v1/topups \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=2000 \-d currency=usd \-d description="Top-up for Jenny Rosen"\-d statement_descriptor=Top-up
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null}
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null}
```

# Update a top-up
Updates the metadata of a top-up. Other top-up details are not editable by design.

### Parameters
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### descriptionstring

#### metadataobject

### Returns
The newly updated top-up object if the call succeeded. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null,"metadata":{"order_id":"6735"}}
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null,"metadata":{"order_id":"6735"}}
```

# Retrieve a top-up
Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.

### Parameters
Noparameters.

### Returns
Returns a top-up if a valid identifier was provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null}
```

```
{"id":"tu_1NG6yj2eZvKYlo2C1FOBiHya","object":"topup","amount":2000,"balance_transaction":null,"created":123456789,"currency":"usd","description":"Top-up for Jenny Rosen","expected_availability_date":123456789,"failure_code":null,"failure_message":null,"livemode":false,"source":null,"statement_descriptor":"Top-up","status":"pending","transfer_group":null}
```