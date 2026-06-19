# updateCustomPolicy

This method updates an existing custom policy specified by the <b>custom_policy_id</b> path parameter. Since this method overwrites the policy's <b>name</b>, <b>label</b>, and <b>description</b> fields, always include the complete and current text of all three policy fields in the request payload, even if they are not being updated.<br/> <br/>For example, the value for the <b>label</b> field is to be updated, but the <b>name</b> and <b>description</b> values will remain unchanged. The existing <b>name</b> and <b>description</b> values, as they are defined in the current policy, must also be passed in. <br/><br/>A successful policy update call returns an HTTP status code of <b>204 No Content</b>.

## Endpoint

```
PUT /custom_policy/{custom_policy_id}
```

## API

Account API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **custom_policy_id** (required): This path parameter is the unique identifier of the custom policy to update.<br><br><span class="tablenote"><b>Note:</b> A list of custom policies defined for a seller's account that includes this ID can be retrieved by calling the <a href="/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies" target="_blank ">getCustomPolicies</a> method.</span> (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/CustomPolicyRequest`


## Response

**204**: No Content

## Example

```bash
curl -X PUT \
  https://api.ebay.com/custom_policy/{custom_policy_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

custom_policy

## Reference

- [eBay Account API Documentation](https://developer.ebay.com/api-docs/sell/account/overview.html)
