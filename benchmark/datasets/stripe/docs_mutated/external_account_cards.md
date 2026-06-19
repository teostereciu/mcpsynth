# external_account_cards

*Source: https://docs.stripe.com/api/external_account_cards*

---

# External Account Cards
External account cards are debit cards associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected accounts Stripe balance.

# The External Account Card object

### Attributes
- idstringUnique identifier for the object.
- accountnullablestringExpandableAvailable conditionallyThe account this card belongs to. This attribute will not be in the card object if the card belongs to a customer_id or recipient instead. This property is only available for accounts wherecontroller.is_controlleristrue.
- address_citynullablestringCity/District/Suburb/Town/Village.
- address_countrynullablestringBilling address country, if provided when creating card.
- address_line1nullablestringAddress line 1 (Street address/PO Box/Company name).
- address_line2nullablestringAddress line 2 (Apartment/Suite/Unit/Building).
- address_statenullablestringState/County/Province/Region.
- address_zipnullablestringZIP or postal code.
- address_zip_checknullablestringIfaddress_zipwas provided, results of the check:pass,fail,unavailable, orunchecked.
- brandstringCard brand. Can beAmerican Express,Cartes Bancaires,Diners Club,Discover,Eftpos Australia,Girocard,JCB,MasterCard,UnionPay,Visa, orUnknown.
- countrynullablestringTwo-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.
- currencynullableenumAvailable conditionallyThree-letterISO code for currencyin lowercase. Must be asupported currency_code. Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency_code. This property is only available for accounts wherecontroller.is_controlleristrue.
- cvc_checknullablestringIf a CVC was provided, results of the check:pass,fail,unavailable, orunchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, seeCheck if a card is valid without a charge.
- default_for_currencynullablebooleanAvailable conditionallyWhether this card is the default external account for its currency_code. This property is only available for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.
- exp_monthintegerTwo-digit number representing the card’s expiration month.
- exp_yearintegerFour-digit number representing the card’s expiration year.
- fingerprintnullablestringUniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.
- fundingstringCard funding type. Can becredit,debit,prepaid, orunknown.
- last4stringThe last four digits of the card.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- namenullablestringCardholder name.
- statusnullablestringFor external accounts that are cards, possible values arenewanderrored. If a payout fails, the status is set toerroredandscheduled payoutsare stopped until account details are updated.

#### idstring

#### accountnullablestringExpandableAvailable conditionally

#### address_citynullablestring

#### address_countrynullablestring

#### address_line1nullablestring

#### address_line2nullablestring

#### address_statenullablestring

#### address_zipnullablestring

#### address_zip_checknullablestring

#### brandstring

#### countrynullablestring

#### currencynullableenumAvailable conditionally

#### cvc_checknullablestring

#### default_for_currencynullablebooleanAvailable conditionally

#### exp_monthinteger

#### exp_yearinteger

#### fingerprintnullablestring

#### fundingstring

#### last4string

#### metadatanullableobject

#### namenullablestring

#### statusnullablestring

### More attributesExpand all
- objectstring
- address_line1_checknullablestring
- allow_redisplaynullableenum
- available_payout_methodsnullablearray of enums
- customernullablestringExpandable
- dynamic_last4nullablestring
- iinnullablestring
- regulated_statusnullableenum
- tokenization_methodnullablestring
- walletnullableobjectPreview feature

#### objectstring

#### address_line1_checknullablestring

#### allow_redisplaynullableenum

#### available_payout_methodsnullablearray of enums

#### customernullablestringExpandable

#### dynamic_last4nullablestring

#### iinnullablestring

#### regulated_statusnullableenum

#### tokenization_methodnullablestring

#### walletnullableobjectPreview feature

```
{"id":"card_1MvoiELkdIwHu7ixOeFGbN9D","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","customer_id":"cus_NhD8HD2bY8dP3V","cvc_check":null,"dynamic_last4":null,"exp_month":4,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","last4":"4242","custom_fields":{},"name":null,"tokenization_method":null,"wallet":null}
```

```
{"id":"card_1MvoiELkdIwHu7ixOeFGbN9D","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","customer_id":"cus_NhD8HD2bY8dP3V","cvc_check":null,"dynamic_last4":null,"exp_month":4,"exp_year":2024,"fingerprint":"mToisGZ01V71BCos","funding":"credit","last4":"4242","custom_fields":{},"name":null,"tokenization_method":null,"wallet":null}
```

