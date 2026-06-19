# transfer-webhooks/4/post/balancePlatform.transfer.created

*Source: https://docs.adyen.com/api-explorer/transfer-webhooks/4/post/balancePlatform.transfer.created*

---

# Transfer created
Adyen sends this webhook when there are fund movements on your platform.
Contains details about the event.
The account holder associated with the balance account involved in the transfer.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The amount of the transfer.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains information about the balance account involved in the transfer.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The unique identifier of the balance platform.
The list of the latest balance statuses in the transfer.
The amount in the payment's currency that is debited or credited on the balance accounting register.
The three-characterISO currency code.
The amount in the payment's currency that is debited or credited on the received accounting register.
The amount in the payment's currency that is debited or credited on the reserved accounting register.
The category of the transfer.
Possible values:
- bank: A transfer involving atransfer instrumentor a bank account.
- card: A transfer involving a third-party card.
- internal: A transfer betweenbalance accountswithin your platform.
- issuedCard: A transfer initiated by an Adyen-issued card.
- platformPayment: Funds movements related to payments that are acquired for your users.
- topUp: An incoming transfer initiated by your user to top up their balance account.
The relevant data according to the transfer category.
The other party in the transfer.
The unique identifier of the counterpartybalance account.
Contains information about the counterparty bank account.
Information about the owner of the bank account.
The address of the bank account or card owner.
The name of the city.
Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.
Required when thecategoryiscard.
The two-character ISO 3166-1 alpha-2 country code. For example,US,NL, orGB.
The first line of the street address.
Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.
Required when thecategoryiscard.
The second line of the street address.
Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.
Required when thecategoryiscard.
The postal code.
Maximum length:
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
Supported characters:[a-z] [A-Z] [0-9]and Space.
Required for addresses in the US.
The two-letter ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The date of birth of the individual inISO-8601format. For example,YYYY-MM-DD.
Allowed only whentypeisindividual.
The email address of the organization or individual. Maximum length: 254 characters.
The first name of the individual.
Supported characters: [a-z] [A-Z] - . / — and space.
This parameter is:
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
The full name of the entity that owns the bank account or card.
Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.
Required whencategoryisbank.
The last name of the individual.
Supported characters: [a-z] [A-Z] - . / — and space.
This parameter is:
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.
Required when you includecardIdentification.storedPaymentMethodId.
The type of entity that owns the bank account or card.
Possible values:individual,organization, orunknown.
Required whencategoryiscard. In this case, the value must beindividual.
The URL of the organization or individual. Maximum length: 255 characters.
Contains the bank account details. The fields required in this object depend on the country of the bank account and the currency of the transfer.
The unique token that identifies the stored bank account details of the counterparty for a payout.
Contains information about the counterparty card.
Contains information about the cardholder.
The address of the bank account or card owner.
The name of the city.
Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.
Required when thecategoryiscard.
The two-character ISO 3166-1 alpha-2 country code. For example,US,NL, orGB.
The first line of the street address.
Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.
Required when thecategoryiscard.
The second line of the street address.
Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.
Required when thecategoryiscard.
The postal code.
Maximum length:
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
Supported characters:[a-z] [A-Z] [0-9]and Space.
Required for addresses in the US.
The two-letter ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The date of birth of the individual inISO-8601format. For example,YYYY-MM-DD.
Allowed only whentypeisindividual.
The email address of the organization or individual. Maximum length: 254 characters.
The first name of the individual.
Supported characters: [a-z] [A-Z] - . / — and space.
This parameter is:
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
The full name of the entity that owns the bank account or card.
Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.
Required whencategoryisbank.
The last name of the individual.
Supported characters: [a-z] [A-Z] - . / — and space.
This parameter is:
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.
Required when you includecardIdentification.storedPaymentMethodId.
The type of entity that owns the bank account or card.
Possible values:individual,organization, orunknown.
Required whencategoryiscard. In this case, the value must beindividual.
The URL of the organization or individual. Maximum length: 255 characters.
Contains the identification details of the card.
The expiry month of the card.
Format: two digits. Add a leading zero for single-digit months. For example:
- 03 = March
- 11 = November
The expiry year of the card.
Format: four digits. For example: 2020
The issue number of the card. Applies only to some UK debit cards.
The card number without any separators.
For security, the response only includes the last four digits of the card number.
The month when the card was issued. Applies only to some UK debit cards.
Format: two digits. Add a leading zero for single-digit months. For example:
- 03 = March
- 11 = November
The year when the card was issued. Applies only to some UK debit cards.
Format: four digits. For example: 2020
The uniquetokencreated to identify the counterparty.
Contains information about the merchant.
The unique identifier of the merchant's acquirer.
The city where the merchant is located.
The country where the merchant is located.
The merchant category code.
The unique identifier of the merchant.
The name of the merchant's shop or service.
The postal code of the merchant.
The unique identifier of the counterpartytransfer instrument.
The date and time when the transfer was created, in ISO 8601 extended format. For example,2020-12-18T10:15:30+01:00.
Use createdAt or updatedAt
The date and time when the event was triggered, in ISO 8601 extended format. For example,2020-12-18T10:15:30+01:00.
Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.
Supported characters:[a-z] [A-Z] [0-9] / - ?: ( ) . , ' + Space
Supported characters forregularandfasttransfers to a US counterparty:[a-z] [A-Z] [0-9] & $ % # @~ = + - _ ' " ! ?
The details of the direct debit.
The date when the direct debit mandate was accepted by your user, inISO-8601format.
The date when the funds are deducted from your user's balance account.
Your unique identifier for the direct debit mandate.
Identifies the direct debit transfer's type.
Possible values:OneOff,First,Recurring,Final.
The direction of the transfer.
Possible values:incoming,outgoing.
The unique identifier of the latest transfer event. Included only when thecategoryisissuedCard.
The list of events leading up to the current status of the transfer.
The original journal amount. Only applicable forissuingintegrations.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The amount adjustments in this transfer. Only applicable forissuingintegrations.
The adjustment amount.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The type of markup that is applied to an authorised payment.
Possible values:exchange,forexMarkup,authHoldReserve,atmMarkup.
The basepoints associated with the applied markup.
Scheme unique arn identifier useful for tracing captures, chargebacks, refunds, etc.
The date when the transfer request was sent.
The estimated time when the beneficiary should have access to the funds.
A list of event data.
The external reason for the transfer status.
The reason code.
The description of the reason code.
The namespace for the reason code.
The unique identifier of the transfer event.
The payment modification. Only applicable forreturned internal transfers.
The direction of the money movement.
Our reference for the modification.
Your reference for the modification, used internally within your platform.
The status of the transfer event.
The type of transfer modification.
The list of balance mutations per event.
The amount in the payment's currency that is debited or credited on the balance accounting register.
The three-characterISO currency code.
The amount in the payment's currency that is debited or credited on the received accounting register.
The amount in the payment's currency that is debited or credited on the reserved accounting register.
The amount in the original currency. Only applicable forissuingintegrations.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The reason for the transfer status.
The status of the transfer event.
Additional information for the tracking event.
The id of the transaction that is related to this accounting event. Only sent for events of typeaccountingwhere the balance changes.
The type of the transfer event. Possible values:accounting,tracking.
The date when the tracking status was updated.
The date when the funds are expected to be deducted from or credited to the balance account. This date can be in either the past or future.
Contains information about the date when the transfer will be processed. The execution date must be within 30 days of the current date.
Until the execution date:
- Thestatusof the transfer remains asreceived.
- Thereasonof the transfer remains aspending.
The date when the transfer will be processed. This date must be:
- Within 30 days of the current date.
- In theISO 8601 formatYYYY-MM-DD. For example: 2025-01-31
The timezone that applies to the execution date. Use a timezone identifier from thetz database.
Example:America/Los_Angeles.
Default value:Europe/Amsterdam.
The external reason of this transfer.
The reason code.
The description of the reason code.
The namespace for the reason code.
The ID of the resource.
Contains information about the payment instrument used in the transfer.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The type of wallet that the network token is associated with.
Additional information about the status of the transfer.
Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.
A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.
Supported characters:a-z,A-Z,0-9.The maximum length depends on thecategory.
- internal: 80 characters
- bank: 35 characters when transferring to an IBAN, 15 characters for others.
Contains status updates related to additional reviews.
Shows the number ofapprovalsrequired to process the transfer.
Shows the status of the Strong Customer Authentication (SCA) process.
Possible values:required,notApplicable.
The sequence number of the transfer webhook. The numbers start from 1 and increase with each new webhook for a specific transfer.
The sequence number can help you restore the correct sequence of events even if they arrive out of order.
The result of the transfer.
For example:
- received: an outgoing transfer request is created.
- refused: the transfer request is rejected by Adyen for one of the following reasons:Lack of funds in the balance account.Transfer limit exceeded.Transaction rule requirements violated.
- authorised: the transfer request is authorized and the funds are reserved.
- booked: the funds are deducted from your user's balance account.
- failed: the transfer is rejected by the counterparty's bank.
- returned: the transfer is returned by the counterparty's bank.
- Lack of funds in the balance account.
- Transfer limit exceeded.
- Transaction rule requirements violated.
The latest tracking information of the transfer.
Contains the results of the evaluation of the transaction rules.
The advice given by the Risk analysis.
Indicates whether the transaction passed the evaluation for all hardblock rules
The score of the Risk analysis.
Array containing all the transaction rules that the transaction triggered.
An explanation about why the transaction rule failed.
Contains information about the transaction rule.
The description of the resource.
The unique identifier of the resource.
The outcome type of the rule.
The reference for the resource.
The transaction score determined by the rule. Returned only whenoutcomeTypeisscoreBased.
Contains information about the resource to which the transaction rule applies.
ID of the resource, when applicable.
Indicates the type of resource for which the transaction rule is defined.
Possible values:
- PaymentInstrumentGroup
- PaymentInstrument
- BalancePlatform
- EntityUsageConfiguration
- PlatformRule: The transaction rule is a platform-wide rule imposed by Adyen.
The type of transfer or transaction. For example,refund,payment,internalTransfer,bankTransfer.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2020-12-18T10:15:30+01:00.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
The type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK