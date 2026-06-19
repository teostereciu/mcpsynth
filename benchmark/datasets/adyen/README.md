# Adyen Payment Platform API Benchmark

This dataset tests AI agents' ability to build a comprehensive Adyen integration for payment processing, financial accounts, card issuing, and marketplace platforms.

## Overview

**API:** Adyen Complete Platform (Checkout, Payment, Management)
**Endpoints:** 591 across 15+ API categories
**Scenarios:** 26 real-world payment and configuration workflows
**Difficulty:** Medium (API key auth, multi-step validation, data analysis)
**Current Version:** v2_harder with strict validation (see CHANGELOG.md)

## What's Tested

### Core Payment Processing
1. **Checkout API** - Modern hosted payment sessions
2. **Payment API** - Classic payment processing (authorize, capture, refund)
3. **Recurring Payments** - Tokenization and subscription billing
4. **Payment Methods** - Cards, wallets, local payment methods
5. **3D Secure** - Authentication and SCA compliance
6. **Modifications** - Captures, cancellations, refunds

### Financial Platform
7. **Balance Platform** - Financial accounts and balance management
8. **Card Issuing** - Virtual and physical card issuance
9. **Transaction Rules** - Spending controls and limits
10. **Account Holders** - KYC and legal entity management
11. **PIN Management** - Card PIN operations

### Transfers & Payouts
12. **Internal Transfers** - Move funds between accounts
13. **Payouts** - Send funds to external bank accounts
14. **Foreign Exchange** - Multi-currency transfers
15. **Bulk Operations** - Batch payouts

### Marketplace & Platforms
16. **Split Payments** - Multi-party payment routing
17. **Connected Accounts** - Manage sub-merchants
18. **Commission** - Platform fees and revenue share

### Disputes & Risk
19. **Chargeback Management** - Dispute handling and defense
20. **Fraud Detection** - Risk scoring and rules
21. **Authentication** - 3DS and SCA flows

### Configuration & Management
22. **Webhooks** - Event notifications across all services
23. **API Credentials** - Key management
24. **Terminal Management** - POS terminal configuration
25. **Account Settings** - Merchant configuration

## Technical Challenges

- **Multi-Service Architecture** - 5+ different API base URLs
- **Complex Financial Flows** - Authorize → Capture → Refund chains
- **Amount Formatting** - Minor units (cents) across all currencies
- **Webhook Verification** - HMAC signature validation
- **Balance Platform** - Account hierarchy and fund flows
- **Card Issuing** - PCI-compliant card data handling
- **Idempotency** - Preventing duplicate transactions
- **Error Handling** - Detailed error codes and retry logic
- **Multi-Currency** - FX rates and currency conversion

## Dataset Structure

```
adyen/
├── docs/                              # 591 endpoint docs
│   ├── api_checkout_*.md             # Checkout API endpoints
│   ├── api_management_*.md           # Management API endpoints
│   └── ...                           # Other API categories
├── tests/
│   ├── conftest.py                   # Pytest configuration
│   └── test_scenarios_v2_validated.py # Validated scenario tests
├── TASK.md                           # Current task (26 scenarios, v2_harder)
├── TASK.md.v1_easy_96percent         # V1 baseline (archived)
├── TASK.md.v2_harder                 # V2 source (current)
├── CHANGELOG.md                      # Version history and updates
└── README.md                         # This file
```

## API Coverage

### Checkout API (71 endpoints)
The modern, recommended way to accept payments.

- **Sessions** (9) - Hosted payment sessions ✅ Recommended
- **Payment Methods** (3) - Available payment options
- **Payments** (14) - Direct payment processing
- **Payment Links** (5) - Generate payment URLs
- **Orders** (7) - Order management
- **Modifications** (8) - Captures, cancellations, refunds
- **Donations** (2) - Charity integrations
- **Card Details** (3) - BIN lookup and validation
- **Utility** (20) - Supporting operations

### Payment API (14 endpoints)
Classic SOAP-style payment processing (still widely used).

- **authorise** - Authorize payment
- **authorise3d** - 3D Secure authentication
- **authorise3ds2** - 3DS2 authentication
- **capture** - Capture authorization
- **cancel** - Cancel authorization
- **cancelOrRefund** - Cancel or refund
- **refund** - Refund payment
- **adjustAuthorisation** - Modify authorization amount
- **technicalCancel** - Technical cancellation
- **voidPendingRefund** - Void pending refund
- **donate** - Charity donation
- **retrieve3ds2Result** - Get 3DS2 result

### Balance Platform (86 endpoints) ✅ Advanced
Complete financial account and card issuing platform.

**Account Management (20)**
- Balance accounts - Financial account lifecycle
- Account holders - KYC and legal entities
- Sweeps - Automated fund transfers
- Transfer limits - Spending controls

