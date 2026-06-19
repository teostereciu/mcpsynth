# Scenario Solutions (eBay Commerce MCP)

## Environment setup

- Set `EBAY_ACCESS_TOKEN` to a valid OAuth token.
- Optional:
  - `EBAY_SANDBOX=true` to use sandbox hosts.
  - `EBAY_API_BASE` / `EBAY_APIM_BASE` to override base URLs.

---

## Scenario 1: Find a product in the eBay catalog and fetch full details

1) Search product summaries:
- Tool: `catalog_search_product_summaries`
- Inputs: `q="iphone 14"`, `marketplace_id="EBAY_US"`, optional `limit`

2) Pick a `productId` from results and fetch details:
- Tool: `catalog_get_product`
- Inputs: `product_id=<productId>`, `marketplace_id="EBAY_US"`

---

## Scenario 2: Determine the best category and required aspects for a listing

1) Get default category tree for marketplace:
- Tool: `taxonomy_get_default_category_tree_id`
- Inputs: `marketplace_id="EBAY_US"`

2) Get category suggestions:
- Tool: `taxonomy_get_category_suggestions`
- Inputs: `category_tree_id=<id>`, `query="wireless earbuds"`

3) For a suggested leaf category, fetch aspects:
- Tool: `taxonomy_get_item_aspects_for_category`
- Inputs: `category_tree_id=<id>`, `category_id=<leafCategoryId>`

---

## Scenario 3: Look up a charity and retrieve details

1) Search charities:
- Tool: `charity_search_charity_orgs`
- Inputs: `marketplace_id="EBAY_US"`, `q="red cross"`

2) Fetch details:
- Tool: `charity_get_charity_org`
- Inputs: `marketplace_id="EBAY_US"`, `charity_org_id=<id>`

---

## Scenario 4: Create notification destination and subscribe to a topic

1) Create destination:
- Tool: `notification_create_destination`
- Inputs: `name`, `endpoint` (HTTPS), `verificationToken`

2) List destinations (optional):
- Tool: `notification_get_destinations`

3) Create subscription:
- Tool: `notification_create_subscription`
- Inputs: `topicId`, `status`, `destinationId`, `payload`

4) Update subscription:
- Tool: `notification_update_subscription`
- Inputs: `subscription_id`, `status`, `destinationId`, `payload`

---

## Scenario 5: Upload media for listings

- Create a document from URL:
  - Tool: `media_create_document_from_url`
  - Inputs: `documentType`, `documentUrl`, `languages`

- Create a video resource:
  - Tool: `media_create_video`
  - Inputs: `title`, `size`, `classification`, optional `description`

- Create an image from a file:
  - Tool: `media_create_image_from_file`
  - Inputs: `file_base64`, `file_name`

---

## Scenario 6: Translate text

- Tool: `translation_translate`
- Inputs: `from_="en"`, `to="de"`, `text="Brand new sealed"`

---

## Scenario 7: Call an endpoint not wrapped by a dedicated tool

- Tool: `ebay_raw_request`
- Example inputs:
  - `method="GET"`
  - `host="api"`
  - `path="commerce/taxonomy/v1/category_tree/0"`
  - `params={...}`
  - `headers={...}`
