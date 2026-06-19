# Scenario Solutions (Alpha Vantage MCP)

This MCP server exposes a **generic** Alpha Vantage query tool plus convenience wrappers for common domains.

## Setup

- Set `ALPHAVANTAGE_API_KEY` in the environment (or pass `apikey` to tools).
- Run: `python server.py` (stdio MCP).

## Scenario 1: Get the latest quote for a stock

Use the generic tool with the documented function name.

```json
{
  "tool": "alphavantage_query",
  "arguments": {
    "function": "GLOBAL_QUOTE",
    "params": {"symbol": "IBM"}
  }
}
```

## Scenario 2: Fetch daily adjusted time series for a ticker

```json
{
  "tool": "stock_time_series",
  "arguments": {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "ticker": "AAPL",
    "output_size": "compact"
  }
}
```

## Scenario 3: Compute a technical indicator (RSI)

```json
{
  "tool": "technical_indicator",
  "arguments": {
    "function": "RSI",
    "ticker": "MSFT",
    "time_interval": "daily",
    "time_period": 14,
    "series_type": "close"
  }
}
```

## Scenario 4: Realtime FX rate

```json
{
  "tool": "fx_exchange_rate",
  "arguments": {
    "from_currency": "EUR",
    "to_currency": "USD"
  }
}
```

## Scenario 5: Market news & sentiment for a ticker

```json
{
  "tool": "news_sentiment",
  "arguments": {
    "tickers": "TSLA",
    "sort": "LATEST",
    "limit": 20
  }
}
```

## Scenario 6: Economic indicator (CPI)

```json
{
  "tool": "economic_indicator",
  "arguments": {
    "function": "CPI",
    "params": {"interval": "monthly"}
  }
}
```

## Scenario 7: Commodities (gold & silver spot)

```json
{
  "tool": "commodities",
  "arguments": {
    "function": "GOLD_SILVER_SPOT"
  }
}
```

## Scenario 8: Options chain (realtime)

```json
{
  "tool": "options_data",
  "arguments": {
    "function": "REALTIME_OPTIONS",
    "ticker": "SPY"
  }
}
```

## Notes on comprehensive coverage

Alpha Vantage exposes many endpoints via a single `/query` route differentiated by the `function` parameter. For any endpoint not covered by a convenience wrapper, use:

- `alphavantage_query(function, params)`

This provides coverage across:
- Time series data
- FX
- Digital/crypto
- Technical indicators
- Fundamentals
- Commodities
- Economic indicators
- Alpha Intelligence
- Options

