import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"

def get_api_key():
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable is not set")
    return api_key

async def make_request(params: dict) -> dict:
    try:
        params["apikey"] = get_api_key()
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}

def register_technical_indicators_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_sma(
        symbol: str,
        interval: str = "daily",
        time_period: int = 20,
        series_type: str = "close"
    ) -> dict:
        """
        Get Simple Moving Average (SMA) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the moving average.
            series_type: The desired price type in the time series (close, open, high, low).
        """
        params = {
            "function": "SMA",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period),
            "series_type": series_type
        }
        return await make_request(params)

    @mcp.tool()
    async def get_ema(
        symbol: str,
        interval: str = "daily",
        time_period: int = 20,
        series_type: str = "close"
    ) -> dict:
        """
        Get Exponential Moving Average (EMA) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the moving average.
            series_type: The desired price type in the time series (close, open, high, low).
        """
        params = {
            "function": "EMA",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period),
            "series_type": series_type
        }
        return await make_request(params)

    @mcp.tool()
    async def get_macd(
        symbol: str,
        interval: str = "daily",
        series_type: str = "close",
        fastperiod: int = 12,
        slowperiod: int = 26,
        signalperiod: int = 9
    ) -> dict:
        """
        Get Moving Average Convergence Divergence (MACD) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            series_type: The desired price type in the time series (close, open, high, low).
            fastperiod: Fast EMA period.
            slowperiod: Slow EMA period.
            signalperiod: Signal line EMA period.
        """
        params = {
            "function": "MACD",
            "symbol": symbol,
            "interval": interval,
            "series_type": series_type,
            "fastperiod": str(fastperiod),
            "slowperiod": str(slowperiod),
            "signalperiod": str(signalperiod)
        }
        return await make_request(params)

    @mcp.tool()
    async def get_rsi(
        symbol: str,
        interval: str = "daily",
        time_period: int = 14,
        series_type: str = "close"
    ) -> dict:
        """
        Get Relative Strength Index (RSI) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the RSI.
            series_type: The desired price type in the time series (close, open, high, low).
        """
        params = {
            "function": "RSI",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period),
            "series_type": series_type
        }
        return await make_request(params)

    @mcp.tool()
    async def get_bbands(
        symbol: str,
        interval: str = "daily",
        time_period: int = 20,
        series_type: str = "close",
        nbdevup: int = 2,
        nbdevdn: int = 2,
        matype: int = 0
    ) -> dict:
        """
        Get Bollinger Bands (BBANDS) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the bands.
            series_type: The desired price type in the time series (close, open, high, low).
            nbdevup: Standard deviation multiplier for the upper band.
            nbdevdn: Standard deviation multiplier for the lower band.
            matype: Moving average type (0 = SMA, 1 = EMA, 2 = WMA, 3 = DEMA, etc.).
        """
        params = {
            "function": "BBANDS",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period),
            "series_type": series_type,
            "nbdevup": str(nbdevup),
            "nbdevdn": str(nbdevdn),
            "matype": str(matype)
        }
        return await make_request(params)

    @mcp.tool()
    async def get_adx(
        symbol: str,
        interval: str = "daily",
        time_period: int = 14
    ) -> dict:
        """
        Get Average Directional Index (ADX) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the ADX.
        """
        params = {
            "function": "ADX",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period)
        }
        return await make_request(params)

    @mcp.tool()
    async def get_cci(
        symbol: str,
        interval: str = "daily",
        time_period: int = 20
    ) -> dict:
        """
        Get Commodity Channel Index (CCI) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the CCI.
        """
        params = {
            "function": "CCI",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period)
        }
        return await make_request(params)

    @mcp.tool()
    async def get_atr(
        symbol: str,
        interval: str = "daily",
        time_period: int = 14
    ) -> dict:
        """
        Get Average True Range (ATR) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            time_period: Number of data points used to calculate the ATR.
        """
        params = {
            "function": "ATR",
            "symbol": symbol,
            "interval": interval,
            "time_period": str(time_period)
        }
        return await make_request(params)

    @mcp.tool()
    async def get_obv(symbol: str, interval: str = "daily") -> dict:
        """
        Get On Balance Volume (OBV) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
        """
        params = {
            "function": "OBV",
            "symbol": symbol,
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stoch(
        symbol: str,
        interval: str = "daily",
        fastkperiod: int = 5,
        slowkperiod: int = 3,
        slowkmatype: int = 0,
        slowdperiod: int = 3,
        slowdmatype: int = 0
    ) -> dict:
        """
        Get Stochastic Oscillator (STOCH) values for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly).
            fastkperiod: Fast %K period.
            slowkperiod: Slow %K period.
            slowkmatype: Slow %K moving average type (0 = SMA, 1 = EMA, etc.).
            slowdperiod: Slow %D period.
            slowdmatype: Slow %D moving average type (0 = SMA, 1 = EMA, etc.).
        """
        params = {
            "function": "STOCH",
            "symbol": symbol,
            "interval": interval,
            "fastkperiod": str(fastkperiod),
            "slowkperiod": str(slowkperiod),
            "slowkmatype": str(slowkmatype),
            "slowdperiod": str(slowdperiod),
            "slowdmatype": str(slowdmatype)
        }
        return await make_request(params)
