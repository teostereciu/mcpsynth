# archive-a-page

*Source: https://developers.notion.com/reference/archive-a-page*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Example request: trash a Notion page

## ​Example request: restore a Notion page

```
curlhttps://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7\-H‘Authorization:Bearer‘"$NOTION_API_KEY"’’\-H"Content-Type: application/json"\-H"Notion-Version: 2026-03-11"\-XPATCH\--data‘{"in_trash":true}’
```

```
const{Client}=require("@notionhq/client")// Initializing a clientconstnotion=newClient({auth:process.env.NOTION_API_KEY,})consttrashPage=async()=>{awaitnotion.pages.update({page_id:pageId,in_trash:true,});}
```

```
{"object":"page","id":"be633bf1-dfa0-436d-b259-571129a590e5","created_time":"2022-10-24T22:54:00.000Z","last_edited_time":"2023-03-08T18:25:00.000Z","created_by": {"object":"user","id":"c2f20311-9e54-4d11-8c79-7398424ae41e"},"last_edited_by": {"object":"user","id":"9188c6a5-7381-452f-b3dc-d4865aa89bdf"},"cover":null,"icon": {"type":"emoji","emoji":"🐞"},"parent": {"type":"database_id","database_id":"a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"},"in_trash":true,"properties": {"Due date": {"id":"M%3BBw","type":"date","date": {"start":"2023-02-23","end":null,"time_zone":null}},"Status": {"id":"Z%3ClH","type":"status","status": {"id":"86ddb6ec-0627-47f8-800d-b65afd28be13","name":"Not started","color":"default"}},"Title": {"id":"title","type":"title","title": [{"type":"text","text": {"content":"Bug bash","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Bug bash","href":null}]}},"url":"https://www.notion.so/Bug-bash-be633bf1dfa0436db259571129a590e5"}
```

```
// Restore a trashed page using the Notion JavaScript SDKconstrestorePage=async()=>{awaitnotion.pages.update({page_id:pageId,in_trash:false,});}
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
- Example request: trash a Notion page
- Example request: restore a Notion page