# billing/credit-balance-summary

*Source: https://docs.stripe.com/api/billing/credit-balance-summary*

---

# Credit Balance Summary
Indicates the billing credit balance for billing credits granted to a customer.

# The Credit Balance Summary object

### Attributes
- objectstringString representing the object’s type. Objects of the same type share the same value.
- balancesarray of objectsThe billing credit balances. One entry per credit grant currency. If a customer only has credit grants in a single currency, then this will have a single balance entry.Show child attributes
- customerstringExpandableThe customer the balance is for.
- customer_accountnullablestringThe account the balance is for.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.

#### objectstring

#### balancesarray of objects

#### customerstringExpandable

#### customer_accountnullablestring

#### livemodeboolean

```
{"object":"billing.credit_balance_summary","balances":[{"available_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"ledger_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"}}],"customer":"cus_QsEHa3GKweMwih","livemode":false}
```

```
{"object":"billing.credit_balance_summary","balances":[{"available_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"ledger_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"}}],"customer":"cus_QsEHa3GKweMwih","livemode":false}
```

# Retrieve the credit balance summary for a customer
Retrieves the credit balance summary for a customer.

### Parameters
- filterobjectRequiredThe filter criteria for the credit balance summary.Show child parameters
- customerstringThe customer whose credit balance summary you’re retrieving.
- customer_accountstringThe account representing the customer whose credit balance summary you’re retrieving.

#### filterobjectRequired

#### customerstring

#### customer_accountstring

### Returns
Returns the credit balance summary.

```
curl-G https://api.stripe.com/v1/billing/credit_balance_summary \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_QsEHa3GKweMwih \-d"filter[type]"=credit_grant \-d"filter[credit_grant]"=credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW
```

```
curl-G https://api.stripe.com/v1/billing/credit_balance_summary \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer=cus_QsEHa3GKweMwih \-d"filter[type]"=credit_grant \-d"filter[credit_grant]"=credgr_test_61R9rvFh1HgrFIoCp41L6nFOS1ekDCeW
```

```
{"object":"billing.credit_balance_summary","balances":[{"available_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"ledger_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"}}],"customer":"cus_QsEHa3GKweMwih","livemode":false}
```

```
{"object":"billing.credit_balance_summary","balances":[{"available_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"},"ledger_balance":{"monetary":{"currency":"usd","value":1000},"type":"monetary"}}],"customer":"cus_QsEHa3GKweMwih","livemode":false}
```