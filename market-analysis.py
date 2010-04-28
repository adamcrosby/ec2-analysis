#!/usr/bin/env python
import json, math

guiddict = {
	"b398aace-c81c-4442-bd71-1fe9baa57257": "CA m1.small",
	"993fa3fd-a527-474e-8c82-cf1e2fa474cb": "CA c1.medium",
	"bed6b804-9631-44f7-aaf8-2e899810f86f": "CA m1.large",
	"1d6ce0f8-25b2-49f3-a8a0-c63f7a3d073a": "CA m1.xlarge",
	"3348ecef-c985-4d25-80b9-078cd9f7fa49": "CA m2.xlarge",
	"0c64cb77-cacd-41e6-9971-5e5b647eb812": "CA m2.2xlarge",
	"e4ca9224-3e0a-49bd-902b-2d0a7dc485fb": "CA m2.4xlarge",
	"18afcf29-2acc-4704-bbef-10d98a04de6c": "CA c1.xlarge",
	"a5f52738-8cf4-4a58-96cc-a9c21e8e8f18": "EU m1.small",
	"406f27ee-6cd8-49dc-988c-6c084778f6a6": "EU c1.medium",
	"a6469205-bf41-4c22-a940-91efb51093d3": "EU m1.large",
	"bf2b045f-7832-455f-a20d-77ccf92a59fc": "EU m1.xlarge",
	"ba501899-e828-4d77-ac68-b2c2d755dd73": "EU m2.xlarge",
	"c30d5a21-cab1-42f0-b6f8-1179418bf7cb": "EU m2.2xlarge",
	"daa8ae39-6046-489e-8ec1-3fbac50a0ac7": "EU m2.4xlarge",
	"de852146-0bf8-48dd-b6bf-54a06d8f2fde": "EU c1.xlarge",
	"36df7f6c-58f6-4079-816a-475b5a08080b": "VA m1.small",
	"12e7fbda-8aff-4fa2-a22d-9172d63c2473": "VA c1.medium",
	"9c3cf92d-f3af-4fec-86a1-19e4c8e4b8c3": "VA m1.large",
	"e2bfa455-c73f-4a36-b948-93907bd1d538": "VA m1.xlarge",
	"19fded0f-8a07-44c6-9112-6a2915aced4a": "VA m2.xlarge",
	"81a46287-ba6e-45fe-8ad6-b6c554e01753": "VA m2.2xlarge",
	"76d94bf3-abe8-413c-a22f-a5a49b4ece75": "VA m2.4xlarge",
	"88fe17f7-6e01-4b7c-ac87-211f2790c164": "VA c1.xlarge"
}

def populationStdDev(prices):	
	squares = []
	mean = math.fsum(prices)/len(prices)
	for item in prices:
		# Std deviation requires the squares of all of the differences of items in the population from the mean
		squares.append((item-mean)**2)
	# Standard deviation for an entire population is the square root of the sum of the squares over the number of items in the population
	stddev = math.sqrt(math.fsum(squares)/len(squares))
	return stddev
	
	
# open market history file
markethistory = open("ec2-spotmarket-total.json")		

#each line in the file is a separate market history, and a separate json "document"
marketdata = []
for jsondb in markethistory:
	data = json.loads(jsondb)
	marketdata.append(data)

marketinfo = [] # each item will be: {"name":"", "guid":"", "entries":"", "stddev":"", "mean":""}

for market in marketdata:
	prices = []

	for spotPrice in market['priceChange']:
		pricedata.append((spotPrice['spotPrice'], spotPrice['timestamp']))
		prices.append(spotPrice['spotPrice'])
	info = {"name": guiddict[market['requests']['describeSpotHistory']], 
		"guid": 	market['requests']['describeSpotHistory'], 
		"entries": 	len(market['priceChange']), 
		"minprice":	min(prices),
		"maxprice":	max(prices),
		"stddev":	populationStdDev(prices), 
		"mean": math.fsum(prices)/len(prices)}
	marketinfo.append(info)	

for market in marketinfo:
#	print "Market name: %s (%s entries)" % (market['name'], market['entries'])
#	print "\tMin: %s\tMax: %s\tAvg: %s" % (market['minprice'], market['maxprice'], market['mean'])
#	print "\tStd Deviation: %s" % (market['stddev'])
#	print "-----------------------------------------"
	print "\"%s\",%s,%s,%s,%s,%s" % (market['name'], market['entries'], market['minprice'], market['maxprice'], market['mean'], market['stddev'])




""""{"requests":
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
"""		
