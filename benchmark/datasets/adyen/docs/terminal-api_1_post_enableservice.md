# terminal-api/1/post/enableservice

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/enableservice*

---

# EnableService Request
It conveys the services that will be enabled for the POI Terminal without the request of the Sale System, and a possible invitation for the Customer to start the services.
Content of the Enable Service Request message.
Action to realise on a transaction. In anEnableServicerequest message:
- Starts a transaction by a swipe-ahead mechanism, with the services which are enabled.
- Aborts a swipe-ahead transaction or started by aCardAcquisition, and not followed by a service request from the Sale System to complete the transaction.
Possible values:
- AbortTransaction
- StartTransaction
Services which are enabled before the start-up of a transaction.
Mandatory ifTransactionActionisStartTransaction, absent if not.
Possible values:
- CardAcquisition
- Loyalty
- Payment
Information to display and how to process it.
Contains a complete display operation for a Display or an Input Device type. For the Input Devices, Diagnosis andEnableService,ResponseRequiredFlag, andMinimumDisplayTimeshall be absent.
Indicates if the message response is required.
Number of seconds the message has to be displayed.
Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print, or store), or input (keyboard) for the Cashier or the Customer.
Possible values:
- CashierDisplay
- CashierInput
- CustomerDisplay
- CustomerInput
Qualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer. Allows the manager of the device, Sale or POI Terminal, to send the information to a particular physical device or to present the information accordingly.
Possible values:
- CustomerAssistance
- Display
- Document
- Error
- Input
- POIReplication
- Receipt
- Sound
- Status
- Voucher
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
An entry of the menu to present to the Cashier. It conveys the message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entryof the menu.
Characteristics related to the selection of a menu entry.
Possible values:
- NonSelectable
- NonSelectableSubMenu
- Selectable
- SubMenu
Selection of a menu entry to be displayed. In Input request message, it allows selection of one or several menu entries before any user action.
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
Content of text message to display or print. It conveys Information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole Text content.
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
Vendor-specific signature of the text message to display or print.
If protection has to be provided to the vendor on the text to display or print.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys the result of the Enable Service processing.
Content of the Enable Service Response message.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.

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