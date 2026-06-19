# block

*Source: https://developers.notion.com/reference/block*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Keys

#### ​Block types that support child blocks

## ​Block type objects

### ​Audio

#### ​Supported audio types

#### ​Supported file upload types

### ​Bookmark

### ​Breadcrumb

### ​Bulleted list item

### ​Callout

### ​Child database

### ​Child page

### ​Code

### ​Column list and column

#### ​Retrieve the content in a column list

### ​Divider

### ​Embed

### ​Equation

### ​File

### ​Headings

### ​Image

#### ​Supported external image types

### ​Link Preview

### ​Meeting notes

### ​Mention

### ​Numbered list item

### ​Paragraph

### ​PDF

### ​Quote

### ​Synced block

#### ​Original synced block

#### ​Duplicate synced block

### ​Table

#### ​Table rows

### ​Table of contents

### ​Template

### ​To do

### ​Toggle blocks

### ​Transcription

### ​Unsupported

### ​Video

#### ​Supported video types

```
{"object":"block","id":"c02fc1d3-db8b-45c5-a222-27595b15aea7","parent": {"type":"page_id","page_id":"59833787-2cf9-4fdf-8782-e53db20768a5"},"created_time":"2022-03-01T19:05:00.000Z","last_edited_time":"2022-07-06T19:41:00.000Z","created_by": {"object":"user","id":"ee5f0f84-409a-440f-983a-a5315961c6e4"},"last_edited_by": {"object":"user","id":"ee5f0f84-409a-440f-983a-a5315961c6e4"},"has_children":false,"in_trash":false,"type":"heading_2","heading_2": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"green"},"plain_text":"Lacinato kale","href":null}],"color":"default","is_toggleable":false}}
```

```
{"type":"audio",//...other keys excluded"audio": {"type":"external","external": {"url":"https://companywebsite.com/files/sample.mp3"}}}
```

```
{//...other keys excluded"type":"bookmark",//...other keys excluded"bookmark": {"caption": [],"url":"https://companywebsite.com"}}
```

```
{//...other keys excluded"type":"breadcrumb",//...other keys excluded"breadcrumb": {}}
```

```
{//...other keys excluded"type":"bulleted_list_item",//...other keys excluded"bulleted_list_item": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null}// ..other keys excluded}],"color":"default","children":[{"type":"paragraph"// ..other keys excluded}]}}
```

```
{//...other keys excluded"type":"callout",// ..other keys excluded"callout": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null}// ..other keys excluded}],"icon": {"emoji":"⭐"},"color":"default"}}
```

```
{//...other keys excluded"type":"child_database",//...other keys excluded"child_database": {"title":"My database"}}
```

```
{//...other keys excluded"type":"child_page",//...other keys excluded"child_page": {"title":"Lacinato kale"}}
```

```
{// ... other keys excluded"type":"code",// ... other keys excluded"code": {"caption": [],"rich_text": [{"type":"text","text": {"content":"const a = 3"}}],"language":"javascript"}}
```

```
{// ... other keys excluded"type":"column_list",// ... other keys excluded"column_list": {}}
```

```
{// ... other keys excluded"type":"column",// ... other keys excluded"column": {"width_ratio":0.25}}
```

```
{//...other keys excluded"type":"divider",//...other keys excluded"divider": {}}
```

```
{//...other keys excluded"type":"embed",//...other keys excluded"embed": {"url":"https://companywebsite.com"}}
```

```
{"children": [{"embed": {"url":"https://player.vimeo.com/video/226053498?h=a1599a8ee9"}}]}
```

```
{//...other keys excluded"type":"equation",//...other keys excluded"equation": {"expression":"e=mc^2"}}
```

```
{// ... other keys excluded"type":"file",// ... other keys excluded"file": {"caption": [],"type":"external","external": {"url":"https://companywebsite.com/files/doc.txt"},"name":"doc.txt"}}
```

