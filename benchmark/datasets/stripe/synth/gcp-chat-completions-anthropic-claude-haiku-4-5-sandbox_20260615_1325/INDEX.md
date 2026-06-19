# Stripe MCP Server - Documentation Index

## Quick Start

1. **Read**: [README.md](README.md) - Installation and basic usage
2. **Install**: `pip install -r requirements.txt`
3. **Configure**: `export STRIPE_API_KEY="sk_test_..."`
4. **Run**: `python server.py`

## Documentation Files

### For Users
- **[README.md](README.md)** - Start here! Installation, features, and usage guide
- **[TOOLS_REFERENCE.md](TOOLS_REFERENCE.md)** - Complete list of all 108 tools with examples

### For Developers
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Technical details and architecture
- **[server.py](server.py)** - Main implementation (40KB, 108 tools)

### For Project Management
- **[DELIVERABLES.md](DELIVERABLES.md)** - Deliverables checklist and verification
- **[COMPLETION_REPORT.md](COMPLETION_REPORT.md)** - Project completion status
- **[TASK.md](TASK.md)** - Original requirements

### For Integration
- **[grounding.json](grounding.json)** - Tool-to-documentation mapping
- **[requirements.txt](requirements.txt)** - Python dependencies

## File Organization

```
.
├── README.md                      # User guide (START HERE)
├── TOOLS_REFERENCE.md             # Complete tool reference
├── IMPLEMENTATION_SUMMARY.md       # Technical details
├── DELIVERABLES.md                # Deliverables checklist
├── COMPLETION_REPORT.md            # Project status
├── INDEX.md                        # This file
├── TASK.md                         # Original requirements
├── server.py                       # Main implementation
├── requirements.txt                # Dependencies
└── grounding.json                  # Tool mappings
```

## What Each File Contains

### README.md
- Feature overview
- Installation instructions
- Running the server
- Authentication details
- Complete tool reference by category
- Example usage patterns
- Limitations and notes

### TOOLS_REFERENCE.md
- All 108 tools listed by category
- Tool statistics
- Common patterns
- Usage examples
- Error handling guide
- Complete API endpoint mapping

### IMPLEMENTATION_SUMMARY.md
- Overview of the implementation
- Tool coverage breakdown
- Key features
- Implementation details
- HTTP methods and request format
- Response format
- Tool organization
- Testing instructions
- Compliance verification
- Future enhancements

### DELIVERABLES.md
- Deliverables checklist
- Implementation coverage
- Technical requirements verification
- Tool count summary
- Documentation files used
- Compliance verification
- Files delivered
- Verification steps

### COMPLETION_REPORT.md
- Project status
- Deliverables summary
- Implementation statistics
- Verification checklist
- Code quality assessment
- Deployment readiness
- Performance characteristics
- Security considerations
- Known limitations
- Future enhancement opportunities
- Support and maintenance

### server.py
- Main MCP server implementation
- 108 tools organized by category
- Helper function for Stripe API requests
- Authentication handling
- Error handling
- Form-encoded request support

### requirements.txt
- fastmcp==3.2.4
- requests==2.32.3

### grounding.json
- Maps each tool to its documentation file
- Maps each tool to its Stripe API endpoint
- 108 tool mappings

## Tool Categories

The 108 tools are organized into 29 categories:

1. **Customers** (5) - Customer management
2. **Payment Intents** (5) - Modern payment flow
3. **Charges** (3) - Legacy payment flow
4. **Refunds** (4) - Refund management
5. **Products** (4) - Product catalog
6. **Prices** (4) - Modern pricing API
7. **Plans** (5) - Legacy pricing API
8. **Subscriptions** (5) - Recurring billing
9. **Subscription Items** (5) - Subscription line items
10. **Invoices** (6) - Invoice management
11. **Invoice Items** (5) - Invoice line items
12. **Checkout Sessions** (3) - Hosted checkout
13. **Payment Links** (4) - Shareable payment links
14. **Payment Methods** (3) - Payment method management
15. **Coupons** (4) - Discount coupons
16. **Promotion Codes** (4) - Promotion code management
17. **Setup Intents** (4) - Future payment setup
18. **Mandates** (1) - Recurring payment mandates
19. **Quotes** (7) - Customer quotes
20. **Discounts** (2) - Discount application
21. **Balance** (2) - Account balance
22. **Transfers** (4) - Platform transfers
23. **Payouts** (4) - Account payouts
24. **Disputes** (4) - Chargeback disputes
25. **Events** (2) - Webhook events
26. **Accounts** (2) - Connected accounts
27. **Credit Notes** (3) - Credit notes
28. **Tax Rates** (4) - Tax rate management

**Total: 108 Tools**

## Quick Reference

### Installation
```bash
pip install -r requirements.txt
export STRIPE_API_KEY="sk_test_..."
python server.py
```

### Common Operations

#### Create a Customer
```python
create_customer(
    email="customer@example.com",
    name="John Doe"
)
```

#### Create a Payment Intent
```python
create_payment_intent(
    amount=2000,
    currency="usd",
    customer="cus_123456"
)
```

#### Create a Subscription
```python
create_subscription(
    customer="cus_123456",
    items=[{"price": "price_123456"}]
)
```

#### Create a Checkout Session
```python
create_checkout_session(
    mode="payment",
    line_items=[{"price": "price_123456", "quantity": 1}],
    success_url="https://example.com/success",
    cancel_url="https://example.com/cancel"
)
```

## Key Features

✅ **108 MCP Tools** - Comprehensive Stripe API coverage
✅ **Bearer Token Auth** - Secure authentication
✅ **Form-Encoded Requests** - Proper request format
✅ **Error Handling** - Graceful error responses
✅ **No Generic Tools** - Every tool is specific
✅ **Complete Documentation** - 8 documentation files
✅ **Production Ready** - Tested and verified
✅ **Easy to Deploy** - Simple setup process

## Support

For issues or questions:
1. Check [README.md](README.md) for installation help
2. Check [TOOLS_REFERENCE.md](TOOLS_REFERENCE.md) for tool usage
3. Check [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for technical details
4. Refer to [Stripe API Documentation](https://docs.stripe.com/api)

## Project Status

✅ **COMPLETE** - All deliverables ready for production use

---

**Last Updated**: 2024
**Version**: 1.0
**Tools**: 108
**Documentation Files**: 8
