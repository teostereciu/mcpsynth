# New Request page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/new_request_page/*

---

## On this page

  * [New Request page](/api-reference/help_center/help-center-templates/new_request_page/#new-request-page)
  * [Available properties](/api-reference/help_center/help-center-templates/new_request_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/new_request_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/new_request_page/#example)


# New Request page

## On this page

  * [New Request page](/api-reference/help_center/help-center-templates/new_request_page/#new-request-page)
  * [Available properties](/api-reference/help_center/help-center-templates/new_request_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/new_request_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/new_request_page/#example)


## New Request page

The New Request page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/requests/new`.

### Available properties

You can use the following properties in the New Request page template.

Name| Type| Description
---|---|---
parent| object| A [request](/api-reference/help_center/help-center-templates/objects#request-object) object that represents a related closed request. It may or may not exist
new_request_form| object| A [new request form](/api-reference/help_center/help-center-templates/objects#new-request-form-object) object containing information about the new request form. Available only from Templating API v4 and above
answer_bot| object| An [answer_bot](/api-reference/help_center/help-center-templates/objects#answer-bot-object) object that holds information about Answer Bot. Available only from Templating API v4 and above
answer_bot_generative_experience| object| An [answer_bot_generative_experience](/api-reference/help_center/help-center-templates/objects#answer-bot-generative-experience-object) object containing the required fields for the generative AI response experience
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user
path_steps| array| An array of [path_step](/api-reference/help_center/help-center-templates/objects#path_step-object) objects

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the Request List page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
follow_up| Link to the parent request, if it exists. See [follow_up helper](/api-reference/help_center/help-center-templates/advanced_helpers#follow_up-helper). Not available from Templating API v4 and above
request_form| The request form. See [request_form helper](/api-reference/help_center/help-center-templates/advanced_helpers#request_form-helper). Not available from Templating API v4 and above

### Example

#### Templating API v3


    <nav class="sub-nav">  {{breadcrumbs}}  {{search}}</nav>
    <h1 class="page-header">  {{t 'submit_a_request'}}  {{#if parent}}    <span class="follow-up-hint">      {{follow_up}}    </span>  {{/if}}</h1>
    <div class="form">  {{request_form}}</div>

#### Templating API v4

In Templating API v4, the `new_request_form` object is available. You can use it to render a custom form. Refer to the implementation in the standard [Copenhagen theme](https://github.com/zendesk/copenhagen_theme) for guidance.

When the New Request page is accessed, the `answer_bot` object has an empty `articles` array and null values for the other properties. If Answer Bot is enabled and suggested articles are found, the page is reloaded with the `answer_bot` object populated. The information provided can be used to render the UI showing the suggested articles and interact with the [Article Feedback APIs](/api-reference/answer-bot/answer-bot-api/article_feedback/).

The `answer_bot_generative_experience` object can be used instead of the `answer_bot` object. When a user submits a request through the web form, the object displays a generative answer, if a suitable one can be found, that attempts to resolve the user's request directly. This replaces the article suggestion experience, if both are active at the same time.

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)