**Card Issuing (25)**
- Payment instruments - Virtual/physical cards
- Card orders - Bulk card ordering
- PIN management - Set/reveal/change PINs
- Network tokens - Card tokenization
- Authorized users - Additional cardholders

**Transaction Controls (15)**
- Transaction rules - Spending limits and controls
- Grant accounts - Capital and financing
- Grant offers - Funding offers
- Mandates - Direct debit mandates

**Configuration (26)**
- Payment instrument groups - Card grouping
- Registered devices - Mobile device binding
- SCA devices - Strong Customer Authentication
- Webhooks - Event notifications
- Public keys - Encryption keys

### Transfers API (17 endpoints)
Move money between accounts and to external recipients.

- **Transfers** (7) - Create, list, get, approve, cancel
- **Transactions** (3) - Transaction history
- **Returns** (2) - Return funds
- **Grants** (3) - Capital grants
- **Route calculation** (2) - FX and fee calculation

### Legal Entity Management API (35 endpoints)
KYC, onboarding, and compliance.

- **Legal Entities** (18) - Create, update, retrieve entities
- **Business Lines** (4) - Business activity management
- **Transfer Instruments** (4) - Bank account management
- **Documents** (4) - Upload verification documents
- **Terms of Service** (3) - TOS acceptance
- **Onboarding** (2) - Hosted onboarding flows

### Management API (158 endpoints)
Configure accounts, terminals, and integrations.

**Merchant Management (45)**
- Merchants - Sub-merchant accounts
- Stores - Physical/online stores
- API credentials - Key management
- Webhooks - Notification setup
- Payment methods - Method configuration

**Terminal Management (35)**
- Terminals - POS terminal management
- Terminal orders - Order physical terminals
- Terminal settings - Configuration
- Actions - Send commands to terminals

**Account Configuration (40)**
- Users - User management
- Allowed origins - CORS configuration
- Payout settings - Payout configuration
- Split configurations - Revenue sharing
- Shipping locations - Pickup points

**Additional (38)**
- Companies - Company-level settings
- Billing entities - Invoicing
- Android apps - Mobile app files
- My API credentials - Self-service keys

### Disputes API (9 endpoints)
Chargeback and dispute management.

- **Disputes** (5) - List, get, create, update disputes
- **Attachments** (4) - Upload evidence documents

### Capital API (12 endpoints) ✅ Advanced
Business financing and cash advances.

- **Grants** (6) - Loan/advance management
- **Grant offers** (3) - Financing offers
- **Dynamic offers** (3) - Real-time offer calculation

### Recurring API (6 endpoints)
Subscription and tokenized payments.

- **disable** - Disable stored payment method
- **listRecurringDetails** - Get stored methods
- **scheduleAccountUpdater** - Update card details
- **notifyShopper** - Send payment reminder
- **createPermit** - Create mandate
- **disablePermit** - Revoke mandate

### Payout API (6 endpoints)
Send funds to recipients.

- **payout** - Initiate payout
- **storeDetail** - Store payout method
- **submitThirdParty** - Third-party payout
- **confirmThirdParty** - Confirm payout
- **declineThirdParty** - Decline payout
- **storeDetailAndSubmitThirdParty** - Combined operation

### Terminal API (19 endpoints)
Cloud-based POS terminal integration.

- **payment** - Process payment
- **refund** - Process refund
- **reversal** - Reverse transaction
- **input** - Get terminal input
- **display** - Show message on terminal
- **print** - Print receipt
- **storedvalue** - Gift card operations
- **cardacquisition** - Card tokenization
- **login/logout** - Terminal session
- **abort** - Cancel operation

### Webhooks (160+ endpoints across 12 categories)
Most comprehensive webhook system of any payment provider.

**Standard Webhooks** (44 events)
- AUTHORISATION, CAPTURE, REFUND
- CHARGEBACK, DISPUTE events
- PAYOUT events
- RECURRING_CONTRACT events

**Balance Platform Webhooks** (15 events)
- Account holder created/updated
- Balance account events
- Payment instrument events
- Network token events

**Transfer Webhooks** (3 events)
- Transfer created/updated
- Transaction events

**Payment Webhooks** (4 events)
- Incoming/outgoing transfers
- Payment created/updated

**And 8 more webhook categories:**
- ACS webhooks (authentication)
- Dispute webhooks
- Capital webhooks
- Transaction webhooks
- Report webhooks
- Balance webhooks
- Tokenization webhooks
- Management notifications

## Authentication

Adyen uses API key authentication:

```bash
X-API-Key: your_api_key_here
Content-Type: application/json
```

Different API services may require different API keys with specific permissions.

## API Versioning

Adyen uses versioned APIs:

