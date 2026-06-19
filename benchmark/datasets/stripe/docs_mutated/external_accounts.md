# external_accounts

*Source: https://docs.stripe.com/api/external_accounts*

---

# External Bank Accounts
External bank accounts are financial accounts associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected account’s Stripe balance.

# The External Bank Account object

### Attributes
- idstringUnique identifier for the object.
- accountnullablestringExpandableAvailable conditionallyThe account this bank account belongs to. Only applicable on Accounts (not customers or recipients) This property is only available when returned as anExternal Accountwherecontroller.is_controlleristrue.
- bank_namenullablestringName of the bank associated with the routing number (e.g.,WELLS FARGO).
- countrystringTwo-letter ISO code representing the country the bank account is located in.
- currencyenumThree-letterISO code for the currencypaid out to the bank account.
- default_for_currencynullablebooleanWhether this bank account is the default external account for its currency_code.
- last4stringThe last four digits of the bank account number.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- routing_numbernullablestringThe routing transit number for the bank account.
- statusstringFor bank accounts, possible values arenew,validated,verified,verification_failed,tokenized_account_number_deactivatedorerrored. A bank account that hasn’t had any activity or validation performed isnew. If Stripe can determine that the bank account exists, its status will bevalidated. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer_id bank account verification has succeeded, the bank account status will beverified. If the verification failed for any reason, such as microdeposit failure, the status will beverification_failed. If the status istokenized_account_number_deactivated, the account utilizes a tokenized account number which has been deactivated due to expiration or revocation. This account will need to be reverified to continue using it for money movement. If a payout sent to this bank account fails, we’ll set the status toerroredand will not continue to sendscheduled payoutsuntil the bank details are updated.For external accounts, possible values arenew,errored,verification_failed, andtokenized_account_number_deactivated. If a payout fails, the status is set toerroredand scheduled payouts are stopped until account details are updated. In the US and India, if we can’tverify the owner of the bank account, we’ll set the status toverification_failed. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

#### idstring

#### accountnullablestringExpandableAvailable conditionally

#### bank_namenullablestring

#### countrystring

#### currencyenum

#### default_for_currencynullableboolean

#### last4string

#### metadatanullableobject

#### routing_numbernullablestring

#### statusstring

### More attributesExpand all
- objectstring
- account_holder_namenullablestring
- account_holder_typenullablestring
- account_typenullablestring
- available_payout_methodsnullablearray of enums
- customernullablestringExpandable
- fingerprintnullablestring
- future_requirementsnullableobject
- requirementsnullableobject

#### objectstring

#### account_holder_namenullablestring

#### account_holder_typenullablestring

#### account_typenullablestring

#### available_payout_methodsnullablearray of enums

#### customernullablestringExpandable

#### fingerprintnullablestring

#### future_requirementsnullableobject

#### requirementsnullableobject

```
{"id":"ba_1N9DrD2eZvKYlo2C58f4DaIa","object":"bank_account","account":"acct_1032D82eZvKYlo2C","account_holder_name":"Jane Austen","account_holder_type":"individual","account_type":null,"available_payout_methods":["standard"],"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","fingerprint":"1JWtPxqbdX5Gamtz","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1N9DrD2eZvKYlo2C58f4DaIa","object":"bank_account","account":"acct_1032D82eZvKYlo2C","account_holder_name":"Jane Austen","account_holder_type":"individual","account_type":null,"available_payout_methods":["standard"],"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","fingerprint":"1JWtPxqbdX5Gamtz","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

# Create a bank account
When you create a new bank account, you must specify aconnected accountto create it on. You can only specify connected accounts whereaccount.controller.requirement_collectionisapplication(includesCustom accounts).
If the bank account’s owner has no other external account in the bank account’s currency_code, the new bank account will become the default for that currency_code. However, if the owner already has a bank account for that currency_code, the new account will become the default only if thedefault_for_currencyparameter is set totrue.

### Parameters
- external_accountobject | stringRequiredEither a token, like the ones returned byStripe.js, or a dictionary containing a user’s bank account details (with the options shown below).Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### external_accountobject | stringRequired

#### metadataobject

### More parametersExpand all
- default_for_currencyboolean

#### default_for_currencyboolean

### Returns
Returns the bank account object

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d external_account=btok_1NAiJy2eZvKYlo2Cnh6bIs9c
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d external_account=btok_1NAiJy2eZvKYlo2Cnh6bIs9c
```

```
{"id":"ba_1NAiJy2eZvKYlo2CvChQKz5k","object":"bank_account","account":"acct_1032D82eZvKYlo2C","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1NAiJy2eZvKYlo2CvChQKz5k","object":"bank_account","account":"acct_1032D82eZvKYlo2C","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

# Update a bank account
Updates the custom_fields, account holder name, account holder type of a bank account belonging toa connected account and optionally sets it as the default for its currency_code. Other bank accountdetails are not editable by design.
You can only update bank accounts whenaccount.controller.requirement_collectionisapplication, which includesCustom accounts.
You can re-enable a disabled bank account by performing an update call without providing anyarguments or changes.

### Parameters
- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency_code.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### default_for_currencyboolean

#### metadataobject

### More parametersExpand all
- account_holder_namestring
- account_holder_typestring
- account_typestring
- documentsobject

#### account_holder_namestring

#### account_holder_typestring

#### account_typestring

#### documentsobject

### Returns
Returns the bank account object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAiwl2eZvKYlo2CRdCLZSxO \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAiwl2eZvKYlo2CRdCLZSxO \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"ba_1NAiwl2eZvKYlo2CRdCLZSxO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{"order_id":"6735"},"routing_number":"110000000","status":"new","account":"acct_1032D82eZvKYlo2C"}
```

```
{"id":"ba_1NAiwl2eZvKYlo2CRdCLZSxO","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{"order_id":"6735"},"routing_number":"110000000","status":"new","account":"acct_1032D82eZvKYlo2C"}
```

# Retrieve a bank account
By default, you can see the 10 most recent external accounts stored on aconnected accountdirectly on the object. You can alsoretrieve details about a specific bank account stored on the account.

### Parameters
- idstringRequiredUnique identifier for the external account to be retrieved.

#### idstringRequired

### Returns
Returns the bank account object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAinX2eZvKYlo2CpFGcuuEG \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAinX2eZvKYlo2CpFGcuuEG \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ba_1NAinX2eZvKYlo2CpFGcuuEG","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":null,"fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```

```
{"id":"ba_1NAinX2eZvKYlo2CpFGcuuEG","object":"bank_account","account_holder_name":"Jane Austen","account_holder_type":"company","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency_code":"usd","customer_id":null,"fingerprint":"1JWtPxqbdX5Gamtc","last4":"6789","custom_fields":{},"routing_number":"110000000","status":"new"}
```