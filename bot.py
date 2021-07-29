import tweepy
import time

# Get these from the Developer Site
consumer_key = 'API KEY'
consumer_secret = 'API SECRET KEY'
key = 'ACCESS TOKEN'
secret = 'ACCESS SECRET TOKEN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# This updates the status
# api.update_status('Welcome to The Original Main Street! Tag #OriginalMainStreet for all of your Sauk Centre, MN adventures!')
# print("Status Updated")

# This is the file for storing the latest Tweet ID
FILE_NAME = 'last_seen.txt'

# This function Reads the last ID
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# This function stores that last seen ID
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# Hashtag to search for (must be commonly used)
hashtag = "SinclairLewis"
tweetNumber = 2

# This uses Tweepy to search using the api and then find that many Tweets
reTweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

# This iterates through the tweets and retweets them
def searchbot():
    for tweet in reTweets:
        try:
            tweet.retweet()
            print("Retweet Done")
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

def joke():
    url = "https://icanhazdadjoke.com"

    response = requests.get(url, headers={"Accept": "application/json"})

    return (response.json()["joke"])

def reply():
    # This brings in all tweets with mention and reads the FILE_NAME for last tweet
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')

    # This iterates through the tweets and checks for the Hashtag #testtweet - then stores the most current tweet ID in 'last_seen.txt'
    for tweet in reversed(tweets):
        if '#originalmainstreet' in tweet.full_text.lower():
            print("Replied to ID: " + str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Thanks for the Main Street Love!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
        elif '#tellmeajoke' in tweet.full_text.lower():
            print("Joke given to ID: " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " " + joke() + " \U0001F923 \U0001F923", tweet.id)
            api.create_favorite(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    searchbot()
    time.sleep(300)
    print("Working --- 5 more minutes...")
    time.sleep(300)