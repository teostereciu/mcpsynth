# post-page

*Source: https://developers.notion.com/reference/post-page*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Use cases

#### ​Choosing a parent

#### ​Setting up page properties

#### ​Setting up page content

### ​General behavior

### ​Errors

#### Authorizations

#### Headers

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Showchild attributes
Page content as Notion-flavored Markdown. Mutually exclusive with content/children.
The page object type name.
The ID of the page.
Date and time when this page was created.
Date and time when this page was last edited.
Whether the page is in trash.
Whether the page has been archived.
Whether the page is locked from editing in the Notion app UI.
The URL of the Notion page.
The public URL of the Notion page, if it has been published to the web.
Information about the page's parent.
Property values of this page.
Page cover image.
User who created the page.
User who last edited the page.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.pages.create({parent:{data_source_id:"d9824bdc-8445-4327-be8b-5b47500af6ce"},properties:{Name:{title:[{text:{content:"New Page Title"} }]}}})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","created_time":"2023-11-07T05:31:56Z","last_edited_time":"2023-11-07T05:31:56Z","in_trash":true,"is_archived":true,"is_locked":true,"url":"<string>","public_url":"<string>","parent": {"type":"<string>","database_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"},"properties": {},"icon": {"type":"<string>","emoji":"<string>"},"cover": {"type":"<string>","file": {"url":"<string>","expiry_time":"2023-11-07T05:31:56Z"}},"created_by": {"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","object":"<string>"},"last_edited_by": {"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","object":"<string>"}}
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
- PagesPOSTCreate a pageGETRetrieve a pageGETRetrieve a page property itemPOSTMove a pageUpdate pageMarkdown content
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a page
- GETRetrieve a page
- GETRetrieve a page property item
- POSTMove a page
- Update page
- Markdown content
- Pages
- File uploads
- default: Apply the data source’s default template.This is only allowed for pages created under a data source that has a default template configured in the Notion app.
- template_id: Provide a specifictemplate_idto use as the blueprint for your page.The API bot must have access to the template page, and it must be within the same workspace.Although any valid page ID can be used as thetemplate[template_id], we recommend only using pages that are configured as actualdatabase templatesunder the same data source as the parent of your new page to make sure that page properties can get merged in correctly.
- This is only allowed for pages created under a data source that has a default template configured in the Notion app.
- The API bot must have access to the template page, and it must be within the same workspace.
- Although any valid page ID can be used as thetemplate[template_id], we recommend only using pages that are configured as actualdatabase templatesunder the same data source as the parent of your new page to make sure that page properties can get merged in correctly.
- Page Id
- Database Id
- Data Source Id
- Workspace
- File Upload
- External
- Custom Emoji
- Embed
- Bookmark
- Image
- Video
- Pdf
- Audio
- Code
- Equation
- Divider
- Breadcrumb
- Tab
- Table Of Contents
- Link To Page
- Table Row
- Table
- Column List
- Column
- Heading 1
- Heading 2
- Heading 3
- Paragraph
- Bulleted List Item
- Numbered List Item
- Quote
- To Do
- Toggle
- Template
- Callout
- Synced Block
- Option 1
- Option 2
- Option 3
- Option 4
- Option 5