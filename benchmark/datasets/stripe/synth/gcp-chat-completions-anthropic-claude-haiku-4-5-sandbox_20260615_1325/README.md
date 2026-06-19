# Stripe MCP Server

A comprehensive Model Context Protocol (MCP) server for the Stripe API, enabling autonomous agents to manage payments, customers, subscriptions, and more.

## Features

This MCP server provides 100+ tools covering the most important Stripe API operations:

### Core Payment Operations
- **Payment Intents**: Create, confirm, cancel, and manage payment intents
- **Charges**: Retrieve and update charges (legacy API)
- **Refunds**: Create, retrieve, update, and list refunds
- **Payment Methods**: Manage payment methods and attach/detach from customers

### Customer Management
- **Customers**: Create, retrieve, update, delete, and list customers
- **Discounts**: Apply and remove discounts from customers and subscriptions

### Subscriptions & Billing
- **Subscriptions**: Create, retrieve, update, cancel, and list subscriptions
- **Subscription Items**: Manage individual items within subscriptions
- **Invoices**: Create, finalize, pay, void, and list invoices
- **Invoice Items**: Add, update, and remove line items from invoices
- **Credit Notes**: Create and manage credit notes for invoices

### Products & Pricing
- **Products**: Create, retrieve, update, and list products
- **Prices**: Create, retrieve, update, and list prices (modern pricing API)
- **Plans**: Create, retrieve, update, delete, and list plans (legacy API)

### Checkout & Payment Links
- **Checkout Sessions**: Create and manage checkout sessions for one-time and recurring payments
- **Payment Links**: Create shareable payment links for customers

### Quotes & Proposals
- **Quotes**: Create, retrieve, update, accept, cancel, and finalize quotes

### Promotions
- **Coupons**: Create, retrieve, delete, and list coupons
- **Promotion Codes**: Create, retrieve, update, and list promotion codes

### Setup & Mandates
- **Setup Intents**: Create, retrieve, confirm, and list setup intents for future payments
- **Mandates**: Retrieve mandate details for recurring payments

### Connect (Platform Operations)
- **Accounts**: Retrieve connected accounts
- **Transfers**: Create, retrieve, update, and list transfers to connected accounts
- **Payouts**: Create, retrieve, cancel, and list payouts

### Disputes & Chargebacks
- **Disputes**: Retrieve, update, close, and list disputes

### Account & Reporting
- **Balance**: Retrieve account balance
- **Balance Transactions**: List balance transactions
- **Events**: Retrieve and list webhook events
- **Tax Rates**: Create, retrieve, update, and list tax rates

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Stripe API key:
```bash
export STRIPE_API_KEY="sk_test_..."
```

## Running the Server

```bash
python server.py
```

The server will start and listen for MCP protocol messages over stdio.

## Authentication

The server uses Bearer token authentication with your Stripe API key. Ensure the `STRIPE_API_KEY` environment variable is set with a valid test or live secret key.

## API Request Format

All requests to the Stripe API are made using form-encoded data (`application/x-www-form-urlencoded`), not JSON. The server handles this automatically.

## Error Handling

The server returns errors as JSON dictionaries with an `error` key:
```json
{
  "error": "API error 404",
  "details": "..."
}
```

Expected errors (like 404s for missing resources) are returned as JSON responses, not raised as exceptions, allowing agents to handle them gracefully.

## Tool Categories

### Customers (5 tools)
- `create_customer` - Create a new customer
- `get_customer` - Retrieve a customer
- `update_customer` - Update customer details
- `delete_customer` - Delete a customer
- `list_customers` - List all customers

### Payment Intents (5 tools)
- `create_payment_intent` - Create a payment intent
- `get_payment_intent` - Retrieve a payment intent
- `confirm_payment_intent` - Confirm a payment intent
- `cancel_payment_intent` - Cancel a payment intent
- `list_payment_intents` - List payment intents

### Charges (3 tools)
- `get_charge` - Retrieve a charge
- `update_charge` - Update charge metadata
- `list_charges` - List charges

### Refunds (4 tools)
- `create_refund` - Create a refund
- `get_refund` - Retrieve a refund
- `update_refund` - Update refund metadata
- `list_refunds` - List refunds

### Products (4 tools)
- `create_product` - Create a product
- `get_product` - Retrieve a product
- `update_product` - Update product details
- `list_products` - List products

### Prices (4 tools)
- `create_price` - Create a price
- `get_price` - Retrieve a price
- `update_price` - Update price details
- `list_prices` - List prices

### Subscriptions (5 tools)
- `create_subscription` - Create a subscription
- `get_subscription` - Retrieve a subscription
- `update_subscription` - Update subscription details
- `cancel_subscription` - Cancel a subscription
- `list_subscriptions` - List subscriptions

### Invoices (6 tools)
- `create_invoice` - Create an invoice
- `get_invoice` - Retrieve an invoice
- `finalize_invoice` - Finalize an invoice
- `pay_invoice` - Pay an invoice
- `void_invoice` - Void an invoice
- `list_invoices` - List invoices