```
{//...other keys excluded"type":"heading_1",//...other keys excluded"heading_1": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null}}],"color":"default","is_toggleable":false}}
```

```
{//...other keys excluded"type":"heading_2",//...other keys excluded"heading_2": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null}}],"color":"default","is_toggleable":false}}
```

```
{//...other keys excluded"type":"heading_3",//...other keys excluded"heading_3": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null}}],"color":"default","is_toggleable":false}}
```

```
{// ... other keys excluded"type":"image",// ... other keys excluded"image": {"type":"external","external": {"url":"https://website.domain/images/image.png"}}}
```

```
{//...other keys excluded"type":"link_preview",//...other keys excluded"link_preview": {"url":"https://github.com/example/example-repo/pull/1234"}}
```

```
{"object":"block","id":"d7b3c8f4-9e6e-4c1a-b5b8-2c0f4a0c5b8e","type":"meeting_notes",//...other keys excluded"meeting_notes": {"title": [{"type":"text","text": {"content":"Team Sync","link":null},"plain_text":"Team Sync","href":null}],"status":"notes_ready","children": {"summary_block_id":"a1b2c3d4-5678-9abc-def0-1234567890ab","notes_block_id":"b2c3d4e5-6789-abcd-ef01-234567890abc","transcript_block_id":"c3d4e5f6-789a-bcde-f012-34567890abcd"},"calendar_event": {"attendees": ["ee5f0f84-409a-440f-983a-a5315961c6e4"],"start_time":"2026-02-24T10:00:00.000Z","end_time":"2026-02-24T10:45:00.000Z"},"recording": {"start_time":"2026-02-24T10:00:00.000Z","end_time":"2026-02-24T10:45:00.000Z"}}}
```

```
{//...other keys excluded"type":"page","page": {"id":"3c612f56-fdd0-4a30-a4d6-bda7d7426309"}}
```

```
{//...other keys excluded"type":"numbered_list_item","numbered_list_item": {"rich_text": [{"type":"text","text": {"content":"Finish reading the docs","link":null}}],"color":"default"}}
```

```
{//...other keys excluded"type":"paragraph",//...other keys excluded"paragraph": {"rich_text": [{"type":"text","text": {"content":"Lacinato kale","link":null}}],"color":"default"}
```

```
{//...other keys excluded"type":"paragraph","paragraph":{"rich_text": [{"type":"mention","mention": {"type":"date","date": {"start":"2023-03-01","end":null,"time_zone":null}},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"2023-03-01","href":null},{"type":"text","text": {"content":" ","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":" ","href":null}],"color":"default"}}
```

```
{//...other keys excluded"type":"pdf",//...other keys excluded"pdf": {"type":"external","external": {"url":"https://website.domain/files/doc.pdf"}}}
```

```
{//...other keys excluded"type":"quote",//...other keys excluded"quote": {"rich_text": [{"type":"text","text": {"content":"To be or not to be...","link":null},//...other keys excluded}],//...other keys excluded"color":"default"}}
```

```
{//...other keys excluded"type":"synced_block","synced_block": {"synced_from":null,"children": [{"callout": {"rich_text": [{"type":"text","text": {"content":"Callout in synced block"}}]}}]}}
```

```
{//...other keys excluded"type":"table","table": {"table_width":2,"has_column_header":false,"has_row_header":false}}
```

```
{//...other keys excluded"type":"table_row","table_row": {"cells": [[{"type":"text","text": {"content":"column 1 content","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"column 1 content","href":null}],[{"type":"text","text": {"content":"column 2 content","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"column 2 content","href":null}],[{"type":"text","text": {"content":"column 3 content","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"column 3 content","href":null}]]}}
```

```
{//...other keys excluded"type":"table_of_contents","table_of_contents": {"color":"default"}}
```

