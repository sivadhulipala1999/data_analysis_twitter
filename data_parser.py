# data:  https://www.kaggle.com/datasets/rsrishav/twitter-trending-tweets?resource=download

import os
import subprocess

import json
import csv

import uuid

from IPython.display import display_javascript, display_html, display

import pandas as pd
import numpy as np

from datetime import datetime, date, time

import snscrape.modules.twitter as sntwitter

out_folder = '/working'
in_folder = '/input'

json_filename = out_folder + '/pisa2018-query-tweets.json'

#Using the OS library to call CLI commands in Python
os.system(f'snscrape --max-results 500 --jsonl --progress --since 2019-12-01 twitter-search "#pisa2018 lang:fr until:2020-12-31" > {json_filename}')

start = date(2016, 12, 5)
start = start.strftime('%Y-%m-%d')

stop = date(2016, 12, 14)
stop = stop.strftime('%Y-%m-%d')

keyword = 'pisa2018'

maxTweets = 1000

#We are going to write the data into a csv file
filename = out_folder + '/' + keyword + start + '-' + stop + '.csv'
csvFile = open(filename, 'a', newline='', encoding='utf8')

#We write to the csv file by using csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id', 'date', 'tweet'])

#I will use the following Twitter search operators:
# since - start date for Tweets collection
# stop  - stop date for Tweets collection
# -filter:links - not very clear what this does, from Twitter search operators documentation: https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
#                 but it looks like this will exclude tweets with links from the search results
# -filter:replies - removes @reply tweets from search results
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + 'since:' + start + ' until:' + \
                                                        stop + ' -filter:links -filter:replies').get_items()):
    if i > maxTweets :
        break
    csvWriter.writerow([tweet.id, tweet.date, tweet.content])

csvFile.close()

filename = 'pisa2018-query-tweets'
file = in_folder + '/pisa2018-keyword-in-tweeter-archive/' + filename
tweets_df = pd.read_json(file + '.json', lines=True)

tweets_df.to_csv(out_folder + '/' + filename + '.csv', index=False)

