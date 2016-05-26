import urllib
import json

while True:
	location = raw_input("enter the location or quit: ")
	if len(location) < 1 :
		location = "University of Connecticut"
	elif location == "quit":
		break

	url = "http://maps.googleapis.com/maps/api/geocode/json?" + urllib.urlencode({"senor": "false", "address" : location})

	data = urllib.urlopen(url).read()

	try: 
		js = json.loads(str(data))
 	except: 
 		js = None
 	if 'status' not in js or js['status'] != 'OK':
 		print 'failed to get any data, try again'
 		continue

	print "place ID is ", js["results"][0]["place_id"]