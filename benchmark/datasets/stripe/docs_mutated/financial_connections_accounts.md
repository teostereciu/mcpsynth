# financial_connections/accounts

*Source: https://docs.stripe.com/api/financial_connections/accounts*

---

# Accounts
A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

# The Account object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- account_holdernullableobjectThe account holder that this account belongs to.Show child attributes
- account_numbersnullablearray of objectsDetails about the account numbers.Show child attributes
- balancenullableobjectThe most recent information about the account’s balance.Show child attributes
- balance_refreshnullableobjectThe state of the most recent attempt to refresh the account balance.Show child attributes
- categoryenumThe type of the account. Account category is further divided insubcategory.Possible enum valuescashThe account represents real funds held by the institution (e.g. a checking or savings account).creditThe account represents credit extended by the institution (e.g. a credit card or mortgage).investmentThe account represents investments, or any account where there are funds of unknown liquidity.otherThe account does not fall under the other categories.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- display_namenullablestringA human-readable name that has been assigned to this account, either by the account holder or by the institution.
- institution_namestringThe name of the institution that holds this account.
- last4nullablestringThe last 4 digits of the account number. If present, this will be 4 numeric characters.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- ownershipnullablestringExpandableThe most recent information about the account’s owners.
- ownership_refreshnullableobjectThe state of the most recent attempt to refresh the account owners.Show child attributes
- permissionsnullablearray of enumsThe list of permissions granted by this account.Possible enum valuesbalancesAllows accessing balance data from the account.ownershipAllows accessing ownership data from the account.payment_methodAllows the creation of a payment method from the account.transactionsAllows accessing transactions data from the account.
- statusenumThe status of the link to the account.Possible enum valuesactiveStripe is able to retrieve data from the Account without issues.disconnectedAccount connection has been terminated through thedisconnect APIor anend user request.inactiveStripe cannot retrieve data from the Account.
- subcategoryenumIfcategoryiscash, one of:checkingsavingsotherIfcategoryiscredit, one of:mortgageline_of_creditcredit_cardotherIfcategoryisinvestmentorother, this will beother.Possible enum valuescheckingThe account is a checking account.credit_cardThe account represents a credit card.line_of_creditThe account represents a line of credit.mortgageThe account represents a mortgage.otherThe account does not fall under any of the other subcategories.savingsThe account is a savings account.
- subscriptionsnullablearray of enumsThe list of data refresh subscriptions requested on this account.Possible enum valuestransactionsSubscribes to periodic transactions data refreshes from the account.
- supported_payment_method_typesarray of enumsThePaymentMethod type(s) that can be created from this account.Possible enum valueslinkAlinkPaymentMethod can be created.us_bank_accountAus_bank_accountPaymentMethod can be created.
- transaction_refreshnullableobjectThe state of the most recent attempt to refresh the account transactions.Show child attributes

#### idstring

#### objectstring

#### account_holdernullableobject

#### account_numbersnullablearray of objects

#### balancenullableobject

#### balance_refreshnullableobject

#### categoryenum

[TABLE]
cashThe account represents real funds held by the institution (e.g. a checking or savings account).
creditThe account represents credit extended by the institution (e.g. a credit card or mortgage).
investmentThe account represents investments, or any account where there are funds of unknown liquidity.
otherThe account does not fall under the other categories.
[/TABLE]

#### createdtimestamp

#### display_namenullablestring

#### institution_namestring

#### last4nullablestring

#### livemodeboolean

#### ownershipnullablestringExpandable

#### ownership_refreshnullableobject

#### permissionsnullablearray of enums

[TABLE]
balancesAllows accessing balance data from the account.
ownershipAllows accessing ownership data from the account.
payment_methodAllows the creation of a payment method from the account.
transactionsAllows accessing transactions data from the account.
[/TABLE]

```
payment_instrument
```

```
transactions
```

#### statusenum

[TABLE]
activeStripe is able to retrieve data from the Account without issues.
disconnectedAccount connection has been terminated through thedisconnect APIor anend user request.
inactiveStripe cannot retrieve data from the Account.
[/TABLE]

```
disconnected
```

#### subcategoryenum
- checking
- savings
- other
- mortgage
- line_of_credit
- credit_card
- other

[TABLE]
checkingThe account is a checking account.
credit_cardThe account represents a credit card.
line_of_creditThe account represents a line of credit.
mortgageThe account represents a mortgage.
otherThe account does not fall under any of the other subcategories.
savingsThe account is a savings account.
[/TABLE]

```
credit_card
```

```
line_of_credit
```

#### subscriptionsnullablearray of enums

[TABLE]
transactionsSubscribes to periodic transactions data refreshes from the account.
[/TABLE]

```
transactions
```

#### supported_payment_method_typesarray of enums

[TABLE]
linkAlinkPaymentMethod can be created.
us_bank_accountAus_bank_accountPaymentMethod can be created.
[/TABLE]

```
us_bank_account
```

#### transaction_refreshnullableobject

```
{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"active","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}
```

```
{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"active","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}
```

# Retrieve an Account
Retrieves the details of an Financial ConnectionsAccount.

### Parameters
Noparameters.

### Returns
Returns anAccountobject if a valid identifier was provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"active","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}
```

```
{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"active","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}
```

# List Accounts
Returns a list of Financial ConnectionsAccountobjects.

### Parameters
- account_holderobjectIf present, only return accounts that belong to the specified account holder.account_holder[customer_id]andaccount_holder[account]are mutually exclusive.Show child parameters
- sessionstringIf present, only return accounts that were collected as part of the given session.

#### account_holderobject

#### sessionstring

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitAccountobjects, starting after accountstarting_after. Each entry in the array is a separateAccountobject. If no more accounts are available, the resulting array will be empty. This request willraisean error if more than one ofaccount_holder[account],account_holder[customer_id], orsessionis specified.

```
curl-G https://api.stripe.com/v1/financial_connections/accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/financial_connections/accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/financial_connections/accounts","has_more":false,"data":[{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"active","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}]}
```

```
{"object":"list","url":"/v1/financial_connections/accounts","has_more":false,"data":[{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"active","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}]}
```

# Disconnect an Account
Disables your access to a Financial ConnectionsAccount. You will no longer be able to access data associated with the account (e.g. balances, transactions).

### Parameters
Noparameters.

### Returns
Returns anAccountobject if a valid identifier was provided, andraisesan errorotherwise.

```
curl-X POST https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/disconnect \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X POST https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/disconnect \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"disconnected","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}
```

```
{"id":"fca_1MwVK82eZvKYlo2Cjw8FMxXf","object":"financial_connections.account","account_holder":{"customer_id":"cus_9s6XI9OFIdpjIg","type":"customer_id"},"balance":null,"balance_refresh":null,"category":"cash","created":1681412208,"display_name":"Sample Checking Account","institution_name":"StripeBank","last4":"6789","livemode":false,"ownership":null,"ownership_refresh":null,"permissions":[],"status":"disconnected","subcategory":"checking","subscriptions":[],"supported_payment_method_types":["us_bank_account"],"transaction_refresh":null}
```