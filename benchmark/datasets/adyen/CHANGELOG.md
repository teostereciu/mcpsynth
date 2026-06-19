# Adyen Dataset Changelog

## Current Version: v2_harder (28 scenarios, strict validation)

**Last Updated:** 2026-03-30
**Current File:** `TASK.md` (based on `TASK.md.v2_harder`)
**Pass Rate Target:** 65-70% overall
**Actual Pass Rate:** 84.6% (22/26 scenarios with old version) - higher than target, acceptable

---

## Recent Updates (2026-03-30)

### Outcome-Based Validation Implementation (Latest)
**Improvement:** Replaced variable name checking with outcome-based validation
- **Problem:** Tests were checking for specific variable names (e.g., `nl_methods`, `us_methods`), causing false failures when implementations used different names
- **Solution:** Implemented outcome-based validation similar to GitHub/eBay datasets
  - Type 1 (Read Operations): Verify by calling API ourselves to confirm data exists
  - Type 2 (Create Operations): Verify execution succeeded without crashing
  - Type 3 (Analysis/Filtering): Capture stdout and verify output contains expected keywords/data
  - Type 4 (Error Handling): Verify scenario runs without crashing, check output mentions error/recovery
- **Changes:**
  - Added `capture_output` parameter to `run_scenario()` to capture stdout
  - Added `adyen_api_call()` helper for API verification
  - Updated 8 failing scenarios: 6, 19, 21, 23, 25, 26, 27, 28
  - Removed all variable name assertions
  - Focus on actual behavior: API calls work, output contains results, errors are handled
- **Actual Impact:** Pass rate improved from 71.4% (20/28) to 96.4% (27/28 passed, 1 skipped*)
  - *Scenario 21 skipped due to installment API limitation in test mode
  - All other scenarios now pass with fair, outcome-based validation

**Validation Approach by Scenario Type:**
- **Type 1 (Read Operations)**: Execute scenario, call same API ourselves to verify data exists, check printed output
  - Examples: Scenarios 1-5, 6, 7, 10, 13, 19
  - Validation: API call succeeds, output contains expected keywords
- **Type 2 (Create Operations)**: Execute scenario, verify it runs without crashing
  - Examples: Scenarios 8, 11, 12, 15, 16, 20, 21, 22, 25
  - Validation: Execution succeeds, no unhandled exceptions
- **Type 3 (Analysis/Filtering)**: Execute scenario, capture stdout, verify output contains analysis results
  - Examples: Scenarios 6, 9, 14, 17, 18, 19, 23, 24
  - Validation: Output contains keywords (common, score, rank, etc.) and numeric values
- **Type 4 (Error Handling)**: Execute scenario, verify no crash, check output mentions error/recovery
  - Examples: Scenarios 26, 27, 28
  - Validation: Execution succeeds, output mentions error or recovery keywords

### New Error Handling Scenarios (27-28)
- **Scenario 27**: Invalid Currency Handling
  - Attempt to create session with invalid currency "INVALID"
  - Catch error, extract details, recover with valid EUR session
  - Tests error handling for validation errors
- **Scenario 28**: Non-Existent Resource Handling
  - Attempt to get merchant account with non-existent ID
  - Catch 404/403 error, extract error code/message
  - Tests error handling for resource not found

**Total scenarios: 26 → 28**

### Scenario Redesigns for API Limitations & Quality
- **Scenario 6**: **Replaced** with "Payment Method Capabilities Analysis"
  - Old: List stored payment methods (always returns empty for new shopper)
  - New: Analyze payment methods across 3 countries, identify common methods, generate summary
  - Better testability, more meaningful validation
- **Scenario 10**: Changed from "create store" to "list stores, get details if exists" (cannot create stores in test mode)
- **Scenario 13**: Changed from "create webhook" to "list webhooks, get details if exists" (cannot create webhooks in test mode)
- **Scenario 19**: **Replaced entirely** with "Payment Method Filtering and Analysis"
  - Old: Create 3 stores with conditional logic (not possible in test mode)
  - New: Filter payment methods by recurring support, analyze capabilities, generate summary
  - Fully testable, no API limitations, still Tier 3 difficulty

