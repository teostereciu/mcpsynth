# Stripe MCP Server

A comprehensive Model Context Protocol (MCP) server for the Stripe API, enabling autonomous agents to interact with Stripe's payment processing platform.

## Features

This MCP server provides tools for:

### Core Payment Operations
- **Payment Intents**: Create, confirm, cancel, and manage payment intents
- **Charges**: Create and manage charges (legacy API)
- **Refunds**: Create, retrieve, and manage refunds
- **Payment Methods**: Create, attach, detach, and manage payment methods

### Customer Management
- **Customers**: Create, retrieve, update, list, and delete customers
- **Customer Sources**: Manage customer payment sources and bank accounts
- **Customer Bank Accounts**: Create and manage customer bank accounts

### Billing & Subscriptions
- **Subscriptions**: Create, retrieve, update, cancel, and list subscriptions
- **Subscription Items**: Manage items within subscriptions
- **Invoices**: Create, finalize, pay, and manage invoices
- **Invoice Items**: Create and manage individual invoice line items
- **Credit Notes**: Create and manage credit notes

### Products & Pricing
- **Products**: Create, retrieve, update, and list products
- **Prices**: Create, retrieve, update, and list prices
- **Plans**: Create, retrieve, update, and manage billing plans (legacy)

### Promotions & Discounts
- **Coupons**: Create, retrieve, delete, and list coupons
- **Promotion Codes**: Create, retrieve, update, and list promotion codes
- **Discounts**: Create and delete discounts

### Checkout & Payment Links
- **Checkout Sessions**: Create and manage checkout sessions
- **Payment Links**: Create, retrieve, update, and list payment links

### Connect (Marketplace)
- **Transfers**: Create, retrieve, update, and list transfers to connected accounts
- **Payouts**: Create, retrieve, cancel, and list payouts
- **Connected Accounts**: Create, retrieve, and update connected accounts

### Disputes & Risk Management
- **Disputes**: Retrieve, update, close, and list disputes
- **Setup Intents**: Create, retrieve, confirm, and list setup intents

### Taxes & Compliance
- **Tax Codes**: Retrieve and list tax codes
- **Tax Rates**: Create, retrieve, update, and list tax rates

### Shipping
- **Shipping Rates**: Create, retrieve, update, and list shipping rates

### Account & Reporting
- **Balance**: Retrieve account balance
- **Balance Transactions**: List balance transactions
- **Events**: Retrieve and list webhook events
- **Mandates**: Retrieve and list payment mandates

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Set the `STRIPE_API_KEY` environment variable with your Stripe test secret key:

```bash
export STRIPE_API_KEY=sk_test_...
```

## Running the Server

```bash
python server.py
```

The server will start and listen for MCP protocol messages over stdio.

## API Reference

All tools are documented with their parameters and return types. The server uses Bearer token authentication with the Stripe API and handles form-encoded request bodies as required by Stripe.

### Error Handling

The server returns errors as JSON dictionaries with an `error` key containing the error message. Expected errors (like 404s for invalid IDs) are returned as JSON rather than raising exceptions, allowing agents to handle them gracefully.

### Request Format

All requests use form-encoded bodies (application/x-www-form-urlencoded) as required by the Stripe API. Nested parameters are handled using bracket notation (e.g., `metadata[key]=value`).

## Tool Categories

- **100+ tools** covering all major Stripe API operations
- **CRUD operations** for all primary resources
- **List operations** with pagination support
- **Specialized operations** like confirm, finalize, cancel, etc.

## Documentation

Each tool includes:
- Clear description of what it does
- Parameter documentation
- Links to relevant Stripe API documentation via `grounding.json`

## Grounding

The `grounding.json` file maps each tool to its corresponding Stripe API documentation file and endpoint, enabling agents to understand the relationship between tools and the underlying API.

## Requirements

- Python 3.8+
- FastMCP 3.2.4+
- Requests 2.32.3+
- Valid Stripe API key (test or live)

## License

This MCP server is provided as-is for use with the Stripe API.
