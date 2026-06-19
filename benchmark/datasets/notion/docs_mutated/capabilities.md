# capabilities

*Source: https://developers.notion.com/reference/capabilities*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Content capabilities

## ​Comment capabilities

## ​User capabilities

## ​Capability Behaviors and Best Practices
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
- Content capabilities
- Comment capabilities
- User capabilities
- Capability Behaviors and Best Practices
- Read content: This capability gives an integration access to read existing content in a Notion workspace. For example, an integration with only this capability is able to callRetrieve a database, but notUpdate database.
- Update content: This capability gives an integration permission to update existing content in a Notion workspace. For example, an integration with only this capability is able to call theUpdate pageendpoint, but is not able to create new pages.
- Insert content: This capability gives an integration permission to create new content in a Notion workspace. This capability does not give the integration access to read full objects. For example an integration with only this capability is able toCreate a pagebut is not able to update existing pages.
- Read comments: This capability gives the integration permission toread commentsfrom a Notion page or block.
- Insert comments: This capability gives the integration permission toinsert commentsin a page or in an existing discussion.
- No user information: Selecting this option prevents an integration from requesting any information about users. User objects will not include any information about the user, including name, profile image, or their email address.
- User information without email addresses: Selecting this option ensures that User objects will include all information about a user, including name and profile image, but omit the email address.
- User information with email addresses: Selecting this option ensures that User objects will include all information about the user, including name, profile image, and their email address.
- If your integration is solely bringing data into Notion (creating new pages, or adding blocks), your integration only needsInsert contentcapabilities.
- If your integration is reading data to export it out of Notion, your integration will only needRead contentcapabilities.
- If your integration is simply updating a property on a page or an existing block, your integration will only needUpdate contentcapabilities.