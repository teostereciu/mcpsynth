# findListingRecommendations

The <b>find</b> method currently returns information for a single recommendation type (<code>AD</code>) which contains information that sellers can use to configure <a href="/api-docs/sell/static/marketing/promoted-listings.html" title="Selling Integration Guide">Promoted Listings</a> ad campaigns. <p>The response from this method includes an array of the seller's listing IDs, where each element in the array contains recommendations related to the associated listing ID. For details on how to use this method, see <a href="/api-docs/sell/static/marketing/pl-reco-api.html" title="Selling Integration Guide">Using the Recommendation API to help configure campaigns</a>.</p>  <h3>The AD recommendation type</h3>  </p>  <p>The <code>AD</code> type contains two sets of information:</p>  <ul><li><b>The promoteWithAd indicator</b> <br>The <b>promoteWithAd</b> response field indicates whether or not eBay recommends you place the associated listing in a Promoted Listings ad campaign. <p>The returned value is set to either <code>RECOMMENDED</code> or <code>UNDETERMINED</code>, where <code>RECOMMENDED</code> identifies the listings that will benefit the most from having them included in an ad campaign.</p></li>  <li><b>The bid percentage</b> <br>Also known as the "ad rate," the <b>bidPercentage</b> field provides the current trending bid percentage of similarly promoted items in the marketplace. <p>The ad rate is a user-specified value that indicates the level of promotion that eBay applies to the campaign across the marketplace. The value is also used to calculate the Promotion Listings fee, which is assessed to the seller if a Promoted Listings action results in the sale of an item.</p></li></ul>  <h3>Configuring the request</h3> <p>You can configure a request to review all of a seller's currently active listings, or just a subset of them.</p>  <ul><li><b>All active listings</b> &ndash; If you leave the request body empty, the request targets <i>all</i> the items currently listed by the seller. <p>Here, the response is filtered to contain only the items where <b>promoteWithAd</b> equals <code>RECOMMENDED</code>. In this case, eBay recommends that all the returned listings should be included in a Promoted Listings ad campaign.</p></li> <li><b>Selected listing IDs</b> &ndash; If you populate the request body with a set of <b>listingIds</b>, the response contains data for all the specified listing IDs. <p>In this scenario, the response provides you with information on listings where the <b>promoteWithAd</b> can be either <code>RECOMMENDED</code> or <code>UNDETERMINED</code>.</li></ul>  <h3>The paginated response</h3>  <p>Because the response can contain many listing IDs, the <b>findListingRecommendations</b> method paginates the response set.</p> <p>You can control size of the returned pages, as well as an offset that dictates where to start the pagination, using query parameters in the request.

## Endpoint

```
POST /find
```

## API

Recommendation API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **filter**: Provide a list of key-value pairs to specify the criteria you want to use to filter the response.  <br><br>In the list, separate each filter key from its associated value with a colon ("<code>:</code>").  <br><br>Currently, the only supported filter value is <b>recommendationTypes</b> and it supports only the ("<code>AD</code>") type. Follow the <b>recommendationTypes</b> specifier with the filter type(s) enclosed in curly braces ("<code>{ }</code>"), and separate multiple types with commas.  <br><br><b>Example:</b> <code>filter=recommendationTypes:{AD}</code>  <br><br><b>Default:</b> <code>recommendationTypes:{AD}</code> (Type: `string`)
- **limit**: Use this query parameter to set the maximum number of ads to return on a page from the paginated response.  <br><br><b>Default: </b>10 <br><b>Maximum:</b> 500 (Type: `string`)
- **offset**: Specifies the number of ads to skip in the result set before returning the first ad in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set.</p> <p><b>Default:</b> 0</p> (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header specifies the eBay marketplace where you list the items for which you want to get recommendations.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl" target="_blank">HTTP Request Headers</a> for a list of supported eBay marketplace ID values. (Type: `string`)

### Request Body

See schema: `#/components/schemas/FindListingRecommendationRequest`


## Response

**200**: Success

**204**: No Content

## Example

```bash
curl -X POST \
  https://api.ebay.com/find \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

listing_recommendation

## Reference

- [eBay Recommendation API Documentation](https://developer.ebay.com/api-docs/sell/recommendation/overview.html)
