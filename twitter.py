import tweepy
import time

auth = tweepy.OAuthHandler("API keys are a secret",
                           "Yes they are")
auth.set_access_token("Secret token",
                      "Top Secret")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '100DaysOfCode'
nrTweets = 1000
n = 38
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:

        tweet.favorite()
        tweet.retweet()
        n = n+1
        print('Tweet Liked', n)
        time.sleep(1)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