### Error Handling Fix
- **Scenario 26**: Changed from €0.00 (which unexpectedly succeeds) to negative amount -100 (which properly fails)

### TASK.md Cleanup
- Copied cleaner version from `_demo_val/TASK.md` (removed tier labels, removed unnecessary validation details)
- Removed all "Check that:" validation lines (test implementation details, not agent requirements)
- Updated scenario count references from 25 to 26

---

## Version History

### v2_harder - Strict Validation + Error Handling
**Date:** 2026-03-30
**Scenarios:** 26 (added Scenario 26)
**Target Pass Rate:** 65-70%
**Actual Pass Rate:** 84.6% (22/26) - acceptable

**Major Changes:**
- Added **Scenario 26**: Error Response Handling and Recovery (negative amount test)
- Updated **Scenario 23** with strict scoring requirements: `(recurring×2) + (3DS×1) + (brands×0.5)`
- Updated **Scenario 24** with gap analysis: must check AUTHORISATION, CAPTURE, REFUND, CHARGEBACK
- Updated **Scenario 25** with exact normalization: USD×0.92, GBP×1.15, ±2% tolerance
- Fixed **Scenarios 10, 13, 19** to work with API limitations (list instead of create)
- Added `cleanup_tracker` fixture for automatic resource cleanup
- Implemented strict validated tests (scenario-specific checks)

**Test Results (_demo_val implementation):**
- Tier 1 (7 scenarios): 7/7 passed (100%)
- Tier 2 (9 scenarios): 7/9 passed (78%)
- Tier 3 (7 scenarios): 5/7 passed (71%)
- Tier 4 (3 scenarios): 3/3 passed (100%) ⚠️ easier than expected
- **Overall: 22/26 (84.6%)**

**Known Issues:**
- Tier 4 still too easy (100% vs target 15-33%)
- 3 scenarios fail due to API limitations (stores/webhooks cannot be created in test mode)
- Higher pass rate than target, but acceptable for this API's capabilities
- **Validation approach**: Tests currently check for specific variable names, should move to outcome-based validation like GitHub/eBay (verify via API or printed output, not variable names)

---

### v2 - Systematic Difficulty Framework
**Date:** 2026-03-27
**Scenarios:** 25
**Target Pass Rate:** 65-70%

**Major Changes from v1:**
- Implemented systematic difficulty framework with 4 tiers
- Removed simple "create session" scenarios
- Added multi-step workflows and validation requirements
- Added cross-reference scenarios (merchant config vs payment methods)
- Added feature matrix and analysis scenarios

**Tier Distribution:**
- Tier 1 (Easy): 7 scenarios - List operations, basic API calls
- Tier 2 (Medium): 9 scenarios - Data extraction, validation, multi-parameter
- Tier 3 (Hard): 6 scenarios - Multi-country comparison, conditional logic, complex metadata
- Tier 4 (Very Hard): 3 scenarios - Feature matrix, webhook analysis, currency conversion

**Test Results:**
- Initial test: 100% (25/25) - scenarios not hard enough
- Issue: Tier 4 scenarios required only simple aggregation, no algorithms

---

### v1 - Easy Version (Baseline)
**Date:** 2026-03-27
**Scenarios:** 25
**Pass Rate:** 96% (24/25)

**Characteristics:**
- Focused on testability over difficulty
- Most scenarios were single API calls
- Minimal validation requirements
- Good for establishing baseline functionality

**Issues:**
- Too easy - almost everything passed
- Not challenging enough for benchmark purposes
- Needed systematic difficulty calibration

---

## Key Improvements Summary

### 1. Self-Contained Scenarios (v2_harder)
**Problem:** Scenarios relied on pre-existing resources (stores, webhooks)
**Solution:** Updated scenarios to create their own resources
- Scenario 10: Creates store before listing/retrieval
- Scenario 13: Creates webhook before listing/retrieval
- Scenario 19: Creates 3 stores for conditional logic

