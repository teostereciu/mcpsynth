# terminal-api/1/post/cardacquisition

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/cardacquisition*

---

# CardAcquisition Request
It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair.
Content of the Card Acquisition Request message.
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
Data related to the payment and loyalty card acquisition.
Card payment brands allowed by the Sale System for the payment transaction.
Loyalty brands or programs allowed by the Sale System for the loyalty transaction.
Type of Loyalty processing requested by the Sale System. An way to specify what the POI has to handle concerning the loyalty.
Possible values:
- Allowed
- Forbidden
- Processed
- Proposed
- Required
The language used on the terminal screen or in text printed by the terminal.
Typical use case is setting the language on unattended terminals. Format: two-characterISO 639:2023format.
Payment instrument entry mode requested by the Sale System. Avoid retry on an out of order card reading device, when the sale system knows that some card entry modes on the POI do not work.
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
Indicates if the Customer realises the selection of the card application.
Amount of a transaction. In the Card Acquisition Request message, it allows the processing of a contactless card.
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
Cash back has been requested with the payment transaction. Allows choice of the Customer language when the POI displays messages or print text to Merchant interface.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered by the Customer.
Content of the Card Acquisition Response message.Show moreShow lessResponseobjectResult of a message request processing.
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
If Result is Success.PaymentBrandarray[string]Type of payment card.
Brands available for payment by the card and not chosen by the Customer.PaymentInstrumentDataobjectData related to the instrument of payment for the transaction.
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
Possible values:AccountNumberBarCodeISOTrack2PANPhoneNumberStoredValueIDstringStored value account identification. The identification of the stored value account conforming to the IdentificationType.LoyaltyAccountarray[object]Data related to the loyalty System.Show childrenHide childrenLoyaltyAccountIDobjectIdentification of a Loyalty account.
In the Payment Request message, it allows to identify the loyalty account by the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the Cashier on a scanner device).Show childrenHide childrenEntryModearray[string]Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.
Possible values:ContactlessFileICCKeyedMagStripeManualMobileRFIDScannedSynchronousICCTappedIdentificationTypestringType of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.
Possible values:AccountNumberBarCodeISOTrack2PANPhoneNumberIdentificationSupportstringSupport of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:HybridCardLinkedCardLoyaltyCardNoCardLoyaltyIDstringLoyalty account identification conforming to the IdentificationType.LoyaltyBrandstringIdentification of a Loyalty brand.
If a card is analysed.

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