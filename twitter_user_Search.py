# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:44:40 2017
@author: Kevin McGrath
Putpose: Use twitter api via TwitterSearch to access a given user's tweets
"""

from TwitterSearch import *
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

tweeter = "[your tweeter]"

tuo = TwitterUserOrder(tweeter)
userTweets = {}


ts = TwitterSearch(consumer_key = '[your consumer key]',\
                 consumer_secret = '[your consumer secret]',\
                 access_token = '[your access token]',\
                 access_token_secret = '[your access token secret]'\
        )

outfile = open('tweeterTimeline.txt', 'w')
outfile.write('Name\t\tTweets')
outfile.write('\n.........................................................')

for tweet in  ts.search_tweets_iterable(tso):
    outfile.write("\n" + tweet['created_at'] + ": (" + tweet['user']['name'] + ") " + tweet['text'].encode('utf8'))

outfile.close()

