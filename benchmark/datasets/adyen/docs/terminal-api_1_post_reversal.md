# terminal-api/1/post/reversal

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/reversal*

---

# Reversal Request
It conveys Information related to the reversal of a previous payment or a loyalty transaction.
Content of the Reversal Request message.
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
Amount of the payment or loyalty to reverse.
ReversedAmount is implicitly equal to the AuthorizedAmount if absent.
Reason of the payment or loyalty reversal.
Possible values:
- CustCancel
- Malfunction
- MerchantCancel
- Unable2Compl
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys Information related to the reversal processed by the POI System.
Content of the Reversal Response message.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.POIDataobjectData related to the POI System.
In the Message Response, identification of the POI transaction.Show childrenHide childrenPOITransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.POIReconciliationIDintegerIdentification of the reconciliation period between Sale and POI.
If Result is Success.OriginalPOITransactionobjectIdentification of a previous POI transaction.
In the Payment Request message, it allows using the card of a previous CardAcquisition or Payment request.Show childrenHide childrenSaleIDstringIdentification of a Sale System for the NEXO SaletoPOI protocol.POIIDstringIdentification of a payment terminal for the NEXO SaletoPOI protocol.
If original transaction is coming from another POI.POITransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.ReuseCardDataFlagbooleanIndicates if the card data has to be retrieved from a previous transaction.ApprovalCodestringCode assigned to a transaction approval by the Acquirer.
If referral.AcquirerIDintegerIdentification of the Acquirer.
Restrict to the Acquirer if present.AmountValuenumberMaximum:99999999.999999Value of an amount.HostTransactionIDobjectIdentification of a transaction for the Sale System or the POI System.Show childrenHide childrenTransactionIDstringUnique identification of a transaction to identify the transaction on
the Sale System (e.g. ticket number), or the POI System.TimeStampstringDate and time of a transaction for the Sale System, the POI System or the Acquirer.
Ensures the uniqueness of a transaction and indicates the time when the event
occurs in the EventNotification message.ReversedAmountnumberMaximum:99999999.999999Amount of the payment or loyalty to reverse.
Copy.PaymentReceiptarray[object]Show childrenHide childrenDocumentQualifierstringQualification of the document to print to the Cashier or the Customer.
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