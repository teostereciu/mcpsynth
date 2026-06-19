# transfers/4/post/transfers

*Source: https://docs.adyen.com/api-explorer/transfers/4/post/transfers*

---

# Transfer funds
Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.
Starts a request to transfer funds to:
- Balance accounts
- Transfer instruments
- Third-party bank accounts
- Third-party cards
Adyen sends the outcome of the transfer request through webhooks.
To use this endpoint:
- Your API credential must have theTransferService Webservice Initiaterole.
- The account holder must have the requiredcapabilities.
Reach out to your Adyen contact to set up these permissions.
Header for authenticating through SCA
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
The amount of the transfer.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The unique identifier of the sourcebalance account.
If you want to make a transfer using avirtualbankAccountassigned to the balance account, you must specify thepayment instrument IDof thevirtualbankAccount. If you only specify a balance account ID, Adyen uses the defaultphysicalbankAccountpayment instrument assigned to the balance account.
The category of the transfer.
Possible values:
- bank: A transfer involving atransfer instrumentor a bank account.
- card: A transfer involving a third-party card.
- internal: A transfer betweenbalance accountswithin your platform.
- issuedCard: A transfer initiated by an Adyen-issued card.
- platformPayment: Funds movements related to payments that are acquired for your users.
- topUp: An incoming transfer initiated by your user to top up their balance account.
The other party involved in the funds transfer. A bank account, a balance account, a card, or a transfer instrument is required.
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
The unique identifier of the counterpartytransfer instrument.
Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.
Supported characters:[a-z] [A-Z] [0-9] / - ?: ( ) . , ' + Space
Supported characters forregularandfasttransfers to a US counterparty:[a-z] [A-Z] [0-9] & $ % # @~ = + - _ ' " ! ?
The date when the transfer will be processed. This date must be within 30 days of the current date.
Until theexecutionDate:
- Thestatusof the transfer remains asreceived.
- Thereasonof the transfer remains aspending.
The date when the transfer will be processed. This date must be:
- Within 30 days of the current date.
- In theISO 8601 formatYYYY-MM-DD. For example: 2025-01-31
The timezone that applies to the execution date. Use a timezone identifier from thetz database.
Example:America/Los_Angeles.
Default value:Europe/Amsterdam.
The unique identifier of the sourcepayment instrument.
If you want to make a transfer using avirtualbankAccount, you must specify the payment instrument ID of thevirtualbankAccount. If you only specify a balance account ID, Adyen uses the defaultphysicalbankAccountpayment instrument assigned to the balance account.
The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. You can provide multiple priorities. Adyen will try to pay out using the priority you list first. If that's not possible, it moves on to the next option in the order of your provided priorities.
Possible values:
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).
Required for transfers withcategorybank. For more details, seefallback priorities.
The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.
Possible values:
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).
Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.
A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both parties involved in the funds movement.
Supported characters:a-z,A-Z,0-9. The maximum length depends on thecategory.
- internal: 80 characters
- bank: 35 characters when transferring to an IBAN, 15 characters for others.
Contains information required for triggering transfer reviews.
Specifies the number ofapprovalsrequired to process the transfer.
Specifies whether you will initiate Strong Customer Authentication (SCA) in thePOST/transfers/approverequest.
Only applies to transfers made with an Adyenbusiness account.
The type of transfer.
Possible values:
- bankTransfer: for push transfers to a transfer instrument or a bank account. Thecategorymust bebank.
- internalTransfer: for push transfers between balance accounts. Thecategorymust beinternal.
- internalDirectDebit: for pull transfers (direct debits) between balance accounts. Thecategorymust beinternal.
The ultimate sender of the funds of the transfer (ultimate debtor).
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
Details of the card or token used to fund the pay-in transaction.
Card details used for the transfer, such as the Primary Account Number (PAN) or stored payment method ID. Required ifsourceOfFundsisDEBIT. Provide either:
- storedPaymentMethodIdor
- expiryMonth,expiryYear, andnumber.
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
The unique reference assigned by the card network for the pay-in transaction.
Your internal reference that identifies this funding instrument. Required ifsourceOfFundsisDEPOSIT_ACCOUNT.
Indicates where the funds used for the transfer originated. Possible values are:
- DEBITfor card-to-card transfers.
- DEPOSIT_ACCOUNTfor wallet-to-card transfers.
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
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 202 - AcceptedThe request has been accepted for processing, but the processing has not been completed.Show moreShow lessaccountHolderobjectThe account holder associated with the balance account involved in the transfer.Show childrenHide childrendescriptionstringThe description of the resource.idstringThe unique identifier of the resource.referencestringThe reference for the resource.amountobjectThe amount of the transfer.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.balanceAccountobjectContains information about the balance account involved in the transfer.Show childrenHide childrendescriptionstringThe description of the resource.idstringThe unique identifier of the resource.referencestringThe reference for the resource.categorystringThe category of the transfer.Possible values:bank: A transfer involving atransfer instrumentor a bank account.card: A transfer involving a third-party card.internal: A transfer betweenbalance accountswithin your platform.issuedCard: A transfer initiated by an Adyen-issued card.platformPayment: Funds movements related to payments that are acquired for your users.topUp: An incoming transfer initiated by your user to top up their balance account.categoryDataThe relevant data according to the transfer category.Select categoryDataBankCategoryDataInternalCategoryDataIssuedCardPlatformPaymentcounterpartyobjectThe other party in the transfer.Show childrenHide childrenbalanceAccountIdstringThe unique identifier of the counterpartybalance account.bankAccountobjectContains information about the counterparty bank account.Show childrenHide childrenaccountHolderobjectInformation about the owner of the bank account.Show childrenHide childrenaddressobjectThe address of the bank account or card owner.Show childrenHide childrencitystringMin length:3The name of the city.Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.Required when thecategoryiscard.countrystringThe two-character ISO 3166-1 alpha-2 country code. For example,US,NL, orGB.line1stringThe first line of the street address.Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.Required when thecategoryiscard.line2stringThe second line of the street address.Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.Required when thecategoryiscard.postalCodestringMin length:3The postal code.
Maximum length:5 digits for an address in the US.10 characters for an address in all other countries.Supported characters:[a-z] [A-Z] [0-9]and Space.Required for addresses in the US.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.dateOfBirthstringThe date of birth of the individual inISO-8601format. For example,YYYY-MM-DD.Allowed only whentypeisindividual.emailstringMax length:254The email address of the organization or individual. Maximum length: 254 characters.firstNamestringThe first name of the individual.Supported characters: [a-z] [A-Z] - . / — and space.This parameter is:Allowed only whentypeisindividual.Required whencategoryiscard.fullNamestringThe full name of the entity that owns the bank account or card.Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.Required whencategoryisbank.lastNamestringThe last name of the individual.Supported characters: [a-z] [A-Z] - . / — and space.This parameter is:Allowed only whentypeisindividual.Required whencategoryiscard.referencestringMax length:150A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.Required when you includecardIdentification.storedPaymentMethodId.typestringThe type of entity that owns the bank account or card.Possible values:individual,organization, orunknown.Required whencategoryiscard. In this case, the value must beindividual.urlstringMax length:255The URL of the organization or individual. Maximum length: 255 characters.accountIdentificationContains the bank account details. The fields required in this object depend on the country of the bank account and the currency of the transfer.Select accountIdentificationAULocalAccountIdentificationBRLocalAccountIdentificationCALocalAccountIdentificationCZLocalAccountIdentificationDKLocalAccountIdentificationHKLocalAccountIdentificationHULocalAccountIdentificationIbanAccountIdentificationNOLocalAccountIdentificationNZLocalAccountIdentificationNumberAndBicAccountIdentificationPLLocalAccountIdentificationSELocalAccountIdentificationSGLocalAccountIdentificationUKLocalAccountIdentificationUSLocalAccountIdentificationstoredPaymentMethodIdstringThe unique token that identifies the stored bank account details of the counterparty for a payout.cardobjectContains information about the counterparty card.Show childrenHide childrencardHolderobjectContains information about the cardholder.Show childrenHide childrenaddressobjectThe address of the bank account or card owner.Show childrenHide childrencitystringMin length:3The name of the city.Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.Required when thecategoryiscard.countrystringThe two-character ISO 3166-1 alpha-2 country code. For example,US,NL, orGB.line1stringThe first line of the street address.Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.Required when thecategoryiscard.line2stringThe second line of the street address.Supported characters:[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |and Space.Required when thecategoryiscard.postalCodestringMin length:3The postal code.
Maximum length:5 digits for an address in the US.10 characters for an address in all other countries.Supported characters:[a-z] [A-Z] [0-9]and Space.Required for addresses in the US.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US orONin Canada.Required for the US and Canada.dateOfBirthstringThe date of birth of the individual inISO-8601format. For example,YYYY-MM-DD.Allowed only whentypeisindividual.emailstringMax length:254The email address of the organization or individual. Maximum length: 254 characters.firstNamestringThe first name of the individual.Supported characters: [a-z] [A-Z] - . / — and space.This parameter is:Allowed only whentypeisindividual.Required whencategoryiscard.fullNamestringThe full name of the entity that owns the bank account or card.Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.Required whencategoryisbank.lastNamestringThe last name of the individual.Supported characters: [a-z] [A-Z] - . / — and space.This parameter is:Allowed only whentypeisindividual.Required whencategoryiscard.referencestringMax length:150A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.Required when you includecardIdentification.storedPaymentMethodId.typestringThe type of entity that owns the bank account or card.Possible values:individual,organization, orunknown.Required whencategoryiscard. In this case, the value must beindividual.urlstringMax length:255The URL of the organization or individual. Maximum length: 255 characters.cardIdentificationobjectContains the identification details of the card.Show childrenHide childrenexpiryMonthstringMin length:2Max length:2The expiry month of the card.Format: two digits. Add a leading zero for single-digit months. For example:03 = March11 = NovemberexpiryYearstringMin length:4Max length:4The expiry year of the card.Format: four digits. For example: 2020issueNumberstringMin length:1Max length:2The issue number of the card. Applies only to some UK debit cards.numberstringMin length:4Max length:19The card number without any separators.For security, the response only includes the last four digits of the card number.startMonthstringMin length:2Max length:2The month when the card was issued. Applies only to some UK debit cards.Format: two digits. Add a leading zero for single-digit months. For example:03 = March11 = NovemberstartYearstringMin length:4Max length:4The year when the card was issued. Applies only to some UK debit cards.Format: four digits. For example: 2020storedPaymentMethodIdstringThe uniquetokencreated to identify the counterparty.merchantobjectContains information about the merchant.Show childrenHide childrenacquirerIdstringThe unique identifier of the merchant's acquirer.mccstringThe merchant category code.merchantIdstringThe unique identifier of the merchant.nameLocationobjectContains the name and location of the merchant.Show childrenHide childrencitystringThe city where the merchant is located.countrystringThe country where the merchant is located inthree-letter country codeformat.countryOfOriginstringThe home country inthree-digit country codeformat, used for government-controlled merchants such as embassies.namestringThe name of the merchant's shop or service.rawDatastringThe raw data.statestringThe state where the merchant is located.postalCodestringThe postal code of the merchant.transferInstrumentIdstringThe unique identifier of the counterpartytransfer instrument.createdAtstringThe date and time when the transfer was created, in ISO 8601 extended format. For example,2020-12-18T10:15:30+01:00.creationDatestringDeprecated in version 3Use createdAt or updatedAtThe date and time when the event was triggered, in ISO 8601 extended format. For example,2020-12-18T10:15:30+01:00.descriptionstringYour description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.Supported characters:[a-z] [A-Z] [0-9] / - ?: ( ) . , ' + SpaceSupported characters forregularandfasttransfers to a US counterparty:[a-z] [A-Z] [0-9] & $ % # @~ = + - _ ' " ! ?directDebitInformationobjectThe details of the direct debit.Show childrenHide childrendateOfSignaturestringThe date when the direct debit mandate was accepted by your user, inISO-8601format.dueDatestringThe date when the funds are deducted from your user's balance account.mandateIdstringYour unique identifier for the direct debit mandate.sequenceTypestringIdentifies the direct debit transfer's type.
Possible values:OneOff,First,Recurring,Final.directionstringThe direction of the transfer.Possible values:incoming,outgoing.executionDateobjectContains information about the date when the transfer will be processed. The execution date must be within 30 days of the current date.Until the execution date:Thestatusof the transfer remains asreceived.Thereasonof the transfer remains aspending.Show childrenHide childrendatestringThe date when the transfer will be processed. This date must be:Within 30 days of the current date.In theISO 8601 formatYYYY-MM-DD. For example: 2025-01-31timezonestringThe timezone that applies to the execution date. Use a timezone identifier from thetz database.Example:America/Los_Angeles.
Default value:Europe/Amsterdam.idstringThe ID of the resource.paymentInstrumentobjectContains information about the payment instrument used in the transfer.Show childrenHide childrendescriptionstringThe description of the resource.idstringThe unique identifier of the resource.referencestringThe reference for the resource.tokenTypestringThe type of wallet that the network token is associated with.reasonstringAdditional information about the status of the transfer.referencestringMax length:80Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.referenceForBeneficiarystringA reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.Supported characters:a-z,A-Z,0-9.The maximum length depends on thecategory.internal: 80 charactersbank: 35 characters when transferring to an IBAN, 15 characters for others.reviewobjectContains status updates related to additional reviews.Show childrenHide childrennumberOfApprovalsRequiredintegerShows the number ofapprovalsrequired to process the transfer.scaOnApprovalstringShows the status of the Strong Customer Authentication (SCA) process.Possible values:required,notApplicable.statusstringThe result of the transfer.For example:received: an outgoing transfer request is created.refused: the transfer request is rejected by Adyen for one of the following reasons:Lack of funds in the balance account.Transfer limit exceeded.Transaction rule requirements violated.authorised: the transfer request is authorized and the funds are reserved.booked: the funds are deducted from your user's balance account.failed: the transfer is rejected by the counterparty's bank.returned: the transfer is returned by the counterparty's bank.typestringThe type of transfer or transaction. For example,refund,payment,internalTransfer,bankTransfer.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.routingDetailsarray[object]Detailed explanation of each attempt to route the transfer with the priorities from the request.Show childrenHide childrendetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).titlestringA short, human-readable summary of the problem type.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.routingDetailsarray[object]Detailed explanation of each attempt to route the transfer with the priorities from the request.Show childrenHide childrendetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).titlestringA short, human-readable summary of the problem type.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.routingDetailsarray[object]Detailed explanation of each attempt to route the transfer with the priorities from the request.Show childrenHide childrendetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).titlestringA short, human-readable summary of the problem type.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 202 - Accepted
- bank: A transfer involving atransfer instrumentor a bank account.
- card: A transfer involving a third-party card.
- internal: A transfer betweenbalance accountswithin your platform.
- issuedCard: A transfer initiated by an Adyen-issued card.
- platformPayment: Funds movements related to payments that are acquired for your users.
- topUp: An incoming transfer initiated by your user to top up their balance account.
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
- Allowed only whentypeisindividual.
- Required whencategoryiscard.
- 03 = March
- 11 = November
- 03 = March
- 11 = November
- Thestatusof the transfer remains asreceived.
- Thereasonof the transfer remains aspending.
- Within 30 days of the current date.
- In theISO 8601 formatYYYY-MM-DD. For example: 2025-01-31
- internal: 80 characters
- bank: 35 characters when transferring to an IBAN, 15 characters for others.
- received: an outgoing transfer request is created.
- refused: the transfer request is rejected by Adyen for one of the following reasons:Lack of funds in the balance account.Transfer limit exceeded.Transaction rule requirements violated.
- authorised: the transfer request is authorized and the funds are reserved.
- booked: the funds are deducted from your user's balance account.
- failed: the transfer is rejected by the counterparty's bank.
- returned: the transfer is returned by the counterparty's bank.
- Lack of funds in the balance account.
- Transfer limit exceeded.
- Transaction rule requirements violated.

#### 401 - Unauthorized

#### 403 - Forbidden
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

#### 422 - Unprocessable Entity
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

#### 500 - Internal Server Error
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).