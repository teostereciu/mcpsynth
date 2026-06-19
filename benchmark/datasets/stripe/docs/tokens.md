# tokens

*Source: https://docs.stripe.com/api/tokens*

---

# Tokens
Tokenization is the process Stripe uses to collect sensitive card or bankaccount details, or personally identifiable information (PII), directly fromyour customers in a secure manner. A token representing this information isreturned to your server to use. Use ourrecommended payments integrationsto perform this processon the client-side. This guarantees that no sensitive card data touches your server,and allows your integration to operate in a PCI-compliant way.
If you can’t use client-side tokenization, you can also create tokens usingthe API with either your publishable or secret API key. Ifyour integration uses this method, you’re responsible for any PCI compliancethat it might require, and you must keep your secret API key safe. Unlike withclient-side tokenization, your customer’s information isn’t sent directly toStripe, so we can’t determine how it’s handled or stored.
You can’t store or use tokens more than once. To store card or bank accountinformation for later use, createCustomerobjects orExternal accounts.Radar, our integrated solution for automatic fraud protection,performs best with integrations that use client-side tokenization.

# The Token object

### Attributes
- idstringUnique identifier for the object.
- cardnullableobjectHash describing the card used to make the charge.Show child attributes

#### idstring

#### cardnullableobject

### More attributesExpand all
- objectstring
- bank_accountnullableobject
- client_ipnullablestring
- createdtimestamp
- descriptionnullablestring
- livemodeboolean
- typestring
- usedboolean

#### objectstring

#### bank_accountnullableobject

#### client_ipnullablestring

#### createdtimestamp

#### descriptionnullablestring

#### livemodeboolean

#### typestring

#### usedboolean

```
{"id":"tok_1N3T00LkdIwHu7ixt44h1F8k","object":"token","card":{"id":"card_1N3T00LkdIwHu7ixRdxpVI1Q","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"unchecked","dynamic_last4":null,"exp_month":5,"exp_year":2026,"fingerprint":"mToisGZ01V71BCos","funding":"credit","last4":"4242","metadata":{},"name":null,"tokenization_method":null,"wallet":null},"client_ip":"52.35.78.6","created":1683071568,"livemode":false,"type":"card","used":false}
```

```
{"id":"tok_1N3T00LkdIwHu7ixt44h1F8k","object":"token","card":{"id":"card_1N3T00LkdIwHu7ixRdxpVI1Q","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"unchecked","dynamic_last4":null,"exp_month":5,"exp_year":2026,"fingerprint":"mToisGZ01V71BCos","funding":"credit","last4":"4242","metadata":{},"name":null,"tokenization_method":null,"wallet":null},"client_ip":"52.35.78.6","created":1683071568,"livemode":false,"type":"card","used":false}
```

# Create a bank account token
Creates a single-use token that represents a bank account’s details.You can use this token with any v1 API method in place of a bank accountdictionary. You can only use this token once. To do so, attach it to aconnected accountwherecontroller.requirement_collectionisapplication, which includes Custom accounts.

### Parameters
- bank_accountobjectThe bank account this token will represent.Show child parameters

#### bank_accountobject

### More parametersExpand all
- customerstringConnect only

#### customerstringConnect only

