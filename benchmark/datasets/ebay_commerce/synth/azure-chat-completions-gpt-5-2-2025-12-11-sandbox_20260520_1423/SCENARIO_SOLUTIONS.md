# Scenario Solutions (eBay Commerce MCP)

## Environment setup

Set:
- `EBAY_OAUTH_TOKEN` (required): OAuth access token (Authorization Code grant) with appropriate scopes.
- `EBAY_API_BASE_URL` (optional): defaults to `https://apim.ebay.com`.

Run:

```bash
pip install -r requirements.txt
python server.py
```

---

## Scenario 1: Find a product and fetch full details

1) Search product summaries:
- Tool: `catalog_search_product_summaries`
- Inputs: `q`, optionally `limit`, `offset`, `x_ebay_c_marketplace_id`

2) From results, pick an `epid` (ePID) and fetch full product:
- Tool: `catalog_get_product`
- Inputs: `ep_id`

---

## Scenario 2: Determine the best category for an item and required aspects

1) Get default category tree for a marketplace:
- Tool: `taxonomy_get_default_category_tree_id`
- Input: `marketplace_id` (e.g., `EBAY_US`)

2) Get category suggestions:
- Tool: `taxonomy_get_category_suggestions`
- Inputs: `category_tree_id`, `q`

3) For a chosen category, get required/recommended aspects:
- Tool: `taxonomy_get_item_aspects_for_category`
- Inputs: `category_tree_id`, `category_id`

---

## Scenario 3: Upload an image to EPS for use in a listing

Option A (URL):
- Tool: `media_create_image_from_url`
- Input: `image_url` (must be HTTPS)

Option B (file):
- Tool: `media_create_image_from_file`
- Inputs: `file_path` OR (`file_b64` + `filename`)

Then retrieve details (including EPS URL):
- Tool: `media_get_image`
- Input: `image_id`

---

## Scenario 4: Upload a document and check processing status

1) Create a document ID:
- Tool: `media_create_document`
- Inputs: `document_type`, `languages`

2) Upload the file:
- Tool: `media_upload_document`
- Inputs: `document_id`, `file_path` OR (`file_b64` + `filename`)

3) Poll status:
- Tool: `media_get_document`
- Input: `document_id`

---

## Scenario 5: Configure and test notifications

1) Create a destination:
- Tool: `notification_create_destination`
- Input: `payload` (destination definition)

2) Create a subscription:
- Tool: `notification_create_subscription`
- Input: `payload` (topic + destination + format)

3) Test subscription delivery:
- Tool: `notification_test_subscription`
- Input: `subscription_id`

4) Retrieve public key for signature validation:
- Tool: `notification_get_public_key`

---

## Scenario 6: Translate text

- Tool: `translation_translate`
- Input: `payload` (per Translation API docs; includes source/target language and text fields)
