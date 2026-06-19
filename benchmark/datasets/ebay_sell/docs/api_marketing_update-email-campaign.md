# updateEmailCampaign

This method lets users update an existing email campaign. Pass the <b>emailCampaignId</b> in the request URL and specify the changes to field values in the request payload.<br><br><span class="tablenote"><b>Note: </b>You can only update the custom fields of an email campaign. Fixed values, such as the <b>emailCampaignType</b>, cannot be changed. For full specifications of fixed values for each email campaign type, see the <a href="/api-docs/sell/marketing/resources/email_campaign/methods/createEmailCampaign">createEmailCampaign</a> method documentation.</span>

## Endpoint

```
PUT /email_campaign/{email_campaign_id}
```

## API

Marketing API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **email_campaign_id** (required): This path parameter specifies the unique eBay assigned identifier for the email campaign being updated.<br><br>Use the <a href="/api-docs/sell/marketing/resources/campaign/methods/getEmailCampaigns" target="_blank">getEmailCampaigns</a> method to retrieve a list of email campaign IDs for a seller. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/UpdateCampaignRequest`


## Response

**200**: OK

Response schema: `#/components/schemas/UpdateEmailCampaignResponse`

## Example

```bash
curl -X PUT \
  https://api.ebay.com/email_campaign/{email_campaign_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

email_campaign

## Reference

- [eBay Marketing API Documentation](https://developer.ebay.com/api-docs/sell/marketing/overview.html)
