# terminal/connection_tokens

*Source: https://docs.stripe.com/api/terminal/connection_tokens*

---

# Connection Token
A Connection Token is used by the Stripe Terminal SDK to connect to a reader.
Related guide:Fleet management

# The Connection Token object

### Attributes
- locationnullablestringThe id of the location that this connection token is scoped to. Note that location scoping only applies to internet-connected readers. For more details, seethe docs on scoping connection tokens.
- secretstringYour application should pass this token to the Stripe Terminal SDK.

#### locationnullablestring

#### secretstring

### More attributesExpand all
- objectstring

#### objectstring

```
{"object":"terminal.connection_token","secret":"pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"}
```

```
{"object":"terminal.connection_token","secret":"pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"}
```

# Create a Connection Token
To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.

### Parameters
- locationstringThe id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, seethe docs on scoping connection tokens.

#### locationstring

### Returns
Returns a Connection Token.

```
curl-X POST https://api.stripe.com/v1/terminal/connection_tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X POST https://api.stripe.com/v1/terminal/connection_tokens \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"terminal.connection_token","secret":"pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"}
```

```
{"object":"terminal.connection_token","secret":"pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"}
```