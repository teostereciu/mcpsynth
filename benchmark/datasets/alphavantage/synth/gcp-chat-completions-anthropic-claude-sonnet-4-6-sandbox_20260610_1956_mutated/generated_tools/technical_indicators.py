"""
Technical Indicator tools for Alpha Vantage MCP server.
Source: docs/api_technical_indicators.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> str:
    return os.environ.get("ALPHAVANTAGE_API_KEY", "")


def _fetch(params: dict) -> dict:
    params["apikey"] = _get_api_key()
    try:
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def register_technical_indicator_tools(mcp: FastMCP):

    @mcp.tool()
    def get_sma(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: str = "",
    ) -> dict:
        """
        Return Simple Moving Average (SMA) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM' or 'USDEUR'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per SMA calculation, e.g. 10 or 200.
            price_type: Price series to use: 'close', 'open', 'high', or 'low'.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "SMA",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_ema(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: str = "",
    ) -> dict:
        """
        Return Exponential Moving Average (EMA) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per EMA calculation, e.g. 10 or 200.
            price_type: Price series to use: 'close', 'open', 'high', or 'low'.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "EMA",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_wma(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: str = "",
    ) -> dict:
        """
        Return Weighted Moving Average (WMA) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per WMA calculation, e.g. 10.
            price_type: Price series to use: 'close', 'open', 'high', or 'low'.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "WMA",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_rsi(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: str = "",
    ) -> dict:
        """
        Return Relative Strength Index (RSI) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per RSI calculation, e.g. 14.
            price_type: Price series to use: 'close', 'open', 'high', or 'low'.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "RSI",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_macd(
        ticker: str,
        time_interval: str,
        price_type: str,
        fast_period: int = 12,
        slow_period: int = 26,
        signal_period: int = 9,
        month: str = "",
    ) -> dict:
        """
        Return Moving Average Convergence/Divergence (MACD) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            price_type: Price series to use: 'close', 'open', 'high', or 'low'.
            fast_period: Fast EMA period (default 12).
            slow_period: Slow EMA period (default 26).
            signal_period: Signal line period (default 9).
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "MACD",
            "ticker": ticker,
            "time_interval": time_interval,
            "price_type": price_type,
            "fastperiod": fast_period,
            "slowperiod": slow_period,
            "signalperiod": signal_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_bbands(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        nbdevup: int = 2,
        nbdevdn: int = 2,
        month: str = "",
    ) -> dict:
        """
        Return Bollinger Bands (BBANDS) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per BBANDS calculation, e.g. 20.
            price_type: Price series to use: 'close', 'open', 'high', or 'low'.
            nbdevup: Standard deviation multiplier for upper band (default 2).
            nbdevdn: Standard deviation multiplier for lower band (default 2).
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "BBANDS",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
            "nbdevup": nbdevup,
            "nbdevdn": nbdevdn,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_stoch(
        ticker: str,
        time_interval: str,
        month: str = "",
    ) -> dict:
        """
        Return Stochastic Oscillator (STOCH) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "STOCH",
            "ticker": ticker,
            "time_interval": time_interval,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_adx(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: str = "",
    ) -> dict:
        """
        Return Average Directional Movement Index (ADX) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per ADX calculation, e.g. 14.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "ADX",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_cci(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: str = "",
    ) -> dict:
        """
        Return Commodity Channel Index (CCI) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per CCI calculation, e.g. 20.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "CCI",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_aroon(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: str = "",
    ) -> dict:
        """
        Return Aroon indicator values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per Aroon calculation, e.g. 14.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "AROON",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_obv(
        ticker: str,
        time_interval: str,
        month: str = "",
    ) -> dict:
        """
        Return On Balance Volume (OBV) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "OBV",
            "ticker": ticker,
            "time_interval": time_interval,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_atr(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: str = "",
    ) -> dict:
        """
        Return Average True Range (ATR) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'.
            time_interval: One of '1min','5min','15min','30min','60min','daily','weekly','monthly'.
            time_period: Number of data points per ATR calculation, e.g. 14.
            month: Optional YYYY-MM to restrict to a specific historical month.
        """
        params = {
            "function": "ATR",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)
