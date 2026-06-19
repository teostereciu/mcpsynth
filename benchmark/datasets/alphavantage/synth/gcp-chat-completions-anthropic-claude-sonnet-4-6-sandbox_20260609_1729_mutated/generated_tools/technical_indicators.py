"""
Technical Indicators tools for Alpha Vantage MCP server.
Source: docs/api_technical_indicators.md
"""

import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> str:
    key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    if not key:
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable not set")
    return key


def _call(params: dict) -> dict:
    try:
        params["apikey"] = _get_api_key()
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except ValueError as e:
        return {"error": str(e)}
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def register_technical_indicator_tools(mcp: FastMCP):

    @mcp.tool()
    def get_sma(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Simple Moving Average (SMA) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM' or 'USDEUR'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per SMA calculation, e.g. 10, 50, 200
            price_type: Price type to use: 'close', 'open', 'high', or 'low'
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "SMA",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_ema(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Exponential Moving Average (EMA) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM' or 'USDEUR'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per EMA calculation, e.g. 10, 50, 200
            price_type: Price type to use: 'close', 'open', 'high', or 'low'
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "EMA",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_wma(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Weighted Moving Average (WMA) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per WMA calculation, e.g. 10, 50, 200
            price_type: Price type to use: 'close', 'open', 'high', or 'low'
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "WMA",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_rsi(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Relative Strength Index (RSI) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per RSI calculation, e.g. 14
            price_type: Price type to use: 'close', 'open', 'high', or 'low'
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "RSI",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_macd(
        ticker: str,
        time_interval: str,
        price_type: str,
        fastperiod: Optional[int] = None,
        slowperiod: Optional[int] = None,
        signalperiod: Optional[int] = None,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Moving Average Convergence/Divergence (MACD) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            price_type: Price type to use: 'close', 'open', 'high', or 'low'
            fastperiod: Fast EMA period (default 12)
            slowperiod: Slow EMA period (default 26)
            signalperiod: Signal EMA period (default 9)
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "MACD",
            "ticker": ticker,
            "time_interval": time_interval,
            "price_type": price_type,
        }
        if fastperiod is not None:
            params["fastperiod"] = fastperiod
        if slowperiod is not None:
            params["slowperiod"] = slowperiod
        if signalperiod is not None:
            params["signalperiod"] = signalperiod
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_bbands(
        ticker: str,
        time_interval: str,
        time_period: int,
        price_type: str,
        nbdevup: Optional[int] = None,
        nbdevdn: Optional[int] = None,
        matype: Optional[int] = None,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Bollinger Bands (BBANDS) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per BBANDS calculation, e.g. 20
            price_type: Price type to use: 'close', 'open', 'high', or 'low'
            nbdevup: Standard deviation multiplier for upper band (default 2)
            nbdevdn: Standard deviation multiplier for lower band (default 2)
            matype: Moving average type (0=SMA, 1=EMA, etc.; default 0)
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "BBANDS",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
            "price_type": price_type,
        }
        if nbdevup is not None:
            params["nbdevup"] = nbdevup
        if nbdevdn is not None:
            params["nbdevdn"] = nbdevdn
        if matype is not None:
            params["matype"] = matype
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_stoch(
        ticker: str,
        time_interval: str,
        fastkperiod: Optional[int] = None,
        slowkperiod: Optional[int] = None,
        slowdperiod: Optional[int] = None,
        slowkmatype: Optional[int] = None,
        slowdmatype: Optional[int] = None,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Stochastic Oscillator (STOCH) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            fastkperiod: Fast-K period (default 5)
            slowkperiod: Slow-K period (default 3)
            slowdperiod: Slow-D period (default 3)
            slowkmatype: Slow-K MA type (default 0=SMA)
            slowdmatype: Slow-D MA type (default 0=SMA)
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "STOCH",
            "ticker": ticker,
            "time_interval": time_interval,
        }
        if fastkperiod is not None:
            params["fastkperiod"] = fastkperiod
        if slowkperiod is not None:
            params["slowkperiod"] = slowkperiod
        if slowdperiod is not None:
            params["slowdperiod"] = slowdperiod
        if slowkmatype is not None:
            params["slowkmatype"] = slowkmatype
        if slowdmatype is not None:
            params["slowdmatype"] = slowdmatype
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_adx(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Average Directional Movement Index (ADX) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per ADX calculation, e.g. 14
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "ADX",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_cci(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Commodity Channel Index (CCI) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per CCI calculation, e.g. 20
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "CCI",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_aroon(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Aroon (AROON) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per Aroon calculation, e.g. 14
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "AROON",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_atr(
        ticker: str,
        time_interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Average True Range (ATR) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points per ATR calculation, e.g. 14
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "ATR",
            "ticker": ticker,
            "time_interval": time_interval,
            "time_period": time_period,
        }
        if month is not None:
            params["month"] = month
        return _call(params)

    @mcp.tool()
    def get_obv(
        ticker: str,
        time_interval: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get On Balance Volume (OBV) values for a ticker.

        Args:
            ticker: Equity or forex symbol, e.g. 'IBM'
            time_interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            month: Optional YYYY-MM for a specific historical month, e.g. '2009-01'
        """
        params = {
            "function": "OBV",
            "ticker": ticker,
            "time_interval": time_interval,
        }
        if month is not None:
            params["month"] = month
        return _call(params)
