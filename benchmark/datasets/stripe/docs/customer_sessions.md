# customer_sessions

*Source: https://docs.stripe.com/api/customer_sessions*

---

# Customer Session
A Customer Session allows you to grant Stripe’s frontend SDKs (like Stripe.js) client-side accesscontrol over a Customer.
Related guides:Customer Session with the Payment Element,Customer Session with the Pricing Table,Customer Session with the Buy Button.

# The Customer Session object

### Attributes
- client_secretstringThe client secret of this Customer Session. Used on the client to set up secure access to the givencustomer.The client secret can be used to provide access tocustomerfrom your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret.
- componentsobjectThis hash defines which component is enabled and the features it supports.Show child attributes
- customerstringExpandableThe Customer the Customer Session was created for.
- expires_attimestampThe timestamp at which this Customer Session will expire.

#### client_secretstring

#### componentsobject

#### customerstringExpandable

#### expires_attimestamp

### More attributesExpand all
- objectstring
- createdtimestamp
- customer_accountnullablestring
- livemodeboolean

#### objectstring

#### createdtimestamp

#### customer_accountnullablestring

#### livemodeboolean

```
{"object":"customer_session","client_secret":"_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje","components":{"buy_button":{"enabled":false},"pricing_table":{"enabled":true}},"customer":"cus_PO34b57IOUb83c","expires_at":1684790027,"livemode":false}
```

```
{"object":"customer_session","client_secret":"_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje","components":{"buy_button":{"enabled":false},"pricing_table":{"enabled":true}},"customer":"cus_PO34b57IOUb83c","expires_at":1684790027,"livemode":false}
```

# Create a Customer Session
Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.

### Parameters
- componentsobjectRequiredConfiguration for each component. At least 1 component must be enabled.Show child parameters
- customerstringThe ID of an existing customer for which to create the Customer Session.

#### componentsobjectRequired

#### customerstring

### More parametersExpand all
- customer_accountstring

#### customer_accountstring

### Returns
Returns a Customer Session object.

```
curlhttps://api.stripe.com/v1/customer_sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_PO34b57IOUb83c \-d"components[pricing_table][enabled]"=true
```

```
curlhttps://api.stripe.com/v1/customer_sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_PO34b57IOUb83c \-d"components[pricing_table][enabled]"=true
```

```
{"object":"customer_session","client_secret":"_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje","components":{"buy_button":{"enabled":false},"pricing_table":{"enabled":true}},"customer":"cus_PO34b57IOUb83c","expires_at":1684790027,"livemode":false}
```

```
{"object":"customer_session","client_secret":"_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje","components":{"buy_button":{"enabled":false},"pricing_table":{"enabled":true}},"customer":"cus_PO34b57IOUb83c","expires_at":1684790027,"livemode":false}
```