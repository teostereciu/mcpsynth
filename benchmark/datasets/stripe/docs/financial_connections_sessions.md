# financial_connections/sessions

*Source: https://docs.stripe.com/api/financial_connections/sessions*

---

# Session
A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.

# The Session object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- account_holdernullableobjectThe account holder for whom accounts are collected in this session.Show child attributes
- accountsobjectThe accounts that were collected as part of this Session.Show child attributes
- client_secretnullablestringA value that will be passed to the client to launch the authentication flow.
- filtersnullableobjectFilters applied to this session that restrict the kinds of accounts to collect.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- permissionsarray of enumsPermissions requested for accounts collected during this session.Possible enum valuesbalancesRequests access for balance data on accounts collected in this session.ownershipRequests access for ownership data on accounts collected in this session.payment_methodRequests permission for the creation of a payment method from an account collected in this session.transactionsRequests access for transaction data on accounts collected in this session.
- prefetchnullablearray of enumsData features requested to be retrieved upon account creation.Possible enum valuesbalancesRequests to prefetch balance data on accounts collected in this session.ownershipRequests to prefetch ownership data on accounts collected in this session.transactionsRequests to prefetch transaction data on accounts collected in this session.
- return_urlnullablestringFor webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

#### idstring

#### objectstring

#### account_holdernullableobject

#### accountsobject

#### client_secretnullablestring

#### filtersnullableobject

#### livemodeboolean

#### permissionsarray of enums

[TABLE]
balancesRequests access for balance data on accounts collected in this session.
ownershipRequests access for ownership data on accounts collected in this session.
payment_methodRequests permission for the creation of a payment method from an account collected in this session.
transactionsRequests access for transaction data on accounts collected in this session.
[/TABLE]

```
payment_method
```

```
transactions
```

#### prefetchnullablearray of enums

[TABLE]
balancesRequests to prefetch balance data on accounts collected in this session.
ownershipRequests to prefetch ownership data on accounts collected in this session.
transactionsRequests to prefetch transaction data on accounts collected in this session.
[/TABLE]

```
transactions
```

#### return_urlnullablestring

```
{"id":"fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq","object":"financial_connections.session","account_holder":{"customer":"cus_NiKSWdaFz2F6I0","type":"customer"},"accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/financial_connections/accounts"},"client_secret":"fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3","filters":{"countries":["US"]},"livemode":false,"permissions":["balances","payment_method"]}
```

```
{"id":"fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq","object":"financial_connections.session","account_holder":{"customer":"cus_NiKSWdaFz2F6I0","type":"customer"},"accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/financial_connections/accounts"},"client_secret":"fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3","filters":{"countries":["US"]},"livemode":false,"permissions":["balances","payment_method"]}
```

# Create a Session
To launch the Financial Connections authorization flow, create aSession. The session’sclient_secretcan be used to launch the flow using Stripe.js.

### Parameters
- account_holderobjectRequiredThe account holder to link accounts for.Show child parameters
- permissionsarray of stringsRequiredList of data features that you would like to request access to.Possible values arebalances,transactions,ownership, andpayment_method.
- filtersobjectFilters to restrict the kinds of accounts to collect.Show child parameters
- prefetcharray of enumsList of data features that you would like to retrieve upon account creation.Possible enum valuesbalancesRequests to prefetch balance data on accounts collected in this session.ownershipRequests to prefetch ownership data on accounts collected in this session.transactionsRequests to prefetch transaction data on accounts collected in this session.
- return_urlstringFor webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.

#### account_holderobjectRequired

#### permissionsarray of stringsRequired

#### filtersobject

#### prefetcharray of enums

[TABLE]
balancesRequests to prefetch balance data on accounts collected in this session.
ownershipRequests to prefetch ownership data on accounts collected in this session.
transactionsRequests to prefetch transaction data on accounts collected in this session.
[/TABLE]

```
transactions
```

#### return_urlstring

### Returns
Returns theSessionobject.

```
curlhttps://api.stripe.com/v1/financial_connections/sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"account_holder[type]"=customer \-d"account_holder[customer]"=cus_NiKSWdaFz2F6I0 \-d"permissions[]"=payment_method \-d"permissions[]"=balances \-d"filters[countries][]"=US
```

```
curlhttps://api.stripe.com/v1/financial_connections/sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"account_holder[type]"=customer \-d"account_holder[customer]"=cus_NiKSWdaFz2F6I0 \-d"permissions[]"=payment_method \-d"permissions[]"=balances \-d"filters[countries][]"=US
```

```
{"id":"fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq","object":"financial_connections.session","account_holder":{"customer":"cus_NiKSWdaFz2F6I0","type":"customer"},"accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/financial_connections/accounts"},"client_secret":"fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3","filters":{"countries":["US"]},"livemode":false,"permissions":["balances","payment_method"]}
```

```
{"id":"fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq","object":"financial_connections.session","account_holder":{"customer":"cus_NiKSWdaFz2F6I0","type":"customer"},"accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/financial_connections/accounts"},"client_secret":"fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3","filters":{"countries":["US"]},"livemode":false,"permissions":["balances","payment_method"]}
```

# Retrieve a Session
Retrieves the details of a Financial ConnectionsSession

### Parameters
Noparameters.

### Returns
Returns aSessionobject if a valid identifier was provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/financial_connections/sessions/fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/financial_connections/sessions/fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq","object":"financial_connections.session","account_holder":{"customer":"cus_NiKSWdaFz2F6I0","type":"customer"},"accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/financial_connections/accounts"},"client_secret":"fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3","filters":{"countries":["US"]},"livemode":false,"permissions":["balances","payment_method"]}
```

```
{"id":"fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq","object":"financial_connections.session","account_holder":{"customer":"cus_NiKSWdaFz2F6I0","type":"customer"},"accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/financial_connections/accounts"},"client_secret":"fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3","filters":{"countries":["US"]},"livemode":false,"permissions":["balances","payment_method"]}
```