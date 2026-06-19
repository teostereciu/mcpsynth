# terminal-api/1/post/print

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/print*

---

# Print Request
Content of the Print Request message.
It conveys the complete data to print and how to process the print.
Information to print and how to process it.
Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or POI Terminal, to send information to a physical printer or to use the paper type accordingly.
Possible values:
- CashierReceipt
- CustomerReceipt
- Document
- Journal
- SaleReceipt
- Voucher
Message response awaited by the initiator of the Request. Allows various types and synchronisation of requests for Print or Sound.
Possible values:
- Immediate
- NotRequired
- PrintEnd
- SoundEnd
Type of the print integrated in other prints. Allows a separated printing (paper cut if available), or integration with the sale receipt or other print. If the printing is integrated, the response is always immediate, even if theResponseModeis set toPrintEnd.
Indicates that the cardholder payment receipt requires a physical signature by the Customer.
Content to display or print.
This is a sequence of elements if they have different formats.
Format of the content to display or print. Display or print device function.
Possible values:
- BarCode
- MessageRef
- Text
- XHTML
Reference of a predefined message to display or print.
It conveys information related to the predefined message.
Identification of a predefined message to display or print.
Identification of a language.
Content of text message to display or print.
Mandatory, ifOutputFormatis Text, not allowed otherwise. One instance ofOutputTextper shared format.
Content of text message to display, print or play.
Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Row where the text string has to be displayed or printed.
Column where the text string has to be displayed or printed.
Character width of the text string to display or print. Absence of this data element means the characters have normal width.
Possible values:
- DoubleWidth
- SingleWidth
Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Possible values:
- DoubleHeight
- HalfHeight
- SingleHeight
Typographic style of the sequence of characters to display or print. Absence of this data element means the characters have normal style.
Possible values:
- Bold
- Italic
- Normal
- Underline
Alignment of the text string on the display line or print line. Absence of this data element means the characters have normal alignment.
Possible values:
- Centred
- Justified
- Left
- Right
Indicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over return characters after the formatted text.
XHTML document body containing the message to display or print.
Mandatory ifOutputFormatis XHTML, not allowed otherwise.
Barcode content to display or print.
Mandatory ifOutputFormatis Barcode, not allowed otherwise.
Value with a Barcode coding. The barcode value to display or print.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys the result of the print, parallel to the message request, except if response not required and absent.
Content of the Print Response message.Show moreShow lessDocumentQualifierstringQualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or POI Terminal, to send information to a physical printer or to use the paper type accordingly.
Possible values:CashierReceiptCustomerReceiptDocumentJournalSaleReceiptVoucherResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.

#### 200
- CashierReceipt
- CustomerReceipt
- Document
- Journal
- SaleReceipt
- Voucher
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