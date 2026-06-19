# terminal-api/1/post/abort

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/abort*

---

# Abort Request
Body of the Abort Request message.
It conveys Information requested for identification of the message request carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale System (DisplayOutput).
Identification of a previous POI transaction.
To abort a transaction in progress or to request the status of a transaction from which no response has been received. It identifies the message header of the message request to abort or request the status.
Category of message.
CardAcquisition, Display, Input, Loyalty, Payment, Print, CardReaderInit, CardReaderPowerOff.
Possible values:
- Abort
- Admin
- BalanceInquiry
- Batch
- CardAcquisition
- CardReaderInit
- CardReaderPowerOff
- Diagnosis
- Display
- EnableService
- Event
- GetTotals
- Input
- InputUpdate
- Login
- Logout
- Loyalty
- None
- PIN
- Payment
- Print
- Reconciliation
- Reversal
- Sound
- StoredValue
- TransactionStatus
- Transmit
Identification of a message pair, which processes a transaction.
Identification of a device message pair.
Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.
default MessageHeader.SaleID.
Identification of a POI System or a POI Terminal for the Sale to POI protocol.
DefaultMessageHeader.POIID.
Reason of aborting a transaction.
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
- 200A successful `AbortRequest` returns a response with a **200 OK** HTTP status code and no body.

#### 200