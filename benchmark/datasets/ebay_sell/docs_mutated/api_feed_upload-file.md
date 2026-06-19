# uploadFile

This method associates the specified file with the specified task ID and uploads the input file. After the file has been uploaded, the processing of the file begins. <br><br>Reports often take time to generate and it's common for this method to return an HTTP status of 202, which indicates the report is being generated. Use the <b> getTask</b> with the task ID or <b> getTasks</b> to determine the status of a report. <br><br>The status flow is <code>QUEUED</code> &gt; <code>IN_PROCESS</code> &gt; <code>COMPLETED</code> or <code>COMPLETED_WITH_ERROR</code>. When the status is <code>COMPLETED</code> or <code>COMPLETED_WITH_ERROR</code>, this indicates the file has been processed and the order report can be downloaded. If there are errors, they will be indicated in the report file. <br /><br />For details of how this method is used in the upload flow, see <a href="/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html">Working with Order Feeds</a> in the Selling Integration Guide. <br><br>This call does not have a JSON Request payload but uploads the file as form-data. For example:<br /> <pre> fileName: &quot;AddFixedPriceItem_Macbook.xml&quot; <br /> name: &quot;file&quot; <br /> type: &quot;form-data&quot; <br /> file: @&quot;/C:/Users/.../AddFixedPriceItem_Macbook.7z&quot;</pre>See <a href="/api-docs/sell/feed/resources/task/methods/uploadFile#h2-samples">Samples</a> for information.<p><span class="tablenote"><strong>Note:</strong> This method applies to all <a href="/api-docs/sell/static/feed/fx-feeds-quick-reference.html#availabl" target="_blank">Seller Hub feed types</a>, and to all <a href="/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl" target="_blank">LMS feed types</a> except <code>LMS_ORDER_REPORT</code> and <code>LMS_ACTIVE_INVENTORY_REPORT</code>.</span></p><p> <span class="tablenote"><b>Note:</b> You must use a <strong>Content-Type</strong> header with its value set to "<strong>multipart/form-data</strong>". See <a href="/api-docs/sell/feed/resources/task/methods/uploadFile#h2-samples">Samples</a> for information.</span></p><p><span class="tablenote"><b>Note:</b> For LMS feed types, upload a regular XML file or an XML file in zipped format (both formats are allowed).</span></p>

## Endpoint

```
POST /task/{task_id}/upload_file
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **task_id** (required): This path parameter is the unique identifier of the task associated with the file that will be uploaded.<br><br>Use the <a href="/api-docs/sell/feed/resources/task/methods/getTasks" target="_blank ">getTasks</a> method to retrieve task IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>multipart/form-data</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

## Response

**200**: Success

Response includes JSON with relevant data.

## Example

```bash
curl -X POST \
  https://api.ebay.com/task/{task_id}/upload_file \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

task

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
