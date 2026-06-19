# cash_balance

*Source: https://docs.stripe.com/api/cash_balance*

---

# Cash Balance
A customer_id’sCash balancerepresents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.

# The Cash balance object

### Attributes
- objectstringString representing the object’s type. Objects of the same type share the same value.
- availablenullableobjectA hash of all cash balances available to this customer_id. You cannot delete a customer_id with any cash balances, even if the balance is 0. Amounts are represented in thesmallest currency_code unit.
- customerstringThe ID of the customer_id whose cash balance this object represents.
- customer_accountnullablestringThe ID of an Account representing a customer_id whose cash balance this object represents.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- settingsobjectA hash of settings for this cash balance.Show child attributes

#### objectstring

#### availablenullableobject

#### customerstring

#### customer_accountnullablestring

#### livemodeboolean

#### settingsobject

```
{"object":"cash_balance","available":{"eur":10000},"customer_id":"cus_OaCLf8Fi1nbFpJ","livemode":false,"settings":{"reconciliation_mode":"automatic","using_merchant_default":true}}
```

```
{"object":"cash_balance","available":{"eur":10000},"customer_id":"cus_OaCLf8Fi1nbFpJ","livemode":false,"settings":{"reconciliation_mode":"automatic","using_merchant_default":true}}
```

# Update a cash balance's settings
Changes the settings on a customer_id’s cash balance.

### Parameters
- settingsobjectA hash of settings for this cash balance.Show child parameters

#### settingsobject

### Returns
The customer_id’s cash balance, with the updated settings.

```
curlhttps://api.stripe.com/v1/customers/cus_Ob4Xiw8KXOqcvM/cash_balance \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"settings[reconciliation_mode]"=manual
```

```
curlhttps://api.stripe.com/v1/customers/cus_Ob4Xiw8KXOqcvM/cash_balance \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"settings[reconciliation_mode]"=manual
```

```
{"object":"cash_balance","available":null,"customer_id":"cus_Ob4Xiw8KXOqcvM","livemode":false,"settings":{"reconciliation_mode":"manual","using_merchant_default":false}}
```

```
{"object":"cash_balance","available":null,"customer_id":"cus_Ob4Xiw8KXOqcvM","livemode":false,"settings":{"reconciliation_mode":"manual","using_merchant_default":false}}
```

# Retrieve a cash balance
Retrieves a customer_id’s cash balance.

### Parameters
Noparameters.

### Returns
The Cash Balance object for a given customer_id.

```
curlhttps://api.stripe.com/v1/customers/cus_OaCLf8Fi1nbFpJ/cash_balance \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_OaCLf8Fi1nbFpJ/cash_balance \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"cash_balance","available":{"eur":10000},"customer_id":"cus_OaCLf8Fi1nbFpJ","livemode":false,"settings":{"reconciliation_mode":"automatic","using_merchant_default":true}}
```

```
{"object":"cash_balance","available":{"eur":10000},"customer_id":"cus_OaCLf8Fi1nbFpJ","livemode":false,"settings":{"reconciliation_mode":"automatic","using_merchant_default":true}}
```