```
{//...other keys excluded"template": {"rich_text": [{"type":"text","text": {"content":"Add a new to-do","link":null},"annotations": {//...other keys excluded},"plain_text":"Add a new to-do","href":null}]}}
```

```
{//...other keys excluded"type":"to_do","to_do": {"rich_text": [{"type":"text","text": {"content":"Finish Q3 goals","link":null}}],"checked":false,"color":"default","children":[{"type":"paragraph"// ..other keys excluded}]}}
```

```
{//...other keys excluded"type":"toggle","toggle": {"rich_text": [{"type":"text","text": {"content":"Additional project details","link":null}//...other keys excluded}],"color":"default","children":[{"type":"paragraph"// ..other keys excluded}]}}
```

```
{"object":"block","id":"7af38973-3787-41b3-bd75-0ed3a1edfac9","type":"unsupported",//...other keys excluded"unsupported": {"block_type":"form"}}
```

```
{"type":"video",//...other keys excluded"video": {"type":"external","external": {"url":"https://companywebsite.com/files/video.mp4"}}}
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
- Keys
- Block types that support child blocks
- Block type objects
- Audio
- Supported audio types
- Supported file upload types
- Bookmark
- Breadcrumb
- Bulleted list item
- Callout
- Child database
- Child page
- Code
- Column list and column
- Retrieve the content in a column list
- Divider
- Embed
- Equation
- Headings
- Image
- Supported external image types
- Link Preview
- Meeting notes
- Mention
- Numbered list item
- Paragraph
- PDF
- Quote
- Synced block
- Original synced block
- Duplicate synced block
- Table
- Table rows
- Table of contents
- Template
- To do
- Toggle blocks
- Transcription
- Unsupported
- Video
- Supported video types
- Column
- Heading 1, when theis_toggleableproperty istrue
- Heading 2, when theis_toggleableproperty istrue
- Heading 3, when theis_toggleableproperty istrue
- Meeting notes(renamed fromTranscriptionin2026-03-11)
- Toggle
- .mp3
- .wav
- .ogg
- .oga
- .m4a
- .bmp
- .gif
- .heic
- .jpeg
- .jpg
- .png
- .svg
- .tif
- .tiff
- .amv
- .asf
- .avi
- .f4v
- .flv
- .gifv
- .mkv
- .mov
- .mpg
- .mpeg
- .mpv
- .mp4
- .m4v
- .qt
- .wmv
- YouTube video links that includeembedorwatch. E.g.https://www.youtube.com/watch?v=[id],https://www.youtube.com/embed/[id]

[TABLE]
Field | Type | Description | Example value
object* | string | Always"block". | "block"
id* | string(UUIDv4) | Identifier for the block. | "7af38973-3787-41b3-bd75-0ed3a1edfac9"
parent | object | Information about the block’s parent. SeeParent object. | { "type": "block_id", "block_id": "7d50a184-5bbe-4d90-8f29-6bec57ed817b" }
type | string(enum) | Type of block. Possible values are:-"bookmark"-"breadcrumb"-"bulleted_list_item"-"callout"-"child_database"-"child_page"-"column"-"column_list"-"divider"-"embed"-"equation"-"file"-"heading_1"-"heading_2"-"heading_3"-"image"-"link_preview"-"numbered_list_item"-"paragraph"-"pdf"-"quote"-"synced_block"-"table"-"table_of_contents"-"table_row"-"template"-"to_do"-"toggle"-"transcription"-"unsupported"-"video" | "paragraph"
created_time | string(ISO 8601 date time) | Date and time when this block was created. Formatted as anISO 8601 date timestring. | "2020-03-17T19:10:04.968Z"
created_by | Partial User | User who created the block. | {"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}
last_edited_time | string(ISO 8601 date time) | Date and time when this block was last updated. Formatted as anISO 8601 date timestring. | "2020-03-17T19:10:04.968Z"
last_edited_by | Partial User | User who last edited the block. | {"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}
archived | boolean | Deprecated.Usein_trashinstead. This is an alias forin_trashand always returns the same value. | false
in_trash | boolean | Whether the block has been trashed. Use this field to check if a block is in the trash, and as a body parameter inUpdate a blockto trash or restore a block. | false
has_children | boolean | Whether or not the block has children blocks nested within it. | true
{type} | block type object | An object containing type-specific block information. | Refer to theblock type object sectionfor examples of each block type.
[/TABLE]

[TABLE]
Field | Type | Description
caption | array ofrich text objectstext | The caption for the bookmark.
url | string | The link for the bookmark.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text in thebulleted_list_itemblock.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
children | arrayofblock objects | The nested child blocks (if any) of thebulleted_list_itemblock.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text in thecalloutblock.
icon | object | Anemojiorfileobject that represents the callout’s icon. If the callout does not have an icon.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
[/TABLE]

[TABLE]
Field | Type | Description
title | string | The plain text title of the database.
[/TABLE]

[TABLE]
Field | Type | Description
title | string | The plain texttitleof the page.
[/TABLE]

[TABLE]
Field | Type | Description
caption | arrayofRich text objecttext objects | The rich text in the caption of the code block.
rich_text | arrayofRich text objecttext objects | The rich text in the code block.
language | -"abap"-"arduino"-"bash"-"basic"-"c"-"clojure"-"coffeescript"-"c++"-"c#"-"css"-"dart"-"diff"-"docker"-"elixir"-"elm"-"erlang"-"flow"-"fortran"-"f#"-"gherkin"-"glsl"-"go"-"graphql"-"groovy"-"haskell"-"html"-"java"-"javascript"-"json"-"julia"-"kotlin"-"latex"-"less"-"lisp"-"livescript"-"lua"-"makefile"-"markdown"-"markup"-"matlab"-"mermaid"-"nix"-"objective-c"-"ocaml"-"pascal"-"perl"-"php"-"plain text"-"powershell"-"prolog"-"protobuf"-"python"-"r"-"reason"-"ruby"-"rust"-"sass"-"scala"-"scheme"-"scss"-"shell"-"sql"-"swift"-"typescript"-"vb.net"-"verilog"-"vhdl"-"visual basic"-"webassembly"-"xml"-"yaml"-"java/c/c++/c#" | The language of the code contained in the code block.
[/TABLE]

[TABLE]
Field | Type | Description
url | string | The link to the website that the embed block displays.
[/TABLE]

[TABLE]
Field | Type | Description
expression | string | A KaTeX compatible string.
[/TABLE]

[TABLE]
Field | Type | Description
caption | arrayofrich text objects | The caption of the file block.
type | One of:-"file"-"external"-"file_upload" | Type of file. This enum value indicates which of the following three objects are populated.
file | Notion-hosted file object | A file object that details information about the file contained in the block: a temporary downloadurlandexpiry_time. After theexpiry_time, fetch the block again from the API to get a newurl.Only valid as a parameter if copied verbatim from thefilefield of a recent block API response from Notion. To attach a file, provide atypeoffile_uploadinstead.
external | External file object | An object with aurlproperty, identifying a publicly accessible URL.
file_upload | File upload object | An object with theidof aFileUploadto attach to the block. After attaching, the API response responds with a type offile, notfile_upload, so your integration can access a downloadurl.
name | string | The name of the file, as shown in the Notion UI. Note that the UI may auto-append.pdfor other extensions.When attaching afile_upload, thenameparameter is not required.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text of the heading.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
is_toggleable | boolean | Whether or not the heading block is a toggle heading or not. Iftrue, then the heading block toggles and can support children. Iffalse, then the heading block is a static heading block.
[/TABLE]

[TABLE]
Field | Type | Description
title | arrayofrich text objects | The display name of the meeting notes session.
status | string(enum) | The lifecycle status of the transcription. Possible values are:"transcription_not_started","transcription_paused","transcription_in_progress","summary_in_progress","notes_ready".
children | object | Pointers to the related content blocks. Containssummary_block_id,notes_block_id, andtranscript_block_id(each an optional UUID string).
calendar_event | object | Calendar metadata for the meeting. Containsstart_timeandend_time(ISO 8601 timestamps) andattendees(an optional array of user IDs).
recording | object | The recording time window. Containsstart_timeandend_time(ISO 8601 timestamps).
[/TABLE]

[TABLE]
Field | Type | Description
type | "database""date""link_preview""page""user" | A constant string representing the type of the mention.
"database""date""link_preview""page""user" | object | An object with type-specific information about the mention.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text displayed in thenumbered_list_itemblock.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
list_start_index | integer(optional) | The start index of a list, used to represent a list that doesn’t start at 1.Only present on the first item of a list.
list_format | string(enum) (optional) | The type of list format. Possible values are:"numbers","letters", and"roman".Only present on the first item of a list.
children | arrayofblock objects | The nested child blocks (if any) of thenumbered_list_itemblock.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text displayed in the paragraph block.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
children | arrayofblock objects | The nested child blocks (if any) of theparagraphblock.
[/TABLE]

[TABLE]
Property | Type | Description
caption | arrayofrich text objects | A caption, if provided, for the PDF block.
type | One of:-"file"-"external"-"file_upload" | A constant string representing the type of PDF.fileindicates a Notion-hosted file, andexternalrepresents a third-party link.file_uploadis only valid when providing parameters to attach aFile Uploadto a PDF block.
external|file|file_upload | file object | An object containing type-specific information about the PDF.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text displayed in the quote block.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
children | arrayofblock objects | The nested child blocks, if any, of the quote block.
[/TABLE]

[TABLE]
Field | Type | Description
synced_from | null | The value is alwaysnullto signify that this is an original synced block that does not refer to another block.
children | arrayofblock objects | The nested child blocks, if any, of thesynced_blockblock. These blocks will be mirrored in the duplicatesynced_block.
[/TABLE]

[TABLE]
Field | Type | Description
type | string(enum) | The type of the synced from object.Possible values are:-"block_id"
block_id | string(UUIDv4) | An identifier for the originalsynced_block.
[/TABLE]

[TABLE]
Field | Type | Description
table_width | integer | The number of columns in the table.Note that this cannot be changed using the API once a table is created.
has_column_header | boolean | Whether the table has a column header. Iftrue, then the first row in the table appears visually distinct from the other rows.
has_row_header | boolean | Whether the table has a header row. Iftrue, then the first column in the table appears visually distinct from the other columns.
[/TABLE]

[TABLE]
Property | Type | Description
cells | arrayof array ofrich text objects | An array of cell contents in horizontal display order. Each cell is an array of rich text objects.
[/TABLE]

[TABLE]
Property | Type | Description
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text displayed in the title of the template.
children | arrayofblock objects | The nested child blocks, if any, of the template block. These blocks are duplicated when the template block is used in the UI.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text displayed in the To do block.
checked | boolean(optional) | Whether the To do is checked.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
children | arrayofblock objects | The nested child blocks, if any, of the To do block.
[/TABLE]

[TABLE]
Field | Type | Description
rich_text | arrayofrich text objects | The rich text displayed in the Toggle block.
color | string(enum) | The color of the block. Possible values are:-"blue"-"blue_background"-"brown"-"brown_background"-"default"-"gray"-"gray_background"-"green"-"green_background"-"orange"-"orange_background"-"yellow"-"green"-"pink"-"pink_background"-"purple"-"purple_background"-"red"-"red_background"-"yellow_background"
children | arrayofblock objects | The nested child blocks, if any, of the Toggle block.
[/TABLE]

[TABLE]
Field | Type | Description
block_type | string | The underlying block type that is not currently supported by the Notion API. Example values include:tab,form,button,drive.
[/TABLE]