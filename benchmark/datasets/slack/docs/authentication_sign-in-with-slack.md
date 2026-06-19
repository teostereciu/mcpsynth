# Using Sign in with Slack

*Source: https://docs.slack.dev/authentication/sign-in-with-slack/*

---

Sign in with Slack helps users log into your service using their Slack profile.

The Sign in with Slack flow will redirect users to the right Slack URL. Slack will send users back to your service, along with the information your service needs.

The flow is based on the [OpenID Connect standard](https://openid.net/specs/openid-connect-core-1_0.html), built on top of [OAuth 2.0](/authentication/installing-with-oauth). The modern Sign in with Slack flow works with any package that successfully implements this standard. OpenID maintains a list of [certified implementations of the OpenID Connect standard](https://openid.net/developers/certified/). We recommend you make use of one of these packages to take care of the boilerplate surrounding OAuth.

If you already have an existing Sign in with Slack app that uses `identity.*` scopes, you can find [legacy Sign in with Slack documentation here](/legacy/legacy-authentication/legacy-sign-in-with-slack).

Check out [Sign in with Slack links](/authentication/sign-in-with-slack/setting-up-sign-in-with-slack-links), which allows users to share their Slack profile with you when they click a link from your service.

* * *

## Getting started​

Implementation of the Sign in with Slack flow follows the flow of [our OAuth V2 process](/authentication/installing-with-oauth). If you're not familiar with that, you'll want to review these steps.

The key differences between **Sign in with Slack** and a typical OAuth flow for a Slack app are as follows:

  * You redirect users to a special OpenID endpoint, `/openid/connect/authorize`, rather than `/oauth/v2/authorize`.
  * You request the OpenID scopes—[`openid`](/reference/scopes/openid), [`email`](/reference/scopes/email), and [`profile`](/reference/scopes/profile). (With legacy Sign in with Slack, you requested legacy `identity.*` scopes.)
  * You exchange your access code for an access token using an OpenID method, [`/openid.connect.token`](/reference/methods/openid.connect.token), rather than `oauth.v2.access`.
  * You receive the [standard OpenID response](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) sent to your redirect URI with the expected fields encoded in the `id_token`.
  * You use the [`openid.connect.userInfo`](/reference/methods/openid.connect.userInfo) method to retrieve updated user information. (With legacy Sign in with Slack, you used [`users.identity`](/reference/methods/users.identity).)


We'll step through the flow in more detail below.

### App setup​

First, create a Slack app:

[Create an app](https://api.slack.com/apps?new_app=1)

Enter your **App Name** and select the Development Workspace where you'll play around and build your app. Don't fuss too much over either field—no matter what workspace you select, you'll still be able to [distribute your app](/app-management/distribution) to other workspaces if you choose.

Navigate to the **OAuth & Permissions** section and configure a **Redirect URL** to match your service. The Redirect URL signifies where Slack should redirect users when they complete the OAuth flow. If you're using `ngrok`, use the ngrok public forwarding host as the root.

### Discover information on Slack OpenID endpoints​

Slack provides a discovery endpoint so that your OpenID Connect Relying Party can discover which endpoints to call. Our Well Known endpoint is accessible at:


    https://slack.com/.well-known/openid-configuration


The response follows the [OpenID standard](https://openid.net/specs/openid-connect-discovery-1_0.html), as in the following example:


    {
        "issuer": "https://slack.com",
        "authorization_endpoint": "https://slack.com/openid/connect/authorize",
        "token_endpoint": "https://slack.com/api/openid.connect.token",
        "userinfo_endpoint": "https://slack.com/api/openid.connect.userInfo",
        "jwks_uri": "https://slack.com/openid/connect/keys",
        "scopes_supported": ["openid","profile","email"],
        "response_types_supported": ["code"],
        "response_modes_supported": ["form_post"],
        "grant_types_supported": ["authorization_code"],
        "subject_types_supported": ["public"],
        "id_token_signing_alg_values_supported": ["RS256"],
        "claims_supported": ["sub","auth_time","iss"],
        "claims_parameter_supported": false,
        "request_parameter_supported": false,
        "request_uri_parameter_supported": true,
        "token_endpoint_auth_methods_supported": ["client_secret_post","client_secret_basic"]
    }


### Request with scopes​

Send users into the Sign in with Slack authorization flow with a button or other redirect. If you're unsure of what that should look like, check out our design guidelines for tips on how to make the experience as pleasant as possible for your users.

A scope conflict occurs when attempting to combine Sign in with Slack user scopes with non-Sign in with Slack scopes in the same OAuth flow

Each set of scopes must be requested in separate OAuth flows.

You should redirect users to the following URL:


    https://slack.com/openid/connect/authorize


Your request should have the [standard OpenID Connect form](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint), which is why it pays to use a pre-implemented package.

Here's an example:


      GET /openid/connect/authorize?
        response_type=code
        &scope=openid%20profile%20email
        &client_id=s6BhdRkqt3
        &state=af0ifjsldkj
        &team=T1234
        &nonce=abcd
        &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb HTTP/1.1
      Host: https://slack.com


Here's a quick explanation of the parameters:

Parameter| Description| `response_type`| Set equal to `code`. This indicates you're asking for a temporary access code to then exchange for an access token.| `scope`| Which permissions you want the user to grant you. Your app will request `openid`, the base scope you always need to request in any Sign in with Slack flow. You may request `email` and `profile` as well.| `client_id`| Your app's client ID. You can find it in your [app settings](https://api.slack.com/apps) under **Basic Information**.| `state`| Used to avoid forgery attacks. Pass in a value that's unique to the user you're authenticating, and check it when you receive a temporary authorization code.| `nonce`| Used to verify that the entire flow has completed with no forgery. You can verify the `nonce` in the response you receive from the final token exchange to ensure it's the same as what you pass here.| `redirect_uri`| Where Slack will send the user, along with the temporary authorization code, once the user okays your app. You can specify a more _specific_ `redirect_uri` than the one in your [app settings](https://api.slack.com/apps) here, but it must be either an exact match or a subdirectory of one of the redirect URLs in your app settings.| `team`| The workspace the user is intending to authenticate. If that workspace has been previously authenticated, the user will be signed in directly, bypassing the consent screen.
---|---

### Exchange​

After the user successfully grants your app permission to access their Slack profile, they'll be redirected back to your service along with the typical `code` that signifies a temporary access code. Exchange that `code` for a real access token using the [`/openid.connect.token`](/reference/methods/openid.connect.token) method.

You can check that method's documentation for a full list of parameters to pass. As an overview, you'll pass:

  * `code`
  * your app's `client_secret`
  * your app's `client_id`
  * your app's `redirect_uri`


### Response​

After calling the [`openid.connect.token`](/reference/methods/openid.connect.token) method, you'll receive a standard OpenID response:


    {
      "ok": true,
      "access_token": "xoxp-...-...-...-123",
      "token_type": "Bearer",
      "id_token": "123abc...456"
    }


The `id_token` parameter is a [standard](https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse) JSON Web Token (JWT). You can decode it with off-the-shelf libraries in any programming language, and most packages that handle OpenID will handle JWT decoding.

If you've requested the `openid` `email`. and `profile` scopes, the token response decodes into an object as in the following example:


    {
      "iss": "https://slack.com",
      "sub": "U123ABC456",
      "aud": "25259531569.1115258246291",
      "exp": 1626874955,
      "iat": 1626874655,
      "auth_time": 1626874655,
      "nonce": "abcd",
      "at_hash": "abc...123",
      "https://slack.com/team_id": "T0123ABC456",
      "https://slack.com/user_id": "U123ABC456",
      "email": "alice@example.com",
      "email_verified": true,
      "date_email_verified": 1622128723,
      "locale": "en-US",
      "name": "Alice",
      "given_name": "",
      "family_name": "",
      "https://slack.com/team_image_230": "https://secure.gravatar.com/avatar/bc.png",
      "https://slack.com/team_image_default": true
    }


Some additional fields may be included in the payload. Make sure to verify that the `nonce` returned in the JWT payload is the same as the `nonce` you supplied to `authorize`.

Your Sign in with Slack flow has officially completed. Now you can obtain updated user info whenever you want for that authenticated user.

### Get updated user info​

Once you've obtained a user access token from the Sign in with Slack flow, you can use the [`openid.connect.userInfo`](/reference/methods/openid.connect.userInfo) method to get updated user information, such as their profile image and team image. Read up on that documentation for more details on the exact response to expect.

### Token rotation​

[Token rotation](/authentication/using-token-rotation) is supported with Sign in with Slack. It works exactly like regular token rotation, except with the Sign in Slack token exchange endpoint. You'll pass a `grant_type=refresh_token` and use a `refresh_token` parameter to obtain a new access token from [`openid.connect.token`](/reference/methods/openid.connect.token).

* * *

## Button generator​

You can use the Sign in with Slack button generator [here](https://api.slack.com/sign-in-with-slack-button-generator).

* * *

## Migrate a legacy Sign in with Slack app​

If you have a [legacy Sign in with Slack app](/authentication/sign-in-with-slack/), there are only a few steps needed to migrate to the current flow. Request the new OpenID scopes, reconfigure your authorization URL, parse the new response from `openid.connect.token`, and you're good to go.

Here's a map of what legacy Sign in with Slack feature corresponds to what modern feature:

  * The authorization endpoint becomes `/openid/connect/authorize`, rather than `/oauth/v2/authorize`.
  * You exchange your access code for an access token using an OpenID endpoint, [`openid.connect.token`](/reference/methods/openid.connect.token).
  * The `identity.basic` becomes the [`openid`](/reference/scopes/openid) scope.
  * The `identity.email` becomes the [`email`](/reference/scopes/email) scope.
  * The `identity.avatar` is contained in the [`profile`](/reference/scopes/profile) scope.
  * The `identity.team` is also contained in the [`profile`](/reference/scopes/profile) scope.
  * The `users.info` method becomes the [`openid.connect.userInfo`](/reference/methods/openid.connect.userInfo) method.


Enjoy your modern Sign in with Slack app! If you want to get even more nitty gritty details on how best to present a pleasant experience to users, read on for some design guidelines.

* * *

## Button design guidelines​

You should use our button generator to create a Sign in with Slack button. But if you need to modify that button or create your own, here are some basic design guidelines you should follow:

  * Show the button prominently.
  * The Slack logo should always be present.
  * The text should always say Sign in with Slack, with ‘S’ capitalized.
  * Use the same size as other sign in options.
  * Make it visible and keep it above the fold.


### Sizing​

A max size button should be:

  * 296px (width) x 56px (height)
  * 18px font Lato bold
  * Logo : 24px x 24px


A minimum size button should be:

  * 224px (width) x 44px (height)
  * 14px font Lato bold
  * Logo : 16px x 16px


A default size button should be:

  * 256px (width) x 48px (height)
  * 16px font Lato bold
  * Logo : 20px x 20px


### Spacing​

For a center-aligned logo, use:

  * Margin-between: 12px


For a border-aligned logo, use:

  * Margin-left: 16px


### Corners​

Use a border-radius of:

  * Min: 4px
  * Max: height of the button


### Color themes​

For a default theme, use:

  * Background color : #FFFFFF
  * Font color : #000000
  * Border color : #DDDDDD


For a dark theme, recommended only for spaces with sufficient contrast, use:

  * Background color : #4A154B
  * Font color : #FFFFFF
  * Border : none


### Icon sizing​

You can also use an icon button consisting only of the Slack logo.

Dimensions of a max size button:

  * 56px (width) x 56px (height)
  * Logo: 28px x 28px


Min size:

  * 36px (width) x 36px (height)
  * Logo: 18px x 18px


Default size:

  * 48px (width) x 48px (height)
  * Logo: 24px x 24px


### Icon corners​

Use a border-radius of:

  * Min: 4px
  * Max: height of the button


### Icon color themes​

Color guidelines for icon buttons are the same as text buttons above.

### Assets​

If you can't use our button generator, you can use the following static image assets instead. This HTML snippet references our CDN-hosted buttons:


    <img src="https://platform.slack-edge.com/img/sign_in_with_slack.png" srcset="https://platform.slack-edge.com/img/sign_in_with_slack.png 1x, https://platform.slack-edge.com/img/sign_in_with_slack.png 2x" />


If you want to host the assets yourself, you can download these images:

[__Download PNG (170px by 40px)](https://platform.slack-edge.com/img/sign_in_with_slack.png) [__Download PNG (Retina, 344px by 80px)](https://platform.slack-edge.com/img/sign_in_with_slack.png)