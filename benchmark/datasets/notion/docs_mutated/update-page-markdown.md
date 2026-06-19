# update-page-markdown

*Source: https://developers.notion.com/reference/update-page-markdown*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Use cases

#### ​Updating content with search-and-replace (recommended)

#### ​Replacing all page content (recommended)

#### ​Inserting content (legacy)

#### ​Replacing a content range (legacy)

### ​General behavior

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
The ID of the page to update.
Alwaysinsert_content
Insert new content into the page.
Showchild attributes
The type of object, always 'page_markdown'.
The ID of the page or block.
The page content rendered as enhanced Markdown.
Whether the content was truncated due to exceeding the record count limit.
Block IDs that could not be loaded (appeared astags in the markdown). Pass these IDs back to this endpoint to fetch their content separately.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.pages.updateMarkdown({page_id:"b55c9c91-384d-452b-81db-d1ef79372b75",type:"update_content",update_content:{content_updates:[{old_str:"existing text to find",new_str:"replacement text"}]}})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","markdown":"<string>","truncated":true,"unknown_block_ids": ["3c90c3cc-0d44-4b50-8888-8dd25736052a"]}
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
- PagesPOSTCreate a pageGETRetrieve a pageGETRetrieve a page property itemPOSTMove a pageUpdate pageMarkdown contentGETRetrieve a page as markdownPATCHUpdate a page's content as markdown
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
- Markdown contentGETRetrieve a page as markdownPATCHUpdate a page's content as markdown
- GETRetrieve a page as markdown
- PATCHUpdate a page's content as markdown
- Pages
- File uploads
- Insert Content
- Replace Content Range
- Update Content
- Replace Content

[TABLE]
Error code | Condition
validation_error | Thecontent_rangeorafterselection does not match any content in the page, or anold_strinupdate_contentis not found.
validation_error | The operation would delete child pages or databases andallow_deleting_contentis nottrue.
validation_error | Anold_strinupdate_contentmatches multiple locations andreplace_all_matchesis nottrue.
validation_error | The provided ID is a database or non-page block.
validation_error | The target page is a synced page. Synced pages cannot be updated.
object_not_found | The page does not exist or the integration does not have access to it.
[/TABLE]