- **Checkout API**: v71 (current), v70, v69...
- **Payment API**: v68 (current), v67, v64...
- **Balance Platform**: v2
- **Transfers**: v4
- **Management**: v3

Version is part of the URL path. Older versions remain available.

## Test Environment

### Test Mode
Adyen has comprehensive test environment:
- Test API keys with `test.adyen.com` endpoints
- Full feature parity with production
- No real money processed
- Extensive test card numbers

### Test Cards
```
Success (Visa):           4111 1111 1111 1111
Success (Mastercard):     5555 4444 3333 1111
3DS Required:             5212 3456 7890 1234
Declined - Insufficient:  4000 3000 0000 0001
Declined - Fraud:         4000 3000 0000 0003
```

### Test Bank Accounts
Use Adyen test IBANs for payout testing:
```
NL13TEST0123456789
```

## Base URLs

Different APIs use different base URLs:

**Test Environment:**
```
Checkout API:       https://checkout-test.adyen.com
Payment API:        https://pal-test.adyen.com
Balance Platform:   https://balanceplatform-api-test.adyen.com
Transfers:          https://balanceplatform-api-test.adyen.com
Management:         https://management-test.adyen.com
```

**Production:**
Replace `-test` with `-live` in URLs.

## Scenarios

26 scenarios with progressive difficulty tiers (see TASK.md and CHANGELOG.md):

### Tier 1: Basic Operations (7 scenarios)
Simple API calls testing connectivity and basic functionality

### Tier 2: Data Extraction & Validation (9 scenarios)
Multi-step workflows with data extraction, validation, and reuse

### Tier 3: Complex Workflows (7 scenarios)
Multi-country comparisons, conditional logic, error handling

### Tier 4: Advanced Scenarios (3 scenarios)
Feature analysis, scoring algorithms, gap detection

**Target Pass Rate:** 65-70% overall
- Tier 1: 90-95%
- Tier 2: 65-75%
- Tier 3: 50-60%
- Tier 4: 15-33%

See `TASK.md` for detailed scenario descriptions and `CHANGELOG.md` for version history.

## Key Differences from Other APIs

**vs Stripe:**
- More complex architecture (multiple APIs vs unified)
- Better for marketplaces (built-in split payments)
- More extensive Balance Platform features
- More webhook categories (12 vs 3)
- Requires merchant account in many requests

**vs PayPal:**
- More developer-friendly
- Better international coverage
- More payment methods (global)
- Advanced card issuing features

**vs BigCommerce:**
- Payment-focused vs e-commerce platform
- Financial services features (cards, accounts)
- More complex authentication

**vs Other Payment APIs:**
- Most comprehensive webhook system
- Best-in-class Balance Platform
- Extensive card issuing capabilities
- Strong marketplace/platform features

## Success Metrics

A successful implementation should:
- ✅ Handle API key authentication correctly
- ✅ Work with multiple API base URLs (Checkout, Payment, Management)
- ✅ Correctly format amounts in minor units (cents)
- ✅ Process multi-step workflows with data extraction
- ✅ Implement exact calculations (scoring, currency conversion)
- ✅ Parse complex nested response objects
- ✅ Handle error responses gracefully
- ✅ Pass 17+ out of 26 scenarios (65%+ success rate)

See `CHANGELOG.md` for testing infrastructure and validation details.

## Difficulty: Medium

**What makes this challenging:**
1. Multiple API services (3 base URLs: Checkout, Payment, Management)
2. Multi-step workflows requiring data extraction and reuse
3. Exact calculations with specified formulas (scoring, conversion)
4. Strict validation requirements (structure, values, ranges)
5. Error handling and recovery scenarios
6. Gap analysis and recommendation generation

**What makes this accessible:**
1. ✅ Simple authentication (API key only)
2. ✅ Comprehensive API documentation (591 endpoints)
3. ✅ Excellent test environment
4. ✅ Clear error messages
5. ✅ No complex auth flows (OAuth, JWT)

**Calibration:**
- v1: 96% pass rate (too easy)
- v2_harder: 65-70% target (properly calibrated)
- Strict validation ensures scenarios test correctness, not just execution

## References

- [Adyen API Explorer](https://docs.adyen.com/api-explorer/)
- [Checkout API Guide](https://docs.adyen.com/online-payments/)
- [Balance Platform Guide](https://docs.adyen.com/marketplaces-and-platforms/)
- [Webhooks Guide](https://docs.adyen.com/development-resources/webhooks/)
- [Test Card Numbers](https://docs.adyen.com/development-resources/testing/test-card-numbers/)
- [API Credentials](https://docs.adyen.com/development-resources/api-credentials/)
- [Error Codes](https://docs.adyen.com/development-resources/error-codes/)
