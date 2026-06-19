# eBay Buy API MCP Server - Tools Reference

Complete reference of all 28 tools available in the MCP server.

## Browse API (7 tools)

### 1. search_items
**Endpoint**: `GET /buy/browse/v1/item_summary/search`

Search for items by keyword or category with optional filtering and sorting.

**Parameters**:
- `q` (string, required): Search query/keyword
- `category_ids` (string, optional): Comma-separated category IDs
- `limit` (integer, default 50): Max results (1-200)
- `offset` (integer, default 0): Pagination offset
- `sort` (string, optional): Sort order (e.g., "price", "-price", "newlyListed")
- `filter` (string, optional): Filter expression (e.g., "price:[100..500]")

**Returns**: Search results with item summaries

**Example**:
```python
search_items(q="laptop", filter="price:[500..1500]", limit=20)
```

---

### 2. search_items_by_image
**Endpoint**: `POST /buy/browse/v1/item_summary/search_by_image`

Find items using image-based search.

**Parameters**:
- `image_url` (string, required): URL of the image to search with
- `limit` (integer, default 50): Max results

**Returns**: Search results with matching items

**Example**:
```python
search_items_by_image(image_url="https://example.com/image.jpg", limit=10)
```

---

### 3. get_item
**Endpoint**: `GET /buy/browse/v1/item/{item_id}`

Get detailed information about a specific item.

**Parameters**:
- `item_id` (string, required): eBay item ID (e.g., "v1|123456789|0")
- `fieldgroups` (string, optional): Comma-separated field groups
  - `COMPACT`: Minimal fields
  - `PRODUCT`: Product information
  - `ADDITIONAL_SELLER_DETAILS`: Seller details
  - `CHARITY_DETAILS`: Charity information

**Returns**: Detailed item information

**Example**:
```python
get_item(item_id="v1|123456789|0", fieldgroups="PRODUCT,ADDITIONAL_SELLER_DETAILS")
```

---

### 4. get_item_by_legacy_id
**Endpoint**: `GET /buy/browse/v1/item/get_item_by_legacy_id`

Get item details using a legacy eBay item ID.

**Parameters**:
- `legacy_item_id` (string, required): Legacy eBay item ID
- `legacy_variation_id` (string, optional): Legacy variation ID

**Returns**: Item details

**Example**:
```python
get_item_by_legacy_id(legacy_item_id="123456789")
```

---

### 5. get_items
**Endpoint**: `GET /buy/browse/v1/item`

Get details for multiple items in a single request.

**Parameters**:
- `item_ids` (string, required): Comma-separated item IDs

**Returns**: Details for all requested items

**Example**:
```python
get_items(item_ids="v1|123|0,v1|456|0,v1|789|0")
```

---

### 6. get_items_by_item_group
**Endpoint**: `GET /buy/browse/v1/item/get_items_by_item_group`

Get all variations of an item (item group).

**Parameters**:
- `item_group_id` (string, required): Item group ID

**Returns**: All items in the group

**Example**:
```python
get_items_by_item_group(item_group_id="group123")
```

---

### 7. check_item_compatibility
**Endpoint**: `POST /buy/browse/v1/item/{item_id}/check_compatibility`

Check if an item is compatible with specified parts or vehicles.

**Parameters**:
- `item_id` (string, required): Item ID to check
- `compatibility_payload` (string, required): JSON string with compatibility criteria

**Returns**: Compatibility check results

**Example**:
```python
check_item_compatibility(
    item_id="v1|123456789|0",
    compatibility_payload='{"compatibilityProperties": [{"name": "Make", "value": "BMW"}]}'
)
```

---

## Deal API (4 tools)

### 8. get_deal_items
**Endpoint**: `GET /buy/deal/v1/deal_item`

Get current deal items with optional category filtering.

**Parameters**:
- `category_ids` (string, optional): Comma-separated category IDs
- `limit` (integer, default 20): Max results (1-100)
- `offset` (integer, default 0): Pagination offset

**Returns**: List of current deals

**Example**:
```python
get_deal_items(limit=50)
```

---

### 9. get_event_items
**Endpoint**: `GET /buy/deal/v1/event_item`

Get items associated with specific events.

**Parameters**:
- `event_ids` (string, optional): Comma-separated event IDs
- `limit` (integer, default 20): Max results (1-100)
- `offset` (integer, default 0): Pagination offset

**Returns**: Items associated with events

**Example**:
```python
get_event_items(event_ids="event123,event456", limit=30)
```

---

### 10. get_event
**Endpoint**: `GET /buy/deal/v1/event/{event_id}`

Get details about a specific event.

**Parameters**:
- `event_id` (string, required): Event ID

**Returns**: Event details

**Example**:
```python
get_event(event_id="event123")
```

---

### 11. get_events
**Endpoint**: `GET /buy/deal/v1/event`

