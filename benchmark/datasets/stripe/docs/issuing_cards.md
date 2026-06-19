# issuing/cards

*Source: https://docs.stripe.com/api/issuing/cards*

---

# Cards
You cancreate physical or virtual cardsthat are issued to cardholders.

# The Card object

### Attributes
- idstringUnique identifier for the object.
- cancellation_reasonnullableenumThe reason why the card was canceled.Possible enum valuesdesign_rejectedThe design of this card was rejected by Stripe for violating ourpartner guidelines.lostThe card was lost.stolenThe card was stolen.
- cardholderobjectTheCardholderobject to which the card belongs.Show child attributes
- currencyenumThree-letterISO currency code, in lowercase. Supported currencies areusdin the US,eurin the EU, andgbpin the UK.
- exp_monthintegerThe expiration month of the card.
- exp_yearintegerThe expiration year of the card.
- last4stringThe last 4 digits of the card number.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- statusenumWhether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults toinactive.Possible enum valuesactiveThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.canceledThe card will decline authorizations with thecard_canceledreason. This status is permanent.inactiveThe card will decline authorizations with thecard_inactivereason.
- typeenumThe type of the card.Possible enum valuesphysicalA physical card will be printed and shipped. It can be used at physical terminals.virtualNo physical card will be printed. The card can be used online and can beadded to digital wallets.

#### idstring

#### cancellation_reasonnullableenum

[TABLE]
design_rejectedThe design of this card was rejected by Stripe for violating ourpartner guidelines.
lostThe card was lost.
stolenThe card was stolen.
[/TABLE]

```
design_rejected
```

#### cardholderobject

#### currencyenum

#### exp_monthinteger

#### exp_yearinteger

#### last4string

#### metadataobject

#### statusenum

[TABLE]
activeThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.
canceledThe card will decline authorizations with thecard_canceledreason. This status is permanent.
inactiveThe card will decline authorizations with thecard_inactivereason.
[/TABLE]

#### typeenum

[TABLE]
physicalA physical card will be printed and shipped. It can be used at physical terminals.
virtualNo physical card will be printed. The card can be used online and can beadded to digital wallets.
[/TABLE]

### More attributesExpand all
- objectstring
- brandstring
- createdtimestamp
- cvcnullablestringExpandable
- latest_fraud_warningnullableobject
- livemodeboolean
- numbernullablestringExpandable
- personalization_designnullablestringExpandable
- replaced_bynullablestringExpandable
- replacement_fornullablestringExpandable
- replacement_reasonnullableenum
- second_linenullablestring
- shippingnullableobject
- spending_controlsobject
- walletsnullableobject

#### objectstring

#### brandstring

#### createdtimestamp

#### cvcnullablestringExpandable

#### latest_fraud_warningnullableobject

#### livemodeboolean

#### numbernullablestringExpandable

#### personalization_designnullablestringExpandable

#### replaced_bynullablestringExpandable

#### replacement_fornullablestringExpandable

#### replacement_reasonnullableenum

#### second_linenullablestring

#### shippingnullableobject

#### spending_controlsobject

#### walletsnullableobject

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

# Create a card
Creates an IssuingCardobject.

### Parameters
- currencystringRequiredThe currency for the card.
- typeenumRequiredThe type of card to issue. Possible values arephysicalorvirtual.Possible enum valuesphysicalA physical card will be printed and shipped. It can be used at physical terminals.virtualNo physical card will be printed. The card can be used online and can beadded to digital wallets.
- cardholderstringRequiredTheCardholderobject with which the card will be associated.
- exp_monthintegerThe desired expiration month (1-12) for this card ifspecifying a custom expiration date.
- exp_yearintegerThe desired 4-digit expiration year for this card ifspecifying a custom expiration date.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statusenumWhether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults toinactive.Possible enum valuesactiveThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.inactiveThe card will decline authorizations with thecard_inactivereason.

#### currencystringRequired

#### typeenumRequired

[TABLE]
physicalA physical card will be printed and shipped. It can be used at physical terminals.
virtualNo physical card will be printed. The card can be used online and can beadded to digital wallets.
[/TABLE]

#### cardholderstringRequired

#### exp_monthinteger

#### exp_yearinteger

#### metadataobject

#### statusenum

[TABLE]
activeThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.
inactiveThe card will decline authorizations with thecard_inactivereason.
[/TABLE]

### More parametersExpand all
- personalization_designstring
- pinobject
- replacement_forstring
- replacement_reasonenum
- second_linestring
- shippingobject
- spending_controlsobject

#### personalization_designstring

#### pinobject

#### replacement_forstring

#### replacement_reasonenum

#### second_linestring

#### shippingobject

#### spending_controlsobject

### Returns
Returns an IssuingCardobject if creation succeeds.

```
curlhttps://api.stripe.com/v1/issuing/cards \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d cardholder=ich_1MsKAB2eZvKYlo2C3eZ2BdvK \-d currency=usd \-d type=virtual
```

```
curlhttps://api.stripe.com/v1/issuing/cards \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d cardholder=ich_1MsKAB2eZvKYlo2C3eZ2BdvK \-d currency=usd \-d type=virtual
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

# Update a card
Updates the specified IssuingCardobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters
- cancellation_reasonenumReason why thestatusof this card iscanceled.Possible enum valueslostThe card was lost.stolenThe card was stolen.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statusenumDictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults toinactive. If this card is being canceled because it was lost or stolen, this information should be provided ascancellation_reason.Possible enum valuesactiveThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.canceledThe card will decline authorizations with thecard_canceledreason. This status is permanent.inactiveThe card will decline authorizations with thecard_inactivereason.

#### cancellation_reasonenum

[TABLE]
lostThe card was lost.
stolenThe card was stolen.
[/TABLE]

#### metadataobject

#### statusenum

[TABLE]
activeThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.
canceledThe card will decline authorizations with thecard_canceledreason. This status is permanent.
inactiveThe card will decline authorizations with thecard_inactivereason.
[/TABLE]

### More parametersExpand all
- pinobject
- shippingobject
- spending_controlsobject

#### pinobject

#### shippingobject

#### spending_controlsobject

### Returns
Returns an updated IssuingCardobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{"order_id":"6735"},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{"order_id":"6735"},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

# Retrieve a card
Retrieves an IssuingCardobject.

### Parameters
Noparameters.

### Returns
Returns an IssuingCardobject if a valid identifier was provided. When requesting the ID of a card that has been deleted, a subset of the card’s information will be returned, including adeletedproperty, which will be true.

```
curlhttps://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```

```
{"id":"ic_1MvSieLkdIwHu7ixn6uuO0Xu","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1MsKAB2eZvKYlo2C3eZ2BdvK","object":"issuing.cardholder","billing":{"address":{"city":"Anytown","country":"US","line1":"123 Main Street","line2":null,"postal_code":"12345","state":"CA"}},"company":null,"created":1680415995,"email":null,"individual":null,"livemode":false,"metadata":{},"name":"John Doe","phone_number":null,"requirements":{"disabled_reason":"requirements.past_due","past_due":["individual.card_issuing.user_terms_acceptance.ip","individual.card_issuing.user_terms_acceptance.date","individual.first_name","individual.last_name"]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1681163868,"currency":"usd","exp_month":8,"exp_year":2024,"last4":"4242","livemode":false,"metadata":{},"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"google_pay":{"eligible":false,"ineligible_reason":"missing_cardholder_contact"},"primary_account_identifier":null}}
```