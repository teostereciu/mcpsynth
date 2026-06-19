"""
Technical Indicator tools for Alpha Vantage MCP server.
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
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable is not set")
    return key


def _fetch(params: dict) -> dict:
    try:
        params["apikey"] = _get_api_key()
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except ValueError as e:
        return {"error": str(e)}
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


def register_technical_indicators_tools(mcp: FastMCP):

    @mcp.tool()
    def get_sma(
        symbol: str,
        interval: str,
        time_period: int,
        series_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Simple Moving Average (SMA) values for a stock or forex pair.

        Args:
            symbol: Ticker symbol, e.g. 'IBM' or 'USDEUR'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for each SMA calculation, e.g. 10, 50, 200
            series_type: Price type: 'close', 'open', 'high', 'low'
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "SMA",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_ema(
        symbol: str,
        interval: str,
        time_period: int,
        series_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Exponential Moving Average (EMA) values for a stock or forex pair.

        Args:
            symbol: Ticker symbol, e.g. 'IBM' or 'USDEUR'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for each EMA calculation, e.g. 10, 50, 200
            series_type: Price type: 'close', 'open', 'high', 'low'
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "EMA",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_wma(
        symbol: str,
        interval: str,
        time_period: int,
        series_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Weighted Moving Average (WMA) values for a stock or forex pair.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for each WMA calculation
            series_type: Price type: 'close', 'open', 'high', 'low'
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "WMA",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_macd(
        symbol: str,
        interval: str,
        series_type: str,
        fastperiod: Optional[int] = 12,
        slowperiod: Optional[int] = 26,
        signalperiod: Optional[int] = 9,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Moving Average Convergence/Divergence (MACD) values for a stock or forex pair.
        Returns MACD line, signal line, and histogram.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            series_type: Price type: 'close', 'open', 'high', 'low'
            fastperiod: Fast EMA period (default 12)
            slowperiod: Slow EMA period (default 26)
            signalperiod: Signal line period (default 9)
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "MACD",
            "symbol": symbol,
            "interval": interval,
            "series_type": series_type,
            "fastperiod": fastperiod,
            "slowperiod": slowperiod,
            "signalperiod": signalperiod,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_rsi(
        symbol: str,
        interval: str,
        time_period: int,
        series_type: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Relative Strength Index (RSI) values for a stock or forex pair.
        RSI above 70 typically indicates overbought; below 30 indicates oversold.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for RSI calculation, typically 14
            series_type: Price type: 'close', 'open', 'high', 'low'
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "RSI",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_bbands(
        symbol: str,
        interval: str,
        time_period: int,
        series_type: str,
        nbdevup: Optional[int] = 2,
        nbdevdn: Optional[int] = 2,
        matype: Optional[int] = 0,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Bollinger Bands (BBANDS) values for a stock or forex pair.
        Returns upper band, middle band (SMA), and lower band.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for each band calculation, typically 20
            series_type: Price type: 'close', 'open', 'high', 'low'
            nbdevup: Standard deviation multiplier for upper band (default 2)
            nbdevdn: Standard deviation multiplier for lower band (default 2)
            matype: Moving average type (0=SMA, 1=EMA, 2=WMA, etc.)
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "BBANDS",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type,
            "nbdevup": nbdevup,
            "nbdevdn": nbdevdn,
            "matype": matype,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_stoch(
        symbol: str,
        interval: str,
        fastkperiod: Optional[int] = 5,
        slowkperiod: Optional[int] = 3,
        slowdperiod: Optional[int] = 3,
        slowkmatype: Optional[int] = 0,
        slowdmatype: Optional[int] = 0,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Stochastic Oscillator (STOCH) values for a stock or forex pair.
        Returns SlowK and SlowD lines.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            fastkperiod: Fast-K period (default 5)
            slowkperiod: Slow-K period (default 3)
            slowdperiod: Slow-D period (default 3)
            slowkmatype: Slow-K MA type (default 0=SMA)
            slowdmatype: Slow-D MA type (default 0=SMA)
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "STOCH",
            "symbol": symbol,
            "interval": interval,
            "fastkperiod": fastkperiod,
            "slowkperiod": slowkperiod,
            "slowdperiod": slowdperiod,
            "slowkmatype": slowkmatype,
            "slowdmatype": slowdmatype,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_adx(
        symbol: str,
        interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Average Directional Movement Index (ADX) values for a stock or forex pair.
        ADX measures trend strength; values above 25 indicate a strong trend.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for ADX calculation, typically 14
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "ADX",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_cci(
        symbol: str,
        interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Commodity Channel Index (CCI) values for a stock or forex pair.
        CCI above +100 may indicate overbought; below -100 may indicate oversold.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for CCI calculation, typically 20
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "CCI",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_aroon(
        symbol: str,
        interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Aroon indicator values (Aroon Up and Aroon Down) for a stock or forex pair.
        Used to identify trend changes and trend strength.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for Aroon calculation, typically 14
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "AROON",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_obv(
        symbol: str,
        interval: str,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get On Balance Volume (OBV) values for a stock or forex pair.
        OBV uses volume flow to predict changes in stock price.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "OBV",
            "symbol": symbol,
            "interval": interval,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_atr(
        symbol: str,
        interval: str,
        time_period: int,
        month: Optional[str] = None,
    ) -> dict:
        """
        Get Average True Range (ATR) values for a stock or forex pair.
        ATR measures market volatility.

        Args:
            symbol: Ticker symbol, e.g. 'IBM'
            interval: Time interval: '1min','5min','15min','30min','60min','daily','weekly','monthly'
            time_period: Number of data points for ATR calculation, typically 14
            month: Optional month in YYYY-MM format for historical intraday indicators
        """
        params = {
            "function": "ATR",
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
        }
        if month:
            params["month"] = month
        return _fetch(params)
