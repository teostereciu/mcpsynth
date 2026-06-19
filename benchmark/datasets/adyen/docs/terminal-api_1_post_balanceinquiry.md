# terminal-api/1/post/balanceinquiry

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/balanceinquiry*

---

# BalanceInquiry Request
It conveys Information related to the account for which a Balance Inquiry is requested.
Content of the Balance Inquiry Request message.
Data related to the account pointed by the payment card.
Type of cardholder account used for the transaction. Allows a cardholder to select the type of account used for the transaction.
Possible values:
- CardTotals
- Checking
- CreditCard
- Default
- EpurseCard
- Investment
- Savings
- Universal
Identification of a transaction for the Sale System or the POI System.
Unique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.
Date and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.
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
Data related to a requested Loyalty program or account.
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
- 200Content of the Balance Inquiry Response message.
It conveys the balance and the identification of the associated payment, loyalty or stored value account.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.PaymentAccountStatusobjectData related to the result of a Balance Inquiry request.
If BalanceInquiryRequest. PaymentAccount present.Show childrenHide childrenPaymentInstrumentDataobjectData related to the instrument of payment for the transaction.
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
Possible values:AccountNumberBarCodeISOTrack2PANPhoneNumberStoredValueIDstringStored value account identification. The identification of the stored value account conforming to the IdentificationType.CurrentBalancenumberMaximum:99999999.999999Balance of an account after processing of the transaction.CurrencystringCurrency of a monetary amount.PaymentAcquirerDataobjectData related to the response from the payment Acquirer.Show childrenHide childrenAcquirerIDintegerIdentification of the Acquirer.
Identification of the Acquirer when the POI System is multi-acquirer.MerchantIDstringIdentification of the Merchant for the Acquirer.AcquirerPOIIDstringIdentification of the POI for the payment Acquirer.AcquirerTransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.ApprovalCodestringCode assigned to a transaction approval by the Acquirer.
If available.HostReconciliationIDstringIdentifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to the Acquirer reconciliation (or batch).PaymentReceiptarray[object]Show childrenHide childrenDocumentQualifierstringQualification of the document to print to the Cashier or the Customer.
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