import tweepy
import configparser
import pandas as pd
from flask import *


config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


auth =tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getinput', methods=['POST', 'GET'])
def getinput():
    search_words = request.form['search_word']
    count = request.form['count']
    dname = request.form['dname']
    data(search_words, dname, count)
    return render_template('index.html')

@app.route('/data', methods=['POST', 'GET'])
def data(search_words, dname, count):
    no_of_tweets= int(count)

    columns = ['time', 'Tweet']
    data = []
    tweets = tweepy.Cursor(api.search_tweets, q=search_words,lang="en").items(no_of_tweets)
    for tweet in tweets:

        data.append([tweet.created_at, tweet.text])

        df = pd.DataFrame(data, columns=columns)
        df.to_csv (r'/home/amal/Desktop/Twitter/{}.csv'.format(dname), index = False, header=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()





