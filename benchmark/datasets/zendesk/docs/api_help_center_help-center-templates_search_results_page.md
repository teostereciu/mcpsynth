# Search Results page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/search_results_page/*

---

## On this page

  * [Search Results page](/api-reference/help_center/help-center-templates/search_results_page/#search-results-page)
  * [Available properties](/api-reference/help_center/help-center-templates/search_results_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/search_results_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/search_results_page/#example)


# Search Results page

## On this page

  * [Search Results page](/api-reference/help_center/help-center-templates/search_results_page/#search-results-page)
  * [Available properties](/api-reference/help_center/help-center-templates/search_results_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/search_results_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/search_results_page/#example)


## Search Results page

The Search Results page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/search`.

### Available properties

You can use the following properties in the search results template.

Name| Type| Description
---|---|---
query| string| The searched query
results_count| integer| The number of results of the search
results| array| An array of [search result](/api-reference/help_center/help-center-templates/objects#search-result-object) objects containing all the article and post results from the knowledge base and community
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
help_center_filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter) objects. Use these filters to iterate through help centers when searching multiple help centers
source_filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter) objects. Use these filters to iterate through help centers and external sources when searching multiple help centers and/or external sources
type_filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter) objects. Use these filters to iterate through content types (articles, posts or external types) when searching across multiple content types
filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter) objects
subfilters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter) objects. Use these filters to drill down into the search results categories (for knowledge base results) or topics (for community posts)
content_tag_filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter) objects. Use these filters to iterate through content tags when searching by them. Searching by multiple content tags isn't supported
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user
path_steps| array| An array of [path_step](/api-reference/help_center/help-center-templates/objects#path_step-object) objects

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the search page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
generative_answers| Quick answers box that displays AI-generated answers to the user's question. See [generative answers helper](/api-reference/help_center/help-center-templates/advanced_helpers/#generative_answers-helper)

### Example


    <nav class="sub-nav sub-nav-far clearfix">  {{breadcrumbs}}  {{search}}</nav>
    <div class="search-results clearfix">  <h1>{{results_count}} results found</h1>
      {{#each help_center_filters}}    <li>      <a href="{{url}}">{{name}} ({{count}})</a>    </li>  {{/each}}
      {{#each filters}}    <li>      <a href="{{url}}">{{name}} ({{count}})</a>    </li>  {{/each}}
      {{#each subfilters}}    <li>      <a href="{{url}}">{{name}} ({{count}})</a>    </li>  {{/each}}
      {{#each results}}    <div>      <a href="{{url}}">{{title}}</a>      <p class="search-result-description">{{text}}</p>    </div>  {{/each}}
    </div>
    {{pagination}}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)