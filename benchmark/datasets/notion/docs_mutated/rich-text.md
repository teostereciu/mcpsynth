# rich-text

*Source: https://developers.notion.com/reference/rich-text*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​The annotation object

## ​Rich text type objects

### ​Equation

#### ​Example rich textequationobject

### ​Mention

#### ​Database mention type object

#### ​Date mention type object

#### ​Link Preview mention type object

#### ​Page mention type object

#### ​Template mention type object

#### ​User mention type object

### ​Text

#### ​Example rich texttextobject without link

#### ​Example richtexttext object with link

```
{"type":"text","text": {"content":"Some words ","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Some words ","href":null}
```

```
{"type":"equation","equation": {"expression":"E = mc^2"},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"E = mc^2","href":null}
```

```
{"type":"mention","mention": {"type":"database","database": {"id":"a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Database with test things","href":"https://www.notion.so/a1d8501e1ac143e9a6bdea9fe6c8822b"}
```

```
{"type":"mention","mention": {"type":"date","date": {"start":"2022-12-16","end":null}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"2022-12-16","href":null}
```

```
{"type":"mention","mention": {"type":"link_preview","link_preview": {"url":"https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD"}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD","href":"https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD"}
```

```
{"type":"mention","mention": {"type":"page","page": {"id":"3c612f56-fdd0-4a30-a4d6-bda7d7426309"}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"This is a test page","href":"https://www.notion.so/3c612f56fdd04a30a4d6bda7d7426309"}
```

```
{"type":"mention","mention": {"type":"template_mention","template_mention": {"type":"template_mention_date","template_mention_date":"today"}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"@Today","href":null}
```

```
{"type":"mention","mention": {"type":"user","user": {"object":"user","id":"b2e19928-b427-4aad-9a9d-fde65479b1d9"}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"@Anonymous","href":null}
```

```
{"type":"text","text": {"content":"This is an ","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"This is an ","href":null}
```

```
{"type":"text","text": {"content":"inline link","link": {"url":"https://developers.notion.com/"}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"inline link","href":"https://developers.notion.com/"}
```
- Status
- Community
- Blog
- Introduction
- Integration capabilities
- Webhooks
- Request limits
- Status codes
- Versioning
- BlockOverviewRich text
- Page
- Database
- Data source
- View
- Comment
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Overview
- Rich text
- Authentication
- Blocks
- Pages
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- File uploads
- The annotation object
- Rich text type objects
- Equation
- Example rich text equation object
- Mention
- Database mention type object
- Date mention type object
- Link Preview mention type object
- Page mention type object
- Template mention type object
- User mention type object
- Text
- Example rich text text object without link
- Example rich text text object with link

[TABLE]
Field | Type | Description | Example value
type | string(enum) | The type of this rich text object. Possible type values are:"text","mention","equation". | "text"
text|mention|equation | object | An object containing type-specific configuration.Refer to the rich text type objects section below for details on type-specific values. | Refer to the rich text type objects section below for examples.
annotations | object | The information used to style the rich text object. Refer to the annotation object section below for details. | Refer to the annotation object section below for examples.
plain_text | string | The plain text without annotations. | "Some words "
href | string(optional) | The URL of any link or Notion mention in this text, if any. | "https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
bold | boolean | Whether the text isbolded. | true
italic | boolean | Whether the text isitalicized. | true
strikethrough | boolean | Whether the text is struck through. | false
underline | boolean | Whether the text is underlined. | false
code | boolean | Whether the text iscode style. | true
color | string(enum) | Color of the text. Possible values include:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background”-"yellow"-"yellow_background" | "green"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
expression | string | The LaTeX string representing the inline equation. | "\frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}}"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
type | string(enum) | The type of the inline mention. Possible values include:-"database"-"date"-"link_preview"-"page"-"template_mention"-"user" | "user"
database|date|link_preview|page|template_mention|user | object | An object containing type-specific configuration. Refer to the mention type object sections below for details. | Refer to the mention type object sections below for example values.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
template_mention_date | string(enum) | The type of the date mention. Possible values include:"today"and"now". | "today"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
template_mention_user | string(enum) | The type of the user mention. The only possible value is"me". | "me"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
content | string | The actual text content of the text. | "Some words "
link | object(optional) | An object with information about any inline link in this text, if included.If the text contains an inline link, then the object key isurland the value is the URL’s string web address.If the text doesn’t have any inline links, then the value isnull. | { "url": "https://developers.notion.com/" }
[/TABLE]