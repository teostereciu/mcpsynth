# getInputFile

This method downloads the file previously uploaded using <strong>uploadFile</strong>. Specify the task_id from the <strong>uploadFile</strong> call. <p><span class="tablenote"><strong>Note:</strong> With respect to LMS, this method applies to all feed types except <code>LMS_ORDER_REPORT</code> and <code>LMS_ACTIVE_INVENTORY_REPORT</code>. See <a href="/api-docs/sell/static/feed/lms-feeds.html">LMS API Feeds</a> in the Selling Integration Guide.</span></p>

## Endpoint

```
GET /task/{task_id}/download_input_file
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **task_id** (required): This path parameter is the unique identifier of the task associated with the input file to be downloaded.<br><br>Use the <a href="/api-docs/sell/feed/resources/task/methods/getTasks" target="_blank ">getTasks</a> method to retrieve task IDs. (Type: `string`)

## Response

**200**: Success

## Example

```bash
curl -X GET \
  https://api.ebay.com/task/{task_id}/download_input_file \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

task

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
