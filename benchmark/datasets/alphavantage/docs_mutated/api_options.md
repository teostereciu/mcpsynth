# Options Data

*Source: https://www.alphavantage.co/documentation/#options*

---

## Options Data APIs

This suite of APIs provide realtime and historical US options data, spanning 15+ years of history with full market coverage. Bullish/bearish option signals such as put-call ratios are also provided.


#### Realtime Options Trending Premium


This API returns realtime US options data with full market coverage. Option chains are sorted by expiration dates in chronological order. Within the same expiration date, contracts are sorted by strike prices from low to high.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=REALTIME_OPTIONS`

**❚ Required:`ticker`**

The name of the equity of your choice. For example: `ticker=IBM`

❚ Optional: `require_greeks`

Enable greeks & implied volatility (IV) fields. By default, `require_greeks=false`. Set `require_greeks=true` to enable greeks & IVs in the API response.

❚ Optional: `contract`

The US options contract ID you would like to specify. By default, the `contract` parameter is not set and the entire option chain for a given ticker will be returned.

❚ Optional: `expiration`

The contract expiration date (in YYYY-MM-DD format) you would like to specify. By default, the `expiration` parameter is not set and contracts across all expiration dates will be returned. The expiration date must be in YYYY-MM-DD format and must be on or after today's date.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the options data in JSON format; `csv` returns the data as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

_By default, the entire realtime option chain is returned_

[`https://www.alphavantage.co/query?**function** =REALTIME_OPTIONS&**ticker** =IBM&**apikey** =demo`](https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&apikey=demo)

 _Set require_greeks=true to enable greeks & implied volatility (IV) fields in the API response_

[`https://www.alphavantage.co/query?**function** =REALTIME_OPTIONS&**ticker** =IBM&**require_greeks** =true&**apikey** =demo`](https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&require_greeks=true&apikey=demo)

 _Query a specific contract (instead of the entire option chain) with greeks & IVs enabled_

[`https://www.alphavantage.co/query?**function** =REALTIME_OPTIONS&**ticker** =IBM&**require_greeks** =true&**contract** =IBM270115C00390000&**apikey** =demo`](https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&require_greeks=true&contract=IBM270115C00390000&apikey=demo)


