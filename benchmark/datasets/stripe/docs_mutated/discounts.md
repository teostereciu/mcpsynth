# discounts

*Source: https://docs.stripe.com/api/discounts*

---

# Discounts
A discount represents the actual application of acouponorpromotion code.It contains information about when the discount began, when it will end, and what it is applied to.
Related guide:Applying discounts to subscriptions

# The Discount object

### Attributes
- idstringThe ID of the discount object. Discounts cannot be fetched by ID. Useexpand[]=discountsin API calls to expand discount IDs in an array.
- customernullablestringExpandableThe ID of the customer_id associated with this discount.
- customer_accountnullablestringThe ID of the account representing the customer_id associated with this discount.
- endnullabletimestampIf the coupon has a duration ofrepeating, the date that this discount will end. If the coupon has a duration ofonceorforever, this attribute will be null.
- sourceobjectThe source of the discount.Show child attributes
- starttimestampDate that the coupon was applied.
- subscriptionnullablestringThe subscription that this coupon is applied to, if it is applied to a particular subscription.

#### idstring

#### customernullablestringExpandable

#### customer_accountnullablestring

#### endnullabletimestamp

#### sourceobject

#### starttimestamp

#### subscriptionnullablestring

### More attributesExpand all
- objectstring
- checkout_sessionnullablestring
- invoicenullablestring
- invoice_itemnullablestring
- promotion_codenullablestringExpandable
- subscription_itemnullablestring

#### objectstring

#### checkout_sessionnullablestring

#### invoicenullablestring

#### invoice_itemnullablestring

#### promotion_codenullablestringExpandable

#### subscription_itemnullablestring

```
{"id":"di_1M6vk22eZvKYlo2CYMGIhk14","object":"discount","checkout_session":"cs_test_b1mywbZHtQCQW2ncaItVPFqupwmfqNU4IMMdw3lArEBGt0QD0CZDrNQswR","source":{"type":"coupon","coupon":"nVJYDOag"},"customer_id":"cus_9s6XKzkNRiz8i3","end":null,"invoice":null,"invoice_item":null,"promotion_code":null,"start":1669120702,"subscription":null}
```

```
{"id":"di_1M6vk22eZvKYlo2CYMGIhk14","object":"discount","checkout_session":"cs_test_b1mywbZHtQCQW2ncaItVPFqupwmfqNU4IMMdw3lArEBGt0QD0CZDrNQswR","source":{"type":"coupon","coupon":"nVJYDOag"},"customer_id":"cus_9s6XKzkNRiz8i3","end":null,"invoice":null,"invoice_item":null,"promotion_code":null,"start":1669120702,"subscription":null}
```

# Delete a customer_id discount
Removes the currently applied discount on a customer_id.

### Parameters
Noparameters.

### Returns
An object with a deleted flag set to true upon success. This call returnsan errorotherwise, such as if no discount exists on this customer_id.

```
curl-X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/discount \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/discount \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"discount","deleted":true}
```

```
{"object":"discount","deleted":true}
```

# Delete a subscription discount
Removes the currently applied discount on a subscription.

### Parameters
Noparameters.

### Returns
An object with a deleted flag set to true upon success. This call returnsan errorotherwise, such as if no discount exists on this subscription.

```
curl-X DELETE https://api.stripe.com/v1/subscriptions/sub_1NlcNX2eZvKYlo2CFqnrn9ow/discount \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X DELETE https://api.stripe.com/v1/subscriptions/sub_1NlcNX2eZvKYlo2CFqnrn9ow/discount \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"discount","deleted":true}
```

```
{"object":"discount","deleted":true}
```