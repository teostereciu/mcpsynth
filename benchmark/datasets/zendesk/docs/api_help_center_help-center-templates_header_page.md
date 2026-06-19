# Header

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/header_page/*

---

## On this page

  * [Header](/api-reference/help_center/help-center-templates/header_page/#header)
  * [Available properties](/api-reference/help_center/help-center-templates/header_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/header_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/header_page/#example)


# Header

## On this page

  * [Header](/api-reference/help_center/help-center-templates/header_page/#header)
  * [Available properties](/api-reference/help_center/help-center-templates/header_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/header_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/header_page/#example)


## Header

The Header template is rendered at the top of every page in the help center.

### Available properties

You can use the following properties in the Header template.

Name| Type| Description
---|---|---
current_locale| object| A [locale](/api-reference/help_center/help-center-templates/objects#locale-object) object corresponding to the one currently used by the user
alternative_locales| array| An array of [locale](/api-reference/help_center/help-center-templates/objects#locale-object) objects corresponding to all the available locales in help center except the current one
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object
signed_in| boolean| Whether the user is logged in or not
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers). You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
my_profile| Shows the current user's profile. See [my_profile helper](/api-reference/help_center/help-center-templates/helpers#my_profile-helper)
change_password| Show the change password modal. See [change_password helper](/api-reference/help_center/help-center-templates/helpers#change_password-helper)

### Example


    <header class="header">  <div class="logo">    {{#link 'help_center'}}      <img src="{{settings.logo}}" alt="{{t 'logo'}}">    {{/link}}  </div>  <nav class="user-nav">    {{link "new_request" class="submit-a-request" role="button"}}  </nav></header>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)