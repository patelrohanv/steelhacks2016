import tweepy
from tweepy import OAuthHandler
import json


consumer_key = 'FKO8HPqgt7rJ0EYxQ5pGNYnOM'
consumer_secret = 'Nhv0BOtTvEub1RD8LA5Azk3uZW8qn5PCgpnyD2BnYkfQ0m5mGr'
access_token = '1979407176-HJlgun5ty2DHwkV7tG6ErQuMNIAHsp66Q6cR5sl'
access_secret = 'BU9a0YiJl9W4Xhj3H9Qg1Ypvu8Bn7NZCUTcRutr1FKJdH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
rate_limit = api.rate_limit_status();
user = api.get_user('guccimanesy')

out_file = open("testFILE.json","w")


def process_or_store(tweet):
    json.dump(tweet,out_file, indent=4)

#print user.screen_name
print(json.dumps(rate_limit, indent = 4))

#for status in tweepy.Cursor(api.home_timeline).items(10):
#Process a single status
#    print(status.text)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)


