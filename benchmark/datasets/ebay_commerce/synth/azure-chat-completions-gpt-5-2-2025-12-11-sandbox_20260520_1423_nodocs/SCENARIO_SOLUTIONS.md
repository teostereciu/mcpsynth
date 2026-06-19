# Scenario Solutions (eBay Commerce MCP)

## Scenario 1: Find a product in the catalog and inspect details

1. Call `catalog_search` with a query:
   - `q`: e.g. "iphone 14 pro"
   - optional: `category_ids`
2. From results, pick a `productId` (EPID).
3. Call `catalog_get_product` with that EPID to retrieve full product details.

## Scenario 2: Determine category and required aspects for listing

1. Call `taxonomy_get_default_category_tree` with `marketplace_id` (e.g. `EBAY_US`).
2. Call `taxonomy_get_category_suggestions` with the returned `categoryTreeId` and your query.
3. Choose a `categoryId`.
4. Call `taxonomy_get_item_aspects_for_category` to get required/optional aspects.

## Scenario 3: Translate listing text

1. Call `translation_translate` with:
   - `from_lang`: e.g. `en`
   - `to_lang`: e.g. `de`
   - `text`: your title/description

## Scenario 4: Upload an image to eBay Media

1. Base64-encode the image bytes.
2. Call `media_upload_image` with:
   - `image_base64`: base64 string
   - `content_type`: e.g. `image/jpeg` or `image/png`
3. Use the returned image URL/ID in downstream listing flows (