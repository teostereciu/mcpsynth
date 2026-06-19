# retrieve-page-markdown

*Source: https://developers.notion.com/reference/retrieve-page-markdown*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Use cases

### ​General behavior

### ​Unknown blocks

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
The ID of the page (or block) to retrieve as markdown. Non-navigable block IDs from truncated responses can be passed here to fetch their subtrees.
Whether to include meeting note transcripts. Defaults to false. When true, full transcripts are included; when false, a placeholder with the meeting note URL is shown instead.
The type of object, always 'page_markdown'.
The ID of the page or block.
The page content rendered as enhanced Markdown.
Whether the content was truncated due to exceeding the record count limit.
Block IDs that could not be loaded (appeared astags in the markdown). Pass these IDs back to this endpoint to fetch their content separately.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.pages.retrieveMarkdown({page_id:"b55c9c91-384d-452b-81db-d1ef79372b75"})console.log(response.markdown)
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
- Truncation: The page exceeds the record limit (approximately 20,000 blocks) and some blocks could not be loaded.
- Permissions: The page contains child pages or other content that is not shared with the integration.
- Unsupported block types: Certain block types (such as bookmarks, embeds, and link previews) arenot yet supportedin the markdown format.