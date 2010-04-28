&copy; 2010 Adam Crosby
http://www.uptill3.com/

This python script is for analyzing Amazon EC2 Spot Instance market historical data.

The .json files are extracted from the EC2 management website.

TODO:
Generate query per 'time period', to see if certain periods of time are 'hotspots' (ie: noon in EST, vs. noon in PST)

TODO:
Hook into amazon ec2 api query (http://developer.amazonwebservices.com/connect/thread.jspa?threadID=45305):
			Yes, you can do so using the DescribeSpotPriceHistory API ( http://docs.amazonwebservices.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSpotPriceHistory.html). 

			You can also query this data using the EC2 API tools ( http://developer.amazonwebservices.com/connect/entry.jspa?categoryID=88&externalID=351).  

			For example, to pull recent prices for m1.small instances, you can do something like this: 

			$ ec2-describe-spot-price-history -t m1.small -s 2010-04-17T22:00:00 
			SPOTINSTANCEPRICE    0.058    2010-04-17T05:14:33-0800    m1.small    Windows 
			SPOTINSTANCEPRICE    0.029    2010-04-17T19:35:50-0800    m1.small    Linux/UNIX
			
			
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
	]}

###SQLite Table schema:###
	CREATE TABLE pricehistory (
		location TEXT,
		instanceType TEXT,
		spotPrice DECIMAL,
		timestamp TEXT )
	
