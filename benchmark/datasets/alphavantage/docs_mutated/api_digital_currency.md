# Digital / Crypto Currency

*Source: https://www.alphavantage.co/documentation/#digital-currency*

---

## Digital & Crypto Currencies

APIs under this section provide a wide range of data feed for digital and crypto currencies such as Bitcoin.


#### CURRENCY_EXCHANGE_RATE Trending


This API returns the realtime exchange rate for any pair of cryptocurrency (e.g., Bitcoin) or physical currency (e.g., USD).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=CURRENCY_EXCHANGE_RATE`

**❚ Required:`from_currency`**

The currency you would like to get the exchange rate for. It can either be a [ physical currency](https://www.alphavantage.co/physical_currency_list/) or [cryptocurrency](https://www.alphavantage.co/cryptocurrency_list/). For example: `from_currency=USD` or `from_currency=BTC`.

**❚ Required:`to_currency`**

The destination currency for the exchange rate. It can either be a [ physical currency](https://www.alphavantage.co/physical_currency_list/) or [cryptocurrency](https://www.alphavantage.co/cryptocurrency_list/). For example: `to_currency=USD` or `to_currency=BTC`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo`](https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo)

[`https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo`](https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo"
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


#### CRYPTO_INTRADAY Trending Premium


This API returns intraday time series (timestamp, open, high, low, close, volume) of the cryptocurrency specified, updated realtime.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=CRYPTO_INTRADAY`

**❚ Required:`ticker`**

The cryptocurrency of your choice. It can be any of the "from" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `ticker=ETH`.

**❚ Required:`market`**

The exchange market of your choice. It can be any of the "to" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `market=USD`.

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`

❚ Optional: `output_size`

By default, `output_size=compact`. Strings `compact` and `full` are accepted with the following specifications: `compact` returns only the latest 100 data points in the intraday time series; `full` returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the intraday time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =CRYPTO_INTRADAY&**ticker** =ETH&**market** =USD&**time_interval** =5min&**apikey** =demo`](https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&apikey=demo)

[`https://www.alphavantage.co/query?**function** =CRYPTO_INTRADAY&**ticker** =ETH&**market** =USD&**time_interval** =5min&**output_size** =full&**apikey** =demo`](https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&output_size=full&apikey=demo)

[`https://www.alphavantage.co/query?**function** =CRYPTO_INTRADAY&**ticker** =ETH&**market** =USD&**time_interval** =5min&**apikey** =demo&**format** =csv`](https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&apikey=demo&format=csv)


💡 Tip: this is a premium API function. Subscribe to a [premium membership plan](https://www.alphavantage.co/premium/) to instantly unlock all premium APIs.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&ticker=ETH&market=USD&time_interval=5min&apikey=demo"
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


#### DIGITAL_CURRENCY_DAILY


This API returns the daily historical time series for a cryptocurrency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=DIGITAL_CURRENCY_DAILY`

**❚ Required:`ticker`**

The cryptocurrency of your choice. It can be any of the "from" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `ticker=BTC`.

**❚ Required:`market`**

The exchange market of your choice. It can be any of the "to" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `market=EUR`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo`](https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo)

[`https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo&format=csv`](https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo&format=csv)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&ticker=BTC&market=EUR&apikey=demo"
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


#### DIGITAL_CURRENCY_WEEKLY Trending


This API returns the weekly historical time series for a cryptocurrency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=DIGITAL_CURRENCY_WEEKLY`

**❚ Required:`ticker`**

The cryptocurrency of your choice. It can be any of the "from" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `ticker=BTC`.

**❚ Required:`market`**

The exchange market of your choice. It can be any of the "to" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `market=EUR`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo`](https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo)

[`https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo&format=csv`](https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo&format=csv)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&ticker=BTC&market=EUR&apikey=demo"
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


#### DIGITAL_CURRENCY_MONTHLY Trending


This API returns the monthly historical time series for a cryptocurrency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=DIGITAL_CURRENCY_MONTHLY`

**❚ Required:`ticker`**

The cryptocurrency of your choice. It can be any of the "from" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `ticker=BTC`.

**❚ Required:`market`**

The exchange market of your choice. It can be any of the "to" currencies in the [cryptocurrency list](https://www.alphavantage.co/cryptocurrency_list/). For example: `market=EUR`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo`](https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo)

[`https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo&format=csv`](https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo&format=csv)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&ticker=BTC&market=EUR&apikey=demo"
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