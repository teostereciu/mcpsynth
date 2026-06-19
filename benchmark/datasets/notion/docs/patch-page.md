# patch-page

*Source: https://developers.notion.com/reference/patch-page*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Use cases

#### ​Updating properties

#### ​Setting the icon, cover, or “in trash” status

#### ​Locking and unlocking a page

#### ​Applying a page template

#### ​Erasing content from a page

#### ​Adding content to a page

### ​General behavior

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Showchild attributes
Whether the page should be locked from editing in the Notion app UI. If not provided, the locked state will not be updated.
Whether to erase all existing content from the page. When used with a template, the template content replaces the existing content. When used without a template, simply clears the page content.
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
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.pages.update({page_id:"b55c9c91-384d-452b-81db-d1ef79372b75",properties:{Name:{title:[{text:{content:"Updated Title"} }]}}})
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
- PagesPOSTCreate a pageGETRetrieve a pageGETRetrieve a page property itemPOSTMove a pageUpdate pagePATCHUpdate pageTrash a pageMarkdown content
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
- Update pagePATCHUpdate pageTrash a page
- Markdown content
- PATCHUpdate page
- Trash a page
- Pages
- File uploads
- Updatingrollup property valuesis not supported.
- A page’sparentcannot be changed.
- File Upload
- External
- Custom Emoji
- Option 1
- Option 2
- Option 3
- Option 4
- Option 5