from flask import Flask, flash, request, redirect, render_template
import tweepy
import time

global n
global m

m = 0
n = 0

app = Flask(__name__)


def retlike():
    global n
    global m
    auth = tweepy.OAuthHandler("nBzN5fIGo7eIac2dXzxEkmJTf",
                               "QyRJWpA7sUwpXa3sMteB5RGXzHi6zEAdIHVUQAVeSOTTmnzEGH")
    auth.set_access_token("1272918562403782661-HgpnGSh9kVARsqozKdFI3sjZ4Ozd8o",
                          "6zJNJanh4Y0SS8ffKjIJm28SShwu6J0ZqAUU5zYyGHDdq")

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    user = api.me()

    search = '100DaysOfCode'
    nrTweets = 1
    for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
        try:

            tweet.favorite()
            tweet.retweet()
            n = n+1
            print('Tweet Liked', n)
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
            m = m+1

        except StopIteration:
            break


@app.route("/")
def hometweet():
    return render_template("dashboard-notactive.html", retweets=n, fails=m)


@app.route("/activate")
def acti():
    t = render_template("dashboard-active.html", retweets=n, fails=m)
    for i in range(1000):
        retlike()
    return render_template("dashboard-active.html", retweets=n, fails=m)

if __name__ == "__main__":
    app.run(debug=True)
