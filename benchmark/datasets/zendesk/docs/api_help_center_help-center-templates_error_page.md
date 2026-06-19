# Error page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/error_page/*

---

## On this page

  * [Error page](/api-reference/help_center/help-center-templates/error_page/#error-page)
  * [Available properties](/api-reference/help_center/help-center-templates/error_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/error_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/error_page/#example)


# Error page

## On this page

  * [Error page](/api-reference/help_center/help-center-templates/error_page/#error-page)
  * [Available properties](/api-reference/help_center/help-center-templates/error_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/error_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/error_page/#example)


## Error page

The Error page template is rendered when a there is an error or when the requested page doesn't exist.

### Available properties

You can use the following properties in the Error page template.

Name| Type| Description
---|---|---
error| string| The error type
status_code| integer| The error status code
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

Possible errors and status codes:

Error| Status Code| Description
---|---|---
"unauthorized"| 401| User has to be authenticated to proceed
"forbidden"| 403| User is not allowed to proceed
"not_found"| others| Page doesn't exist or there was another problem

### Available helpers

You can use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers) in this page template.

### Example


    <div class="error-page">  <h1>{{t 'oops'}}</h1>
      {{#is error 'unauthorized'}}    <h2>{{link 'sign_in'}}</h2>  {{/is}}
      {{#is error 'forbidden'}}    <h2>{{t 'not_authorized'}}</h2>  {{/is}}
      {{#is error 'not_found'}}    <h2>{{t 'nonexistent_page'}}</h2>    <p>{{t 'mistyped_address_or_moved_page'}}</p>  {{/is}}
      {{#link 'help_center'}}    {{t 'back_to_homepage'}}  {{/link}}</div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)