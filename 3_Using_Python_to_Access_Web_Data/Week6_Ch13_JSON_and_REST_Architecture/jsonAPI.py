# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson
# This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
# To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly
# URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py
# Just for fun, you can also test your program with the real Google API:
# http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=University+of+Michigan
# Singe Google's data is always changing, the data returned from the Google API could easily be different than from my local copy API.
# And the Google API has rate limits. But your code should work with the Google API with no modifications other than the base URL.

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'
	
	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ===='
		#print data
		continue
	
	#print json.dumps(js, indent=4)
	
	place_id = js["results"][0]["place_id"]
	print 'place_id', place_id