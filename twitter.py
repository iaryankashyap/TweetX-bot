import tweepy
import time

auth = tweepy.OAuthHandler("nBzN5fIGo7eIac2dXzxEkmJTf",
                           "QyRJWpA7sUwpXa3sMteB5RGXzHi6zEAdIHVUQAVeSOTTmnzEGH")
auth.set_access_token("1272918562403782661-HgpnGSh9kVARsqozKdFI3sjZ4Ozd8o",
                      "6zJNJanh4Y0SS8ffKjIJm28SShwu6J0ZqAUU5zYyGHDdq")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '100DaysOfCode'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
