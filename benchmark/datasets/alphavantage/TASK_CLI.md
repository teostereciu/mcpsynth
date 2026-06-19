# Task: Build a CLI Tool for the Alpha Vantage API

## What You're Building

A command-line interface (CLI) tool that covers Alpha Vantage financial data API functionality, suitable for use by an autonomous agent completing real-world tasks.

## What You Have

- **API documentation** in `docs/` — 9 markdown files covering the Alpha Vantage API endpoints.
- **Environment variables** for authentication:
  - `ALPHAVANTAGE_API_KEY` — API key
- **Base URL:** `https://www.alphavantage.co/query`
- **Auth:** `apikey` query parameter appended to every request.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Stock quotes (global quote, daily, weekly, monthly, intraday time series)
- Symbol search
- Forex (exchange rates, FX time series)
- Cryptocurrency exchange rates
- Technical indicators (SMA, EMA, RSI, MACD)
- Fundamental data (company overview, earnings)
- Economic indicators (CPI, GDP, inflation)

## Technical Requirements

- **No generic passthrough commands**: do not expose a generic `query` or `request` command that accepts arbitrary function names and parameters. Every command must correspond to a specific, named operation.

## Deliverables

- `alphavantage_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