💡 Tip: this is a premium API function. Subscribe to either the 600 requests per minute or the 1200 requests per minute [premium membership plan](https://www.alphavantage.co/premium/) to unlock realtime options data.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=REALTIME_OPTIONS&ticker=IBM&apikey=demo";
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


#### Realtime Put-Call Ratio


This API returns realtime put-call ratios for both the entire option chain and for specific expiration dates. A lower put-call ratio (<=0.6) typically signals bullish sentiment, as investors are purchasing more call options in expectation of rising prices. On the other hand, a higher ratio (>=1.0) suggests bearish sentiment. However, because this metric is often used as a contrarian indicator, extreme values can imply the opposite - e.g., readings much higher than 1.0 may actually indicate a bullish outlook, while very low readings close to zero can point to potential bearish conditions.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=REALTIME_PUT_CALL_RATIO`

**❚ Required:`ticker`**

The name of the equity of your choice. For example: `ticker=IBM`

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =REALTIME_PUT_CALL_RATIO&**ticker** =IBM&**apikey** =demo`](https://www.alphavantage.co/query?function=REALTIME_PUT_CALL_RATIO&ticker=IBM&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=REALTIME_PUT_CALL_RATIO&ticker=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=REALTIME_PUT_CALL_RATIO&ticker=IBM&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=REALTIME_PUT_CALL_RATIO&ticker=IBM&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=REALTIME_PUT_CALL_RATIO&ticker=IBM&apikey=demo";
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


#### Realtime Volume-to-Open-Interest Ratio


This API returns realtime volume-to-open-interest ratios within an option chain. A high ratio (volume much larger than open interest) often suggests heavy trading activity relative to existing positions, which can indicate short-term speculation, increased liquidity, or possible trend changes. A low ratio (volume small compared to open interest) implies that most positions are being held rather than actively traded, signaling more stable or less volatile conditions. Traders use this ratio to understand whether price moves are driven by new participation (potentially stronger signals) or just minor adjustments within existing positions.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=REALTIME_VOLUME_OPEN_INTEREST_RATIO`

**❚ Required:`ticker`**

The name of the equity of your choice. For example: `ticker=NVDA`

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =REALTIME_VOLUME_OPEN_INTEREST_RATIO&**ticker** =NVDA&**apikey** =demo`](https://www.alphavantage.co/query?function=REALTIME_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=REALTIME_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=REALTIME_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=REALTIME_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=REALTIME_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&apikey=demo";
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


#### Historical Options Trending Premium


This API returns the full historical options chain for a specific ticker on a specific date, covering 15+ years of history. Implied volatility (IV) and common Greeks (e.g., delta, gamma, theta, vega, rho) are also returned. Option chains are sorted by expiration dates in chronological order. Within the same expiration date, contracts are sorted by strike prices from low to high.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=HISTORICAL_OPTIONS`

**❚ Required:`ticker`**

The name of the equity of your choice. For example: `ticker=IBM`

❚ Optional: `date`

By default, the `date` parameter is not set and the API will return data for the previous trading session. Any date later than 2008-01-01 is accepted. For example, `date=2017-11-15`.

❚ Optional: `contract`

The US options contract ID you would like to specify. By default, the `contract` parameter is not set and the entire option chain for a given ticker will be returned.

❚ Optional: `format`

By default, `format=json`. Strings `json` and `csv` are accepted with the following specifications: `json` returns the options data in JSON format; `csv` returns the data as a CSV (comma separated value) file.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Example (click for JSON output)**

_When the date parameter is not set, data from the previous trading session is returned_

[`https://www.alphavantage.co/query?**function** =HISTORICAL_OPTIONS&**ticker** =IBM&**apikey** =demo`](https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&apikey=demo)

 _Specify a date to retrieve options data for any trading day in the past 15+ years (since 2008-01-01)_

[`https://www.alphavantage.co/query?**function** =HISTORICAL_OPTIONS&**ticker** =IBM&**date** =2017-11-15&**apikey** =demo`](https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&date=2017-11-15&apikey=demo)

[`https://www.alphavantage.co/query?**function** =HISTORICAL_OPTIONS&**ticker** =IBM&**date** =2017-11-15&**apikey** =demo&**format** =csv`](https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&date=2017-11-15&apikey=demo&format=csv)


💡 Tip: this is a premium API function. Subscribe to any of the [premium membership plans](https://www.alphavantage.co/premium/) to unlock historical options data.


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&ticker=IBM&apikey=demo";
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


#### Historical Put-Call Ratio


This API returns historical put-call ratios for both the entire option chain and for specific expiration dates. A lower put-call ratio (<=0.6) typically signals bullish sentiment, as investors are purchasing more call options in expectation of rising prices. On the other hand, a higher ratio (>=1.0) suggests bearish sentiment. However, because this metric is often used as a contrarian indicator, extreme values can imply the opposite - e.g., readings much higher than 1.0 may actually indicate a bullish outlook, while very low readings close to zero can point to potential bearish conditions.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=HISTORICAL_PUT_CALL_RATIO`

**❚ Required:`ticker`**

The name of the equity of your choice. For example: `ticker=IBM`

❚ Optional: `date`

By default, the `date` parameter is not set and the API will return data for the previous trading session. Any date later than 2008-01-01 is accepted. For example, `date=2026-03-12`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HISTORICAL_PUT_CALL_RATIO&**ticker** =IBM&**date** =2026-03-12&**apikey** =demo`](https://www.alphavantage.co/query?function=HISTORICAL_PUT_CALL_RATIO&ticker=IBM&date=2026-03-12&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HISTORICAL_PUT_CALL_RATIO&ticker=IBM&date=2026-03-12&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HISTORICAL_PUT_CALL_RATIO&ticker=IBM&date=2026-03-12&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HISTORICAL_PUT_CALL_RATIO&ticker=IBM&date=2026-03-12&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HISTORICAL_PUT_CALL_RATIO&ticker=IBM&date=2026-03-12&apikey=demo";
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


#### Historical Volume-to-Open-Interest Ratio


This API returns historical volume-to-open-interest ratios within an option chain. A high ratio (volume much larger than open interest) often suggests heavy trading activity relative to existing positions, which can indicate short-term speculation, increased liquidity, or possible trend changes. A low ratio (volume small compared to open interest) implies that most positions are being held rather than actively traded, signaling more stable or less volatile conditions. Traders use this ratio to understand whether price moves are driven by new participation (potentially stronger signals) or just minor adjustments within existing positions.


###### **API Parameters**

**❚ Required:`function`**

The time series of your choice. In this case, `function=HISTORICAL_VOLUME_OPEN_INTEREST_RATIO`

**❚ Required:`ticker`**

The name of the equity of your choice. For example: `ticker=NVDA`

❚ Optional: `date`

By default, the `date` parameter is not set and the API will return data for the previous trading session. Any date later than 2008-01-01 is accepted. For example, `date=2026-04-06`.

**❚ Required:`apikey`**

Your API key. Claim your free API key [here](https://www.alphavantage.co/support/#api-key).


###### **Examples (click for JSON output)**

[`https://www.alphavantage.co/query?**function** =HISTORICAL_VOLUME_OPEN_INTEREST_RATIO&**ticker** =NVDA&**date** =2026-04-06&**apikey** =demo`](https://www.alphavantage.co/query?function=HISTORICAL_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&date=2026-04-06&apikey=demo)


###### **Language-specific guides**

Python NodeJS PHP C#/.NET ✨MCP & Other


    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=HISTORICAL_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&date=2026-04-06&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)


    'use strict';
    var request = require('request');

    // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    var url = 'https://www.alphavantage.co/query?function=HISTORICAL_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&date=2026-04-06&apikey=demo';

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
    $json = file_get_contents('https://www.alphavantage.co/query?function=HISTORICAL_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&date=2026-04-06&apikey=demo');

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
                string QUERY_URL = "https://www.alphavantage.co/query?function=HISTORICAL_VOLUME_OPEN_INTEREST_RATIO&ticker=NVDA&date=2026-04-06&apikey=demo";
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