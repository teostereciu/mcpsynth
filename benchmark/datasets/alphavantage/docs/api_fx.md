# Forex / FX

*Source: https://www.alphavantage.co/documentation/#fx*

---

## Foreign Exchange Rates (FX)

APIs under this section provide a wide range of data feed for realtime and historical forex (FX) rates.


#### CURRENCY_EXCHANGE_RATE Trending


This API returns the realtime exchange rate for a pair of fiat currencies (e.g., USD, EUR, CNY, etc.).

💡 Tip: Looking for gold and silver spot prices? Please check out our dedicated gold & silver APIs in the Commodities section.


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

[`https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo`](https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo)

[`https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo`](https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo"
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


#### FX_INTRADAY Premium Trending


This API returns intraday time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=FX_INTRADAY`

**❚ Required:`from_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `from_symbol=EUR`

**❚ Required:`to_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `to_symbol=USD`

**❚ Required:`interval`**

Time interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`

❚ Optional: `outputsize`

By default, `outputsize=compact`. Strings `compact` and `full` are accepted with the following specifications: `compact` returns only the latest 100 data points in the intraday time series; `full` returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the intraday time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =FX_INTRADAY&**from_symbol** =EUR&**to_symbol** =USD&**interval** =5min&**apikey** =demo`](https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo)

[`https://www.alphavantage.co/query?**function** =FX_INTRADAY&**from_symbol** =EUR&**to_symbol** =USD&**interval** =5min&**outputsize** =full&**apikey** =demo`](https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&outputsize=full&apikey=demo)

[`https://www.alphavantage.co/query?**function** =FX_INTRADAY&**from_symbol** =EUR&**to_symbol** =USD&**interval** =5min&**apikey** =demo&**datatype** =csv`](https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo&datatype=csv)


💡 Tip: this is a premium API function. Subscribe to a [premium membership plan](https://www.alphavantage.co/premium/) to instantly unlock all premium APIs.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo"
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


#### FX_DAILY


This API returns the daily time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=FX_DAILY`

**❚ Required:`from_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `from_symbol=EUR`

**❚ Required:`to_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `to_symbol=USD`

❚ Optional: `outputsize`

By default, `outputsize=compact`. Strings `compact` and `full` are accepted with the following specifications: `compact` returns only the latest 100 data points in the daily time series; `full` returns the full-length daily time series. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =FX_DAILY&**from_symbol** =EUR&**to_symbol** =USD&**apikey** =demo`](https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo)

[`https://www.alphavantage.co/query?**function** =FX_DAILY&**from_symbol** =EUR&**to_symbol** =USD&**outputsize** =full&**apikey** =demo`](https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey=demo)

[`https://www.alphavantage.co/query?**function** =FX_DAILY&**from_symbol** =EUR&**to_symbol** =USD&**apikey** =demo&**datatype** =csv`](https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo&datatype=csv)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo"
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


#### FX_WEEKLY


This API returns the weekly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.

The latest data point is the price information for the week (or partial week) containing the current trading day, updated realtime.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=FX_WEEKLY`

**❚ Required:`from_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `from_symbol=EUR`

**❚ Required:`to_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `to_symbol=USD`

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the weekly time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =FX_WEEKLY&**from_symbol** =EUR&**to_symbol** =USD&**apikey** =demo`](https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo)

[`https://www.alphavantage.co/query?**function** =FX_WEEKLY&**from_symbol** =EUR&**to_symbol** =USD&**apikey** =demo&**datatype** =csv`](https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo&datatype=csv)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo"
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


#### FX_MONTHLY


This API returns the monthly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.

The latest data point is the prices information for the month (or partial month) containing the current trading day, updated realtime.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=FX_MONTHLY`

**❚ Required:`from_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `from_symbol=EUR`

**❚ Required:`to_symbol`**

A three-letter symbol from the [ forex currency list](https://www.alphavantage.co/physical_currency_list/). For example: `to_symbol=USD`

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the monthly time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =FX_MONTHLY&**from_symbol** =EUR&**to_symbol** =USD&**apikey** =demo`](https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo)

[`https://www.alphavantage.co/query?**function** =FX_MONTHLY&**from_symbol** =EUR&**to_symbol** =USD&**apikey** =demo&**datatype** =csv`](https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo&datatype=csv)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo"
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