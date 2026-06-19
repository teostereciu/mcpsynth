# url_verification

*Source: https://docs.slack.dev/reference/events/url_verification*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This Events API-only event type has no "inner event". Instead, the complete payload you'll receive is similar to this JSON:


    {
        "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
        "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
        "type": "url_verification"
    }


This event does not require a specific OAuth scope or subscription. You'll automatically receive it whenever configuring an [Events API](/apis/events-api/) Request URL.

Once you receive the event, [verify the request's authenticity](/authentication/verifying-requests-from-slack) and then respond in plaintext with the `challenge` attribute value. In this example, that might be:


    HTTP 200 OK
    Content-type: text/plain
    3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P


If you prefer, you can respond with `application/x-www-form-urlencoded`:


    HTTP 200 OK
    Content-type: application/x-www-form-urlencoded
    challenge=3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P


Or even JSON:


    HTTP 200 OK
    Content-type: application/json
    {"challenge":"3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P"}


The important thing is to quickly [validate the request's origin](/authentication/verifying-requests-from-slack) and respond with the challenge. You can ignore the `token` provided in the event payload. This is a holdover of the deprecated verification token.

[Learn more about URL verification](/apis/events-api/#url_verification).