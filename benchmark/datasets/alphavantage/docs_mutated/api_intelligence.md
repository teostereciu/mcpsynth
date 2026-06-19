# Alpha Intelligence

*Source: https://www.alphavantage.co/documentation/#intelligence*

---

## Alpha Intelligence™

The APIs in this section contain advanced market intelligence built with our decades of expertise in AI, machine learning, and quantitative finance. We hope these highly differentiated alternative datasets can help turbocharge your trading strategy, market research, and financial software application to the next level.


#### Market News & Sentiment Trending

Looking for market news data to train your LLM models or to augment your trading strategy? You have just found it. This API returns live and historical market news & sentiment data from a large & growing selection of premier news outlets around the world, covering stocks, cryptocurrencies, forex, and a wide range of topics such as fiscal policy, mergers & acquisitions, IPOs, etc. This API, combined with our core stock API, fundamental data, and technical indicator APIs, can provide you with a 360-degree view of the financial market and the broader economy.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=NEWS_SENTIMENT`

**❚ Optional:`tickers`**

The stock/crypto/forex symbols of your choice. For example: `tickers=IBM` will filter for articles that mention the IBM ticker; `tickers=COIN,CRYPTO:BTC,FOREX:USD` will filter for articles that _simultaneously_ mention Coinbase (COIN), Bitcoin (CRYPTO:BTC), and US Dollar (FOREX:USD) in their content.

**❚ Optional:`topics`**

The news topics of your choice. For example: `topics=technology` will filter for articles that write about the technology sector; `topics=technology,ipo` will filter for articles that _simultaneously_ cover technology _and_ IPO in their content. Below is the full list of supported topics:

  * Blockchain: `blockchain`
  * Earnings: `earnings`
  * IPO: `ipo`
  * Mergers & Acquisitions: `mergers_and_acquisitions`
  * Financial Markets: `financial_markets`
  * Economy - Fiscal Policy (e.g., tax reform, government spending): `economy_fiscal`
  * Economy - Monetary Policy (e.g., interest rates, inflation): `economy_monetary`
  * Economy - Macro/Overall: `economy_macro`
  * Energy & Transportation: `energy_transportation`
  * Finance: `finance`
  * Life Sciences: `life_sciences`
  * Manufacturing: `manufacturing`
  * Real Estate & Construction: `real_estate`
  * Retail & Wholesale: `retail_wholesale`
  * Technology: `technology`


**❚ Optional:`time_from` and `time_to`**

The time range of the news articles you are targeting, in YYYYMMDDTHHMM format. For example: `time_from=20220410T0130`. If time_from is specified but time_to is missing, the API will return articles published between the time_from value and the current time.

**❚ Optional:`sort`**

By default, `sort=LATEST` and the API will return the latest articles first. You can also set `sort=EARLIEST` or `sort=RELEVANCE` based on your use case.

**❚ Optional:`limit`**

By default, `limit=50` and the API will return up to 50 matching results. You can also set `limit=1000` to output up to 1000 results.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

_Querying news articles that mention the AAPL ticker._

[`https://www.alphavantage.co/query?**function** =NEWS_SENTIMENT&**tickers** =AAPL&**apikey** =demo`](https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo)

 _Querying news articles that _simultaneously_ mention the Coinbase stock (COIN), Bitcoin (CRYPTO:BTC), and US Dollar (FOREX:USD) and are published on or after 2022-04-10, 1:30am UTC._

[`https://www.alphavantage.co/query?**function** =NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=1000&apikey=demo`](https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=1000&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo"
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).


#### Earnings Call Transcript Trending

This API returns the earnings call transcript for a given company in a specific quarter, covering over 15 years of history and enriched with LLM-based sentiment signals.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=EARNINGS_CALL_TRANSCRIPT`

**❚ Required:`ticker`**

The ticker of the ticker of your choice. For example: `ticker=IBM`.

**❚ Required:`quarter`**

Fiscal quarter in YYYYQM format. For example: `quarter=2024Q1`. Any quarter since 2010Q1 is supported.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =EARNINGS_CALL_TRANSCRIPT&**ticker** =IBM&**quarter** =2024Q1&**apikey** =demo`](https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&ticker=IBM&quarter=2024Q1&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&ticker=IBM&quarter=2024Q1&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&ticker=IBM&quarter=2024Q1&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&ticker=IBM&quarter=2024Q1&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&ticker=IBM&quarter=2024Q1&apikey=demo";
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).


#### Top Gainers, Losers, and Most Actively Traded Tickers (US Market)


This endpoint returns the top 20 gainers, losers, and the most active traded tickers in the US market.


###### **API Parameters**