Get all current events.

**Parameters**:
- `limit` (integer, default 20): Max results (1-100)
- `offset` (integer, default 0): Pagination offset

**Returns**: List of current events

**Example**:
```python
get_events(limit=100)
```

---

## Feed API (4 tools)

### 12. get_item_feed
**Endpoint**: `GET /buy/feed/v1/item`

Download an item feed file (TSV_GZIP format).

**Parameters**:
- `category_id` (string, required): Category ID for the feed
- `date` (string, required): Date in YYYYMMDD format
- `feed_scope` (string, default "NEWLY_LISTED"): 
  - `NEWLY_LISTED`: Daily feed
  - `ALL_ACTIVE`: Weekly bootstrap feed

**Returns**: Feed file download information

**Example**:
```python
get_item_feed(category_id="15687", date="20240101", feed_scope="NEWLY_LISTED")
```

---

### 13. get_item_group_feed
**Endpoint**: `GET /buy/feed/v1/item_group`

Download an item group feed file.

**Parameters**:
- `category_id` (string, required): Category ID
- `date` (string, required): Date in YYYYMMDD format

**Returns**: Feed file download information

**Example**:
```python
get_item_group_feed(category_id="15687", date="20240101")
```

---

### 14. get_item_priority_feed
**Endpoint**: `GET /buy/feed/v1/item_priority`

Download an item priority feed file.

**Parameters**:
- `category_id` (string, required): Category ID
- `date` (string, required): Date in YYYYMMDD format

**Returns**: Feed file download information

**Example**:
```python
get_item_priority_feed(category_id="15687", date="20240101")
```

---

### 15. get_item_snapshot_feed
**Endpoint**: `GET /buy/feed/v1/item_snapshot`

Download an item snapshot feed file.

**Parameters**:
- `category_id` (string, required): Category ID
- `snapshot_date` (string, required): Snapshot date in YYYYMMDD format

**Returns**: Feed file download information

**Example**:
```python
get_item_snapshot_feed(category_id="15687", snapshot_date="20240101")
```

---

## Marketing API (1 tool)

### 16. get_merchandised_products
**Endpoint**: `GET /buy/marketing/v1/merchandised_product`

Get merchandised products for a category.

**Parameters**:
- `category_id` (string, required): Category ID
- `limit` (integer, default 30): Max results (1-100)

**Returns**: Merchandised products

**Example**:
```python
get_merchandised_products(category_id="15687", limit=50)
```

---

## Offer API (2 tools)

### 17. get_bidding
**Endpoint**: `GET /buy/offer/v1/bidding/{item_id}`

Get bidding information for an auction item.

**Parameters**:
- `item_id` (string, required): Item ID

**Returns**: Bidding information

**Example**:
```python
get_bidding(item_id="v1|123456789|0")
```

---

### 18. place_proxy_bid
**Endpoint**: `POST /buy/offer/v1/bidding/{item_id}/place_proxy_bid`

Place a proxy bid on an auction item.

**Parameters**:
- `item_id` (string, required): Item ID to bid on
- `bid_amount` (string, required): Bid amount (as string for precision)

**Returns**: Bid placement result

**Example**:
```python
place_proxy_bid(item_id="v1|123456789|0", bid_amount="150.00")
```

---

## Order API - Guest Checkout (7 tools)

### 19. initiate_guest_checkout_session
**Endpoint**: `POST /buy/order/v2/guest_checkout_session/initiate`

Initiate a guest checkout session (first step in checkout flow).

**Parameters**:
- `items_payload` (string, required): JSON string with items and shipping address

**Returns**: Checkout session details with session ID

**Example**:
```python
initiate_guest_checkout_session(items_payload='''
{
  "contactEmail": "buyer@example.com",
  "lineItemInputs": [
    {
      "itemId": "v1|123456789|0",
      "quantity": 1
    }
  ],
  "shippingAddress": {
    "addressLine1": "123 Main St",
    "city": "San Jose",
    "stateOrProvince": "CA",
    "postalCode": "95131",
    "country": "US",
    "firstName": "John",
    "lastName": "Doe",
    "phoneNumber": "+14155551234"
  }
}
''')
```

---

### 20. get_guest_checkout_session
**Endpoint**: `GET /buy/order/v2/guest_checkout_session/{checkoutSessionId}`

Get details of a guest checkout session.

**Parameters**:
- `checkout_session_id` (string, required): Checkout session ID

**Returns**: Checkout session details

**Example**:
```python
get_guest_checkout_session(checkout_session_id="session123")
```

---

### 21. apply_guest_coupon
**Endpoint**: `POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/apply_coupon`

Apply a coupon code to a checkout session.

**Parameters**:
- `checkout_session_id` (string, required): Checkout session ID
- `coupon_code` (string, required): Coupon code to apply

**Returns**: Updated checkout session

