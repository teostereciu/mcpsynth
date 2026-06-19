# promotion_codes

*Source: https://docs.stripe.com/api/promotion_codes*

---

# Promotion Code
A Promotion Code represents a customer_id-redeemable code for an underlying promotion.You can create multiple codes for a single promotion.
If you enable promotion codes in yourcustomer portal configuration, then customers can redeem a code themselves when updating a subscription in the portal.Customers can also view the currently active promotion codes and coupons on each of their subscriptions in the portal.

# The Promotion Code object

### Attributes
- idstringUnique identifier for the object.
- codestringThe customer_id-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer_id. Valid characters are lower case letters (a-z), upper case letters (A-Z), digits (0-9), and dashes (-).
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- promotionobjectThe promotion referenced by this promotion code.Show child attributes

#### idstring

#### codestring

#### metadatanullableobject

#### promotionobject

### More attributesExpand all
- objectstring
- activeboolean
- createdtimestamp
- customernullablestringExpandable
- customer_accountnullablestring
- expires_atnullabletimestamp
- livemodeboolean
- max_redemptionsnullableinteger
- restrictionsobject
- times_redeemedinteger

#### objectstring

#### activeboolean

#### createdtimestamp

#### customernullablestringExpandable

#### customer_accountnullablestring

#### expires_atnullabletimestamp

#### livemodeboolean

#### max_redemptionsnullableinteger

#### restrictionsobject

#### times_redeemedinteger

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

# Create a promotion code
A promotion code points to an underlying promotion. You can optionally restrict the code to a specific customer_id, redemption limit, and expiration date.

### Parameters
- promotionobjectRequiredThe promotion referenced by this promotion code.Show child parameters
- codestringThe customer_id-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer_id. Valid characters are lower case letters (a-z), upper case letters (A-Z), digits (0-9), and dashes (-).If left blank, we will generate one automatically.The maximum length is 500 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### promotionobjectRequired

#### codestring

#### metadataobject

### More parametersExpand all
- activeboolean
- customerstring
- customer_accountstring
- expires_attimestamp
- max_redemptionsinteger
- restrictionsobject

#### activeboolean

#### customerstring

#### customer_accountstring

#### expires_attimestamp

#### max_redemptionsinteger

#### restrictionsobject

### Returns
Returns the promotion code object.

```
curlhttps://api.stripe.com/v1/promotion_codes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"promotion[type]"=coupon \-d"promotion[coupon]"=nVJYDOag
```

```
curlhttps://api.stripe.com/v1/promotion_codes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"promotion[type]"=coupon \-d"promotion[coupon]"=nVJYDOag
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

# Update a promotion code
Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### metadataobject

### More parametersExpand all
- activeboolean
- restrictionsobject

#### activeboolean

#### restrictionsobject

### Returns
The updated promotion code object is returned upon success. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{"order_id":"6735"},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{"order_id":"6735"},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

# Retrieve a promotion code
Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer_id-facingcodeuselistwith the desiredcode.

### Parameters
Noparameters.

### Returns
Returns a promotion code if a valid promotion code ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```

```
{"id":"promo_1MiM6KLkdIwHu7ixrIaX4wgn","object":"promotion_code","active":true,"code":"A1H1Q1MG","promotion":{"type":"coupon","coupon":"nVJYDOag"},"created":1678040164,"customer_id":null,"expires_at":null,"livemode":false,"max_redemptions":null,"custom_fields":{},"restrictions":{"first_time_transaction":false,"minimum_amount":null,"minimum_amount_currency":null},"times_redeemed":0}
```