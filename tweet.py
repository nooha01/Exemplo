from os import link
import tweepy
import config
import json
from urllib.request import urlopen
client = tweepy.Client(
    consumer_key=config.api_key,
    consumer_secret=config.api_key_secrets,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
)

try:
    print("Authentication OK")
    url = "https://clist.by/api/v2/contest/?format=json&username=muhammed-mizaj&api_key=eec5f945658a9e7b937ff881dd102967eca28e0a"
    response = urlopen(url)
    data_json = json.loads(response.read())
    sample_data=data_json["objects"]
    data = sorted(sample_data, key=lambda k: k['start'], reverse=True)
    for i in range(0,15):
         t=data[i]
         link=t['href']
         start_date=t['start']
         end_date=t['end']
         msg=t['event']
         client.create_tweet(text="Hey there,\n"+str(msg)+" is happening from "+str(start_date)+" to "+str(end_date)+"! \Visit :"+str(link))

except Exception as error:
     print(error)