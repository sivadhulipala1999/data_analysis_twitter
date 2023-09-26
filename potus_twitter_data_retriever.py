import tweepy

 # - API key
 # - API key secret
 # - access token
 # - access token secret

consumer_key = "PsYVXzKDhQZXFaUX0dejGKatI"
consumer_secret = "oM81IPCBuiajBCvlenFXA7O9azeBaMyXusElKI9f9hHWNWZdTy"
access_token = "1549360442644267008-Yx6xAI26fWYYQBnwkR29pb27vTtzZJ"
access_token_secret = "1HI9o8iPPAHOWqSkpwxSym2s4IOgVDgnHX2zpo4tDJI9u"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

twitterAPI = tweepy.API(auth)

# Get 200 tweets every time and add it onto the list (200 max tweets per request). Keep looping until there's no more to fetch.
username = "POTUS"
tweets = []
fetchedTweets = twitterAPI.user_timeline(screen_name=username, count=20)
tweets.extend(fetchedTweets)
lastTweetInList = tweets[-1].id - 1

while len(fetchedTweets) > 0:
        fetchedTweets = twitterAPI.user_timeline(screen_name=username, count=20, max_id=lastTweetInList)
        tweets.extend(fetchedTweets)
        lastTweetInList = tweets[-1].id - 1
        print(f"Fetched {len(tweets)} tweets so far.")

print(tweets)