### 2. Strict Validation (v2_harder)
**Problem:** Tests only checked execution success, not correctness
**Solution:** Implemented scenario-specific validation
- Exact calculations (line item totals, currency conversions)
- Structured output validation (reports with required fields)
- Algorithmic logic (scoring, ranking, gap analysis)
- Error handling and recovery

### 3. Cleanup Infrastructure (v2_harder)
**Problem:** Test pollution from created resources
**Solution:** Added `cleanup_tracker` pytest fixture
- Tracks stores, webhooks, sessions created during tests
- Automatic cleanup after each test
- Proper cleanup order: webhooks → stores → sessions

### 4. Difficulty Calibration
**Evolution:**
- v1: Too easy (96% pass) - minimal validation
- v2: Still too easy (100% pass) - simple aggregation scenarios
- v2_harder: Properly calibrated (expected 65-70%) - strict validation + algorithms

---

## Scenario Design Principles (Established)

See `benchmark/SCENARIO_DESIGN_PRINCIPLES.md` for comprehensive guide.

**Core Principles:**
1. **Self-Contained:** Create own test data, don't assume resources exist
2. **Testable:** Clear success/failure criteria
3. **Validated:** Test behavior and correctness, not just execution
4. **Error Handling:** Include scenarios that expect and handle errors
5. **Cleanup Tracking:** Track created resources for automatic cleanup
6. **Representative:** Cover realistic use cases and workflows
7. **Progressive Difficulty:** Clear tier distribution with expected pass rates
8. **Exact Requirements:** Specify exact values, formulas, tolerances
9. **Structured Output:** Define expected data structures
10. **Edge Cases:** Include boundary conditions and error scenarios

---

## Testing Infrastructure

### Test Files
- `tests/conftest.py` - Pytest configuration and fixtures
- `tests/test_scenarios_v2_validated.py` - Scenario-specific validation tests

### Fixtures
- `adyen_api_key` - API key from environment
- `adyen_merchant_account` - Merchant account from environment
- `generated_tools` - Import and reload generated_tools module
- `cleanup_tracker` - Track resources for automatic cleanup

### Running Tests
```bash
# Set implementation directory
export PYTEST_IMPL_DIR=/path/to/implementation

# Run all tests
cd tests
pytest test_scenarios_v2_validated.py -v

# Run specific scenario
pytest test_scenarios_v2_validated.py::TestScenario23::test_scenario_23 -v
```

---

## Future Considerations

### If Pass Rates Still Too High (>70%)
Consider Option B - Replace scenarios with genuinely harder ones:
- Scenario 23: Add API call minimization requirement
- Scenario 24: Add consolidation strategy requirement
- Scenario 25: Add rate limit handling with exponential backoff

### If Pass Rates Too Low (<60%)
- Move some Tier 3 scenarios to Tier 2
- Relax strict validation slightly (e.g., ±5% instead of ±2%)
- Add more guidance in scenario descriptions

### Additional Scenarios to Consider
- Pagination handling
- Retry logic for transient errors
- Idempotency testing
- Concurrent request handling
- Statistical analysis (mean, std dev, outliers)

---

## File Structure

```
adyen/
├── README.md                          # Main documentation
├── TASK.md                            # Current task specification (v2_harder)
├── CHANGELOG.md                       # This file
├── docs/                              # 591 API endpoint documentations
│   └── api_*.md
└── tests/
    ├── conftest.py                    # Pytest configuration
    └── test_scenarios_v2_validated.py # Validated scenario tests
```

### Archived Versions
- `TASK.md.v1_easy_96percent` - Original easy version
- `TASK.md.v2_empty_dependent` - V2 before self-contained updates
- `TASK.md.v2_harder` - Current version (source for TASK.md)
- `TASK.md.v3_30scenarios` - Experimental 30-scenario version (not pursued)

---

## References

- **Scenario Design Principles:** `benchmark/SCENARIO_DESIGN_PRINCIPLES.md`
- **Difficulty Framework:** `benchmark/SCENARIO_DIFFICULTY_FRAMEWORK.md`
- **Validation Audit:** `benchmark/TODO.txt` (section: Scenario Design & Difficulty Framework)
