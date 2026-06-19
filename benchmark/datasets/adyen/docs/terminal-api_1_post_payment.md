# terminal-api/1/post/payment

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/payment*

---

# Payment Request
Request sent to terminal to initiate payment.
It conveys Information related to the Payment transaction to process.
Content of thePaymentRequestmessage.
Data associated with the Sale System, with a particular value during the processing of the payment by the POI, including the cards acquisition.
Identification of the Cashier or Operator.
Language of the Cashier or Operator.
If different from the Login.
Shift number.
If different from the Login, see Login SaleData.
Identification of a transaction for the Sale System or the POI System.
Unique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.
Date and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.
Identification of a Sale global transaction for a sequence of related POI transactions.
If payment reservation.
Information related to the software and hardware features of the Sale Terminal.
Sent in the Login Request if a Sale Terminal is involved in the login. In other messages, sent when a logical device is out of order (SaleCapabilities) or when other data have changed or were missing in the Login.
Identification of a group of transactions on a POI Terminal, having the same Sale features.
Could be used to group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login Request.
Type of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a merchant, to use a token for a transaction only or for a longer period.
Possible values:
- Customer
- Transaction
Additional and optional identification of a customer order.
List of customer order open, closed or both to be sent in the response messages.
Possible values:
- Both
- Closed
- Open
Sale information intended for the POI.
Stored with the transaction.
Sale information intended for the Acquirer.
Send to the Acquirer if present.
Sale information intended for the Issuer.
The POI System receives this information and sends it to the Acquirer for the Issuer without any change.
Label to print on the bank statement.
Data related to the payment and loyalty transaction.
Various amounts related to the payment request from the Sale System.
Currency of a monetary amount.
Amount requested by the Sale for the payment.
The cash-back part of the amount requested by the Sale for the payment.
Amount paid for a tip. Allow the printing of the tip on the receipt, and to qualify the tip part of the amount.
Amount already paid in case of split payment. Depending on the context, a split payment is either a split amount, or a split basket (required by some payment means as fleet cards). The PaidAmount is present when the split payment is a split
of the amount. Split of the basket involves two Sale Transactions, and does not have to be recognised by
the POI.
Minimum amount the Sale System is allowed to deliver for this payment. For the OneTimeReservation, when the maximum amount is unknown, the Sale System indicates the minimum amount it allows.
Maximum amount which could be requested for cash-back to the Sale System. Allows the Cashier
to limit the amount value of cash-back to deliver to the Customer.
Minimum amount of a split, which could be requested by a Customer.Allows the Merchant to limit the number of split requested by the Customer.
Identification of a previous POI transaction.
In the Payment Request message, it allows using the card of a previous CardAcquisition or Payment request.
Identification of a Sale System for the NEXO SaletoPOI protocol.
Identification of a payment terminal for the NEXO SaletoPOI protocol.
If original transaction is coming from another POI.
Identification of a transaction for the Sale System or the POI System.
Unique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.
Date and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.
Indicates if the card data has to be retrieved from a previous transaction.
Code assigned to a transaction approval by the Acquirer.
If referral.
Identification of the Acquirer.
Restrict to the Acquirer if present.
Value of an amount.
Identification of a transaction for the Sale System or the POI System.
Unique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.
Date and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.
Conditions on which the transaction must be processed.
Payment brands accepted for this transaction.
Card payment brands allowed by the Sale System for the payment transaction.
Restrict brand if data sent.
Identification of the Acquirer.
Restrict to these Acquirer if present.
The preferred type of payment is a debit transaction rather than a credit transaction.
Loyalty brands or programs allowed by the Sale System for the loyalty transaction.
Restrict brand if data sent.
Type of Loyalty processing requested by the Sale System.
Possible values:
- Allowed
- Forbidden
- Processed
- Proposed
- Required
The language used on the terminal screen or in text printed by the terminal.
Typical use case is setting the language on unattended terminals. Format: two-characterISO 639:2023format.
Indicates if the Cashier requires POI forces online access to the Acquirer.
Go online if data sent.
Payment instrument entry mode requested by the Sale System.
Restrict entry mode if sent.
Possible values:
- CheckReader
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- RFID
- Scanned
- SynchronousICC
- Tapped
The code which identifies the category of the transaction (MCC).
The payment implies a specific MCC.
Data related to the payment transaction.
If one data element is present.
Type of payment transaction. Elements requested by the Sale System that are related to the payment only.
Possible values:
- CashAdvance
- CashDeposit
- Completion
- FirstReservation
- Instalment
- IssuerInstalment
- Normal
- OneTimeReservation
- PaidOut
- Recurring
- Refund
- UpdateReservation
Indicates if the payment of the Sale transaction is split. Allows the POI to decline payment means that cannot accept split payment.
Requested validity date for the reservation. Allows a specific period for the reservation according to the need of the Merchant for the first reservation and the reservation updates as well.
Identification of a transaction for the Sale System or the POI System.
Unique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.
Date and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.
Information related an instalment transaction. To request an instalment to the issuer, or to make individual instalments of a payment transaction.
Type of instalment transaction. For requesting an instalment payment transaction.
Possible values:
- DeferredInstalments
- EqualInstalments
- InequalInstalments
Sequence number of the instalment. For an instalment payment transaction, number of the payment, from 1 to TotalNbOfPayments.
Identification of an instalment plan.
Period of time with defined unit of time. A period between 2 payment instalments.
Type of instalment transaction.
Possible values:
- Annual
- Daily
- Monthly
- Weekly
First date of a payment. For instalment, the date of the first payments, if not immediate.
Total number of payments. For instalment, the number of payments, including the first one.
Sum of a collection of amounts. Total amount of the payment instalments.
First amount of the payment instalments.
Charges related to a transaction. Charge related to the payment instalments.
Data related to the instrument of payment for the transaction.
Sent in the result of the payment transaction. For a card, it could also be sent in theCardAcquisitionresponse, to be processed by the Sale System.
Type of payment instrument.
Possible values:
- Card
- Cash
- Check
- Mobile
- StoredValue
Sensitive information related to the payment card, protected by CMS.
SensitiveCardData protected by CMS EnvelopedData.
Information related to the payment card used for the transaction.
Allows acquisition of the card data by the Sale System before the Payment, CardAcquisition, or BalanceInquiry request to the POI. It can also be sent in the CardAcquisition response, to be processed by the Sale System.
Type of payment card.
If card PAN is readable.
Indicates the card used to pay in the PaymentResponse. Sent in the CardAcquisitionResponse, to leave the Cashier to choose between several applications in a smartcard, or several brand in a co-branded card. In this case, the CardAcquisitionRequest.ForceCustomerSelectionFlag must contain the value False. Brands are part of the POI and Sale Systems configurations.
Masked Primary Account Number
Part of the PAN is replaced by a string of * characters, to identify a customer account or relationship. Presence of this data element, which replace the PAN when SensitiveCardData is protected and replaced by ProtectedCardData. Alternatively the MaskedPAN can be used as a token to identify a customer.
Reference of the PAN, which identifies the PAN or the card uniquely, named also PAR (Payment Account Reference). This reference may be defined by the card issuer or by a token service provider under the control of the card issuer, and cannot be used for a payment transaction.
Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.
Possible values:
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- Mobile
- RFID
- Scanned
- SynchronousICC
- Tapped
Country Code attached to the card (3 numerics).
If available in the card.
Sensitive information related to the payment card, protected by CMS.
SensitiveCardData protected by CMS EnvelopedData.
This data structure could be CMS protected (EnvelopedData). In this case the data structure SensitiveCardData is replaced by the data structure ProtectedCardData of type ContentInformationType.
When this data is protected, the exact content is unknown by the Sale System, and might include
all the information which are required by an external backup POI Server to make a batch payment
transaction in case of problem with the POI System.
Sensitive information related to the payment card, entered or read
by the Sale System.
Primary Account Number.
Card Sequence Number.
If EntryMode is File, Keyed, or Manual.
Date after which the card cannot be used.
If EntryMode is File.
Magnetic track or magnetic ink characters line.
If EntryMode is MagStripe or RFID .
Card track number.
Magnetic track or magnetic ink characters line.
Possible values:
- AAMVA
- ISO
Card track content.
Surrogate of the PAN (Primary Account Number) of the payment card to
identify the payment mean of the customer. It allows, for a merchant, to identify
the customer.
Type of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a merchant, to use a token for a transaction only or for a longer period.
Possible values:
- Customer
- Transaction
Payment token replacing the PAN of the payment card to identify the payment
mean of the customer.
Expiry date and time. Limits the validity of a payment token.
Information related to the paper check used for the transaction.
Allows the check information to be provided by the Sale System before requesting the payment, or stored by the Sale System after processing of the payment.
Identification of the bank.
Mandatory if TrackData absent.
Identification of the customer account.
Mandatory if TrackData absent.
Identification of the bank check.
Mandatory if TrackData absent.
Magnetic track or magnetic ink characters line.
ISO 7813 - ISO 4909.
Generic data structure for a card track, used when the magstripe card reader is located on the Sale Terminal, or for magstripe Card Reader device request. The data structure is also used to store the line at the bottom of a bank check.
Card track number.
Magnetic track or magnetic ink characters line.
Possible values:
- AAMVA
- ISO
Card track content.
Check guarantee card number.
If provided by the customer.
Type of bank check.
Possible values:
- Company
- Personal
Country of the bank check.
Absent if country of the Sale system.
Mobile phone is used as a payment instrument for the transaction.
Information related to the mobile for the payment transaction.
Identifies the country of a mobile phone operator.
If data available.
Identifies the mobile phone operator inside a country.
If data available.
Masked Mobile Subscriber Integrated Service Digital Network.
If data available.
Geographic location specified by geographic or UTM coordinates.
If data available.
Angular distance of a location on the earth south or north of the equator.
Angular measurement of the distance of a location on the earth east or west of the Greenwich observatory.
UTM grid zone combination of the longitude zone (1 to 60) and the latitude band (C to X, excluding I and O).
X-coordinate of the Universal Transverse Mercator coordinate system.
Y-coordinate of the Universal Transverse Mercator coordinate system.
Sensitive information related to the mobile phone, protected by CMS.
SensitiveMobileData.
Sensitive information related to the mobile phone.
If unprotected mobile data.
Mobile Subscriber Integrated Service Digital Network (i.e. mobile phone number of the SIM card). Country, National Destination Code, and Subscriber Number.
International Mobile Subscriber Identity. Unique number associated with the mobile phone user, containing the Mobile Country Code (MCC), the Mobile Network Code (MNC), and the Mobile Identification Number (MSIN)
International Mobile Equipment Identity. Unique number associated with the mobile phone device.
Identification of the stored value account or the stored value card and the associated product sold by the Sale System for stored value requests.
Type of stored value account. Allows the distinction of the stored value instrument to access the stored value account.
Possible values:
- GiftCard
- Other
- PhoneCard
Identification of the provider of the stored value account load/reload. When the ProductCode is not sufficient to identify the provider host which delivers the load or reload of the stored value account (for example if it contains the identification of the application.)
Name of the owner of a stored value account.
Date after which the card cannot be used. If EMV expiry date is present, it overrides Track2 information. Format is MMYY.
Entry mode of the payment instrument information. In the Payment, Loyalty, or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. (e.g. because the payment instrument information are a barcode read by the Cashier on a scanner device).
Possible values:
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- Mobile
- RFID
- Scanned
- SynchronousICC
- Tapped
Type of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.
Possible values:
- AccountNumber
- BarCode
- ISOTrack2
- PAN
- PhoneNumber
Stored value account identification. The identification of the stored value account conforming to the IdentificationType.
Data related to a Loyalty program or account.
Loyalty cards used with the payment transaction and read by the Sale System.
Identification of a transaction for the Sale System or the POI System.
Unique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.
Date and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.
Identification of a Loyalty account.
In the Payment Request message, it allows to identify the loyalty account by the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the Cashier on a scanner device).
Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.
Possible values:
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- Mobile
- RFID
- Scanned
- SynchronousICC
- Tapped
Type of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.
Possible values:
- AccountNumber
- BarCode
- ISOTrack2
- PAN
- PhoneNumber
Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:
- HybridCard
- LinkedCard
- LoyaltyCard
- NoCard
Loyalty account identification conforming to the IdentificationType.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys Information related to the Payment transaction processed by the POI System.
Content of the Payment Response message.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.SaleDataobjectData associated with the Sale System, with a particular value during the processing of the payment by the POI, including the cards acquisition.Show childrenHide childrenOperatorIDstringIdentification of the Cashier or Operator.OperatorLanguagestringLanguage of the Cashier or Operator.
If different from the Login.ShiftNumberstringShift number.
If different from the Login, see Login SaleData.SaleTransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.SaleReferenceIDstringIdentification of a Sale global transaction for a sequence of related POI transactions.
If payment reservation.SaleTerminalDataobjectInformation related to the software and hardware features of the Sale Terminal.
Sent in the Login Request if a Sale Terminal is involved in the login. In other messages, sent when a logical device is out of order (SaleCapabilities) or when other data have changed or were missing in the Login.Show childrenHide childrenTotalsGroupIDstringIdentification of a group of transactions on a POI Terminal, having the same Sale features.
Could be used to group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login Request.TokenRequestedTypestringType of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a merchant, to use a token for a transaction only or for a longer period.
Possible values:CustomerTransactionCustomerOrderIDstringAdditional and optional identification of a customer order.CustomerOrderReqarray[string]List of customer order open, closed or both to be sent in the response messages.
Possible values:BothClosedOpenSaleToPOIDatastringSale information intended for the POI.
Stored with the transaction.SaleToAcquirerDatastringSale information intended for the Acquirer.
Send to the Acquirer if present.SaleToIssuerDataobjectSale information intended for the Issuer.
The POI System receives this information and sends it to the Acquirer for the Issuer without any change.Show childrenHide childrenStatementReferencestringLabel to print on the bank statement.POIDataobjectData related to the POI System.
In the Message Response, identification of the POI transaction.Show childrenHide childrenPOITransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.POIReconciliationIDintegerIdentification of the reconciliation period between Sale and POI.
If Result is Success.PaymentResultobjectData related to the result of a processed payment transaction.
If one data element is present.Show childrenHide childrenPaymentTypestringType of payment transaction. Elements requested by the Sale System that are related to the payment only.
Possible values:CashAdvanceCashDepositCompletionFirstReservationInstalmentIssuerInstalmentNormalOneTimeReservationPaidOutRecurringRefundUpdateReservationPaymentInstrumentDataobjectData related to the instrument of payment for the transaction.
Sent in the result of the payment transaction. For a card, it could also be sent in theCardAcquisitionresponse, to be processed by the Sale System.Show childrenHide childrenPaymentInstrumentTypestringType of payment instrument.
Possible values:CardCashCheckMobileStoredValueProtectedCardDatastringSensitive information related to the payment card, protected by CMS.
SensitiveCardData protected by CMS EnvelopedData.CardDataobjectInformation related to the payment card used for the transaction.
Allows acquisition of the card data by the Sale System before the Payment, CardAcquisition, or BalanceInquiry request to the POI. It can also be sent in the CardAcquisition response, to be processed by the Sale System.Show childrenHide childrenPaymentBrandstringType of payment card.
If card PAN is readable.
Indicates the card used to pay in the PaymentResponse. Sent in the CardAcquisitionResponse, to leave the Cashier to choose between several applications in a smartcard, or several brand in a co-branded card. In this case, the CardAcquisitionRequest.ForceCustomerSelectionFlag must contain the value False. Brands are part of the POI and Sale Systems configurations.MaskedPanstringMasked Primary Account Number
Part of the PAN is replaced by a string of * characters, to identify a customer account or relationship. Presence of this data element, which replace the PAN when SensitiveCardData is protected and replaced by ProtectedCardData. Alternatively the MaskedPAN can be used as a token to identify a customer.PaymentAccountRefstringReference of the PAN, which identifies the PAN or the card uniquely, named also PAR (Payment Account Reference). This reference may be defined by the card issuer or by a token service provider under the control of the card issuer, and cannot be used for a payment transaction.EntryModearray[string]Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.
Possible values:ContactlessFileICCKeyedMagStripeManualMobileRFIDScannedSynchronousICCTappedCardCountryCodeintegerMinimum:3Maximum:3Country Code attached to the card (3 numerics).
If available in the card.ProtectedCardDatastringSensitive information related to the payment card, protected by CMS.
SensitiveCardData protected by CMS EnvelopedData.SensitiveCardDataobjectThis data structure could be CMS protected (EnvelopedData). In this case the data structure SensitiveCardData is replaced by the data structure ProtectedCardData of type ContentInformationType.
When this data is protected, the exact content is unknown by the Sale System, and might include
all the information which are required by an external backup POI Server to make a batch payment
transaction in case of problem with the POI System.
Sensitive information related to the payment card, entered or read
by the Sale System.Show childrenHide childrenPANintegerMinimum:8Maximum:28Primary Account Number.CardSeqNumbintegerMinimum:2Maximum:3Card Sequence Number.
If EntryMode is File, Keyed, or Manual.ExpiryDateintegerMinimum:4Maximum:4Date after which the card cannot be used.
If EntryMode is File.TrackDataarray[object]Magnetic track or magnetic ink characters line.
If EntryMode is MagStripe or RFID .Show childrenHide childrenTrackNumbintegerMinimum:1Maximum:3Card track number.TrackFormatstringMagnetic track or magnetic ink characters line.
Possible values:AAMVAISOTrackValuestringCard track content.PaymentTokenobjectSurrogate of the PAN (Primary Account Number) of the payment card to
identify the payment mean of the customer. It allows, for a merchant, to identify
the customer.Show childrenHide childrenTokenRequestedTypestringType of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a merchant, to use a token for a transaction only or for a longer period.
Possible values:CustomerTransactionTokenValuestringPayment token replacing the PAN of the payment card to identify the payment
mean of the customer.ExpiryDateTimestringExpiry date and time. Limits the validity of a payment token.CheckDataobjectInformation related to the paper check used for the transaction.
Allows the check information to be provided by the Sale System before requesting the payment, or stored by the Sale System after processing of the payment.Show childrenHide childrenBankIDstringIdentification of the bank.
Mandatory if TrackData absent.AccountNumberstringIdentification of the customer account.
Mandatory if TrackData absent.CheckNumberstringIdentification of the bank check.
Mandatory if TrackData absent.TrackDataobjectMagnetic track or magnetic ink characters line.
ISO 7813 - ISO 4909.
Generic data structure for a card track, used when the magstripe card reader is located on the Sale Terminal, or for magstripe Card Reader device request. The data structure is also used to store the line at the bottom of a bank check.Show childrenHide childrenTrackNumbintegerMinimum:1Maximum:3Card track number.TrackFormatstringMagnetic track or magnetic ink characters line.
Possible values:AAMVAISOTrackValuestringCard track content.CheckCardNumberstringCheck guarantee card number.
If provided by the customer.TypeCodestringType of bank check.
Possible values:CompanyPersonalCountrystringCountry of the bank check.
Absent if country of the Sale system.MobileDataobjectMobile phone is used as a payment instrument for the transaction.
Information related to the mobile for the payment transaction.Show childrenHide childrenMobileCountryCodeintegerMinimum:3Maximum:3Identifies the country of a mobile phone operator.
If data available.MobileNetworkCodeintegerMinimum:2Maximum:3Identifies the mobile phone operator inside a country.
If data available.MaskedMSISDNintegerMasked Mobile Subscriber Integrated Service Digital Network.
If data available.GeolocationobjectGeographic location specified by geographic or UTM coordinates.
If data available.Show childrenHide childrenGeographicCoordinatesobjectShow childrenHide childrenLatitudestringAngular distance of a location on the earth south or north of the equator.LongitudestringAngular measurement of the distance of a location on the earth east or west of the Greenwich observatory.UTMCoordinatesobjectShow childrenHide childrenUTMZonestringUTM grid zone combination of the longitude zone (1 to 60) and the latitude band (C to X, excluding I and O).UTMEastwardstringX-coordinate of the Universal Transverse Mercator coordinate system.UTMNorthwardstringY-coordinate of the Universal Transverse Mercator coordinate system.ProtectedMobileDatastringSensitive information related to the mobile phone, protected by CMS.
SensitiveMobileData.SensitiveMobileDataobjectSensitive information related to the mobile phone.
If unprotected mobile data.Show childrenHide childrenMSISDNintegerMobile Subscriber Integrated Service Digital Network (i.e. mobile phone number of the SIM card). Country, National Destination Code, and Subscriber Number.IMSIintegerInternational Mobile Subscriber Identity. Unique number associated with the mobile phone user, containing the Mobile Country Code (MCC), the Mobile Network Code (MNC), and the Mobile Identification Number (MSIN)IMEIintegerInternational Mobile Equipment Identity. Unique number associated with the mobile phone device.StoredValueAccountIDobjectIdentification of the stored value account or the stored value card and the associated product sold by the Sale System for stored value requests.Show childrenHide childrenStoredValueAccountTypestringType of stored value account. Allows the distinction of the stored value instrument to access the stored value account.
Possible values:GiftCardOtherPhoneCardStoredValueProviderstringIdentification of the provider of the stored value account load/reload. When the ProductCode is not sufficient to identify the provider host which delivers the load or reload of the stored value account (for example if it contains the identification of the application.)OwnerNamestringName of the owner of a stored value account.ExpiryDateintegerMinimum:4Maximum:4Date after which the card cannot be used. If EMV expiry date is present, it overrides Track2 information. Format is MMYY.EntryModearray[string]Entry mode of the payment instrument information. In the Payment, Loyalty, or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. (e.g. because the payment instrument information are a barcode read by the Cashier on a scanner device).
Possible values:ContactlessFileICCKeyedMagStripeManualMobileRFIDScannedSynchronousICCTappedIdentificationTypestringType of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.
Possible values:AccountNumberBarCodeISOTrack2PANPhoneNumberStoredValueIDstringStored value account identification. The identification of the stored value account conforming to the IdentificationType.AmountsRespobjectVarious amounts related to the payment response from the POI System. Amounts approved by the POI and the Acquirer for the payment and loyalty transaction, containing:The authorised amount to be paid.The amount of the rebates.The amount of financial fees.The cash back part of the requested amount for a payment with cash back.The tip part of the requested amount for a payment with tip.Show childrenHide childrenCurrencystringCurrency of a monetary amount.AuthorizedAmountnumberMaximum:99999999.999999Amount requested by the Sale for the payment.TotalRebatesAmountnumberMaximum:99999999.999999Sum of rebates in amount (total amount or line item amount) for all the loyalty programs.TotalFeesAmountnumberMaximum:99999999.999999Total amount of financial fees.CashBackAmountnumberMaximum:99999999.999999The cash-back part of the amount requested by the Sale for the payment.TipAmountnumberMaximum:99999999.999999Amount paid for a tip. Allow the printing of the tip on the receipt, and to qualify the tip part of the amount.InstalmentobjectInformation related an instalment transaction. To request an instalment to the issuer, or to make individual instalments of a payment transaction.Show childrenHide childrenInstalmentTypestringType of instalment transaction. For requesting an instalment payment transaction.
Possible values:DeferredInstalmentsEqualInstalmentsInequalInstalmentsSequenceNumberintegerSequence number of the instalment. For an instalment payment transaction, number of the payment, from 1 to TotalNbOfPayments.PlanIDstringIdentification of an instalment plan.PeriodintegerPeriod of time with defined unit of time. A period between 2 payment instalments.PeriodUnitstringType of instalment transaction.
Possible values:AnnualDailyMonthlyWeeklyFirstPaymentDatestringFirst date of a payment. For instalment, the date of the first payments, if not immediate.TotalNbOfPaymentsintegerTotal number of payments. For instalment, the number of payments, including the first one.CumulativeAmountnumberMaximum:99999999.999999Sum of a collection of amounts. Total amount of the payment instalments.FirstAmountnumberMaximum:99999999.999999First amount of the payment instalments.ChargesnumberMaximum:99999999.999999Charges related to a transaction. Charge related to the payment instalments.CurrencyConversionarray[object]Information related to a currency conversion. A currency conversion occurred in the payment, and the merchant needs to know information related to this conversion (e.g. to print on the sale receipt).Show childrenHide childrenCustomerApprovedFlagbooleanNotify if the customer has approved something. Indicates if the customer has accepted a currency conversion.ConvertedAmountobjectAmount after a currency conversion.Show childrenHide childrenAmountValuenumberMaximum:99999999.999999Value of an amount.CurrencystringCurrency of a monetary amount.RatestringRate of currency conversion.MarkupstringMarkup of a currency conversion amount as a percentage.CommissionnumberMaximum:99999999.999999Commission for a currency conversion.DeclarationstringDeclaration to present to the customer or the cashier for validation.
If a declaration has to be presented to the customer.MerchantOverrideFlagbooleanIndicates that the Merchant forced the result of the payment to successful. Allows the Sale System to be sure that the payment has been forced.CapturedSignatureobjectNumeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a cardholder on the merchant payment receipt. Only one format of the signature is allowed:The size of the pad area where the signature is written, given with the maximum abscissa and ordinate values.The sequence of coordinates where the pen changes direction or lift.Show childrenHide childrenAreaSizeobjectSize of an area. Contain the size of the pad area where the signature is written, given with the maximum abscissa and ordinate values (X and Y). The maximum value is FFFF.Show childrenHide childrenXstringAbscissa of a point coordinates. The hexadecimal value in text of the abscissa of the coordinates of a point. Leading zero can be removed (e.g. 3BC, 0, and 1287).YstringOrdinate of a point coordinates. The hexadecimal value in text of the ordinate of the coordinates of a point. Leading zero can be removed (e.g. 3BC, 0, and 1287).SignaturePointarray[object]Coordinates of a point where the pen changes direction or lift. Contain the Coordinates of a point of the written signature where the pen changes direction or lift where (X and Y). When the signer lifts the pen, both X and Y have the value FFFF.Show childrenHide childrenXstringThe hexadecimal value of the coordinates of a point on the abscissa.YstringThe hexadecimal value of the coordinates of a point on the ordinate.ProtectedSignaturestringNumeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a cardholder on the merchant payment receipt. The format before encryption is the encoded data structure CapturedSignature. The data structure before encryption includes the start and end tags for an XML encoding, the identifier and length bytes for an ASN.1 encoding, and the complete member ProtectedSignature for a JSON encoding.CustomerLanguagestringThe language of the customer that was used on the terminal screen or in text printed by the terminal. Format: two-characterISO 639:2023format.OnlineFlagbooleanIndicate that the payment transaction processing has required the approval of a host. Allows the Sale System to know if the payment was online or offline.AuthenticationMethodarray[string]Method for customer authentication. Allows the Sale System informed about customer authentication for the payment transaction.
Possible values:BypassManualVerificationMerchantAuthenticationOfflinePINOnlinePINPaperSignatureSecureCertificateSecureNoCertificateSecuredChannelSignatureCaptureUnknownMethodValidityDatestringEnd of the validity period for the reservation, for the first reservation, and the reservation updates as well.PaymentAcquirerDataobjectData related to the response from the payment Acquirer.Show childrenHide childrenAcquirerIDintegerIdentification of the Acquirer.
Identification of the Acquirer when the POI System is multi-acquirer.MerchantIDstringIdentification of the Merchant for the Acquirer.AcquirerPOIIDstringIdentification of the POI for the payment Acquirer.AcquirerTransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.ApprovalCodestringCode assigned to a transaction approval by the Acquirer.
If available.HostReconciliationIDstringIdentifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to the Acquirer reconciliation (or batch).LoyaltyResultarray[object]Data related to the result of a processed loyalty transaction.
Loyalty cards used with the payment transaction.Show childrenHide childrenLoyaltyAccountobjectThis data structure conveys the identification of the account and the associated loyalty brand.
Data related to a loyalty account processed in the transaction.Show childrenHide childrenLoyaltyAccountIDobjectIdentification of a Loyalty account.
In the Payment Request message, it allows to identify the loyalty account by the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the Cashier on a scanner device).Show childrenHide childrenEntryModearray[string]Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.
Possible values:ContactlessFileICCKeyedMagStripeManualMobileRFIDScannedSynchronousICCTappedIdentificationTypestringType of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.
Possible values:AccountNumberBarCodeISOTrack2PANPhoneNumberIdentificationSupportstringSupport of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:HybridCardLinkedCardLoyaltyCardNoCardLoyaltyIDstringLoyalty account identification conforming to the IdentificationType.LoyaltyBrandstringIdentification of a Loyalty brand.
If a card is analysed.CurrentBalancenumberMaximum:99999999.999999Balance of an account.
If known (provided by the card or an external host).LoyaltyAcquirerDataobjectData related to the loyalty Acquirer during a loyalty transaction.
If content not empty.Show childrenHide childrenLoyaltyAcquirerIDstringIdentification of the loyalty Acquirer.ApprovalCodestringCode assigned to a transaction approval by the Acquirer. Could be an identifier of the approved transaction for the Acquirer. This data element is conditional for the Loyalty Acquirers. Used in the PaymentRequest request for a referral.LoyaltyTransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.HostReconciliationIDstringIdentifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to the Acquirer reconciliation (or batch).PaymentReceiptarray[object]Customer or Merchant payment receipt. If the payment receipts are printed by the Sale system and the POI or the Sale does not implement the Print exchange (Basic profile).Show childrenHide childrenDocumentQualifierstringQualification of the document to print to the Cashier or the Customer.
SaleReceipt or CashierReceipt.
Possible values:CashierReceiptCustomerReceiptDocumentJournalSaleReceiptVoucherIntegratedPrintFlagbooleanType of the print integrated to other prints.RequiredSignatureFlagbooleanIndicate that the cardholder payment receipt requires a physical signature by the Customer.OutputContentobjectContent to display or print.
This is a sequence of elements if they have different formats.Show childrenHide childrenOutputFormatstringFormat of the content to display or print. Display or print device function.
Possible values:BarCodeMessageRefTextXHTMLPredefinedContentobjectReference of a predefined message to display or print.
It conveys information related to the predefined message.Show childrenHide childrenReferenceIDstringIdentification of a predefined message to display or print.LanguagestringIdentification of a language.OutputTextarray[object]Content of text message to display or print.
Mandatory, ifOutputFormatis Text, not allowed otherwise. One instance ofOutputTextper shared format.Show childrenHide childrenTextstringContent of text message to display, print or play.CharacterSetintegerCharacter height of the text string to display or print. Absence of this data element means the characters have normal height.StartRowintegerMinimum:1Maximum:500Row where the text string has to be displayed or printed.StartColumnintegerMinimum:1Maximum:500Column where the text string has to be displayed or printed.CharacterWidthstringCharacter width of the text string to display or print. Absence of this data element means the characters have normal width.
Possible values:DoubleWidthSingleWidthCharacterHeightstringCharacter height of the text string to display or print. Absence of this data element means the characters have normal height.
Possible values:DoubleHeightHalfHeightSingleHeightCharacterStylestringTypographic style of the sequence of characters to display or print. Absence of this data element means the characters have normal style.
Possible values:BoldItalicNormalUnderlineAlignmentstringAlignment of the text string on the display line or print line. Absence of this data element means the characters have normal alignment.
Possible values:CentredJustifiedLeftRightEndOfLineFlagbooleanIndicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over return characters after the formatted text.OutputXHTMLstringXHTML document body containing the message to display or print.
Mandatory ifOutputFormatis XHTML, not allowed otherwise.OutputBarcodeobjectBarcode content to display or print.
Mandatory ifOutputFormatis Barcode, not allowed otherwise.Show childrenHide childrenBarcodeValuestringValue with a Barcode coding. The barcode value to display or print.

