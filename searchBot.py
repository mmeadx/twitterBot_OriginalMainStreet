import tweepy
import time

consumer_key = 'API KEY'
consumer_secret = 'API SECRET KEY'
key = 'ACCESS TOKEN'
secret = 'ACCESS SECRET TOKEN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Hashtag to search for (must be commonly used)
hashtag = "SinclairLewis"
tweetNumber = 3

# This uses Tweepy to search using the api and then find that many Tweets
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

# This iterates through the tweets and retweets them
def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done")
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()