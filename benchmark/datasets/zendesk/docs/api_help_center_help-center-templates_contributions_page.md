# Contributions page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/contributions_page/*

---

## On this page

  * [Contributions page](/api-reference/help_center/help-center-templates/contributions_page/#contributions-page)
  * [Available properties](/api-reference/help_center/help-center-templates/contributions_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/contributions_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/contributions_page/#example)


# Contributions page

## On this page

  * [Contributions page](/api-reference/help_center/help-center-templates/contributions_page/#contributions-page)
  * [Available properties](/api-reference/help_center/help-center-templates/contributions_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/contributions_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/contributions_page/#example)


## Contributions page

The Contributions page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/contributions/comments`, `https://{yoursubdomain}.zendesk.com/hc/contributions/posts` or `https://{yoursubdomain}.zendesk.com/hc/contributions/community_comments`.

### Available properties

You can use the following properties in the Contributions page template.

Name| Type| Description
---|---|---
current_filter| object| The current [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object
contributions| array| An array of [contribution](/api-reference/help_center/help-center-templates/objects#contribution-object) objects, filtered by `current_filter`
filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects for the page
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
breadcrumbs| Breadcrumbs for the Contributions page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)

### Example


    <header class="my-activities-header">  {{breadcrumbs}}</header>
    <nav class="my-activities-sub-nav nav-bordered">  <ul>    {{#each filters}}      <li>        {{#if selected}}          {{name}}        {{else}}          <a href="{{url}}">{{name}}</a>        {{/if}}      </li>    {{/each}}  </ul></nav>
    <div class="contributions-list">  <ul>  {{#each contributions}}    <li>      <a href="{{url}}">        {{title}} ({{type}})      </a>    </li>  {{/each}}  </ul></div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)