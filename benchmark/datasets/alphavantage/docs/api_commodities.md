# Commodities

*Source: https://www.alphavantage.co/documentation/#commodities*

---

## Commodities

APIs under this section provide price data for major commodities such as gold, silver, crude oil, natural gas, copper, wheat, etc., spanning across various temporal horizons (daily, weekly, monthly, quarterly, etc.)


#### Gold & Silver Spot Prices Trending


This API returns the live spot prices of gold and silver metals.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=GOLD_SILVER_SPOT`

**❚ Required:`symbol`**

For gold, strings `GOLD` and `XAU` are accepted. For silver, strings `SILVER` and `XAG` are accepted.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

_Silver spot price (symbol=SILVER and symbol=XAG are both accepted)_

[`https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=demo`](https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=demo";
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


#### Gold & Silver Historical Prices Trending


This API returns the historical gold and silver prices in daily, weekly, and monthly horizons.

💡 Tip: Looking for gold and silver live prices instead? Please check out our dedicated gold & silver spot price API.


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=GOLD_SILVER_HISTORY`

**❚ Required:`symbol`**

For gold, strings `GOLD` and `XAU` are accepted. For silver, strings `SILVER` and `XAG` are accepted.

**❚ Required:`interval`**

Strings `daily`, `weekly` and `monthly` are accepted

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

_Daily close prices for silver (symbol=SILVER and symbol=XAG are both accepted)_

[`https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=SILVER&interval=daily&apikey=demo`](https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=SILVER&interval=daily&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=SILVER&interval=daily&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=SILVER&interval=daily&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=SILVER&interval=daily&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&symbol=SILVER&interval=daily&apikey=demo";
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


#### Crude Oil Prices: West Texas Intermediate (WTI) Trending


This API returns the West Texas Intermediate (WTI) crude oil prices in daily, weekly, and monthly horizons.

Source: U.S. Energy Information Administration, Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=WTI`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `daily`, `weekly`, and `monthly` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo"
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


#### Crude Oil Prices (Brent) Trending


This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.

Source: U.S. Energy Information Administration, Crude Oil Prices: Brent - Europe, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=BRENT`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `daily`, `weekly`, and `monthly` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo"
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


#### Natural Gas


This API returns the Henry Hub natural gas spot prices in daily, weekly, and monthly horizons.

Source: U.S. Energy Information Administration, Henry Hub Natural Gas Spot Price, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=NATURAL_GAS`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `daily`, `weekly`, and `monthly` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo";
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


#### Global Price of Copper


This API returns the global price of copper in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Copper, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=COPPER`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo";
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


#### Global Price of Aluminum


This API returns the global price of aluminum in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Aluminum, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=ALUMINUM`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo";
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


#### Global Price of Wheat


This API returns the global price of wheat in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Wheat, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=WHEAT`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo";
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


#### Global Price of Corn


This API returns the global price of corn in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Corn, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=CORN`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo";
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


#### Global Price of Cotton


This API returns the global price of cotton in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Cotton, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=COTTON`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo";
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


#### Global Price of Sugar


This API returns the global price of sugar in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Sugar, No. 11, World, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=SUGAR`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo";
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


#### Global Price of Coffee


This API returns the global price of coffee in monthly, quarterly, and annual horizons.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global price of Coffee, Other Mild Arabica, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=COFFEE`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo";
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


#### Global Price Index of All Commodities


This API returns the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.

Source: International Monetary Fund ([IMF Terms of Use](https://www.imf.org/external/terms.htm)), Global Price Index of All Commodities, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is _not_ endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the [FRED® API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html).


###### **API Parameters**

**❚ Required:`function`**

The function of your choice. In this case, `function=ALL_COMMODITIES`

❚ Optional: `interval`

By default, `interval=monthly`. Strings `monthly`, `quarterly`, and `annual` are accepted.

❚ Optional: `datatype`

By default, `datatype=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the time series in JSON format; `csv` returns the time series as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo`](https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo"
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