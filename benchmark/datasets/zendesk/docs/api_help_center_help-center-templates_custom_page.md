# Custom Page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/custom_page/*

---

## On this page

  * [Custom page](/api-reference/help_center/help-center-templates/custom_page/#custom-page)
  * [Available properties](/api-reference/help_center/help-center-templates/custom_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/custom_page/#available-helpers)


# Custom Page

## On this page

  * [Custom page](/api-reference/help_center/help-center-templates/custom_page/#custom-page)
  * [Available properties](/api-reference/help_center/help-center-templates/custom_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/custom_page/#available-helpers)


## Custom page

The Custom page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/p/{page_name}`.

Custom pages are different from other types of page templates in that you create each template from scratch and then link to the resulting page from anywhere in your help center or from any other webpage or application. For more information, see [Creating custom pages in your help center](https://support.zendesk.com/hc/en-us/articles/4409012911770) in Zendesk help.

### Available properties

You can use the following properties in the Custom page template.

Name| Type| Description
---|---|---
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object
signed_in| boolean| Whether the user is logged in or not
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

### Available helpers

You can use any [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers).

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)