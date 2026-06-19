# moveStoreCategory

This method is used to move an existing user's eBay store custom category through an asynchronous request. A successful call returns the <b>getStoreTask</b> URI in the Location response header. The user calls <b>getStoreTask</b> to retrieve the status of the move category operation.<br><br><div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> If you initiate a category change, you cannot make additional category changes until the previous change request has completed. Use getStoreTask (or getStoreTasks) method to get latest status of your last request.</p></div>

## Endpoint

```
POST /store/categories/move_category
```

## API

Stores API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/MoveStoreCategoryRequestType`


## Response

**202**: The request is accepted, user should get the location url in response to retrieve async task status.

## Example

```bash
curl -X POST \
  https://api.ebay.com/store/categories/move_category \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

store

## Reference

- [eBay Stores API Documentation](https://developer.ebay.com/api-docs/sell/stores/overview.html)
