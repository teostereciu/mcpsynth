# account_sessions

*Source: https://docs.stripe.com/api/account_sessions*

---

# Account Session
An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.
We recommend that you create an AccountSession each time you need to display an embedded componentto your user. Do not save AccountSessions to your database as they expire relativelyquickly, and cannot be used more than once.
Related guide:Connect embedded components

# The Account Session object

### Attributes
- accountstringThe ID of the account the AccountSession was created for
- client_secretstringThe client secret of this AccountSession. Used on the client to set up secure access to the givenaccount.The client secret can be used to provide access toaccountfrom your frontend. It should not be stored, logged, or exposed to anyone other than the connected account. Make sure that you have TLS enabled on any page that includes the client secret.Refer to our docs tosetup Connect embedded componentsand learn about howclient_secretshould be handled.
- componentsobjectInformation about which embedded components and component features are enabled for this Account Session. Components that have no features have an emptyfeatureshash.Show child attributes
- expires_attimestampThe timestamp at which this AccountSession will expire.

#### accountstring

#### client_secretstring

#### componentsobject

#### expires_attimestamp

### More attributesExpand all
- objectstring
- livemodeboolean

#### objectstring

#### livemodeboolean

```
{"object":"account_session","account":"acct_1NkDjjJyhOZfPCWt","client_secret":"_OXIKXxEihJokDBnDoe2sgG5OGSO2Q12shKvbeboxpALZGng","expires_at":1693261123,"livemode":false,"components":{"account_management":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"account_onboarding":{"enabled":true,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"balances":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"documents":{"enabled":false,"features":{}},"financial_account":{"enabled":false,"features":{"disable_stripe_user_authentication":false,"external_account_collection":false,"money_movement":false,"send_money":false,"transfer_balance":false}},"financial_account_transactions":{"enabled":false,"features":{"card_spend_dispute_management":false}},"issuing_card":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"spend_control_management":false}},"issuing_cards_list":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"disable_stripe_user_authentication":false,"spend_control_management":false}},"notification_banner":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"payment_details":{"enabled":false,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payments":{"enabled":true,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payouts":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"payouts_list":{"enabled":false,"features":{}},"tax_registrations":{"enabled":false,"features":{}},"tax_settings":{"enabled":false,"features":{}}}}
```

```
{"object":"account_session","account":"acct_1NkDjjJyhOZfPCWt","client_secret":"_OXIKXxEihJokDBnDoe2sgG5OGSO2Q12shKvbeboxpALZGng","expires_at":1693261123,"livemode":false,"components":{"account_management":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"account_onboarding":{"enabled":true,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"balances":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"documents":{"enabled":false,"features":{}},"financial_account":{"enabled":false,"features":{"disable_stripe_user_authentication":false,"external_account_collection":false,"money_movement":false,"send_money":false,"transfer_balance":false}},"financial_account_transactions":{"enabled":false,"features":{"card_spend_dispute_management":false}},"issuing_card":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"spend_control_management":false}},"issuing_cards_list":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"disable_stripe_user_authentication":false,"spend_control_management":false}},"notification_banner":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"payment_details":{"enabled":false,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payments":{"enabled":true,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payouts":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"payouts_list":{"enabled":false,"features":{}},"tax_registrations":{"enabled":false,"features":{}},"tax_settings":{"enabled":false,"features":{}}}}
```

# Create an Account Session
Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.

### Parameters
- accountstringRequiredThe identifier of the account to create an Account Session for.
- componentsobjectRequiredEach key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).Show child parameters

#### accountstringRequired

#### componentsobjectRequired

### Returns
Returns an Account Session object if the call succeeded.

```
curlhttps://api.stripe.com/v1/account_sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d account=acct_1NkDjjJyhOZfPCWt \-d"components[account_onboarding][enabled]"=true \-d"components[payments][enabled]"=true \-d"components[payouts][enabled]"=true \-d"components[balances][enabled]"=true
```

```
curlhttps://api.stripe.com/v1/account_sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d account=acct_1NkDjjJyhOZfPCWt \-d"components[account_onboarding][enabled]"=true \-d"components[payments][enabled]"=true \-d"components[payouts][enabled]"=true \-d"components[balances][enabled]"=true
```

```
{"object":"account_session","account":"acct_1NkDjjJyhOZfPCWt","client_secret":"_OXIKXxEihJokDBnDoe2sgG5OGSO2Q12shKvbeboxpALZGng","expires_at":1693261123,"livemode":false,"components":{"account_management":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"account_onboarding":{"enabled":true,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"balances":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"documents":{"enabled":false,"features":{}},"financial_account":{"enabled":false,"features":{"disable_stripe_user_authentication":false,"external_account_collection":false,"money_movement":false,"send_money":false,"transfer_balance":false}},"financial_account_transactions":{"enabled":false,"features":{"card_spend_dispute_management":false}},"issuing_card":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"spend_control_management":false}},"issuing_cards_list":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"disable_stripe_user_authentication":false,"spend_control_management":false}},"notification_banner":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"payment_details":{"enabled":false,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payments":{"enabled":true,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"disputes_list":{"enabled":false,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payment_disputes":{"enabled":false,"features":{"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payouts":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"payouts_list":{"enabled":false,"features":{}},"tax_registrations":{"enabled":false,"features":{}},"tax_settings":{"enabled":false,"features":{}},"instant_payouts_promotion":{"enabled":false,"features":{"disable_stripe_user_authentication":false,"external_account_collection":true,"instant_payouts":false}},"payout_details":{"enabled":false,"features":{}}}}
```

```
{"object":"account_session","account":"acct_1NkDjjJyhOZfPCWt","client_secret":"_OXIKXxEihJokDBnDoe2sgG5OGSO2Q12shKvbeboxpALZGng","expires_at":1693261123,"livemode":false,"components":{"account_management":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"account_onboarding":{"enabled":true,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"balances":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"documents":{"enabled":false,"features":{}},"financial_account":{"enabled":false,"features":{"disable_stripe_user_authentication":false,"external_account_collection":false,"money_movement":false,"send_money":false,"transfer_balance":false}},"financial_account_transactions":{"enabled":false,"features":{"card_spend_dispute_management":false}},"issuing_card":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"spend_control_management":false}},"issuing_cards_list":{"enabled":false,"features":{"card_management":false,"card_spend_dispute_management":false,"cardholder_management":false,"disable_stripe_user_authentication":false,"spend_control_management":false}},"notification_banner":{"enabled":false,"features":{"external_account_collection":true,"disable_stripe_user_authentication":false}},"payment_details":{"enabled":false,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payments":{"enabled":true,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"disputes_list":{"enabled":false,"features":{"capture_payments":true,"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payment_disputes":{"enabled":false,"features":{"destination_on_behalf_of_charge_management":false,"dispute_management":true,"refund_management":true}},"payouts":{"enabled":true,"features":{"edit_payout_schedule":false,"instant_payouts":false,"standard_payouts":false,"external_account_collection":true,"disable_stripe_user_authentication":false}},"payouts_list":{"enabled":false,"features":{}},"tax_registrations":{"enabled":false,"features":{}},"tax_settings":{"enabled":false,"features":{}},"instant_payouts_promotion":{"enabled":false,"features":{"disable_stripe_user_authentication":false,"external_account_collection":true,"instant_payouts":false}},"payout_details":{"enabled":false,"features":{}}}}
```