**❚ Required:`function`**

The API function of your choice. In this case, `function=TOP_GAINERS_LOSERS`

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =TOP_GAINERS_LOSERS&**apikey** =demo`](https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo)


💡 Tip: By default, the top gainers, losers, and the most active traded ticker information is updated at the end of each trading day for all users. If you would like to access realtime or 15-minute delayed data, please subscribe to a [premium membership plan](https://www.alphavantage.co/premium/) for your personal use. For commercial use, please [contact sales](/cdn-cgi/l/email-protection#1a696f6a6a75686e5a7b766a727b6c7b746e7b7d7f347975).

* Realtime and 15-minute delayed US market data is regulated by the stock exchanges, FINRA, and the SEC. [Learn more](https://www.alphavantage.co/realtime_data_policy/) about the key market data policies you need to know as a data consumer.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo";
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).


#### Insider Transactions Trending

This API returns the latest and historical insider transactions made by key stakeholders (e.g., founders, executives, board members, etc.) of a specific company.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=INSIDER_TRANSACTIONS`

**❚ Required:`ticker`**

The ticker of the ticker of your choice. For example: `ticker=IBM`.

❚ Optional: `from`

An optional date filter in YYYY-MM-DD format that only keeps transaction records made on or after a certain date. For example: `from=2026-03-01`. By default, this parameter is not set and all transactions will be returned.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =INSIDER_TRANSACTIONS&**ticker** =IBM&**apikey** =demo`](https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&ticker=IBM&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&ticker=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&ticker=IBM&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&ticker=IBM&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&ticker=IBM&apikey=demo";
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).


#### Institutional Holdings

This API returns the institutional ownership and holdings information for an equity of interest.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=INSTITUTIONAL_HOLDINGS`

**❚ Required:`ticker`**

The ticker of the ticker of your choice. For example: `ticker=IBM`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =INSTITUTIONAL_HOLDINGS&**ticker** =IBM&**apikey** =demo`](https://www.alphavantage.co/query?function=INSTITUTIONAL_HOLDINGS&ticker=IBM&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=INSTITUTIONAL_HOLDINGS&ticker=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=INSTITUTIONAL_HOLDINGS&ticker=IBM&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://www.alphavantage.co/query?function=INSTITUTIONAL_HOLDINGS&ticker=IBM&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://www.alphavantage.co/query?function=INSTITUTIONAL_HOLDINGS&ticker=IBM&apikey=demo";
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).


#### Advanced Analytics (Fixed Window)

This endpoint returns a rich set of advanced analytics metrics (e.g., total return, variance, auto-correlation, etc.) for a given time series over a fixed temporal window.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=ANALYTICS_FIXED_WINDOW`

**❚ Required:`SYMBOLS`**

A list of symbols for the calculation. It can be a comma separated list of symbols as a string. Free API keys can specify up to 5 symbols per API request. Premium API keys can specify up to 50 symbols per API request.

**❚ Required:`RANGE`**

This is the date range for the series being requested. By default, the date range is the full set of data for the equity history. This can be further modified by the LIMIT variable.

RANGE can take certain text values as inputs. They are:

  * `full`
  * `{N}day`
  * `{N}week`
  * `{N}month`
  * `{N}year`


For intraday time series, the following RANGE values are also accepted:

  * `{N}minute`
  * `{N}hour`


Aside from the “full” value which represents the entire time series, the other values specify an time_interval to return the series for as measured backwards from the current date/time.

To specify start & end dates for your analytics calcuation, simply add two RANGE parameters in your API request. For example: `RANGE=2023-07-01&RANGE=2023-08-31` or `RANGE=2020-12-01T00:04:00&RANGE=2020-12-06T23:59:59` with minute-level precision for intraday analytics. If the end date is missing, the end date is assumed to be the last trading date. In addition, you can request a full month of data by using YYYY-MM format like `2020-12`. One day of intraday data can be requested by using YYYY-MM-DD format like `2020-12-06`

**❚ Optional:`OHLC`**

This allows you to choose which open, high, low, or close field the calculation will be performed on. By default, `OHLC=close`. Valid values for these fields are `open`, `high`, `low`, `close`.

**❚ Required:`INTERVAL`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `DAILY`, `WEEKLY`, `MONTHLY`.

**❚ Required:`CALCULATIONS`**

