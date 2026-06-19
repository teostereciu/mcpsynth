# customer_bank_accounts

*Source: https://docs.stripe.com/api/customer_bank_accounts*

---

# Bank Accounts
These bank accounts are payment methods onCustomerobjects.
On the other handExternal Accountsare transferdestinations onAccountobjects for connected accounts.They can be bank accounts or debit cards as well, and are documented in the links above.
Related guide:Bank debits and transfers

# The Bank Account object

### Attributes
- idstringUnique identifier for the object.
- account_holder_namenullablestringThe name of the person or business that owns the bank account.
- account_holder_typenullablestringThe type of entity that holds the account. This can be eitherindividualorcompany.
- bank_namenullablestringName of the bank associated with the routing number (e.g.,WELLS FARGO).
- countrystringTwo-letter ISO code representing the country the bank account is located in.
- currencyenumThree-letterISO code for the currencypaid out to the bank account.
- customernullablestringExpandableThe ID of the customer_id that the bank account is associated with.
- fingerprintnullablestringUniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
- last4stringThe last four digits of the bank account number.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- routing_numbernullablestringThe routing transit number for the bank account.

#### idstring

#### account_holder_namenullablestring

#### account_holder_typenullablestring

#### bank_namenullablestring

#### countrystring

#### currencyenum

#### customernullablestringExpandable

#### fingerprintnullablestring

#### last4string

#### metadatanullableobject

#### routing_numbernullablestring

### More attributesExpand all
- objectstring
- accountnullablestringExpandableAvailable conditionally
- account_typenullablestring
- available_payout_methodsnullablearray of enums
- statusstring

#### objectstring

#### accountnullablestringExpandableAvailable conditionally

#### account_typenullablestring

#### available_payout_methodsnullablearray of enums

#### statusstring

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

# Create a bank account
When you create a new bank account, you must specify aCustomerobject on which to create it.

### Parameters
- sourceobject | stringRequiredEither a token, like the ones returned byStripe.js, or a dictionary containing a user’s bank account details (with the options shown below).Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### sourceobject | stringRequired

#### metadataobject

### Returns
Returns the bank account object.

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d source=btok_1MvoS32eZvKYlo2CDhGTErAe
```

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d source=btok_1MvoS32eZvKYlo2CDhGTErAe
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

# Update a bank account
Updates theaccount_holder_name,account_holder_type, andmetadataof a bank account belonging to a customer_id. Other bank account details are not editable, by design.

### Parameters
- account_holder_namestringThe name of the person or business that owns the bank account.
- account_holder_typestringThe type of entity that holds the account. This can be eitherindividualorcompany.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### account_holder_namestring

#### account_holder_typestring

#### metadataobject

### Returns
Returns the bank account object.

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources/ba_1MvoIJ2eZvKYlo2CO9f0MabO \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources/ba_1MvoIJ2eZvKYlo2CO9f0MabO \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{"order_id":"6735"},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{"order_id":"6735"},"routing_number":"110000000","status":"new"}
```

# Retrieve a bank account
By default, you can see the 10 most recent sources stored on a Customer directly on the object, but you can also retrieve details about a specific bank account stored on the Stripe account.

### Parameters
Noparameters.

### Returns
Returns the bank account object.

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts/ba_1MvoIJ2eZvKYlo2CO9f0MabO \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts/ba_1MvoIJ2eZvKYlo2CO9f0MabO \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1MvoIJ2eZvKYlo2CO9f0MabO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":"cus_9s6XI9OFIdpjIg","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```