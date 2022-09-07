import tweepy
import configparser
import pandas as pd



config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#print(api_key)

auth =tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

search_words = "#bones"

tweets = tweepy.Cursor(api.search_tweets, q=search_words, tweet_mode='extended').items(5)
#tweets = api.search_tweets(search_words)

columns = ['time', 'Tweet']
data = []

for tweet in tweets:
#    text = tweet._json["full_text"]
    data.append([tweet.created_at, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
df.to_csv (r'/home/amal/Desktop/Twitter/export_dataframe.csv', index = False, header=True)


