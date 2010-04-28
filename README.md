#EC2 Analysis#
This python script is for analyzing Amazon EC2 Spot Instance market historical data.

The .json files are extracted from the EC2 management website.

##Current Status##
Currently, the EC2 analysis framework generates basic statistical information from Amazon's historical market pricing information.
* Minimum price
* Maximum price
* Mean (average) price
* Standard Deviation of price

These prices and statistics are created per-market, with a single market being defined as a specific instance type (e.g. m1.small) in a specific geographic location (VA, CA, or Ireland).

##Next Steps##
After loading all of the JSON historical data into a SQLite database, I intend to hook a python daemon up to Amazon's EC2 api, and begin continuously populating the pricing information.

I also want to be able to do time-of-day queries and other specific statistical regressions on the data set.


###Amazon JSON structure###

    {"requests":
		{"describeSpotHistory":"36df7f6c-58f6-4079-816a-475b5a08080b"},
		"priceChange":[
		
			{"instanceType":"m1.small",
				"productDescription":"Linux/UNIX",
				"spotPrice":0.029,
				"timestamp":"2010-04-17T06:11:24.000Z",
				"epochtime":1271484684000},
		
			{"instanceType":"m1.small"
			,"productDescription":"Linux/UNIX",
			"spotPrice":0.031,
			"timestamp":"2010-04-17T04:52:45.000Z",
			"epochtime":1271479965000}
		]
	}

###SQLite Table schema:###
	CREATE TABLE pricehistory (
		location TEXT,
		instanceType TEXT,
		spotPrice DECIMAL,
		timestamp TEXT )
	