#### 200
- Failure
- Partial
- Success
- Aborted
- Busy
- Cancel
- DeviceOut
- InProgress
- InsertedCard
- InvalidCard
- LoggedOut
- MessageFormat
- NotAllowed
- NotFound
- PaymentRestriction
- Refusal
- UnavailableDevice
- UnavailableService
- UnreachableHost
- WrongPIN
- Customer
- Transaction
- Both
- Closed
- Open
- CashAdvance
- CashDeposit
- Completion
- FirstReservation
- Instalment
- IssuerInstalment
- Normal
- OneTimeReservation
- PaidOut
- Recurring
- Refund
- UpdateReservation
- Card
- Cash
- Check
- Mobile
- StoredValue
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- Mobile
- RFID
- Scanned
- SynchronousICC
- Tapped
- AAMVA
- ISO
- Customer
- Transaction
- AAMVA
- ISO
- Company
- Personal
- GiftCard
- Other
- PhoneCard
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- Mobile
- RFID
- Scanned
- SynchronousICC
- Tapped
- AccountNumber
- BarCode
- ISOTrack2
- PAN
- PhoneNumber
- The authorised amount to be paid.
- The amount of the rebates.
- The amount of financial fees.
- The cash back part of the requested amount for a payment with cash back.
- The tip part of the requested amount for a payment with tip.
- DeferredInstalments
- EqualInstalments
- InequalInstalments
- Annual
- Daily
- Monthly
- Weekly
- The size of the pad area where the signature is written, given with the maximum abscissa and ordinate values.
- The sequence of coordinates where the pen changes direction or lift.
- Bypass
- ManualVerification
- MerchantAuthentication
- OfflinePIN
- OnlinePIN
- PaperSignature
- SecureCertificate
- SecureNoCertificate
- SecuredChannel
- SignatureCapture
- UnknownMethod
- Contactless
- File
- ICC
- Keyed
- MagStripe
- Manual
- Mobile
- RFID
- Scanned
- SynchronousICC
- Tapped
- AccountNumber
- BarCode
- ISOTrack2
- PAN
- PhoneNumber
- HybridCard
- LinkedCard
- LoyaltyCard
- NoCard
- CashierReceipt
- CustomerReceipt
- Document
- Journal
- SaleReceipt
- Voucher
- BarCode
- MessageRef
- Text
- XHTML
- DoubleWidth
- SingleWidth
- DoubleHeight
- HalfHeight
- SingleHeight
- Bold
- Italic
- Normal
- Underline
- Centred
- Justified
- Left
- Right