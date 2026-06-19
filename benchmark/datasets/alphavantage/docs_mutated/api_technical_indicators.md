# Technical Indicators

*Source: https://www.alphavantage.co/documentation/#technical-indicators*

---

## Technical Indicators

Technical indicator APIs for a given equity or currency exchange pair, derived from the underlying time series based stock API and forex data. All indicators are calculated from _adjusted_ time series data to eliminate artificial price/volume perturbations from historical split and dividend events.


#### SMA Trending


This API returns the simple moving average (SMA) values. See also: [SMA explainer](https://www.alphavantage.co/simple_moving_average_sma/) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=SimpleMA.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=SMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =SMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=SMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)

[`https://www.alphavantage.co/query?**function** =SMA&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=SMA&ticker=USDEUR&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=SMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=SMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=SMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=SMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### EMA Trending


This API returns the exponential moving average (EMA) values. See also: [EMA explainer](https://www.alphavantage.co/exponential_moving_average_ema/) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=ExpMA.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=EMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =EMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=EMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)

[`https://www.alphavantage.co/query?**function** =EMA&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=EMA&ticker=USDEUR&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=EMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=EMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=EMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=EMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### WMA


This API returns the weighted moving average (WMA) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=WeightedMA.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=WMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =WMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=WMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=WMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=WMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=WMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=WMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### DEMA


This API returns the double exponential moving average (DEMA) values. See also: [Investopedia article](http://www.investopedia.com/articles/trading/10/double-exponential-moving-average.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=DEMA.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=DEMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =DEMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=DEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=DEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=DEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=DEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=DEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### TEMA


This API returns the triple exponential moving average (TEMA) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=TEMA.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=TEMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =TEMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=TEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=TEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=TEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=TEMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### TRIMA


This API returns the triangular moving average (TRIMA) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=TriangularMA.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=TRIMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =TRIMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=TRIMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TRIMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=TRIMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=TRIMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=TRIMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### KAMA


This API returns the Kaufman adaptive moving average (KAMA) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=KAMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =KAMA&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=KAMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=KAMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=KAMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=KAMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=KAMA&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### MAMA


This API returns the MESA adaptive moving average (MAMA) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MAMA`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `fastlimit`

Positive floats are accepted. By default, `fastlimit=0.01`.

❚ Optional: `slowlimit`

Positive floats are accepted. By default, `slowlimit=0.01`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MAMA&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**fastlimit** =0.02&**apikey** =demo`](https://www.alphavantage.co/query?function=MAMA&ticker=IBM&time_interval=daily&price_type=close&fastlimit=0.02&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MAMA&ticker=IBM&time_interval=daily&price_type=close&fastlimit=0.02&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MAMA&ticker=IBM&time_interval=daily&price_type=close&fastlimit=0.02&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MAMA&ticker=IBM&time_interval=daily&price_type=close&fastlimit=0.02&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MAMA&ticker=IBM&time_interval=daily&price_type=close&fastlimit=0.02&apikey=demo"
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


#### VWAP Trending Premium


This API returns the volume weighted average price (VWAP) for _intraday_ time series. See also: [Investopedia article](https://www.investopedia.com/terms/v/vwap.asp).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=VWAP`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. In keeping with mainstream investment literatures on VWAP, the following intraday intervals are supported: `1min`, `5min`, `15min`, `30min`, `60min`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =VWAP&**ticker** =IBM&**time_interval** =15min&**apikey** =demo`](https://www.alphavantage.co/query?function=VWAP&ticker=IBM&time_interval=15min&apikey=demo)


💡 Tip: this is a premium API function. Subscribe to a [premium membership plan](https://www.alphavantage.co/premium/) to instantly unlock all premium APIs.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=VWAP&ticker=IBM&time_interval=15min&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=VWAP&ticker=IBM&time_interval=15min&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=VWAP&ticker=IBM&time_interval=15min&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=VWAP&ticker=IBM&time_interval=15min&apikey=demo"
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


#### T3


This API returns the Tilson moving average (T3) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=T3.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=T3`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =T3&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=T3&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=T3&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=T3&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=T3&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=T3&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### MACD Trending Premium


This API returns the moving average convergence / divergence (MACD) values. See also: [Investopedia article](http://www.investopedia.com/articles/forex/05/macddiverge.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=MACD.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MACD`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `fastperiod`

Positive integers are accepted. By default, `fastperiod=12`.

❚ Optional: `slowperiod`

Positive integers are accepted. By default, `slowperiod=26`.

❚ Optional: `signalperiod`

Positive integers are accepted. By default, `signalperiod=9`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MACD&**ticker** =IBM&**time_interval** =daily&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=MACD&ticker=IBM&time_interval=daily&price_type=open&apikey=demo)

[`https://www.alphavantage.co/query?**function** =MACD&**ticker** =USDEUR&**time_interval** =weekly&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=MACD&ticker=USDEUR&time_interval=weekly&price_type=open&apikey=demo)


💡 Tip: this is a premium API function. Subscribe to a [premium membership plan](https://www.alphavantage.co/premium/) to instantly unlock all premium APIs.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MACD&ticker=IBM&time_interval=daily&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MACD&ticker=IBM&time_interval=daily&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MACD&ticker=IBM&time_interval=daily&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MACD&ticker=IBM&time_interval=daily&price_type=open&apikey=demo"
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


#### MACDEXT


This API returns the moving average convergence / divergence values with controllable moving average type. See also: [Investopedia article](http://www.investopedia.com/articles/forex/05/macddiverge.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=MACD.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MACDEXT`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `fastperiod`

Positive integers are accepted. By default, `fastperiod=12`.

❚ Optional: `slowperiod`

Positive integers are accepted. By default, `slowperiod=26`.

❚ Optional: `signalperiod`

Positive integers are accepted. By default, `signalperiod=9`.

❚ Optional: `fastmatype`

Moving average type for the faster moving average. By default, `fastmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `slowmatype`

Moving average type for the slower moving average. By default, `slowmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `signalmatype`

Moving average type for the signal moving average. By default, `signalmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MACDEXT&**ticker** =IBM&**time_interval** =daily&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=MACDEXT&ticker=IBM&time_interval=daily&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MACDEXT&ticker=IBM&time_interval=daily&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MACDEXT&ticker=IBM&time_interval=daily&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MACDEXT&ticker=IBM&time_interval=daily&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MACDEXT&ticker=IBM&time_interval=daily&price_type=open&apikey=demo"
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


#### STOCH Trending


This API returns the stochastic oscillator (STOCH) values. See also: [Investopedia article](https://www.investopedia.com/terms/s/stochasticoscillator.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=StochasticOscillator.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=STOCH`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `fastkperiod`

The time period of the fastk moving average. Positive integers are accepted. By default, `fastkperiod=5`.

❚ Optional: `slowkperiod`

The time period of the slowk moving average. Positive integers are accepted. By default, `slowkperiod=3`.

❚ Optional: `slowdperiod`

The time period of the slowd moving average. Positive integers are accepted. By default, `slowdperiod=3`.

❚ Optional: `slowkmatype`

Moving average type for the slowk moving average. By default, `slowkmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `slowdmatype`

Moving average type for the slowd moving average. By default, `slowdmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =STOCH&**ticker** =IBM&**time_interval** =daily&**apikey** =demo`](https://www.alphavantage.co/query?function=STOCH&ticker=IBM&time_interval=daily&apikey=demo)

[`https://www.alphavantage.co/query?**function** =STOCH&**ticker** =USDEUR&**time_interval** =weekly&**apikey** =demo`](https://www.alphavantage.co/query?function=STOCH&ticker=USDEUR&time_interval=weekly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCH&ticker=IBM&time_interval=daily&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=STOCH&ticker=IBM&time_interval=daily&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=STOCH&ticker=IBM&time_interval=daily&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=STOCH&ticker=IBM&time_interval=daily&apikey=demo"
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


#### STOCHF


This API returns the stochastic fast (STOCHF) values. See also: [Investopedia article](http://www.investopedia.com/university/indicator_oscillator/ind_osc8.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=StochasticOscillator.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=STOCHF`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `fastkperiod`

The time period of the fastk moving average. Positive integers are accepted. By default, `fastkperiod=5`.

❚ Optional: `fastdperiod`

The time period of the fastd moving average. Positive integers are accepted. By default, `fastdperiod=3`.

❚ Optional: `fastdmatype`

Moving average type for the fastd moving average. By default, `fastdmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =STOCHF&**ticker** =IBM&**time_interval** =daily&**apikey** =demo`](https://www.alphavantage.co/query?function=STOCHF&ticker=IBM&time_interval=daily&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCHF&ticker=IBM&time_interval=daily&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=STOCHF&ticker=IBM&time_interval=daily&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=STOCHF&ticker=IBM&time_interval=daily&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=STOCHF&ticker=IBM&time_interval=daily&apikey=demo"
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


#### RSI Trending


This API returns the relative strength index (RSI) values. See also: [RSI explainer](https://www.alphavantage.co/relative_strength_index_rsi/) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=RSI.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=RSI`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each RSI value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =RSI&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=RSI&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo)

[`https://www.alphavantage.co/query?**function** =RSI&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =10&**price_type** =open&**apikey** =demo`](https://www.alphavantage.co/query?function=RSI&ticker=USDEUR&time_interval=weekly&time_period=10&price_type=open&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=RSI&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=RSI&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=RSI&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=RSI&ticker=IBM&time_interval=weekly&time_period=10&price_type=open&apikey=demo"
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


#### STOCHRSI


This API returns the stochastic relative strength index (STOCHRSI) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=StochRSI.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=STOCHRSI`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each STOCHRSI value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `fastkperiod`

The time period of the fastk moving average. Positive integers are accepted. By default, `fastkperiod=5`.

❚ Optional: `fastdperiod`

The time period of the fastd moving average. Positive integers are accepted. By default, `fastdperiod=3`.

❚ Optional: `fastdmatype`

Moving average type for the fastd moving average. By default, `fastdmatype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =STOCHRSI&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**price_type** =close&**fastkperiod** =6&**fastdmatype** =1&**apikey** =demo`](https://www.alphavantage.co/query?function=STOCHRSI&ticker=IBM&time_interval=daily&time_period=10&price_type=close&fastkperiod=6&fastdmatype=1&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCHRSI&ticker=IBM&time_interval=daily&time_period=10&price_type=close&fastkperiod=6&fastdmatype=1&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=STOCHRSI&ticker=IBM&time_interval=daily&time_period=10&price_type=close&fastkperiod=6&fastdmatype=1&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=STOCHRSI&ticker=IBM&time_interval=daily&time_period=10&price_type=close&fastkperiod=6&fastdmatype=1&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=STOCHRSI&ticker=IBM&time_interval=daily&time_period=10&price_type=close&fastkperiod=6&fastdmatype=1&apikey=demo"
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


#### WILLR


This API returns the Williams' %R (WILLR) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=WilliamsR.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=WILLR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each WILLR value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =WILLR&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=WILLR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=WILLR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=WILLR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=WILLR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=WILLR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### ADX Trending


This API returns the average directional movement index (ADX) values. See also: [Investopedia article](http://www.investopedia.com/articles/trading/07/adx-trend-indicator.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=ADX.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ADX`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each ADX value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ADX&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=ADX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)

[`https://www.alphavantage.co/query?**function** =ADX&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=ADX&ticker=USDEUR&time_interval=weekly&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ADX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ADX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ADX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ADX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### ADXR


This API returns the average directional movement index rating (ADXR) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=ADXR.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ADXR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each ADXR value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ADXR&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=ADXR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ADXR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ADXR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ADXR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ADXR&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### APO


This API returns the absolute price oscillator (APO) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=PriceOscillator.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=APO`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `fastperiod`

Positive integers are accepted. By default, `fastperiod=12`.

❚ Optional: `slowperiod`

Positive integers are accepted. By default, `slowperiod=26`.

❚ Optional: `matype`

Moving average type. By default, `matype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =APO&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**fastperiod** =10&**matype** =1&**apikey** =demo`](https://www.alphavantage.co/query?function=APO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=APO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=APO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=APO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=APO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo"
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


#### PPO


This API returns the percentage price oscillator (PPO) values. See also: [Investopedia article](http://www.investopedia.com/articles/investing/051214/use-percentage-price-oscillator-elegant-indicator-picking-stocks.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=PriceOscillatorPct.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=PPO`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `fastperiod`

Positive integers are accepted. By default, `fastperiod=12`.

❚ Optional: `slowperiod`

Positive integers are accepted. By default, `slowperiod=26`.

❚ Optional: `matype`

Moving average type. By default, `matype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =PPO&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**fastperiod** =10&**matype** =1&**apikey** =demo`](https://www.alphavantage.co/query?function=PPO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=PPO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=PPO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=PPO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=PPO&ticker=IBM&time_interval=daily&price_type=close&fastperiod=10&matype=1&apikey=demo"
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


#### MOM


This API returns the momentum (MOM) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/03/070203.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=Momentum.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MOM`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each MOM value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MOM&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=MOM&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MOM&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MOM&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MOM&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MOM&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo"
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


#### BOP


This API returns the balance of power (BOP) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=BOP`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =BOP&**ticker** =IBM&**time_interval** =daily&**apikey** =demo`](https://www.alphavantage.co/query?function=BOP&ticker=IBM&time_interval=daily&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=BOP&ticker=IBM&time_interval=daily&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=BOP&ticker=IBM&time_interval=daily&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=BOP&ticker=IBM&time_interval=daily&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=BOP&ticker=IBM&time_interval=daily&apikey=demo"
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


#### CCI Trending


This API returns the commodity channel index (CCI) values. See also: [Investopedia article](http://www.investopedia.com/articles/trading/05/041805.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=CCI.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=CCI`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each CCI value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =CCI&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=CCI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)

[`https://www.alphavantage.co/query?**function** =CCI&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=CCI&ticker=USDEUR&time_interval=weekly&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CCI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=CCI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=CCI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=CCI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### CMO


This API returns the Chande momentum oscillator (CMO) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=CMO.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=CMO`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each CMO value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =CMO&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=CMO&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CMO&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=CMO&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=CMO&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=CMO&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo"
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


#### ROC


This API returns the rate of change (ROC) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/092401.asp).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ROC`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each ROC value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ROC&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=ROC&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ROC&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ROC&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ROC&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ROC&ticker=IBM&time_interval=weekly&time_period=10&price_type=close&apikey=demo"
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


#### ROCR


This API returns the rate of change ratio (ROCR) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/092401.asp).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ROCR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each ROCR value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ROCR&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=ROCR&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ROCR&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ROCR&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ROCR&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ROCR&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo"
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


#### AROON Trending


This API returns the Aroon (AROON) values. See also: [Investopedia article](http://www.investopedia.com/articles/trading/06/aroon.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=Aroon.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=AROON`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each AROON value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =AROON&**ticker** =IBM&**time_interval** =daily&**time_period** =14&**apikey** =demo`](https://www.alphavantage.co/query?function=AROON&ticker=IBM&time_interval=daily&time_period=14&apikey=demo)

[`https://www.alphavantage.co/query?**function** =AROON&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =14&**apikey** =demo`](https://www.alphavantage.co/query?function=AROON&ticker=USDEUR&time_interval=weekly&time_period=14&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=AROON&ticker=IBM&time_interval=daily&time_period=14&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=AROON&ticker=IBM&time_interval=daily&time_period=14&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=AROON&ticker=IBM&time_interval=daily&time_period=14&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=AROON&ticker=IBM&time_interval=daily&time_period=14&apikey=demo"
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


#### AROONOSC


This API returns the Aroon oscillator (AROONOSC) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=AroonOscillator.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=AROONOSC`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each AROONOSC value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =AROONOSC&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=AROONOSC&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=AROONOSC&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=AROONOSC&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=AROONOSC&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=AROONOSC&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### MFI


This API returns the money flow index (MFI) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/03/072303.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=MoneyFlowIndex.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MFI`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each MFI value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MFI&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=MFI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MFI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MFI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MFI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MFI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo"
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


#### TRIX


This API returns the 1-day rate of change of a triple smooth exponential moving average (TRIX) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/092402.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=TRIX.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=TRIX`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each TRIX value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =TRIX&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=TRIX&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TRIX&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=TRIX&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=TRIX&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=TRIX&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo"
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


#### ULTOSC


This API returns the ultimate oscillator (ULTOSC) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=UltimateOsc.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ULTOSC`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `timeperiod1`

The first time period for the indicator. Positive integers are accepted. By default, `timeperiod1=7`.

❚ Optional: `timeperiod2`

The second time period for the indicator. Positive integers are accepted. By default, `timeperiod2=14`.

❚ Optional: `timeperiod3`

The third time period for the indicator. Positive integers are accepted. By default, `timeperiod3=28`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ULTOSC&**ticker** =IBM&**time_interval** =daily&**timeperiod1** =8&**apikey** =demo`](https://www.alphavantage.co/query?function=ULTOSC&ticker=IBM&time_interval=daily&timeperiod1=8&apikey=demo)

[`https://www.alphavantage.co/query?**function** =ULTOSC&**ticker** =IBM&**time_interval** =daily&**apikey** =demo`](https://www.alphavantage.co/query?function=ULTOSC&ticker=IBM&time_interval=weekly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ULTOSC&ticker=IBM&time_interval=daily&timeperiod1=8&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ULTOSC&ticker=IBM&time_interval=daily&timeperiod1=8&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ULTOSC&ticker=IBM&time_interval=daily&timeperiod1=8&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ULTOSC&ticker=IBM&time_interval=daily&timeperiod1=8&apikey=demo"
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


#### DX


This API returns the directional movement index (DX) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/050602.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=DX.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=DX`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each DX value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =DX&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=DX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=DX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=DX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=DX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=DX&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### MINUS_DI


This API returns the minus directional indicator (MINUS_DI) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/050602.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=DI.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MINUS_DI`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each MINUS_DI value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MINUS_DI&**ticker** =IBM&**time_interval** =weekly&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=MINUS_DI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MINUS_DI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MINUS_DI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MINUS_DI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MINUS_DI&ticker=IBM&time_interval=weekly&time_period=10&apikey=demo"
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


#### PLUS_DI


This API returns the plus directional indicator (PLUS_DI) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/050602.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=DI.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=PLUS_DI`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each PLUS_DI value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =PLUS_DI&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=PLUS_DI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=PLUS_DI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=PLUS_DI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=PLUS_DI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=PLUS_DI&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### MINUS_DM


This API returns the minus directional movement (MINUS_DM) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/050602.asp)


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MINUS_DM`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each MINUS_DM value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MINUS_DM&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=MINUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MINUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MINUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MINUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MINUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### PLUS_DM


This API returns the plus directional movement (PLUS_DM) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/050602.asp)


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=PLUS_DM`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each PLUS_DM value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =PLUS_DM&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=PLUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=PLUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=PLUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=PLUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=PLUS_DM&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### BBANDS Trending


This API returns the Bollinger bands (BBANDS) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/04/030304.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=Bollinger.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=BBANDS`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each BBANDS value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `nbdevup`

The standard deviation multiplier of the upper band. Positive integers are accepted. By default, `nbdevup=2`.

❚ Optional: `nbdevdn`

The standard deviation multiplier of the lower band. Positive integers are accepted. By default, `nbdevdn=2`.

❚ Optional: `matype`

Moving average type of the time series. By default, `matype=0`. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =BBANDS&**ticker** =IBM&**time_interval** =weekly&**time_period** =5&**price_type** =close&**nbdevup** =3&**nbdevdn** =3&**apikey** =demo`](https://www.alphavantage.co/query?function=BBANDS&ticker=IBM&time_interval=weekly&time_period=5&price_type=close&nbdevup=3&nbdevdn=3&apikey=demo)

[`https://www.alphavantage.co/query?**function** =BBANDS&**ticker** =USDEUR&**time_interval** =weekly&**time_period** =5&**price_type** =close&**nbdevup** =3&**nbdevdn** =3&**apikey** =demo`](https://www.alphavantage.co/query?function=BBANDS&ticker=USDEUR&time_interval=weekly&time_period=5&price_type=close&nbdevup=3&nbdevdn=3&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=BBANDS&ticker=IBM&time_interval=weekly&time_period=5&price_type=close&nbdevup=3&nbdevdn=3&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=BBANDS&ticker=IBM&time_interval=weekly&time_period=5&price_type=close&nbdevup=3&nbdevdn=3&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=BBANDS&ticker=IBM&time_interval=weekly&time_period=5&price_type=close&nbdevup=3&nbdevdn=3&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=BBANDS&ticker=IBM&time_interval=weekly&time_period=5&price_type=close&nbdevup=3&nbdevdn=3&apikey=demo"
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


#### MIDPOINT


This API returns the midpoint (MIDPOINT) values. MIDPOINT = (highest value + lowest value)/2.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MIDPOINT`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each MIDPOINT value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MIDPOINT&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=MIDPOINT&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MIDPOINT&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MIDPOINT&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MIDPOINT&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MIDPOINT&ticker=IBM&time_interval=daily&time_period=10&price_type=close&apikey=demo"
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


#### MIDPRICE


This API returns the midpoint price (MIDPRICE) values. MIDPRICE = (highest high + lowest low)/2.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=MIDPRICE`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each MIDPRICE value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =MIDPRICE&**ticker** =IBM&**time_interval** =daily&**time_period** =10&**apikey** =demo`](https://www.alphavantage.co/query?function=MIDPRICE&ticker=IBM&time_interval=daily&time_period=10&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=MIDPRICE&ticker=IBM&time_interval=daily&time_period=10&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=MIDPRICE&ticker=IBM&time_interval=daily&time_period=10&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=MIDPRICE&ticker=IBM&time_interval=daily&time_period=10&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=MIDPRICE&ticker=IBM&time_interval=daily&time_period=10&apikey=demo"
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


#### SAR


This API returns the parabolic SAR (SAR) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/02/042202.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=SAR.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=SAR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `acceleration`

The acceleration factor. Positive floats are accepted. By default, `acceleration=0.01`.

❚ Optional: `maximum`

The acceleration factor maximum value. Positive floats are accepted. By default, `maximum=0.20`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =SAR&**ticker** =IBM&**time_interval** =weekly&**acceleration** =0.05&**maximum** =0.25&**apikey** =demo`](https://www.alphavantage.co/query?function=SAR&ticker=IBM&time_interval=weekly&acceleration=0.05&maximum=0.25&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=SAR&ticker=IBM&time_interval=weekly&acceleration=0.05&maximum=0.25&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=SAR&ticker=IBM&time_interval=weekly&acceleration=0.05&maximum=0.25&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=SAR&ticker=IBM&time_interval=weekly&acceleration=0.05&maximum=0.25&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=SAR&ticker=IBM&time_interval=weekly&acceleration=0.05&maximum=0.25&apikey=demo"
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


#### TRANGE


This API returns the true range (TRANGE) values. See also: [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=TR.htm)


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=TRANGE`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =TRANGE&**ticker** =IBM&**time_interval** =daily&**apikey** =demo`](https://www.alphavantage.co/query?function=TRANGE&ticker=IBM&time_interval=daily&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TRANGE&ticker=IBM&time_interval=daily&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=TRANGE&ticker=IBM&time_interval=daily&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=TRANGE&ticker=IBM&time_interval=daily&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=TRANGE&ticker=IBM&time_interval=daily&apikey=demo"
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


#### ATR


This API returns the average true range (ATR) values. See also: [Investopedia article](http://www.investopedia.com/articles/trading/08/average-true-range.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=ATR.htm)


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ATR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each ATR value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ATR&**ticker** =IBM&**time_interval** =daily&**time_period** =14&**apikey** =demo`](https://www.alphavantage.co/query?function=ATR&ticker=IBM&time_interval=daily&time_period=14&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ATR&ticker=IBM&time_interval=daily&time_period=14&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ATR&ticker=IBM&time_interval=daily&time_period=14&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ATR&ticker=IBM&time_interval=daily&time_period=14&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ATR&ticker=IBM&time_interval=daily&time_period=14&apikey=demo"
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


#### NATR


This API returns the normalized average true range (NATR) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=NATR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`time_period`**

Number of data points used to calculate each NATR value. Positive integers are accepted (e.g., `time_period=60`, `time_period=200`)

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =NATR&**ticker** =IBM&**time_interval** =weekly&**time_period** =14&**apikey** =demo`](https://www.alphavantage.co/query?function=NATR&ticker=IBM&time_interval=weekly&time_period=14&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=NATR&ticker=IBM&time_interval=weekly&time_period=14&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=NATR&ticker=IBM&time_interval=weekly&time_period=14&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=NATR&ticker=IBM&time_interval=weekly&time_period=14&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=NATR&ticker=IBM&time_interval=weekly&time_period=14&apikey=demo"
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


#### AD Trending


This API returns the Chaikin A/D line (AD) values. See also: [Investopedia article](http://www.investopedia.com/articles/active-trading/031914/understanding-chaikin-oscillator.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=AccumDist.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=AD`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =AD&**ticker** =IBM&**time_interval** =daily&**apikey** =demo`](https://www.alphavantage.co/query?function=AD&ticker=IBM&time_interval=daily&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=AD&ticker=IBM&time_interval=daily&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=AD&ticker=IBM&time_interval=daily&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=AD&ticker=IBM&time_interval=daily&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=AD&ticker=IBM&time_interval=daily&apikey=demo"
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


#### ADOSC


This API returns the Chaikin A/D oscillator (ADOSC) values. See also: [Investopedia article](http://www.investopedia.com/articles/active-trading/031914/understanding-chaikin-oscillator.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=AccumDist.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=ADOSC`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `fastperiod`

The time period of the fast EMA. Positive integers are accepted. By default, `fastperiod=3`.

❚ Optional: `slowperiod`

The time period of the slow EMA. Positive integers are accepted. By default, `slowperiod=10`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example(click for JSON output)**

[`https://www.alphavantage.co/query?**function** =ADOSC&**ticker** =IBM&**time_interval** =daily&**fastperiod** =5&**apikey** =demo`](https://www.alphavantage.co/query?function=ADOSC&ticker=IBM&time_interval=daily&fastperiod=5&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ADOSC&ticker=IBM&time_interval=daily&fastperiod=5&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ADOSC&ticker=IBM&time_interval=daily&fastperiod=5&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ADOSC&ticker=IBM&time_interval=daily&fastperiod=5&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ADOSC&ticker=IBM&time_interval=daily&fastperiod=5&apikey=demo"
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


#### OBV Trending


This API returns the on balance volume (OBV) values. See also: [Investopedia article](http://www.investopedia.com/articles/technical/100801.asp) and [mathematical reference](http://www.fmlabs.com/reference/default.htm?url=OBV.htm).


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=OBV`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =OBV&**ticker** =IBM&**time_interval** =weekly&**apikey** =demo`](https://www.alphavantage.co/query?function=OBV&ticker=IBM&time_interval=weekly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=OBV&ticker=IBM&time_interval=weekly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=OBV&ticker=IBM&time_interval=weekly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=OBV&ticker=IBM&time_interval=weekly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=OBV&ticker=IBM&time_interval=weekly&apikey=demo"
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


#### HT_TRENDLINE


This API returns the Hilbert transform, instantaneous trendline (HT_TRENDLINE) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=HT_TRENDLINE`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HT_TRENDLINE&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=HT_TRENDLINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HT_TRENDLINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HT_TRENDLINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HT_TRENDLINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HT_TRENDLINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo"
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


#### HT_SINE


This API returns the Hilbert transform, sine wave (HT_SINE) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=HT_SINE`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HT_SINE&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=HT_SINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HT_SINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HT_SINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HT_SINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HT_SINE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo"
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


#### HT_TRENDMODE


This API returns the Hilbert transform, trend vs cycle mode (HT_TRENDMODE) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=HT_TRENDMODE`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HT_TRENDMODE&**ticker** =IBM&**time_interval** =weekly&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=HT_TRENDMODE&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HT_TRENDMODE&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HT_TRENDMODE&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HT_TRENDMODE&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HT_TRENDMODE&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo"
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


#### HT_DCPERIOD


This API returns the Hilbert transform, dominant cycle period (HT_DCPERIOD) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=HT_DCPERIOD`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HT_DCPERIOD&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=HT_DCPERIOD&ticker=IBM&time_interval=daily&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HT_DCPERIOD&ticker=IBM&time_interval=daily&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HT_DCPERIOD&ticker=IBM&time_interval=daily&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HT_DCPERIOD&ticker=IBM&time_interval=daily&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HT_DCPERIOD&ticker=IBM&time_interval=daily&price_type=close&apikey=demo"
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


#### HT_DCPHASE


This API returns the Hilbert transform, dominant cycle phase (HT_DCPHASE) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=HT_DCPHASE`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HT_DCPHASE&**ticker** =IBM&**time_interval** =daily&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=HT_DCPHASE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HT_DCPHASE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HT_DCPHASE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HT_DCPHASE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HT_DCPHASE&ticker=IBM&time_interval=daily&price_type=close&apikey=demo"
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


#### HT_PHASOR


This API returns the Hilbert transform, phasor components (HT_PHASOR) values.


###### **API Parameters**

**❚ Required:`function`**

The technical indicator of your choice. In this case, `function=HT_PHASOR`

**❚ Required:`ticker`**

The name of the ticker of your choice. For example: `ticker=IBM`

**❚ Required:`time_interval`**

Time time_interval between two consecutive data points in the time series. The following values are supported: `1min`, `5min`, `15min`, `30min`, `60min`, `daily`, `weekly`, `monthly`

❚ Optional: `month`

By default, this parameter is not set and the technical indicator values will be calculated based on the default length of the underlying intraday, daily, weekly, or monthly time series data. You can use the `month` parameter (in YYYY-MM format) to return technical indicators for a specific month in history. For example, `month=2009-01`.

**❚ Required:`price_type`**

The desired price type in the time series. Four types are supported: `close`, `open`, `high`, `low`

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the daily time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

❚ Optional: `entitlement`

This parameter controls the freshness of the data returned. By default, `entitlement` is not set and _historical_ data is returned. Setting the parameter to `entitlement=realtime` will return _realtime_ data during the US trading day. Setting the parameter to `entitlement=delayed` will return _15-minute delayed_ data during the US trading day.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HT_PHASOR&**ticker** =IBM&**time_interval** =weekly&**price_type** =close&**apikey** =demo`](https://www.alphavantage.co/query?function=HT_PHASOR&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HT_PHASOR&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HT_PHASOR&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HT_PHASOR&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HT_PHASOR&ticker=IBM&time_interval=weekly&price_type=close&apikey=demo"
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