# search-optimizations-and-limitations

*Source: https://developers.notion.com/reference/search-optimizations-and-limitations*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Optimizations

## ​Limitations
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
- SearchSearch by titleSearch optimizations and limitations
- Users
- Search by title
- Search optimizations and limitations
- File uploads
- Optimizations
- Limitations
- Exhaustively enumerating through all the documents that a bot has access to in a workspace.Search is not guaranteed to return everything, and the index may change as your integration iterates through pages and databases.
- Searching or filtering within a particular database.This use case is much better served by finding the database ID and using theQuery a data sourceendpoint.
- Immediate and complete results.Search indexing is not immediate. If an integration performs a search quickly after a page is shared with the integration (such as immediately after a user performs OAuth), then the response may not contain the page.When an integration needs to present a user interface that depends on search results, we recommend including aRefreshbutton to retry the search. This will allow users to determine if the expected result is present or not, and give them a way to try again.
- When an integration needs to present a user interface that depends on search results, we recommend including aRefreshbutton to retry the search. This will allow users to determine if the expected result is present or not, and give them a way to try again.