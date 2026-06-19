# Using HTTP Request URLs

*Source: https://docs.slack.dev/apis/events-api/using-http-request-urls*

---

Once you've weighed the pros and cons and [made the decision to use HTTP](/apis/events-api/comparing-http-socket-mode) in your app, you will need to set up and verify your request URL. This guide will show you how to set this up.

## Handling app installation and authentication with Request URLs​

Request URLs operate similarly to [slash command](/interactivity/implementing-slash-commands) invocation URLs in that they receive an HTTP POST containing data in response to activity. In the Events API, your Events API request URL is the target location where all of the events your application is subscribed to will be delivered, regardless of the workspace or event type.

Since your application will have only one Events API request URL, you'll need to do any additional dispatch or routing server-side after receiving event data.

Your request URL will receive JSON-based payloads containing wrapped [event types](/reference/events). The volume of events will vary depending on the events you subscribe to and the size and activity of the workspaces that install your application.

Your request URL might receive _many_ events and requests. Consider decoupling your ingestion of events from the processing and reaction to them.

Review the Events API guide section on [rate limiting](/apis/events-api/#rate_limiting) to better understand the maximum event volume you may receive.

### Request URL configuration and verification​

After you create your app, navigate to the [app settings page](https://api.slack.com/apps) and select your app to view its settings. In the **Event Subscriptions** section, toggle the feature on. This will reveal a field where you should enter your request URL.

Your Event request URL must be confirmed before saving this form. If your server takes some time to "wake up" and your initial attempt at URL verification fails due to a timeout, use the **Retry** button to attempt verification again. Careful, request URLs are case-sensitive.

### URL verification handshake​

The events sent to your request URL may contain sensitive information associated with the workspaces having approved your Slack app. To ensure that events are being delivered to a server under your direct control, we must verify your ownership by issuing you a challenge request.

After you've completed typing your URL, we'll dispatch an HTTP POST to your request URL. We'll verify your SSL certificate and we'll send a `application/json` POST body containing three fields:


    {
        "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
        "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
        "type": "url_verification"
    }


This event does not require a specific OAuth scope or subscription. You'll automatically receive it whenever configuring an [Events API](/apis/events-api/) request URL. The attributes Slack sends include:

  * `token`: This deprecated verification token is proof that the request is coming from Slack on behalf of your application. You'll find this value in the **App Credentials** section of the **Basic Information** of your [app settings](https://api.slack.com/apps). Verifying this value is more important when working with real events after this verification sequence has been completed. When responding to real events, always use the [more secure signing secret process](/authentication/verifying-requests-from-slack) to verify Slack requests' authenticity.
  * `challenge`: a randomly generated string produced by Slack. The purpose for sending this string is that you'll respond to this request with a response body containing this value.
  * `type`: this payload is similarly formatted to other event types you'll encounter in the Events API. To help you differentiate URL verification requests form other event types, we inform you that this is of the `url_verification` variety.


### Respond to the challenge​

Once you receive the event, complete the sequence by responding with HTTP 200 and the `challenge` attribute value.

Responses can be sent in plaintext:


    HTTP 200 OK
    Content-type: text/plain
    3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P


Alternatively, if you're feeling more formal, respond with `application/x-www-form-urlencoded` and a named `challenge` parameter:


    HTTP 200 OK
    Content-type: application/x-www-form-urlencoded
    challenge=3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P


Or if you feel like showing off, respond with `application/json`:


    HTTP 200 OK
    Content-type: application/json
    {"challenge":"3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P"}


Once URL verification is complete, you'll see a green check mark celebrating your victory.

If you receive an error from your server, a timeout, or other exceptional condition occurs, you'll see error messages that will hopefully help you understand what's amiss before you try again.

Especially when working with large workspaces, many workspaces, or subscribing to a large number of events, de-coupling the processing of and reaction to events is key. With this challenging handshake complete, you're ready to open up our [event type catalog](/reference/events) and decide which events to subscribe to.

## Next steps​

Now that you've set up your app to use HTTP request URLs, explore the [Events API](/apis/events-api/) guide to learn how to subscribe to, receive, and handle events. Also be sure to check out the [Interactivity](/interactivity/handling-user-interaction) guide, including [Shortcuts](/interactivity/implementing-shortcuts) and [Slash commands](/interactivity/implementing-slash-commands) for additional ways to customize your app.