### Checkout Sessions (3 tools)
- `create_checkout_session` - Create a checkout session
- `get_checkout_session` - Retrieve a checkout session
- `list_checkout_sessions` - List checkout sessions

### Payment Methods (3 tools)
- `get_payment_method` - Retrieve a payment method
- `list_payment_methods` - List payment methods for a customer
- `detach_payment_method` - Detach a payment method

### Coupons (4 tools)
- `create_coupon` - Create a coupon
- `get_coupon` - Retrieve a coupon
- `delete_coupon` - Delete a coupon
- `list_coupons` - List coupons

### Promotion Codes (4 tools)
- `create_promotion_code` - Create a promotion code
- `get_promotion_code` - Retrieve a promotion code
- `update_promotion_code` - Update a promotion code
- `list_promotion_codes` - List promotion codes

### Setup Intents (4 tools)
- `create_setup_intent` - Create a setup intent
- `get_setup_intent` - Retrieve a setup intent
- `confirm_setup_intent` - Confirm a setup intent
- `list_setup_intents` - List setup intents

### Balance (2 tools)
- `get_balance` - Retrieve account balance
- `list_balance_transactions` - List balance transactions

### Transfers (4 tools)
- `create_transfer` - Create a transfer to a connected account
- `get_transfer` - Retrieve a transfer
- `update_transfer` - Update transfer metadata
- `list_transfers` - List transfers

### Payouts (4 tools)
- `create_payout` - Create a payout
- `get_payout` - Retrieve a payout
- `cancel_payout` - Cancel a payout
- `list_payouts` - List payouts

### Disputes (4 tools)
- `get_dispute` - Retrieve a dispute
- `update_dispute` - Update dispute evidence
- `close_dispute` - Close a dispute
- `list_disputes` - List disputes

### Events (2 tools)
- `get_event` - Retrieve an event
- `list_events` - List events

### Accounts (2 tools)
- `get_account` - Retrieve account details
- `list_accounts` - List connected accounts

### Credit Notes (3 tools)
- `create_credit_note` - Create a credit note
- `get_credit_note` - Retrieve a credit note
- `list_credit_notes` - List credit notes

### Tax Rates (4 tools)
- `create_tax_rate` - Create a tax rate
- `get_tax_rate` - Retrieve a tax rate
- `update_tax_rate` - Update a tax rate
- `list_tax_rates` - List tax rates

### Payment Links (4 tools)
- `create_payment_link` - Create a payment link
- `get_payment_link` - Retrieve a payment link
- `update_payment_link` - Update a payment link
- `list_payment_links` - List payment links

### Mandates (1 tool)
- `get_mandate` - Retrieve a mandate

### Subscription Items (5 tools)
- `create_subscription_item` - Create a subscription item
- `get_subscription_item` - Retrieve a subscription item
- `update_subscription_item` - Update a subscription item
- `delete_subscription_item` - Delete a subscription item
- `list_subscription_items` - List subscription items

### Discounts (2 tools)
- `create_discount` - Apply a discount
- `delete_discount` - Remove a discount

### Invoice Items (5 tools)
- `create_invoice_item` - Create an invoice item
- `get_invoice_item` - Retrieve an invoice item
- `update_invoice_item` - Update an invoice item
- `delete_invoice_item` - Delete an invoice item
- `list_invoice_items` - List invoice items

### Plans (5 tools)
- `create_plan` - Create a plan (legacy API)
- `get_plan` - Retrieve a plan
- `update_plan` - Update a plan
- `delete_plan` - Delete a plan
- `list_plans` - List plans

### Quotes (7 tools)
- `create_quote` - Create a quote
- `get_quote` - Retrieve a quote
- `update_quote` - Update a quote
- `accept_quote` - Accept a quote
- `cancel_quote` - Cancel a quote
- `finalize_quote` - Finalize a quote
- `list_quotes` - List quotes

## Grounding

All tools are documented in `grounding.json`, which maps each tool to its source documentation file and corresponding Stripe API endpoint.

## Example Usage

### Create a Customer
```python
result = create_customer(
    email="customer@example.com",
    name="John Doe",
    description="Premium customer"
)
```

### Create a Payment Intent
```python
result = create_payment_intent(
    amount=2000,  # $20.00 in cents
    currency="usd",
    customer="cus_123456",
    description="Order #12345"
)
```

### Create a Subscription
```python
result = create_subscription(
    customer="cus_123456",
    items=[
        {"price": "price_123456", "quantity": 1}
    ],
    currency="usd"
)
```

### Create a Checkout Session
```python
result = create_checkout_session(
    mode="payment",
    line_items=[
        {"price": "price_123456", "quantity": 1}
    ],
    success_url="https://example.com/success",
    cancel_url="https://example.com/cancel"
)
```

## Limitations

- The server does not expose generic passthrough tools. Every tool corresponds to a specific, named operation.
- Some advanced features (like custom webhooks or complex tax calculations) may require direct API access.
- The server uses form-encoded requests, which is the standard for Stripe's API.

## Support

For issues or questions about the Stripe API, refer to the official [Stripe API documentation](https://docs.stripe.com/api).

## License

This MCP server is provided as-is for use with the Stripe API.
