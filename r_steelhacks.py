import geopy as geopy
from tweepy import OAuthHandler
from tweepy import Cursor
import json
from geopy.geocoders import Nominatim
import geojson
from geojson import Point
from geopy.exc import GeocoderTimedOut


'''
consumer_key = 'FKO8HPqgt7rJ0EYxQ5pGNYnOM'
consumer_secret = 'Nhv0BOtTvEub1RD8LA5Azk3uZW8qn5PCgpnyD2BnYkfQ0m5mGr'
access_token = '1979407176-HJlgun5ty2DHwkV7tG6ErQuMNIAHsp66Q6cR5sl'
access_secret = 'BU9a0YiJl9W4Xhj3H9Qg1Ypvu8Bn7NZCUTcRutr1FKJdH'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q="#sick", count=15, result_type="recent", include_entities=True, lang="en").items():
    print (json.dumps(tweet))
'''
#open file
locs = open('stream_flu_more_data.txt', 'r')
#empty list for cities
cities = []

#load cities into list
for line in locs:
        cities.append(line)

#close file
locs.close()

#from the interwebs
geolocator = Nominatim()

#coordinates list
coor = [] 

w = open('geo_data.json', 'w')

#load geocode into coordinates
for c in cities:
    location = geolocator.geocode(c)
    try:
	    point = Point((location.longitude, location.latitude))
	    print(point)
	    coor.append(point)
    except AttributeError, GeocoderTimedOut:
    	pass


for c in coor:
    w.write(str(c))


w.close()
