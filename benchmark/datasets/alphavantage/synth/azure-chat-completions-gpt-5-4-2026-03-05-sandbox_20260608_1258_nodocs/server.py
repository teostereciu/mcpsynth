from mcp.server.fastmcp import FastMCP

from generated_tools.crypto import (
    get_digital_currency_daily,
    get_digital_currency_monthly,
    get_digital_currency_weekly,
)
from generated_tools.economic import (
    get_cpi,
    get_durables,
    get_federal_funds_rate,
    get_inflation,
    get_nonfarm_payroll,
    get_real_gdp,
    get_real_gdp_per_capita,
    get_retail_sales,
    get_treasury_yield,
    get_unemployment,
)
from generated_tools.forex import (
    get_currency_exchange_rate,
    get_fx_daily,
    get_fx_monthly,
    get_fx_weekly,
)
from generated_tools.fundamentals import (
    get_balance_sheet,
    get_company_overview,
    get_earnings,
    get_income_statement,
)
from generated_tools.sector import get_sector_performance
from generated_tools.stocks import (
    get_daily_adjusted_time_series,
    get_daily_time_series,
    get_global_quote,
    get_intraday_time_series,
    get_monthly_adjusted_time_series,
    get_monthly_time_series,
    get_weekly_adjusted_time_series,
    get_weekly_time_series,
    search_symbols,
)
from generated_tools.technical import get_bbands, get_ema, get_macd, get_rsi, get_sma

mcp = FastMCP("alphavantage")

mcp.tool()(get_global_quote)
mcp.tool()(search_symbols)
mcp.tool()(get_intraday_time_series)
mcp.tool()(get_daily_time_series)
mcp.tool()(get_daily_adjusted_time_series)
mcp.tool()(get_weekly_time_series)
mcp.tool()(get_weekly_adjusted_time_series)
mcp.tool()(get_monthly_time_series)
mcp.tool()(get_monthly_adjusted_time_series)

mcp.tool()(get_currency_exchange_rate)
mcp.tool()(get_fx_daily)
mcp.tool()(get_fx_weekly)
mcp.tool()(get_fx_monthly)

mcp.tool()(get_digital_currency_daily)
mcp.tool()(get_digital_currency_weekly)
mcp.tool()(get_digital_currency_monthly)

mcp.tool()(get_sma)
mcp.tool()(get_ema)
mcp.tool()(get_rsi)
mcp.tool()(get_macd)
mcp.tool()(get_bbands)

mcp.tool()(get_company_overview)
mcp.tool()(get_income_statement)
mcp.tool()(get_balance_sheet)
mcp.tool()(get_earnings)

mcp.tool()(get_cpi)
mcp.tool()(get_inflation)
mcp.tool()(get_real_gdp)
mcp.tool()(get_unemployment)
mcp.tool()(get_treasury_yield)
mcp.tool()(get_federal_funds_rate)
mcp.tool()(get_retail_sales)
mcp.tool()(get_durables)
mcp.tool()(get_nonfarm_payroll)
mcp.tool()(get_real_gdp_per_capita)

mcp.tool()(get_sector_performance)


if __name__ == "__main__":
    mcp.run()
