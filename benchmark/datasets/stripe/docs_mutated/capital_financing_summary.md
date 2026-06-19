# capital/financing_summary

*Source: https://docs.stripe.com/api/capital/financing_summary*

---

# Financing SummaryPreview
A financing summary object describes a connected account’s financing status in real time.A financing status is eitheraccepted,delivered, ornone.You can read the status of your connected accounts.

# The Financing Summary objectPreview

### Attributes
- objectstringThe object type: financing_summary
- detailsnullableobjectAdditional information about the financing summary. Describes currency_code, advance amount,fee amount, withhold rate, remaining amount, paid amount, current repayment interval,repayment start date, and advance payout date.Only present for financing offers with thepaid_outstatus.Show child attributes
- financing_offernullablestringThe unique identifier of the Financing Offer object that corresponds to the Financing Summary object.
- statusnullableenumDeprecatedThe financing status of the connected account.Possible enum valuesacceptedThe connected account has an active financing offer that has been paid out.deliveredA financing offer has been marketed to the connected account, but the account hasn’t accepted it yet.noneThe connected account doesn’t have any active financing.

#### objectstring

#### detailsnullableobject

#### financing_offernullablestring

#### statusnullableenumDeprecated

[TABLE]
acceptedThe connected account has an active financing offer that has been paid out.
deliveredA financing offer has been marketed to the connected account, but the account hasn’t accepted it yet.
noneThe connected account doesn’t have any active financing.
[/TABLE]

```
{"object":"capital.financing_summary","details":{"advance_amount":100000,"advance_paid_out_at":1688424277.0578003,"currency_code":"usd","current_repayment_interval":null,"fee_amount":10000,"paid_amount":100263,"remaining_amount":9737,"repayments_begin_at":1688424277.0577993,"withhold_rate":0.05},"financing_offer":"financingoffer_1NPvU12eZvKYlo2CotjdGRzu","status":"accepted"}
```

```
{"object":"capital.financing_summary","details":{"advance_amount":100000,"advance_paid_out_at":1688424277.0578003,"currency_code":"usd","current_repayment_interval":null,"fee_amount":10000,"paid_amount":100263,"remaining_amount":9737,"repayments_begin_at":1688424277.0577993,"withhold_rate":0.05},"financing_offer":"financingoffer_1NPvU12eZvKYlo2CotjdGRzu","status":"accepted"}
```

# Retrieve financing summary
Retrieve the financing summary object for the account.

### Parameters
Noparameters.

### Returns
Returns a financing summary object for the account.

```
curlhttps://api.stripe.com/v1/capital/financing_summary \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-H"Stripe-Account:{{CONNECTED_ACCOUNT_ID}}"
```

```
curlhttps://api.stripe.com/v1/capital/financing_summary \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-H"Stripe-Account:{{CONNECTED_ACCOUNT_ID}}"
```

```
{"object":"capital.financing_summary","details":{"advance_amount":100000,"advance_paid_out_at":1688424277.0578003,"currency_code":"usd","current_repayment_interval":null,"fee_amount":10000,"paid_amount":100263,"remaining_amount":9737,"repayments_begin_at":1688424277.0577993,"withhold_rate":0.05},"financing_offer":"financingoffer_1NPvU12eZvKYlo2CotjdGRzu","status":"accepted"}
```

```
{"object":"capital.financing_summary","details":{"advance_amount":100000,"advance_paid_out_at":1688424277.0578003,"currency_code":"usd","current_repayment_interval":null,"fee_amount":10000,"paid_amount":100263,"remaining_amount":9737,"repayments_begin_at":1688424277.0577993,"withhold_rate":0.05},"financing_offer":"financingoffer_1NPvU12eZvKYlo2CotjdGRzu","status":"accepted"}
```