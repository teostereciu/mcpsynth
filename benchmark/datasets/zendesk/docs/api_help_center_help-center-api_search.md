# Search

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/search/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/search/#json-format)
  * [Unified Search](/api-reference/help_center/help-center-api/search/#unified-search)
  * [Search Articles](/api-reference/help_center/help-center-api/search/#search-articles)
  * [Search Posts](/api-reference/help_center/help-center-api/search/#search-posts)


# Search

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/search/#json-format)
  * [Unified Search](/api-reference/help_center/help-center-api/search/#unified-search)
  * [Search Articles](/api-reference/help_center/help-center-api/search/#search-articles)
  * [Search Posts](/api-reference/help_center/help-center-api/search/#search-posts)


The Help Center API has three different search endpoints. The [Search Articles](/api-reference/help_center/help-center-api/search/#search-articles) and [Search Posts](/api-reference/help_center/help-center-api/search/#search-posts) endpoints enable you to search for articles and posts respectively. The [Unified Search](/api-reference/help_center/help-center-api/search/#unified-search) endpoint allows you to search across articles, posts, and external content in a single query.

#### Authentication

The Search Articles and Search Posts endpoints allow unauthenticated requests. However, requests from JavaScript clients will fail because of clients' [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). In that case, client requests can be authenticated using an OAuth access token. For more information, see [Making client-side CORS requests to the Ticketing API](/documentation/ticketing/using-the-zendesk-api/making-cross-origin-browser-side-api-requests/).

Requests to the Unified Search endpoint must be authenticated. Also, the endpoint doesn't implement a Cross-Origin Resource Sharing (CORS) policy that would let a JavaScript client access its resources from other domains.

### JSON format

Search are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
results| array| false| true| An array with the base articles or community posts

### Unified Search

  * `GET /api/v2/guide/search?filter[locales]={filter[locales]}`


Use the Unified Search endpoint to search for knowledge base articles, community posts, and [external records](https://developer.zendesk.com/api-reference/help_center/federated-search/introduction/).

The only mandatory parameter is `filter[locales]`. You can add other parameters to narrow down the search result set.

If you specify an invalid locale or a locale that's not enabled for any of your account's help centers, no search results are returned. You can check for valid locales with the following API: [List all enabled locales and default locale](https://developer.zendesk.com/api-reference/help_center/help-center-api/translations/#list-enabled-locales-and-default-locale).

If the `query` parameter is used, results are sorted by relevance according to the rules described in [About Help Center End User Search](https://support.zendesk.com/hc/en-us/articles/4408894061338-About-Help-Center-end-user-search) in Zendesk help. If the `query` parameter is not used, results are sorted using an internal ordering.

#### Pagination

This API only supports cursor-based pagination. See [Using cursor based pagination](https://developer.zendesk.com/api-reference/help_center/help-center-api/introduction/#using-cursor-based-pagination) in the Help Center API docs. Currently, this API does not support backwards pagination.

The endpoint returns a default number of 10 results per page. It can return a maximum of 50 records per page.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[brand_ids]| string| Query| false| Limit the search to articles or posts within these brands. If no brand is specified, results are returned across all brands. If you want to scope the result of your search with multiple brands, separate each value with a comma
filter[category_ids]| string| Query| false| Limit the search to articles in these categories. See Filtering by Category
filter[content_types]| string| Query| false| Limit the search to one of these content types: ARTICLE, POST. At present, it is not possible to specify `EXTERNAL_RECORD`. Instead, use the `filter[external_source_id]` parameter above
filter[external_source_ids]| string| Query| false| Use this parameter to scope the result of your search to a specific external source or external sources. If no external source is given, results are returned across all sources
filter[locales]| string| Query| true| Limit the search to these locales. See Filtering by Locale
filter[section_ids]| string| Query| false| Limit the search to articles in these sections. See Filtering by Section
filter[topic_ids]| string| Query| false| Limit the search to posts in these topics. See Filtering by Topic
page[after]| string| Query| false| A string representing the cursor to the next page.
page[size]| integer| Query| false| A numeric value that indicates the maximum number of items that can be included in a response. The value of this parameter has an upper limit of 50. The default value is 10.
query| string| Query| false| The search text to be matched or a search string

#### Code Samples

**curl**


    # Use commas to separate multiple parameter values. Example:# query=print,orderscurl -G "https://{subdomain}.zendesk.com/api/v2/guide/search" \  --data-urlencode "query=Printing" \  --data-urlencode "filter[locales]=en-us,en-gb" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/search?filter[brand_ids]=73%2C67&filter[category_ids]=42%2C43&filter[content_types]=ARTICLE%2CPOST&filter[external_source_ids]=01EC05A5T1J4ZSDJX4Q8JGFRHP&filter[locales]=en-us%2Cen-gb&filter[section_ids]=42%2C43&filter[topic_ids]=42%2C43&page[after]=&page[size]=&query=carrot"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/search")		.newBuilder()		.addQueryParameter("filter[brand_ids]", "73,67")		.addQueryParameter("filter[category_ids]", "42,43")		.addQueryParameter("filter[content_types]", "ARTICLE,POST")		.addQueryParameter("filter[external_source_ids]", "01EC05A5T1J4ZSDJX4Q8JGFRHP")		.addQueryParameter("filter[locales]", "en-us,en-gb")		.addQueryParameter("filter[section_ids]", "42,43")		.addQueryParameter("filter[topic_ids]", "42,43")		.addQueryParameter("page[after]", "")		.addQueryParameter("page[size]", "")		.addQueryParameter("query", "carrot");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/guide/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[brand_ids]': '73%2C67',    'filter[category_ids]': '42%2C43',    'filter[content_types]': 'ARTICLE%2CPOST',    'filter[external_source_ids]': '01EC05A5T1J4ZSDJX4Q8JGFRHP',    'filter[locales]': 'en-us%2Cen-gb',    'filter[section_ids]': '42%2C43',    'filter[topic_ids]': '42%2C43',    'page[after]': '',    'page[size]': '',    'query': 'carrot',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/search?filter[brand_ids]=73%2C67&filter[category_ids]=42%2C43&filter[content_types]=ARTICLE%2CPOST&filter[external_source_ids]=01EC05A5T1J4ZSDJX4Q8JGFRHP&filter[locales]=en-us%2Cen-gb&filter[section_ids]=42%2C43&filter[topic_ids]=42%2C43&page[after]=&page[size]=&query=carrot"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/search")uri.query = URI.encode_www_form("filter[brand_ids]": "73,67", "filter[category_ids]": "42,43", "filter[content_types]": "ARTICLE,POST", "filter[external_source_ids]": "01EC05A5T1J4ZSDJX4Q8JGFRHP", "filter[locales]": "en-us,en-gb", "filter[section_ids]": "42,43", "filter[topic_ids]": "42,43", "page[after]": "", "page[size]": "", "query": "carrot")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "WzEuMCwxNjld",    "before_cursor": "WzEuMCwxNjhd",    "has_more": true  },  "results": [    {      "title": "How to make fish stew",      "type": "ARTICLE",      "updated_at": "2021-10-11T15:02:22Z",      "url": "http://example.zendesk.com/hc/en-us/articles/38393937-How-to-make-fish-stew"    },    {      "title": "Latest updates on fish stew",      "type": "EXTERNAL_RECORD",      "updated_at": "2021-11-12T15:02:22Z",      "url": "http://example.com/blog/fish-stew-latest"    }  ]}

### Search Articles

  * `GET /api/v2/help_center/articles/search`


Returns a default number of 25 articles per page, up to a maximum of 1000 results. See [Pagination](/api-reference/introduction/pagination/). The `per_page` parameter, if provided, must be an integer between 1 and 100.

The `page` parameter, if provided, must be an integer greater than 0.

The results are sorted by relevance by default. You can also sort the results by `created_at` or `updated_at`.

The [article objects](/api-reference/help_center/help-center-api/articles) returned by the search endpoint contain two additional properties:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
result_type| string| yes| no| For articles, always the string "article"
snippet| string| yes| no| The portion of an article that is relevant to the search query, with matching words or phrases delimited by `<em></em>` tags. Example: a query for "carrot potato" might return the snippet "...don't confuse `<em>`carrots`</em>` with `<em>`potatoes`</em>`..."

You must specify at least one of the following parameters in your request:

  * query
  * category
  * section
  * label_names


#### Pagination

  * Offset pagination only


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 articles per page.

#### Allowed for

  * Anonymous users


#### Filtering by Date

You can filter the search results by the creation or update date with the following parameters:

  * created_before
  * created_after
  * created_at
  * updated_before
  * updated_after
  * updated_at


`GET /api/v2/help_center/articles/search.json?query={search_string}&updated_after=2014-01-01&updated_before=2014-02-01`

When filtering by `updated_*`, the results might not always match the `updated_at` timestamps for the documents returned. The reason is that not all updates are propagated to the search index. Only updates that are meaningful for search, such as content changes, are re-indexed. As a result, it's possible for an article to have an `updated_at` timestamp of "2019-10-31" but be returned in a search with the filter `updated_before=2019-08-01` if no meaningful content changes have been made to the article.

#### Filtering by Labels

If you want to search for articles with specific labels, use the `label_names` parameter and pass a comma-separated list of label names to filter the results:

`GET /api/v2/help_center/articles/search.json?label_names=photos,camera`

An article must have at least one of the labels to match. Also, matching is not case-sensitive. For example, 'camera' matches both 'Camera' and 'camera'.

This feature is only available on Professional and Enterprise.

#### Filtering by Locale

By default, searches are carried out in the default language specified in the Help Center settings. Use the `locale` parameter to search for articles in another language.

`GET /api/v2/help_center/articles/search.json?query={search_string}&locale={locale}`

If you specify an invalid locale or a locale that's not enabled for Help Center, the default locale for the account is used for the search. You can check for valid locales with the API. See [List all enabled locales and default locale](/api-reference/help_center/help-center-api/translations#list-all-enabled-locales-and-default-locale).

If you use `locale=*`, search is carried out across all valid locales and returns all article translations in all languages, that match the search criteria.

#### Filtering by Category

If you want to scope the result of your search within a given category, use the `category` parameter.

`GET /api/v2/help_center/articles/search.json?query={search_string}&category={category_id}`

If you want to scope the result of your search with multiple categories, use the `category` parameter as above and separate each value with a comma.

`GET /api/v2/help_center/articles/search.json?query={search_string}&category={category_id},{another_category_id}`

#### Filtering by Section

If you want to scope the result of your search within a given section, use the `section` parameter.

`GET /api/v2/help_center/articles/search.json?query={search_string}&section={section id}`

If you want to scope the result of your search with multiple sections, use `section` parameter as above and separate each value with a comma.

`GET /api/v2/help_center/articles/search.json?query={search_string}&section={section_id},{another_section_id}`

#### Filtering by Brand

Use the `multibrand` parameter to search across all brands, or `brand_id` to scope the result of your search to a specific brand.

`GET /api/v2/help_center/articles/search.json?query={search_string}&brand_id={brand_id}`

`GET /api/v2/help_center/articles/search.json?query={search_string}&multibrand=true`

If you use `multibrand=true` in your request and no `brand_id`, search will return results from all brands that match the query criteria. If you use `brand_id` in your request, the search results will be scoped to the specified brand, regardless of the use of the `multibrand` parameter.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Query| false| Search for articles in the specified brand.
category| integer| Query| false| Limit the search to this category id. See Filtering by Category
created_after| string| Query| false| Limit the search to articles created after a given date (format YYYY-MM-DD).
created_at| string| Query| false| Limit the search to articles created on a given date (format YYYY-MM-DD).
created_before| string| Query| false| Limit the search to articles created before a given date (format YYYY-MM-DD).
label_names| string| Query| false| A comma-separated list of label names. See Filtering by Labels
locale| string| Query| false| Search for articles in the specified locale. See Filtering by Locale
multibrand| boolean| Query| false| Enable search across all brands if true. Defaults to false if omitted.
query| string| Query| false| The search text to be matched or a search string. Examples: "carrot potato", "'carrot potato'".
section| integer| Query| false| Limit the search to this section id. See Filtering by Section
sort_by| string| Query| false| One of created_at or updated_at. Defaults to sorting by relevance
sort_order| string| Query| false| One of asc or desc. Defaults to desc
updated_after| string| Query| false| Limit the search to articles updated after a given date (format YYYY-MM-DD).
updated_at| string| Query| false| Limit the search to articles updated on a given date (format YYYY-MM-DD).
updated_before| string| Query| false| Limit the search to articles updated before a given date (format YYYY-MM-DD).

#### Code Samples

**curl**


    # Use commas to separate multiple search terms. Example:# query=print,orderscurl "https://{subdomain}.zendesk.com/api/v2/help_center/articles/search.json \  --data-urlencode "que/token:{api_token}" \  --data-urlencode "updated_after=2024-01-01" \  --data-urlencode "updated_before=2024-02-01" \  -v -u {email_address}:{password}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/search?brand_id=&category=&created_after=&created_at=&created_before=&label_names=&locale=&multibrand=&query=&section=&sort_by=&sort_order=&updated_after=&updated_at=&updated_before="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/search")		.newBuilder()		.addQueryParameter("brand_id", "")		.addQueryParameter("category", "")		.addQueryParameter("created_after", "")		.addQueryParameter("created_at", "")		.addQueryParameter("created_before", "")		.addQueryParameter("label_names", "")		.addQueryParameter("locale", "")		.addQueryParameter("multibrand", "")		.addQueryParameter("query", "")		.addQueryParameter("section", "")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "")		.addQueryParameter("updated_after", "")		.addQueryParameter("updated_at", "")		.addQueryParameter("updated_before", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'brand_id': '',    'category': '',    'created_after': '',    'created_at': '',    'created_before': '',    'label_names': '',    'locale': '',    'multibrand': '',    'query': '',    'section': '',    'sort_by': '',    'sort_order': '',    'updated_after': '',    'updated_at': '',    'updated_before': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/search?brand_id=&category=&created_after=&created_at=&created_before=&label_names=&locale=&multibrand=&query=&section=&sort_by=&sort_order=&updated_after=&updated_at=&updated_before="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/search")uri.query = URI.encode_www_form("brand_id": "", "category": "", "created_after": "", "created_at": "", "created_before": "", "label_names": "", "locale": "", "multibrand": "", "query": "", "section": "", "sort_by": "", "sort_order": "", "updated_after": "", "updated_at": "", "updated_before": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "results": [    {      "author_id": 888887,      "draft": false,      "id": 35467,      "locale": "en",      "permission_group_id": 123,      "title": "Printing orders",      "user_segment_id": 12    }  ]}

### Search Posts

  * `GET /api/v2/help_center/community_posts/search?query={query}`


Returns a maximum of 25 posts per page, up to a maximum of 1000 results. See [Pagination](/api-reference/introduction/pagination/).

The results are sorted by relevance by default. You can also sort the results by `created_at` or `updated_at`.

#### Pagination

  * Offset pagination only


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 articles per page.

#### Allowed for

  * End users


#### Filtering by Date

You can filter the search results by the creation or update date with the following parameters:

  * created_before
  * created_after
  * created_at
  * updated_before
  * updated_after
  * updated_at


`GET /api/v2/community/posts/search.json?query={search_string}&updated_after=2014-01-01&updated_before=2014-02-01`

#### Filtering by Topic

If you want to scope the result of your search within a given topic, use the `topic` parameter.

`GET /api/v2/community/posts/search.json?query={search_string}&topic={topic id}`

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
created_after| string| Query| false| Search posts created after a given date (format YYYY-MM-DD)
created_at| string| Query| false| Search posts created on a given date (format YYYY-MM-DD)
created_before| string| Query| false| the search to posts created before a given date (format YYYY-MM-DD)
query| string| Query| true| Search text to be matched or a search string. Examples: "carrot potato", "''carrot potato''"'
sort_by| string| Query| false| Sort by `created_at` or `updated_at`. Defaults to sorting by relevance
sort_order| string| Query| false| Sort in ascending or descending order. Default is descending order.
topic| integer| Query| false| Search by topic ID. See Filtering by Topic
updated_after| string| Query| false| Search posts updated after a given date (format YYYY-MM-DD)
updated_at| string| Query| false| Search posts updated on a given date (format YYYY-MM-DD)
updated_before| string| Query| false| Search posts updated before a given date (format YYYY-MM-DD)

#### Code Samples

**curl**


    # Use commas to separate multiple search terms. Example:# query=print,orderscurl "https://{subdomain}.zendesk.com/api/v2/help_center/community_posts/search.json \  --data-urlencode "que/token:{api_token}string}" \  -v -u {email_address}:{password}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/community_posts/search?created_after=&created_at=&created_before=&query=help+center&sort_by=&sort_order=&topic=&updated_after=&updated_at=&updated_before="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/community_posts/search")		.newBuilder()		.addQueryParameter("created_after", "")		.addQueryParameter("created_at", "")		.addQueryParameter("created_before", "")		.addQueryParameter("query", "help center")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "")		.addQueryParameter("topic", "")		.addQueryParameter("updated_after", "")		.addQueryParameter("updated_at", "")		.addQueryParameter("updated_before", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/community_posts/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'created_after': '',    'created_at': '',    'created_before': '',    'query': 'help+center',    'sort_by': '',    'sort_order': '',    'topic': '',    'updated_after': '',    'updated_at': '',    'updated_before': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/community_posts/search?created_after=&created_at=&created_before=&query=help+center&sort_by=&sort_order=&topic=&updated_after=&updated_at=&updated_before="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/community_posts/search")uri.query = URI.encode_www_form("created_after": "", "created_at": "", "created_before": "", "query": "help center", "sort_by": "", "sort_order": "", "topic": "", "updated_after": "", "updated_at": "", "updated_before": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "results": [    {      "author_id": 4333787,      "id": 4212256,      "title": "How do I make a return?"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)