### Returns
Returns the created bank account token if it’s successful. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"bank_account[country]"=US \-d"bank_account[currency]"=usd \-d"bank_account[account_holder_name]"="Jenny Rosen"\-d"bank_account[account_holder_type]"=individual \-d"bank_account[routing_number]"=110000000 \-d"bank_account[account_number]"=000123456789
```

```
curlhttps://api.stripe.com/v1/tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"bank_account[country]"=US \-d"bank_account[currency]"=usd \-d"bank_account[account_holder_name]"="Jenny Rosen"\-d"bank_account[account_holder_type]"=individual \-d"bank_account[routing_number]"=110000000 \-d"bank_account[account_number]"=000123456789
```

```
{"id":"btok_1N3T00LkdIwHu7ixt44h1F8k","object":"token","bank_account":{"id":"ba_1NWScr2eZvKYlo2C8MgV5Cwn","object":"bank_account","account_holder_name":"Jenny Rosen","account_holder_type":"individual","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency":"usd","fingerprint":"1JWtPxqbdX5Gamtz","last4":"6789","routing_number":"110000000","status":"new"},"client_ip":null,"created":1689981645,"livemode":false,"redaction":null,"type":"bank_account","used":false}
```

```
{"id":"btok_1N3T00LkdIwHu7ixt44h1F8k","object":"token","bank_account":{"id":"ba_1NWScr2eZvKYlo2C8MgV5Cwn","object":"bank_account","account_holder_name":"Jenny Rosen","account_holder_type":"individual","account_type":null,"bank_name":"STRIPE TEST BANK","country":"US","currency":"usd","fingerprint":"1JWtPxqbdX5Gamtz","last4":"6789","routing_number":"110000000","status":"new"},"client_ip":null,"created":1689981645,"livemode":false,"redaction":null,"type":"bank_account","used":false}
```

# Create a card token
Creates a single-use token that represents a credit card’s details.You can use this token in place of a credit carddictionarywith any v1 API method.You can only use these tokens oncebycreating a new Charge objector by attaching them to aCustomer object.
To use this functionality, you need toenable accessto the raw card data APIs.In most cases, you can use our recommendedpayments integrationsinstead of using the API.

### Parameters
- cardobject | stringThe card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this isa dictionarycontaining a user’s credit card details, with the options described below.Show child parameters

#### cardobject | string

### Returns
Returns the created card token if it’s successful. Otherwise, this call raisesan error.

```
curlhttps://api.stripe.com/v1/tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"card[number]"=4242424242424242 \-d"card[exp_month]"=5 \-d"card[exp_year]"=2026 \-d"card[cvc]"=314
```

```
curlhttps://api.stripe.com/v1/tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"card[number]"=4242424242424242 \-d"card[exp_month]"=5 \-d"card[exp_year]"=2026 \-d"card[cvc]"=314
```

```
{"id":"tok_1N3T00LkdIwHu7ixt44h1F8k","object":"token","card":{"id":"card_1N3T00LkdIwHu7ixRdxpVI1Q","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"unchecked","dynamic_last4":null,"exp_month":5,"exp_year":2026,"fingerprint":"mToisGZ01V71BCos","funding":"credit","last4":"4242","metadata":{},"name":null,"tokenization_method":null,"wallet":null},"client_ip":"52.35.78.6","created":1683071568,"livemode":false,"type":"card","used":false}
```

```
{"id":"tok_1N3T00LkdIwHu7ixt44h1F8k","object":"token","card":{"id":"card_1N3T00LkdIwHu7ixRdxpVI1Q","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"unchecked","dynamic_last4":null,"exp_month":5,"exp_year":2026,"fingerprint":"mToisGZ01V71BCos","funding":"credit","last4":"4242","metadata":{},"name":null,"tokenization_method":null,"wallet":null},"client_ip":"52.35.78.6","created":1683071568,"livemode":false,"type":"card","used":false}
```

# Create a CVC update token
Creates a single-use token that represents an updated CVC value that you can use forCVC re-collection.Use this token whenyou confirm a card paymentor use a saved card on aPaymentIntentwithconfirmation_method: manual.
For most cases, use ourJavaScript libraryinstead of using the API. For aPaymentIntentwithconfirmation_method: automatic, use our recommendedpayments integrationwithout tokenizing the CVC value.

### Parameters
- cvc_updateobjectRequiredThe updated CVC value this token represents.Show child parameters

#### cvc_updateobjectRequired

### Returns
Returns the created CVC update token if it’s successful. Otherwise, this call raisesan error.

```
curlhttps://api.stripe.com/v1/tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"cvc_update[cvc]"=123
```

```
curlhttps://api.stripe.com/v1/tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"cvc_update[cvc]"=123
```

```
{"id":"cvctok_1NkWsu2eZvKYlo2CFDm6ab7X","object":"token","client_ip":null,"created":1693334608,"livemode":false,"redaction":null,"type":"cvc_update","used":false}
```

```
{"id":"cvctok_1NkWsu2eZvKYlo2CFDm6ab7X","object":"token","client_ip":null,"created":1693334608,"livemode":false,"redaction":null,"type":"cvc_update","used":false}
```