#!usr/bin/python3
'''collect data from twitter using tweepy API.
to use api,Remember,we need:
-consumer key
-consumer secret
-acces token
-acces token secret

for this you  will reviw your developer acount in twitter. 
'''
#pip install tweepy

#import local  libraries
import pandas as pd
import numpy as np
import json

#import external libraries
import tweepy

#import concrete modules
from tweepy import OAuthHandler

#define variables for authentication
consumer_key="your consumerkey"
consumer_secret="your..."
access_token="your..."
accces_token_secret="your..."

#calling API
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_acces_token(acces_token,acces_token_secret)
api =tweepy.API(auth)

#provide the query you want to pull the data for retrieve tweets.

query="internet of things"

tweets = api.search(query,count=10,lang='en',exclude='retweets')