A comma separated list of the analytics metrics you would like to calculate:

  * `MIN`: The minimum return (largest negative or smallest positive) for all values in the series
  * `MAX`: The maximum return for all values in the series
  * `MEAN`: The mean of all returns in the series
  * `MEDIAN`: The median of all returns in the series
  * `CUMULATIVE_RETURN`: The total return from the beginning to the end of the series range
  * `VARIANCE`: The population variance of returns in the series range. Optionally, you can use `VARIANCE(annualized=True)`to normalize the output to an annual value. By default, the variance is not annualized.
  * `STDDEV`: The population standard deviation of returns in the series range for each ticker. Optionally, you can use `STDDEV(annualized=True)`to normalize the output to an annual value. By default, the standard deviation is not annualized.
  * `MAX_DRAWDOWN`: Largest peak to trough time_interval for each ticker in the series range
  * `HISTOGRAM`: For each ticker, place the observed total returns in bins. By default, bins=10. Use `HISTOGRAM(bins=20)` to specify a custom bin value (e.g., 20).
  * `AUTOCORRELATION`: For each ticker place, calculate the autocorrelation for the given lag (e.g., the lag in neighboring points for the autocorrelation calculation). By default, lag=1. Use `AUTOCORRELATION(lag=2)` to specify a custom lag value (e.g., 2).
  * `COVARIANCE`: Returns a covariance matrix for the input symbols. Optionally, you can use `COVARIANCE(annualized=True)`to normalize the output to an annual value. By default, the covariance is not annualized.
  * `CORRELATION`: Returns a correlation matrix for the input symbols, using the PEARSON method as default. You can also specify the KENDALL or SPEARMAN method through `CORRELATION(method=KENDALL)` or `CORRELATION(method=SPEARMAN)`, respectively.


**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

_For AAPL, MSFT, and IBM, calculate the mean & standard deviation of their returns based on daily close prices between 2023-07-01 and 2023-08-31, along with a correlation matrix among the three tickers. _

[`https://www.alphavantage.co/query?function=ANALYTICS_FIXED_WINDOW&SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo`](https://www.alphavantage.co/query?function=ANALYTICS_FIXED_WINDOW&SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo";
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).


#### Advanced Analytics (Sliding Window) Trending