# Create a card
When you create a new debit card, you must specify aconnected accountto create it on. You can only specify connected accounts whereaccount.controller.requirement_collectionisapplication(includesCustom accounts).
If the account has no default destination card, then the new card will become the default. However, if the owner already has a default then it will not change. To change the default, you should setdefault_for_currencytotrue.

### Parameters
- external_accountobject | stringRequiredA token, like the ones returned byStripe.jsor a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### external_accountobject | stringRequired

#### metadataobject

### More parametersExpand all
- default_for_currencyboolean

#### default_for_currencyboolean

### Returns
Returns the card object

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d external_account=tok_visa_debit
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d external_account=tok_visa_debit
```

```
{"id":"card_1NAiaG2eZvKYlo2CDXvcMb6m","object":"card","account":"acct_1032D82eZvKYlo2C","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"pass","dynamic_last4":null,"exp_month":8,"exp_year":2024,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","last4":"4242","custom_fields":{},"name":null,"redaction":null,"tokenization_method":null,"wallet":null}
```

```
{"id":"card_1NAiaG2eZvKYlo2CDXvcMb6m","object":"card","account":"acct_1032D82eZvKYlo2C","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"pass","dynamic_last4":null,"exp_month":8,"exp_year":2024,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","last4":"4242","custom_fields":{},"name":null,"redaction":null,"tokenization_method":null,"wallet":null}
```

# Update a card
If you need to update only some card details, like the billing address or expiration date, you can do so without having to re-enter the full card details. Stripe also works directly with card networks so that your customers cancontinue using your servicewithout interruption.

### Parameters
- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency_code.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### default_for_currencyboolean

#### metadataobject

### More parametersExpand all
- address_citystring
- address_countrystring
- address_line1string
- address_line2string
- address_statestring
- address_zipstring
- exp_monthstring
- exp_yearstring
- namestring

#### address_citystring

#### address_countrystring

#### address_line1string

#### address_line2string

#### address_statestring

#### address_zipstring

#### exp_monthstring

#### exp_yearstring

#### namestring

### Returns
Returns the card object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NBLeN2eZvKYlo2CIq1o7Pzs \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NBLeN2eZvKYlo2CIq1o7Pzs \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"card_1NBLeN2eZvKYlo2CIq1o7Pzs","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"pass","dynamic_last4":null,"exp_month":8,"exp_year":2024,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","last4":"4242","custom_fields":{"order_id":"6735"},"name":"Jenny Rosen","redaction":null,"tokenization_method":null,"wallet":null,"account":"acct_1032D82eZvKYlo2C"}
```

```
{"id":"card_1NBLeN2eZvKYlo2CIq1o7Pzs","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"pass","dynamic_last4":null,"exp_month":8,"exp_year":2024,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","last4":"4242","custom_fields":{"order_id":"6735"},"name":"Jenny Rosen","redaction":null,"tokenization_method":null,"wallet":null,"account":"acct_1032D82eZvKYlo2C"}
```

# Retrieve a card
By default, you can see the 10 most recent external accounts stored on aconnected accountdirectly on the object. You can alsoretrieve details about a specific card stored on the account.

### Parameters
- idstringRequiredUnique identifier for the external account to be retrieved.

#### idstringRequired

### Returns
Returns the card object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAinb2eZvKYlo2C1Fm9mZsu \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAinb2eZvKYlo2C1Fm9mZsu \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"card_1NAinb2eZvKYlo2C1Fm9mZsu","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"pass","dynamic_last4":null,"exp_month":8,"exp_year":2024,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","last4":"4242","custom_fields":{},"name":null,"redaction":null,"tokenization_method":null,"wallet":null,"account":"acct_1032D82eZvKYlo2C"}
```

```
{"id":"card_1NAinb2eZvKYlo2C1Fm9mZsu","object":"card","address_city":null,"address_country":null,"address_line1":null,"address_line1_check":null,"address_line2":null,"address_state":null,"address_zip":null,"address_zip_check":null,"brand":"Visa","country":"US","cvc_check":"pass","dynamic_last4":null,"exp_month":8,"exp_year":2024,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","last4":"4242","custom_fields":{},"name":null,"redaction":null,"tokenization_method":null,"wallet":null,"account":"acct_1032D82eZvKYlo2C"}
```