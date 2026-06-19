# user

*Source: https://developers.notion.com/reference/user*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Where user objects appear in the API

## ​All users

## ​People

## ​Bots
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
- Where user objects appear in the API
- All users
- People
- Bots
- Block objectundercreated_byandlast_edited_by.
- Page objectundercreated_byandlast_edited_byand inpeopleproperty items.
- Database objectundercreated_byandlast_edited_by.
- Rich text object, as user mentions.
- Property objectwhen the property is apeopleproperty.

[TABLE]
Property | Updatable | Type | Description | Example value
object* | Display-only | "user" | Always “user” | "user"
id* | Display-only | string(UUID) | Unique identifier for this user. | "e79a0b74-3aba-4149-9f74-0bb5791a6ee6"
type | Display-only | string(optional, enum) | Type of the user. Possible values are"person"and"bot". | "person"
name | Display-only | string(optional) | User’s name, as displayed in Notion. | "Avocado Lovelace"
avatar_url | Display-only | string(optional) | Chosen avatar image. | "https://secure.notion-static.com/e6a352a8-8381-44d0-a1dc-9ed80e62b53d.jpg"
[/TABLE]

[TABLE]
Property | Updatable | Type | Description | Example value
person | Display-only | object | Properties only present for non-bot users. | 
person.email | Display-only | string | Email address of person. This is only present if an integration has user capabilities that allow access to email addresses. | "[email protected]"
[/TABLE]

[TABLE]
Property | Updatable | Type | Description | Example value
bot | Display-only | object | If you’re usingGET /v1/users/meorGET /v1/users/{{your_bot_id}}, then this field returns data about the bot, includingowner,owner.type, andworkspace_name. These properties are detailed below. | { "object": "user", "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf", "name": "Test Integration", "avatar_url": null, "type": "bot", "bot": { "owner": { "type": "workspace", "workspace": true }, "workspace_name": "Ada Lovelace’s Notion" } }
owner | Display-only | object | Information about who owns this bot. | { "type": "workspace", "workspace": true }
owner.type | Display-only | stringenum | The type of owner, either"workspace"or"user". | "workspace"
workspace_name | Display-only | stringenum | If theowner.typeis"workspace", thenworkspace.nameidentifies the name of the workspace that owns the bot. If theowner.typeis"user", thenworkspace.nameisnull. | "Ada Lovelace’s Notion"
workspace_id | Display-only | string | ID of the bot’s workspace. | "17ab3186-873d-418f-b899-c3f6a43f68de"
workspace_limits | Display-only | object | Information about the limits and restrictions that apply to the bot’s workspace. | {"max_file_upload_size_in_bytes": 5242880}
workspace_limits.max_file_upload_size_in_bytes | Display-only | integer | The maximum allowable size of afile upload, in bytes. | 5242880
[/TABLE]