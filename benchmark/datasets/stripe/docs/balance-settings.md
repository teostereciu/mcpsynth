# balance-settings

*Source: https://docs.stripe.com/api/balance-settings*

---

# Balance Settings
Options for customizing account balances and payout settings for a Stripe platform’s connected accounts.

# The Balance Setting object

### Attributes
- objectstringString representing the object’s type. Objects of the same type share the same value.
- paymentsobjectSettings that apply to thePayments Balance.Show child attributes

#### objectstring

#### paymentsobject

```
{"object":"balance_settings","payments":{"debit_negative_balances":true,"payouts":{"minimum_balance_by_currency":{"usd":1500,"cad":8000},"schedule":{"interval":"weekly","weekly_payout_days":["monday","wednesday"]},"statement_descriptor":null,"status":"enabled"},"settlement_timing":{"delay_days_override":3,"delay_days":3}}}
```

```
{"object":"balance_settings","payments":{"debit_negative_balances":true,"payouts":{"minimum_balance_by_currency":{"usd":1500,"cad":8000},"schedule":{"interval":"weekly","weekly_payout_days":["monday","wednesday"]},"statement_descriptor":null,"status":"enabled"},"settlement_timing":{"delay_days_override":3,"delay_days":3}}}
```

# Update balance settings
Updates balance settings for a given connected account.Related guide:Making API calls for connected accounts

### Parameters
- paymentsobjectSettings that apply to thePayments Balance.Show child parameters

#### paymentsobject

### Returns
Returns the updated balance settings object for the account that was authenticated in the request.

```
curlhttps://api.stripe.com/v1/balance_settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-H"Stripe-Account:{{CONNECTED_ACCOUNT_ID}}"\-d"payments[payouts][schedule][interval]"=monthly \-d"payments[payouts][schedule][monthly_payout_days][]"=5 \-d"payments[payouts][schedule][monthly_payout_days][]"=20
```

```
curlhttps://api.stripe.com/v1/balance_settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-H"Stripe-Account:{{CONNECTED_ACCOUNT_ID}}"\-d"payments[payouts][schedule][interval]"=monthly \-d"payments[payouts][schedule][monthly_payout_days][]"=5 \-d"payments[payouts][schedule][monthly_payout_days][]"=20
```

```
{"object":"balance_settings","payments":{"debit_negative_balances":true,"payouts":{"minimum_balance_by_currency":{"usd":1500,"cad":8000},"schedule":{"interval":"monthly","monthly_payout_days":[5,20]},"statement_descriptor":null,"status":"enabled"},"settlement_timing":{"delay_days_override":3,"delay_days":3}}}
```

```
{"object":"balance_settings","payments":{"debit_negative_balances":true,"payouts":{"minimum_balance_by_currency":{"usd":1500,"cad":8000},"schedule":{"interval":"monthly","monthly_payout_days":[5,20]},"statement_descriptor":null,"status":"enabled"},"settlement_timing":{"delay_days_override":3,"delay_days":3}}}
```

# Retrieve balance settings
Retrieves balance settings for a given connected account.Related guide:Making API calls for connected accounts

### Parameters
Noparameters.

### Returns
Returns a balance settings object for the account specified in the request.

```
curlhttps://api.stripe.com/v1/balance_settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-H"Stripe-Account:{{CONNECTED_ACCOUNT_ID}}"
```

```
curlhttps://api.stripe.com/v1/balance_settings \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-H"Stripe-Account:{{CONNECTED_ACCOUNT_ID}}"
```

```
{"object":"balance_settings","payments":{"debit_negative_balances":true,"payouts":{"minimum_balance_by_currency":{"usd":1500,"cad":8000},"schedule":{"interval":"weekly","weekly_payout_days":["monday","wednesday"]},"statement_descriptor":null,"status":"enabled"},"settlement_timing":{"delay_days_override":3,"delay_days":3}}}
```

```
{"object":"balance_settings","payments":{"debit_negative_balances":true,"payouts":{"minimum_balance_by_currency":{"usd":1500,"cad":8000},"schedule":{"interval":"weekly","weekly_payout_days":["monday","wednesday"]},"statement_descriptor":null,"status":"enabled"},"settlement_timing":{"delay_days_override":3,"delay_days":3}}}
```