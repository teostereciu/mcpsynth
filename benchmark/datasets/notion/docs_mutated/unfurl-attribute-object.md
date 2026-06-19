# unfurl-attribute-object

*Source: https://developers.notion.com/reference/unfurl-attribute-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​The unfurl attribute object

### ​Inline sub-type objects

#### ​Thedevattribute

### ​Embed sub-type child objects

### ​Thesectionvalue

```
[{"id":"title","name":"Title","type":"inline","inline": {"title": {"value":"Feature Request: Link Previews","section":"title"}}},{"id":"dev","name":"Developer Name","type":"inline","inline": {"plain_text": {"value":"Acme Inc","section":"secondary"}}},{"id":"state","name":"State","type":"relation","relation": {"uri":"acme:item_state/open","mention": {"section":"primary"}}},{"id":"itemId","name":"Item Id","type":"inline","inline": {"plain_text": {"value":"#23487","section":"identifier"}}},{"id":"itemIcon","name":"Item Icon","type":"inline","inline": {"color": {"value": {"r":247,"g":247,"b":42},"section":"entity"}}},{"id":"description","name":"Description","type":"inline","inline": {"plain_text": {"value":"Would love to be able to preview some Acme resources in Notion!\nMaybe an open item?","section":"body"}}},{"id":"updated_at","name":"Updated At","type":"inline","inline": {"datetime": {"value":"2022-01-11T19:53:18.829Z","section":"secondary"}}},{"id":"label","name":"Label","type":"inline","inline": {"enum": {"value":"🔨 Ready to Build","color": {"r":100,"g":100,"b":100},"section":"primary"}}},{"id":"media","name":"Embed","embed": {"src_url":"https://c.tenor.com/XgaU95K_XiwAAAAC/kermit-typing.gif","image": {"section":"embed"}}}]
```

```
{"id":"title","name":"Title","type":"inline","inline": {"title": {"value":"Feature Request: Link Previews","section":"title"}}}
```

```
{"id":"dev","name":"Developer Name","type":"inline","inline": {"plain_text": {"value":"Acme Inc","section":"secondary"}}}
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
- Block
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
- The unfurl attribute object
- Inline sub-type objects
- The dev attribute
- Embed sub-type child objects
- The section value
- Introduction to Link Preview integrationsguide
- Build a Link Preview integrationguide
- Help Centreguide

[TABLE]
Field | Type | Description | Example value
id | string | A unique identifier for the attribute. If more than one attribute with the sameidis provided, then the latter attribute overrides the value of the first. | "title"
name | string | A human readable name describing the attribute. | "Title"
type | inline||embed | The type of attribute. Most attributes areinline. Useembedfor rich media sub-types likeimage,video, oraudio. | "inline"
inline||embed | object | An object whose key is a sub-type. The child sub-type object includes thevalueto display and thesectionof the Link Preview where the data is rendered. | { "title": { "value": "Feature Request: Link Previews", "section": "title" } }
[/TABLE]

[TABLE]
Sub-type | Description | Example value
color | A color with r, b, g values. | { "value": { "r": 247, "g": 247, "b": 42 }, "section": "entity" }
date | A date. | { "value": "2022-01-11", "section": "secondary" }
datetime | A datetime. | { "value": "2022-01-11T19:53:18.829Z", "section": "secondary" }
enum | A string value and optional color object. | { "value": "🔨 Ready to Build", "color": { "r": 100, "g": 100, "b": 100 }, "section": "primary" }
plain_text | Any plain text content. | { "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?", "section": "body" }
title* | The title of the Link Preview. *An unfurl attribute object of this type must be included in every payload to create a Link Preview. | { "value": "Feature Request: Link Previews", "section": "title" }
[/TABLE]

[TABLE]
Sub-type | Description | Example value
audio | Audio from a source URL. | { "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "audio": { "section": "embed" } }
html | HTML from a source URL that is rendered in an iFrame. | { "src_url": "https://s3.us-east-3.amazonaws.com/12345.html", "html": { "section": "embed" } }
image | Image from a source URL. | { "src_url": "https://s3.us-east-3.amazonaws.com/12345.png", "image": { "section": "avatar" } }
video | Video from a source URL. | { "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "video": { "section": "embed" } }
[/TABLE]

[TABLE]
Section | Description | Valid parent sub-types
avatar | The picture found on the bottom left of a Link Preview. | image,plain_text
background | A background color for the Link Preview. | color
body | The main string content of a Link Preview. | plain_text
embed | The large space where the content of anembedattribute type is displayed in a Link Preview. | audio,html,image,pdf,video
entity | The small picture found in the subheading of a Link Preview and in a Mention. | color,image
identifier | The subheading found on the bottom of a Link Preview and on the left side of a Mention. | image,plain_text
primary | The first subheading section. | enum,date,datetime,plain_text
secondary | The second subheading section. | date,datetime,plain_text
title* | The main heading in a Link Preview or Mention. *Required. | title
[/TABLE]