**Example**:
```python
apply_guest_coupon(checkout_session_id="session123", coupon_code="SAVE10")
```

---

### 22. remove_guest_coupon
**Endpoint**: `POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/remove_coupon`

Remove a coupon from a checkout session.

**Parameters**:
- `checkout_session_id` (string, required): Checkout session ID

**Returns**: Updated checkout session

**Example**:
```python
remove_guest_coupon(checkout_session_id="session123")
```

---

### 23. update_guest_quantity
**Endpoint**: `POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/update_quantity`

Update the quantity of an item in a checkout session.

**Parameters**:
- `checkout_session_id` (string, required): Checkout session ID
- `line_item_id` (string, required): Line item ID to update
- `quantity` (integer, required): New quantity

**Returns**: Updated checkout session

**Example**:
```python
update_guest_quantity(
    checkout_session_id="session123",
    line_item_id="line123",
    quantity=2
)
```

---

### 24. update_guest_shipping_address
**Endpoint**: `POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/update_shipping_address`

Update the shipping address for a checkout session.

**Parameters**:
- `checkout_session_id` (string, required): Checkout session ID
- `address_payload` (string, required): JSON string with address details

**Returns**: Updated checkout session

**Example**:
```python
update_guest_shipping_address(
    checkout_session_id="session123",
    address_payload='''
{
  "address": {
    "addressLine1": "456 Oak Ave",
    "city": "Los Angeles",
    "stateOrProvince": "CA",
    "postalCode": "90001",
    "country": "US",
    "firstName": "Jane",
    "lastName": "Smith",
    "phoneNumber": "+14155559999"
  }
}
'''
)
```

---

### 25. update_guest_shipping_option
**Endpoint**: `POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/update_shipping_option`

Select a shipping option for a checkout session.

**Parameters**:
- `checkout_session_id` (string, required): Checkout session ID
- `shipping_option_id` (string, required): Shipping option ID to select

**Returns**: Updated checkout session

**Example**:
```python
update_guest_shipping_option(
    checkout_session_id="session123",
    shipping_option_id="STANDARD_SHIPPING"
)
```

---

### 26. get_guest_purchase_order
**Endpoint**: `GET /buy/order/v2/guest_purchase_order/{purchaseOrderId}`

Get details of a guest purchase order.

**Parameters**:
- `purchase_order_id` (string, required): Purchase order ID

**Returns**: Purchase order details

**Example**:
```python
get_guest_purchase_order(purchase_order_id="order123")
```

---

## Complete Checkout Workflow Example

```python
# 1. Search for items
results = search_items(q="laptop", limit=5)
item_id = results["itemSummaries"][0]["itemId"]

# 2. Get item details
item = get_item(item_id=item_id, fieldgroups="PRODUCT")

# 3. Initiate checkout
session = initiate_guest_checkout_session(items_payload='''
{
  "contactEmail": "buyer@example.com",
  "lineItemInputs": [{"itemId": "''' + item_id + '''", "quantity": 1}],
  "shippingAddress": {
    "addressLine1": "123 Main St",
    "city": "San Jose",
    "stateOrProvince": "CA",
    "postalCode": "95131",
    "country": "US",
    "firstName": "John",
    "lastName": "Doe",
    "phoneNumber": "+14155551234"
  }
}
''')
session_id = session["checkoutSessionId"]

# 4. Apply coupon if available
apply_guest_coupon(checkout_session_id=session_id, coupon_code="SAVE10")

# 5. Select shipping option
session = get_guest_checkout_session(checkout_session_id=session_id)
shipping_option_id = session["lineItems"][0]["shippingOptions"][0]["shippingOptionId"]
update_guest_shipping_option(
    checkout_session_id=session_id,
    shipping_option_id=shipping_option_id
)

# 6. Get final order details
final_session = get_guest_checkout_session(checkout_session_id=session_id)
print(f"Total: {final_session['pricing']['total']}")
```

---

## Error Handling

All tools return JSON-serializable responses. Errors are returned as:

```json
{
  "error": "Error message or API error details"
}
```

Check for the `error` key in responses to handle failures gracefully.

---

## Rate Limits

- Standard API rate limits apply per eBay documentation
- Implement exponential backoff for rate limit errors
- Monitor your API usage in the eBay developer dashboard

---

## Marketplace Support

Currently configured for EBAY_US. To use other marketplaces, modify the `X-EBAY-C-MARKETPLACE-ID` header in the `make_request()` function.

Supported marketplaces:
- EBAY_US, EBAY_GB, EBAY_DE, EBAY_FR, EBAY_IT, EBAY_ES, EBAY_CA, EBAY_AU, and others

---

## Authentication

All tools require valid eBay API credentials:
- `EBAY_APP_ID` - OAuth client ID
- `EBAY_CERT_ID` - OAuth client secret

Set these as environment variables before running the server.