This endpoint returns a rich set of advanced analytics metrics (e.g., total return, variance, auto-correlation, etc.) for a given time series over sliding time windows. For example, we can calculate a moving variance over 5 years with a window of 100 points to see how the variance changes over time.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=ANALYTICS_SLIDING_WINDOW`

**❚ Required:`SYMBOLS`**

A list of symbols for the calculation. It can be a comma separated list of symbols as a string. Free API keys can specify up to 5 symbols per API request. Premium API keys can specify up to 50 symbols per API request.

**❚ Required:`RANGE`**

This is the date range for the series being requested. By default, the date range is the full set of data for the equity history. This can be further modified by the LIMIT variable.

RANGE can take certain text values as inputs. They are:

  * `full`
  * `{N}day`
  * `{N}week`
  * `{N}month`
  * `{N}year`


For intraday time series, the following RANGE values are also accepted:

  * `{N}minute`
  * `{N}hour`


Aside from the “full” value which represents the entire time series, the other values specify an time_interval to return the series for as measured backwards from the current date/time.

To specify start & end dates for your analytics calcuation, simply add two RANGE parameters in your API request. For example: `RANGE=2023-07-01&RANGE=2023-08-31` or `RANGE=2020-12-01T00:04:00&RANGE=2020-12-06T23:59:59` with minute-level precision for intraday analytics. If the end date is missing, the end date is assumed to be the last trading date. In addition, you can request a full month of data by using YYYY-MM format like `2020-12`. One day of intraday data can be requested by using YYYY-MM-DD format like `2020-12-06`

**❚ Optional:`OHLC`**

This allows you to choose which open, high, low, or close field the calculation will be performed on. By default, `OHLC=close`. Valid values for these fields are `open`, `high`, `low`, `close`.

**❚ Required:`INTERVAL`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `DAILY`, `WEEKLY`, `MONTHLY`.

**❚ Required:`WINDOW_SIZE`**

An integer representing the size of the moving window. A hard lower boundary of 10 has been set though it is recommended to make this window larger to make sure the running calculations are statistically significant.

**❚ Required:`CALCULATIONS`**

A comma separated list of the analytics metrics you would like to calculate. Free API keys can specify 1 metric to be calculated per API request. Premium API keys can specify multiple metrics to be calculated simultaneously per API request.

  * `MEAN`: The mean of all returns in the series
  * `MEDIAN`: The median of all returns in the series
  * `CUMULATIVE_RETURN`: The total return from the beginning to the end of the series range
  * `VARIANCE`: The population variance of returns in the series range. Optionally, you can use `VARIANCE(annualized=True)`to normalize the output to an annual value. By default, the variance is not annualized.
  * `STDDEV`: The population standard deviation of returns in the series range for each ticker. Optionally, you can use `STDDEV(annualized=True)`to normalize the output to an annual value. By default, the standard deviation is not annualized.
  * `COVARIANCE`: Returns a covariance matrix for the input symbols. Optionally, you can use `COVARIANCE(annualized=True)`to normalize the output to an annual value. By default, the covariance is not annualized.
  * `CORRELATION`: Returns a correlation matrix for the input symbols, using the PEARSON method as default. You can also specify the KENDALL or SPEARMAN method through `CORRELATION(method=KENDALL)` or `CORRELATION(method=SPEARMAN)`, respectively.


**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

_For AAPL and IBM, calculate the running mean & annualized standard deviation of their returns based on daily close prices in the trailing 2 months, with a sliding window size of 20. _

[`https://www.alphavantage.co/query?function=ANALYTICS_SLIDING_WINDOW&SYMBOLS=AAPL,IBM&RANGE=2month&INTERVAL=DAILY&OHLC=close&WINDOW_SIZE=20&CALCULATIONS=MEAN,STDDEV(annualized=True)&apikey=demo`](https://www.alphavantage.co/query?function=ANALYTICS_SLIDING_WINDOW&SYMBOLS=AAPL,IBM&RANGE=2month&INTERVAL=DAILY&OHLC=close&WINDOW_SIZE=20&CALCULATIONS=MEAN,STDDEV\(annualized=True\)&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://alphavantageapi.co/timeseries/running_analytics?SYMBOLS=AAPL,IBM&RANGE=2month&INTERVAL=DAILY&OHLC=close&WINDOW_SIZE=20&CALCULATIONS=MEAN,STDDEV(annualized=True)&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://alphavantageapi.co/timeseries/running_analytics?SYMBOLS=AAPL,IBM&RANGE=2month&INTERVAL=DAILY&OHLC=close&WINDOW_SIZE=20&CALCULATIONS=MEAN,STDDEV(annualized=True)&apikey=demo';

    request.get({
        url: url,
        json: true,
        headers: {'User-Agent': 'request'}
      }, (err, res, data) => {
        if (err) {
          console.log('Error:', err);
        } else if (res.statusCode !== 200) {
          console.log('Status:', res.statusCode);
        } else {
          // data is successfully parsed as a JSON object:
          console.log(data);
        }
    });


    <?php
    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    $json = file_get_contents('https://alphavantageapi.co/timeseries/running_analytics?SYMBOLS=AAPL,IBM&RANGE=2month&INTERVAL=DAILY&OHLC=close&WINDOW_SIZE=20&CALCULATIONS=MEAN,STDDEV(annualized=True)&apikey=demo');

    $data = json_decode($json,true);

    print_r($data);

    exit;


    using System;
    using System.Collections.Generic;
    using System.Net;

    // -------------------------------------------------------------------------
    // if using .NET Framework
    // https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.8
    // This requires including the reference to System.Web.Extensions in your project
    using System.Web.Script.Serialization;
    // -------------------------------------------------------------------------
    // if using .Net Core
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    using System.Text.Json;
    // -------------------------------------------------------------------------

    namespace ConsoleTests
    {
        internal class Program
        {
            private static void Main(string[] args)
            {
                // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                string QUERY_URL = "https://alphavantageapi.co/timeseries/running_analytics?SYMBOLS=AAPL,IBM&RANGE=2month&INTERVAL=DAILY&OHLC=close&WINDOW_SIZE=20&CALCULATIONS=MEAN,STDDEV(annualized=True)&apikey=demo";
                Uri queryUri = new Uri(QUERY_URL);

                using (WebClient client = new WebClient())
                {
                     // -------------------------------------------------------------------------
                     // if using .NET Framework (System.Web.Script.Serialization)

                    JavaScriptSerializer js = new JavaScriptSerializer();
                    dynamic json_data = js.Deserialize(client.DownloadString(queryUri), typeof(object));

                    // -------------------------------------------------------------------------
                    // if using .NET Core (System.Text.Json)
                    // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                    // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/

                    dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));

                    // -------------------------------------------------------------------------

                    // do something with the json_data
                }
            }
        }
    }


❚ Looking for more programming languages? The open-source community has developed over 1000 libraries for Alpha Vantage across 20+ programming languages and frameworks - you may want to [give them a try](https://github.com/search?q=alpha+vantage).

❚ ✨Want to integrate stock market data into your LLMs or AI agents? Check out our official [MCP server](https://mcp.alphavantage.co/).

❚ If you are a spreadsheet user (e.g., Excel or Google Sheets), please check out our dedicated [spreadsheet add-ons](https://www.alphavantage.co/spreadsheets/).